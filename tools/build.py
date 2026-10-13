"""모든 문제의 정답을 sympy로 다시 계산해 확인한 뒤 assets/problems.js 와 assets/mock-problems.js 를 만든다.

사용법 (저장소 루트에서):
    pip install sympy mpmath
    python3 tools/build.py            # 전체 검산 + 생성 (단계당 120문제 확인)
    python3 tools/build.py --partial  # 작업 중: 아직 120문제가 안 된 단계는 개수 확인을 건너뜀
"""
import importlib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bank_lib  # noqa: E402
import mock  # noqa: E402
from bank_lib import PROBLEMS, CHAPTERS, SECTIONS, TYPES, LEVELS  # noqa: E402

PARTIAL = "--partial" in sys.argv
# 단계마다 원래 30문제(levelN.py) + 추가 90문제(levelN_c1213 / _c14 / _c15 / _c16)
MODULES = [f"level{lv}{part}" for lv in (1, 2, 3, 4) for part in ("", "_c1213", "_c14", "_c15", "_c16")]
for _name in MODULES:
    try:
        importlib.import_module(_name)
    except ModuleNotFoundError as _e:
        if not (PARTIAL and _e.name == _name):
            raise

OUT = os.path.join(HERE, "..", "assets", "problems.js")
MOCK_OUT = os.path.join(HERE, "..", "assets", "mock-problems.js")
PER_LEVEL = 120
EXPECTED_PER_CHAPTER = {12: 8, 13: 6, 14: 46, 15: 36, 16: 24}


def fix_html(text):
    """수식 안의 '<' 가 HTML 태그로 해석되지 않도록 \\lt 로 바꾼다 (<br> 은 유지)."""
    text = re.sub(r"<(?!br>|/?b>|/?i>)", r"\\lt ", text)
    return text


def space_text(text):
    """수식 밖에서 연속 공백(문항 (a)/(b) 구분 등)을 &emsp; 로 바꿔 HTML에서도 간격이 보이게 한다."""
    parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", text, flags=re.S)
    return "".join(seg if seg.startswith("$") else re.sub(r" {2,}", "&emsp;", seg) for seg in parts)


def bank_html(text):
    """문제 은행 문자열: 행렬·cases 의 '&' 가 HTML 에서 깨지지 않게 &amp; 로, '<' 는 \\lt 로."""
    return space_text(fix_html(text.replace("&", "&amp;")))


def check_dollars(pid, field, text):
    body = text.replace("$$", "")
    if body.count("$") % 2:
        raise SystemExit(f"[{pid}] {field}: $ 짝이 맞지 않음")


def main():
    failed = []
    for p in PROBLEMS:
        try:
            p["check"]()
        except Exception as e:  # noqa: BLE001
            failed.append((p["id"], repr(e)))
    if failed:
        for pid, err in failed:
            print("FAIL", pid, err)
        raise SystemExit(f"{len(failed)}개 문제의 정답 확인 실패")

    ids = [p["id"] for p in PROBLEMS]
    assert len(ids) == len(set(ids)), "중복 id"
    for lv in (1, 2, 3, 4):
        items = [p for p in PROBLEMS if p["lv"] == lv]
        if PARTIAL and len(items) != PER_LEVEL:
            print(f"  (작업 중) {lv}단계 {len(items)}문제 — 개수 확인 건너뜀")
            continue
        assert len(items) == PER_LEVEL, f"{lv}단계 문제 수 {len(items)}"
        cnt = Counter(p["ch"] for p in items)
        assert dict(cnt) == EXPECTED_PER_CHAPTER, f"{lv}단계 단원 분배 {dict(cnt)}"
        nums = sorted(int(p["id"].split("-")[1]) for p in items)
        assert nums == list(range(1, PER_LEVEL + 1)), f"{lv}단계 번호 누락"
    unused = [k for k in TYPES if not any(p["type"] == k for p in PROBLEMS)]
    if unused and not PARTIAL:
        raise SystemExit(f"문제가 없는 유형: {unused}")

    out = []
    for p in sorted(PROBLEMS, key=lambda q: (q["lv"], int(q["id"].split("-")[1]))):
        item = {k: p[k] for k in ("id", "lv", "ch", "sec", "type", "src", "q", "hint", "ans", "sol")}
        for f in ("q", "hint", "ans"):
            check_dollars(p["id"], f, item[f])
            item[f] = bank_html(item[f])
        for i, line in enumerate(item["sol"]):
            check_dollars(p["id"], f"sol[{i}]", line)
        item["sol"] = [bank_html(line) for line in item["sol"]]
        out.append(item)

    data = {
        "chapters": {str(k): v for k, v in CHAPTERS.items()},
        "sections": SECTIONS,
        "types": TYPES,
        "levels": {str(k): v for k, v in LEVELS.items()},
        "problems": out,
    }
    js = ("/* 자동 생성 파일 — tools/build.py 로 다시 만드세요. 직접 고치면 다음 빌드 때 덮어써져요. */\n"
          "window.CM_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(js)
    print(f"정답 확인 {len(PROBLEMS)}문제 모두 통과 · 유형 {len(TYPES)}개 · {os.path.relpath(OUT)} 작성")
    build_mock()


def glue_math(text, max_math=20, max_tail=6):
    """인라인 수식 바로 뒤에 붙은 문장부호·조사('$\\frac12$.' '$P$에서')가 줄바꿈으로 다음 줄
    맨 앞에 떨어지지 않게 한다. 짧은 수식은 뒤 글자와 함께 <span class="nw"> 로 묶고, 긴 수식은
    (수식 안에서 줄이 바뀌어야 휴대폰 화면에 들어가므로) 뒤의 문장부호만 수식 끝에 \\text{} 로 넣는다."""
    parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", text, flags=re.S)
    out = []
    for i, seg in enumerate(parts):
        if not seg:
            continue
        if seg.startswith("$") and not seg.startswith("$$") and i + 1 < len(parts):
            nxt = parts[i + 1]
            if len(seg) <= max_math:
                tail = re.match(r"[^\s$<&]+", nxt)
                if tail and len(tail.group(0)) <= max_tail:
                    out.append('<span class="nw">' + seg + tail.group(0) + "</span>")
                    parts[i + 1] = nxt[tail.end():]
                    continue
            else:
                punct = re.match(r"[.,:;)]+", nxt)
                if punct:
                    out.append(seg[:-1] + "\\text{" + punct.group(0) + "}$")
                    parts[i + 1] = nxt[punct.end():]
                    continue
        out.append(seg)
    return "".join(out)


def mock_html(pid, field, text):
    """예상 모의고사 문자열: aligned 의 '&' 가 HTML 에서 깨지지 않게 &amp; 로, '<' 는 \\lt 로."""
    check_dollars(pid, field, text)
    return glue_math(space_text(fix_html(text.replace("&", "&amp;"))))


def build_mock():
    results = mock.check_all()
    bad = [r for r in results if not r[1]]
    if bad:
        for name, _, got, want in bad:
            print("FAIL mock", name, "| got", got, "| want", want)
        raise SystemExit(f"예상 모의고사 {len(bad)}개 항목 정답 확인 실패")

    def conv(q):
        pid = q["id"]
        return {
            "id": pid, "no": q["no"], "type": q["type"], "ref": q["ref"],
            "stem": mock_html(pid, "stem", q["stem"]),
            "parts": [[lab, mock_html(pid, f"part {lab}", txt)] for lab, txt in q["parts"]],
            "answer": [[lab, mock_html(pid, f"answer {lab}", txt)] for lab, txt in q["answer"]],
            "solution": [[lab, [mock_html(pid, f"sol {lab}", st) for st in steps]] for lab, steps in q["solution"]],
        }

    exam, extra = [conv(q) for q in mock.EXAM], [conv(q) for q in mock.EXTRA]
    ids = [q["id"] for q in exam + extra]
    assert len(ids) == len(set(ids)), "예상 모의고사 id 중복"
    assert len(exam) == 10, f"예상 문제 수 {len(exam)}"
    data = {
        "exam": exam,
        "extra": extra,
        "map": [{"no": no, "what": mock_html("map", no, what), "sec": sec, "mine": mine, "here": here, "href": href}
                for no, what, sec, mine, here, href in mock.MAP_MID],
    }
    assert all(row["href"] in ids for row in data["map"]), "비교표 링크가 없는 문항을 가리킴"
    js = ("/* 자동 생성 파일 — tools/mock.py 를 고친 뒤 tools/build.py 로 다시 만드세요. */\n"
          "window.CM_MOCK = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
    with open(MOCK_OUT, "w", encoding="utf-8") as fh:
        fh.write(js)
    print(f"예상 모의고사 검산 {len(results)}개 모두 통과 · {len(exam)}+{len(extra)}문항 · {os.path.relpath(MOCK_OUT)} 작성")


if __name__ == "__main__":
    main()

"""모든 문제의 정답을 sympy로 다시 계산해 확인한 뒤 assets/problems.js 를 만든다.

사용법 (저장소 루트에서):
    pip install sympy
    python3 tools/build.py
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bank_lib  # noqa: E402
import level1, level2, level3, level4  # noqa: E402,F401
from bank_lib import PROBLEMS, CHAPTERS, SECTIONS, TYPES, LEVELS  # noqa: E402

OUT = os.path.join(HERE, "..", "assets", "problems.js")
EXPECTED_PER_CHAPTER = {12: 6, 13: 4, 14: 9, 15: 6, 16: 5}


def fix_html(text):
    """수식 안의 '<' 가 HTML 태그로 해석되지 않도록 \\lt 로 바꾼다 (<br> 은 유지)."""
    text = re.sub(r"<(?!br>|/?b>|/?i>)", r"\\lt ", text)
    return text


def space_text(text):
    """수식 밖에서 연속 공백(문항 (a)/(b) 구분 등)을 &emsp; 로 바꿔 HTML에서도 간격이 보이게 한다."""
    parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", text, flags=re.S)
    return "".join(seg if seg.startswith("$") else re.sub(r" {2,}", "&emsp;", seg) for seg in parts)


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
        assert len(items) == 30, f"{lv}단계 문제 수 {len(items)}"
        cnt = Counter(p["ch"] for p in items)
        assert dict(cnt) == EXPECTED_PER_CHAPTER, f"{lv}단계 단원 분배 {dict(cnt)}"
        nums = sorted(int(p["id"].split("-")[1]) for p in items)
        assert nums == list(range(1, 31)), f"{lv}단계 번호 누락"
    unused = [k for k in TYPES if not any(p["type"] == k for p in PROBLEMS)]
    assert not unused, f"문제가 없는 유형: {unused}"

    out = []
    for p in sorted(PROBLEMS, key=lambda q: (q["lv"], int(q["id"].split("-")[1]))):
        item = {k: p[k] for k in ("id", "lv", "ch", "sec", "type", "src", "q", "hint", "ans", "sol")}
        for f in ("q", "hint", "ans"):
            check_dollars(p["id"], f, item[f])
            item[f] = space_text(fix_html(item[f]))
        for i, line in enumerate(item["sol"]):
            check_dollars(p["id"], f"sol[{i}]", line)
        item["sol"] = [space_text(fix_html(line)) for line in item["sol"]]
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


if __name__ == "__main__":
    main()

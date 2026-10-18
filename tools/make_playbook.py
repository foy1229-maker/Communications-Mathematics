# -*- coding: utf-8 -*-
"""풀이 행동강령 페이지 만들기: tools/playbook_content.py → playbook.html (+ assets/playbook-map.js, 마크다운).

사용법 (저장소 루트에서, tools/build.py 로 assets/problems.js · mock-problems.js 를 만든 뒤):
    python3 tools/make_playbook.py              # playbook.html, assets/playbook-map.js 생성
    python3 tools/make_playbook.py --md 파일.md  # 같은 내용을 마크다운으로도 저장 (인쇄·공유용)

확인하는 것: 카드 id 중복, 문제 은행 유형 키·문제 번호(예: 3-97)·모의고사 문항(예: C4(b))이 실제로 있는지,
수식 구분자 $ 짝, 카드에 적은 모의고사 문항이 그 유형을 다루는 문항과 맞는지(빠진 것은 경고로 알려 줌).
"""
import html
import json
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

import playbook_content as C  # noqa: E402

SETS = "ABCDE"
KEEP = ("<b>", "</b>", "<i>", "</i>", "<br>")


def load_js(name):
    with open(os.path.join(ROOT, "assets", name), encoding="utf-8") as f:
        s = f.read()
    return json.loads(s[s.index("{"): s.rindex("}") + 1])


BANK = load_js("problems.js")
MOCK = load_js("mock-problems.js")
PROBS = {p["id"]: p for p in BANK["problems"]}
TYPES = BANK["types"]
MOCK_TYPES = {}          # 'A5' -> {'15-cyl', ...}
for si, s in enumerate(MOCK["sets"]):
    for p in s["problems"]:
        MOCK_TYPES[SETS[si] + str(p["no"])] = {t[0] for t in p["types"]}

ERRORS = []
WARN = []


# ───────────────────────────── 문자열 ─────────────────────────────
def check_math(where, s):
    n = len(re.findall(r"(?<!\\)\$", s))
    if n % 2:
        ERRORS.append(f"{where}: '$' 개수가 홀수예요 → {s[:60]}")


def tx(s, where="?"):
    """내용 문자열 → HTML. <b>·<i>·<br> 만 태그로 두고 나머지(수식 속 < > & 포함)는 이스케이프."""
    check_math(where, s)
    out = html.escape(s, quote=False)
    for t in KEEP:
        out = out.replace(html.escape(t, quote=False), t)
    return out


def md(s):
    """내용 문자열 → 마크다운 (굵게만 바꾸고 나머지 태그는 지움)."""
    s = s.replace("<b>", "**").replace("</b>", "**").replace("<i>", "*").replace("</i>", "*").replace("<br>", " ")
    return s


def attr(s):
    return html.escape(s, quote=True)


# ───────────────────────────── 링크 ─────────────────────────────
MOCK_RE = re.compile(r"^([A-E])(\d{1,2})(.*)$")


def mock_ref(ref, where):
    m = MOCK_RE.match(ref)
    if not m or (m.group(1) + m.group(2)) not in MOCK_TYPES:
        ERRORS.append(f"{where}: 모의고사 문항 '{ref}' 을(를) 찾을 수 없어요")
        return None
    si = SETS.index(m.group(1)) + 1
    return f"mock.html?set={si}#q{int(m.group(2))}", m.group(1) + m.group(2)


def bank_ref(pid, where):
    p = PROBS.get(pid)
    if not p:
        ERRORS.append(f"{where}: 문제 은행 '{pid}' 이(가) 없어요")
        return None
    return f"bank.html?level={p['lv']}#p{pid}"


def ref_links(refs, where):
    """['3-97', 'C4(b)', ...] → <a> 목록 HTML"""
    out = []
    for r in refs:
        if re.match(r"^\d-\d{2,3}$", r):
            href = bank_ref(r, where)
            if href:
                p = PROBS[r]
                out.append(f'<a href="{href}" title="문제 은행 {p["lv"]}단계 · {attr(TYPES.get(p["type"], ""))}">{r}</a>')
        else:
            got = mock_ref(r, where)
            if got:
                out.append(f'<a class="mk" href="{got[0]}" title="모의고사 {r[0]}세트 {got[1][1:]}번">모의 {attr(r)}</a>')
    return "".join(out)


def practice(types, where):
    """유형 키 → 단계별 연습 링크 (data-ids 로 맞은 수를 JS 가 채움)"""
    parts = []
    total = 0
    for key in types:
        if key not in TYPES:
            ERRORS.append(f"{where}: 유형 키 '{key}' 이(가) 문제 은행에 없어요")
            continue
        ps = [p for p in BANK["problems"] if p["type"] == key]
        total += len(ps)
        links = []
        for lv in (1, 2, 3, 4):
            items = [p["id"] for p in ps if p["lv"] == lv]
            if not items:
                continue
            links.append(f'<a href="bank.html?level={lv}&amp;type={key}" data-ids="{" ".join(items)}" '
                         f'title="{lv}단계에서 \'{attr(TYPES[key])}\' {len(items)}문제만 보기">{lv}단계 <span>{len(items)}</span></a>')
        if links:
            name = f'<span class="pt-n">{html.escape(TYPES[key])}</span>' if len(types) > 1 else ""
            parts.append(f'<span class="pt">{name}{"".join(links)}</span>')
    if not parts:
        return ""
    return f'<div class="practice pb-practice"><span class="lbl">연습 {total}문제</span>{"".join(parts)}</div>'


# ───────────────────────────── 카드 ─────────────────────────────
class Counter:
    def __init__(self):
        self.items = 0
        self.steps = 0
        self.checks = 0
        self.cases = 0
        self.cards = 0


CNT = Counter()


def ck_item(item_id):
    CNT.items += 1
    return f' data-item="{item_id}"'


def steps_html(cid, steps):
    groups = []          # [(제목, [항목...])]
    for s in steps:
        if s.startswith("## "):
            groups.append((s[3:], []))
        else:
            if not groups:
                groups.append((None, []))
            groups[-1][1].append(s)
    out = []
    n = 0
    for title, items in groups:
        lis = []
        for s in items:
            n += 1
            CNT.steps += 1
            lis.append(f'<li{ck_item(f"{cid}.s{n}")}><span class="tx">{tx(s, cid)}</span></li>')
        start = n - len(items) + 1
        head = f'<p class="pb-grp">{tx(title, cid)}</p>' if title else ""
        st = f' start="{start}"' if start != 1 else ""
        out.append(f'<div class="pb-g">{head}<ol{st}>{"".join(lis)}</ol></div>')
    return "".join(out)


def checks_html(cid, checks):
    lis = []
    for i, s in enumerate(checks, 1):
        CNT.checks += 1
        lis.append(f'<li{ck_item(f"{cid}.c{i}")}><span class="tx">{tx(s, cid)}</span></li>')
    return f'<ul class="pb-ul">{"".join(lis)}</ul>'


def table_html(cid, t, idx=1):
    head = "".join(f"<th>{tx(h, cid)}</th>" for h in t["head"])
    rows = "".join("<tr>" + "".join(f"<td>{tx(c, cid)}</td>" for c in r) + "</tr>" for r in t["rows"])
    cap = t.get("caption") or ""
    return (f'<div class="pb-table"{ck_item(f"{cid}.t{idx}")}>'
            f'<p class="pb-cap"><span class="tx">{tx(cap, cid) if cap else "표로 정리"}</span></p>'
            f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></div>')


def cases_html(cid, cases):
    lis = []
    for i, c in enumerate(cases, 1):
        CNT.cases += 1
        sit, act = c[0], c[1]
        refs = c[2] if len(c) > 2 else []
        links = ref_links(refs, cid)
        lis.append(f'<li{ck_item(f"{cid}.k{i}")}><span class="tx"><span class="if">{tx(sit, cid)}</span>'
                   f'<span class="then">{tx(act, cid)}</span>'
                   f'{f"<span class=refs>{links}</span>" if links else ""}</span></li>')
    return f'<ul class="pb-cases">{"".join(lis)}</ul>'


def auto_mock(types):
    """그 유형을 다루는 모의고사 문항 (mock-problems.js 기준)"""
    return sorted((k for k, ts in MOCK_TYPES.items() if ts & set(types)), key=lambda k: (k[0], int(k[1:])))


def card_html(card, seen):
    cid = card["id"]
    if cid in seen:
        ERRORS.append(f"카드 id 중복: {cid}")
    seen.add(cid)
    CNT.cards += 1
    out_tag = '<span class="out-tag">수업 자료 밖</span>' if card.get("outside") else ""
    parts = [f'<article class="pb-card" id="{cid}" data-card>',
             f'<header class="pb-h"><h3>{tx(card["title"], cid)}{out_tag}</h3>'
             f'<span class="pb-cnt" aria-live="polite"></span><span class="sec-tag">{tx(card["sec"], cid)}</span></header>']
    if card.get("when"):
        parts.append(f'<p class="pb-when"><span class="lbl">이런 문제</span><span>{tx(card["when"], cid)}</span></p>')
    cols = [f'<div class="pb-col"><h4>행동강령</h4>{steps_html(cid, card["steps"])}</div>']
    if card.get("checks"):
        cols.append(f'<div class="pb-col pb-chk"><h4>세부 체크</h4>{checks_html(cid, card["checks"])}</div>')
    parts.append(f'<div class="pb-cols">{"".join(cols)}</div>')
    tables = card.get("tables") or ([card["table"]] if card.get("table") else [])
    for i, t in enumerate(tables, 1):
        parts.append(table_html(cid, t, i))
    if card.get("cases"):
        parts.append(f'<div class="pb-sit"><h4>이럴 땐 이렇게 <small>문제 은행·모의고사에서 나온 상황</small></h4>{cases_html(cid, card["cases"])}</div>')
    foot = []
    if card.get("types"):
        foot.append(practice(card["types"], cid))
        # 모의고사 문항 확인: 적어 둔 문항 vs 유형으로 찾은 문항
        listed = []
        for r in card.get("mock", []):
            m = MOCK_RE.match(r)
            if m:
                listed.append(m.group(1) + m.group(2))
        missing = [k for k in auto_mock(card["types"]) if k not in listed]
        if missing and not card.get("mock_skip"):
            WARN.append(f"{cid}: 이 유형을 다루는 모의고사 문항 중 카드에 없는 것 {missing}")
    if card.get("mock"):
        links = ref_links(card["mock"], cid)
        foot.append(f'<div class="similar pb-mock"><span class="lbl">모의고사</span>{links}</div>')
    if foot:
        parts.append(f'<footer class="pb-foot">{"".join(foot)}</footer>')
    parts.append('<p class="pb-donemsg">이 카드의 항목은 모두 내 강령에 있어요.</p>')
    parts.append(memo_html(cid, "내 강령에만 있는 것, 헷갈렸던 것", "예: 경계가 원이면 매개화보다 라그랑주가 빨랐음"))
    parts.append("</article>")
    return "".join(parts)


def memo_html(cid, hint, placeholder=""):
    ph = f' placeholder="{attr(placeholder)}"' if placeholder else ""
    return (f'<div class="pb-memo"><label for="m-{cid}">내 메모 <small>{hint}</small></label>'
            f'<textarea id="m-{cid}" data-memo="{cid}" rows="2"{ph}></textarea>'
            f'<p class="pb-memo-print" aria-hidden="true"></p></div>')


def signals_html():
    t = C.SIGNALS
    rows = []
    for i, r in enumerate(t["rows"], 1):
        sig, act, target = r
        rows.append(f'<tr{ck_item(f"sig.{i}")}><td><span class="tx">{tx(sig, "sig")}</span></td>'
                    f'<td>{tx(act, "sig")}</td><td class="c"><a href="#{target}">카드 →</a></td></tr>')
    head = "".join(f"<th>{h}</th>" for h in t["head"])
    return (f'<div class="pb-signal"><div class="tw"><table><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div></div>')


def common_html():
    c = C.COMMON
    cid = c["id"]
    return (f'<article class="pb-card pb-common" id="{cid}" data-card>'
            f'<header class="pb-h"><h3>{tx(c["title"], cid)}</h3><span class="pb-cnt" aria-live="polite"></span>'
            f'<span class="sec-tag">{c["sec"]}</span></header>'
            f'<div class="pb-cols"><div class="pb-col"><h4>문제를 받으면</h4>{steps_html(cid, c["steps"])}</div>'
            f'<div class="pb-col pb-chk"><h4>답안 쓰기</h4>{checks_html(cid, c["checks"])}</div></div>'
            f'<p class="pb-donemsg">이 카드의 항목은 모두 내 강령에 있어요.</p>'
            f'{memo_html(cid, "내 강령에만 있는 것")}</article>')


def unit_html(u, seen):
    cards = "".join(card_html(c, seen) for c in u["cards"])
    mini = "".join(f'<a href="#{c["id"]}">{tx(c.get("short") or c["title"], c["id"])}</a>' for c in u["cards"])
    return (f'<section class="sec pb-unit" id="{u["id"]}" aria-labelledby="h-{u["id"]}">'
            f'<div class="sec-h"><p class="k">{u["k"]}</p><h2 id="h-{u["id"]}">{tx(u["title"], u["id"])}</h2>'
            f'<p>{tx(u["lead"], u["id"])}</p></div>'
            f'<nav class="pb-mini" aria-label="{attr(u["title"])} 유형">{mini}</nav>'
            f'{cards}</section>')


TOC_N = {"u12": "12", "u13": "13", "u14a": "14.1–3", "u14b": "14.4–6", "u14c": "14.7–8",
         "u15a": "15.1–3", "u15b": "15.6–8", "u15c": "15.9", "u16": "16"}
TOC = [("p-start", None, "공통·신호")] + [(u["id"], TOC_N.get(u["id"], u["k"]), u.get("toc") or u["title"]) for u in C.UNITS]


def page_html():
    seen = set()
    common = common_html()
    signals = signals_html()
    units = "".join(unit_html(u, seen) for u in C.UNITS)
    toc = "".join(
        f'<a href="#{i}">{f"<span class=n>{n}</span>" if n else ""}{tx(t, "toc")}</a>' for i, n, t in TOC)
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>풀이 행동강령 · 기초통신수학 II</title>
  <meta name="description" content="기초통신수학 II 중간고사 범위 Ch.12~16.4 유형별 풀이 행동강령 {CNT.cards}가지 — 단계별 행동, 세부 체크(적분 범위·변수변환·경계 임계점), 문제 은행·모의고사 상황별 대처. 내 강령과 비교 체크">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/img/favicon-16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <link rel="stylesheet" href="assets/site.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
  <script defer src="assets/common.js"></script>
  <script defer src="assets/playbook.js"></script>
</head>
<!-- 자동 생성 파일 — tools/playbook_content.py 를 고친 뒤 python3 tools/make_playbook.py 로 다시 만드세요. -->
<body class="pb-page">
  <header class="top wrap">
    <a class="brand" href="index.html">
      <img src="assets/img/ku-emblem.webp" alt="" width="164" height="220">
      <span><b>기초통신수학 II</b>중간고사 문제 은행</span>
    </a>
    <nav class="top-links" aria-label="페이지">
      <a href="concepts.html">개념 정리</a>
      <a href="index.html">대시보드</a>
    </nav>
  </header>

  <section class="hero wrap">
    <p class="eyebrow ko">시험 범위 Ch.12 – 16.4 · 유형별</p>
    <h1>풀이 행동강령</h1>
    <p class="lead">문제를 보고 <b>무엇부터, 어떤 순서로</b> 할지 유형마다 정리했어요. 적분 범위 잡기, 변환을 안 줬을 때 고르는 법, 경계에서 임계점 찾기처럼 놓치기 쉬운 세부 체크와, 문제 은행·모의고사에 실제로 나온 상황별 대처까지 담았어요.</p>
    <div class="facts">
      <span><b>{CNT.cards}</b>개 유형 카드</span>
      <span><b>{CNT.steps}</b>개 행동</span>
      <span><b>{CNT.checks}</b>개 세부 체크</span>
      <span><b>{CNT.cases}</b>개 상황별 대처</span>
    </div>
  </section>

  <section class="wrap pb-panel" aria-labelledby="h-compare">
    <div class="pb-panel-in">
      <div class="pb-panel-tx">
        <h2 id="h-compare">내 행동강령과 비교하기</h2>
        <p><b>비교 모드</b>를 켜면 항목마다 체크 칸이 생겨요. 내 강령에도 있는 항목을 체크하고 <b>빠진 것만 보기</b>를 누르면 내 강령에 없는 항목만 남아요. 카드 아래 <b>내 메모</b>에는 내 강령에만 있는 것을 적어 두세요. 체크와 메모는 이 브라우저에만 저장돼요.</p>
      </div>
      <div class="pb-panel-act">
        <button class="btn" type="button" id="pb-mode" aria-pressed="false">비교 모드 켜기</button>
        <button class="chip" type="button" data-act="missing" aria-pressed="false" disabled>빠진 것만 보기</button>
        <span class="pb-total" aria-live="polite"><b data-total-have>0</b> / <span data-total-all>{CNT.items}</span> 체크</span>
        <span class="tools">
          <button class="tool" type="button" id="pb-reset" disabled>체크·메모 지우기</button>
          <button class="tool" type="button" id="pb-print">인쇄</button>
        </span>
      </div>
    </div>
  </section>

  <nav class="toc" aria-label="단원 목차">
    <div class="wrap">{toc}</div>
  </nav>

  <main class="wrap">
    <section class="sec pb-unit" id="p-start" aria-labelledby="h-start">
      <div class="sec-h">
        <p class="k">시험장</p>
        <h2 id="h-start">공통 행동강령과 첫 행동</h2>
        <p>어느 단원이든 같은 순서로 시작해요. 문제에서 아래 신호가 보이면 첫 행동이 정해져요 — 오른쪽 링크로 그 유형 카드로 가요.</p>
      </div>
      {common}
      <h3 class="sub">신호 → 첫 행동</h3>
      {signals}
    </section>
    {units}
    <nav class="next" aria-label="다음으로">
      <a href="concepts.html" class="ghost">← 개념 정리</a>
      <a href="mock.html">모의고사로 확인하기 →</a>
    </nav>
  </main>

  <div class="pb-float" hidden>
    <span class="pb-total"><b data-total-have>0</b> / {CNT.items}</span>
    <button class="chip" type="button" data-act="missing" aria-pressed="false">빠진 것만</button>
    <button class="chip" type="button" data-act="off">비교 끄기</button>
  </div>

  <footer class="foot">수업 자료(강의 예제·복습문제·과제)와 이 사이트의 문제 은행 492문제 · 모의고사 50문항을 보고 정리한 개인 학습용 자료예요.<br>
    <a href="index.html">대시보드</a> · <a href="concepts.html">개념 정리</a> · <a href="bank.html?level=1">문제 은행</a> · <a href="mock.html">모의고사</a></footer>
  <noscript><p>체크·메모 기능과 수식 표시는 JavaScript가 필요해요.</p></noscript>
</body>
</html>
'''


# ───────────────────────────── 마크다운 ─────────────────────────────
def md_table(t):
    lines = ["| " + " | ".join(md(h) for h in t["head"]) + " |", "|" + "---|" * len(t["head"])]
    for r in t["rows"]:
        lines.append("| " + " | ".join(md(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(lines)


def md_steps(steps):
    out = []
    n = 0
    for s in steps:
        if s.startswith("## "):
            out.append(f"\n*{md(s[3:])}*\n")
        else:
            n += 1
            out.append(f"{n}. {md(s)}")
    return "\n".join(out)


def md_card(c):
    lines = [f"### {md(c['title'])} ({c['sec']})" + (" — 수업 자료 밖" if c.get("outside") else "")]
    if c.get("when"):
        lines.append(f"**이런 문제:** {md(c['when'])}\n")
    lines.append("**행동강령**\n")
    lines.append(md_steps(c["steps"]))
    if c.get("checks"):
        lines.append("\n**세부 체크**\n")
        lines += [f"- {md(s)}" for s in c["checks"]]
    for t in (c.get("tables") or ([c["table"]] if c.get("table") else [])):
        lines.append("")
        lines.append(md_table(t))
    if c.get("cases"):
        lines.append("\n**이럴 땐 이렇게**\n")
        for k in c["cases"]:
            refs = f" `{', '.join(k[2])}`" if len(k) > 2 and k[2] else ""
            lines.append(f"- {md(k[0])} → {md(k[1])}{refs}")
    if c.get("mock"):
        lines.append(f"\n모의고사: {', '.join(c['mock'])}")
    return "\n".join(lines)


def page_md():
    out = ["# 기통수2 풀이 행동강령 (중간고사 Ch.12–16.4)",
           "",
           "유형마다 '무엇부터 어떤 순서로' 할지, 세부 체크, 문제 은행·모의고사에 나온 상황별 대처를 정리했어요. "
           "문제 번호(예: `3-97`)는 사이트 문제 은행(3단계 97번), `C4`는 모의고사 C세트 4번이에요. "
           "사이트: https://foy1229-maker.github.io/Communications-Mathematics/playbook.html",
           "",
           "## 공통 행동강령", "",
           md_steps(C.COMMON["steps"]), "",
           *[f"- {md(s)}" for s in C.COMMON["checks"]], "",
           "### 신호 → 첫 행동", "",
           md_table({"head": C.SIGNALS["head"][:2], "rows": [r[:2] for r in C.SIGNALS["rows"]]}), ""]
    for u in C.UNITS:
        out.append(f"## {u['k']} {md(u['title'])}\n")
        out.append(md(u["lead"]) + "\n")
        for c in u["cards"]:
            out.append(md_card(c))
            out.append("")
    return "\n".join(out)


def main():
    page = page_html()
    # 신호 표의 카드 링크 확인
    ids = {c["id"] for u in C.UNITS for c in u["cards"]} | {C.COMMON["id"]}
    for r in C.SIGNALS["rows"]:
        if r[2] not in ids:
            ERRORS.append(f"신호 표: 카드 '{r[2]}' 이(가) 없어요")
    if ERRORS:
        print("오류:\n  " + "\n  ".join(ERRORS))
        sys.exit(1)
    with open(os.path.join(ROOT, "playbook.html"), "w", encoding="utf-8") as f:
        f.write(page)
    # 개념 정리 페이지에서 유형 → 행동강령 카드로 가는 링크용
    tmap = OrderedDict()
    for u in C.UNITS:
        for c in u["cards"]:
            for t in c.get("types", []):
                tmap.setdefault(t, c["id"])
    missing_types = [k for k in TYPES if k not in tmap]
    if missing_types:
        WARN.append(f"행동강령 카드가 없는 유형: {missing_types}")
    with open(os.path.join(ROOT, "assets", "playbook-map.js"), "w", encoding="utf-8") as f:
        f.write("/* 자동 생성 파일 — tools/make_playbook.py.\n"
                "   types: 문제 은행 유형 키 → 행동강령 카드 id (개념 정리의 '행동강령' 링크), total: 비교 체크 항목 수 (대시보드) */\n")
        data = OrderedDict([("total", CNT.items), ("cards", CNT.cards), ("types", tmap)])
        f.write("window.CM_PLAYBOOK = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
    if "--md" in sys.argv:
        path = sys.argv[sys.argv.index("--md") + 1]
        with open(path, "w", encoding="utf-8") as f:
            f.write(page_md())
        print("마크다운:", path)
    for w in WARN:
        print("참고:", w)
    print(f"playbook.html: 카드 {CNT.cards} · 행동 {CNT.steps} · 체크 {CNT.checks} · 상황 {CNT.cases} · 체크 항목 {CNT.items}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""모의고사 세트를 인쇄용 A4 PDF 로 만들어요 — 시험지(문항당 한 쪽, 풀이 공간 · 답란) + 정답 및 풀이(빠른 정답표 포함).

사용법 (저장소 루트에서):
    python3 tools/print_sets.py --sets c d e --out print/
    python3 tools/print_sets.py --sets a b c d e --out print/ --katex /path/to/katex/dist

- 세트 데이터는 tools/mock_sets.py 의 SETS (id: a b c d e).
- 수식은 KaTeX(0.16.11)로 그려요. --katex 로 dist 폴더를 주면 그걸 쓰고, 없으면 jsDelivr CDN 에서 불러와요.
- Playwright(Chromium)와 한글 글꼴(Noto Sans CJK KR)이 필요해요.
- 결과: '기통수2 모의고사 {X}세트 시험지.pdf', '기통수2 모의고사 {X}세트 정답풀이.pdf'
"""
import argparse
import html
import os
import pathlib
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mock_sets  # noqa: E402

COURSE = "2026학년도 2학기 · 기초통신수학 II (미적분학 2) · 중간고사 대비"
CDN = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"
RULES = "· 계산기 사용 불가. &nbsp;· 풀이 과정을 반드시 쓰시오(답만 쓰면 감점). &nbsp;· 각 문항의 풀이는 해당 쪽 빈칸에 작성하시오."

CSS = r"""
@page { size: A4; margin: 16mm; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Noto Sans CJK KR", "Noto Sans KR", "Apple SD Gothic Neo", sans-serif; color: #111;
       font-size: 10.4pt; line-height: 1.55; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.katex { font-size: 1.12em; }
b, strong { font-weight: 700; }

/* 머리말 상자 */
.headbox { display: flex; border: 1.4px solid #111; }
.headbox .ttl { flex: 1; padding: 4.2mm 5mm 3.6mm; }
.headbox .course { font-size: 9.5pt; color: #222; }
.headbox h1 { margin: 1.2mm 0 1.4mm; font-size: 17pt; font-weight: 800; letter-spacing: -.2px; line-height: 1.25; }
.headbox .sub { font-size: 9.5pt; color: #222; }
.headbox table { border-collapse: collapse; width: 63mm; flex: none; }
.headbox td { border-left: 1px solid #111; border-top: 1px solid #111; padding: 0 3.4mm; font-size: 10pt; }
.headbox tr:first-child td { border-top: none; }
.headbox td.k { width: 16.5mm; background: #f2f2f2; text-align: center; }
.headbox td.val { text-align: right; }

/* 시험지 */
.page { height: 265mm; display: flex; flex-direction: column; page-break-after: always; break-after: page; overflow: hidden; }
.page:last-child { page-break-after: auto; break-after: auto; }
.rules { margin: 5mm 0 0; font-size: 9pt; color: #222; }
.score { width: 100%; border-collapse: collapse; margin: 5.4mm 0 0; table-layout: fixed; }
.score th, .score td { border: 1px solid #111; text-align: center; }
.score th { background: #f2f2f2; font-size: 10pt; font-weight: 700; height: 7.8mm; }
.score td { font-size: 8pt; color: #666; height: 8.8mm; }
.score col.sum { width: 22.5mm; }
.qhead { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1.2px solid #111;
         padding-bottom: 1.6mm; margin-top: 6.4mm; }
.page.later .qhead { margin-top: 0; }
.qhead .no { font-size: 16pt; font-weight: 800; line-height: 1.1; }
.qhead .pts { font-size: 10pt; font-weight: 700; }
.stem { margin: 3.2mm 0 0; padding-bottom: 2.6mm; border-bottom: 1px dashed #aaa; }
.parts { flex: 1; display: flex; flex-direction: column; min-height: 0; }
.part { display: flex; flex-direction: column; border-bottom: 1px dashed #aaa; padding: 2.2mm 0 2mm; min-height: 0; }
.part:last-child { border-bottom: none; }
.prow { display: flex; align-items: flex-start; gap: 3mm; }
.prow .lab { font-weight: 700; flex: none; width: 6.5mm; }
.prow .txt { flex: 1; }
.prow .p { flex: none; font-size: 9.5pt; color: #333; padding-left: 2mm; }
.ansline { margin-top: auto; margin-left: auto; width: 39.5%; border-top: 1.1px solid #111; padding-top: .6mm;
           font-size: 8.5pt; color: #333; }
.foot { text-align: center; font-size: 8.5pt; color: #555; padding-top: 3mm; }

/* 정답 및 풀이 */
.sol-page { padding: 0; }
.qa-title { font-size: 13pt; font-weight: 800; margin: 6.5mm 0 0; padding-bottom: 1.6mm; border-bottom: 1.4px solid #111; }
.qa { width: 100%; border-collapse: collapse; margin-top: 2.2mm; }
.qa th { width: 12mm; background: #f2f2f2; border: 1px solid #111; vertical-align: top; padding: 2.2mm 0; font-size: 10pt; }
.qa td { border: 1px solid #111; padding: 1.1mm 3.2mm; }
.qa .line { padding: .2mm 0; line-height: 1.52; }
.qa .katex { font-size: 1.2em; }
.qa-wrap { break-after: page; page-break-after: always; }
.sol { margin-top: 0; }
.sol + .sol { margin-top: 7mm; }
.sol h3 { margin: 0 0 3mm; padding-bottom: 1.6mm; border-bottom: 1.2px solid #111; font-size: 9.5pt; font-weight: 400; color: #333;
          break-after: avoid; page-break-after: avoid; }
.sol h3 .no { font-size: 14pt; font-weight: 800; color: #111; margin-right: 2.4mm; }
.ph { margin: 3.6mm 0 1.6mm; break-after: avoid; page-break-after: avoid; }
.ph b { font-size: 11pt; }
.ph .pts { font-size: 9pt; color: #555; margin-left: 1mm; }
.ansbox { background: #f2f2f2; border-left: 4px solid #222; padding: 2.4mm 4mm; margin: 0 0 2.4mm;
          break-inside: avoid; page-break-inside: avoid; }
.steps { margin: 0; padding-left: 6mm; }
.steps li { margin: .9mm 0; break-inside: avoid; page-break-inside: avoid; }
.steps .katex-display { margin: 1.4mm 0; }
"""


KEEP_TAGS = ("<br>", "<b>", "</b>", "<i>", "</i>")


def text_html(s):
    """글자 이스케이프(KaTeX 가 나중에 원래 글자로 읽어요). <br> <b> <i> 태그는 그대로 두고 **굵게** 는 <b> 로."""
    for k, tag in enumerate(KEEP_TAGS):
        s = s.replace(tag, f"\x00{k}\x00")
    s = html.escape(s, quote=False)
    for k, tag in enumerate(KEEP_TAGS):
        s = s.replace(f"\x00{k}\x00", tag)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def compact(tex):
    """빠른 정답표용: 큰 분수·적분 기호(\\dfrac, \\displaystyle)를 글자 크기로 줄여 줄 간격이 겹치지 않게 해요."""
    return tex.replace("\\dfrac", "\\frac").replace("\\displaystyle", "")


def split_points(txt):
    """'… 구하시오. [4점] $$…$$' → (문장, 4, 뒤에 오는 표시 수식·정의 문장)"""
    m = re.search(r"\s*\[(\d+)점\]\s*", txt)
    if not m:
        return txt, None, ""
    return txt[:m.start()], int(m.group(1)), txt[m.end():]


def head_box(title, sub, rows):
    cells = "".join(f'<tr><td class="k">{k}</td><td class="val">{v}</td></tr>' for k, v in rows)
    return (f'<div class="headbox"><div class="ttl"><div class="course">{COURSE}</div>'
            f'<h1>{html.escape(title)}</h1><div class="sub">{sub}</div></div><table>{cells}</table></div>')


def doc(title, body, katex):
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<link rel="stylesheet" href="{katex}/katex.min.css"><style>{CSS}</style></head><body>{body}
<script src="{katex}/katex.min.js"></script><script src="{katex}/contrib/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}],
                                       throwOnError: false, strict: 'ignore'}});
  window.__mathDone = true;
</script></body></html>"""


def exam_html(S):
    label, probs = S["label"], S["problems"]
    mins = sum(q["mins"] for q in probs)
    pages = []
    for i, q in enumerate(probs):
        top = ""
        if i == 0:
            top = (head_box(f"모의고사 {label}세트", f"{len(probs)}문항 · 100점 만점 · 권장 시간 {mins}분",
                            [("학번", ""), ("이름", ""), ("점수", "/ 100")])
                   + f'<p class="rules">{RULES}</p>'
                   + '<table class="score"><colgroup>' + "<col>" * len(probs) + '<col class="sum"></colgroup><tr>'
                   + "".join(f"<th>{n}</th>" for n in range(1, len(probs) + 1)) + "<th>합계</th></tr><tr>"
                   + "<td>/10</td>" * len(probs) + "<td>/100</td></tr></table>")
        parts = []
        for lab, txt in q["parts"]:
            before, pts, after = split_points(txt)
            body = text_html(before) + (" " + text_html(after) if after else "")
            parts.append(f'<div class="part" style="flex:{pts} 1 0"><div class="prow"><span class="lab">({lab})</span>'
                         f'<span class="txt">{body}</span><span class="p">[{pts}점]</span></div>'
                         f'<div class="ansline">답</div></div>')
        pages.append(f'<section class="page{"" if i == 0 else " later"}">{top}'
                     f'<div class="qhead"><span class="no">{q["no"]}.</span><span class="pts">[10점]</span></div>'
                     f'<div class="stem">{text_html(q["stem"])}</div><div class="parts">{"".join(parts)}</div>'
                     f'<div class="foot">{label}세트 · {i + 1} / {len(probs)}</div></section>')
    return "".join(pages)


def sol_html(S):
    label, probs = S["label"], S["problems"]
    rows = []
    for q in probs:
        lines = "".join(f'<div class="line"><b>({lab})</b> {text_html(compact(a))}</div>' for lab, a in q["answer"])
        rows.append(f'<tr><th>{q["no"]}</th><td>{lines}</td></tr>')
    out = [f'<div class="qa-wrap">'
           + head_box(f"모의고사 {label}세트 — 정답 및 풀이", "15개 주제 · 10문항 · 각 10점", [("채점", ""), ("점수", "/ 100")])
           + f'<h2 class="qa-title">빠른 정답표</h2><table class="qa">{"".join(rows)}</table></div>']
    for q in probs:
        blocks = [f'<h3><span class="no">{q["no"]}.</span>{html.escape(q["type"])} · 교재 {html.escape(q["ref"])}</h3>']
        ans = dict(q["answer"])
        for lab, txt in q["parts"]:
            _, pts, _ = split_points(txt)
            steps = dict(q["solution"])[lab]
            blocks.append(f'<div class="ph"><b>({lab})</b><span class="pts">[{pts}점]</span></div>'
                          f'<div class="ansbox">답: {text_html(ans[lab])}</div>'
                          '<ul class="steps">' + "".join(f"<li>{text_html(st)}</li>" for st in steps) + "</ul>")
        out.append(f'<section class="sol">{"".join(blocks)}</section>')
    return "".join(out)


def render(sets, out_dir, katex):
    from playwright.sync_api import sync_playwright
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for S in sets:
            for kind, title, body in (("시험지", f"모의고사 {S['label']}세트 시험지", exam_html(S)),
                                      ("정답풀이", f"모의고사 {S['label']}세트 정답 및 풀이", sol_html(S))):
                src = out_dir / f".{S['id']}-{kind}.html"
                src.write_text(doc(title, body, katex), encoding="utf-8")
                page.goto(src.resolve().as_uri(), wait_until="load")
                page.wait_for_function("window.__mathDone === true")
                page.evaluate("document.fonts.ready")
                errs = page.evaluate("document.querySelectorAll('.katex-error').length")
                if errs:
                    raise SystemExit(f"{title}: KaTeX 오류 {errs}개")
                if kind == "시험지":
                    over = page.evaluate("""Array.from(document.querySelectorAll('.page')).filter(pg => {
                        const parts = pg.querySelector('.parts'); return parts.scrollHeight > parts.clientHeight + 1; }).length""")
                    if over:
                        raise SystemExit(f"{title}: 한 쪽에 다 들어가지 않는 문항 {over}개")
                pdf = out_dir / f"기통수2 모의고사 {S['label']}세트 {kind}.pdf"
                page.pdf(path=str(pdf), print_background=True, prefer_css_page_size=True)
                src.unlink()
                made.append(pdf)
        browser.close()
    return made


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sets", nargs="+", default=[S["id"] for S in mock_sets.SETS], help="세트 id (a b c d e)")
    ap.add_argument("--out", default=os.path.join(HERE, "..", "print"), help="PDF 를 저장할 폴더")
    ap.add_argument("--katex", default=None, help="KaTeX dist 폴더 (없으면 CDN)")
    args = ap.parse_args()
    by_id = {S["id"]: S for S in mock_sets.SETS}
    unknown = [i for i in args.sets if i not in by_id]
    if unknown:
        raise SystemExit(f"모르는 세트 id: {unknown} (있는 id: {list(by_id)})")
    katex = pathlib.Path(args.katex).resolve().as_uri() if args.katex else CDN
    for pdf in render([by_id[i] for i in args.sets], args.out, katex):
        print("작성:", pdf)


if __name__ == "__main__":
    main()

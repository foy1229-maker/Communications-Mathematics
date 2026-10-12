# Communications-Mathematics

기통수2 중간고사 문제은행 — 고려대학교 차세대통신학과 **기초통신수학 II (미적분학)** 중간고사 대비 사이트예요.
시험 범위 **Ch.12 벡터 ~ 16.4 그린 정리**의 개념 정리 한 페이지와 1~4단계 문제 은행(단계당 30문제, 총 120문제)으로 구성돼요.

사이트 주소 (GitHub Pages): https://foy1229-maker.github.io/Communications-Mathematics/

## 페이지

| 파일 | 내용 |
|---|---|
| `index.html` | 대시보드 — 카드 5장 (개념 정리 + 1·2·3·4단계), 단계별 진행률 표시 |
| `concepts.html` | 강의 단위 8개(12 / 13 / 14.1–3 / 14.4–6 / 14.7–8 / 15.1–3 / 15.6–8 / 16.1–4)의 핵심 공식, 출제 유형 52가지와 풀이 순서, 자주 하는 실수. 유형마다 연습 문제로 바로 가는 링크 |
| `bank.html?level=1` ~ `4` | 단계별 문제 은행. 문제마다 힌트·정답·풀이, 단원/풀이 상태 필터, 맞음·다시 풀기 기록(브라우저에 저장) |

| 단계 | 성격 | 단원별 문항 수 |
|---|---|---|
| 1단계 · 기본 | 공식 바로 적용 | Ch.12 6 · 13 4 · 14 9 · 15 6 · 16 5 |
| 2단계 · 표준 | 강의 예제·과제 유형 (숫자만 바꾼 유사 문항) | 같음 |
| 3단계 · 응용 | 각 장 복습문제(연습) 유형 | 같음 |
| 4단계 · 심화 | 복습문제(심화)·실전형 고난도 | 같음 |

모든 정답은 계산기 없이 손으로 구할 수 있는 정확한 값(분수·근호·π·e·ln)이에요.

## 배포

GitHub Pages가 꺼져 있다면 한 번만 켜 주세요: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
빌드 도구가 필요 없는 정적 사이트라 merge하면 바로 반영돼요. (`.nojekyll` 포함)

## 문제 수정·추가

문제 원본은 `tools/level1.py` ~ `tools/level4.py`에 있고, 문제마다 sympy로 정답을 다시 계산하는 `check`가 붙어 있어요.

```bash
pip install sympy
python3 tools/build.py   # 120문제 정답 확인 → assets/problems.js 생성
```

`assets/problems.js`는 자동 생성 파일이라 직접 고치지 말고 `tools/` 쪽을 고친 뒤 다시 빌드하세요.
`build.py`는 단계당 30문제, 단원별 문항 수, 모든 출제 유형에 문제가 1개 이상 있는지도 함께 확인해요.

## 구성

```
index.html          대시보드
concepts.html       개념 정리 · 출제 유형
bank.html           문제 은행 (?level=1..4)
assets/
  site.css          개념·문제 은행 공통 스타일
  common.js         수식 렌더링(KaTeX), 풀이 기록 저장
  bank.js           문제 은행 화면
  concepts.js       유형별 연습 문제 링크, 목차 표시
  problems.js       문제 데이터 (자동 생성)
  img/              고려대 엠블럼, 본관 배경 사진
tools/              문제 원본과 정답 검증·빌드 스크립트
```

수식은 KaTeX, 글꼴은 Pretendard를 jsDelivr CDN에서 불러와요.
수업 자료의 강의 예제·복습문제·과제 유형을 바탕으로 새로 만든 개인 학습용 문제예요.

"""문제 은행 공통 정의: 단원·소단원·출제 유형·단계 메타데이터와 문제 등록/검증 도우미.

각 문제는 P(...)로 등록하고, check 함수에서 sympy로 정답을 다시 계산해 확인한다.
build.py가 모든 check를 실행한 뒤 assets/problems.js 를 만든다.
"""
from sympy import (Matrix, Rational as R, sqrt, pi, E, exp, log, sin, cos, tan, asin, acos, atan2,
                   integrate, diff, simplify, symbols, limit, solve, N, sympify, oo, Function, expand, factor)

x, y, z, t, s, r, u, v, w = symbols('x y z t s r u v w', real=True)
th, ph, rho = symbols('theta phi rho', real=True)

CHAPTERS = {
    12: {"name": "벡터와 공간기하", "range": "12.1–12.5"},
    13: {"name": "벡터함수", "range": "13.1–13.3"},
    14: {"name": "편도함수", "range": "14.1–14.8"},
    15: {"name": "중적분", "range": "15.1–15.3 · 15.6–15.9"},
    16: {"name": "벡터 미적분", "range": "16.1–16.4"},
}

SECTIONS = {
    "12.1": "3차원 좌표계", "12.2": "벡터", "12.3": "내적", "12.4": "외적", "12.5": "직선과 평면",
    "13.1": "벡터함수와 공간곡선", "13.2": "벡터함수의 미분·적분", "13.3": "호의 길이",
    "14.1": "다변수함수", "14.2": "극한과 연속", "14.3": "편도함수", "14.4": "접평면·선형근사",
    "14.5": "연쇄법칙", "14.6": "방향도함수·기울기", "14.7": "최댓값·최솟값", "14.8": "라그랑주 승수",
    "15.1": "직사각형 영역 이중적분", "15.2": "일반 영역 이중적분", "15.3": "극좌표 이중적분",
    "15.6": "삼중적분", "15.7": "원주좌표 삼중적분", "15.8": "구면좌표 삼중적분", "15.9": "변수변환",
    "16.1": "벡터장", "16.2": "선적분", "16.3": "선적분의 기본정리", "16.4": "그린 정리",
}

# 출제 유형 (개념 페이지의 data-type 과 같은 키)
TYPES = {
    "12-sphere": "구의 방정식·등거리 집합",
    "12-vec": "벡터 연산·단위벡터·일차결합",
    "12-dot": "내적·사잇각·방향코사인",
    "12-proj": "정사영과 일",
    "12-cross": "외적·넓이·수직 벡터",
    "12-triple": "스칼라 삼중적·부피·공면",
    "12-line": "직선의 방정식·두 직선의 위치",
    "12-plane": "평면의 방정식·사잇각·교선",
    "12-dist": "거리 공식",
    "12-identity": "내적·외적 관계식",
    "13-func": "정의역·극한·연속",
    "13-curve": "교선의 매개화",
    "13-deriv": "도함수·단위접선·접선",
    "13-integ": "벡터함수의 적분",
    "13-motion": "속도·속력·가속도",
    "13-arc": "호의 길이",
    "13-arcfn": "호의 길이 함수·재매개화",
    "13-tplane": "두 곡선으로 접평면",
    "14-domain": "정의역·치역·등위곡선",
    "14-limit": "극한 계산·존재 보이기",
    "14-dne": "극한이 존재하지 않음",
    "14-partial": "편도함수·변화율",
    "14-implicit": "음함수 편미분",
    "14-higher": "고계 편도함수·라플라스",
    "14-defpartial": "연속성 판정·정의로 구하는 편도함수",
    "14-tangent": "접평면·선형근사",
    "14-diff": "전미분·오차 추정",
    "14-differentiable": "미분가능성의 정의 (ε₁·ε₂)",
    "14-chain": "연쇄법칙",
    "14-chain2": "2계 연쇄법칙",
    "14-dir": "방향도함수",
    "14-maxrate": "최대 변화율과 방향",
    "14-levelsurf": "등위곡면의 접평면·법선",
    "14-crit": "임계점·2계 판정법",
    "14-absext": "닫힌 영역의 최댓값·최솟값",
    "14-optim": "최적화 응용",
    "14-lagrange": "라그랑주 승수",
    "14-lagrange2": "제약조건 2개 라그랑주",
    "15-rect": "직사각형 영역·리만합",
    "15-general": "일반 영역(Type I/II)·부피",
    "15-order": "적분 순서 바꾸기",
    "15-polar": "극좌표 이중적분·넓이",
    "15-mass": "질량·질량중심",
    "15-triple": "직교좌표 삼중적분·부피",
    "15-order3": "삼중적분 순서 바꾸기",
    "15-cyl": "원주좌표",
    "15-sph": "구면좌표 삼중적분",
    "15-sphconv": "구면좌표로 바꾸어 쓰기",
    "15-change": "변수변환·야코비안",
    "16-field": "벡터장·기울기장",
    "16-scalar": "스칼라 선적분 ∫f ds",
    "16-vector": "벡터 선적분·일",
    "16-conserv": "보존장 판정·퍼텐셜",
    "16-ftli": "선적분의 기본정리",
    "16-green": "그린 정리",
    "16-greenarea": "그린 정리로 넓이",
    "16-singular": "특이점이 있는 벡터장",
}

LEVELS = {
    1: {"name": "기본", "eyebrow": "LEVEL 1 · BASIC", "title": "1단계 · 기본",
        "focus": "공식 바로 적용",
        "lead": "정의와 공식을 그대로 대입하면 풀리는 문제예요. 편도함수·그래디언트·방향도함수, 극좌표·원주·구면좌표 적분, 선적분과 그린 정리처럼 시험에서 절대 놓치면 안 되는 계산을 14~16장 위주로 손에 익혀요."},
    2: {"name": "표준", "eyebrow": "LEVEL 2 · STANDARD", "title": "2단계 · 표준",
        "focus": "강의 예제·과제 유형",
        "lead": "강의 예제와 과제 문항을 숫자만 바꾼 유사 문제예요. 두 경로로 극한 판정, 연쇄법칙, 등위곡면의 접평면, 극값 판정, 적분 순서 바꾸기, 퍼텐셜 함수처럼 시험에 그대로 나올 수 있는 유형이에요."},
    3: {"name": "응용", "eyebrow": "LEVEL 3 · APPLIED", "title": "3단계 · 응용",
        "focus": "복습문제·기출 유형",
        "lead": "각 장 복습문제와 기출(2022·2024·2025 미적분학 II) 수준의 여러 단계 문제예요. 조임정리·곡선 경로 극한, 음함수와 선형근사, 정의로 판정하는 미분가능성, 닫힌 영역의 최대·최소, 적분식 변환, u·v 변수변환, 구면좌표, 곡선을 닫아서 쓰는 그린 정리까지 연결해요."},
    4: {"name": "심화", "eyebrow": "LEVEL 4 · ADVANCED", "title": "4단계 · 심화",
        "focus": "기출 실전형·심화",
        "lead": "기출 실전형과 복습문제(심화) 수준의 고난도 문제예요. 2계 연쇄법칙, 주어진 정보로 그래디언트 복원, 미분가능성의 정의와 반례, 제약조건 2개 라그랑주, 질량중심, 비선형 변수변환, 구면좌표 변환, 원점을 감는 벡터장처럼 개념 두세 개를 엮어야 풀려요. 막히면 힌트 → 정답 → 풀이 순서로 열어 보세요."},
}


PROBLEMS = []


def P(**kw):
    required = ["id", "ch", "sec", "type", "src", "q", "hint", "ans", "sol", "check"]
    for k in required:
        assert k in kw, f"{kw.get('id')} missing {k}"
    assert kw["type"] in TYPES, f"{kw['id']}: unknown type {kw['type']}"
    assert kw["sec"] in SECTIONS, f"{kw['id']}: unknown sec {kw['sec']}"
    assert str(kw["ch"]) == kw["sec"].split(".")[0], f"{kw['id']}: chapter/section mismatch"
    kw["lv"] = int(kw["id"].split("-")[0])
    PROBLEMS.append(kw)


def EQ(a, b, tol=1e-12):
    """sympy 식/행렬/리스트가 같은지 (기호적으로, 안 되면 수치적으로) 확인"""
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(EQ(p, q, tol) for p, q in zip(a, b))
    if hasattr(a, "shape"):
        return a.shape == Matrix(b).shape and all(EQ(p, q, tol) for p, q in zip(list(a), list(Matrix(b))))
    d = sympify(a) - sympify(b)
    try:
        if simplify(d) == 0:
            return True
    except Exception:
        pass
    try:
        return abs(complex(N(d, 40))) < tol
    except Exception:
        return False


def grad(f, vars_):
    return Matrix([diff(f, q) for q in vars_])

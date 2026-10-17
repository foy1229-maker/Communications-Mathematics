# -*- coding: utf-8 -*-
"""중간고사 모의고사 A–E 세트 (mock.html?set=1~5) — 문제 · 정답 · 풀이 원본과 sympy 검산.

모든 세트가 시험 범위의 15개 주제(TOPICS)를 10문항(각 10점)에 빠짐없이 담고,
75–90분 안에 평균 70점 정도가 나오도록 소문항 배점과 계산량을 맞췄어요. 단원 순서는 섞어 배치했어요.

문항마다
  id, no, type(유형 이름), ref(단원), mins(권장 풀이 시간, 분), topics(주제 번호),
  stem, parts, answer, solution, types(문제 은행 유형 키 — '비슷한 문제' 링크), check(검산 함수)
를 가져요. build.py 가 check 를 모두 실행하고, 세트마다 15개 주제가 다 들어 있는지와
권장 시간 합이 75–90분인지 확인한 뒤 assets/mock-problems.js 로 내보내요.
"""
import random

import mpmath as mp
from sympy import (E, Matrix, N, Rational as R, atan, cos, diff, exp, expand, factor, integrate, lambdify,
                   limit, log, pi, simplify, sin, solve, sqrt, symbols, sympify)

x, y, z, t, s, r, u, v = symbols('x y z t s r u v', real=True)
th, ph, rho = symbols('theta phi rho', real=True)

# 시험 범위에서 꼭 나올 15개 주제 — 세트마다 모두 들어가야 해요.
TOPICS = {
    1: "극좌표 꽃잎(장미곡선) 이중적분",
    2: "라그랑주 승수법",
    3: "다변수 극한의 존재성",
    4: "미분가능성의 정의",
    5: "원주좌표 삼중적분",
    6: "구면좌표 삼중적분",
    7: "u·v 변수변환 (야코비안)",
    8: "적분 순서 바꾸기 (이중·삼중)",
    9: "그린 정리 · 곡선 나누어 직접 계산",
    10: "편도함수와 그래디언트",
    11: "곡선의 길이",
    12: "연쇄법칙",
    13: "스칼라 사영·벡터 사영 (comp·proj)",
    14: "접평면과 그래디언트",
    15: "2계 도함수 판정법 (극값·안장점)",
}


def EQ(a, b, tol=1e-12):
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


def grad(f, vs):
    return Matrix([diff(f, q) for q in vs])


def line_int(F, rr, a, b, vs=(x, y, z)):
    """∫_C F·dr, C: r(t) = rr (a ≤ t ≤ b)"""
    sub = dict(zip(vs, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


def nquad(f, a, b):
    """mpmath 수치적분 (구간 끝점·꺾이는 점 목록 허용)"""
    nodes = a if isinstance(a, (list, tuple)) else [a, b]
    return mp.quad(f, [mp.mpf(q) for q in nodes])


SETS = []


def Q(store, **kw):
    for key in ("id", "no", "type", "ref", "mins", "topics", "stem", "parts", "answer", "solution", "types", "check"):
        assert key in kw, f"{kw.get('id')} missing {key}"
    store.append(kw)


DEF7 = (r"(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 "
        r"$\Delta z=f_x(a,b)\Delta x+f_y(a,b)\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 이고 "
        r"$(\Delta x,\Delta y)\to(0,0)$ 일 때 $\varepsilon_1,\varepsilon_2\to0$ 인 $\varepsilon_1,\varepsilon_2$ 가 존재한다는 뜻이다.)")


# ════════════════════════════════════════════════════════════════════
# A세트
# ════════════════════════════════════════════════════════════════════
SA = []


def _c():
    T = symbols('T', positive=True)
    rr = Matrix([2*T, T**2, log(T)])
    vt = rr.diff(T)
    assert simplify(vt.dot(vt) - (2*T + 1/T)**2) == 0
    assert EQ(integrate(2*T + 1/T, (T, 1, E)), E**2)
    num = nquad(lambda q: mp.sqrt(4 + 4*q*q + 1/(q*q)), [1, mp.e], None)
    assert abs(num - mp.e**2) < 1e-10
    vv, aa = vt.subs(T, 1), rr.diff(T, 2).subs(T, 1)
    assert vv == Matrix([2, 2, 1]) and aa == Matrix([0, 2, -1])
    assert vv.dot(aa) / vv.norm() == 1
    proj = (vv.dot(aa) / vv.dot(vv)) * vv
    assert proj == Matrix([R(2, 3), R(2, 3), R(1, 3)])
    orth = aa - proj
    assert orth == Matrix([-R(2, 3), R(4, 3), -R(4, 3)]) and orth.dot(vv) == 0 and orth.norm() == 2
    assert vv.cross(aa) == Matrix([-4, 2, 4]) and vv.cross(aa).norm() / vv.norm() == 2
Q(SA, id="q1", no="1", type="곡선의 길이 · 사영(comp·proj)", ref="13.3 · 12.3 · 13.2", mins=6, topics=[11, 13],
  types=["13-arc", "12-proj", "13-motion"],
  stem=r"곡선 $\mathbf r(t)=\langle 2t,\ t^2,\ \ln t\rangle\ (t>0)$ 에 대하여",
  parts=[("a", r"$1\le t\le e$ 부분의 길이를 구하시오. [4점]"),
         ("b", r"$t=1$ 에서의 속도 $\mathbf v=\mathbf r'(1)$, 가속도 $\mathbf a=\mathbf r''(1)$ 에 대하여 $\operatorname{comp}_{\mathbf v}\mathbf a$ 와 $\operatorname{proj}_{\mathbf v}\mathbf a$ 를 구하시오. [4점]"),
         ("c", r"$\mathbf a$ 를 $\mathbf v$ 에 평행한 벡터와 $\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [2점]")],
  answer=[("a", r"$e^2$"),
          ("b", r"$\operatorname{comp}_{\mathbf v}\mathbf a=1$,  $\operatorname{proj}_{\mathbf v}\mathbf a=\big\langle\frac23,\ \frac23,\ \frac13\big\rangle$"),
          ("c", r"$\mathbf a=\big\langle\frac23,\frac23,\frac13\big\rangle+\big\langle-\frac23,\frac43,-\frac43\big\rangle$, 수직인 벡터의 크기 $2$")],
  solution=[("a", [r"$\mathbf r'(t)=\big\langle 2,\ 2t,\ \frac1t\big\rangle$, $\ |\mathbf r'(t)|^2=4t^2+4+\dfrac1{t^2}=\Big(2t+\dfrac1t\Big)^2$ → $|\mathbf r'(t)|=2t+\dfrac1t$ (완전제곱이 되는지 먼저 보기)",
                   r"$$\begin{aligned}L&=\int_1^e\Big(2t+\frac1t\Big)dt=\Big[t^2+\ln t\Big]_1^e\\&=(e^2+1)-1=e^2\end{aligned}$$"]),
            ("b", [r"$\mathbf r''(t)=\big\langle0,\ 2,\ -\frac1{t^2}\big\rangle$ → $\mathbf v=\langle2,2,1\rangle$, $\mathbf a=\langle0,2,-1\rangle$, $|\mathbf v|=3$, $\mathbf a\cdot\mathbf v=0+4-1=3$",
                   r"$\operatorname{comp}_{\mathbf v}\mathbf a=\dfrac{\mathbf a\cdot\mathbf v}{|\mathbf v|}=\dfrac33=1$",
                   r"$\operatorname{proj}_{\mathbf v}\mathbf a=\dfrac{\mathbf a\cdot\mathbf v}{|\mathbf v|^2}\,\mathbf v=\dfrac39\langle2,2,1\rangle=\big\langle\frac23,\frac23,\frac13\big\rangle$"]),
            ("c", [r"수직 성분: $\mathbf a-\operatorname{proj}_{\mathbf v}\mathbf a=\big\langle-\frac23,\ \frac43,\ -\frac43\big\rangle$ (확인: $\mathbf v$ 와 내적하면 $\frac{-4+8-4}{3}=0$)",
                   r"크기 $\dfrac{\sqrt{4+16+16}}{3}=2$. 가속도를 접선 방향 $1$ 과 법선 방향 $2$ 로 나눈 셈이에요. ($a_N=\frac{|\mathbf v\times\mathbf a|}{|\mathbf v|}=\frac{|\langle-4,2,4\rangle|}{3}=2$ 와 같아요.)"])],
  check=_c)


def _c():
    assert EQ(integrate(r, (r, 0, 2*sin(2*th)), (th, 0, pi/2)), pi/2)
    assert EQ(integrate(r**2*cos(th), (r, 0, 2*sin(2*th)), (th, 0, pi/2)), R(128, 105))
    assert EQ(integrate(sin(th)**3*cos(th)**4, (th, 0, pi/2)), R(2, 35))
    num = nquad(lambda T: (2*mp.sin(2*T))**3 / 3 * mp.cos(T), 0, mp.pi/2)
    assert abs(num - mp.mpf(128)/105) < 1e-12
Q(SA, id="q2", no="2", type="극좌표 이중적분 (장미곡선)", ref="15.3", mins=7, topics=[1],
  types=["15-polar"],
  stem=r"$D$ 는 장미곡선 $r=2\sin2\theta$ 의 제1사분면에 있는 꽃잎 $\big(0\le\theta\le\frac\pi2\big)$ 으로 둘러싸인 영역이다.",
  parts=[("a", r"$D$ 의 넓이를 이중적분으로 구하시오. [4점]"),
         ("b", r"$\displaystyle\iint_D x\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\pi}{2}$"), ("b", r"$\dfrac{128}{105}$")],
  solution=[("a", [r"$D:\ 0\le\theta\le\frac\pi2,\ 0\le r\le2\sin2\theta$, $\ dA=r\,dr\,d\theta$",
                   r"$$\begin{aligned}A&=\int_0^{\pi/2}\!\!\int_0^{2\sin2\theta}r\,dr\,d\theta\\&=\int_0^{\pi/2}2\sin^22\theta\,d\theta\\&=\int_0^{\pi/2}(1-\cos4\theta)\,d\theta=\frac\pi2\end{aligned}$$"]),
            ("b", [r"$x=r\cos\theta$: $$\begin{aligned}\iint_Dx\,dA&=\int_0^{\pi/2}\!\!\int_0^{2\sin2\theta}r^2\cos\theta\,dr\,d\theta\\&=\frac83\int_0^{\pi/2}\sin^32\theta\,\cos\theta\,d\theta\end{aligned}$$",
                   r"$\sin2\theta=2\sin\theta\cos\theta$ 이므로 $\sin^32\theta\cos\theta=8\sin^3\theta\cos^4\theta=8(1-\cos^2\theta)\cos^4\theta\,\sin\theta$",
                   r"$u=\cos\theta$ 로 치환: $$\begin{aligned}\frac{64}{3}\int_0^1(u^4-u^6)\,du&=\frac{64}{3}\Big(\frac15-\frac17\Big)\\&=\frac{64}{3}\cdot\frac{2}{35}=\frac{128}{105}\end{aligned}$$"])],
  check=_c)


def _c():
    kk, mm = symbols('kk mm', real=True)
    g = x*y**2/(x**2 + y**4)
    assert simplify(g.subs(x, kk*y**2) - kk/(kk**2 + 1)) == 0
    assert limit(g.subs(y, mm*x), x, 0) == 0
    assert simplify(g.subs(x, y**2)) == R(1, 2)
    f = x*y**2/(x**2 + y**2)
    hh = symbols('hh', nonzero=True, real=True)
    assert f.subs({x: hh, y: 0}) == 0 and f.subs({x: 0, y: hh}) == 0
    assert simplify(f.subs({x: hh, y: hh}) / hh) == R(1, 2)
    rnd = random.Random(1)
    for _ in range(300):
        X, Y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        assert abs(X*Y*Y/(X*X + Y*Y)) <= abs(X) + 1e-15
Q(SA, id="q3", no="3", type="극한의 존재성 · 미분가능성의 정의", ref="14.2 · 14.4", mins=9, topics=[3, 4],
  types=["14-dne", "14-differentiable"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy^2}{x^2+y^4}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("b", r"$f(x,y)=\dfrac{xy^2}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $\ f(0,0)=0$ 일 때, $f$ 가 원점에서 연속임을 보이고 $f_x(0,0),\ f_y(0,0)$ 을 구하시오. [3점]"),
         ("c", r"(b)의 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>" + DEF7)],
  answer=[("a", r"존재하지 않음 ($x$축을 따라 $0$, 곡선 $x=y^2$ 을 따라 $\frac12$)"),
          ("b", r"연속, $\ f_x(0,0)=0,\ f_y(0,0)=0$"),
          ("c", r"미분가능하지 않음 ($\Delta y=\Delta x$ 로 두면 $\varepsilon_1+\varepsilon_2=\frac12$)")],
  solution=[("a", [r"$x$축 $(y=0)$ 을 따라 $0$. 직선 $y=mx$ 를 따라가도 $\dfrac{m^2x^3}{x^2+m^4x^4}=\dfrac{m^2x}{1+m^4x^2}\to0$ 이라 직선만으로는 판정이 안 돼요.",
                   r"분모의 두 항 차수를 맞추는 곡선 $x=y^2$ 을 따라가면 $\dfrac{y^4}{y^4+y^4}=\dfrac12\to\dfrac12$",
                   r"경로에 따라 값이 다르므로 극한은 존재하지 않아요."]),
            ("b", [r"$\dfrac{y^2}{x^2+y^2}\le1$ 이므로 $|f(x,y)|\le|x|\to0=f(0,0)$ → 조임정리로 연속",
                   r"$f(h,0)=0,\ f(0,h)=0$ 이므로 $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{f(h,0)-f(0,0)}{h}=0$, 같은 방법으로 $f_y(0,0)=0$"]),
            ("c", [r"미분가능하다고 가정하면 (b)에 의해 $\Delta z=f(\Delta x,\Delta y)-f(0,0)=\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 이고 $\varepsilon_1,\varepsilon_2\to0$ 이어야 해요.",
                   r"$\Delta y=\Delta x\ (\ne0)$ 로 두면 좌변은 $f(\Delta x,\Delta x)=\dfrac{(\Delta x)^3}{2(\Delta x)^2}=\dfrac{\Delta x}{2}$, 우변은 $(\varepsilon_1+\varepsilon_2)\Delta x$ → $\varepsilon_1+\varepsilon_2=\dfrac12$",
                   r"그런데 $\Delta x\to0$ 이면 $(\Delta x,\Delta y)\to(0,0)$ 이므로 $\varepsilon_1+\varepsilon_2\to0$ 이어야 해요. 모순이므로 $f$ 는 원점에서 <b>미분가능하지 않아요</b>. (연속이고 편도함수도 있지만 미분가능하지 않은 예)"])],
  check=_c)


def _c():
    F = (x*y, x**2)
    I1 = line_int(F, (t, t**2), 0, 1, vs=(x, y))
    I2 = line_int(F, (t, t), 1, 0, vs=(x, y))
    assert I1 == R(3, 4) and I2 == -R(2, 3) and I1 + I2 == R(1, 12)
    curl = diff(F[1], x) - diff(F[0], y)
    assert simplify(curl - x) == 0
    assert integrate(curl, (y, x**2, x), (x, 0, 1)) == R(1, 12)
    A1 = line_int((0, x), (t, t**2), 0, 1, vs=(x, y))
    A2 = line_int((0, x), (t, t), 1, 0, vs=(x, y))
    assert A1 == R(2, 3) and A2 == -R(1, 2) and A1 + A2 == R(1, 6)
    assert integrate(x - x**2, (x, 0, 1)) == R(1, 6)
Q(SA, id="q4", no="4", type="그린 정리 · 곡선 나누어 직접 계산", ref="16.2 · 16.4", mins=9, topics=[9],
  types=["16-vector", "16-green", "16-greenarea"],
  stem=r"$C$ 는 곡선 $y=x^2$ 과 직선 $y=x$ 로 둘러싸인 영역 $D$ 의 경계이고, 양의 방향(반시계 방향)이다. $\displaystyle I=\oint_C xy\,dx+x^2\,dy$ 에 대하여",
  parts=[("a", r"$C$ 를 두 곡선으로 나누어 $I$ 를 직접 계산하시오. [4점]"),
         ("b", r"그린 정리를 이용해 $I$ 를 계산하고 (a)와 같은지 확인하시오. [4점]"),
         ("c", r"그린 정리를 이용하여 $D$ 의 넓이를 선적분으로 구하시오. [2점]")],
  answer=[("a", r"$\dfrac{1}{12}$"), ("b", r"$\dfrac{1}{12}$"), ("c", r"$\dfrac16$")],
  solution=[("a", [r"양의 방향: $C_1$ 은 $y=x^2$ 을 따라 $(0,0)\to(1,1)$, $C_2$ 는 $y=x$ 를 따라 $(1,1)\to(0,0)$",
                   r"$C_1:\ x=t,\ y=t^2\ (0\le t\le1)$, $dx=dt,\ dy=2t\,dt$ → $\displaystyle\int_{C_1}=\int_0^1\big(t^3+t^2\cdot2t\big)\,dt=\int_0^13t^3\,dt=\frac34$",
                   r"$C_2:\ x=t,\ y=t\ (t:1\to0)$ → $\displaystyle\int_{C_2}=\int_1^0\big(t^2+t^2\big)\,dt=-\frac23$",
                   r"$I=\dfrac34-\dfrac23=\dfrac1{12}$"]),
            ("b", [r"$P=xy,\ Q=x^2$ → $Q_x-P_y=2x-x=x$, $\ D:\ 0\le x\le1,\ x^2\le y\le x$",
                   r"$$\begin{aligned}I&=\iint_Dx\,dA=\int_0^1 x\,(x-x^2)\,dx\\&=\frac13-\frac14=\frac1{12}\end{aligned}$$ — (a)와 같아요."]),
            ("c", [r"$P=0,\ Q=x$ 이면 $Q_x-P_y=1$ 이므로 넓이 $A=\displaystyle\oint_C x\,dy$",
                   r"$\displaystyle\int_{C_1}x\,dy=\int_0^1t\cdot2t\,dt=\frac23$, $\ \displaystyle\int_{C_2}x\,dy=\int_1^0t\,dt=-\frac12$ → $A=\dfrac23-\dfrac12=\dfrac16$",
                   r"(확인: $\displaystyle\int_0^1(x-x^2)\,dx=\frac16$)"])],
  check=_c)


def _c():
    assert EQ(integrate(r**3, (z, 0, 4 - r**2), (r, 0, 2), (th, 0, 2*pi)), 32*pi/3)
    cyl = integrate(z*r, (z, r/sqrt(3), sqrt(4 - r**2)), (r, 0, sqrt(3)), (th, 0, 2*pi))
    sph = integrate(rho**3*cos(ph)*sin(ph), (rho, 0, 2), (ph, 0, pi/3), (th, 0, 2*pi))
    assert EQ(cyl, 3*pi) and EQ(sph, 3*pi)
    assert EQ(atan(sqrt(3)), pi/3)
    assert sqrt(3) in solve(r**2 + r**2/3 - 4, r)
Q(SA, id="q5", no="5", type="원주좌표 · 구면좌표 삼중적분", ref="15.7 · 15.8", mins=9, topics=[5, 6],
  types=["15-cyl", "15-sphconv"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$E$ 가 포물면 $z=4-x^2-y^2$ 과 $xy$ 평면으로 둘러싸인 입체일 때, 원주좌표를 이용하여 $\displaystyle\iiint_E(x^2+y^2)\,dV$ 를 구하시오. [5점]"),
         ("b", r"다음 적분을 구면좌표의 적분으로 바꾸어 쓰고, 그 값을 구하시오. [5점] $$\int_0^{2\pi}\!\!\int_0^{\sqrt3}\!\!\int_{r/\sqrt3}^{\sqrt{4-r^2}}z\,r\,dz\,dr\,d\theta$$")],
  answer=[("a", r"$\dfrac{32\pi}{3}$"),
          ("b", r"$\int_0^{2\pi}\!\int_0^{\pi/3}\!\int_0^2\rho^3\cos\phi\,\sin\phi\,d\rho\,d\phi\,d\theta$, 값 $3\pi$")],
  solution=[("a", [r"원주좌표: $E:\ 0\le\theta\le2\pi,\ 0\le r\le2,\ 0\le z\le4-r^2$, $\ x^2+y^2=r^2$, $\ dV=r\,dz\,dr\,d\theta$",
                   r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{4-r^2}r^3\,dz\,dr\,d\theta\\&=2\pi\int_0^2(4r^3-r^5)\,dr\\&=2\pi\Big(16-\frac{64}{6}\Big)=\frac{32\pi}{3}\end{aligned}$$"]),
            ("b", [r"아래 경계 $z=\dfrac{r}{\sqrt3}$ 은 원뿔: $\tan\phi=\dfrac rz=\sqrt3$ → $\phi=\dfrac\pi3$. 위 경계 $z=\sqrt{4-r^2}$ 은 구 $\rho=2$ (두 곡면은 $r=\sqrt3$ 에서 만나요).",
                   r"$E:\ 0\le\theta\le2\pi,\ 0\le\phi\le\frac\pi3,\ 0\le\rho\le2$, $\ z=\rho\cos\phi$, $\ r\,dz\,dr\,d\theta=dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
                   r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^{\pi/3}\!\!\int_0^2\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta\\&=2\pi\cdot\Big[\frac{\sin^2\phi}{2}\Big]_0^{\pi/3}\cdot\frac{2^4}{4}\\&=2\pi\cdot\frac38\cdot4=3\pi\end{aligned}$$"])],
  check=_c)


def _c():
    f = x**3 - 6*x*y + 3*y**2
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    assert sorted((c[x], c[y]) for c in crit) == [(0, 0), (2, 2)]
    fxx, fyy, fxy = diff(f, x, 2), diff(f, y, 2), diff(f, x, y)
    D = fxx*fyy - fxy**2
    assert D.subs({x: 0, y: 0}) == -36
    assert D.subs({x: 2, y: 2}) == 36 and fxx.subs({x: 2, y: 2}) == 12 and f.subs({x: 2, y: 2}) == -4
    assert expand(f.subs(x, 3) - 3*(y - 3)**2) == 0
    g3 = f.subs(y, 3)
    assert sqrt(6) in solve(diff(g3, x), x)
    assert EQ(g3.subs(x, sqrt(6)), 27 - 12*sqrt(6))
    cands = [f.subs({x: a, y: b}) for a, b in [(2, 2), (0, 0), (3, 0), (0, 3), (3, 3), (sqrt(6), 3)]]
    assert max(cands, key=lambda c: float(c)) == 27 and min(cands, key=lambda c: float(c)) == -4
    fn = lambdify((x, y), f)
    vals = [fn(3*i/300, 3*j/300) for i in range(301) for j in range(301)]
    assert abs(max(vals) - 27) < 1e-9 and min(vals) >= -4 - 1e-9
    assert 12**2 * 6 < 31**2
Q(SA, id="q6", no="6", type="2계 도함수 판정법 · 닫힌 영역의 최대·최소", ref="14.7", mins=9, topics=[15],
  types=["14-crit", "14-absext"],
  stem=r"$f(x,y)=x^3-6xy+3y^2$ 에 대하여",
  parts=[("a", r"$f$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"),
         ("b", r"정사각형 영역 $R=\{(x,y)\mid0\le x\le3,\ 0\le y\le3\}$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]")],
  answer=[("a", r"$(0,0)$: 안장점,  $(2,2)$: 극솟값 $-4$"),
          ("b", r"최댓값 $27$ (점 $(3,0),\ (0,3)$), 최솟값 $-4$ (점 $(2,2)$)")],
  solution=[("a", [r"$f_x=3x^2-6y=0,\ \ f_y=-6x+6y=0$ → $y=x$, $\ 3x^2-6x=0$ → $x=0,\ 2$ → 임계점 $(0,0),\ (2,2)$",
                   r"$f_{xx}=6x,\ f_{yy}=6,\ f_{xy}=-6$, $\ D=f_{xx}f_{yy}-f_{xy}^2=36x-36$",
                   r"$(0,0)$: $D=-36<0$ → 안장점.  $(2,2)$: $D=36>0,\ f_{xx}=12>0$ → 극솟값 $f(2,2)=8-24+12=-4$"]),
            ("b", [r"내부 임계점은 $(2,2)$ 하나 (값 $-4$). 경계는 네 변으로 나누어 1변수 문제로 봐요.",
                   r"$y=0$: $f=x^3\in[0,27]$.  $x=0$: $f=3y^2\in[0,27]$.  $x=3$: $f=3y^2-18y+27=3(y-3)^2\in[0,27]$",
                   r"$y=3$: $f=x^3-18x+27$, $\ f'=3x^2-18=0 \Rightarrow x=\sqrt6$ → $f(\sqrt6,3)=27-12\sqrt6\ (\approx-2.4)$, 끝점에서는 $27,\ 0$",
                   r"후보 비교: $27-12\sqrt6>-4 \iff 12\sqrt6<31 \iff 864<961$ → 최댓값 $27$ (점 $(3,0),\ (0,3)$), 최솟값 $-4$ (점 $(2,2)$)"])],
  check=_c)


def _c():
    X, Y = r*cos(th), r*sin(th)
    for ft in (x**2*y + y**3, exp(x)*sin(y), x*y**2 - 3*x):
        fx, fy = diff(ft, x).subs({x: X, y: Y}), diff(ft, y).subs({x: X, y: Y})
        Z = ft.subs({x: X, y: Y})
        assert simplify(diff(Z, r) - (fx*cos(th) + fy*sin(th))) == 0
        assert simplify(diff(Z, th) - (-fx*r*sin(th) + fy*r*cos(th))) == 0
        assert simplify(fx**2 + fy**2 - (diff(Z, r)**2 + diff(Z, th)**2 / r**2)) == 0
    a, b = symbols('a b')
    sol = solve([a*cos(pi/2) + b*sin(pi/2) - 3, -a*2*sin(pi/2) + b*2*cos(pi/2) + 4], [a, b], dict=True)[0]
    assert sol[a] == 2 and sol[b] == 3 and sqrt(sol[a]**2 + sol[b]**2) == sqrt(13)
    assert 3**2 + R(1, 4)*(-4)**2 == 13
Q(SA, id="q7", no="7", type="연쇄법칙 · 그래디언트", ref="14.5 · 14.6", mins=8, topics=[12, 10],
  types=["14-chain", "14-maxrate"],
  stem=r"$z=f(x,y)$ 는 미분가능하고 $x=r\cos\theta,\ y=r\sin\theta$ 이다.",
  parts=[("a", r"$\dfrac{\partial z}{\partial r},\ \dfrac{\partial z}{\partial\theta}$ 를 $f_x,\ f_y$ 로 나타내시오. [3점]"),
         ("b", r"$\big(f_x\big)^2+\big(f_y\big)^2=\Big(\dfrac{\partial z}{\partial r}\Big)^2+\dfrac{1}{r^2}\Big(\dfrac{\partial z}{\partial\theta}\Big)^2$ 임을 보이시오. [4점]"),
         ("c", r"$(r,\theta)=\big(2,\frac\pi2\big)$ 에서 $\dfrac{\partial z}{\partial r}=3,\ \dfrac{\partial z}{\partial\theta}=-4$ 일 때, 점 $(0,2)$ 에서 $\nabla f$ 와 $f$ 의 최대 변화율을 구하시오. [3점]")],
  answer=[("a", r"$z_r=f_x\cos\theta+f_y\sin\theta$,  $z_\theta=-f_x\,r\sin\theta+f_y\,r\cos\theta$"),
          ("b", r"아래 풀이"),
          ("c", r"$\nabla f(0,2)=\langle2,\ 3\rangle$, 최대 변화율 $\sqrt{13}$")],
  solution=[("a", [r"$z_r=f_x\dfrac{\partial x}{\partial r}+f_y\dfrac{\partial y}{\partial r}=f_x\cos\theta+f_y\sin\theta$",
                   r"$z_\theta=f_x\dfrac{\partial x}{\partial\theta}+f_y\dfrac{\partial y}{\partial\theta}=-f_x\,r\sin\theta+f_y\,r\cos\theta$"]),
            ("b", [r"$z_r^2=f_x^2\cos^2\theta+2f_xf_y\sin\theta\cos\theta+f_y^2\sin^2\theta$",
                   r"$\dfrac{1}{r^2}z_\theta^2=f_x^2\sin^2\theta-2f_xf_y\sin\theta\cos\theta+f_y^2\cos^2\theta$",
                   r"더하면 교차항이 지워지고 $\sin^2\theta+\cos^2\theta=1$ 이므로 $z_r^2+\dfrac{1}{r^2}z_\theta^2=f_x^2+f_y^2$"]),
            ("c", [r"$(r,\theta)=\big(2,\frac\pi2\big)$ 이면 $(x,y)=(0,2)$, $\ \cos\theta=0,\ \sin\theta=1$",
                   r"$z_r=f_y=3$, $\ z_\theta=-2f_x=-4 \Rightarrow f_x=2$ → $\nabla f(0,2)=\langle2,3\rangle$",
                   r"최대 변화율 $|\nabla f(0,2)|=\sqrt{4+9}=\sqrt{13}$ (방향 $\frac1{\sqrt{13}}\langle2,3\rangle$). (b)로 확인: $3^2+\frac14(-4)^2=13$"])],
  check=_c)


def _c():
    J = Matrix([[diff((u + v)/2, u), diff((u + v)/2, v)], [diff((u - v)/2, u), diff((u - v)/2, v)]]).det()
    assert J == -R(1, 2)
    assert expand(((u + v)/2)**2 - ((u - v)/2)**2 - u*v) == 0
    assert EQ(integrate(u*exp(u*v)*R(1, 2), (v, 0, 2), (u, 0, 3)), (exp(6) - 7)/4)

    def inner(X):
        lo, hi = max(-X, X - 2), min(3 - X, X)
        return mp.quad(lambda Y: (X + Y)*mp.e**(X*X - Y*Y), [lo, hi]) if hi > lo else mp.mpf(0)
    num = nquad(inner, [0, 1, 1.5, 2.5], None)
    assert abs(num - (mp.e**6 - 7)/4) < 1e-8
Q(SA, id="q8", no="8", type="변수변환 (야코비안)", ref="15.9", mins=8, topics=[7],
  types=["15-change"],
  stem=r"$R$ 은 네 직선 $x-y=0,\ x-y=2,\ x+y=0,\ x+y=3$ 으로 둘러싸인 영역이다. 변환 $u=x+y,\ v=x-y$ 를 이용하여",
  parts=[("a", r"야코비안 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"),
         ("b", r"$\displaystyle\iint_R(x+y)\,e^{x^2-y^2}\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\partial(x,y)}{\partial(u,v)}=-\dfrac12$ (절댓값 $\frac12$), $\ S=\{(u,v)\mid0\le u\le3,\ 0\le v\le2\}$"),
          ("b", r"$\dfrac{e^6-7}{4}$")],
  solution=[("a", [r"$x=\dfrac{u+v}{2},\ y=\dfrac{u-v}{2}$ → $$\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\frac12&\frac12\\[2pt]\frac12&-\frac12\end{vmatrix}=-\frac14-\frac14=-\frac12$$",
                   r"네 직선이 $v=0,\ v=2,\ u=0,\ u=3$ 이 되므로 $S:\ 0\le u\le3,\ 0\le v\le2$ (직사각형)"]),
            ("b", [r"$x^2-y^2=(x+y)(x-y)=uv$, $\ dA=\Big|\dfrac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv=\dfrac12\,du\,dv$",
                   r"$$\begin{aligned}&\iint_R(x+y)e^{x^2-y^2}\,dA\\&=\frac12\int_0^3\!\!\int_0^2 u\,e^{uv}\,dv\,du\end{aligned}$$ $v$ 로 먼저 적분하면 $u\,e^{uv}$ 가 바로 적분돼요.",
                   r"$$\begin{aligned}&\frac12\int_0^3\Big[e^{uv}\Big]_{v=0}^{v=2}du\\&=\frac12\int_0^3\big(e^{2u}-1\big)\,du\\&=\frac12\Big(\frac{e^6-1}{2}-3\Big)=\frac{e^6-7}{4}\end{aligned}$$"])],
  check=_c)


def _c():
    lam = symbols('lam', real=True)
    g = x**2 + 2*y**2 + 3*z**2
    sols = solve([1 - lam*diff(g, x), 1 - lam*diff(g, y), 1 - lam*diff(g, z), g - 66], [x, y, z, lam], dict=True)
    got = sorted([(q[x], q[y], q[z], q[x] + q[y] + q[z]) for q in sols], key=lambda p: p[3])
    assert got == [(-6, -3, -2, -11), (6, 3, 2, 11)]
    n = grad(g, (x, y, z)).subs({x: 6, y: 3, z: 2})
    assert n == Matrix([12, 12, 12])
    assert expand(n.dot(Matrix([x - 6, y - 3, z - 2])) / 12 - (x + y + z - 11)) == 0
Q(SA, id="q9", no="9", type="라그랑주 승수법 · 접평면과 그래디언트", ref="14.8 · 14.6", mins=9, topics=[2, 14],
  types=["14-lagrange", "14-levelsurf"],
  stem=r"타원면 $E:\ x^2+2y^2+3z^2=66$ 과 함수 $f(x,y,z)=x+y+z$ 에 대하여",
  parts=[("a", r"라그랑주 승수법으로 $E$ 위에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]"),
         ("b", r"$f$ 가 최댓값을 갖는 점에서 $E$ 의 접평면의 방정식을 구하시오. [3점]"),
         ("c", r"(b)의 접평면이 $f$ 의 등위면 $f(x,y,z)=k$ ($k$ 는 (a)의 최댓값)와 같은 평면인 이유를 그래디언트를 이용해 설명하시오. [2점]")],
  answer=[("a", r"최댓값 $11$ (점 $(6,3,2)$), 최솟값 $-11$ (점 $(-6,-3,-2)$)"),
          ("b", r"$x+y+z=11$"),
          ("c", r"최대점에서 $\nabla f=\lambda\nabla g$ — 두 평면의 법선벡터가 평행하고 같은 점을 지나요.")],
  solution=[("a", [r"$g=x^2+2y^2+3z^2$, $\ \nabla f=\lambda\nabla g$: $1=2\lambda x,\ 1=4\lambda y,\ 1=6\lambda z$ ($\lambda\ne0$) → $x=\dfrac1{2\lambda},\ y=\dfrac1{4\lambda},\ z=\dfrac1{6\lambda}$",
                   r"제약식에 대입: $\dfrac{1}{\lambda^2}\Big(\dfrac14+\dfrac28+\dfrac3{36}\Big)=\dfrac{11}{24\lambda^2}=66 \Rightarrow \lambda^2=\dfrac1{144},\ \lambda=\pm\dfrac1{12}$",
                   r"$\lambda=\frac1{12}$: 점 $(6,3,2)$, $f=11$.  $\lambda=-\frac1{12}$: 점 $(-6,-3,-2)$, $f=-11$ → 최댓값 $11$, 최솟값 $-11$"]),
            ("b", [r"$\nabla g=\langle2x,\ 4y,\ 6z\rangle$ → $\nabla g(6,3,2)=\langle12,\ 12,\ 12\rangle\parallel\langle1,1,1\rangle$",
                   r"$(x-6)+(y-3)+(z-2)=0 \Rightarrow x+y+z=11$"]),
            ("c", [r"최대점에서 $\nabla f=\lambda\nabla g$ 이므로 등위면 $f=11$ 의 법선 $\nabla f=\langle1,1,1\rangle$ 과 $E$ 의 법선 $\nabla g$ 가 평행해요.",
                   r"두 평면 모두 점 $(6,3,2)$ 를 지나고 법선이 평행하므로 같은 평면이에요. (평면 $x+y+z=k$ 를 밀어 가다 $E$ 에 마지막으로 접하는 순간의 $k$ 가 최댓값)"])],
  check=_c)


def _c():
    assert EQ(integrate(exp(x**3), (y, 0, x**2), (x, 0, 1)), (E - 1)/3)
    num = nquad(lambda Y: mp.quad(lambda X: mp.e**(X**3), [mp.sqrt(Y), 1]), 0, 1)
    assert abs(num - (mp.e - 1)/3) < 1e-10
    assert EQ(integrate(6*cos(y**3), (z, 0, x), (x, 0, y), (y, 0, 1)), sin(1))
    numb = nquad(lambda X: mp.quad(lambda Y: 6*mp.cos(Y**3)*X, [X, 1]), 0, 1)
    assert abs(numb - mp.sin(1)) < 1e-10
Q(SA, id="q10", no="10", type="적분 순서 바꾸기 (이중·삼중)", ref="15.2 · 15.6", mins=7, topics=[8],
  types=["15-order", "15-order3"],
  stem=r"적분 순서를 바꾸어 다음 값을 구하시오.",
  parts=[("a", r"$\displaystyle\int_0^1\!\!\int_{\sqrt y}^1 e^{x^3}\,dx\,dy$ [4점]"),
         ("b", r"$\displaystyle\int_0^1\!\!\int_x^1\!\!\int_0^x 6\cos(y^3)\,dz\,dy\,dx$ [6점]")],
  answer=[("a", r"$\dfrac{e-1}{3}$"), ("b", r"$\sin1$")],
  solution=[("a", [r"영역: $0\le y\le1,\ \sqrt y\le x\le1$ → $0\le x\le1,\ 0\le y\le x^2$",
                   r"$$\begin{aligned}\int_0^1\!\!\int_0^{x^2}e^{x^3}\,dy\,dx&=\int_0^1x^2e^{x^3}\,dx\\&=\Big[\frac{e^{x^3}}{3}\Big]_0^1=\frac{e-1}{3}\end{aligned}$$"]),
            ("b", [r"$\cos(y^3)$ 은 $y$ 로 바로 적분할 수 없으니 $y$ 를 가장 바깥으로 보내요.",
                   r"영역: $0\le x\le1,\ x\le y\le1,\ 0\le z\le x$ → $0\le y\le1,\ 0\le x\le y,\ 0\le z\le x$",
                   r"$$\begin{aligned}&\int_0^1\!\!\int_0^y\!\!\int_0^x6\cos(y^3)\,dz\,dx\,dy\\&=\int_0^16\cos(y^3)\cdot\frac{y^2}{2}\,dy\\&=\Big[\sin(y^3)\Big]_0^1=\sin1\end{aligned}$$"])],
  check=_c)

SETS.append({"id": "a", "no": 1, "label": "A", "title": "모의고사 A세트", "focus": "15개 주제 · 10문항 · 각 10점",
             "lead": "15개 주제를 10문항에 모두 담은 첫 번째 세트예요. 곡선의 길이와 사영으로 가볍게 시작해서 장미곡선 적분, 극한과 미분가능성의 정의, 그린 정리(두 방법), 원주·구면좌표, 극값과 닫힌 영역, 극좌표 연쇄법칙, u·v 변수변환, 라그랑주와 접평면, 적분 순서 바꾸기까지 단원 순서를 섞어 배치했어요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
             "problems": SA})


# ════════════════════════════════════════════════════════════════════
# B세트
# ════════════════════════════════════════════════════════════════════
SB = []


def _c():
    dx = symbols('dx', nonzero=True)
    G = x**2
    assert simplify((G.subs(x, 1 + dx) - G.subs(x, 1))/dx - diff(G, x).subs(x, 1)) == dx   # 예: g=x^2, a=1 이면 ε=Δx
    mm = symbols('mm', real=True)
    g = x**2*y/(x**4 + y**2)
    assert limit(g.subs(y, 0), x, 0) == 0 and limit(g.subs(y, mm*x), x, 0) == 0
    assert simplify(g.subs(y, x**2)) == R(1, 2)
    f = x**2*y**2/(x**2 + y**2)
    hh = symbols('hh', nonzero=True, real=True)
    assert f.subs({x: hh, y: 0}) == 0 and f.subs({x: 0, y: hh}) == 0
    assert simplify(x*y**2/(x**2 + y**2)*x - f) == 0
    rnd = random.Random(7)
    for _ in range(300):
        X, Y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        assert abs(X*Y*Y/(X*X + Y*Y)) <= abs(X) + 1e-15
Q(SB, id="q1", no="1", type="미분가능성의 정의 · 극한의 존재성", ref="14.4 · 14.2", mins=9, topics=[4, 3],
  types=["14-differentiable", "14-dne"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"일변수함수 $y=g(x)$ 가 $x=a$ 에서 미분가능할 때, 미분의 정의로부터 $$\Delta y=g'(a)\,\Delta x+\varepsilon\,\Delta x$$ 이고 $\Delta x\to0$ 일 때 $\varepsilon\to0$ 인 $\varepsilon$ 이 존재함을 보이시오. 단, $\Delta y=g(a+\Delta x)-g(a)$ 이다. [3점]"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^4+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("c", r"$f(x,y)=\dfrac{x^2y^2}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $\ f(0,0)=0$ 일 때, $f_x(0,0),\ f_y(0,0)$ 을 구하고 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>" + DEF7)],
  answer=[("a", r"아래 풀이"),
          ("b", r"존재하지 않음 ($x$축을 따라 $0$, 곡선 $y=x^2$ 을 따라 $\frac12$)"),
          ("c", r"$f_x(0,0)=f_y(0,0)=0$, 미분가능 $\Big(\varepsilon_1=\dfrac{\Delta x\,(\Delta y)^2}{(\Delta x)^2+(\Delta y)^2},\ \varepsilon_2=0\Big)$")],
  solution=[("a", [r"$\Delta x\ne0$ 일 때 $\varepsilon=\dfrac{\Delta y}{\Delta x}-g'(a)$ 로 정의해요.",
                   r"미분의 정의 $g'(a)=\displaystyle\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}$ 에서 $\displaystyle\lim_{\Delta x\to0}\varepsilon=g'(a)-g'(a)=0$",
                   r"정의한 식의 양변에 $\Delta x$ 를 곱하면 $\Delta y=g'(a)\Delta x+\varepsilon\Delta x$. $\ \Delta x=0$ 일 때는 $\varepsilon=0$ 으로 정하면 양변이 모두 $0$ 이라 그대로 성립해요."]),
            ("b", [r"$x$축 $(y=0)$ 을 따라 $0$. 직선 $y=mx$ 를 따라가도 $\dfrac{mx^3}{x^4+m^2x^2}=\dfrac{mx}{x^2+m^2}\to0$ 이라 직선만으로는 판정이 안 돼요.",
                   r"곡선 $y=x^2$ 을 따라가면 $\dfrac{x^4}{x^4+x^4}=\dfrac12$ → 경로마다 값이 다르므로 극한은 존재하지 않아요."]),
            ("c", [r"$f(h,0)=f(0,h)=0$ 이므로 $f_x(0,0)=f_y(0,0)=0$",
                   r"$$\begin{aligned}\Delta z&=f(\Delta x,\Delta y)-f(0,0)\\&=\frac{(\Delta x)^2(\Delta y)^2}{(\Delta x)^2+(\Delta y)^2}\\&=\underbrace{\frac{\Delta x\,(\Delta y)^2}{(\Delta x)^2+(\Delta y)^2}}_{\varepsilon_1}\,\Delta x+\underbrace{0}_{\varepsilon_2}\cdot\Delta y\end{aligned}$$",
                   r"$\dfrac{(\Delta y)^2}{(\Delta x)^2+(\Delta y)^2}\le1$ 이므로 $|\varepsilon_1|\le|\Delta x|\to0$ (조임정리), $\ \varepsilon_2=0$ → 정의를 만족하므로 원점에서 <b>미분가능</b>해요."])],
  check=_c)


def _c():
    f = x*exp(y) + y*z**2
    P0 = {x: 2, y: 0, z: 1}
    gP = grad(f, (x, y, z)).subs(P0)
    assert gP == Matrix([1, 3, 0]) and f.subs(P0) == 2
    PQ = Matrix([2, 1, 2])
    assert PQ.norm() == 3 and gP.dot(PQ / 3) == R(5, 3)
    assert gP.norm() == sqrt(10)
    assert expand(gP.dot(Matrix([x - 2, y, z - 1])) - (x + 3*y - 2)) == 0
Q(SB, id="q2", no="2", type="그래디언트 · 방향도함수 · 접평면", ref="14.6 · 14.3", mins=8, topics=[10, 14],
  types=["14-dir", "14-maxrate", "14-levelsurf"],
  stem=r"$f(x,y,z)=x\,e^{y}+yz^2$ 과 점 $P(2,0,1)$ 에 대하여",
  parts=[("a", r"$f_x,\ f_y,\ f_z$ 와 $\nabla f(P)$ 를 구하시오. [2점]"),
         ("b", r"$P$ 에서 점 $Q(4,1,3)$ 을 향하는 방향으로의 방향도함수를 구하시오. [3점]"),
         ("c", r"$P$ 에서 $f$ 가 가장 빠르게 증가하는 방향(단위벡터)과 그 방향의 변화율을 구하시오. [2점]"),
         ("d", r"등위곡면 $f(x,y,z)=2$ 위의 점 $P$ 에서 접평면과 법선의 방정식을 구하시오. [3점]")],
  answer=[("a", r"$f_x=e^y,\ f_y=xe^y+z^2,\ f_z=2yz$, $\ \nabla f(P)=\langle1,3,0\rangle$"),
          ("b", r"$\dfrac53$"),
          ("c", r"$\dfrac{1}{\sqrt{10}}\langle1,3,0\rangle$, 변화율 $\sqrt{10}$"),
          ("d", r"접평면 $x+3y=2$, 법선 $x=2+t,\ y=3t,\ z=1$")],
  solution=[("a", [r"$f_x=e^y,\ \ f_y=xe^y+z^2,\ \ f_z=2yz$ → $\nabla f(2,0,1)=\langle1,\ 2+1,\ 0\rangle=\langle1,3,0\rangle$"]),
            ("b", [r"$\overrightarrow{PQ}=\langle2,1,2\rangle$, $|\overrightarrow{PQ}|=3$, $\ \mathbf u=\frac13\langle2,1,2\rangle$ (반드시 단위벡터로)",
                   r"$D_{\mathbf u}f(P)=\nabla f(P)\cdot\mathbf u=\dfrac{2+3+0}{3}=\dfrac53$"]),
            ("c", [r"가장 빠르게 증가하는 방향은 $\nabla f(P)$ 방향: $\mathbf u=\dfrac{1}{\sqrt{10}}\langle1,3,0\rangle$, 그 변화율은 $|\nabla f(P)|=\sqrt{10}$"]),
            ("d", [r"$f(P)=2e^0+0=2$ 이므로 $P$ 는 등위곡면 $f=2$ 위의 점이고 법선벡터는 $\nabla f(P)=\langle1,3,0\rangle$",
                   r"접평면: $1(x-2)+3(y-0)+0(z-1)=0 \Rightarrow x+3y=2$",
                   r"법선: $x=2+t,\ y=3t,\ z=1$"])],
  check=_c)


def _c():
    assert Matrix([[diff(x - 2*y, x), diff(x - 2*y, y)], [diff(3*x - y, x), diff(3*x - y, y)]]).det() == 5
    inv = solve([x - 2*y - u, 3*x - y - v], [x, y], dict=True)[0]
    assert Matrix([[diff(inv[x], u), diff(inv[x], v)], [diff(inv[y], u), diff(inv[y], v)]]).det() == R(1, 5)
    assert EQ(integrate(u/v*R(1, 5), (u, 0, 4), (v, 1, 8)), 24*log(2)/5)

    def inner(X):
        lo, hi = max((X - 4)/2, 3*X - 8), min(X/2, 3*X - 1)
        return mp.quad(lambda Y: (X - 2*Y)/(3*X - Y), [lo, hi]) if hi > lo else mp.mpf(0)
    num = nquad(inner, [-0.4, 0.4, 2.4, 3.2], None)
    assert abs(num - 24*mp.log(2)/5) < 1e-8
Q(SB, id="q3", no="3", type="변수변환 (야코비안)", ref="15.9", mins=8, topics=[7],
  types=["15-change"],
  stem=r"$R$ 은 네 직선 $x-2y=0,\ x-2y=4,\ 3x-y=1,\ 3x-y=8$ 로 둘러싸인 평행사변형이다. 변환 $u=x-2y,\ v=3x-y$ 를 이용하여",
  parts=[("a", r"야코비안 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"),
         ("b", r"$\displaystyle\iint_R\frac{x-2y}{3x-y}\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac15$, $\ S=\{(u,v)\mid0\le u\le4,\ 1\le v\le8\}$"),
          ("b", r"$\dfrac{8\ln8}{5}=\dfrac{24\ln2}{5}$")],
  solution=[("a", [r"$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&-2\\3&-1\end{vmatrix}=-1+6=5$$ 이므로 $\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac{1}{5}$ (역변환 $x,y$ 를 따로 구하지 않아도 돼요)",
                   r"네 직선이 $u=0,\ u=4,\ v=1,\ v=8$ 로 바뀌어 $S:\ 0\le u\le4,\ 1\le v\le8$ (직사각형)"]),
            ("b", [r"$dA=\dfrac15\,du\,dv$ → $$\begin{aligned}\iint_R\frac{x-2y}{3x-y}\,dA&=\frac15\int_1^8\!\!\int_0^4\frac uv\,du\,dv\\&=\frac15\cdot\Big[\frac{u^2}{2}\Big]_0^4\cdot\Big[\ln v\Big]_1^8\end{aligned}$$",
                   r"$=\dfrac15\cdot8\cdot\ln8=\dfrac{8\ln8}{5}=\dfrac{24\ln2}{5}$"])],
  check=_c)


def _c():
    assert EQ(4*integrate(r, (r, 0, 2*cos(2*th)), (th, -pi/4, pi/4)), 2*pi)
    assert EQ(8*integrate(r, (r, 0, 2*cos(2*th)), (th, 0, pi/4)), 2*pi)
    petal = integrate(r, (r, 0, 1), (th, -pi/6, pi/6)) + 2*integrate(r, (r, 0, 2*cos(2*th)), (th, pi/6, pi/4))
    assert EQ(petal, pi/3 - sqrt(3)/4) and EQ(4*petal, 4*pi/3 - sqrt(3))
    num = 4*nquad(lambda T: min(1, abs(2*mp.cos(2*T)))**2 / 2, [0, mp.pi/6, mp.pi/4, mp.pi/3, mp.pi/2], None)
    assert abs(num - (4*mp.pi/3 - mp.sqrt(3))) < 1e-10
Q(SB, id="q4", no="4", type="극좌표 이중적분 (장미곡선)", ref="15.3", mins=8, topics=[1],
  types=["15-polar"],
  stem=r"장미곡선 $r=2\cos2\theta$ 에 대하여",
  parts=[("a", r"장미곡선이 둘러싸는 영역 전체(꽃잎 4장)의 넓이를 구하시오. [4점]"),
         ("b", r"장미곡선의 내부이면서 원 $r=1$ 의 내부인 영역의 넓이를 구하시오. [6점]")],
  answer=[("a", r"$2\pi$"), ("b", r"$\dfrac{4\pi}{3}-\sqrt3$")],
  solution=[("a", [r"꽃잎 한 장: $-\frac\pi4\le\theta\le\frac\pi4,\ 0\le r\le2\cos2\theta$. 꽃잎 4장이 합동이고 한 장은 $x$축 대칭이라 $0\le\theta\le\frac\pi4$ 부분의 8배예요.",
                   r"넓이 $A$: $$\begin{aligned}&8\int_0^{\pi/4}\!\!\int_0^{2\cos2\theta}r\,dr\,d\theta\\&=8\int_0^{\pi/4}2\cos^22\theta\,d\theta\\&=8\int_0^{\pi/4}(1+\cos4\theta)\,d\theta=8\cdot\frac\pi4=2\pi\end{aligned}$$"]),
            ("b", [r"교점: $2\cos2\theta=1 \Rightarrow \theta=\pm\frac\pi6$ (오른쪽 꽃잎). 꽃잎 안에서 $|\theta|\le\frac\pi6$ 이면 원이 안쪽($r\le1$), $\frac\pi6\le|\theta|\le\frac\pi4$ 이면 장미곡선이 안쪽($r\le2\cos2\theta$)",
                   r"꽃잎 한 장에서: $$\begin{aligned}&\int_{-\pi/6}^{\pi/6}\!\!\int_0^1r\,dr\,d\theta\\&\quad+2\int_{\pi/6}^{\pi/4}\!\!\int_0^{2\cos2\theta}r\,dr\,d\theta\\&=\frac\pi6+2\int_{\pi/6}^{\pi/4}(1+\cos4\theta)\,d\theta\\&=\frac\pi6+2\Big(\frac\pi{12}-\frac{\sqrt3}{8}\Big)=\frac\pi3-\frac{\sqrt3}{4}\end{aligned}$$",
                   r"꽃잎 4장이 합동이므로 $4\Big(\dfrac\pi3-\dfrac{\sqrt3}4\Big)=\dfrac{4\pi}3-\sqrt3$"])],
  check=_c)


def _c():
    xs, ys = s**2*t, s + t
    pt = {s: 1, t: 2}
    assert xs.subs(pt) == 2 and ys.subs(pt) == 3
    ws = -1*diff(xs, s).subs(pt) + 4*diff(ys, s).subs(pt)
    wt = -1*diff(xs, t).subs(pt) + 4*diff(ys, t).subs(pt)
    assert ws == 0 and wt == 3
    ft = -(x - 2) + 4*(y - 3) + (x - 2)**2*(y - 3)   # f_x(2,3)=-1, f_y(2,3)=4 인 함수로도 확인
    W = ft.subs({x: xs, y: ys})
    assert diff(W, s).subs(pt) == 0 and diff(W, t).subs(pt) == 3
    F = x*z + y*exp(z) - 2
    P0 = {x: 1, y: 2, z: 0}
    assert F.subs(P0) == 0
    zx, zy = (-diff(F, x)/diff(F, z)).subs(P0), (-diff(F, y)/diff(F, z)).subs(P0)
    assert zx == 0 and zy == -R(1, 3)
    assert zx*R(3, 100) + zy*R(-6, 100) == R(2, 100)
    root = mp.findroot(lambda q: mp.mpf('1.03')*q + mp.mpf('1.94')*mp.e**q - 2, 0.02)
    assert abs(root - mp.mpf('0.02')) < 1e-3
Q(SB, id="q5", no="5", type="연쇄법칙 (합성함수 · 음함수)", ref="14.5 · 14.4", mins=7, topics=[12],
  types=["14-chain", "14-implicit", "14-tangent"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$f$ 는 미분가능하고 $f_x(2,3)=-1,\ f_y(2,3)=4$ 이다. $w=f(s^2t,\ s+t)$ 일 때 $(s,t)=(1,2)$ 에서 $\dfrac{\partial w}{\partial s},\ \dfrac{\partial w}{\partial t}$ 를 구하시오. [4점]"),
         ("b", r"방정식 $xz+y\,e^{z}=2$ 가 점 $(1,2,0)$ 근처에서 $z=z(x,y)$ 를 정한다. 양변을 $x,\ y$ 에 대해 연쇄법칙으로 미분하여 $z_x(1,2),\ z_y(1,2)$ 를 구하시오. [4점]"),
         ("c", r"(b)의 결과와 선형근사를 이용하여 $z(1.03,\ 1.94)$ 의 근삿값을 구하시오. [2점]")],
  answer=[("a", r"$\dfrac{\partial w}{\partial s}=0,\ \ \dfrac{\partial w}{\partial t}=3$"),
          ("b", r"$z_x(1,2)=0,\ \ z_y(1,2)=-\dfrac13$"),
          ("c", r"$0.02$")],
  solution=[("a", [r"$x=s^2t,\ y=s+t$: $(s,t)=(1,2)$ 이면 $(x,y)=(2,3)$, $\ x_s=2st=4,\ x_t=s^2=1,\ y_s=y_t=1$",
                   r"$w_s=f_x\,x_s+f_y\,y_s=(-1)(4)+4(1)=0$,  $w_t=f_x\,x_t+f_y\,y_t=(-1)(1)+4(1)=3$"]),
            ("b", [r"$x$ 로 미분 ($z$ 는 $x,y$ 의 함수): $z+x\,z_x+y\,e^{z}z_x=0 \Rightarrow z_x=-\dfrac{z}{x+ye^z}$",
                   r"$y$ 로 미분: $x\,z_y+e^z+y\,e^zz_y=0 \Rightarrow z_y=-\dfrac{e^z}{x+ye^z}$",
                   r"$(1,2,0)$ 에서 $x+ye^z=3$ → $z_x=0,\ z_y=-\dfrac13$ (공식 $z_x=-F_x/F_z,\ z_y=-F_y/F_z$ 와 같아요)"]),
            ("c", [r"$z\approx z(1,2)+z_x(1,2)(x-1)+z_y(1,2)(y-2)=0+0\cdot0.03-\dfrac13(-0.06)=0.02$"])],
  check=_c)


def _c():
    F = (x**2*y, x*y)
    I1 = line_int(F, (2*t, 0*t), 0, 1, vs=(x, y))
    I2 = line_int(F, (2 + 0*t, t), 0, 1, vs=(x, y))
    I3 = line_int(F, (2 - 2*t, 1 - t), 0, 1, vs=(x, y))
    assert I1 == 0 and I2 == 1 and I3 == -R(8, 3) and I1 + I2 + I3 == -R(5, 3)
    assert integrate(x**3/2 + x**2/4, (x, 2, 0)) == -R(8, 3)
    curl = diff(F[1], x) - diff(F[0], y)
    assert simplify(curl - (y - x**2)) == 0
    assert integrate(curl, (y, 0, x/2), (x, 0, 2)) == -R(5, 3)
Q(SB, id="q6", no="6", type="그린 정리 · 곡선 나누어 직접 계산", ref="16.2 · 16.4", mins=9, topics=[9],
  types=["16-vector", "16-green"],
  stem=r"$C$ 는 세 점 $(0,0),\ (2,0),\ (2,1)$ 을 꼭짓점으로 하는 삼각형의 경계이고, 양의 방향이다. $\displaystyle I=\oint_C x^2y\,dx+xy\,dy$ 에 대하여",
  parts=[("a", r"$C$ 를 세 선분으로 나누어 $I$ 를 직접 계산하시오. [5점]"),
         ("b", r"그린 정리를 이용해 $I$ 를 계산하시오. [5점]")],
  answer=[("a", r"$-\dfrac53$"), ("b", r"$-\dfrac53$")],
  solution=[("a", [r"양의 방향(반시계): $C_1:(0,0)\to(2,0)$, $\ C_2:(2,0)\to(2,1)$, $\ C_3:(2,1)\to(0,0)$",
                   r"$C_1$: $y=0,\ dy=0$ → $0$.  $C_2$: $x=2,\ dx=0$ → $\displaystyle\int_0^1 2y\,dy=1$",
                   r"$C_3$: 직선 $y=\frac x2$ 위를 $x:2\to0$, $\ dy=\frac12dx$ → $$\int_2^0\Big(\frac{x^3}{2}+\frac{x^2}{4}\Big)dx=-\Big(2+\frac23\Big)=-\frac83$$",
                   r"$I=0+1-\dfrac83=-\dfrac53$"]),
            ("b", [r"$P=x^2y,\ Q=xy$ → $Q_x-P_y=y-x^2$, $\ D:\ 0\le x\le2,\ 0\le y\le\frac x2$",
                   r"$$\begin{aligned}I&=\int_0^2\!\!\int_0^{x/2}(y-x^2)\,dy\,dx\\&=\int_0^2\Big(\frac{x^2}{8}-\frac{x^3}{2}\Big)dx=\frac13-2=-\frac53\end{aligned}$$ — (a)와 같아요."])],
  check=_c)


def _c():
    rr = Matrix([exp(t)*cos(t), exp(t)*sin(t), exp(t)])
    vt = rr.diff(t)
    assert simplify(vt.dot(vt) - 3*exp(2*t)) == 0
    assert EQ(integrate(sqrt(3)*exp(t), (t, 0, log(3))), 2*sqrt(3))
    assert EQ(simplify(vt[2] / (sqrt(3)*exp(t))), 1/sqrt(3))
    assert simplify(rr.diff(t, 2) - exp(t)*Matrix([-2*sin(t), 2*cos(t), 1])) == Matrix([0, 0, 0])
    v0, a0 = vt.subs(t, 0), rr.diff(t, 2).subs(t, 0)
    assert v0 == Matrix([1, 1, 1]) and a0 == Matrix([0, 2, 1])
    proj = (a0.dot(v0) / v0.dot(v0)) * v0
    assert proj == Matrix([1, 1, 1]) and a0 - proj == Matrix([-1, 1, 0]) and (a0 - proj).dot(v0) == 0
Q(SB, id="q7", no="7", type="곡선의 길이 · 사영(comp·proj)", ref="13.3 · 12.3 · 13.2", mins=7, topics=[11, 13],
  types=["13-arc", "12-proj", "13-motion"],
  stem=r"곡선 $\mathbf r(t)=\langle e^t\cos t,\ e^t\sin t,\ e^t\rangle$ 에 대하여",
  parts=[("a", r"$0\le t\le\ln3$ 부분의 길이를 구하시오. [4점]"),
         ("b", r"모든 $t$ 에서 $\operatorname{comp}_{\mathbf r'(t)}\mathbf k$ 가 일정함을 보이고 그 값을 구하시오. (즉, 접선과 $z$축 사이의 각이 일정하다.) [3점]"),
         ("c", r"$\mathbf r''(0)$ 을 $\operatorname{proj}_{\mathbf r'(0)}\mathbf r''(0)$ 과 $\mathbf r'(0)$ 에 수직인 벡터의 합으로 나타내시오. [3점]")],
  answer=[("a", r"$2\sqrt3$"),
          ("b", r"$\dfrac{1}{\sqrt3}$"),
          ("c", r"$\langle0,2,1\rangle=\langle1,1,1\rangle+\langle-1,1,0\rangle$")],
  solution=[("a", [r"$\mathbf r'(t)=e^t\langle\cos t-\sin t,\ \sin t+\cos t,\ 1\rangle$",
                   r"$|\mathbf r'(t)|^2=e^{2t}\big[(\cos t-\sin t)^2+(\sin t+\cos t)^2+1\big]=e^{2t}(2+1)$ → $|\mathbf r'(t)|=\sqrt3\,e^t$",
                   r"$L=\displaystyle\int_0^{\ln3}\sqrt3\,e^t\,dt=\sqrt3\,(3-1)=2\sqrt3$"]),
            ("b", [r"$\operatorname{comp}_{\mathbf r'}\mathbf k=\dfrac{\mathbf k\cdot\mathbf r'}{|\mathbf r'|}=\dfrac{e^t}{\sqrt3\,e^t}=\dfrac1{\sqrt3}$ — $t$ 와 무관한 상수",
                   r"$\mathbf k$ 가 단위벡터라 이 값이 곧 접선과 $z$축 사잇각의 코사인이에요: $\cos\alpha=\frac1{\sqrt3}$"]),
            ("c", [r"$\mathbf r''(t)=e^t\langle-2\sin t,\ 2\cos t,\ 1\rangle$ → $\mathbf r''(0)=\langle0,2,1\rangle$, $\ \mathbf r'(0)=\langle1,1,1\rangle$",
                   r"$\operatorname{proj}_{\mathbf r'(0)}\mathbf r''(0)=\dfrac{0+2+1}{3}\langle1,1,1\rangle=\langle1,1,1\rangle$, 수직 성분 $\langle0,2,1\rangle-\langle1,1,1\rangle=\langle-1,1,0\rangle$",
                   r"(확인: $\langle-1,1,0\rangle\cdot\langle1,1,1\rangle=0$) → $\mathbf r''(0)=\langle1,1,1\rangle+\langle-1,1,0\rangle$"])],
  check=_c)


def _c():
    f = x**2*y - x**2 - 2*y**2
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    assert sorted((c[x], c[y]) for c in crit) == [(-2, 1), (0, 0), (2, 1)]
    fxx, fyy, fxy = diff(f, x, 2), diff(f, y, 2), diff(f, x, y)
    D = fxx*fyy - fxy**2
    assert D.subs({x: 0, y: 0}) == 8 and fxx.subs({x: 0, y: 0}) == -2 and f.subs({x: 0, y: 0}) == 0
    assert D.subs({x: 2, y: 1}) == -16 and D.subs({x: -2, y: 1}) == -16
    lam = symbols('lam', real=True)
    h, g = x**2 + x*y + y**2, x**2 + y**2
    sols = solve([diff(h, x) - lam*diff(g, x), diff(h, y) - lam*diff(g, y), g - 2], [x, y, lam], dict=True)
    assert sorted(set(h.subs(q) for q in sols)) == [1, 3]
    assert sorted((q[x], q[y]) for q in sols if h.subs(q) == 3) == [(-1, -1), (1, 1)]
    assert sorted((q[x], q[y]) for q in sols if h.subs(q) == 1) == [(-1, 1), (1, -1)]
Q(SB, id="q8", no="8", type="2계 도함수 판정법 · 라그랑주 승수법", ref="14.7 · 14.8", mins=9, topics=[15, 2],
  types=["14-crit", "14-lagrange"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$f(x,y)=x^2y-x^2-2y^2$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"),
         ("b", r"라그랑주 승수법으로 원 $x^2+y^2=2$ 위에서 $h(x,y)=x^2+xy+y^2$ 의 최댓값과 최솟값을 구하시오. [5점]")],
  answer=[("a", r"$(0,0)$: 극댓값 $0$,  $(2,1),\ (-2,1)$: 안장점"),
          ("b", r"최댓값 $3$ (점 $(1,1),\ (-1,-1)$), 최솟값 $1$ (점 $(1,-1),\ (-1,1)$)")],
  solution=[("a", [r"$f_x=2xy-2x=2x(y-1)=0,\ \ f_y=x^2-4y=0$",
                   r"$x=0$ 이면 $y=0$ → $(0,0)$.  $y=1$ 이면 $x^2=4$ → $(\pm2,1)$",
                   r"$f_{xx}=2y-2,\ f_{yy}=-4,\ f_{xy}=2x$, $\ D=-4(2y-2)-4x^2$",
                   r"$(0,0)$: $D=8>0,\ f_{xx}=-2<0$ → 극댓값 $f(0,0)=0$.  $(\pm2,1)$: $D=0-16=-16<0$ → 안장점"]),
            ("b", [r"$g=x^2+y^2$, $\ \nabla h=\lambda\nabla g$: $2x+y=2\lambda x,\ \ x+2y=2\lambda y$",
                   r"두 식을 빼면 $(x-y)(1-2\lambda)=0$, 더하면 $(x+y)(3-2\lambda)=0$. $x=y=0$ 은 원 위에 없으므로 $\lambda=\frac32$ 이고 $x=y$, 또는 $\lambda=\frac12$ 이고 $x=-y$",
                   r"$x=y$: $2x^2=2$ → $(1,1),\ (-1,-1)$, $\ h=3$.  $x=-y$: $(1,-1),\ (-1,1)$, $\ h=1$",
                   r"최댓값 $3$, 최솟값 $1$"])],
  check=_c)


def _c():
    assert EQ(integrate(exp(x**2), (y, 0, 2*x), (x, 0, 1)), E - 1)
    num = nquad(lambda Y: mp.quad(lambda X: mp.e**(X*X), [Y/2, 1]), 0, 2)
    assert abs(num - (mp.e - 1)) < 1e-10
    assert EQ(integrate(6*sin(x**3), (z, 0, y), (y, 0, x), (x, 0, 1)), 1 - cos(1))
    # 원래 순서: z 를 바깥에 둔 채 안쪽 dx dy 를 수치로 (안쪽 dx 는 z 와 무관하니 y 에 대한 함수로 미리 계산)
    inner_x = lambda Y: mp.quad(lambda X: 6*mp.sin(X**3), [Y, 1])
    numb = nquad(lambda Y: inner_x(Y) * Y, 0, 1)   # ∫_0^1 (∫_0^y dz) · ∫_y^1 6sin(x^3) dx dy
    assert abs(numb - (1 - mp.cos(1))) < 1e-10
Q(SB, id="q9", no="9", type="적분 순서 바꾸기 (이중·삼중)", ref="15.2 · 15.6", mins=7, topics=[8],
  types=["15-order", "15-order3"],
  stem=r"적분 순서를 바꾸어 다음 값을 구하시오.",
  parts=[("a", r"$\displaystyle\int_0^2\!\!\int_{y/2}^1 e^{x^2}\,dx\,dy$ [4점]"),
         ("b", r"$\displaystyle\int_0^1\!\!\int_z^1\!\!\int_y^1 6\sin(x^3)\,dx\,dy\,dz$ [6점]")],
  answer=[("a", r"$e-1$"), ("b", r"$1-\cos1$")],
  solution=[("a", [r"영역: $0\le y\le2,\ \frac y2\le x\le1$ → $0\le x\le1,\ 0\le y\le2x$",
                   r"$$\begin{aligned}\int_0^1\!\!\int_0^{2x}e^{x^2}\,dy\,dx&=\int_0^12x\,e^{x^2}\,dx\\&=\Big[e^{x^2}\Big]_0^1=e-1\end{aligned}$$"]),
            ("b", [r"$\sin(x^3)$ 은 $x$ 로 바로 적분할 수 없으니 $x$ 를 가장 바깥으로 보내요.",
                   r"영역: $0\le z\le1,\ z\le y\le1,\ y\le x\le1$, 즉 $0\le z\le y\le x\le1$ → $0\le x\le1,\ 0\le y\le x,\ 0\le z\le y$",
                   r"$$\begin{aligned}&\int_0^1\!\!\int_0^x\!\!\int_0^y6\sin(x^3)\,dz\,dy\,dx\\&=\int_0^16\sin(x^3)\cdot\frac{x^2}{2}\,dx\\&=\Big[-\cos(x^3)\Big]_0^1=1-\cos1\end{aligned}$$"])],
  check=_c)


def _c():
    assert EQ(integrate(r, (z, 0, r), (r, 0, 2*cos(th)), (th, -pi/2, pi/2)), R(32, 9))
    num = nquad(lambda X: mp.quad(lambda Y: mp.sqrt(X*X + Y*Y), [-mp.sqrt(2*X - X*X), mp.sqrt(2*X - X*X)]), 0, 2)
    assert abs(num - mp.mpf(32)/9) < 1e-8
    assert EQ(integrate(cos(th)**3, (th, -pi/2, pi/2)), R(4, 3))
    assert EQ(integrate(rho**3*cos(ph)*sin(ph), (rho, 1, 2), (ph, 0, pi/6), (th, 0, 2*pi)), 15*pi/16)
    assert EQ(atan(1/sqrt(3)), pi/6)
Q(SB, id="q10", no="10", type="원주좌표 · 구면좌표 삼중적분", ref="15.7 · 15.8", mins=9, topics=[5, 6],
  types=["15-cyl", "15-sph"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"원기둥 $x^2+y^2=2x$ 의 내부에 있고 원뿔 $z=\sqrt{x^2+y^2}$ 의 아래, $xy$ 평면의 위에 있는 입체의 부피를 원주좌표로 구하시오. [5점]"),
         ("b", r"두 구면 $x^2+y^2+z^2=1,\ x^2+y^2+z^2=4$ 사이에 있고 원뿔 $z=\sqrt3\,\sqrt{x^2+y^2}$ 의 위쪽에 있는 입체를 $E$ 라 할 때, 구면좌표로 $\displaystyle\iiint_E z\,dV$ 를 구하시오. [5점]")],
  answer=[("a", r"$\dfrac{32}{9}$"), ("b", r"$\dfrac{15\pi}{16}$")],
  solution=[("a", [r"$x^2+y^2=2x \iff r=2\cos\theta\ \big(-\frac\pi2\le\theta\le\frac\pi2\big)$, 높이 $0\le z\le r$",
                   r"$$\begin{aligned}V&=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}\!\!\int_0^r r\,dz\,dr\,d\theta\\&=\int_{-\pi/2}^{\pi/2}\frac{8\cos^3\theta}{3}\,d\theta=\frac83\cdot\frac43=\frac{32}{9}\end{aligned}$$",
                   r"$\displaystyle\int_{-\pi/2}^{\pi/2}\cos^3\theta\,d\theta=\Big[\sin\theta-\frac{\sin^3\theta}{3}\Big]_{-\pi/2}^{\pi/2}=\frac43$"]),
            ("b", [r"원뿔 $z=\sqrt3\,r$: $\tan\phi=\dfrac rz=\dfrac1{\sqrt3}$ → $\phi=\dfrac\pi6$. 원뿔의 위쪽이므로 $0\le\phi\le\frac\pi6$, $\ 1\le\rho\le2$",
                   r"$$\begin{aligned}&\iiint_Ez\,dV\\&=\int_0^{2\pi}\!\!\int_0^{\pi/6}\!\!\int_1^2\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta\\&=2\pi\cdot\Big[\frac{\sin^2\phi}{2}\Big]_0^{\pi/6}\cdot\Big[\frac{\rho^4}{4}\Big]_1^2\\&=2\pi\cdot\frac18\cdot\frac{15}{4}=\frac{15\pi}{16}\end{aligned}$$"])],
  check=_c)

SETS.append({"id": "b", "no": 2, "label": "B", "title": "모의고사 B세트", "focus": "15개 주제 · 10문항 · 각 10점",
             "lead": "같은 15개 주제를 다른 조합으로 묶은 두 번째 세트예요. 교수님이 예고한 일변수 증분식 유도로 시작해서 그래디언트와 접평면, 평행사변형 변수변환, 장미곡선과 원의 공통부분, 합성함수·음함수 연쇄법칙, 삼각형 위 그린 정리(두 방법), 곡선의 길이와 사영, 극값 판정과 라그랑주, 이중·삼중 적분 순서, 원주·구면좌표를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
             "problems": SB})


# ════════════════════════════════════════════════════════════════════
# C세트
# ════════════════════════════════════════════════════════════════════
SC = []


def _c():
    T = symbols('T', real=True)
    rr = Matrix([exp(T), exp(-T), sqrt(2)*T])
    vt = rr.diff(T)
    assert simplify(vt.dot(vt) - (exp(T) + exp(-T))**2) == 0
    assert EQ(integrate(exp(T) + exp(-T), (T, 0, 1)), E - 1/E)
    num = nquad(lambda q: mp.sqrt(mp.e**(2*q) + mp.e**(-2*q) + 2), 0, 1)
    assert abs(num - (mp.e - 1/mp.e)) < 1e-12
    f = x**2*y + y*z + z**2
    comp = f.subs({x: rr[0], y: rr[1], z: rr[2]}, simultaneous=True)
    assert simplify(comp - (exp(T) + sqrt(2)*T*exp(-T) + 2*T**2)) == 0
    assert EQ(diff(comp, T).subs(T, 0), 1 + sqrt(2))
    g = grad(f, (x, y, z)).subs({x: 1, y: 1, z: 0})
    assert list(g) == [2, 1, 1]
    v0 = vt.subs(T, 0)
    assert list(v0) == [1, -1, sqrt(2)] and EQ(v0.norm(), 2)
    assert EQ(g.dot(v0), 1 + sqrt(2)) and EQ(g.dot(v0) / v0.norm(), (1 + sqrt(2))/2)
Q(SC, id="q1", no="1", type="곡선의 길이 · 연쇄법칙", ref="13.3 · 14.5 · 14.6", mins=7, topics=[11, 12],
  types=["13-arc", "14-chain", "14-dir"],
  stem=r"곡선 $\mathbf r(t)=\langle e^t,\ e^{-t},\ \sqrt2\,t\rangle$ 와 함수 $f(x,y,z)=x^2y+yz+z^2$ 에 대하여",
  parts=[("a", r"$0\le t\le1$ 부분의 길이를 구하시오. [4점]"),
         ("b", r"점이 곡선을 따라 움직일 때 $t=0$ 에서 $\dfrac{d}{dt}f(\mathbf r(t))$ 를 연쇄법칙으로 구하시오. [3점]"),
         ("c", r"$\mathbf r(0)$ 에서 곡선의 단위접선벡터 $\mathbf T(0)$ 방향으로의 $f$ 의 방향도함수를 구하시오. [3점]")],
  answer=[("a", r"$e-\dfrac1e$"), ("b", r"$1+\sqrt2$"), ("c", r"$\dfrac{1+\sqrt2}{2}$")],
  solution=[("a", [r"$\mathbf r'(t)=\langle e^t,\ -e^{-t},\ \sqrt2\rangle$, $\ |\mathbf r'(t)|^2=e^{2t}+e^{-2t}+2=\big(e^t+e^{-t}\big)^2$ → $|\mathbf r'(t)|=e^t+e^{-t}$ (완전제곱이 되는지 먼저 보기)",
                   r"$$\begin{aligned}L&=\int_0^1\big(e^t+e^{-t}\big)\,dt=\Big[e^t-e^{-t}\Big]_0^1\\&=e-\frac1e\end{aligned}$$"]),
            ("b", [r"$\mathbf r(0)=(1,1,0)$, $\ \mathbf r'(0)=\langle1,\ -1,\ \sqrt2\rangle$",
                   r"$\nabla f=\langle 2xy,\ x^2+z,\ y+2z\rangle$ → $\nabla f(1,1,0)=\langle2,\ 1,\ 1\rangle$",
                   r"$\dfrac{d}{dt}f(\mathbf r(t))\Big|_{t=0}=\nabla f(1,1,0)\cdot\mathbf r'(0)=2-1+\sqrt2=1+\sqrt2$ (확인: $f(\mathbf r(t))=e^t+\sqrt2\,te^{-t}+2t^2$ 을 미분해도 같아요)"]),
            ("c", [r"$|\mathbf r'(0)|=e^0+e^0=2$ → $\mathbf T(0)=\dfrac{\mathbf r'(0)}{|\mathbf r'(0)|}=\dfrac12\langle1,\ -1,\ \sqrt2\rangle$",
                   r"$D_{\mathbf T}f=\nabla f(1,1,0)\cdot\mathbf T(0)=\dfrac{1+\sqrt2}{2}$ — (b)의 변화율을 속력 $2$ 로 나눈 값이에요."])],
  check=_c)


def _c():
    J = Matrix([[diff(x + y, x), diff(x + y, y)], [diff(y - 2*x, x), diff(y - 2*x, y)]]).det()
    assert J == 3
    xs, ys = (u - v)/3, (2*u + v)/3
    assert simplify(xs + ys - u) == 0 and simplify(ys - 2*xs - v) == 0
    Jinv = Matrix([[diff(xs, u), diff(xs, v)], [diff(ys, u), diff(ys, v)]]).det()
    assert Jinv == R(1, 3)
    val = integrate(v*exp(u) * R(1, 3), (v, 0, 3), (u, 1, 4))
    assert EQ(val, R(3, 2)*(exp(4) - E))
    # 원래 xy 영역(평행사변형)에서 수치적분: x∈[-2/3,1/3] 은 1-x ≤ y ≤ 2x+3, x∈[1/3,4/3] 은 2x ≤ y ≤ 4-x
    lo = lambda X: 1 - X if X <= mp.mpf(1)/3 else 2*X
    hi = lambda X: 2*X + 3 if X <= mp.mpf(1)/3 else 4 - X
    num = mp.quad(lambda X: mp.quad(lambda Y: (Y - 2*X)*mp.e**(X + Y), [lo(X), hi(X)]),
                  [-mp.mpf(2)/3, mp.mpf(1)/3, mp.mpf(4)/3])
    assert abs(num - mp.mpf(3)/2*(mp.e**4 - mp.e)) < 1e-8
Q(SC, id="q2", no="2", type="변수변환 (야코비안)", ref="15.9", mins=8, topics=[7],
  types=["15-change"],
  stem=r"$R$ 은 네 직선 $x+y=1,\ x+y=4,\ y-2x=0,\ y-2x=3$ 으로 둘러싸인 평행사변형이다. 변환 $u=x+y,\ v=y-2x$ 를 이용하여",
  parts=[("a", r"야코비안 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"),
         ("b", r"$\displaystyle\iint_R(y-2x)\,e^{x+y}\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac13$, $\ S=\{(u,v)\mid1\le u\le4,\ 0\le v\le3\}$"),
          ("b", r"$\dfrac32\big(e^4-e\big)$")],
  solution=[("a", [r"$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&1\\-2&1\end{vmatrix}=1+2=3$$ 이므로 $\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac13$ (역변환 $x=\frac{u-v}{3},\ y=\frac{2u+v}{3}$ 으로 직접 계산해도 같아요)",
                   r"네 직선이 $u=1,\ u=4,\ v=0,\ v=3$ 이 되어 $S:\ 1\le u\le4,\ 0\le v\le3$ (직사각형)"]),
            ("b", [r"피적분함수 $(y-2x)e^{x+y}=v\,e^u$, $\ dA=\Big|\dfrac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv=\dfrac13\,du\,dv$",
                   r"$$\begin{aligned}&\iint_R(y-2x)e^{x+y}\,dA\\&=\frac13\int_1^4\!\!\int_0^3v\,e^u\,dv\,du\\&=\frac13\cdot\frac92\cdot\big(e^4-e\big)=\frac32\big(e^4-e\big)\end{aligned}$$"])],
  check=_c)


def _c():
    m, k = symbols('m k', real=True)
    f1 = x*y/(x**2 + x*y + y**2)
    assert simplify(f1.subs(y, m*x) - m/(1 + m + m**2)) == 0
    assert (m/(1 + m + m**2)).subs(m, 0) == 0 and (m/(1 + m + m**2)).subs(m, 1) == R(1, 3)
    f2 = 2*x*y**3/(x**2 + y**6)
    assert limit(f2.subs(y, m*x), x, 0) == 0 and f2.subs(x, 0) == 0
    assert simplify(f2.subs(x, k*y**3) - 2*k/(k**2 + 1)) == 0
    assert simplify(f2.subs(x, y**3)) == 1
    g = (x**3 + y**3)/(x**2 + y**2)
    rp = symbols('rp', positive=True)
    gp = simplify(g.subs({x: rp*cos(th), y: rp*sin(th)}))
    assert simplify(gp - rp*(cos(th)**3 + sin(th)**3)) == 0
    assert max(abs(mp.cos(a)**3 + mp.sin(a)**3) for a in mp.linspace(0, 2*mp.pi, 721)) <= 2
    h = symbols('h', nonzero=True, real=True)
    assert simplify(g.subs({x: h, y: 0})) == h and simplify(g.subs({x: 0, y: h})) == h
    assert limit(g.subs({x: h, y: 0})/h, h, 0) == 1 and limit(g.subs({x: 0, y: h})/h, h, 0) == 1
Q(SC, id="q3", no="3", type="극한의 존재성 · 연속 · 편도함수", ref="14.2 · 14.3", mins=8, topics=[3, 10],
  types=["14-dne", "14-limit", "14-defpartial"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy}{x^2+xy+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{2xy^3}{x^2+y^6}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("c", r"$g(x,y)=\dfrac{x^3+y^3}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $\ g(0,0)=0$ 일 때, $g$ 가 원점에서 연속임을 보이고 편도함수의 정의를 이용해 $g_x(0,0),\ g_y(0,0)$ 을 구하시오. [4점]")],
  answer=[("a", r"존재하지 않음 (직선 $y=mx$ 를 따라 $\dfrac{m}{1+m+m^2}$: $x$축에서 $0$, $y=x$ 에서 $\frac13$)"),
          ("b", r"존재하지 않음 (직선을 따라서는 모두 $0$, 곡선 $x=y^3$ 을 따라 $1$)"),
          ("c", r"연속, $\ g_x(0,0)=1,\ g_y(0,0)=1$")],
  solution=[("a", [r"직선 $y=mx\ (x\ne0)$ 를 따라가면 $$\frac{mx^2}{x^2+mx^2+m^2x^2}=\frac{m}{1+m+m^2}$$ 으로 기울기 $m$ 에 따라 값이 달라요.",
                   r"$x$축($m=0$)에서는 $0$, 직선 $y=x$($m=1$)에서는 $\frac13$ → 극한은 존재하지 않아요."]),
            ("b", [r"직선 $y=mx$: $\dfrac{2m^3x^4}{x^2+m^6x^6}=\dfrac{2m^3x^2}{1+m^6x^4}\to0$, $\ y$축 위에서도 $0$ → 직선만으로는 판정이 안 돼요.",
                   r"분모의 $x^2$ 과 $y^6$ 의 차수를 맞추는 곡선 $x=y^3$ 을 따라가면 $\dfrac{2y^6}{y^6+y^6}=1\to1$",
                   r"경로에 따라 값($0$ 과 $1$)이 다르므로 극한은 존재하지 않아요. (일반적으로 곡선 $x=ky^3$ 을 따라 $\frac{2k}{k^2+1}$)"]),
            ("c", [r"극좌표 $x=r\cos\theta,\ y=r\sin\theta$: $\ |g|=r\,|\cos^3\theta+\sin^3\theta|\le2r\to0=g(0,0)$ → 원점에서 연속",
                   r"$g(h,0)=\dfrac{h^3}{h^2}=h$ → $g_x(0,0)=\displaystyle\lim_{h\to0}\frac{g(h,0)-g(0,0)}{h}=\lim_{h\to0}\frac hh=1$",
                   r"같은 방법으로 $g(0,h)=h$ 이므로 $g_y(0,0)=1$"])],
  check=_c)


def _c():
    A = integrate(r, (r, 0, 2*cos(3*th)), (th, -pi/6, pi/6))
    assert EQ(A, pi/3)
    B = integrate(r**3, (r, 0, 2*cos(3*th)), (th, -pi/6, pi/6))
    assert EQ(B, pi/2)
    assert EQ(integrate(cos(u)**4, (u, -pi/2, pi/2)), 3*pi/8)
    assert EQ(2*cos(3*(pi/9)), 1)
    one = integrate((4*cos(3*th)**2 - 1)/2, (th, -pi/9, pi/9))
    assert EQ(one, pi/9 + sqrt(3)/6) and EQ(3*one, pi/3 + sqrt(3)/2)
    # 수치: 장미곡선 전체(θ∈[0,π])에서 max(r_rose,1) 바깥 부분
    num = mp.quad(lambda a: max((2*mp.cos(3*a))**2 - 1, 0)/2, mp.linspace(0, mp.pi, 19))
    assert abs(num - (mp.pi/3 + mp.sqrt(3)/2)) < 1e-10
    numB = mp.quad(lambda a: (2*mp.cos(3*a))**4/4, [-mp.pi/6, mp.pi/6])
    assert abs(numB - mp.pi/2) < 1e-12
Q(SC, id="q4", no="4", type="극좌표 이중적분 (장미곡선)", ref="15.3", mins=8, topics=[1],
  types=["15-polar"],
  stem=r"장미곡선 $r=2\cos3\theta$ (꽃잎 3장)에 대하여, 꽃잎 한 장 $\big(-\frac\pi6\le\theta\le\frac\pi6\big)$ 으로 둘러싸인 영역을 $D$ 라 하자.",
  parts=[("a", r"$D$ 의 넓이를 이중적분으로 구하시오. [3점]"),
         ("b", r"$\displaystyle\iint_D(x^2+y^2)\,dA$ 를 구하시오. [3점]"),
         ("c", r"장미곡선의 내부이면서 원 $r=1$ 의 외부인 영역(꽃잎 3장 전체)의 넓이를 구하시오. [4점]")],
  answer=[("a", r"$\dfrac\pi3$"), ("b", r"$\dfrac\pi2$"), ("c", r"$\dfrac\pi3+\dfrac{\sqrt3}{2}$")],
  solution=[("a", [r"$D:\ -\frac\pi6\le\theta\le\frac\pi6,\ 0\le r\le2\cos3\theta$, $\ dA=r\,dr\,d\theta$",
                   r"$$\begin{aligned}A&=\int_{-\pi/6}^{\pi/6}\!\!\int_0^{2\cos3\theta}r\,dr\,d\theta\\&=\int_{-\pi/6}^{\pi/6}2\cos^23\theta\,d\theta\\&=\int_{-\pi/6}^{\pi/6}(1+\cos6\theta)\,d\theta=\frac\pi3\end{aligned}$$"]),
            ("b", [r"$x^2+y^2=r^2$: $$\begin{aligned}\iint_D(x^2+y^2)\,dA&=\int_{-\pi/6}^{\pi/6}\!\!\int_0^{2\cos3\theta}r^3\,dr\,d\theta\\&=4\int_{-\pi/6}^{\pi/6}\cos^43\theta\,d\theta\end{aligned}$$",
                   r"$u=3\theta$ 로 치환하고 $\cos^4u=\dfrac38+\dfrac12\cos2u+\dfrac18\cos4u$: $$\frac43\int_{-\pi/2}^{\pi/2}\cos^4u\,du=\frac43\cdot\frac{3\pi}{8}=\frac\pi2$$"]),
            ("c", [r"교점: $2\cos3\theta=1 \Rightarrow 3\theta=\pm\frac\pi3 \Rightarrow \theta=\pm\frac\pi9$. 꽃잎 $D$ 에서 $|\theta|\le\frac\pi9$ 일 때 장미곡선이 원 바깥에 있어요.",
                   r"$$\begin{aligned}&\frac12\int_{-\pi/9}^{\pi/9}\big(4\cos^23\theta-1\big)\,d\theta\\&=\frac12\int_{-\pi/9}^{\pi/9}(1+2\cos6\theta)\,d\theta\\&=\frac12\Big(\frac{2\pi}{9}+\frac23\sin\frac{2\pi}{3}\Big)=\frac\pi9+\frac{\sqrt3}{6}\end{aligned}$$",
                   r"꽃잎 3장이 합동이므로 $3\Big(\dfrac\pi9+\dfrac{\sqrt3}6\Big)=\dfrac\pi3+\dfrac{\sqrt3}2$"])],
  check=_c)


def _c():
    assert solve((r**2) - (8 - r**2), r) in ([-2, 2], [2, -2])
    I1 = integrate(z*r, (z, r**2, 8 - r**2), (r, 0, 2), (th, 0, 2*pi))
    assert EQ(I1, 64*pi)
    num1 = mp.quad(lambda X: mp.quad(lambda Y: ((8 - X*X - Y*Y)**2 - (X*X + Y*Y)**2)/2,
                                     [-mp.sqrt(4 - X*X), mp.sqrt(4 - X*X)]), [-2, 2])
    assert abs(num1 - 64*mp.pi) < 1e-6
    I2 = integrate(rho**2*sin(ph), (rho, 0, 2*cos(ph)), (ph, 0, pi/4), (th, 0, 2*pi))
    assert EQ(I2, pi)
    # 원주좌표로 다시: 원뿔 z=r 과 구 r^2+(z-1)^2=1 은 r=1 에서 만나요
    I2c = integrate((1 + sqrt(1 - r**2) - r)*r, (r, 0, 1)) * 2*pi
    assert EQ(I2c, pi)
    num2 = 2*mp.pi*mp.quad(lambda q: (1 + mp.sqrt(1 - q*q) - q)*q, [0, 1])
    assert abs(num2 - mp.pi) < 1e-10
Q(SC, id="q5", no="5", type="원주좌표 · 구면좌표 삼중적분", ref="15.7 · 15.8", mins=9, topics=[5, 6],
  types=["15-cyl", "15-sph"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"두 포물면 $z=x^2+y^2$ 과 $z=8-x^2-y^2$ 으로 둘러싸인 입체를 $E$ 라 할 때, 원주좌표를 이용하여 $\displaystyle\iiint_Ez\,dV$ 를 구하시오. [5점]"),
         ("b", r"구 $x^2+y^2+z^2=2z$ 의 내부이고 원뿔 $z=\sqrt{x^2+y^2}$ 의 위쪽에 있는 입체의 부피를 구면좌표로 구하시오. [5점]")],
  answer=[("a", r"$64\pi$"), ("b", r"$\pi$")],
  solution=[("a", [r"두 곡면은 $r^2=8-r^2$, 즉 $r=2$ 에서 만나요. $E:\ 0\le\theta\le2\pi,\ 0\le r\le2,\ r^2\le z\le8-r^2$, $\ dV=r\,dz\,dr\,d\theta$",
                   r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^2\!\!\int_{r^2}^{8-r^2}z\,r\,dz\,dr\,d\theta\\&=2\pi\int_0^2\frac{(8-r^2)^2-r^4}{2}\,r\,dr\\&=\pi\int_0^2(64-16r^2)\,r\,dr\\&=\pi\Big[32r^2-4r^4\Big]_0^2=64\pi\end{aligned}$$"]),
            ("b", [r"구: $\rho^2=2\rho\cos\phi \Rightarrow \rho=2\cos\phi$.  원뿔 $z=r$: $\tan\phi=1 \Rightarrow \phi=\frac\pi4$, 그 위쪽이므로 $0\le\phi\le\frac\pi4$",
                   r"$$\begin{aligned}V&=\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^{2\cos\phi}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta\\&=2\pi\int_0^{\pi/4}\frac{8\cos^3\phi}{3}\sin\phi\,d\phi\\&=\frac{16\pi}{3}\Big[-\frac{\cos^4\phi}{4}\Big]_0^{\pi/4}\\&=\frac{16\pi}{3}\cdot\frac14\Big(1-\frac14\Big)=\pi\end{aligned}$$"])],
  check=_c)


def _c():
    lam = symbols('lam', real=True)
    F = (x - 1)**2 + (y - 2)**2 + (z + 1)**2
    G = 2*x - y + 2*z
    sol = solve([diff(F, x) - lam*diff(G, x), diff(F, y) - lam*diff(G, y), diff(F, z) - lam*diff(G, z), G - 16],
                [x, y, z, lam], dict=True)
    assert len(sol) == 1 and (sol[0][x], sol[0][y], sol[0][z], sol[0][lam]) == (5, 0, 3, 4)
    assert sqrt(F.subs(sol[0])) == 6
    # 평면 위 다른 점들과 비교 (매개화 x=a, y=b, z=(16-2a+b)/2)
    best = min(((a - 1)**2 + (b - 2)**2 + ((16 - 2*a + b)/2 + 1)**2, a, b)
               for a in [i/4 for i in range(0, 41)] for b in [j/4 for j in range(-20, 21)])
    assert abs(best[0] - 36) < 1e-9 and (best[1], best[2]) == (5, 0)
    n = Matrix([2, -1, 2])
    PQ = Matrix([1, 2, -1]) - Matrix([8, 0, 0])
    assert 2*8 == 16 and n.norm() == 3 and n.dot(PQ) == -18
    assert n.dot(PQ) / n.norm() == -6
    proj = (n.dot(PQ) / n.dot(n)) * n
    assert list(proj) == [-4, 2, -4]
    assert list(Matrix([1, 2, -1]) - proj) == [5, 0, 3]
    refl = Matrix([1, 2, -1]) - 2*proj
    assert list(refl) == [9, -2, 7]
    mid = (refl + Matrix([1, 2, -1])) / 2
    assert 2*mid[0] - mid[1] + 2*mid[2] == 16
Q(SC, id="q6", no="6", type="사영 · 라그랑주 승수법", ref="12.3 · 12.5 · 14.8", mins=8, topics=[13, 2],
  types=["14-lagrange", "12-proj", "12-dist"],
  stem=r"평면 $\Pi:\ 2x-y+2z=16$ 과 점 $Q(1,\ 2,\ -1)$ 에 대하여",
  parts=[("a", r"라그랑주 승수법으로 $\Pi$ 위에서 $Q$ 에 가장 가까운 점과 그 거리를 구하시오. [5점]"),
         ("b", r"$\Pi$ 위의 점 $P_0(8,0,0)$ 과 법선벡터 $\mathbf n=\langle2,-1,2\rangle$ 에 대하여 $\operatorname{comp}_{\mathbf n}\overrightarrow{P_0Q}$ 와 $\operatorname{proj}_{\mathbf n}\overrightarrow{P_0Q}$ 를 구하고, 이것으로 (a)의 결과를 확인하시오. [3점]"),
         ("c", r"평면 $\Pi$ 에 대하여 $Q$ 와 대칭인 점을 구하시오. [2점]")],
  answer=[("a", r"가장 가까운 점 $(5,\ 0,\ 3)$, 거리 $6$"),
          ("b", r"$\operatorname{comp}_{\mathbf n}\overrightarrow{P_0Q}=-6$, $\ \operatorname{proj}_{\mathbf n}\overrightarrow{P_0Q}=\langle-4,\ 2,\ -4\rangle$"),
          ("c", r"$(9,\ -2,\ 7)$")],
  solution=[("a", [r"거리의 제곱 $f=(x-1)^2+(y-2)^2+(z+1)^2$ 을 제약 $g=2x-y+2z=16$ 아래에서 최소화해요. $\nabla f=\lambda\nabla g$:",
                   r"$2(x-1)=2\lambda,\ \ 2(y-2)=-\lambda,\ \ 2(z+1)=2\lambda$ → $x=1+\lambda,\ y=2-\frac\lambda2,\ z=-1+\lambda$",
                   r"제약식에 대입: $2(1+\lambda)-\big(2-\frac\lambda2\big)+2(-1+\lambda)=16 \Rightarrow \frac92\lambda=18,\ \lambda=4$ → 점 $(5,0,3)$, 거리 $\sqrt{16+4+16}=6$ (평면 위에서 멀어질수록 $f$ 가 커지므로 이 점에서 최소)"]),
            ("b", [r"$\overrightarrow{P_0Q}=\langle-7,\ 2,\ -1\rangle$, $\ |\mathbf n|=3$, $\ \mathbf n\cdot\overrightarrow{P_0Q}=-14-2-2=-18$",
                   r"$\operatorname{comp}_{\mathbf n}\overrightarrow{P_0Q}=\dfrac{-18}{3}=-6$ → $Q$ 와 평면 사이의 거리는 $|-6|=6$",
                   r"$\operatorname{proj}_{\mathbf n}\overrightarrow{P_0Q}=\dfrac{-18}{9}\langle2,-1,2\rangle=\langle-4,\ 2,\ -4\rangle$ 는 평면에서 $Q$ 로 가는 수직 벡터예요. 가장 가까운 점은 $Q-\langle-4,2,-4\rangle=(5,0,3)$ → (a)와 같아요."]),
            ("c", [r"$Q$ 에서 평면까지 수직으로 $\langle4,-2,4\rangle$ 만큼 가면 $(5,0,3)$ 이므로, 한 번 더 가면 대칭점: $Q+2\langle4,-2,4\rangle=(9,\ -2,\ 7)$",
                   r"(확인: 중점 $(5,0,3)$ 이 평면 위에 있고 $\langle8,-4,8\rangle\parallel\mathbf n$)"])],
  check=_c)


def _c():
    P, Qf = x**2 - y**2, x*y
    c1 = integrate(P.subs(y, 0), (x, -1, 1))
    assert c1 == R(2, 3)
    integrand = (P.subs({x: t, y: 1 - t**2}) * 1 + Qf.subs({x: t, y: 1 - t**2}) * diff(1 - t**2, t))
    assert simplify(integrand - (t**4 + t**2 - 1)) == 0
    c2 = integrate(integrand, (t, 1, -1))
    assert c2 == R(14, 15) and c1 + c2 == R(8, 5)
    curl = diff(Qf, x) - diff(P, y)
    assert simplify(curl - 3*y) == 0
    assert integrate(3*y, (y, 0, 1 - x**2), (x, -1, 1)) == R(8, 5)
    assert integrate((1 - x**2)**2, (x, -1, 1)) == R(16, 15)
    num = mp.quad(lambda q: (q*q - (1 - q*q)**2) - 2*q*q*(1 - q*q), [1, -1]) + mp.mpf(2)/3
    assert abs(num - mp.mpf(8)/5) < 1e-12
    P2, Q2 = 2*x*y + exp(x), x**2 + cos(y)
    assert simplify(diff(Q2, x) - diff(P2, y)) == 0
    pot = x**2*y + exp(x) + sin(y)
    assert simplify(diff(pot, x) - P2) == 0 and simplify(diff(pot, y) - Q2) == 0
Q(SC, id="q7", no="7", type="그린 정리 · 곡선 나누어 직접 계산", ref="16.2 · 16.4", mins=9, topics=[9],
  types=["16-green", "16-vector", "16-conserv"],
  stem=r"$D$ 는 포물선 $y=1-x^2$ 과 $x$축으로 둘러싸인 영역이고, $C$ 는 $D$ 의 경계로 양의 방향(반시계 방향)이다. $\displaystyle I=\oint_C(x^2-y^2)\,dx+xy\,dy$ 에 대하여",
  parts=[("a", r"$C$ 를 선분과 포물선으로 나누어 $I$ 를 직접 계산하시오. [4점]"),
         ("b", r"그린 정리를 이용해 $I$ 를 계산하고 (a)와 같은지 확인하시오. [4점]"),
         ("c", r"같은 $C$ 에서 $\displaystyle\oint_C(2xy+e^x)\,dx+(x^2+\cos y)\,dy=0$ 인 이유를 그린 정리로 설명하시오. [2점]")],
  answer=[("a", r"$\dfrac85$"), ("b", r"$\dfrac85$"),
          ("c", r"$Q_x-P_y=2x-2x=0$ 이므로 $\displaystyle\oint_C=\iint_D0\,dA=0$")],
  solution=[("a", [r"양의 방향: $C_1$ 은 $x$축 위 선분 $(-1,0)\to(1,0)$, $C_2$ 는 포물선을 따라 $(1,0)\to(-1,0)$",
                   r"$C_1:\ y=0,\ dy=0$ → $\displaystyle\int_{C_1}=\int_{-1}^1x^2\,dx=\frac23$",
                   r"$C_2:\ x=t,\ y=1-t^2\ (t:1\to-1)$, $\ dy=-2t\,dt$: $$\begin{aligned}\int_{C_2}&=\int_1^{-1}\Big[t^2-(1-t^2)^2-2t^2(1-t^2)\Big]dt\\&=-\int_{-1}^1\big(t^4+t^2-1\big)\,dt\\&=-\Big(\frac25+\frac23-2\Big)=\frac{14}{15}\end{aligned}$$",
                   r"$I=\dfrac23+\dfrac{14}{15}=\dfrac{24}{15}=\dfrac85$"]),
            ("b", [r"$P=x^2-y^2,\ Q=xy$ → $Q_x-P_y=y-(-2y)=3y$, $\ D:\ -1\le x\le1,\ 0\le y\le1-x^2$",
                   r"$$\begin{aligned}I&=\iint_D3y\,dA=\int_{-1}^1\frac32(1-x^2)^2\,dx\\&=\frac32\cdot\frac{16}{15}=\frac85\end{aligned}$$ — (a)와 같아요."]),
            ("c", [r"$P=2xy+e^x,\ Q=x^2+\cos y$ 이면 $Q_x-P_y=2x-2x=0$",
                   r"그린 정리로 $\displaystyle\oint_C=\iint_D0\,dA=0$. ($\mathbf F=\nabla\big(x^2y+e^x+\sin y\big)$ 인 보존장이라 닫힌 곡선을 한 바퀴 돌면 $0$ 이에요.)"])],
  check=_c)


def _c():
    dx_, dy_ = symbols('dx dy', real=True)
    f = x*y**2
    fx, fy = diff(f, x).subs({x: 2, y: 1}), diff(f, y).subs({x: 2, y: 1})
    assert (fx, fy) == (1, 4) and f.subs({x: 2, y: 1}) == 2
    dz = expand(f.subs({x: 2 + dx_, y: 1 + dy_}) - 2)
    assert dz == expand(dx_ + 4*dy_ + 2*dy_**2 + 2*dx_*dy_ + dx_*dy_**2)
    e1, e2 = 2*dy_ + dy_**2, 2*dy_
    assert expand(fx*dx_ + fy*dy_ + e1*dx_ + e2*dy_ - dz) == 0
    assert e1.subs(dy_, 0) == 0 and e2.subs(dy_, 0) == 0
    L = 2 + fx*(x - 2) + fy*(y - 1)
    assert expand(L - (x + 4*y - 4)) == 0
    approx = L.subs({x: R(202, 100), y: R(97, 100)})
    assert approx == R(19, 10)
    assert abs(f.subs({x: R(202, 100), y: R(97, 100)}) - R(1900618, 1000000)) == 0
Q(SC, id="q8", no="8", type="미분가능성의 정의 · 접평면", ref="14.4", mins=8, topics=[4, 14],
  types=["14-differentiable", "14-tangent"],
  stem=r"$f(x,y)=xy^2$ 과 점 $(2,1)$ 에 대하여",
  parts=[("a", r"$\Delta z=f(2+\Delta x,\ 1+\Delta y)-f(2,1)$ 을 전개하여 $\Delta z=f_x(2,1)\Delta x+f_y(2,1)\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 를 만족하는 $\varepsilon_1,\ \varepsilon_2$ 를 찾고, 정의를 이용해 $f$ 가 $(2,1)$ 에서 미분가능함을 보이시오. [4점]<br>" + DEF7),
         ("b", r"곡면 $z=f(x,y)$ 위의 점 $(2,\ 1,\ 2)$ 에서의 접평면의 방정식을 구하시오. [3점]"),
         ("c", r"선형근사를 이용하여 $f(2.02,\ 0.97)$ 의 근삿값을 구하시오. [3점]")],
  answer=[("a", r"$\varepsilon_1=2\Delta y+(\Delta y)^2,\ \ \varepsilon_2=2\Delta y$ (둘 다 $\to0$) → 미분가능"),
          ("b", r"$z=x+4y-4$"), ("c", r"$1.9$")],
  solution=[("a", [r"$f_x=y^2,\ f_y=2xy$ → $f_x(2,1)=1,\ f_y(2,1)=4$",
                   r"$$\begin{aligned}\Delta z&=(2+\Delta x)(1+\Delta y)^2-2\\&=\Delta x+4\Delta y+2(\Delta y)^2\\&\quad+2\Delta x\Delta y+\Delta x(\Delta y)^2\end{aligned}$$",
                   r"$$\begin{aligned}\Delta z&=1\cdot\Delta x+4\Delta y\\&\quad+\underbrace{\big(2\Delta y+(\Delta y)^2\big)}_{\varepsilon_1}\Delta x+\underbrace{2\Delta y}_{\varepsilon_2}\Delta y\end{aligned}$$",
                   r"$(\Delta x,\Delta y)\to(0,0)$ 이면 $\varepsilon_1\to0,\ \varepsilon_2\to0$ 이므로 정의에 의해 $(2,1)$ 에서 **미분가능**해요. ($\varepsilon_1,\varepsilon_2$ 를 고르는 방법은 하나가 아니에요.)"]),
            ("b", [r"$z=f(2,1)+f_x(2,1)(x-2)+f_y(2,1)(y-1)=2+(x-2)+4(y-1)$",
                   r"정리하면 $z=x+4y-4$"]),
            ("c", [r"$L(x,y)=x+4y-4$ → $f(2.02,\ 0.97)\approx2.02+3.88-4=1.9$",
                   r"(실제 값 $2.02\times0.9409=1.900618$ — 오차 $\Delta z-dz=\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 가 아주 작아요)"])],
  check=_c)


def _c():
    f = x*y*(3 - x - y)
    fx, fy = diff(f, x), diff(f, y)
    assert simplify(fx - y*(3 - 2*x - y)) == 0 and simplify(fy - x*(3 - x - 2*y)) == 0
    crit = solve([fx, fy], [x, y], dict=True)
    pts = sorted((c[x], c[y]) for c in crit)
    assert pts == [(0, 0), (0, 3), (1, 1), (3, 0)]
    fxx, fyy, fxy = diff(f, x, 2), diff(f, y, 2), diff(f, x, y)
    Dd = lambda a, b: (fxx*fyy - fxy**2).subs({x: a, y: b})
    assert Dd(0, 0) == -9 and Dd(3, 0) == -9 and Dd(0, 3) == -9
    assert Dd(1, 1) == 3 and fxx.subs({x: 1, y: 1}) == -2 and f.subs({x: 1, y: 1}) == 1
    hyp = f.subs(y, 4 - x)
    assert expand(hyp + x*(4 - x)) == 0
    assert solve(diff(hyp, x), x) == [2] and hyp.subs(x, 2) == -4
    # 삼각형 격자 탐색
    vals = [(float(f.subs({x: R(i, 40), y: R(j, 40)})), i, j) for i in range(0, 161) for j in range(0, 161 - i)]
    assert abs(max(vals)[0] - 1) < 1e-12 and abs(min(vals)[0] + 4) < 1e-12
Q(SC, id="q9", no="9", type="2계 도함수 판정법 · 닫힌 영역의 최대·최소", ref="14.7", mins=9, topics=[15],
  types=["14-crit", "14-absext"],
  stem=r"$f(x,y)=xy(3-x-y)$ 에 대하여",
  parts=[("a", r"$f$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"),
         ("b", r"세 점 $(0,0),\ (4,0),\ (0,4)$ 를 꼭짓점으로 하는 닫힌 삼각형 영역 $T$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]")],
  answer=[("a", r"$(0,0),\ (3,0),\ (0,3)$: 안장점,  $(1,1)$: 극댓값 $1$"),
          ("b", r"최댓값 $1$ (점 $(1,1)$), 최솟값 $-4$ (점 $(2,2)$)")],
  solution=[("a", [r"$f=3xy-x^2y-xy^2$: $\ f_x=y(3-2x-y)=0,\ \ f_y=x(3-x-2y)=0$",
                   r"$x=0$ 이면 $f_x=y(3-y)=0$ → $(0,0),\ (0,3)$.  $y=0$ 이면 $f_y=x(3-x)=0$ → $(3,0)$.  $x,y\ne0$ 이면 $2x+y=3,\ x+2y=3$ → $(1,1)$",
                   r"$f_{xx}=-2y,\ f_{yy}=-2x,\ f_{xy}=3-2x-2y$, $\ D=4xy-(3-2x-2y)^2$",
                   r"$(0,0),(3,0),(0,3)$: $D=-9<0$ → 안장점.  $(1,1)$: $D=4-1=3>0,\ f_{xx}=-2<0$ → 극댓값 $f(1,1)=1$"]),
            ("b", [r"내부 임계점은 $(1,1)$ 하나 (값 $1$). 나머지 임계점은 경계(두 변) 위에 있어요.",
                   r"두 변 $x=0$, $y=0$ 위에서는 $f=0$",
                   r"빗변 $x+y=4\ (0\le x\le4)$: $f=xy(3-4)=-x(4-x)$ → $x=2$ 에서 최소 $f(2,2)=-4$, 양 끝에서 $0$",
                   r"후보 $1,\ 0,\ -4$ 를 비교하면 최댓값 $1$ (점 $(1,1)$), 최솟값 $-4$ (점 $(2,2)$)"])],
  check=_c)


def _c():
    Ia = integrate(x*sin(x**2), (x, 0, sqrt(pi)))
    assert EQ(Ia, 1)
    num_a = mp.quad(lambda Y: mp.quad(lambda X: mp.sin(X*X), [Y, mp.sqrt(mp.pi)]), [0, mp.sqrt(mp.pi)])
    assert abs(num_a - 1) < 1e-10
    Ib = integrate(9*sqrt(1 + z**3)*z**2/2, (z, 0, 1))
    assert EQ(Ib, 2*sqrt(2) - 1)
    assert integrate(1, (x, 0, y), (y, 0, z)) == z**2/2
    # 원래 순서 그대로 수치적분 (z 가 가장 안쪽)
    num_b = mp.quad(lambda X: mp.quad(lambda Y: mp.quad(lambda Z: 9*mp.sqrt(1 + Z**3), [Y, 1]), [X, 1]), [0, 1])
    assert abs(num_b - (2*mp.sqrt(2) - 1)) < 1e-8
Q(SC, id="q10", no="10", type="적분 순서 바꾸기 (이중·삼중)", ref="15.2 · 15.6", mins=7, topics=[8],
  types=["15-order", "15-order3"],
  stem=r"적분 순서를 바꾸어 다음 값을 구하시오.",
  parts=[("a", r"$\displaystyle\int_0^{\sqrt\pi}\!\!\int_y^{\sqrt\pi}\sin(x^2)\,dx\,dy$ [4점]"),
         ("b", r"$\displaystyle\int_0^1\!\!\int_x^1\!\!\int_y^1 9\sqrt{1+z^3}\,dz\,dy\,dx$ [6점]")],
  answer=[("a", r"$1$"), ("b", r"$2\sqrt2-1$")],
  solution=[("a", [r"$\sin(x^2)$ 은 $x$ 로 바로 적분할 수 없으니 $x$ 를 바깥으로 보내요. 영역: $0\le y\le\sqrt\pi,\ y\le x\le\sqrt\pi$ → $0\le x\le\sqrt\pi,\ 0\le y\le x$",
                   r"$$\begin{aligned}\int_0^{\sqrt\pi}\!\!\int_0^x\sin(x^2)\,dy\,dx&=\int_0^{\sqrt\pi}x\sin(x^2)\,dx\\&=\Big[-\frac{\cos(x^2)}{2}\Big]_0^{\sqrt\pi}=\frac{1+1}{2}=1\end{aligned}$$"]),
            ("b", [r"$\sqrt{1+z^3}$ 은 $z$ 로 바로 적분할 수 없으니 $z$ 를 가장 바깥으로 보내요.",
                   r"영역: $0\le x\le1,\ x\le y\le1,\ y\le z\le1$, 즉 $0\le x\le y\le z\le1$ → $0\le z\le1,\ 0\le y\le z,\ 0\le x\le y$",
                   r"$$\begin{aligned}&\int_0^1\!\!\int_0^z\!\!\int_0^y9\sqrt{1+z^3}\,dx\,dy\,dz\\&=\int_0^19\sqrt{1+z^3}\cdot\frac{z^2}{2}\,dz\\&=\Big[(1+z^3)^{3/2}\Big]_0^1=2\sqrt2-1\end{aligned}$$"])],
  check=_c)

SETS.append({"id": "c", "no": 3, "label": "C", "title": "모의고사 C세트", "focus": "15개 주제 · 10문항 · 각 10점",
        "lead": "같은 15개 주제를 또 다른 조합으로 묶은 세 번째 세트예요. 곡선 위에서의 변화율(연쇄법칙)과 곡선의 길이로 시작해서 평행사변형 변수변환, 직선·곡선 경로로 보는 극한과 정의로 구하는 편도함수, 세 잎 장미곡선, 두 포물면 사이와 구·원뿔 삼중적분, 평면까지의 거리(라그랑주와 사영), 포물선 영역의 그린 정리, 다항함수의 ε₁·ε₂ 와 선형근사, 삼각형 영역의 최대·최소, 적분 순서 바꾸기를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
        "problems": SC})


# ════════════════════════════════════════════════════════════════════
# D세트
# ════════════════════════════════════════════════════════════════════
SD = []


def _c():
    h = 12 - x**2 - y**2 + x*y - 4*x
    assert h.subs({x: 1, y: 2}) == 5
    g = grad(h, (x, y)).subs({x: 1, y: 2})
    assert list(g) == [-4, -3] and g.norm() == 5
    assert Matrix([3, -4]).dot(g) == 0
    a, b = symbols('a b', real=True)
    sol = solve([g[0]*a + g[1]*b - 3, a**2 + b**2 - 1], [a, b], dict=True)
    assert sorted((s_[a], s_[b]) for s_ in sol) == [(-R(24, 25), R(7, 25)), (0, -1)]
    # 접평면 z = h(P) + h_x(x-1) + h_y(y-2)
    plane = 5 + g[0]*(x - 1) + g[1]*(y - 2)
    assert expand(plane - (15 - 4*x - 3*y)) == 0
    # 접평면 근처에서 h 와 평면의 차가 2차로 작아지는지
    for d in (1e-3, -2e-3):
        diffv = float((h - plane).subs({x: 1 + d, y: 2 - d}))
        assert abs(diffv) < 10*d*d
Q(SD, id="q1", no="1", type="그래디언트 · 방향도함수 · 접평면", ref="14.6 · 14.4", mins=8, topics=[10, 14],
  types=["14-maxrate", "14-dir", "14-tangent"],
  stem=r"어떤 언덕의 높이가 $h(x,y)=12-x^2-y^2+xy-4x$ 이고, 등산객이 점 $P(1,2)$ 에 서 있다.",
  parts=[("a", r"$\nabla h(P)$ 를 구하고, $P$ 에서 가장 가파르게 올라가는 방향(단위벡터)과 그 방향의 기울기(변화율)를 구하시오. [3점]"),
         ("b", r"$P$ 에서 높이가 변하지 않는 방향(단위벡터)을 모두 구하시오. [2점]"),
         ("c", r"$D_{\mathbf u}h(P)=3$ 을 만족하는 단위벡터 $\mathbf u$ 를 모두 구하시오. [2점]"),
         ("d", r"곡면 $z=h(x,y)$ 위의 점 $(1,\ 2,\ 5)$ 에서의 접평면과 법선의 방정식을 구하시오. [3점]")],
  answer=[("a", r"$\nabla h(P)=\langle-4,\ -3\rangle$, 방향 $\big\langle-\frac45,\ -\frac35\big\rangle$, 기울기 $5$"),
          ("b", r"$\pm\big\langle\frac35,\ -\frac45\big\rangle$"),
          ("c", r"$\langle0,\ -1\rangle$, $\ \big\langle-\frac{24}{25},\ \frac{7}{25}\big\rangle$"),
          ("d", r"접평면 $4x+3y+z=15$, 법선 $x=1+4t,\ y=2+3t,\ z=5+t$")],
  solution=[("a", [r"$h_x=-2x+y-4,\ \ h_y=-2y+x$ → $\nabla h(1,2)=\langle-2+2-4,\ -4+1\rangle=\langle-4,\ -3\rangle$",
                   r"가장 가파르게 올라가는 방향은 $\nabla h$ 방향: $\mathbf u=\dfrac15\langle-4,-3\rangle=\big\langle-\frac45,-\frac35\big\rangle$, 그 기울기는 $|\nabla h(P)|=5$"]),
            ("b", [r"$D_{\mathbf u}h=\nabla h\cdot\mathbf u=0 \iff \mathbf u\perp\langle-4,-3\rangle$ → $\mathbf u=\pm\dfrac15\langle3,-4\rangle$ (등위곡선의 접선 방향)"]),
            ("c", [r"$\mathbf u=\langle a,b\rangle,\ a^2+b^2=1$, $\ -4a-3b=3 \Rightarrow b=-1-\frac43a$",
                   r"대입: $a^2+\big(1+\frac43a\big)^2=1 \Rightarrow \frac{25}{9}a^2+\frac83a=0 \Rightarrow a=0$ 또는 $a=-\frac{24}{25}$",
                   r"$\mathbf u=\langle0,\ -1\rangle$ 또는 $\big\langle-\frac{24}{25},\ \frac7{25}\big\rangle$ (최대 기울기 $5$ 보다 작은 값이라 방향이 두 개 나와요)"]),
            ("d", [r"$z=h(x,y)$ 의 접평면: $z=5+h_x(P)(x-1)+h_y(P)(y-2)=5-4(x-1)-3(y-2)$ → $4x+3y+z=15$",
                   r"법선벡터 $\langle h_x,\ h_y,\ -1\rangle=\langle-4,-3,-1\rangle\parallel\langle4,3,1\rangle$ → 법선 $x=1+4t,\ y=2+3t,\ z=5+t$"])],
  check=_c)


def _c():
    Ia = integrate(x/2*exp(-x**2), (x, 0, 2))
    assert EQ(Ia, (1 - exp(-4))/4)
    num_a = mp.quad(lambda Y: mp.quad(lambda X: mp.e**(-X*X), [2*Y, 2]), [0, 1])
    assert abs(num_a - (1 - mp.e**-4)/4) < 1e-12
    Ib = integrate(sin(z)/z * 2*z, (z, 0, pi))
    assert EQ(Ib, 4)
    # 원래 순서 그대로 (z 가 가장 안쪽, y 는 0..2)
    num_b = 2*mp.quad(lambda X: mp.quad(lambda Z: mp.sin(Z)/Z, [X, mp.pi]), [0, mp.pi])
    assert abs(num_b - 4) < 1e-8
Q(SD, id="q2", no="2", type="적분 순서 바꾸기 (이중·삼중)", ref="15.2 · 15.6", mins=7, topics=[8],
  types=["15-order", "15-order3"],
  stem=r"적분 순서를 바꾸어 다음 값을 구하시오.",
  parts=[("a", r"$\displaystyle\int_0^1\!\!\int_{2y}^2e^{-x^2}\,dx\,dy$ [4점]"),
         ("b", r"$\displaystyle\int_0^\pi\!\!\int_0^2\!\!\int_x^\pi\frac{\sin z}{z}\,dz\,dy\,dx$ [6점]")],
  answer=[("a", r"$\dfrac{1-e^{-4}}{4}$"), ("b", r"$4$")],
  solution=[("a", [r"$e^{-x^2}$ 은 $x$ 로 바로 적분할 수 없어요. 영역: $0\le y\le1,\ 2y\le x\le2$ → $0\le x\le2,\ 0\le y\le\frac x2$",
                   r"$$\begin{aligned}\int_0^2\!\!\int_0^{x/2}e^{-x^2}\,dy\,dx&=\int_0^2\frac x2e^{-x^2}\,dx\\&=\Big[-\frac{e^{-x^2}}{4}\Big]_0^2=\frac{1-e^{-4}}{4}\end{aligned}$$"]),
            ("b", [r"$\dfrac{\sin z}{z}$ 는 $z$ 로 바로 적분할 수 없으니 $z$ 를 가장 바깥으로 보내요.",
                   r"영역: $0\le x\le\pi,\ 0\le y\le2,\ x\le z\le\pi$ → $0\le z\le\pi,\ 0\le x\le z,\ 0\le y\le2$",
                   r"$$\begin{aligned}&\int_0^\pi\!\!\int_0^z\!\!\int_0^2\frac{\sin z}{z}\,dy\,dx\,dz\\&=\int_0^\pi\frac{\sin z}{z}\cdot2z\,dz=2\int_0^\pi\sin z\,dz=4\end{aligned}$$"])],
  check=_c)


def _c():
    T = symbols('T', real=True)
    rr = Matrix([2*T, T**2, T**3/3])
    vt = rr.diff(T)
    assert expand(vt.dot(vt) - (T**2 + 2)**2) == 0
    assert integrate(T**2 + 2, (T, 0, 3)) == 15
    num = nquad(lambda q: mp.sqrt(4 + 4*q*q + q**4), 0, 3)
    assert abs(num - 15) < 1e-12
    vv, aa = vt.subs(T, 2), rr.diff(T, 2).subs(T, 2)
    assert list(vv) == [2, 4, 4] and list(aa) == [0, 2, 4] and vv.norm() == 6 and vv.dot(aa) == 24
    assert vv.dot(aa) / vv.norm() == 4 and diff(T**2 + 2, T).subs(T, 2) == 4
    proj = (vv.dot(aa) / vv.dot(vv)) * vv
    assert list(proj) == [R(4, 3), R(8, 3), R(8, 3)]
    orth = aa - proj
    assert list(orth) == [-R(4, 3), -R(2, 3), R(4, 3)] and orth.dot(vv) == 0 and orth.norm() == 2
    assert list(vv.cross(aa)) == [8, -8, 4] and vv.cross(aa).norm() / vv.norm() == 2
Q(SD, id="q3", no="3", type="곡선의 길이 · 사영(comp·proj)", ref="13.3 · 12.3 · 13.2", mins=7, topics=[11, 13],
  types=["13-arc", "12-proj", "13-motion"],
  stem=r"곡선 $\mathbf r(t)=\big\langle 2t,\ t^2,\ \tfrac13t^3\big\rangle$ 에 대하여",
  parts=[("a", r"$0\le t\le3$ 부분의 길이를 구하시오. [3점]"),
         ("b", r"$t=2$ 에서의 속도 $\mathbf v=\mathbf r'(2)$, 가속도 $\mathbf a=\mathbf r''(2)$ 에 대하여 $\operatorname{comp}_{\mathbf v}\mathbf a$ 와 $\operatorname{proj}_{\mathbf v}\mathbf a$ 를 구하시오. [4점]"),
         ("c", r"$\mathbf a$ 를 $\mathbf v$ 에 평행한 벡터와 $\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [3점]")],
  answer=[("a", r"$15$"),
          ("b", r"$\operatorname{comp}_{\mathbf v}\mathbf a=4$, $\ \operatorname{proj}_{\mathbf v}\mathbf a=\big\langle\frac43,\ \frac83,\ \frac83\big\rangle$"),
          ("c", r"$\mathbf a=\big\langle\frac43,\frac83,\frac83\big\rangle+\big\langle-\frac43,-\frac23,\frac43\big\rangle$, 수직인 벡터의 크기 $2$")],
  solution=[("a", [r"$\mathbf r'(t)=\langle2,\ 2t,\ t^2\rangle$, $\ |\mathbf r'(t)|^2=4+4t^2+t^4=(t^2+2)^2$ → $|\mathbf r'(t)|=t^2+2$ (완전제곱)",
                   r"$L=\displaystyle\int_0^3(t^2+2)\,dt=9+6=15$"]),
            ("b", [r"$\mathbf r''(t)=\langle0,\ 2,\ 2t\rangle$ → $\mathbf v=\langle2,4,4\rangle$, $\ \mathbf a=\langle0,2,4\rangle$, $\ |\mathbf v|=6$, $\ \mathbf a\cdot\mathbf v=0+8+16=24$",
                   r"$\operatorname{comp}_{\mathbf v}\mathbf a=\dfrac{24}{6}=4$ (속력 $t^2+2$ 의 변화율 $2t$ 의 $t=2$ 값과 같아요)",
                   r"$\operatorname{proj}_{\mathbf v}\mathbf a=\dfrac{24}{36}\langle2,4,4\rangle=\big\langle\frac43,\frac83,\frac83\big\rangle$"]),
            ("c", [r"수직 성분: $\mathbf a-\operatorname{proj}_{\mathbf v}\mathbf a=\big\langle-\frac43,\ -\frac23,\ \frac43\big\rangle$ (확인: $\mathbf v$ 와 내적하면 $\frac{-8-8+16}{3}=0$)",
                   r"크기 $\dfrac{\sqrt{16+4+16}}{3}=2$ ($\frac{|\mathbf v\times\mathbf a|}{|\mathbf v|}=\frac{|\langle8,-8,4\rangle|}{6}=2$ 와 같아요)"])],
  check=_c)


def _c():
    m, k = symbols('m k', real=True)
    f1 = x**3*y/(x**6 + y**2)
    assert limit(f1.subs(y, m*x), x, 0) == 0 and f1.subs(x, 0) == 0
    assert simplify(f1.subs(y, k*x**3) - k/(1 + k**2)) == 0 and simplify(f1.subs(y, x**3)) == R(1, 2)
    f = x**3/(x**2 + y**2)
    hh = symbols('hh', nonzero=True, real=True)
    assert limit(f.subs({x: hh, y: 0})/hh, hh, 0) == 1 and f.subs({x: 0, y: hh}) == 0
    # 연속: |f| <= |x|
    for (a, b) in [(0.3, -0.7), (-1e-3, 2e-3), (5e-4, 5e-4)]:
        assert abs(f.subs({x: a, y: b})) <= abs(a) + 1e-15
    # 미분불가능: Δy=Δx 이면 Δz - Δx = -Δx/2
    assert simplify(f.subs({x: hh, y: hh}) - hh/2) == 0
    assert simplify((f.subs({x: hh, y: hh}) - 1*hh) / hh) == -R(1, 2)
Q(SD, id="q4", no="4", type="극한의 존재성 · 미분가능성의 정의", ref="14.2 · 14.4", mins=9, topics=[3, 4],
  types=["14-dne", "14-differentiable"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3y}{x^6+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("b", r"$f(x,y)=\dfrac{x^3}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $\ f(0,0)=0$ 일 때, $f$ 가 원점에서 연속임을 보이고 $f_x(0,0),\ f_y(0,0)$ 을 구하시오. [3점]"),
         ("c", r"(b)의 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>" + DEF7)],
  answer=[("a", r"존재하지 않음 (직선을 따라서는 $0$, 곡선 $y=x^3$ 을 따라 $\frac12$)"),
          ("b", r"연속, $\ f_x(0,0)=1,\ f_y(0,0)=0$"),
          ("c", r"미분가능하지 않음 ($\Delta y=\Delta x$ 로 두면 $\varepsilon_1+\varepsilon_2=-\frac12$)")],
  solution=[("a", [r"직선 $y=mx$: $\dfrac{mx^4}{x^6+m^2x^2}=\dfrac{mx^2}{x^4+m^2}\to0$, $\ y$축($x=0$) 위에서도 $0$ → 직선만으로는 판정이 안 돼요.",
                   r"분모의 $x^6$ 과 $y^2$ 의 차수를 맞추는 곡선 $y=x^3$ 을 따라가면 $\dfrac{x^6}{x^6+x^6}=\dfrac12$",
                   r"경로에 따라 값이 다르므로 극한은 존재하지 않아요. (일반적으로 곡선 $y=kx^3$ 을 따라 $\frac{k}{1+k^2}$)"]),
            ("b", [r"$\dfrac{x^2}{x^2+y^2}\le1$ 이므로 $|f(x,y)|\le|x|\to0=f(0,0)$ → 조임정리로 연속",
                   r"$f(h,0)=\dfrac{h^3}{h^2}=h$ → $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{h-0}{h}=1$",
                   r"$f(0,h)=0$ → $f_y(0,0)=\displaystyle\lim_{h\to0}\frac{0-0}{h}=0$"]),
            ("c", [r"미분가능하다고 가정하면 $\Delta z=f(\Delta x,\Delta y)-f(0,0)=1\cdot\Delta x+0\cdot\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 이고 $\varepsilon_1,\varepsilon_2\to0$ 이어야 해요.",
                   r"$\Delta y=\Delta x\ (\ne0)$ 로 두면 좌변은 $f(\Delta x,\Delta x)=\dfrac{(\Delta x)^3}{2(\Delta x)^2}=\dfrac{\Delta x}{2}$ → $\dfrac{\Delta x}2=\Delta x+(\varepsilon_1+\varepsilon_2)\Delta x$ → $\varepsilon_1+\varepsilon_2=-\dfrac12$",
                   r"그런데 $\Delta x\to0$ 이면 $(\Delta x,\Delta y)\to(0,0)$ 이므로 $\varepsilon_1+\varepsilon_2\to0$ 이어야 해서 모순 → 원점에서 **미분가능하지 않아요**. (연속이고 편도함수도 있지만 미분가능하지 않은 예)"])],
  check=_c)


def _c():
    P, Qf = x + y**2, 3*x*y
    c1 = integrate(P.subs(y, 0), (x, 0, 2))
    assert c1 == 2
    X, Y = 2*cos(t), 2*sin(t)
    arc = P.subs({x: X, y: Y}, simultaneous=True)*diff(X, t) + Qf.subs({x: X, y: Y}, simultaneous=True)*diff(Y, t)
    assert simplify(arc - (-4*sin(t)*cos(t) - 8*sin(t)**3 + 24*cos(t)**2*sin(t))) == 0
    c2 = integrate(arc, (t, 0, pi/2))
    assert EQ(c2, R(2, 3))
    c3 = integrate(Qf.subs(x, 0), (y, 2, 0))
    assert c3 == 0 and EQ(c1 + c2 + c3, R(8, 3))
    curl = diff(Qf, x) - diff(P, y)
    assert simplify(curl - y) == 0
    G = integrate(r*sin(th)*r, (r, 0, 2), (th, 0, pi/2))
    assert EQ(G, R(8, 3))
    num = mp.quad(lambda X_: mp.quad(lambda Y_: Y_, [0, mp.sqrt(4 - X_*X_)]), [0, 2])
    assert abs(num - mp.mpf(8)/3) < 1e-10
Q(SD, id="q5", no="5", type="그린 정리 · 곡선 나누어 직접 계산", ref="16.2 · 16.4", mins=9, topics=[9],
  types=["16-green", "16-vector"],
  stem=r"$D$ 는 원 $x^2+y^2=4$ 의 제1사분면 부분(사분원판)이고, $C$ 는 $D$ 의 경계로 양의 방향이다. $\displaystyle I=\oint_C(x+y^2)\,dx+3xy\,dy$ 에 대하여",
  parts=[("a", r"$C$ 를 두 선분과 원호로 나누어 $I$ 를 직접 계산하시오. [5점]"),
         ("b", r"그린 정리를 이용해 $I$ 를 계산하시오. [5점]")],
  answer=[("a", r"$\dfrac83$"), ("b", r"$\dfrac83$")],
  solution=[("a", [r"양의 방향: $C_1:(0,0)\to(2,0)$, $\ C_2$: 원호 $(2,0)\to(0,2)$, $\ C_3:(0,2)\to(0,0)$",
                   r"$C_1:\ y=0,\ dy=0$ → $\displaystyle\int_0^2x\,dx=2$.  $\ C_3:\ x=0,\ dx=0$ 이고 $Q=3xy=0$ → $0$",
                   r"$C_2:\ x=2\cos t,\ y=2\sin t\ \big(0\le t\le\frac\pi2\big)$: $$\begin{aligned}&\int_0^{\pi/2}\Big[(2\cos t+4\sin^2t)(-2\sin t)\\&\qquad+12\cos t\sin t\cdot2\cos t\Big]dt\\&=\int_0^{\pi/2}\big(-4\sin t\cos t-8\sin^3t\\&\qquad+24\cos^2t\sin t\big)\,dt\\&=-2-\frac{16}{3}+8=\frac23\end{aligned}$$",
                   r"$I=2+\dfrac23+0=\dfrac83$"]),
            ("b", [r"$P=x+y^2,\ Q=3xy$ → $Q_x-P_y=3y-2y=y$",
                   r"$$\begin{aligned}I&=\iint_Dy\,dA=\int_0^{\pi/2}\!\!\int_0^2r\sin\theta\cdot r\,dr\,d\theta\\&=\frac83\Big[-\cos\theta\Big]_0^{\pi/2}=\frac83\end{aligned}$$ — (a)와 같아요."])],
  check=_c)


def _c():
    xs, ys = (v - u)/2, (u + v)/2
    assert simplify(ys - xs - u) == 0 and simplify(ys + xs - v) == 0
    Jinv = Matrix([[diff(xs, u), diff(xs, v)], [diff(ys, u), diff(ys, v)]]).det()
    assert Jinv == -R(1, 2)
    # 경계 대응: y=0 → u=-v, x=0 → u=v
    assert simplify((ys).subs(u, -v)) == 0 and simplify((xs).subs(u, v)) == 0
    val = integrate(cos(u/v)/2, (u, -v, v), (v, 2, 4))
    assert EQ(val, 6*sin(1))
    num = (mp.quad(lambda X: mp.quad(lambda Y: mp.cos((Y - X)/(Y + X)), [2 - X, 4 - X]), [0, 2])
           + mp.quad(lambda X: mp.quad(lambda Y: mp.cos((Y - X)/(Y + X)), [0, 4 - X]), [2, 4]))
    assert abs(num - 6*mp.sin(1)) < 1e-8
Q(SD, id="q6", no="6", type="변수변환 (야코비안)", ref="15.9", mins=8, topics=[7],
  types=["15-change"],
  stem=r"$R$ 은 네 점 $(2,0),\ (4,0),\ (0,4),\ (0,2)$ 를 꼭짓점으로 하는 사다리꼴이다. 변환 $u=y-x,\ v=y+x$ 를 이용하여",
  parts=[("a", r"야코비안 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 부등식으로 나타내시오. [4점]"),
         ("b", r"$\displaystyle\iint_R\cos\Big(\frac{y-x}{y+x}\Big)\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\partial(x,y)}{\partial(u,v)}=-\dfrac12$ (절댓값 $\frac12$), $\ S=\{(u,v)\mid2\le v\le4,\ -v\le u\le v\}$"),
          ("b", r"$6\sin1$")],
  solution=[("a", [r"$x=\dfrac{v-u}{2},\ y=\dfrac{u+v}{2}$ → $$\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}-\frac12&\frac12\\[2pt]\frac12&\frac12\end{vmatrix}=-\frac14-\frac14=-\frac12$$",
                   r"경계: $x+y=2,\ x+y=4$ → $v=2,\ v=4$.  $\ y=0$ → $u=-v$,  $\ x=0$ → $u=v$",
                   r"$S:\ 2\le v\le4,\ -v\le u\le v$ (사다리꼴 — $u$ 의 범위가 $v$ 에 따라 달라져요)"]),
            ("b", [r"$dA=\dfrac12\,du\,dv$, 피적분함수 $\cos\dfrac uv$ 는 $u$ 로 먼저 적분하면 쉬워요.",
                   r"$$\begin{aligned}&\frac12\int_2^4\!\!\int_{-v}^{v}\cos\frac uv\,du\,dv\\&=\frac12\int_2^4\Big[v\sin\frac uv\Big]_{u=-v}^{u=v}dv\\&=\frac12\int_2^42v\sin1\,dv=\sin1\cdot\Big[\frac{v^2}{2}\Big]_2^4=6\sin1\end{aligned}$$"])],
  check=_c)


def _c():
    S_, T_ = symbols('S T', real=True)
    X, Y = 2*S_ + T_, S_ - 2*T_
    tests = [exp(x)*sin(y) + x**3*y**2, x**2*y - 3*x*y**3 + cos(x + 2*y), log(1 + x**2 + y**2)*x]
    for F in tests:
        Z = F.subs({x: X, y: Y}, simultaneous=True)
        fx, fy = diff(F, x), diff(F, y)
        sub = lambda e: e.subs({x: X, y: Y}, simultaneous=True)
        assert simplify(diff(Z, S_) - sub(2*fx + fy)) == 0
        assert simplify(diff(Z, T_) - sub(fx - 2*fy)) == 0
        lap = diff(Z, S_, 2) + diff(Z, T_, 2) - sub(5*(diff(F, x, 2) + diff(F, y, 2)))
        assert simplify(lap) == 0
        mixed = diff(Z, S_, T_) - sub(2*diff(F, x, 2) - 3*diff(F, x, y) - 2*diff(F, y, 2))
        assert simplify(mixed) == 0
    # 주어진 값: (s,t)=(1,1) → (x,y)=(3,-1), f_xx=4, f_xy=-1, f_yy=2 인 2차식으로 확인
    assert (X.subs({S_: 1, T_: 1}), Y.subs({S_: 1, T_: 1})) == (3, -1)
    F = 2*(x - 3)**2 - (x - 3)*(y + 1) + (y + 1)**2
    assert (diff(F, x, 2), diff(F, x, y), diff(F, y, 2)) == (4, -1, 2)
    Z = F.subs({x: X, y: Y}, simultaneous=True)
    assert diff(Z, S_, T_).subs({S_: 1, T_: 1}) == 7
    assert (diff(Z, S_, 2) + diff(Z, T_, 2)).subs({S_: 1, T_: 1}) == 30
Q(SD, id="q7", no="7", type="2계 연쇄법칙", ref="14.5", mins=7, topics=[12],
  types=["14-chain2", "14-chain"],
  stem=r"$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=2s+t,\ y=s-2t$ 이다.",
  parts=[("a", r"$z_s,\ z_t$ 를 $f_x,\ f_y$ 로 나타내시오. [3점]"),
         ("b", r"$z_{ss}+z_{tt}=5\big(f_{xx}+f_{yy}\big)$ 임을 보이시오. [4점]"),
         ("c", r"$z_{st}$ 를 $f_{xx},\ f_{xy},\ f_{yy}$ 로 나타내고, $f_{xx}(3,-1)=4,\ f_{xy}(3,-1)=-1,\ f_{yy}(3,-1)=2$ 일 때 $(s,t)=(1,1)$ 에서 $z_{st}$ 와 $z_{ss}+z_{tt}$ 의 값을 구하시오. [3점]")],
  answer=[("a", r"$z_s=2f_x+f_y,\ \ z_t=f_x-2f_y$"),
          ("b", r"아래 풀이"),
          ("c", r"$z_{st}=2f_{xx}-3f_{xy}-2f_{yy}$;  $(s,t)=(1,1)$ 에서 $z_{st}=7,\ \ z_{ss}+z_{tt}=30$")],
  solution=[("a", [r"$x_s=2,\ x_t=1,\ y_s=1,\ y_t=-2$ (모두 상수)",
                   r"$z_s=f_x\,x_s+f_y\,y_s=2f_x+f_y$,  $\ z_t=f_x\,x_t+f_y\,y_t=f_x-2f_y$"]),
            ("b", [r"$f_x,\ f_y$ 도 $s,t$ 의 함수라 연쇄법칙을 한 번 더: $(f_x)_s=2f_{xx}+f_{xy}$, $\ (f_y)_s=2f_{xy}+f_{yy}$, $\ (f_x)_t=f_{xx}-2f_{xy}$, $\ (f_y)_t=f_{xy}-2f_{yy}$",
                   r"$z_{ss}=2(2f_{xx}+f_{xy})+(2f_{xy}+f_{yy})=4f_{xx}+4f_{xy}+f_{yy}$",
                   r"$z_{tt}=(f_{xx}-2f_{xy})-2(f_{xy}-2f_{yy})=f_{xx}-4f_{xy}+4f_{yy}$",
                   r"더하면 $f_{xy}$ 항이 지워져 $z_{ss}+z_{tt}=5f_{xx}+5f_{yy}=5\big(f_{xx}+f_{yy}\big)$"]),
            ("c", [r"$z_{st}=(z_s)_t=2(f_x)_t+(f_y)_t=2(f_{xx}-2f_{xy})+(f_{xy}-2f_{yy})=2f_{xx}-3f_{xy}-2f_{yy}$",
                   r"$(s,t)=(1,1)$ 이면 $(x,y)=(3,-1)$ → $z_{st}=8+3-4=7$, $\ z_{ss}+z_{tt}=5(4+2)=30$"])],
  check=_c)


def _c():
    A = integrate(9*sin(2*th)**2/2, (th, 0, 2*pi))
    assert EQ(A, 9*pi/2)
    one = integrate(9*sin(2*th)**2/2, (th, 0, pi/2))
    assert EQ(4*one, 9*pi/2)
    B = integrate(r**2, (r, 0, 3*sin(2*th)), (th, 0, pi/2))
    assert EQ(B, 6)
    C = integrate(r**3*cos(th)*sin(th), (r, 0, 3*sin(2*th)), (th, 0, pi/2))
    assert EQ(C, R(27, 5))
    assert EQ(integrate((1 - u**2)**2, (u, -1, 1)), R(16, 15))
    numB = mp.quad(lambda a: (3*mp.sin(2*a))**3/3, [0, mp.pi/2])
    numC = mp.quad(lambda a: (3*mp.sin(2*a))**4/4*mp.cos(a)*mp.sin(a), [0, mp.pi/2])
    assert abs(numB - 6) < 1e-12 and abs(numC - mp.mpf(27)/5) < 1e-12
Q(SD, id="q8", no="8", type="극좌표 이중적분 (장미곡선)", ref="15.3", mins=8, topics=[1],
  types=["15-polar"],
  stem=r"장미곡선 $r=3\sin2\theta$ (꽃잎 4장)에 대하여, 제1사분면의 꽃잎 $\big(0\le\theta\le\frac\pi2\big)$ 으로 둘러싸인 영역을 $D$ 라 하자.",
  parts=[("a", r"장미곡선 전체(꽃잎 4장)로 둘러싸인 영역의 넓이를 구하시오. [3점]"),
         ("b", r"$\displaystyle\iint_D\sqrt{x^2+y^2}\,dA$ 를 구하시오. [3점]"),
         ("c", r"$\displaystyle\iint_D xy\,dA$ 를 구하시오. [4점]")],
  answer=[("a", r"$\dfrac{9\pi}{2}$"), ("b", r"$6$"), ("c", r"$\dfrac{27}{5}$")],
  solution=[("a", [r"$\theta$ 가 $0$ 에서 $2\pi$ 까지 변하는 동안 꽃잎 4장을 한 번씩 그려요 ($r<0$ 인 구간은 반대쪽 사분면의 꽃잎).",
                   r"$$\begin{aligned}A&=\frac12\int_0^{2\pi}9\sin^22\theta\,d\theta\\&=\frac94\int_0^{2\pi}(1-\cos4\theta)\,d\theta=\frac{9\pi}{2}\end{aligned}$$ (꽃잎 한 장 $\frac{9\pi}8$ 의 4배)"]),
            ("b", [r"$\sqrt{x^2+y^2}=r$: $$\begin{aligned}\iint_Dr\,dA&=\int_0^{\pi/2}\!\!\int_0^{3\sin2\theta}r^2\,dr\,d\theta\\&=9\int_0^{\pi/2}\sin^32\theta\,d\theta\end{aligned}$$",
                   r"$u=2\theta$: $\ \dfrac92\displaystyle\int_0^{\pi}\sin^3u\,du=\frac92\Big[-\cos u+\frac{\cos^3u}{3}\Big]_0^{\pi}=\frac92\cdot\frac43=6$"]),
            ("c", [r"$xy=r^2\cos\theta\sin\theta=\dfrac{r^2}{2}\sin2\theta$: $$\begin{aligned}\iint_Dxy\,dA&=\int_0^{\pi/2}\!\!\int_0^{3\sin2\theta}\frac{\sin2\theta}{2}\,r^3\,dr\,d\theta\\&=\frac{81}{8}\int_0^{\pi/2}\sin^52\theta\,d\theta\end{aligned}$$",
                   r"$u=2\theta$ 로 바꾸고 $\sin^5u=(1-\cos^2u)^2\sin u$, $\ w=\cos u$: $$\frac{81}{16}\int_{-1}^{1}(1-w^2)^2\,dw=\frac{81}{16}\cdot\frac{16}{15}=\frac{27}{5}$$"])],
  check=_c)


def _c():
    lam = symbols('lam', real=True)
    f = x*y - x - y
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    assert crit == [{x: 1, y: 1}] and f.subs({x: 1, y: 1}) == -1
    assert (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2) == -1
    g = x**2 + y**2
    sols = solve([diff(f, x) - lam*diff(g, x), diff(f, y) - lam*diff(g, y), g - 4], [x, y, lam], dict=True)
    vals = sorted(set(simplify(f.subs(sl)) for sl in sols), key=lambda e: float(e))
    assert len(sols) == 4
    assert EQ(vals[0], -R(5, 2)) and EQ(vals[-1], 2 + 2*sqrt(2)) and EQ(vals[1], 2 - 2*sqrt(2))
    xm = (1 + sqrt(7))/2
    assert EQ(xm**2 + (1 - xm)**2, 4) and EQ(f.subs({x: xm, y: 1 - xm}), -R(5, 2))
    # 원 위 수치 탐색과 내부 격자
    bd = [float(f.subs({x: 2*mp.cos(a), y: 2*mp.sin(a)})) for a in mp.linspace(0, 2*mp.pi, 2001)]
    assert abs(max(bd) - (2 + 2*2**0.5)) < 1e-5 and abs(min(bd) + 2.5) < 1e-5
    inner = [float(f.subs({x: a/10, y: b/10})) for a in range(-20, 21) for b in range(-20, 21) if a*a + b*b <= 400]
    assert max(inner) <= 2 + 2*2**0.5 + 1e-9 and min(inner) >= -2.5 - 1e-9
Q(SD, id="q9", no="9", type="2계 도함수 판정법 · 라그랑주 승수법", ref="14.7 · 14.8", mins=9, topics=[15, 2],
  types=["14-crit", "14-lagrange", "14-absext"],
  stem=r"$f(x,y)=xy-x-y$ 의 닫힌 원판 $R=\{(x,y)\mid x^2+y^2\le4\}$ 에서의 최댓값과 최솟값을 구하려고 한다.",
  parts=[("a", r"$f$ 의 임계점을 구하고 2계 도함수 판정법으로 판정하시오. [3점]"),
         ("b", r"라그랑주 승수법으로 경계 $x^2+y^2=4$ 위에서 $f$ 의 최댓값과 최솟값의 후보를 구하시오. [4점]"),
         ("c", r"$R$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [3점]")],
  answer=[("a", r"$(1,1)$: 안장점 ($f_{xx}f_{yy}-f_{xy}^2=-1<0$)"),
          ("b", r"$x=y$ 에서 $2\mp2\sqrt2$ (점 $\pm(\sqrt2,\sqrt2)$),  $x+y=1$ 인 두 점에서 $-\frac52$"),
          ("c", r"최댓값 $2+2\sqrt2$ (점 $(-\sqrt2,-\sqrt2)$), 최솟값 $-\dfrac52$ (점 $\big(\frac{1\pm\sqrt7}{2},\ \frac{1\mp\sqrt7}{2}\big)$)")],
  solution=[("a", [r"$f_x=y-1=0,\ f_y=x-1=0$ → 임계점 $(1,1)$ ($R$ 의 내부: $1+1<4$)",
                   r"$f_{xx}=0,\ f_{yy}=0,\ f_{xy}=1$ → $f_{xx}f_{yy}-f_{xy}^2=0-1=-1<0$ → 안장점 ($f(1,1)=-1$). 내부에는 극값이 없어요."]),
            ("b", [r"$g=x^2+y^2=4$, $\ \nabla f=\lambda\nabla g$: $\ y-1=2\lambda x,\ \ x-1=2\lambda y$",
                   r"두 식을 빼면 $y-x=2\lambda(x-y) \Rightarrow (x-y)(1+2\lambda)=0$ → $x=y$ 또는 $\lambda=-\frac12$",
                   r"$x=y$: $2x^2=4,\ x=\pm\sqrt2$ → $f(\sqrt2,\sqrt2)=2-2\sqrt2$, $\ f(-\sqrt2,-\sqrt2)=2+2\sqrt2$",
                   r"$\lambda=-\frac12$: $y-1=-x$, 즉 $x+y=1$. 이때 $xy=\dfrac{(x+y)^2-(x^2+y^2)}{2}=\dfrac{1-4}{2}=-\dfrac32$ → $f=xy-(x+y)=-\dfrac52$ (점 $x=\frac{1\pm\sqrt7}{2},\ y=1-x$)"]),
            ("c", [r"닫힌 유계 영역이라 최댓값·최솟값이 존재하고, 내부 임계점은 안장점뿐이라 후보는 경계의 값들이에요.",
                   r"$2\sqrt2<3$ 이므로 $2-2\sqrt2>-1>-\frac52$ → 최댓값 $2+2\sqrt2$ (점 $(-\sqrt2,-\sqrt2)$), 최솟값 $-\dfrac52$"])],
  check=_c)


def _c():
    V = integrate((r*cos(th) + 3)*r, (r, 0, 2), (th, 0, 2*pi))
    assert EQ(V, 12*pi)
    Mx = integrate(r*cos(th)*(r*cos(th) + 3)*r, (r, 0, 2), (th, 0, 2*pi))
    assert EQ(Mx, 4*pi)
    numV = mp.quad(lambda X: mp.quad(lambda Y: X + 3, [-mp.sqrt(4 - X*X), mp.sqrt(4 - X*X)]), [-2, 2])
    numM = mp.quad(lambda X: mp.quad(lambda Y: X*(X + 3), [-mp.sqrt(4 - X*X), mp.sqrt(4 - X*X)]), [-2, 2])
    assert abs(numV - 12*mp.pi) < 1e-6 and abs(numM - 4*mp.pi) < 1e-6
    H = integrate(rho**4*sin(ph)**3, (rho, 0, 2), (ph, 0, pi/2), (th, 0, 2*pi))
    assert EQ(H, 128*pi/15)
    assert EQ(integrate(sin(ph)**3, (ph, 0, pi/2)), R(2, 3))
    numH = 2*mp.pi*mp.quad(lambda q: q**2*q*(2*mp.sqrt(4 - q*q))/2, [0, 2])   # 원주좌표: ∫ r^2 · (높이 √(4-r^2)) · r dr
    assert abs(numH - 128*mp.pi/15) < 1e-8
Q(SD, id="q10", no="10", type="원주좌표 · 구면좌표 삼중적분", ref="15.7 · 15.8", mins=9, topics=[5, 6],
  types=["15-cyl", "15-sph"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"원기둥 $x^2+y^2=4$ 의 안쪽, 평면 $z=0$ 의 위쪽, 평면 $z=x+3$ 의 아래쪽에 있는 입체를 $E$ 라 할 때, 원주좌표를 이용하여 $E$ 의 부피와 $\displaystyle\iiint_Ex\,dV$ 를 구하시오. [5점]"),
         ("b", r"반구 $H=\{(x,y,z)\mid x^2+y^2+z^2\le4,\ z\ge0\}$ 에서 구면좌표를 이용하여 $\displaystyle\iiint_H(x^2+y^2)\,dV$ 를 구하시오. [5점]")],
  answer=[("a", r"부피 $12\pi$, $\ \displaystyle\iiint_Ex\,dV=4\pi$"), ("b", r"$\dfrac{128\pi}{15}$")],
  solution=[("a", [r"$r\le2$ 에서 $x+3=r\cos\theta+3\ge1>0$ 이므로 $E:\ 0\le\theta\le2\pi,\ 0\le r\le2,\ 0\le z\le r\cos\theta+3$",
                   r"$$\begin{aligned}V&=\int_0^{2\pi}\!\!\int_0^2(r\cos\theta+3)\,r\,dr\,d\theta\\&=0+3\cdot2\pi\cdot\frac{2^2}{2}=12\pi\end{aligned}$$ ($\cos\theta$ 항은 한 바퀴 적분하면 $0$)",
                   r"$$\begin{aligned}\iiint_Ex\,dV&=\int_0^{2\pi}\!\!\int_0^2r\cos\theta\,(r\cos\theta+3)\,r\,dr\,d\theta\\&=\int_0^{2\pi}\cos^2\theta\,d\theta\cdot\int_0^2r^3\,dr=\pi\cdot4=4\pi\end{aligned}$$"]),
            ("b", [r"$x^2+y^2=\rho^2\sin^2\phi$, $\ H:\ 0\le\theta\le2\pi,\ 0\le\phi\le\frac\pi2,\ 0\le\rho\le2$",
                   r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^2\rho^4\sin^3\phi\,d\rho\,d\phi\,d\theta\\&=2\pi\cdot\int_0^{\pi/2}\sin^3\phi\,d\phi\cdot\frac{2^5}{5}\\&=2\pi\cdot\frac23\cdot\frac{32}{5}=\frac{128\pi}{15}\end{aligned}$$"])],
  check=_c)

SETS.append({"id": "d", "no": 4, "label": "D", "title": "모의고사 D세트", "focus": "15개 주제 · 10문항 · 각 10점",
        "lead": "15개 주제를 네 번째 조합으로 묶은 세트예요. 언덕 높이 함수의 그래디언트·방향도함수·접평면으로 시작해서 적분 순서 바꾸기, 곡선의 길이와 접선 방향 가속도(사영), 경로로 보는 극한과 미분가능성의 정의(미분가능하지 않은 예), 사분원판 그린 정리, 사다리꼴 변수변환, 2계 연쇄법칙, 네 잎 장미곡선, 원판 위 최대·최소(판정법과 라그랑주), 원주·구면좌표를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
        "problems": SD})


# ════════════════════════════════════════════════════════════════════
# E세트
# ════════════════════════════════════════════════════════════════════
SE = []


def _c():
    F = x*y*z
    assert F.subs({x: 1, y: 2, z: 3}) == 6
    n = grad(F, (x, y, z)).subs({x: 1, y: 2, z: 3})
    assert list(n) == [6, 3, 2] and n.norm() == 7
    plane = n.dot(Matrix([x - 1, y - 2, z - 3]))
    assert expand(plane - (6*x + 3*y + 2*z - 18)) == 0
    OP = Matrix([1, 2, 3])
    assert n.dot(OP) / n.norm() == R(18, 7)
    foot = (n.dot(OP) / n.dot(n)) * n
    assert list(foot) == [R(108, 49), R(54, 49), R(36, 49)]
    assert 6*foot[0] + 3*foot[1] + 2*foot[2] == 18 and foot.norm() == R(18, 7)
    # 평면 위 다른 점들보다 원점에 가까운지 (수치)
    pts = [(a, b, (18 - 6*a - 3*b)/2) for a in [i/10 for i in range(-10, 41)] for b in [j/10 for j in range(-10, 41)]]
    assert min((a*a + b*b + c*c)**0.5 for a, b, c in pts) >= 18/7 - 1e-12
Q(SE, id="q1", no="1", type="접평면 · 사영(comp·proj)", ref="14.6 · 12.3 · 12.5", mins=7, topics=[13, 14],
  types=["14-levelsurf", "12-proj", "12-dist"],
  stem=r"곡면 $S:\ xyz=6$ 위의 점 $P(1,\ 2,\ 3)$ 에 대하여",
  parts=[("a", r"$P$ 에서 $S$ 의 접평면과 법선의 방정식을 구하시오. [4점]"),
         ("b", r"$\operatorname{comp}$ 를 이용하여 원점에서 (a)의 접평면까지의 거리를 구하시오. [3점]"),
         ("c", r"$\operatorname{proj}$ 를 이용하여 (a)의 접평면 위에서 원점에 가장 가까운 점을 구하시오. [3점]")],
  answer=[("a", r"접평면 $6x+3y+2z=18$, 법선 $x=1+6t,\ y=2+3t,\ z=3+2t$"),
          ("b", r"$\dfrac{18}{7}$"),
          ("c", r"$\Big(\dfrac{108}{49},\ \dfrac{54}{49},\ \dfrac{36}{49}\Big)$")],
  solution=[("a", [r"$F=xyz$ 라 두면 $S$ 는 등위곡면 $F=6$, $\ \nabla F=\langle yz,\ xz,\ xy\rangle$ → $\nabla F(1,2,3)=\langle6,\ 3,\ 2\rangle$",
                   r"접평면: $6(x-1)+3(y-2)+2(z-3)=0 \Rightarrow 6x+3y+2z=18$",
                   r"법선: $x=1+6t,\ y=2+3t,\ z=3+2t$"]),
            ("b", [r"$\mathbf n=\langle6,3,2\rangle$, $\ |\mathbf n|=\sqrt{36+9+4}=7$. 원점 $O$ 에서 평면 위의 점 $P$ 로 가는 벡터 $\overrightarrow{OP}=\langle1,2,3\rangle$",
                   r"$\operatorname{comp}_{\mathbf n}\overrightarrow{OP}=\dfrac{6+6+6}{7}=\dfrac{18}{7}$ → 원점과 접평면 사이의 거리는 $\dfrac{18}7$"]),
            ("c", [r"$\operatorname{proj}_{\mathbf n}\overrightarrow{OP}=\dfrac{18}{49}\langle6,3,2\rangle$ 은 원점에서 평면에 내린 수선 벡터예요.",
                   r"가장 가까운 점 $\Big(\dfrac{108}{49},\ \dfrac{54}{49},\ \dfrac{36}{49}\Big)$ (확인: $\frac{648+162+72}{49}=\frac{882}{49}=18$ 이라 평면 위)"])],
  check=_c)


def _c():
    Ia = integrate(2*y/(1 + y**4), (y, 0, 1))
    assert EQ(Ia, pi/4)
    num_a = mp.quad(lambda X: mp.quad(lambda Y: 2/(1 + Y**4), [X, 1]), [0, 1])
    assert abs(num_a - mp.pi/4) < 1e-12
    assert integrate(1, (y, 0, x), (x, 0, z)) == z**2/2
    Ib = integrate(3*z**2*log(1 + z**3), (z, 0, 1))
    assert EQ(Ib, 2*log(2) - 1)
    num_b = mp.quad(lambda Y: mp.quad(lambda X: mp.quad(lambda Z: 6*mp.log(1 + Z**3), [X, 1]), [Y, 1]), [0, 1])
    assert abs(num_b - (2*mp.log(2) - 1)) < 1e-8
Q(SE, id="q2", no="2", type="적분 순서 바꾸기 (이중·삼중)", ref="15.2 · 15.6", mins=7, topics=[8],
  types=["15-order", "15-order3"],
  stem=r"적분 순서를 바꾸어 다음 값을 구하시오.",
  parts=[("a", r"$\displaystyle\int_0^1\!\!\int_x^1\frac{2}{1+y^4}\,dy\,dx$ [4점]"),
         ("b", r"$\displaystyle\int_0^1\!\!\int_y^1\!\!\int_x^1 6\ln(1+z^3)\,dz\,dx\,dy$ [6점]")],
  answer=[("a", r"$\dfrac\pi4$"), ("b", r"$2\ln2-1$")],
  solution=[("a", [r"$\dfrac{1}{1+y^4}$ 은 $y$ 로 적분하기가 매우 번거로워요. 영역: $0\le x\le1,\ x\le y\le1$ → $0\le y\le1,\ 0\le x\le y$",
                   r"$$\begin{aligned}\int_0^1\!\!\int_0^y\frac{2}{1+y^4}\,dx\,dy&=\int_0^1\frac{2y}{1+y^4}\,dy\\&=\Big[\arctan(y^2)\Big]_0^1=\frac\pi4\end{aligned}$$ ($w=y^2$ 로 치환)"]),
            ("b", [r"$\ln(1+z^3)$ 을 $z$ 로 먼저 적분하기 어려우니 $z$ 를 가장 바깥으로 보내요.",
                   r"영역: $0\le y\le1,\ y\le x\le1,\ x\le z\le1$, 즉 $0\le y\le x\le z\le1$ → $0\le z\le1,\ 0\le x\le z,\ 0\le y\le x$",
                   r"$$\begin{aligned}&\int_0^1\!\!\int_0^z\!\!\int_0^x6\ln(1+z^3)\,dy\,dx\,dz\\&=\int_0^13z^2\ln(1+z^3)\,dz\quad(w=1+z^3)\\&=\int_1^2\ln w\,dw=\Big[w\ln w-w\Big]_1^2\\&=2\ln2-1\end{aligned}$$"])],
  check=_c)


def _c():
    Ia = integrate(r*r, (z, r**2, 1), (r, 0, 1), (th, 0, 2*pi))
    assert EQ(Ia, 4*pi/15)
    # 원래 직교좌표 반복적분: z 적분은 바로 → √(x²+y²)(1-x²-y²) 를 단위원판에서 수치적분
    num_a = mp.quad(lambda X: mp.quad(lambda Y: mp.sqrt(X*X + Y*Y)*(1 - X*X - Y*Y),
                                      [-mp.sqrt(1 - X*X), 0, mp.sqrt(1 - X*X)]), [-1, 0, 1])
    assert abs(num_a - 4*mp.pi/15) < 1e-6
    Ib = integrate(rho**4*cos(ph)*sin(ph), (rho, 0, 2), (ph, 0, pi/2), (th, 0, pi/2))
    assert EQ(Ib, 8*pi/5)
    # z 적분: ∫_0^{√(4-x²-y²)} z√(x²+y²+z²) dz = (8-(x²+y²)^{3/2})/3
    w = symbols('w', positive=True)
    assert simplify(integrate(z*sqrt(w + z**2), (z, 0, sqrt(4 - w))) - (8 - w**R(3, 2))/3) == 0
    num_b = mp.quad(lambda X: mp.quad(lambda Y: (8 - (X*X + Y*Y)**1.5)/3, [0, mp.sqrt(4 - X*X)]), [0, 2])
    assert abs(num_b - 8*mp.pi/5) < 1e-6
Q(SE, id="q3", no="3", type="원주좌표 · 구면좌표 삼중적분", ref="15.7 · 15.8", mins=9, topics=[5, 6],
  types=["15-cyl", "15-sphconv", "15-sph"],
  stem=r"다음 적분을 지시한 좌표계의 적분으로 바꾸어 쓰고, 그 값을 구하시오.",
  parts=[("a", r"원주좌표로 바꾸어 계산하시오. [5점] $$\int_{-1}^{1}\!\!\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\!\!\int_{x^2+y^2}^{1}\sqrt{x^2+y^2}\,dz\,dy\,dx$$"),
         ("b", r"구면좌표로 바꾸어 계산하시오. [5점] $$\int_0^2\!\!\int_0^{\sqrt{4-x^2}}\!\!\int_0^{\sqrt{4-x^2-y^2}}z\sqrt{x^2+y^2+z^2}\,dz\,dy\,dx$$")],
  answer=[("a", r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1\!\!\int_{r^2}^1r^2\,dz\,dr\,d\theta=\frac{4\pi}{15}$"),
          ("b", r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^{\pi/2}\!\!\int_0^2\rho^4\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=\frac{8\pi}{5}$")],
  solution=[("a", [r"영역 읽기: $(x,y)$ 는 단위원판 $x^2+y^2\le1$, $z$ 는 포물면 $z=r^2$ 부터 평면 $z=1$ 까지 → $0\le\theta\le2\pi,\ 0\le r\le1,\ r^2\le z\le1$",
                   r"$\sqrt{x^2+y^2}=r$, $\ dV=r\,dz\,dr\,d\theta$: $$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^1\!\!\int_{r^2}^1r^2\,dz\,dr\,d\theta\\&=2\pi\int_0^1(r^2-r^4)\,dr\\&=2\pi\Big(\frac13-\frac15\Big)=\frac{4\pi}{15}\end{aligned}$$"]),
            ("b", [r"영역 읽기: $x\ge0,\ y\ge0,\ z\ge0$ 이고 $x^2+y^2+z^2\le4$ → 구의 제1팔분공간 부분: $0\le\theta\le\frac\pi2,\ 0\le\phi\le\frac\pi2,\ 0\le\rho\le2$",
                   r"$z\sqrt{x^2+y^2+z^2}=\rho\cos\phi\cdot\rho$, $\ dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$: $$\begin{aligned}&\int_0^{\pi/2}\!\!\int_0^{\pi/2}\!\!\int_0^2\rho^4\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta\\&=\frac\pi2\cdot\Big[\frac{\sin^2\phi}{2}\Big]_0^{\pi/2}\cdot\frac{2^5}{5}\\&=\frac\pi2\cdot\frac12\cdot\frac{32}5=\frac{8\pi}{5}\end{aligned}$$"])],
  check=_c)


def _c():
    d = symbols('d', real=True)
    dy = expand((1 + d)**3 - 1)
    eps = 3*d + d**2
    assert expand(3*d + eps*d - dy) == 0 and eps.subs(d, 0) == 0
    w = symbols('w', positive=True)
    assert limit((1 - cos(w))/w**2, w, 0, '+') == R(1, 2)
    # 극좌표로 보면 r 만의 식 (θ 무관)
    rp = symbols('rp', positive=True)
    g = (1 - cos(x**2 + y**2))/(x**2 + y**2)**2
    assert simplify(g.subs({x: rp*cos(th), y: rp*sin(th)}) - (1 - cos(rp**2))/rp**4) == 0
    f = x*y**2/sqrt(x**2 + y**2)
    h = symbols('h', nonzero=True, real=True)
    assert simplify(f.subs({x: h, y: 0})) == 0 and simplify(f.subs({x: 0, y: h})) == 0
    e1 = y**2/sqrt(x**2 + y**2)
    assert simplify(e1*x - f) == 0
    for (a, b) in [(0.3, -0.4), (-1e-3, 2e-3), (5e-4, -5e-4), (0, 1e-3)]:
        assert abs(float(e1.subs({x: a, y: b}))) <= abs(b) + 1e-15
Q(SE, id="q4", no="4", type="미분가능성의 정의 · 극한의 존재성", ref="14.4 · 14.2", mins=9, topics=[4, 3],
  types=["14-differentiable", "14-limit"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"$g(x)=x^3$ 이고 $\Delta y=g(1+\Delta x)-g(1)$ 일 때, $\Delta y=g'(1)\,\Delta x+\varepsilon\,\Delta x$ 를 만족하는 $\varepsilon$ 을 $\Delta x$ 로 나타내고, $\Delta x\to0$ 이면 $\varepsilon\to0$ 임을 보이시오. [3점]"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{1-\cos(x^2+y^2)}{(x^2+y^2)^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"),
         ("c", r"$f(x,y)=\dfrac{xy^2}{\sqrt{x^2+y^2}}\ \big((x,y)\ne(0,0)\big)$, $\ f(0,0)=0$ 일 때, $f_x(0,0),\ f_y(0,0)$ 을 구하고 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>" + DEF7)],
  answer=[("a", r"$\varepsilon=3\Delta x+(\Delta x)^2\to0$"),
          ("b", r"$\dfrac12$"),
          ("c", r"$f_x(0,0)=f_y(0,0)=0$, 미분가능 $\Big(\varepsilon_1=\dfrac{(\Delta y)^2}{\sqrt{(\Delta x)^2+(\Delta y)^2}},\ \varepsilon_2=0\Big)$")],
  solution=[("a", [r"$g'(1)=3$, $\ \Delta y=(1+\Delta x)^3-1=3\Delta x+3(\Delta x)^2+(\Delta x)^3$",
                   r"$\Delta y=3\Delta x+\big(3\Delta x+(\Delta x)^2\big)\Delta x$ 이므로 $\varepsilon=3\Delta x+(\Delta x)^2$",
                   r"$\Delta x\to0$ 이면 $\varepsilon\to0$. (일반적으로 $\varepsilon=\frac{\Delta y}{\Delta x}-g'(a)$ 로 두면 미분의 정의에서 $\varepsilon\to0$ — 교수님이 설명한 유도와 같은 꼴이에요)"]),
            ("b", [r"$x^2+y^2=w$ 로 두면 $(x,y)\to(0,0)$ 일 때 $w\to0^+$ 이고, 식은 $w$ 만의 함수 $\dfrac{1-\cos w}{w^2}$ 가 돼요 (다가가는 방향과 무관).",
                   r"$\displaystyle\lim_{w\to0^+}\frac{1-\cos w}{w^2}=\lim_{w\to0^+}\frac{\sin w}{2w}=\frac12$ (로피탈) → 극한은 존재하고 값은 $\dfrac12$"]),
            ("c", [r"$f(h,0)=0,\ f(0,h)=0$ 이므로 $f_x(0,0)=f_y(0,0)=0$",
                   r"$$\begin{aligned}\Delta z&=f(\Delta x,\Delta y)-f(0,0)\\&=\underbrace{\frac{(\Delta y)^2}{\sqrt{(\Delta x)^2+(\Delta y)^2}}}_{\varepsilon_1}\,\Delta x+\underbrace{0}_{\varepsilon_2}\cdot\Delta y\end{aligned}$$",
                   r"$\dfrac{|\Delta y|}{\sqrt{(\Delta x)^2+(\Delta y)^2}}\le1$ 이므로 $|\varepsilon_1|\le|\Delta y|\to0$ (조임정리), $\ \varepsilon_2=0$ → 정의를 만족하므로 원점에서 **미분가능**해요."])],
  check=_c)


def _c():
    A = integrate(16*sin(2*th)**2/2, (th, 0, 2*pi))
    assert EQ(A, 8*pi)
    B = integrate(r**3, (r, 0, 4*sin(2*th)), (th, 0, pi/2))
    assert EQ(B, 12*pi)
    assert EQ(integrate(sin(u)**4, (u, 0, pi)), 3*pi/8)
    assert EQ(4*sin(2*(pi/8)), 2*sqrt(2)) and EQ(4*sin(2*(3*pi/8)), 2*sqrt(2))
    one = integrate((16*sin(2*th)**2 - 8)/2, (th, pi/8, 3*pi/8))
    assert EQ(one, 2) and EQ(4*one, 8)
    assert simplify((16*sin(2*th)**2 - 8)/2 + 4*cos(4*th)) == 0
    num = mp.quad(lambda a: max((4*mp.sin(2*a))**2 - 8, 0)/2, mp.linspace(0, 2*mp.pi, 33))
    assert abs(num - 8) < 1e-10
Q(SE, id="q5", no="5", type="극좌표 이중적분 (장미곡선)", ref="15.3", mins=8, topics=[1],
  types=["15-polar"],
  stem=r"장미곡선 $r=4\sin2\theta$ (꽃잎 4장)에 대하여",
  parts=[("a", r"장미곡선 전체로 둘러싸인 영역의 넓이를 구하시오. [3점]"),
         ("b", r"제1사분면의 꽃잎 $D\ \big(0\le\theta\le\frac\pi2\big)$ 에서 $\displaystyle\iint_D(x^2+y^2)\,dA$ 를 구하시오. [3점]"),
         ("c", r"장미곡선의 내부이면서 원 $r=2\sqrt2$ 의 외부인 영역(꽃잎 4장 전체)의 넓이를 구하시오. [4점]")],
  answer=[("a", r"$8\pi$"), ("b", r"$12\pi$"), ("c", r"$8$")],
  solution=[("a", [r"$$\begin{aligned}A&=\frac12\int_0^{2\pi}16\sin^22\theta\,d\theta\\&=4\int_0^{2\pi}(1-\cos4\theta)\,d\theta=8\pi\end{aligned}$$ ($0\le\theta\le2\pi$ 동안 꽃잎 4장을 한 번씩 그려요. 꽃잎 한 장은 $2\pi$)"]),
            ("b", [r"$$\begin{aligned}\iint_Dr^2\,dA&=\int_0^{\pi/2}\!\!\int_0^{4\sin2\theta}r^3\,dr\,d\theta\\&=64\int_0^{\pi/2}\sin^42\theta\,d\theta\end{aligned}$$",
                   r"$u=2\theta$ 로 치환하고 $\sin^4u=\dfrac38-\dfrac12\cos2u+\dfrac18\cos4u$: $\ 32\displaystyle\int_0^{\pi}\sin^4u\,du=32\cdot\frac{3\pi}{8}=12\pi$"]),
            ("c", [r"교점: $4\sin2\theta=2\sqrt2 \Rightarrow \sin2\theta=\frac{\sqrt2}2 \Rightarrow \theta=\frac\pi8,\ \frac{3\pi}8$ (제1사분면 꽃잎)",
                   r"$$\begin{aligned}&\frac12\int_{\pi/8}^{3\pi/8}\big(16\sin^22\theta-8\big)\,d\theta\\&=\int_{\pi/8}^{3\pi/8}(-4\cos4\theta)\,d\theta\\&=-\Big[\sin4\theta\Big]_{\pi/8}^{3\pi/8}=-(-1-1)=2\end{aligned}$$",
                   r"꽃잎 4장이 합동이므로 $4\times2=8$ (답에 $\pi$ 가 없어요)"])],
  check=_c)


def _c():
    F = exp(x*z) + y*z - 3
    assert F.subs({x: 0, y: 2, z: 1}) == 0
    Fx, Fy, Fz = [diff(F, w_).subs({x: 0, y: 2, z: 1}) for w_ in (x, y, z)]
    assert (Fx, Fy, Fz) == (1, 1, 2)
    zx, zy = -Fx/Fz, -Fy/Fz
    assert (zx, zy) == (-R(1, 2), -R(1, 2))
    # 풀이에 쓴 식 그대로: x 로 미분 e^{xz}(z + x z_x) + y z_x = 0, y 로 미분 e^{xz} x z_y + z + y z_y = 0
    p, q = symbols('p q', real=True)
    eqx = exp(x*z)*(z + x*p) + y*p
    eqy = exp(x*z)*x*q + z + y*q
    assert solve(eqx.subs({x: 0, y: 2, z: 1}), p) == [zx] and solve(eqy.subs({x: 0, y: 2, z: 1}), q) == [zy]
    # 수치: z(x,y) 를 뉴턴법으로 풀어 차분과 비교
    def zval(X, Y):
        return mp.findroot(lambda Z: mp.e**(X*Z) + Y*Z - 3, 1)
    hh = mp.mpf('1e-6')
    assert abs((zval(hh, 2) - zval(-hh, 2))/(2*hh) + 0.5) < 1e-6
    assert abs((zval(0, 2 + hh) - zval(0, 2 - hh))/(2*hh) + 0.5) < 1e-6
    gz = Matrix([zx, zy])
    assert EQ(gz.norm(), sqrt(2)/2)
    uu = Matrix([3, -4]) / 5
    assert gz.dot(uu) == R(1, 10)
Q(SE, id="q6", no="6", type="연쇄법칙 (음함수) · 그래디언트", ref="14.5 · 14.6", mins=8, topics=[12, 10],
  types=["14-implicit", "14-maxrate", "14-dir"],
  stem=r"방정식 $e^{xz}+yz=3$ 이 점 $(0,\ 2,\ 1)$ 근처에서 $z=z(x,y)$ 를 정한다.",
  parts=[("a", r"양변을 $x,\ y$ 에 대해 연쇄법칙으로 미분하여 $z_x(0,2),\ z_y(0,2)$ 를 구하시오. [4점]"),
         ("b", r"$(0,2)$ 에서 $\nabla z$ 를 구하고, $z$ 가 가장 빠르게 증가하는 방향(단위벡터)과 그 변화율을 구하시오. [3점]"),
         ("c", r"$(0,2)$ 에서 벡터 $\langle3,\ -4\rangle$ 방향으로의 $z$ 의 방향도함수를 구하시오. [3점]")],
  answer=[("a", r"$z_x(0,2)=-\dfrac12,\ \ z_y(0,2)=-\dfrac12$"),
          ("b", r"$\nabla z(0,2)=\big\langle-\frac12,\ -\frac12\big\rangle$, 방향 $\dfrac{1}{\sqrt2}\langle-1,\ -1\rangle$, 변화율 $\dfrac{\sqrt2}{2}$"),
          ("c", r"$\dfrac1{10}$")],
  solution=[("a", [r"$x$ 로 미분 ($z$ 는 $x,y$ 의 함수): $e^{xz}(z+x\,z_x)+y\,z_x=0$ → $(0,2,1)$ 에서 $1\cdot(1+0)+2z_x=0 \Rightarrow z_x=-\dfrac12$",
                   r"$y$ 로 미분: $e^{xz}\,x\,z_y+z+y\,z_y=0$ → $(0,2,1)$ 에서 $0+1+2z_y=0 \Rightarrow z_y=-\dfrac12$",
                   r"(공식 $z_x=-\dfrac{F_x}{F_z},\ z_y=-\dfrac{F_y}{F_z}$, $F=e^{xz}+yz-3$ 으로 구해도 같아요: $F_x=1,\ F_y=1,\ F_z=2$)"]),
            ("b", [r"$\nabla z(0,2)=\langle z_x,\ z_y\rangle=\big\langle-\frac12,-\frac12\big\rangle$",
                   r"가장 빠르게 증가하는 방향 $\dfrac{\nabla z}{|\nabla z|}=\dfrac1{\sqrt2}\langle-1,-1\rangle$, 변화율 $|\nabla z|=\sqrt{\frac14+\frac14}=\dfrac{\sqrt2}2$"]),
            ("c", [r"단위벡터 $\mathbf u=\dfrac15\langle3,-4\rangle$",
                   r"$D_{\mathbf u}z=\nabla z\cdot\mathbf u=\dfrac{-3+4}{10}=\dfrac1{10}$"])],
  check=_c)


def _c():
    J = Matrix([[diff(x*y, x), diff(x*y, y)], [diff(y/x, x), diff(y/x, y)]]).det()
    assert simplify(J - 2*y/x) == 0
    up, vp = symbols('up vp', positive=True)
    xs, ys = sqrt(up/vp), sqrt(up*vp)
    assert simplify(xs*ys - up) == 0 and simplify(ys/xs - vp) == 0
    Jinv = Matrix([[diff(xs, up), diff(xs, vp)], [diff(ys, up), diff(ys, vp)]]).det()
    assert simplify(Jinv - 1/(2*vp)) == 0
    assert simplify(xs*ys*(ys/xs) - ys**2) == 0
    val = integrate(up*vp/(2*vp), (up, 1, 4), (vp, 1, 4))
    assert val == R(45, 4)
    # 원래 영역에서 수치적분: x∈[1/2,1] 은 1/x ≤ y ≤ 4x, x∈[1,2] 는 x ≤ y ≤ 4/x
    num = (mp.quad(lambda X: mp.quad(lambda Y: Y*Y, [1/X, 4*X]), [0.5, 1])
           + mp.quad(lambda X: mp.quad(lambda Y: Y*Y, [X, 4/X]), [1, 2]))
    assert abs(num - mp.mpf(45)/4) < 1e-10
Q(SE, id="q7", no="7", type="변수변환 (야코비안)", ref="15.9", mins=9, topics=[7],
  types=["15-change"],
  stem=r"$R$ 은 제1사분면에서 곡선 $xy=1,\ xy=4$ 와 직선 $y=x,\ y=4x$ 로 둘러싸인 영역이다. 변환 $u=xy,\ v=\dfrac yx$ 를 이용하여",
  parts=[("a", r"$\dfrac{\partial(u,v)}{\partial(x,y)}$ 를 구하여 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 $u,v$ 로 나타내고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"),
         ("b", r"$\displaystyle\iint_Ry^2\,dA$ 를 구하시오. [6점]")],
  answer=[("a", r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac{1}{2v}$, $\ S=\{(u,v)\mid1\le u\le4,\ 1\le v\le4\}$"),
          ("b", r"$\dfrac{45}{4}$")],
  solution=[("a", [r"$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}y&x\\[2pt]-\frac{y}{x^2}&\frac1x\end{vmatrix}=\frac yx+\frac yx=\frac{2y}{x}=2v$$",
                   r"따라서 $\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac{1}{2v}$ (제1사분면이라 $v>0$). (역변환 $x=\sqrt{u/v},\ y=\sqrt{uv}$ 로 직접 계산해도 같아요)",
                   r"$xy=1,\ xy=4$ → $u=1,\ u=4$;  $\ y=x,\ y=4x$ → $v=1,\ v=4$ → $S:\ 1\le u\le4,\ 1\le v\le4$"]),
            ("b", [r"$uv=xy\cdot\dfrac yx=y^2$ 이므로 피적분함수는 $uv$, $\ dA=\dfrac{1}{2v}\,du\,dv$",
                   r"$$\begin{aligned}\iint_Ry^2\,dA&=\int_1^4\!\!\int_1^4uv\cdot\frac1{2v}\,du\,dv\\&=\frac12\int_1^4\!\!\int_1^4u\,du\,dv=\frac12\cdot\frac{15}{2}\cdot3=\frac{45}{4}\end{aligned}$$"])],
  check=_c)


def _c():
    T = symbols('T', nonnegative=True)
    rr = Matrix([3*T**2, 2*T**3])
    vt = rr.diff(T)
    assert simplify(vt.norm() - 6*T*sqrt(1 + T**2)) == 0
    L = integrate(6*T*sqrt(1 + T**2), (T, 0, sqrt(3)))
    assert EQ(L, 14)
    num = nquad(lambda q: mp.sqrt(36*q*q + 36*q**4), 0, mp.sqrt(3))
    assert abs(num - 14) < 1e-10
    vv, aa = vt.subs(T, 1), rr.diff(T, 2).subs(T, 1)
    assert list(vv) == [6, 6] and list(aa) == [6, 12] and vv.dot(aa) == 108
    assert EQ(vv.dot(aa) / vv.norm(), 9*sqrt(2))
    proj = (vv.dot(aa) / vv.dot(vv)) * vv
    assert list(proj) == [9, 9]
    orth = aa - proj
    assert list(orth) == [-3, 3] and orth.dot(vv) == 0 and EQ(orth.norm(), 3*sqrt(2))
Q(SE, id="q8", no="8", type="곡선의 길이 · 사영(comp·proj)", ref="13.3 · 12.3", mins=6, topics=[11, 13],
  types=["13-arc", "12-proj"],
  stem=r"평면곡선 $\mathbf r(t)=\langle 3t^2,\ 2t^3\rangle$ 에 대하여",
  parts=[("a", r"$0\le t\le\sqrt3$ 부분의 길이를 구하시오. [3점]"),
         ("b", r"$t=1$ 에서의 $\mathbf v=\mathbf r'(1),\ \mathbf a=\mathbf r''(1)$ 에 대하여 $\operatorname{comp}_{\mathbf v}\mathbf a$ 와 $\operatorname{proj}_{\mathbf v}\mathbf a$ 를 구하시오. [4점]"),
         ("c", r"$\mathbf a$ 를 $\mathbf v$ 에 평행한 벡터와 $\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [3점]")],
  answer=[("a", r"$14$"),
          ("b", r"$\operatorname{comp}_{\mathbf v}\mathbf a=9\sqrt2$, $\ \operatorname{proj}_{\mathbf v}\mathbf a=\langle9,\ 9\rangle$"),
          ("c", r"$\mathbf a=\langle9,9\rangle+\langle-3,3\rangle$, 수직인 벡터의 크기 $3\sqrt2$")],
  solution=[("a", [r"$\mathbf r'(t)=\langle6t,\ 6t^2\rangle$, $\ |\mathbf r'(t)|=6t\sqrt{1+t^2}\ (t\ge0)$",
                   r"$w=1+t^2$ 로 치환: $$\begin{aligned}L&=\int_0^{\sqrt3}6t\sqrt{1+t^2}\,dt=\int_1^43\sqrt w\,dw\\&=\Big[2w^{3/2}\Big]_1^4=16-2=14\end{aligned}$$"]),
            ("b", [r"$\mathbf r''(t)=\langle6,\ 12t\rangle$ → $\mathbf v=\langle6,6\rangle$, $\ \mathbf a=\langle6,12\rangle$, $\ |\mathbf v|=6\sqrt2$, $\ \mathbf a\cdot\mathbf v=36+72=108$",
                   r"$\operatorname{comp}_{\mathbf v}\mathbf a=\dfrac{108}{6\sqrt2}=9\sqrt2$, $\quad\operatorname{proj}_{\mathbf v}\mathbf a=\dfrac{108}{72}\langle6,6\rangle=\langle9,\ 9\rangle$"]),
            ("c", [r"수직 성분: $\mathbf a-\operatorname{proj}_{\mathbf v}\mathbf a=\langle-3,\ 3\rangle$ (확인: $\langle-3,3\rangle\cdot\langle6,6\rangle=0$)",
                   r"크기 $\sqrt{9+9}=3\sqrt2$"])],
  check=_c)


def _c():
    P, Qf = x**2 - y, x + y**2
    c1 = integrate(P.subs(y, 0), (x, -3, 3))
    assert c1 == 18
    X, Y = 3*cos(t), 2*sin(t)
    arc = P.subs({x: X, y: Y}, simultaneous=True)*diff(X, t) + Qf.subs({x: X, y: Y}, simultaneous=True)*diff(Y, t)
    target = -27*cos(t)**2*sin(t) + 6*sin(t)**2 + 6*cos(t)**2 + 8*sin(t)**2*cos(t)
    assert simplify(arc - target) == 0
    c2 = integrate(arc, (t, 0, pi))
    assert EQ(c2, 6*pi - 18) and EQ(c1 + c2, 6*pi)
    assert diff(Qf, x) - diff(P, y) == 2
    area = integrate(2*sqrt(1 - x**2/9), (x, -3, 3))
    assert EQ(area, 3*pi) and EQ(2*area, 6*pi)
    A2 = integrate((X*diff(Y, t) - Y*diff(X, t))/2, (t, 0, pi))
    assert EQ(A2, 3*pi)
    num = mp.quad(lambda q: (9*mp.cos(q)**2 - 2*mp.sin(q))*(-3*mp.sin(q)) + (3*mp.cos(q) + 4*mp.sin(q)**2)*(2*mp.cos(q)),
                  [0, mp.pi]) + 18
    assert abs(num - 6*mp.pi) < 1e-10
Q(SE, id="q9", no="9", type="그린 정리 · 곡선 나누어 직접 계산", ref="16.2 · 16.4", mins=9, topics=[9],
  types=["16-green", "16-greenarea", "16-vector"],
  stem=r"$D$ 는 위쪽 반타원 영역 $\dfrac{x^2}{9}+\dfrac{y^2}{4}\le1,\ y\ge0$ 이고, $C$ 는 $D$ 의 경계로 양의 방향이다. $\displaystyle I=\oint_C(x^2-y)\,dx+(x+y^2)\,dy$ 에 대하여",
  parts=[("a", r"$C$ 를 선분과 반타원 호로 나누어 $I$ 를 직접 계산하시오. [4점]"),
         ("b", r"그린 정리를 이용해 $I$ 를 계산하시오. [4점]"),
         ("c", r"$\displaystyle A=\frac12\oint_Cx\,dy-y\,dx$ 를 계산하여 $D$ 의 넓이를 구하시오. [2점]")],
  answer=[("a", r"$6\pi$"), ("b", r"$6\pi$"), ("c", r"$3\pi$")],
  solution=[("a", [r"양의 방향: $C_1$ 은 $x$축 위 선분 $(-3,0)\to(3,0)$, $C_2$ 는 호 $x=3\cos t,\ y=2\sin t\ (0\le t\le\pi)$",
                   r"$C_1:\ y=0,\ dy=0$ → $\displaystyle\int_{-3}^3x^2\,dx=18$",
                   r"$C_2$: $dx=-3\sin t\,dt,\ dy=2\cos t\,dt$ $$\begin{aligned}&\int_0^\pi\Big[(9\cos^2t-2\sin t)(-3\sin t)\\&\qquad+(3\cos t+4\sin^2t)(2\cos t)\Big]dt\\&=\int_0^\pi\big(-27\cos^2t\sin t+6\sin^2t\\&\qquad+6\cos^2t+8\sin^2t\cos t\big)\,dt\\&=-18+3\pi+3\pi+0=6\pi-18\end{aligned}$$",
                   r"$I=18+(6\pi-18)=6\pi$"]),
            ("b", [r"$P=x^2-y,\ Q=x+y^2$ → $Q_x-P_y=1-(-1)=2$",
                   r"$I=\displaystyle\iint_D2\,dA=2\times(\text{반타원의 넓이})=2\cdot\frac{\pi\cdot3\cdot2}{2}=6\pi$ — (a)와 같아요."]),
            ("c", [r"$C_1$ 에서는 $y=0,\ dy=0$ 이라 $0$.  $C_2$: $x\,dy-y\,dx=(3\cos t)(2\cos t)\,dt-(2\sin t)(-3\sin t)\,dt=6\,dt$",
                   r"$A=\dfrac12\displaystyle\int_0^\pi6\,dt=3\pi$ (반타원 넓이 $\frac12\pi ab$ 와 같아요)"])],
  check=_c)


def _c():
    lam = symbols('lam', real=True)
    f = x*y*z
    h = x + 2*y + 3*z
    sols = solve([diff(f, x) - lam, diff(f, y) - 2*lam, diff(f, z) - 3*lam, h - 18], [x, y, z, lam], dict=True)
    pos = [sl for sl in sols if all(sl[w_] > 0 for w_ in (x, y, z))]
    assert len(pos) == 1 and (pos[0][x], pos[0][y], pos[0][z]) == (6, 3, 2) and f.subs(pos[0]) == 36
    best = max(a*b*(18 - a - 2*b)/3 for a in [i/4 for i in range(1, 72)] for b in [j/4 for j in range(1, 36)]
               if 18 - a - 2*b > 0)
    assert best <= 36 + 1e-9 and best > 35.9
    g = x**3 - 12*x + y**3 - 3*y
    crit = solve([diff(g, x), diff(g, y)], [x, y], dict=True)
    assert sorted((c[x], c[y]) for c in crit) == [(-2, -1), (-2, 1), (2, -1), (2, 1)]
    D = lambda a, b: (diff(g, x, 2)*diff(g, y, 2) - diff(g, x, y)**2).subs({x: a, y: b})
    assert D(2, 1) == 72 and diff(g, x, 2).subs(x, 2) == 12 and g.subs({x: 2, y: 1}) == -18
    assert D(-2, -1) == 72 and diff(g, x, 2).subs(x, -2) == -12 and g.subs({x: -2, y: -1}) == 18
    assert D(2, -1) == -72 and D(-2, 1) == -72
Q(SE, id="q10", no="10", type="라그랑주 승수법 · 2계 도함수 판정법", ref="14.8 · 14.7", mins=9, topics=[2, 15],
  types=["14-lagrange", "14-crit"],
  stem=r"다음 물음에 답하시오.",
  parts=[("a", r"라그랑주 승수법으로 평면 $x+2y+3z=18$ 의 제1팔분공간 부분($x,y,z>0$)에서 $f(x,y,z)=xyz$ 의 최댓값을 구하시오. [5점]"),
         ("b", r"$g(x,y)=x^3-12x+y^3-3y$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]")],
  answer=[("a", r"최댓값 $36$ (점 $(6,\ 3,\ 2)$)"),
          ("b", r"$(2,1)$: 극솟값 $-18$,  $(-2,-1)$: 극댓값 $18$,  $(2,-1),\ (-2,1)$: 안장점")],
  solution=[("a", [r"$\nabla f=\lambda\nabla h$, $\ h=x+2y+3z$: $\ yz=\lambda,\ \ xz=2\lambda,\ \ xy=3\lambda$",
                   r"$x,y,z>0$ 이므로 첫 두 식을 나누면 $\dfrac xy=2 \Rightarrow x=2y$, 첫·셋째 식을 나누면 $\dfrac xz=3 \Rightarrow x=3z$",
                   r"제약식에 대입: $x+x+x=18 \Rightarrow x=6,\ y=3,\ z=2$ → $f=36$",
                   r"좌표 중 하나가 $0$ 에 가까워지면 $f\to0$ 이므로 이 값이 최댓값이에요."]),
            ("b", [r"$g_x=3x^2-12=0 \Rightarrow x=\pm2$, $\ g_y=3y^2-3=0 \Rightarrow y=\pm1$ → 임계점 4개 $(\pm2,\ \pm1)$",
                   r"$g_{xx}=6x,\ g_{yy}=6y,\ g_{xy}=0$ → $D=36xy$",
                   r"$(2,1)$: $D=72>0,\ g_{xx}=12>0$ → 극솟값 $g=8-24+1-3=-18$.  $(-2,-1)$: $D=72>0,\ g_{xx}=-12<0$ → 극댓값 $g=-8+24-1+3=18$",
                   r"$(2,-1),\ (-2,1)$: $D=-72<0$ → 안장점"])],
  check=_c)

SETS.append({"id": "e", "no": 5, "label": "E", "title": "모의고사 E세트", "focus": "15개 주제 · 10문항 · 각 10점",
        "lead": "다섯 번째 세트예요. 등위곡면의 접평면과 원점까지의 거리(사영)로 시작해서 적분 순서 바꾸기, 직교좌표 적분을 원주·구면좌표로 바꾸기, 교수님이 예고한 일변수 증분식을 구체적인 함수로 써 보는 미분가능성 문항과 극좌표로 보는 극한, 네 잎 장미곡선과 원, 음함수 연쇄법칙과 그래디언트, 비선형 변수변환(u = xy, v = y/x), 평면곡선의 길이와 사영, 반타원 그린 정리, 라그랑주 승수법과 극값 판정을 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
        "problems": SE})


def check_all():
    """모든 세트·문항의 check 를 실행. (이름, 통과 여부, 오류) 목록을 돌려줘요."""
    out = []
    for S in SETS:
        assert len(S["problems"]) == 10, f"{S['id']} 문항 수 {len(S['problems'])}"
        for q in S["problems"]:
            try:
                q["check"]()
                out.append((f"{S['id']}-{q['id']}", True, None))
            except Exception as e:  # noqa: BLE001
                out.append((f"{S['id']}-{q['id']}", False, repr(e)))
    return out


if __name__ == "__main__":
    import time
    for S in SETS:
        for q in S["problems"]:
            t0 = time.time()
            try:
                q["check"]()
                print(f"OK   {S['id']}-{q['id']}  ({time.time() - t0:.1f}s)")
            except Exception as e:  # noqa: BLE001
                import traceback
                print(f"FAIL {S['id']}-{q['id']}  {e!r}")
                traceback.print_exc()

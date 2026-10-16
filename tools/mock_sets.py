# -*- coding: utf-8 -*-
"""중간고사 모의고사 A·B 세트 (mock.html?set=1·2) — 문제 · 정답 · 풀이 원본과 sympy 검산.

두 세트 모두 시험 범위의 15개 주제(TOPICS)를 10문항(각 10점)에 빠짐없이 담고,
75–90분 안에 평균 70점 정도가 나오도록 소문항 배점과 계산량을 맞췄어요. 단원 순서는 섞어 배치했어요.

문항마다
  id, no, type(유형 이름), ref(단원), mins(권장 풀이 시간, 분), topics(주제 번호),
  stem, parts, answer, solution, types(문제 은행 유형 키 — '비슷한 문제' 링크), check(검산 함수)
를 가져요. build.py 가 check 를 모두 실행하고, 세트마다 15개 주제가 다 들어 있는지와
권장 시간 합이 75–90분인지 확인한 뒤 assets/mock-problems.js 로 내보내요.
"""
import random

import mpmath as mp
from sympy import (Matrix, Rational as R, sqrt, pi, E, exp, log, sin, cos, atan,
                   integrate, diff, simplify, symbols, limit, solve, N, sympify, expand, lambdify)

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
  types=["14-dne", "14-defpartial"],
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
  types=[],
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
  types=["14-dne", "14-defpartial"],
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
  types=[],
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

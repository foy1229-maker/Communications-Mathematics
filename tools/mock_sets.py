# -*- coding: utf-8 -*-
"""실전 모의고사 1–5회 (mock.html?set=1…5) — 문제 · 정답 · 풀이 원본과 sympy 검산.

각 회는 실제 시험처럼 10문항 × 10점. 문항마다
  id, no, type(유형 이름), ref(근거 기출·자료), stem, parts, answer, solution,
  types(문제 은행 유형 키 — '비슷한 문제' 링크), check(검산 함수)
를 가져요. build.py 가 check 를 모두 실행한 뒤 assets/mock-problems.js 의 sets 로 내보내요.
"""
import mpmath as mp
from sympy import (Matrix, Rational as R, sqrt, pi, E, exp, log, sin, cos, tan, atan, Abs,
                   integrate, diff, simplify, symbols, limit, solve, N, sympify, oo, expand, lambdify, Function)

x, y, z, t, s, r, u, v = symbols('x y z t s r u v', real=True)
th, ph, rho, k, m = symbols('theta phi rho k m', real=True)


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
    sub = dict(zip(vs, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


def line_num(F, rr, a, b, vs=(x, y, z), pts=None):
    sub = dict(zip(vs, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    fn = lambdify(t, integrand, 'mpmath')
    nodes = pts if pts else [a, b]
    return mp.quad(fn, [mp.mpf(float(N(q, 30))) for q in nodes])


def taylor2(x0, y0, val, fx, fy, fxx, fxy, fyy):
    X, Y = x - x0, y - y0
    return val + fx*X + fy*Y + R(1, 2)*fxx*X**2 + fxy*X*Y + R(1, 2)*fyy*Y**2


SETS = []


def Q(store, **kw):
    for key in ("id", "no", "type", "ref", "stem", "parts", "answer", "solution", "types", "check"):
        assert key in kw, f"{kw.get('id')} missing {key}"
    store.append(kw)


# ════════════════════════════════════════════════════════════════════
# 1회 — 예상 유형 10선 (표준)
# ════════════════════════════════════════════════════════════════════
S1 = []


def _c():
    I_a = integrate(r*r, (r, 0, sqrt(2)), (th, 0, pi/4))
    assert EQ(I_a, sqrt(2)*pi/6)
    num = mp.quad(lambda Y: mp.quad(lambda X: mp.sqrt(X*X + Y*Y), [Y, mp.sqrt(2 - Y*Y)]), [0, 1])
    assert abs(num - mp.sqrt(2)*mp.pi/6) < 1e-10
    I_b = integrate(r*sin(th)*r, (r, 1, 2*sin(th)), (th, pi/6, 5*pi/6))
    assert EQ(I_b, 2*pi/3 + sqrt(3)/4)
    assert EQ(integrate(sin(th)**4, (th, pi/6, 5*pi/6)), pi/4 + 7*sqrt(3)/32)
Q(S1, id="q1", no="1", type="극좌표 이중적분", ref="2025 중간 1번 · 2(b) 유형", types=["15-polar"],
  stem="",
  parts=[("a", r"극좌표로 바꾸어 계산하시오. $\displaystyle\int_0^1\!\!\int_{y}^{\sqrt{2-y^2}}\sqrt{x^2+y^2}\,dx\,dy$"),
         ("b", r"원 $x^2+y^2=2y$ 의 내부이면서 원 $x^2+y^2=1$ 의 외부인 영역을 $D$ 라 할 때 $\displaystyle\iint_D y\,dA$ 를 구하시오.")],
  answer=[("a", r"$\dfrac{\sqrt2\,\pi}{6}$"), ("b", r"$\dfrac{2\pi}{3}+\dfrac{\sqrt3}{4}$")],
  solution=[("a", [r"영역: $0\le y\le1,\ y\le x\le\sqrt{2-y^2}$ → 직선 $y=x$ 아래, $x$축 위, 원 $x^2+y^2=2$ 안의 부채꼴 → $0\le\theta\le\frac\pi4,\ 0\le r\le\sqrt2$",
                   r"$$\int_0^{\pi/4}\!\!\int_0^{\sqrt2}r\cdot r\,dr\,d\theta=\frac\pi4\cdot\frac{2\sqrt2}{3}=\frac{\sqrt2\,\pi}{6}$$"]),
            ("b", [r"$x^2+y^2=2y \iff r=2\sin\theta$. 교점 $2\sin\theta=1 \Rightarrow \theta=\frac\pi6,\ \frac{5\pi}6$ → $D:\ \frac\pi6\le\theta\le\frac{5\pi}6,\ 1\le r\le2\sin\theta$",
                   r"$$\begin{aligned}\iint_Dy\,dA&=\int_{\pi/6}^{5\pi/6}\!\!\int_1^{2\sin\theta}r^2\sin\theta\,dr\,d\theta\\&=\frac13\int_{\pi/6}^{5\pi/6}\big(8\sin^4\theta-\sin\theta\big)\,d\theta\end{aligned}$$",
                   r"$\displaystyle\int_{\pi/6}^{5\pi/6}\sin^4\theta\,d\theta=\Big[\tfrac{3\theta}8-\tfrac{\sin2\theta}4+\tfrac{\sin4\theta}{32}\Big]_{\pi/6}^{5\pi/6}=\frac\pi4+\frac{7\sqrt3}{32}$, $\displaystyle\int_{\pi/6}^{5\pi/6}\sin\theta\,d\theta=\sqrt3$",
                   r"$\dfrac13\Big(2\pi+\dfrac{7\sqrt3}{4}-\sqrt3\Big)=\dfrac{2\pi}3+\dfrac{\sqrt3}4$"])],
  check=_c)


def _c():
    f = x**2*y**2/(x**2 + y**2)**R(3, 2)
    assert limit(f.subs({x: r*cos(R(1, 3)), y: r*sin(R(1, 3))}), r, 0, '+') == 0
    g = x*y**2/(x**2 + 4*y**4)
    kk = symbols('kk', real=True)
    assert simplify(limit(g.subs(x, kk*y**2), y, 0) - kk/(kk**2 + 4)) == 0
    h = (x**3 - y**3)/(x**2 + y**2)
    hh = symbols('hh', nonzero=True)
    assert simplify(h.subs({x: hh, y: 0})/hh) == 1 and simplify(h.subs({x: 0, y: hh})/hh) == -1
Q(S1, id="q2", no="2", type="극한과 연속", ref="2025 중간 3번 · 2022 중간 블럭2 2번 유형", types=["14-limit", "14-dne", "14-defpartial"],
  stem="다음 물음에 답하시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y^2}{(x^2+y^2)^{3/2}}$ 를 구하시오."),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy^2}{x^2+4y^4}$ 가 존재하지 않음을 보이시오."),
         ("c", r"$g(x,y)=\dfrac{x^3-y^3}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $g(0,0)=0$ 일 때 $g$ 가 원점에서 연속임을 보이고 $g_x(0,0),\ g_y(0,0)$ 을 구하시오.")],
  answer=[("a", r"$0$"), ("b", r"곡선 $x=ky^2$ 을 따라 $\dfrac{k}{k^2+4}$ → 존재하지 않음"), ("c", r"연속, $g_x(0,0)=1,\ g_y(0,0)=-1$")],
  solution=[("a", [r"극좌표: $\dfrac{r^4\cos^2\theta\sin^2\theta}{r^3}=r\cos^2\theta\sin^2\theta$, $0\le|\cdot|\le r\to0$ → 극한 $0$"]),
            ("b", [r"직선 $y=mx$ 로는 $\dfrac{m^2x^3}{x^2+4m^4x^4}\to0$ 이라 판정이 안 돼요. 분모 차수를 맞추는 곡선 $x=ky^2$:",
                   r"$\dfrac{ky^4}{k^2y^4+4y^4}=\dfrac{k}{k^2+4}$ → $k=0$ 이면 $0$, $k=2$ 이면 $\frac14$ → 존재하지 않음"]),
            ("c", [r"$|x^3-y^3|\le|x|^3+|y|^3\le\sqrt{x^2+y^2}\,(x^2+y^2)$ → $|g(x,y)|\le\sqrt{x^2+y^2}\to0=g(0,0)$ → 연속",
                   r"$g_x(0,0)=\displaystyle\lim_{h\to0}\frac{g(h,0)-0}{h}=\lim\frac{h^3/h^2}{h}=1$,  $g_y(0,0)=\displaystyle\lim_{h\to0}\frac{-h^3/h^2}{h}=-1$"])],
  check=_c)


def _c():
    F = x**2*y + y**2*z + z**2*x
    P0 = {x: 1, y: 1, z: 1}
    assert F.subs(P0) == 3 and grad(F, (x, y, z)).subs(P0) == Matrix([3, 3, 3])
    G = x**2 + 4*y**2 + z**2
    kk = symbols('kk')
    pts = solve([2*x - 2*kk, 8*y - 4*kk, 2*z - kk, G - 9], [x, y, z, kk], dict=True)
    got = sorted([(q[x], q[y], q[z]) for q in pts], key=lambda p: float(p[0]))
    assert got == [(-2, -1, -1), (2, 1, 1)]
    assert 2*2 + 4*1 + 1 == 9
Q(S1, id="q3", no="3", type="접평면과 법선", ref="2022 중간 블럭1 7번 · 강의 14.6 유형", types=["14-levelsurf", "14-tangent"],
  stem="",
  parts=[("a", r"곡면 $x^2y+y^2z+z^2x=3$ 위의 점 $(1,1,1)$ 에서 접평면과 법선의 방정식을 구하시오."),
         ("b", r"타원면 $x^2+4y^2+z^2=9$ 위에서 접평면이 평면 $2x+4y+z=1$ 과 평행한 점을 모두 구하고, 각 점에서의 접평면을 구하시오.")],
  answer=[("a", r"접평면 $x+y+z=3$, 법선 $x-1=y-1=z-1$"), ("b", r"$(2,1,1)$: $2x+4y+z=9$,  $(-2,-1,-1)$: $2x+4y+z=-9$")],
  solution=[("a", [r"$F=x^2y+y^2z+z^2x$, $\nabla F=\langle2xy+z^2,\ x^2+2yz,\ y^2+2zx\rangle$ → $\nabla F(1,1,1)=\langle3,3,3\rangle$",
                   r"접평면 $3(x-1)+3(y-1)+3(z-1)=0 \Rightarrow x+y+z=3$, 법선 $x=1+t,\ y=1+t,\ z=1+t$"]),
            ("b", [r"$\nabla G=\langle2x,8y,2z\rangle=c\langle2,4,1\rangle$ → $x=c,\ y=\frac c2,\ z=\frac c2$",
                   r"대입: $c^2+c^2+\frac{c^2}{4}=\frac94c^2=9 \Rightarrow c=\pm2$ → 점 $(2,1,1)$, $(-2,-1,-1)$",
                   r"접평면 $2(x-2)+4(y-1)+(z-1)=0 \Rightarrow 2x+4y+z=9$, 반대 점에서는 $2x+4y+z=-9$"])],
  check=_c)


def _c():
    lam, mu = symbols('lam mu')
    sols = solve([1 - 2*lam*x, 2 - 2*lam*y, 2 - 2*lam*z, x**2 + y**2 + z**2 - 9], [x, y, z, lam], dict=True)
    vals = sorted([q[x] + 2*q[y] + 2*q[z] for q in sols])
    assert vals == [-9, 9]
    sols2 = solve([1 - 2*lam*x - mu, 1 - 2*lam*y, 1 - mu, x**2 + y**2 - 2, x + z - 1], [x, y, z, lam, mu], dict=True)
    vals2 = sorted([simplify(q[x] + q[y] + q[z]) for q in sols2], key=float)
    assert EQ(vals2[0], 1 - sqrt(2)) and EQ(vals2[-1], 1 + sqrt(2))
Q(S1, id="q4", no="4", type="라그랑주 승수법", ref="2025 중간 8번 유형", types=["14-lagrange", "14-lagrange2"],
  stem="라그랑주 승수법을 이용하여 다음을 구하시오.",
  parts=[("a", r"구 $x^2+y^2+z^2=9$ 위에서 $f(x,y,z)=x+2y+2z$ 의 최댓값과 최솟값"),
         ("b", r"원기둥 $x^2+y^2=2$ 와 평면 $x+z=1$ 의 교선 위에서 $f(x,y,z)=x+y+z$ 의 최댓값과 최솟값")],
  answer=[("a", r"최댓값 $9$ (점 $(1,2,2)$), 최솟값 $-9$ (점 $(-1,-2,-2)$)"), ("b", r"최댓값 $1+\sqrt2$ (점 $(0,\sqrt2,1)$), 최솟값 $1-\sqrt2$ (점 $(0,-\sqrt2,1)$)")],
  solution=[("a", [r"$\langle1,2,2\rangle=\lambda\langle2x,2y,2z\rangle$ → $x=\frac1{2\lambda},\ y=z=\frac1\lambda$",
                   r"대입: $\frac{1}{4\lambda^2}+\frac{2}{\lambda^2}=\frac{9}{4\lambda^2}=9 \Rightarrow \lambda=\pm\frac12$ → $(1,2,2)$ 에서 $9$, $(-1,-2,-2)$ 에서 $-9$"]),
            ("b", [r"$g=x^2+y^2=2,\ h=x+z=1$: $\langle1,1,1\rangle=\lambda\langle2x,2y,0\rangle+\mu\langle1,0,1\rangle$",
                   r"$z$성분: $\mu=1$ → $x$성분: $2\lambda x=0$, $y$성분: $2\lambda y=1$ 이므로 $\lambda\ne0$ → $x=0$",
                   r"$y=\pm\sqrt2,\ z=1-x=1$ → $f=1\pm\sqrt2$ → 최댓값 $1+\sqrt2$, 최솟값 $1-\sqrt2$"])],
  check=_c)


def _c():
    Ia = integrate(x**2*sqrt(x**3 + 1), (x, 0, 1))
    assert EQ(Ia, R(2, 9)*(2*sqrt(2) - 1))
    num = mp.quad(lambda Y: mp.quad(lambda X: mp.sqrt(X**3 + 1), [mp.sqrt(Y), 1]), [0, 1])
    assert abs(num - float(Ia)) < 1e-10
    V = integrate(x**2 + y**2, (y, x**2, 1), (x, -1, 1))
    assert EQ(V, R(88, 105))
Q(S1, id="q5", no="5", type="이중적분 (순서 바꾸기 · 부피)", ref="2024 중간 2(a) 유형", types=["15-order", "15-general"],
  stem="",
  parts=[("a", r"적분 순서를 바꾸어 계산하시오. $\displaystyle\int_0^1\!\!\int_{\sqrt y}^{1}\sqrt{x^3+1}\,dx\,dy$"),
         ("b", r"포물기둥 $y=x^2$ 과 평면 $y=1,\ z=0$, 곡면 $z=x^2+y^2$ 으로 둘러싸인 입체의 부피를 구하시오.")],
  answer=[("a", r"$\dfrac{2}{9}\big(2\sqrt2-1\big)$"), ("b", r"$\dfrac{88}{105}$")],
  solution=[("a", [r"영역: $0\le y\le1,\ \sqrt y\le x\le1$ ⟺ $0\le x\le1,\ 0\le y\le x^2$",
                   r"$$\int_0^1\!\!\int_0^{x^2}\sqrt{x^3+1}\,dy\,dx=\int_0^1x^2\sqrt{x^3+1}\,dx=\Big[\tfrac29(x^3+1)^{3/2}\Big]_0^1=\tfrac29(2\sqrt2-1)$$"]),
            ("b", [r"밑면 $D=\{-1\le x\le1,\ x^2\le y\le1\}$, 높이 $x^2+y^2$",
                   r"$$\begin{aligned}V&=\int_{-1}^1\!\!\int_{x^2}^1(x^2+y^2)\,dy\,dx\\&=\int_{-1}^1\Big(x^2-x^4+\frac{1-x^6}{3}\Big)dx\\&=2\Big(\frac13-\frac15+\frac13-\frac1{21}\Big)=\frac{88}{105}\end{aligned}$$"])],
  check=_c)


def _c():
    Ia = integrate((4 - r*sin(th))*r*r, (r, 0, 2), (th, 0, 2*pi))
    assert EQ(Ia, 64*pi/3)
    Ib = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, 2), (ph, 0, pi/4), (th, 0, 2*pi))
    assert EQ(Ib, 2*pi)
Q(S1, id="q6", no="6", type="삼중적분 (원주 · 구면좌표)", ref="2025 중간 4번 · 10번 유형", types=["15-cyl", "15-sph"],
  stem="",
  parts=[("a", r"$E$ 가 원기둥 $x^2+y^2=4$ 의 내부에서 평면 $z=0$ 위, 평면 $z=4-y$ 아래에 있는 입체일 때 $\displaystyle\iiint_E\sqrt{x^2+y^2}\,dV$ 를 구하시오."),
         ("b", r"$E$ 가 원뿔 $z=\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=4$ 안에 있는 입체일 때 $\displaystyle\iiint_E z\,dV$ 를 구하시오.")],
  answer=[("a", r"$\dfrac{64\pi}{3}$"), ("b", r"$2\pi$")],
  solution=[("a", [r"원주좌표: $0\le\theta\le2\pi,\ 0\le r\le2,\ 0\le z\le4-r\sin\theta$ ($4-y\ge2>0$)",
                   r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^2(4-r\sin\theta)\,r\cdot r\,dr\,d\theta\\&=4\cdot2\pi\cdot\frac83-\int_0^{2\pi}\sin\theta\,d\theta\cdot4=\frac{64\pi}{3}\end{aligned}$$"]),
            ("b", [r"구면좌표: 원뿔 $z=r$ ⟺ $\phi=\frac\pi4$ → $0\le\phi\le\frac\pi4,\ 0\le\rho\le2$",
                   r"$$\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^2\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot\frac{\sin^2(\pi/4)}{2}\cdot4=2\pi$$"])],
  check=_c)


def _c():
    f = x*y**2 + y*z**3
    g = grad(f, (x, y, z)).subs({x: 2, y: -1, z: 1})
    assert g == Matrix([1, -3, -3])
    d = Matrix([2, 1, -2])
    assert EQ(g.dot(d)/d.norm(), R(5, 3)) and EQ(g.norm(), sqrt(19))
Q(S1, id="q7", no="7", type="방향도함수와 그래디언트", ref="2022 중간 블럭1 5번 · 강의 14.6 유형", types=["14-dir", "14-maxrate"],
  stem=r"$f(x,y,z)=xy^2+yz^3$, $P(2,-1,1)$, $Q(4,0,-1)$ 에 대하여",
  parts=[("a", r"$\nabla f(P)$ 를 구하시오."),
         ("b", r"$P$ 에서 $Q$ 를 향하는 방향의 방향도함수를 구하시오."),
         ("c", r"$P$ 에서 $f$ 가 가장 빨리 감소하는 방향과 그때의 변화율을 구하시오.")],
  answer=[("a", r"$\langle1,-3,-3\rangle$"), ("b", r"$\dfrac53$"), ("c", r"방향 $\dfrac{1}{\sqrt{19}}\langle-1,3,3\rangle$, 변화율 $-\sqrt{19}$")],
  solution=[("a", [r"$f_x=y^2,\ f_y=2xy+z^3,\ f_z=3yz^2$ → $(1,\ -4+1,\ -3)=\langle1,-3,-3\rangle$"]),
            ("b", [r"$\overrightarrow{PQ}=\langle2,1,-2\rangle$, $|\overrightarrow{PQ}|=3$ → $D_{\mathbf u}f=\dfrac{2-3+6}{3}=\dfrac53$"]),
            ("c", [r"가장 빨리 감소하는 방향은 $-\nabla f$ 방향, 변화율은 $-|\nabla f|=-\sqrt{1+9+9}=-\sqrt{19}$"])],
  check=_c)


def _c():
    F = [y**2 + 2*x*z, 2*x*y + z, x**2 + y]
    f = x*y**2 + x**2*z + y*z
    assert all(simplify(a - b) == 0 for a, b in zip(grad(f, (x, y, z)), F))
    rr = [t**2, sin(pi*t/2), exp(t - 1)]
    assert EQ(f.subs({x: 1, y: 1, z: 1}) - f.subs({x: 0, y: 0, z: exp(-1)}), 3)
    num = line_num(F, rr, 0, 1)
    assert abs(num - 3) < 1e-10
    extra = integrate(t**2*exp(t - 1), (t, 0, 1))
    assert EQ(extra, 1 - 2*exp(-1))
    num2 = line_num([F[0], F[1], F[2] + x], rr, 0, 1)
    assert abs(num2 - (4 - 2/mp.e)) < 1e-10
Q(S1, id="q8", no="8", type="선적분의 기본정리", ref="2024 기말 2(b) 유형", types=["16-conserv", "16-ftli"],
  stem=r"$\mathbf F(x,y,z)=\big\langle y^2+2xz,\ 2xy+z,\ x^2+y\big\rangle$, $C:\ \mathbf r(t)=\big\langle t^2,\ \sin\tfrac{\pi t}{2},\ e^{t-1}\big\rangle\ (0\le t\le1)$ 에 대하여",
  parts=[("a", r"$\mathbf F$ 가 보존장임을 보이고 $\mathbf F=\nabla f$ 인 $f$ 를 구하시오."),
         ("b", r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r$ 를 구하시오."),
         ("c", r"$\mathbf G=\mathbf F+\langle0,0,x\rangle$ 일 때 $\displaystyle\int_C\mathbf G\cdot d\mathbf r$ 를 구하시오.")],
  answer=[("a", r"$f=xy^2+x^2z+yz$"), ("b", r"$3$"), ("c", r"$4-\dfrac2e$")],
  solution=[("a", [r"$P_y=2y=Q_x,\ P_z=2x=R_x,\ Q_z=1=R_y$ → 보존장",
                   r"$f=\int(y^2+2xz)\,dx=xy^2+x^2z+g(y,z)$, $f_y=2xy+g_y=2xy+z \Rightarrow g=yz+h(z)$, $f_z=x^2+y \Rightarrow h$ 상수 → $f=xy^2+x^2z+yz$"]),
            ("b", [r"$\mathbf r(0)=(0,0,e^{-1})$, $\mathbf r(1)=(1,1,1)$ → $f(1,1,1)-f(0,0,e^{-1})=3-0=3$"]),
            ("c", [r"$\displaystyle\int_C\mathbf G\cdot d\mathbf r=3+\int_Cx\,dz=3+\int_0^1t^2e^{t-1}\,dt$",
                   r"$\displaystyle\int_0^1t^2e^{t}\,dt=\Big[(t^2-2t+2)e^t\Big]_0^1=e-2$ → $e^{-1}(e-2)=1-\frac2e$ → 답 $4-\dfrac2e$"])],
  check=_c)


def _c():
    Ia = integrate((3*x**2 + 3*y**2).subs({x: r*cos(th), y: r*sin(th)})*r, (r, 0, 2), (th, 0, 2*pi))
    assert EQ(Ia, 24*pi)
    assert EQ(line_int([x**2 - y**3, x**3 + y**2], [2*cos(t), 2*sin(t)], 0, 2*pi, (x, y)), 24*pi)
    P_, Q_ = y + exp(x), 2*x + cos(y)
    tot = 0
    for p0, p1 in [((0, 0), (1, 0)), ((1, 0), (1, 2)), ((1, 2), (0, 0))]:
        tot += line_num([P_, Q_], [p0[0] + (p1[0] - p0[0])*t, p0[1] + (p1[1] - p0[1])*t], 0, 1, (x, y))
    assert abs(tot - 1) < 1e-10
    assert EQ(R(1, 2)*integrate(3*cos(t)*2*cos(t) + 2*sin(t)*3*sin(t), (t, 0, 2*pi)), 6*pi)
Q(S1, id="q9", no="9", type="그린 정리", ref="2024 기말 1번 유형", types=["16-green", "16-greenarea"],
  stem="그린 정리를 이용하여 다음을 구하시오.",
  parts=[("a", r"$C$ 가 원 $x^2+y^2=4$ (반시계 방향)일 때 $\displaystyle\oint_C(x^2-y^3)\,dx+(x^3+y^2)\,dy$"),
         ("b", r"$C$ 가 꼭짓점 $(0,0),\ (1,0),\ (1,2)$ 인 삼각형의 경계(반시계 방향)일 때 $\displaystyle\oint_C(y+e^x)\,dx+(2x+\cos y)\,dy$"),
         ("c", r"타원 $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$ 로 둘러싸인 영역의 넓이")],
  answer=[("a", r"$24\pi$"), ("b", r"$1$"), ("c", r"$6\pi$")],
  solution=[("a", [r"$Q_x-P_y=3x^2+3y^2$ → $\displaystyle\iint_D3r^2\,dA=\int_0^{2\pi}\!\!\int_0^23r^3\,dr\,d\theta=2\pi\cdot12=24\pi$"]),
            ("b", [r"$Q_x-P_y=2-1=1$ → 값 = 삼각형의 넓이 $=\tfrac12\cdot1\cdot2=1$"]),
            ("c", [r"$A=\dfrac12\displaystyle\oint_Cx\,dy-y\,dx$, $x=3\cos t,\ y=2\sin t$: $x\,dy-y\,dx=(6\cos^2t+6\sin^2t)\,dt=6\,dt$",
                   r"$A=\dfrac12\displaystyle\int_0^{2\pi}6\,dt=6\pi$"])],
  check=_c)


def _c():
    T = 100/(1 + x**2 + 2*y**2)
    g = grad(T, (x, y)).subs({x: 1, y: 1})
    assert g == Matrix([R(-25, 2), -25]) and EQ(g.norm(), 25*sqrt(5)/2)
    assert g.dot(Matrix([2, -1])) == 0
    path = x**2
    assert simplify(diff(path, x) - (diff(T, y)/diff(T, x)).subs(y, path)) == 0
Q(S1, id="q10", no="10", type="최대 증가 방향", ref="강의 14.6 예제 응용 · 2022 중간 블럭2 3(a)", types=["14-maxrate", "14-dir"],
  stem=r"평면 위 점 $(x,y)$ 의 온도가 $T(x,y)=\dfrac{100}{1+x^2+2y^2}$ 이다.",
  parts=[("a", r"점 $(1,1)$ 에서 온도가 가장 빨리 증가하는 방향과 최대 증가율을 구하시오."),
         ("b", r"점 $(1,1)$ 에서 온도가 순간적으로 변하지 않는 방향을 모두 구하시오."),
         ("c", r"점 $(1,1)$ 에서 출발해 매 순간 온도가 가장 빨리 증가하는 방향으로 움직이는 입자의 경로를 구하시오.")],
  answer=[("a", r"방향 $\dfrac{1}{\sqrt5}\langle-1,-2\rangle$, 최대 증가율 $\dfrac{25\sqrt5}{2}$"), ("b", r"$\pm\dfrac{1}{\sqrt5}\langle2,-1\rangle$"), ("c", r"$y=x^2$ (원점 쪽으로)")],
  solution=[("a", [r"$\nabla T=\dfrac{-100\langle2x,4y\rangle}{(1+x^2+2y^2)^2}$ → $\nabla T(1,1)=\dfrac{-100\langle2,4\rangle}{16}=\big\langle-\tfrac{25}{2},-25\big\rangle$",
                   r"방향 $\langle-1,-2\rangle/\sqrt5$, 최대 증가율 $|\nabla T|=\tfrac{25}{2}\sqrt{1+4}=\tfrac{25\sqrt5}{2}$"]),
            ("b", [r"$D_{\mathbf u}T=0 \iff \mathbf u\perp\nabla T$ → $\mathbf u=\pm\frac{1}{\sqrt5}\langle2,-1\rangle$ (등온선의 접선 방향)"]),
            ("c", [r"경로의 기울기 $\dfrac{dy}{dx}=\dfrac{T_y}{T_x}=\dfrac{4y}{2x}=\dfrac{2y}{x}$ → $\ln|y|=2\ln|x|+C$ → $y=cx^2$",
                   r"$(1,1)$ 을 지나므로 $y=x^2$. $\nabla T$ 가 원점을 향하므로 입자는 이 포물선을 따라 원점(최고 온도)으로 가요."])],
  check=_c)


SETS.append({"id": "s1", "no": 1, "title": "실전 모의고사 1회", "focus": "예상 유형 10선 · 표준",
             "lead": "예상 유형 10개(극좌표 이중적분, 극한과 연속, 접평면·법선, 라그랑주, 이중적분, 삼중적분, 방향도함수, 선적분의 기본정리, 그린 정리, 최대 증가 방향)를 한 문항씩 표준 난이도로 묶었어요. 처음 푸는 회차로 추천해요.",
             "problems": S1})


# ════════════════════════════════════════════════════════════════════
# 2회 — 2025 중간 스타일
# ════════════════════════════════════════════════════════════════════
S2 = []


def _c():
    M = integrate(r*r, (r, sqrt(2), 2*cos(th)), (th, -pi/4, pi/4))
    My = integrate(r*cos(th)*r*r, (r, sqrt(2), 2*cos(th)), (th, -pi/4, pi/4))
    assert EQ(M, sqrt(2)*(20 - 3*pi)/9) and EQ(My, 28*sqrt(2)/15)
    assert EQ(My/M, 84/(100 - 15*pi))
    assert EQ(integrate(cos(th)**3, (th, -pi/4, pi/4)), 5*sqrt(2)/6)
    assert EQ(integrate(cos(th)**5, (th, -pi/4, pi/4)), 43*sqrt(2)/60)
Q(S2, id="q1", no="1", type="판의 질량중심 (극좌표)", ref="2025 중간 1번 유형", types=["15-mass", "15-polar"],
  stem=r"원 $x^2+y^2=2x$ 의 내부이면서 원 $x^2+y^2=2$ 의 외부인 영역을 차지하는 판의 밀도가 $\rho(x,y)=\sqrt{x^2+y^2}$ 일 때,",
  parts=[("a", r"판의 질량을 구하시오."), ("b", r"판의 질량중심을 구하시오.")],
  answer=[("a", r"$\dfrac{\sqrt2\,(20-3\pi)}{9}$"), ("b", r"$\Big(\dfrac{84}{100-15\pi},\ 0\Big)$")],
  solution=[("a", [r"$x^2+y^2=2x \iff r=2\cos\theta$, 교점 $2\cos\theta=\sqrt2 \Rightarrow \theta=\pm\frac\pi4$ → $D:\ |\theta|\le\frac\pi4,\ \sqrt2\le r\le2\cos\theta$",
                   r"$$\begin{aligned}m&=\int_{-\pi/4}^{\pi/4}\!\!\int_{\sqrt2}^{2\cos\theta}r^2\,dr\,d\theta=\int_{-\pi/4}^{\pi/4}\frac{8\cos^3\theta-2\sqrt2}{3}\,d\theta\end{aligned}$$",
                   r"$\displaystyle\int_{-\pi/4}^{\pi/4}\cos^3\theta\,d\theta=\Big[\sin\theta-\tfrac{\sin^3\theta}{3}\Big]_{-\pi/4}^{\pi/4}=\frac{5\sqrt2}{6}$ → $m=\dfrac{20\sqrt2}{9}-\dfrac{\sqrt2\pi}{3}=\dfrac{\sqrt2(20-3\pi)}{9}$"]),
            ("b", [r"$x$축 대칭 → $\bar y=0$",
                   r"$$\begin{aligned}M_y&=\int_{-\pi/4}^{\pi/4}\!\!\int_{\sqrt2}^{2\cos\theta}r^3\cos\theta\,dr\,d\theta\\&=\int_{-\pi/4}^{\pi/4}\cos\theta\cdot\frac{16\cos^4\theta-4}{4}\,d\theta=4\cdot\frac{43\sqrt2}{60}-\sqrt2=\frac{28\sqrt2}{15}\end{aligned}$$",
                   r"($\int_{-\pi/4}^{\pi/4}\cos^5\theta\,d\theta=\big[\sin\theta-\tfrac23\sin^3\theta+\tfrac15\sin^5\theta\big]_{-\pi/4}^{\pi/4}=\tfrac{43\sqrt2}{60}$)",
                   r"$\bar x=\dfrac{28\sqrt2/15}{\sqrt2(20-3\pi)/9}=\dfrac{84}{5(20-3\pi)}=\dfrac{84}{100-15\pi}\approx1.59$"])],
  check=_c)


def _c():
    f = 2*x**3 + x*y**2 + 5*x**2 + y**2
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    pts = sorted([(q[x], q[y]) for q in crit], key=lambda p: (float(p[0]), float(p[1])))
    assert pts == [(R(-5, 3), 0), (-1, -2), (-1, 2), (0, 0)]
    def D(p):
        sub = {x: p[0], y: p[1]}
        return (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2).subs(sub), diff(f, x, 2).subs(sub)
    assert D((0, 0)) == (20, 10) and D((R(-5, 3), 0))[0] > 0 and D((R(-5, 3), 0))[1] < 0
    assert D((-1, 2))[0] < 0 and D((-1, -2))[0] < 0
    assert EQ(f.subs({x: R(-5, 3), y: 0}), R(125, 27))
    I = integrate(r*cos(th)*r, (r, 1, 2), (th, 0, pi/3))
    assert EQ(I, 7*sqrt(3)/6)
    cart = (integrate(x, (y, sqrt(1 - x**2), sqrt(3)*x), (x, R(1, 2), 1)) + integrate(x, (y, 0, sqrt(4 - x**2)), (x, 1, 2)))
    assert EQ(cart, 7*sqrt(3)/6)
Q(S2, id="q2", no="2", type="극값과 안장점 · 극좌표로 바꾸기", ref="2025 중간 2번 유형", types=["14-crit", "15-polar"],
  stem="",
  parts=[("a", r"$f(x,y)=2x^3+xy^2+5x^2+y^2$ 의 극댓값, 극솟값, 안장점을 구하시오."),
         ("b", r"다음 합을 극좌표의 이중적분 하나로 나타내고, $f(x,y)=x$ 일 때 값을 구하시오. $$\int_{1/2}^{1}\!\!\int_{\sqrt{1-x^2}}^{\sqrt3\,x}f\,dy\,dx+\int_1^2\!\!\int_0^{\sqrt{4-x^2}}f\,dy\,dx$$")],
  answer=[("a", r"극솟값 $f(0,0)=0$, 극댓값 $f\big(-\tfrac53,0\big)=\tfrac{125}{27}$, 안장점 $(-1,\pm2)$"),
          ("b", r"$\displaystyle\int_0^{\pi/3}\!\!\int_1^2f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$, 값 $\dfrac{7\sqrt3}{6}$")],
  solution=[("a", [r"$f_x=6x^2+y^2+10x=0,\ f_y=2y(x+1)=0$",
                   r"$y=0$: $6x^2+10x=0 \Rightarrow x=0,\ -\tfrac53$;  $x=-1$: $y^2=4 \Rightarrow y=\pm2$",
                   r"$f_{xx}=12x+10,\ f_{yy}=2x+2,\ f_{xy}=2y$",
                   r"$(0,0)$: $D=20>0,\ f_{xx}>0$ → 극소 $0$;  $\big(-\tfrac53,0\big)$: $f_{xx}=-10,\ f_{yy}=-\tfrac43$, $D=\tfrac{40}3>0$ → 극대 $\tfrac{125}{27}$;  $(-1,\pm2)$: $D=0-16<0$ → 안장점"]),
            ("b", [r"첫 조각: 원 $r=1$ 바깥, 직선 $y=\sqrt3x$ ($\theta=\frac\pi3$) 아래. 둘째 조각: 원 $r=2$ 안, $x\ge1$ → 합치면 $1\le r\le2,\ 0\le\theta\le\frac\pi3$",
                   r"$$\int_0^{\pi/3}\!\!\int_1^2 r\cos\theta\cdot r\,dr\,d\theta=\frac73\cdot\frac{\sqrt3}{2}=\frac{7\sqrt3}{6}$$"])],
  check=_c)


def _c():
    fa = x**4*sin(y)/(x**2 + y**2)**2
    assert limit(fa.subs({x: r*cos(R(2, 5)), y: r*sin(R(2, 5))}), r, 0, '+') == 0
    N_ = sin(x*y**2)*cos(x) - cos(x*y**2)*sin(x)
    assert simplify(N_ - sin(x*(y**2 - 1))) == 0
    vq = symbols('vq', real=True)
    Nv = sin(x*((1 + vq)**2 - 1))
    kk = symbols('kk', real=True)
    lim_k = limit((Nv/(x**2 + vq**2)).subs(x, kk*vq), vq, 0)
    assert simplify(lim_k - 2*kk/(kk**2 + 1)) == 0
    assert limit((Nv/sqrt(x**2 + vq**2)).subs(x, kk*vq), vq, 0) == 0
Q(S2, id="q3", no="3", type="극한", ref="2025 중간 3번 유형", types=["14-limit", "14-dne"],
  stem="다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^4\sin y}{(x^2+y^2)^2}$"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,1)}\frac{\sin(xy^2)\cos x-\cos(xy^2)\sin x}{x^2+(y-1)^2}$"),
         ("c", r"$\displaystyle\lim_{(x,y)\to(0,1)}\frac{\sin(xy^2)\cos x-\cos(xy^2)\sin x}{\sqrt{x^2+(y-1)^2}}$")],
  answer=[("a", r"$0$"), ("b", r"존재하지 않음 (직선 $x=k(y-1)$ 을 따라 $\tfrac{2k}{k^2+1}$)"), ("c", r"$0$")],
  solution=[("a", [r"$x^4\le(x^2+y^2)^2$ → $\Big|\dfrac{x^4\sin y}{(x^2+y^2)^2}\Big|\le|\sin y|\to0$ → 극한 $0$"]),
            ("b", [r"분자 $=\sin(xy^2-x)=\sin\big(x(y-1)(y+1)\big)$. $v=y-1$ 로 두면 $(x,v)\to(0,0)$",
                   r"직선 $x=kv$: $\dfrac{\sin\big(kv^2(v+2)\big)}{(k^2+1)v^2}\to\dfrac{2k}{k^2+1}$ → $k=0$ 이면 $0$, $k=1$ 이면 $1$ → 존재하지 않음"]),
            ("c", [r"$|\sin w|\le|w|$ → $|\text{분자}|\le|x||v||v+2|\le\dfrac{x^2+v^2}{2}\,|v+2|$",
                   r"$\Big|\dfrac{\text{분자}}{\sqrt{x^2+v^2}}\Big|\le\dfrac{\sqrt{x^2+v^2}}{2}|v+2|\to0$ → 극한 $0$"])],
  check=_c)


def _c():
    Ia = integrate((4 - r**2)*r*cos(th)*r, (r, 0, 2), (th, -pi/2, pi/2))
    Ib = integrate((16 - r**4)/2*r, (r, 0, 2), (th, -pi/2, pi/2))
    assert EQ(Ia, R(128, 15)) and EQ(Ib, 32*pi/3)
Q(S2, id="q4", no="4", type="원주좌표 삼중적분", ref="2025 중간 4번 유형", types=["15-cyl"],
  stem=r"$E$ 가 포물면 $z=x^2+y^2$ 과 평면 $z=4$ 로 둘러싸인 입체 중 $x\ge0$ 인 부분일 때,",
  parts=[("a", r"$\displaystyle\iiint_Ex\,dV$ 를 구하시오."), ("b", r"$\displaystyle\iiint_Ez\,dV$ 를 구하시오.")],
  answer=[("a", r"$\dfrac{128}{15}$"), ("b", r"$\dfrac{32\pi}{3}$")],
  solution=[("a", [r"원주좌표: $-\frac\pi2\le\theta\le\frac\pi2,\ 0\le r\le2,\ r^2\le z\le4$",
                   r"$$\begin{aligned}\iiint_Ex\,dV&=\int_{-\pi/2}^{\pi/2}\!\!\int_0^2(4-r^2)\,r\cos\theta\cdot r\,dr\,d\theta\\&=2\int_0^2(4r^2-r^4)\,dr=2\Big(\frac{32}{3}-\frac{32}{5}\Big)=\frac{128}{15}\end{aligned}$$"]),
            ("b", [r"$$\begin{aligned}\iiint_Ez\,dV&=\int_{-\pi/2}^{\pi/2}\!\!\int_0^2\frac{16-r^4}{2}\,r\,dr\,d\theta\\&=\pi\cdot\frac12\Big(32-\frac{64}{6}\Big)=\frac{32\pi}{3}\end{aligned}$$"])],
  check=_c)


def _c():
    f = taylor2(3, 2, 7, 1, -2, 3, 1, -1)
    Z = f.subs({x: s + t, y: s*t}, simultaneous=True)
    pt = {s: 1, t: 2}
    assert EQ(diff(Z, s, t).subs(pt), 2) and EQ(diff(Z, s, 2).subs(pt), 3)
Q(S2, id="q5", no="5", type="2계 연쇄법칙", ref="2025 중간 5번 유형", types=["14-chain2"],
  stem=r"$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=s+t,\ y=st$ 이다. $f_x(3,2)=1,\ f_y(3,2)=-2,\ f_{xx}(3,2)=3,\ f_{xy}(3,2)=1,\ f_{yy}(3,2)=-1$ 일 때 $(s,t)=(1,2)$ 에서",
  parts=[("a", r"$\dfrac{\partial^2z}{\partial s\,\partial t}$ 를 구하시오."), ("b", r"$\dfrac{\partial^2z}{\partial s^2}$ 를 구하시오.")],
  answer=[("a", r"$2$"), ("b", r"$3$")],
  solution=[("a", [r"$(s,t)=(1,2)$ ↔ $(x,y)=(3,2)$. $z_s=f_x\cdot1+f_y\cdot t$",
                   r"$t$ 로 미분 ($x_t=1,\ y_t=s$): $z_{st}=(f_{xx}+f_{xy}s)+f_y+t\,(f_{yx}+f_{yy}s)$",
                   r"$=(3+1)+(-2)+2(1-1)=2$"]),
            ("b", [r"$s$ 로 미분 ($x_s=1,\ y_s=t$): $z_{ss}=(f_{xx}+f_{xy}t)+t\,(f_{yx}+f_{yy}t)$",
                   r"$=(3+2)+2(1-2)=3$"])],
  check=_c)


def _c():
    zx, zy = R(-3, 2), R(1, 2)
    assert 3*2 - 1 + 2*3 == 11
    assert EQ(zx*R(3, 5) + zy*R(4, 5), R(-1, 2))
    assert EQ(3 + zx*R(1, 10) + zy*R(-2, 10), R(11, 4))
    assert EQ(sqrt(zx**2 + zy**2), sqrt(10)/2)
Q(S2, id="q6", no="6", type="음함수 · 접평면 · 선형근사", ref="2025 중간 6번 유형", types=["14-implicit", "14-tangent", "14-dir"],
  stem=r"미분가능한 함수 $F(x,y,z)$ 에 대해 $F_z\ne0$ 이고, $z=z(x,y)$ 는 $F\big(x,y,z(x,y)\big)=0$ 으로 정해진다. 곡면 $F(x,y,z)=0$ 의 점 $(2,1,3)$ 에서의 접평면이 $3x-y+2z=11$ 일 때,",
  parts=[("a", r"점 $(2,1)$ 에서 $z$ 의 $\mathbf v=\langle3,4\rangle$ 방향으로의 변화율을 구하시오."),
         ("b", r"선형근사로 $z(2.1,\ 0.8)$ 의 근삿값을 구하시오."),
         ("c", r"점 $(2,1)$ 에서 $z$ 의 최대 변화율을 구하시오.")],
  answer=[("a", r"$-\dfrac12$"), ("b", r"$2.75$"), ("c", r"$\dfrac{\sqrt{10}}{2}$")],
  solution=[("a", [r"접평면의 법선 $\langle3,-1,2\rangle\parallel\nabla F$ → $z_x=-\dfrac{F_x}{F_z}=-\dfrac32,\ z_y=-\dfrac{F_y}{F_z}=\dfrac12$",
                   r"$\mathbf u=\big\langle\tfrac35,\tfrac45\big\rangle$: $D_{\mathbf u}z=-\tfrac32\cdot\tfrac35+\tfrac12\cdot\tfrac45=-\tfrac{9}{10}+\tfrac{4}{10}=-\tfrac12$"]),
            ("b", [r"$z(2.1,0.8)\approx3-\tfrac32(0.1)+\tfrac12(-0.2)=3-0.15-0.1=2.75$ (접평면 $z=\tfrac{11-3x+y}{2}$ 에 대입한 값과 같아요)"]),
            ("c", [r"$|\nabla z(2,1)|=\sqrt{\tfrac94+\tfrac14}=\dfrac{\sqrt{10}}{2}$"])],
  check=_c)


def _c():
    f = x**2 + y**2 + y
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: 0, y: R(-1, 2)}
    rq = symbols('rq', nonnegative=True)
    assert simplify((rq**2 + rq*sin(th)).subs(sin(th), 1 - rq) - rq) == 0
    best_max, best_min = -9.0, 9.0
    for i in range(0, 361):
        tq = 2*mp.pi*i/360
        rmax = 1 - mp.sin(tq)
        for j in range(0, 61):
            rr_ = rmax*j/60
            X, Y = rr_*mp.cos(tq), rr_*mp.sin(tq)
            val = float(X*X + Y*Y + Y)
            best_max = max(best_max, val); best_min = min(best_min, val)
    assert abs(best_max - 2) < 1e-9 and abs(best_min + 0.25) < 1e-9
Q(S2, id="q7", no="7", type="닫힌 영역의 최댓값·최솟값", ref="2025 중간 7번 유형", types=["14-absext"],
  stem=r"$f(x,y)=x^2+y^2+y$ 의 영역 $D=\big\{(x,y)\ \big|\ x^2+y^2\le\sqrt{x^2+y^2}-y\big\}$ 위에서의 최댓값과 최솟값을 구하시오.",
  parts=[],
  answer=[("", r"최댓값 $2$ (점 $(0,-2)$), 최솟값 $-\dfrac14$ (점 $\big(0,-\tfrac12\big)$)")],
  solution=[("", [r"극좌표: $r^2\le r-r\sin\theta \iff r\le1-\sin\theta$ (아래로 향한 심장형)",
                  r"내부 임계점: $f_x=2x=0,\ f_y=2y+1=0$ → $\big(0,-\tfrac12\big)$ ($\theta=-\frac\pi2$ 방향, $r=\tfrac12\le2$ 이므로 $D$ 안), $f=-\tfrac14$",
                  r"경계 $r=1-\sin\theta$: $\sin\theta=1-r$ 이므로 $f=r^2+r\sin\theta=r^2+r(1-r)=r$ ($0\le r\le2$)",
                  r"경계에서 $f$ 의 최댓값 $2$ ($r=2$, 즉 $\theta=-\frac\pi2$, 점 $(0,-2)$), 최솟값 $0$",
                  r"후보 비교: 최댓값 $2$ (점 $(0,-2)$), 최솟값 $-\tfrac14$ (점 $(0,-\tfrac12)$)"])],
  check=_c)


def _c():
    lam, mu = symbols('lam mu')
    eqs = [2*x - 2*lam*x - mu, 2*y - 2*lam*y + mu, 2*z - 4*lam*z**3, x**2 + y**2 + z**4 - 2, x - y]
    sols = solve(eqs, [x, y, z, lam, mu], dict=True)
    vals = sorted({simplify((x**2 + y**2 + z**2).subs(q)) for q in sols}, key=float)
    assert EQ(vals[0], sqrt(2)) and EQ(vals[-1], R(9, 4))
Q(S2, id="q8", no="8", type="라그랑주 승수법 (제약 2개)", ref="2025 중간 8번 유형", types=["14-lagrange2"],
  stem=r"라그랑주 승수법을 이용하여 곡면 $x^2+y^2+z^4=2$ 와 평면 $y=x$ 의 교선 위에서 $f(x,y,z)=x^2+y^2+z^2$ 의 최댓값과 최솟값을 구하시오.",
  parts=[],
  answer=[("", r"최댓값 $\dfrac94$ ($x=y=\pm\sqrt{\tfrac78},\ z=\pm\tfrac1{\sqrt2}$), 최솟값 $\sqrt2$ (점 $(0,0,\pm\sqrt[4]2)$)")],
  solution=[("", [r"$\nabla f=\lambda\nabla g+\mu\nabla h$, $g=x^2+y^2+z^4,\ h=x-y$: $2x=2\lambda x+\mu,\ 2y=2\lambda y-\mu,\ 2z=4\lambda z^3$",
                  r"$x=y$ 이므로 처음 두 식을 더하고 빼면 $\mu=0,\ x(1-\lambda)=0$",
                  r"① $x=0$: $z^4=2$ → $f=z^2=\sqrt2$.  ② $z=0$: $2x^2=2$ → $f=2$",
                  r"③ $\lambda=1,\ z\ne0$: $z^2=\dfrac{1}{2\lambda}=\dfrac12$ → $2x^2=2-\tfrac14=\tfrac74$ → $f=\tfrac74+\tfrac12=\tfrac94$",
                  r"후보 $\sqrt2\approx1.41,\ 2,\ \tfrac94$ → 최댓값 $\tfrac94$, 최솟값 $\sqrt2$ (교선은 닫힌 곡선이라 둘 다 존재)"])],
  check=_c)


def _c():
    F = [2*x*cos(y) - z, -x**2*sin(y), -x + 3*z**2]
    f = x**2*cos(y) - x*z + z**3
    assert all(simplify(a - b) == 0 for a, b in zip(grad(f, (x, y, z)), F))
    rr = [1 + t**3, pi/2*sin(pi*t/2), t**2]
    assert EQ(f.subs({x: 2, y: pi/2, z: 1}) - f.subs({x: 1, y: 0, z: 0}), -2)
    assert abs(line_num(F, rr, 0, 1) + 2) < 1e-10
    ff = 6*u*(1 - u) + R(1, 1)
    assert EQ(integrate(ff, (u, 0, 1)), 2)
Q(S2, id="q9", no="9", type="선적분의 기본정리", ref="2024 기말 2·3번 유형", types=["16-ftli", "16-conserv"],
  stem="",
  parts=[("a", r"$\mathbf F(x,y,z)=\big\langle2x\cos y-z,\ -x^2\sin y,\ -x+3z^2\big\rangle$ 이고 $C:\ \mathbf r(t)=\big\langle1+t^3,\ \tfrac\pi2\sin\tfrac{\pi t}{2},\ t^2\big\rangle\ (0\le t\le1)$ 일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$ 를 구하시오."),
         ("b", r"연속함수 $f$ 가 $\displaystyle\int_0^1f(u)\,du=2$ 를 만족한다. $C$ 가 $(0,0,0)$ 에서 $(2,0,1)$ 까지 가는 임의의 매끄러운 곡선일 때 $\displaystyle\int_Cf(x+y-z)\,(dx+dy-dz)$ 를 구하시오.")],
  answer=[("a", r"$-2$"), ("b", r"$2$")],
  solution=[("a", [r"$P_y=-2x\sin y=Q_x,\ P_z=-1=R_x,\ Q_z=0=R_y$ → 보존장",
                   r"$f=x^2\cos y-xz+z^3$ ($f_x=2x\cos y-z$, $f_y=-x^2\sin y$, $f_z=-x+3z^2$)",
                   r"$\mathbf r(0)=(1,0,0)$, $\mathbf r(1)=\big(2,\tfrac\pi2,1\big)$ → $f\big(2,\tfrac\pi2,1\big)-f(1,0,0)=(0-2+1)-1=-2$"]),
            ("b", [r"$g(x,y,z)=\displaystyle\int_0^{x+y-z}f(u)\,du$ 로 두면 $\nabla g=f(x+y-z)\langle1,1,-1\rangle$",
                   r"값 $=g(2,0,1)-g(0,0,0)=\displaystyle\int_0^{1}f(u)\,du=2$"])],
  check=_c)


def _c():
    assert EQ(integrate((7 - 3)*r, (r, 0, 3), (th, 0, 2*pi)), 36*pi)
    P_, Q_ = x**2 + y, 3*x + y**3
    assert simplify(diff(Q_, x) - diff(P_, y)) == 2
    seg = integrate(x**2, (x, -2, 2))
    assert EQ(seg, R(16, 3))
    num = line_num([P_, Q_], [2*cos(t), 2*sin(t)], 0, pi, (x, y))
    assert abs(num - (4*mp.pi - mp.mpf(16)/3)) < 1e-10
Q(S2, id="q10", no="10", type="그린 정리", ref="2024 기말 1번 · 2022 기말 블럭2 4번 유형", types=["16-green"],
  stem="",
  parts=[("a", r"$C$ 가 원 $x^2+y^2=9$ (반시계 방향)일 때 $\displaystyle\oint_C\big(3y-e^{\sin x}\big)\,dx+\big(7x+\sqrt{y^4+1}\big)\,dy$ 를 구하시오."),
         ("b", r"$C$ 가 원 $x^2+y^2=4$ 의 위쪽 반원을 $(2,0)$ 에서 $(-2,0)$ 까지 가는 곡선일 때 그린 정리를 이용하여 $\displaystyle\int_C(x^2+y)\,dx+(3x+y^3)\,dy$ 를 구하시오.")],
  answer=[("a", r"$36\pi$"), ("b", r"$4\pi-\dfrac{16}{3}$")],
  solution=[("a", [r"$Q_x-P_y=7-3=4$ → $\displaystyle\oint_C=\iint_D4\,dA=4\cdot9\pi=36\pi$ (직접 계산하기 힘든 항들이 모두 사라져요)"]),
            ("b", [r"선분 $L$: $(-2,0)\to(2,0)$ 을 붙이면 $C+L$ 은 위쪽 반원판 $D$ 의 양의 방향 경계, $Q_x-P_y=3-1=2$",
                   r"$\displaystyle\oint_{C+L}=\iint_D2\,dA=2\cdot2\pi=4\pi$",
                   r"$L$: $y=0,\ dy=0$ → $\displaystyle\int_L=\int_{-2}^2x^2\,dx=\frac{16}{3}$ → $\displaystyle\int_C=4\pi-\frac{16}{3}$"])],
  check=_c)


SETS.append({"id": "s2", "no": 2, "title": "실전 모의고사 2회", "focus": "2025 중간 스타일",
             "lead": "2025학년도 중간고사의 문항 구성을 그대로 따라가요 — 질량중심, 극값 + 극좌표 변환, 극한, 원주좌표, 2계 연쇄법칙, 음함수와 선형근사, 심장형 영역의 최대·최소, 제약 2개 라그랑주. 마지막 두 문항은 우리 범위인 선적분의 기본정리와 그린 정리예요.",
             "problems": S2})


# ════════════════════════════════════════════════════════════════════
# 3회 — 2024 중간 스타일
# ════════════════════════════════════════════════════════════════════
S3 = []


def _c():
    f = x**4 - 4*x*y + 2*y**2
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    pts = sorted([(q[x], q[y]) for q in crit if q[x].is_real], key=lambda p: float(p[0]))
    assert pts == [(-1, -1), (0, 0), (1, 1)]
    D = lambda a, b: (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2).subs({x: a, y: b})
    assert D(0, 0) == -16 and D(1, 1) == 32 and D(-1, -1) == 32 and f.subs({x: 1, y: 1}) == -1
    F = x**2 + 2*y**2 + 3*z**2 + x*y*z
    P0 = {x: 1, y: 1, z: 1}
    assert F.subs(P0) == 7
    assert EQ((-diff(F, x)/diff(F, z)).subs(P0), R(-3, 7)) and EQ((-diff(F, y)/diff(F, z)).subs(P0), R(-5, 7))
Q(S3, id="q1", no="1", type="임계점 분류 · 음함수 편미분", ref="2024 중간 1번 유형", types=["14-crit", "14-implicit"],
  stem="",
  parts=[("a", r"$f(x,y)=x^4-4xy+2y^2$ 의 임계점을 모두 구하고 분류하시오."),
         ("b", r"$x^2+2y^2+3z^2+xyz=7$ 일 때 점 $(1,1,1)$ 에서 $\dfrac{\partial z}{\partial x},\ \dfrac{\partial z}{\partial y}$ 를 구하시오.")],
  answer=[("a", r"$(0,0)$ 안장점, $(1,1)$ 과 $(-1,-1)$ 에서 극솟값 $-1$"), ("b", r"$z_x=-\dfrac37,\ z_y=-\dfrac57$")],
  solution=[("a", [r"$f_x=4x^3-4y=0,\ f_y=-4x+4y=0$ → $y=x,\ x^3=x$ → $(0,0),\ (1,1),\ (-1,-1)$",
                   r"$f_{xx}=12x^2,\ f_{yy}=4,\ f_{xy}=-4$",
                   r"$(0,0)$: $D=0-16<0$ → 안장점;  $(\pm1,\pm1)$: $D=48-16=32>0,\ f_{xx}=12>0$ → 극솟값 $1-4+2=-1$"]),
            ("b", [r"$F=x^2+2y^2+3z^2+xyz$: $F_x=2x+yz=3,\ F_y=4y+xz=5,\ F_z=6z+xy=7$",
                   r"$z_x=-\dfrac{F_x}{F_z}=-\dfrac37$,  $z_y=-\dfrac{F_y}{F_z}=-\dfrac57$"])],
  check=_c)


def _c():
    Ia = integrate(sin(x**2)*x/2, (x, 0, 1))
    assert EQ(Ia, (1 - cos(1))/4)
    num = mp.quad(lambda Y: mp.quad(lambda X: Y*mp.sin(X*X), [Y*Y, 1]), [0, 1])
    assert abs(num - (1 - mp.cos(1))/4) < 1e-10
    Ib = integrate(y*(x + y), (y, x, sqrt(x)), (x, 0, 1))
    assert EQ(Ib, R(11, 120))
Q(S3, id="q2", no="2", type="이중적분 순서 바꾸기 · 삼중적분", ref="2024 중간 2번 유형", types=["15-order", "15-triple"],
  stem="다음 적분을 계산하시오.",
  parts=[("a", r"$\displaystyle\int_0^1\!\!\int_{y^2}^{1}y\sin(x^2)\,dx\,dy$"),
         ("b", r"$\displaystyle\iiint_Ey\,dV$, $E$ 는 곡면 $y=\sqrt x$, $y=x$, $z=0$, $z=x+y$ 로 둘러싸인 입체")],
  answer=[("a", r"$\dfrac{1-\cos1}{4}$"), ("b", r"$\dfrac{11}{120}$")],
  solution=[("a", [r"$\sin(x^2)$ 은 $x$ 로 적분할 수 없으므로 순서를 바꿔요: $0\le y\le1,\ y^2\le x\le1$ ⟺ $0\le x\le1,\ 0\le y\le\sqrt x$",
                   r"$$\int_0^1\!\!\int_0^{\sqrt x}y\sin(x^2)\,dy\,dx=\int_0^1\frac x2\sin(x^2)\,dx=\Big[-\frac14\cos(x^2)\Big]_0^1=\frac{1-\cos1}{4}$$"]),
            ("b", [r"$0\le x\le1$ 에서 $x\le\sqrt x$ → $E=\{0\le x\le1,\ x\le y\le\sqrt x,\ 0\le z\le x+y\}$",
                   r"$$\begin{aligned}\iiint_Ey\,dV&=\int_0^1\!\!\int_x^{\sqrt x}y(x+y)\,dy\,dx=\int_0^1\Big[\frac{xy^2}{2}+\frac{y^3}{3}\Big]_x^{\sqrt x}dx\\&=\int_0^1\Big(\frac{x^2}{2}+\frac{x^{3/2}}{3}-\frac{5x^3}{6}\Big)dx=\frac16+\frac2{15}-\frac5{24}=\frac{11}{120}\end{aligned}$$"])],
  check=_c)


def _c():
    import random
    random.seed(11)
    for _ in range(300):
        a, b = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
        val = abs(b - b*mp.cos(a))/(a*a + b*b)
        assert val <= abs(b)/2 + 1e-15
    fb = (x*sin(2*y) - 2*y*sin(x))/(x**4 + y**4)
    assert EQ(limit(fb.subs(y, x), x, 0), R(-1, 2)) and simplify(fb.subs(y, 0)) == 0
Q(S3, id="q3", no="3", type="극한", ref="2024 중간 3번 유형", types=["14-limit", "14-dne"],
  stem="다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{y-y\cos x}{x^2+y^2}$"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x\sin2y-2y\sin x}{x^4+y^4}$")],
  answer=[("a", r"$0$"), ("b", r"존재하지 않음 ($y=0$ 을 따라 $0$, $y=x$ 를 따라 $-\tfrac12$)")],
  solution=[("a", [r"$0\le1-\cos x\le\dfrac{x^2}{2}$ → $\Big|\dfrac{y(1-\cos x)}{x^2+y^2}\Big|\le\dfrac{|y|}{2}\cdot\dfrac{x^2}{x^2+y^2}\le\dfrac{|y|}{2}\to0$ → 극한 $0$"]),
            ("b", [r"$y=0$: 분자 $=0$ → $0$",
                   r"$y=x$: $\sin u=u-\frac{u^3}{6}+\cdots$ 로 분자 $=x\big(2x-\tfrac{8x^3}{6}\big)-2x\big(x-\tfrac{x^3}{6}\big)+\cdots=-x^4+\cdots$",
                   r"$\dfrac{-x^4+\cdots}{2x^4}\to-\dfrac12$ → 경로마다 다르므로 존재하지 않음"])],
  check=_c)


def _c():
    lam = symbols('lam')
    sols = solve([8*y*z - lam*x/2, 8*x*z - 2*lam*y/9, 8*x*y - 2*lam*z, x**2/4 + y**2/9 + z**2 - 1], [x, y, z, lam], dict=True)
    best = max([8*q[x]*q[y]*q[z] for q in sols if all(q[v_].is_positive for v_ in (x, y, z))], key=float)
    assert EQ(best, 16*sqrt(3)/3)
Q(S3, id="q4", no="4", type="라그랑주 승수법 (최적화)", ref="2024 중간 4번 유형", types=["14-lagrange", "14-optim"],
  stem=r"라그랑주 승수법을 이용하여, 타원면 $\dfrac{x^2}{4}+\dfrac{y^2}{9}+z^2=1$ 에 내접하고 각 면이 좌표평면과 평행한 직육면체의 부피의 최댓값과 그때의 세 모서리 길이를 구하시오.",
  parts=[],
  answer=[("", r"최대 부피 $\dfrac{16\sqrt3}{3}$, 모서리 $\dfrac{4}{\sqrt3},\ 2\sqrt3,\ \dfrac{2}{\sqrt3}$")],
  solution=[("", [r"제1팔분공간의 꼭짓점을 $(x,y,z)$ 라 하면 $V=8xyz$, 제약 $g=\frac{x^2}{4}+\frac{y^2}{9}+z^2=1$",
                  r"$8yz=\lambda\frac x2,\ 8xz=\lambda\frac{2y}{9},\ 8xy=2\lambda z$ → 각각 $x,y,z$ 를 곱하면 $8xyz=\lambda\frac{x^2}2=\lambda\frac{2y^2}{9}=2\lambda z^2$",
                  r"$\Rightarrow \frac{x^2}{4}=\frac{y^2}{9}=z^2$, 합이 $1$ 이므로 각각 $\frac13$ → $x=\frac{2}{\sqrt3},\ y=\sqrt3,\ z=\frac1{\sqrt3}$",
                  r"$V=8\cdot\frac{2}{\sqrt3}\cdot\sqrt3\cdot\frac{1}{\sqrt3}=\frac{16}{\sqrt3}=\frac{16\sqrt3}{3}$, 모서리 $2x,2y,2z$"])],
  check=_c)


def _c():
    wq = symbols('wq', positive=True)
    Fw = 3 - (wq - 1) + R(5, 2)*(wq - 1)**2 + (wq - 1)**3
    xp, yp = symbols('xp yp', positive=True)
    g = xp**4*Fw.subs(wq, yp/xp**2)
    assert simplify(xp*diff(g, xp) + 2*yp*diff(g, yp) - 4*g) == 0
    pt = {xp: 1, yp: 1}
    assert EQ(g.subs(pt), 3) and EQ(diff(g, xp).subs(pt), 14) and EQ(diff(g, yp).subs(pt), -1)
    assert EQ(3 + 14*R(1, 10) + (-1)*(-R(1, 10)), R(9, 2))
Q(S3, id="q5", no="5", type="연쇄법칙 · 선형근사", ref="2024 중간 5번 유형", types=["14-chain", "14-tangent"],
  stem=r"$F$ 는 미분가능한 한 변수 함수이고 $g(x,y)=x^4F\!\left(\dfrac{y}{x^2}\right)$ ($x>0$) 이다.",
  parts=[("a", r"$x\,g_x+2y\,g_y-4g$ 를 구하시오."),
         ("b", r"$F(1)=3,\ F'(1)=-1$ 일 때, $g$ 의 점 $(1,1)$ 에서의 선형근사를 이용해 $g(1.1,\ 0.9)$ 의 근삿값을 구하시오.")],
  answer=[("a", r"$0$"), ("b", r"$4.5$")],
  solution=[("a", [r"$w=\dfrac{y}{x^2}$: $g_x=4x^3F(w)+x^4F'(w)\cdot\Big(-\dfrac{2y}{x^3}\Big)=4x^3F-2xyF'$,  $g_y=x^4F'(w)\cdot\dfrac{1}{x^2}=x^2F'$",
                   r"$x\,g_x+2y\,g_y=4x^4F-2x^2yF'+2x^2yF'=4x^4F=4g$ → 답 $0$ ($g(tx,t^2y)=t^4g$ 꼴이라 생기는 성질)"]),
            ("b", [r"$(1,1)$ 에서 $w=1$: $g=3$, $g_x=4\cdot3-2\cdot(-1)=14$, $g_y=-1$",
                   r"$g(1.1,0.9)\approx3+14(0.1)+(-1)(-0.1)=3+1.4+0.1=4.5$"])],
  check=_c)


def _c():
    I1 = integrate(r**3, (r, 0, sqrt(3)), (th, 0, 2*pi))
    I2 = integrate(r**3, (r, 0, 2*sqrt(3)*sin(th)), (th, 0, pi))
    I12 = integrate(r**3, (r, 0, sqrt(3)), (th, pi/6, 5*pi/6)) + 2*integrate(r**3, (r, 0, 2*sqrt(3)*sin(th)), (th, 0, pi/6))
    assert EQ(I1, 9*pi/2) and EQ(I2, 27*pi/2) and EQ(I12, 6*pi - 63*sqrt(3)/8)
    assert EQ(I1 + I2 - I12, 12*pi + 63*sqrt(3)/8)
    num = mp.quad(lambda T: max(3, 12*mp.sin(T)**2)**2/4, [0, mp.pi/6, 5*mp.pi/6, mp.pi]) + mp.pi*mp.mpf(9)/4
    assert abs(num - (12*mp.pi + 63*mp.sqrt(3)/8)) < 1e-9
Q(S3, id="q6", no="6", type="극좌표 이중적분 (겹치는 원판)", ref="2024 중간 6번 유형", types=["15-polar"],
  stem=r"$D_1,\ D_2$ 가 각각 원판 $x^2+y^2\le3$ 과 $x^2+y^2\le2\sqrt3\,y$ 일 때 $\displaystyle\iint_{D_1\cup D_2}(x^2+y^2)\,dA$ 를 구하시오.",
  parts=[],
  answer=[("", r"$12\pi+\dfrac{63\sqrt3}{8}$")],
  solution=[("", [r"$\displaystyle\iint_{D_1\cup D_2}=\iint_{D_1}+\iint_{D_2}-\iint_{D_1\cap D_2}$. $D_2$: $r\le2\sqrt3\sin\theta$, 두 원은 $\sin\theta=\frac12$, 즉 $\theta=\frac\pi6,\frac{5\pi}6$ 에서 만나요",
                  r"$\displaystyle\iint_{D_1}r^2\,dA=2\pi\cdot\frac94=\frac{9\pi}2$,  $\displaystyle\iint_{D_2}=\int_0^\pi\frac{(2\sqrt3\sin\theta)^4}{4}d\theta=36\cdot\frac{3\pi}8=\frac{27\pi}{2}$",
                  r"$$\begin{aligned}\iint_{D_1\cap D_2}&=\int_{\pi/6}^{5\pi/6}\frac94\,d\theta+2\int_0^{\pi/6}36\sin^4\theta\,d\theta\\&=\frac{3\pi}{2}+72\Big(\frac\pi{16}-\frac{7\sqrt3}{64}\Big)=6\pi-\frac{63\sqrt3}{8}\end{aligned}$$",
                  r"답: $\dfrac{9\pi}2+\dfrac{27\pi}2-6\pi+\dfrac{63\sqrt3}8=12\pi+\dfrac{63\sqrt3}{8}$"])],
  check=_c)


def _c():
    f = x**3 + x*y**2
    uu = (1/sqrt(2), 1/sqrt(2))
    pf = f.subs({x: 1 + uu[0]*t, y: 2 + uu[1]*t}, simultaneous=True)
    assert EQ(diff(pf, t).subs(t, 0), 11*sqrt(2)/2) and EQ(diff(pf, t, 2).subs(t, 0), 8)
    ph_ = log(pf)
    assert EQ(diff(ph_, t, 2).subs(t, 0), R(-41, 50)) and EQ(diff(ph_, t).subs(t, 0), 11*sqrt(2)/10)
Q(S3, id="q7", no="7", type="2계 방향도함수", ref="2024 중간 7번 유형", types=["14-dir", "14-chain2"],
  stem=r"$f(x,y)=x^3+xy^2$, $\mathbf u=\Big\langle\dfrac1{\sqrt2},\dfrac1{\sqrt2}\Big\rangle$ 이고 $D_{\mathbf u}^2f=D_{\mathbf u}(D_{\mathbf u}f)$ 이다.",
  parts=[("a", r"$D_{\mathbf u}f(1,2)$ 와 $D_{\mathbf u}^2f(1,2)$ 를 구하시오."),
         ("b", r"$h(x,y)=\ln f(x,y)$ 일 때 $D_{\mathbf u}^2h(1,2)$ 를 구하시오.")],
  answer=[("a", r"$D_{\mathbf u}f=\dfrac{11\sqrt2}{2},\ D_{\mathbf u}^2f=8$"), ("b", r"$-\dfrac{41}{50}$")],
  solution=[("a", [r"$f_x=3x^2+y^2=7,\ f_y=2xy=4$ → $D_{\mathbf u}f=\dfrac{7+4}{\sqrt2}=\dfrac{11\sqrt2}{2}$",
                   r"$f_{xx}=6x=6,\ f_{xy}=2y=4,\ f_{yy}=2x=2$ → $D_{\mathbf u}^2f=f_{xx}u_1^2+2f_{xy}u_1u_2+f_{yy}u_2^2=\dfrac{6+8+2}{2}=8$"]),
            ("b", [r"$h=\ln f$: $D_{\mathbf u}h=\dfrac{D_{\mathbf u}f}{f}$, $D_{\mathbf u}^2h=\dfrac{D_{\mathbf u}^2f}{f}-\dfrac{(D_{\mathbf u}f)^2}{f^2}$ (1변수 $\ln$ 의 2계 도함수와 같은 꼴)",
                   r"$f(1,2)=5$: $D_{\mathbf u}^2h=\dfrac85-\dfrac{121/2}{25}=\dfrac{80-121}{50}=-\dfrac{41}{50}$"])],
  check=_c)


def _c():
    cyl = (integrate(z*r, (z, r, sqrt(3)*r), (r, 0, 1/sqrt(3)), (th, 0, 2*pi))
           + integrate(z*r, (z, r, 1), (r, 1/sqrt(3), 1), (th, 0, 2*pi)))
    sph = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, 1/cos(ph)), (ph, pi/6, pi/4), (th, 0, 2*pi))
    assert EQ(cyl, pi/6) and EQ(sph, pi/6)
Q(S3, id="q8", no="8", type="원주좌표 → 구면좌표 변환", ref="2024 중간 8번 유형", types=["15-sphconv", "15-cyl"],
  stem=r"다음 적분 $I$ 에 대하여 $$I=\int_0^{2\pi}\!\!\int_0^{1/\sqrt3}\!\!\int_r^{\sqrt3\,r}zr\,dz\,dr\,d\theta+\int_0^{2\pi}\!\!\int_{1/\sqrt3}^{1}\!\!\int_r^{1}zr\,dz\,dr\,d\theta$$",
  parts=[("a", r"적분 영역 $E$ 를 설명하고 $I$ 를 구면좌표 적분 하나로 나타내시오."), ("b", r"$I$ 의 값을 구하시오.")],
  answer=[("a", r"두 원뿔 $z=r$ 과 $z=\sqrt3\,r$ 사이, 평면 $z=1$ 아래: $\displaystyle\int_0^{2\pi}\!\!\int_{\pi/6}^{\pi/4}\!\!\int_0^{\sec\phi}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta$"), ("b", r"$\dfrac{\pi}{6}$")],
  solution=[("a", [r"$r\le z\le\sqrt3\,r$: 원뿔 $z=r$ ($\phi=\frac\pi4$) 안쪽이고 원뿔 $z=\sqrt3r$ ($\phi=\frac\pi6$) 바깥쪽. 둘째 적분은 $z\le1$ 로 잘린 부분 → $E=\{r\le z\le\sqrt3r,\ z\le1\}$",
                   r"구면좌표: $\frac\pi6\le\phi\le\frac\pi4$, $z=\rho\cos\phi\le1 \iff \rho\le\sec\phi$, 피적분 $z\cdot\rho^2\sin\phi=\rho^3\cos\phi\sin\phi$"]),
            ("b", [r"$$\begin{aligned}I&=2\pi\int_{\pi/6}^{\pi/4}\frac{\sec^4\phi}{4}\cos\phi\sin\phi\,d\phi=\frac\pi2\int_{\pi/6}^{\pi/4}\frac{\sin\phi}{\cos^3\phi}d\phi\\&=\frac\pi2\Big[\frac{1}{2\cos^2\phi}\Big]_{\pi/6}^{\pi/4}=\frac\pi2\Big(1-\frac23\Big)=\frac\pi6\end{aligned}$$"])],
  check=_c)


def _c():
    P_, Q_ = (3*x - y)/(x**2 + y**2), (x + 3*y)/(x**2 + y**2)
    assert simplify(P_ - (R(3, 2)*diff(log(x**2 + y**2), x) - y/(x**2 + y**2))) == 0
    na = line_num([P_, Q_], [t**2 - 4, t], -2, 2, (x, y), pts=[-2, 0, 2])
    assert abs(na + mp.pi) < 1e-10
    nb = line_num([P_, Q_], [2*cos(t), 3*sin(t)], 0, 2*pi, (x, y))
    assert abs(nb - 2*mp.pi) < 1e-10
Q(S3, id="q9", no="9", type="특이점이 있는 벡터장의 선적분", ref="2024 기말 4번 유형", types=["16-singular", "16-ftli"],
  stem=r"$\mathbf F(x,y)=\dfrac{3x-y}{x^2+y^2}\,\mathbf i+\dfrac{x+3y}{x^2+y^2}\,\mathbf j$ 에 대하여",
  parts=[("a", r"$C:\ \mathbf r(t)=(t^2-4)\,\mathbf i+t\,\mathbf j\ (-2\le t\le2)$ 일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$ 를 구하시오."),
         ("b", r"타원 $\dfrac{x^2}{4}+\dfrac{y^2}{9}=1$ 을 반시계 방향으로 한 바퀴 돌 때 $\displaystyle\oint\mathbf F\cdot d\mathbf r$ 를 구하시오.")],
  answer=[("a", r"$-\pi$"), ("b", r"$2\pi$")],
  solution=[("a", [r"$\mathbf F=\dfrac32\nabla\ln(x^2+y^2)+\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$ — 앞부분은 기울기장, 뒷부분의 선적분은 원점에 대한 각 $\theta$ 의 변화량",
                   r"시작 $(0,-2)$, 끝 $(0,2)$: $x^2+y^2$ 가 둘 다 $4$ → 첫 부분 $0$",
                   r"$C$ 는 $(0,-2)\to(-4,0)\to(0,2)$ 로 원점의 왼쪽을 돌아가요: $\theta$ 가 $\frac{3\pi}2\to\pi\to\frac\pi2$ (시계 방향) → $\Delta\theta=-\pi$",
                   r"답 $0+(-\pi)=-\pi$"]),
            ("b", [r"닫힌 곡선이라 기울기장 부분은 $0$, 원점을 반시계로 한 바퀴 감으므로 각의 변화 $2\pi$ → $2\pi$"])],
  check=_c)


def _c():
    V = integrate(rho**2*sin(ph), (rho, 0, cos(ph)**2), (ph, 0, pi/2), (th, 0, 2*pi))
    Mz = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, cos(ph)**2), (ph, 0, pi/2), (th, 0, 2*pi))
    assert EQ(V, 2*pi/21) and EQ(Mz, pi/20)
Q(S3, id="q10", no="10", type="구면좌표 삼중적분", ref="2024 중간 10번 유형", types=["15-sph"],
  stem=r"$E$ 가 곡면 $(x^2+y^2+z^2)^{3/2}=z^2$ 으로 둘러싸인 입체 중 $z\ge0$ 인 부분일 때,",
  parts=[("a", r"$E$ 의 부피를 구하시오."), ("b", r"$\displaystyle\iiint_Ez\,dV$ 를 구하시오.")],
  answer=[("a", r"$\dfrac{2\pi}{21}$"), ("b", r"$\dfrac{\pi}{20}$")],
  solution=[("a", [r"$\rho^3=\rho^2\cos^2\phi$ → 곡면 $\rho=\cos^2\phi$, $E=\{0\le\theta\le2\pi,\ 0\le\phi\le\frac\pi2,\ 0\le\rho\le\cos^2\phi\}$",
                   r"$V=2\pi\displaystyle\int_0^{\pi/2}\frac{\cos^6\phi}{3}\sin\phi\,d\phi=\frac{2\pi}{3}\cdot\frac17=\frac{2\pi}{21}$"]),
            ("b", [r"$\displaystyle\iiint_Ez\,dV=2\pi\int_0^{\pi/2}\!\!\int_0^{\cos^2\phi}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi=\frac\pi2\int_0^{\pi/2}\cos^9\phi\sin\phi\,d\phi=\frac{\pi}{20}$"])],
  check=_c)


SETS.append({"id": "s3", "no": 3, "title": "실전 모의고사 3회", "focus": "2024 중간 스타일",
             "lead": "2024학년도 중간고사 구성을 따라가요 — 임계점 + 음함수, 순서 바꾸기 + 삼중적분, 테일러로 보는 극한, 사면체·직육면체 라그랑주, 동차 꼴 연쇄법칙과 선형근사, 겹치는 원판, 2계 방향도함수, 원주→구면좌표. 9번은 2024 기말의 특이점 벡터장 유형이에요.",
             "problems": S3})


# ════════════════════════════════════════════════════════════════════
# 4회 — 2022 중간 스타일 (+16장)
# ════════════════════════════════════════════════════════════════════
S4 = []


def _c():
    fa = (2*x**3 - x*y)/(x**2 + y**2)
    mm = symbols('mm', real=True)
    assert simplify(limit(fa.subs(y, mm*x), x, 0) + mm/(1 + mm**2)) == 0
    import random
    random.seed(4)
    for _ in range(300):
        a, b, c = [random.uniform(-0.5, 0.5) for _ in range(3)]
        assert abs(a*a*b/(a*a + b*b)*mp.cos(1/(a*a + b*b))) <= abs(b) + 1e-15
        assert abs(a*a*b*c)/(a*a + b*b + c*c) <= (a*a + b*b + c*c) + 1e-15
Q(S4, id="q1", no="1", type="극한 (2변수 · 3변수)", ref="2022 중간 블럭1·2 1번 유형", types=["14-limit", "14-dne"],
  stem="다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
  parts=[("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{2x^3-xy}{x^2+y^2}$"),
         ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^2+y^2}\cos\Big(\frac{1}{x^2+y^2}\Big)$"),
         ("c", r"$\displaystyle\lim_{(x,y,z)\to(0,0,0)}\frac{x^2yz}{x^2+y^2+z^2}$")],
  answer=[("a", r"존재하지 않음 ($y=mx$ 를 따라 $-\tfrac{m}{1+m^2}$)"), ("b", r"$0$"), ("c", r"$0$")],
  solution=[("a", [r"$\dfrac{2x^3}{x^2+y^2}$ 부분은 $|\cdot|\le2|x|\to0$ 이지만 $\dfrac{-xy}{x^2+y^2}$ 은 방향마다 달라요",
                   r"$y=mx$: $\dfrac{2x^3-mx^2}{(1+m^2)x^2}\to-\dfrac{m}{1+m^2}$ → $m=0$ 이면 $0$, $m=1$ 이면 $-\frac12$ → 존재하지 않음"]),
            ("b", [r"$\dfrac{x^2}{x^2+y^2}\le1,\ |\cos(\cdot)|\le1$ → $|\cdot|\le|y|\to0$ → 극한 $0$"]),
            ("c", [r"$\rho^2=x^2+y^2+z^2$ 라 하면 $|x^2yz|\le\rho^2\cdot\rho\cdot\rho=\rho^4$ → $|\cdot|\le\rho^2\to0$ → 극한 $0$"])],
  check=_c)


def _c():
    test = x**2*y + 1
    p1 = integrate(test, (y, x/3, x), (x, 0, 1)) + integrate(test, (y, x/3, 1), (x, 1, 3))
    p2 = integrate(test, (x, y, 3*y), (y, 0, 1))
    assert EQ(p1, p2)
    assert EQ(integrate(2*y*exp(y**2), (y, 0, 1)), E - 1)
    num = (mp.quad(lambda X: mp.quad(lambda Y: mp.e**(Y*Y), [X/3, X]), [0, 1])
           + mp.quad(lambda X: mp.quad(lambda Y: mp.e**(Y*Y), [X/3, 1]), [1, 3]))
    assert abs(num - (mp.e - 1)) < 1e-10
    test2 = x**3 + y + 2
    q1 = integrate(test2, (y, 0, x + 1), (x, -1, 0)) + integrate(test2, (y, 0, 1 - x**2), (x, 0, 1))
    q2 = integrate(test2, (x, y - 1, sqrt(1 - y)), (y, 0, 1))
    assert EQ(q1, q2)
Q(S4, id="q2", no="2", type="적분 순서 바꾸기", ref="2022 중간 블럭1 2번 유형", types=["15-order"],
  stem="",
  parts=[("a", r"적분 영역을 그리고 계산하시오. $$\int_0^1\!\!\int_{x/3}^{x}e^{y^2}\,dy\,dx+\int_1^3\!\!\int_{x/3}^{1}e^{y^2}\,dy\,dx$$"),
         ("b", r"적분 영역을 그리고 순서를 바꾼 반복적분 하나로 나타내시오. (계산하지 않음) $$\int_{-1}^{0}\!\!\int_0^{x+1}f(x,y)\,dy\,dx+\int_0^1\!\!\int_0^{1-x^2}f(x,y)\,dy\,dx$$")],
  answer=[("a", r"$e-1$"), ("b", r"$\displaystyle\int_0^1\!\!\int_{y-1}^{\sqrt{1-y}}f(x,y)\,dx\,dy$")],
  solution=[("a", [r"두 영역을 합치면 직선 $y=x$, $y=\frac x3$, $y=1$ 로 둘러싸인 삼각형 → $0\le y\le1,\ y\le x\le3y$",
                   r"$$\int_0^1\!\!\int_y^{3y}e^{y^2}\,dx\,dy=\int_0^12ye^{y^2}\,dy=e-1$$"]),
            ("b", [r"영역: $x\in[-1,0]$ 에서 $0\le y\le x+1$ (직선), $x\in[0,1]$ 에서 $0\le y\le1-x^2$ (포물선)",
                   r"$y$ 를 고정하면 왼쪽 경계 $x=y-1$, 오른쪽 경계 $x=\sqrt{1-y}$ ($0\le y\le1$) → $\displaystyle\int_0^1\!\!\int_{y-1}^{\sqrt{1-y}}f\,dx\,dy$"])],
  check=_c)


def _c():
    rr_, ss_, tt_ = symbols('rr_ ss_ tt_')
    g = rr_**2*ss_ - tt_**2
    f = g.subs({rr_: 2*x - y, ss_: x**2 + y**2, tt_: x*y}, simultaneous=True)
    pt = {x: 1, y: 1}
    assert EQ(f.subs(pt), 1) and EQ(diff(f, x).subs(pt), 8) and EQ(diff(f, y).subs(pt), -4)
    assert EQ(1 + 8*R(2, 100) - 4*R(-3, 100), R(128, 100))
Q(S4, id="q3", no="3", type="연쇄법칙 · 선형화", ref="2022 중간 블럭1 3번 유형", types=["14-chain", "14-tangent"],
  stem=r"$f(x,y)=g\big(2x-y,\ x^2+y^2,\ xy\big)$, $g(r,s,t)=r^2s-t^2$ 일 때",
  parts=[("a", r"연쇄법칙으로 $f_x(1,1),\ f_y(1,1)$ 을 구하시오."), ("b", r"$f$ 의 점 $(1,1)$ 에서의 선형화를 구하시오."), ("c", r"(b)를 이용해 $f(1.02,\ 0.97)$ 의 근삿값을 구하시오.")],
  answer=[("a", r"$f_x=8,\ f_y=-4$"), ("b", r"$L(x,y)=1+8(x-1)-4(y-1)$"), ("c", r"$1.28$")],
  solution=[("a", [r"$(x,y)=(1,1)$ ↔ $(r,s,t)=(1,2,1)$. $g_r=2rs=4,\ g_s=r^2=1,\ g_t=-2t=-2$",
                   r"$f_x=g_r\cdot2+g_s\cdot2x+g_t\cdot y=8+2-2=8$",
                   r"$f_y=g_r\cdot(-1)+g_s\cdot2y+g_t\cdot x=-4+2-2=-4$"]),
            ("b", [r"$f(1,1)=g(1,2,1)=2-1=1$ → $L(x,y)=1+8(x-1)-4(y-1)$"]),
            ("c", [r"$f(1.02,0.97)\approx1+8(0.02)-4(-0.03)=1+0.16+0.12=1.28$"])],
  check=_c)


def _c():
    f = x**3 + 3*x*y**2 - 3*x**2 - 3*y**2 + 4
    crit = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    pts = sorted([(q[x], q[y]) for q in crit], key=lambda p: (float(p[0]), float(p[1])))
    assert pts == [(0, 0), (1, -1), (1, 1), (2, 0)]
    D = lambda a, b: ((diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2).subs({x: a, y: b}), diff(f, x, 2).subs({x: a, y: b}))
    assert D(0, 0) == (36, -6) and D(2, 0) == (36, 6) and D(1, 1)[0] == -36 and D(1, -1)[0] == -36
    assert f.subs({x: 0, y: 0}) == 4 and f.subs({x: 2, y: 0}) == 0
Q(S4, id="q4", no="4", type="극값과 안장점", ref="2022 중간 블럭1 4번 유형", types=["14-crit"],
  stem=r"$f(x,y)=x^3+3xy^2-3x^2-3y^2+4$ 의 극댓값, 극솟값, 안장점을 구하시오.",
  parts=[],
  answer=[("", r"극댓값 $f(0,0)=4$, 극솟값 $f(2,0)=0$, 안장점 $(1,\pm1)$")],
  solution=[("", [r"$f_x=3x^2+3y^2-6x=0,\ f_y=6xy-6y=6y(x-1)=0$",
                  r"$y=0$: $3x^2-6x=0 \Rightarrow x=0,2$;  $x=1$: $3+3y^2-6=0 \Rightarrow y=\pm1$",
                  r"$f_{xx}=6x-6,\ f_{yy}=6x-6,\ f_{xy}=6y$",
                  r"$(0,0)$: $D=36>0,\ f_{xx}=-6<0$ → 극댓값 $4$;  $(2,0)$: $D=36>0,\ f_{xx}=6>0$ → 극솟값 $0$;  $(1,\pm1)$: $D=0-36<0$ → 안장점"])],
  check=_c)


def _c():
    gf = 3*Matrix([2, 1, -2])/3
    kk = symbols('kk')
    gg = kk*Matrix([1, -2, 2])
    ksol = solve(gg.dot(Matrix([2, -1, 2])/3) + 8, kk)
    assert ksol == [-3]
    gg = gg.subs(kk, -3)
    assert gg == Matrix([-3, 6, -6])
    fP, gP = 2, 1
    gh = gP**2*gf + 2*fP*gP*gg
    assert gh == Matrix([-10, 25, -26]) and EQ(gh.dot(Matrix([1, 2, 2])/3), -4)
Q(S4, id="q5", no="5", type="주어진 정보로 그래디언트 구하기", ref="2022 중간 블럭1 5번 유형", types=["14-dir", "14-maxrate", "14-levelsurf"],
  stem=r"미분가능한 함수 $f,g$ 가 점 $P$ 에서 다음을 만족한다.<br>① $f$ 는 $P$ 에서 $\langle2,1,-2\rangle$ 방향으로 최대 변화율 $3$ 을 가진다.<br>② 곡면 $g(x,y,z)=1$ 의 $P$ 에서의 접평면이 평면 $x-2y+2z=0$ 과 평행하다.<br>③ $\mathbf u=\tfrac13\langle2,-1,2\rangle$ 에 대해 $D_{\mathbf u}g(P)=-8$ 이다.  ④ $f(P)=2,\ g(P)=1$",
  parts=[("a", r"$\nabla f(P)$ 를 구하시오."), ("b", r"$\nabla g(P)$ 를 구하시오."), ("c", r"$h=f\,g^2$ 일 때 $P$ 에서 $\langle1,2,2\rangle$ 방향으로의 $h$ 의 변화율을 구하시오.")],
  answer=[("a", r"$\langle2,1,-2\rangle$"), ("b", r"$\langle-3,6,-6\rangle$"), ("c", r"$-4$")],
  solution=[("a", [r"최대 변화율의 방향 = $\nabla f$ 방향, 크기 = $|\nabla f|=3$ → $\nabla f(P)=3\cdot\dfrac{\langle2,1,-2\rangle}{3}=\langle2,1,-2\rangle$"]),
            ("b", [r"접평면의 법선이 $\nabla g$ → $\nabla g(P)=k\langle1,-2,2\rangle$",
                   r"$D_{\mathbf u}g=k\cdot\dfrac{2+2+4}{3}=\dfrac{8k}{3}=-8 \Rightarrow k=-3$ → $\nabla g(P)=\langle-3,6,-6\rangle$"]),
            ("c", [r"$\nabla h=g^2\nabla f+2fg\nabla g=\langle2,1,-2\rangle+4\langle-3,6,-6\rangle=\langle-10,25,-26\rangle$",
                   r"단위벡터 $\tfrac13\langle1,2,2\rangle$: $D h=\dfrac{-10+50-52}{3}=-4$"])],
  check=_c)


def _c():
    f = 2*x**3 + y**4
    lam = symbols('lam')
    sols = solve([6*x**2 - 2*lam*x, 4*y**3 - 2*lam*y, x**2 + y**2 - 1], [x, y, lam], dict=True)
    vals = sorted({f.subs(q) for q in sols}, key=float)
    assert vals[0] == -2 and vals[-1] == 2 and R(13, 16) in vals and 1 in vals
    assert solve([diff(f, x), diff(f, y)], [x, y]) == [(0, 0)] or solve([diff(f, x), diff(f, y)], [x, y], dict=True) == [{x: 0, y: 0}]
Q(S4, id="q6", no="6", type="닫힌 영역의 최대·최소 (라그랑주)", ref="2022 중간 블럭2 5(b) · 블럭1 6번 유형", types=["14-absext", "14-lagrange"],
  stem=r"$f(x,y)=2x^3+y^4$ 의 닫힌 원판 $D=\{(x,y)\mid x^2+y^2\le1\}$ 위에서의 최댓값과 최솟값을 구하시오. (경계에서는 라그랑주 승수법을 쓰시오.)",
  parts=[],
  answer=[("", r"최댓값 $2$ (점 $(1,0)$), 최솟값 $-2$ (점 $(-1,0)$)")],
  solution=[("", [r"내부: $f_x=6x^2=0,\ f_y=4y^3=0$ → $(0,0)$, $f=0$",
                  r"경계 $x^2+y^2=1$: $6x^2=2\lambda x,\ 4y^3=2\lambda y$ → ($x=0$ 또는 $\lambda=3x$) 그리고 ($y=0$ 또는 $\lambda=2y^2$)",
                  r"$x=0$: $(0,\pm1)$, $f=1$.  $y=0$: $(\pm1,0)$, $f=\pm2$.  둘 다 아니면 $3x=2y^2=2(1-x^2)$ → $2x^2+3x-2=0$ → $x=\frac12,\ y^2=\frac34$, $f=\frac14+\frac9{16}=\frac{13}{16}$",
                  r"후보 $0,\ 1,\ \pm2,\ \frac{13}{16}$ 비교 → 최댓값 $2$ ($(1,0)$), 최솟값 $-2$ ($(-1,0)$)"])],
  check=_c)


def _c():
    m_ = symbols('m_', positive=True)
    # 평면 x + y + m z = 3 이 x^2 + y^2/4 + z^2/2 = 1 에 접할 조건: 접점 (1/3, 4/3, 2m/3)
    msol = solve(R(1, 9) + R(16, 9)/4 + (2*m_/3)**2/2 - 1, m_)
    assert msol == [sqrt(2)]
    pt = Matrix([R(1, 3), R(4, 3), 2*sqrt(2)/3])
    nrm = Matrix([2*pt[0], pt[1]/2, pt[2]])
    assert all(EQ(c_, 0) for c_ in nrm.cross(Matrix([1, 1, sqrt(2)]))) and EQ(pt[0] + pt[1] + sqrt(2)*pt[2], 3)
    a_ = -sqrt(2)/4
    kk = (3 - 2*a_)/sqrt(2) - 2*a_**2
    assert EQ(kk, 3*sqrt(2)/2 + R(1, 4))
    assert EQ(2*a_, -1/sqrt(2))
Q(S4, id="q7", no="7", type="접평면 조건 (타원면 · 포물면)", ref="2022 중간 블럭1 7번 유형", types=["14-levelsurf", "14-tangent"],
  stem="",
  parts=[("a", r"평면 $x+y+mz=3$ 이 타원면 $x^2+\dfrac{y^2}{4}+\dfrac{z^2}{2}=1$ 에 접할 때 양수 $m$ 을 구하시오."),
         ("b", r"(a)의 $m$ 에 대해 평면 $x+y+mz=3$ 이 포물면 $z=x^2+y^2+k$ 에도 접할 때 실수 $k$ 를 구하시오.")],
  answer=[("a", r"$m=\sqrt2$"), ("b", r"$k=\dfrac{3\sqrt2}{2}+\dfrac14$")],
  solution=[("a", [r"접점 $(a,b,c)$ 에서의 접평면: $ax+\dfrac b4y+\dfrac c2z=1$. 이것이 $\dfrac x3+\dfrac y3+\dfrac m3z=1$ 과 같아야 하므로 $a=\tfrac13,\ b=\tfrac43,\ c=\tfrac{2m}{3}$",
                   r"타원면 위: $\tfrac19+\tfrac{16}{9}\cdot\tfrac14+\tfrac{4m^2}{9}\cdot\tfrac12=1 \Rightarrow \tfrac{5}{9}+\tfrac{2m^2}{9}=1 \Rightarrow m^2=2$ → $m=\sqrt2$"]),
            ("b", [r"평면: $z=\dfrac{3-x-y}{\sqrt2}$. 포물면의 $(a,b)$ 에서 접평면 기울기 $2a=2b=-\dfrac1{\sqrt2}$ → $a=b=-\dfrac{\sqrt2}{4}$",
                   r"접점의 높이 $a^2+b^2+k=\tfrac14+k$ 가 평면 위의 값 $\dfrac{3-a-b}{\sqrt2}=\dfrac{3}{\sqrt2}+\dfrac12$ 와 같아야 함",
                   r"$k=\dfrac{3}{\sqrt2}+\dfrac14=\dfrac{3\sqrt2}{2}+\dfrac14$"])],
  check=_c)


def _c():
    M = integrate(r*cos(th)*r, (r, 1, 2*sin(th)), (th, pi/6, pi/2))
    Mx = integrate(r*sin(th)*r*cos(th)*r, (r, 1, 2*sin(th)), (th, pi/6, pi/2))
    assert EQ(M, R(11, 24)) and EQ(Mx, R(9, 16)) and EQ(Mx/M, R(27, 22))
Q(S4, id="q8", no="8", type="판의 질량 · 질량중심", ref="2022 중간 블럭1 8번 유형", types=["15-mass", "15-polar"],
  stem=r"판이 영역 $D=\{(x,y)\mid x^2+y^2\le2y,\ x^2+y^2\ge1,\ x\ge0\}$ 을 차지하고 밀도가 $\rho(x,y)=x$ 일 때",
  parts=[("a", r"판의 질량을 구하시오."), ("b", r"질량중심의 $y$ 좌표를 구하시오.")],
  answer=[("a", r"$\dfrac{11}{24}$"), ("b", r"$\bar y=\dfrac{27}{22}$")],
  solution=[("a", [r"$r=2\sin\theta$ 와 $r=1$ 의 교점 $\theta=\frac\pi6$, $x\ge0$ → $D:\ \frac\pi6\le\theta\le\frac\pi2,\ 1\le r\le2\sin\theta$",
                   r"$$\begin{aligned}m&=\int_{\pi/6}^{\pi/2}\!\!\int_1^{2\sin\theta}r^2\cos\theta\,dr\,d\theta=\int_{\pi/6}^{\pi/2}\frac{8\sin^3\theta-1}{3}\cos\theta\,d\theta\\&=\frac13\Big[2\sin^4\theta-\sin\theta\Big]_{\pi/6}^{\pi/2}=\frac13\Big(1-\big(\tfrac18-\tfrac12\big)\Big)=\frac{11}{24}\end{aligned}$$"]),
            ("b", [r"$$\begin{aligned}M_x&=\iint_Dy\,\rho\,dA=\int_{\pi/6}^{\pi/2}\!\!\int_1^{2\sin\theta}r^3\sin\theta\cos\theta\,dr\,d\theta\\&=\frac14\Big[\frac{16\sin^6\theta}{6}-\frac{\sin^2\theta}{2}\Big]_{\pi/6}^{\pi/2}=\frac14\Big(\frac{13}{6}+\frac1{12}\Big)=\frac{9}{16}\end{aligned}$$",
                   r"$\bar y=\dfrac{9/16}{11/24}=\dfrac{27}{22}$"])],
  check=_c)


def _c():
    tq = symbols('tq', real=True)
    # ∫f = 2, ∫uf = 1/2 를 만족하는 f 의 예 두 개로 확인
    for fexpr in (5 - 6*u, 6 - 12*u + 6*u**2):
        assert EQ(integrate(fexpr, (u, 0, 1)), 2) and EQ(integrate(u*fexpr, (u, 0, 1)), R(1, 2))
        G = integrate(fexpr, (u, 0, tq))
        assert EQ(integrate(G*sqrt(2), (tq, 0, 1)), 3*sqrt(2)/2)
    rr = Matrix([tq, 0, -tq])
    assert simplify(rr[0]*rr[1] - rr[2] - tq) == 0 and simplify(rr.diff(tq).norm() - sqrt(2)) == 0
Q(S4, id="q9", no="9", type="선적분의 기본정리 (적분으로 정의된 함수)", ref="2024 기말 3번 유형", types=["16-ftli", "16-scalar"],
  stem=r"연속함수 $f$ 가 $\displaystyle\int_0^1f(u)\,du=2,\ \int_0^1uf(u)\,du=\frac12$ 를 만족하고 $g(x,y,z)=\displaystyle\int_0^{xy-z}f(u)\,du$ 이다.",
  parts=[("a", r"$C$ 가 $(1,1,1)$ 에서 $(1,1,0)$ 까지 가는 임의의 매끄러운 곡선일 때 $\displaystyle\int_Cf(xy-z)\,(y\,dx+x\,dy-dz)$ 를 구하시오."),
         ("b", r"$C$ 가 $(0,0,0)$ 에서 $(1,0,-1)$ 까지의 선분일 때 $\displaystyle\int_Cg(x,y,z)\,ds$ 를 구하시오.")],
  answer=[("a", r"$2$"), ("b", r"$\dfrac{3\sqrt2}{2}$")],
  solution=[("a", [r"$\nabla g=f(xy-z)\,\langle y,\ x,\ -1\rangle$ → 피적분 벡터장이 $\nabla g$",
                   r"값 $=g(1,1,0)-g(1,1,1)=\displaystyle\int_0^1f\,du-\int_0^0f\,du=2$"]),
            ("b", [r"$\mathbf r(t)=\langle t,0,-t\rangle$: $xy-z=t$, $ds=\sqrt2\,dt$ → $\displaystyle\int_Cg\,ds=\sqrt2\int_0^1G(t)\,dt$, $G(t)=\int_0^tf$",
                   r"부분적분: $\displaystyle\int_0^1G(t)\,dt=\big[tG(t)\big]_0^1-\int_0^1tf(t)\,dt=2-\frac12=\frac32$ → $\dfrac{3\sqrt2}{2}$"])],
  check=_c)


def _c():
    P_, Q_ = exp(x) + x*y, x**2 + 3*x + sin(y)
    assert simplify(diff(Q_, x) - diff(P_, y) - (x + 3)) == 0
    I = integrate((r*cos(th) + 3)*r, (r, 0, 2*cos(th)), (th, 0, pi/2))
    assert EQ(I, 2*pi)
    num = line_num([P_, Q_], [1 + cos(t), sin(t)], 0, pi, (x, y))
    assert abs(num - (2*mp.pi + 1 - mp.e**2)) < 1e-10
Q(S4, id="q10", no="10", type="그린 정리 (열린 곡선 닫기)", ref="2022 기말 블럭2 4번 유형", types=["16-green"],
  stem=r"$\mathbf F(x,y)=\big\langle e^x+xy,\ x^2+3x+\sin y\big\rangle$ 이고 $C$ 는 원 $x^2+y^2=2x$ 의 위쪽 반원을 $(2,0)$ 에서 $(0,0)$ 까지 가는 곡선이다. 그린 정리를 이용하여 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$ 를 구하시오.",
  parts=[],
  answer=[("", r"$2\pi+1-e^2$")],
  solution=[("", [r"선분 $L$: $(0,0)\to(2,0)$ 을 붙이면 $C+L$ 은 위쪽 반원판 $D$ ($(x-1)^2+y^2\le1,\ y\ge0$) 의 양의 방향 경계",
                  r"$Q_x-P_y=(2x+3)-x=x+3$ → $\displaystyle\iint_D(x+3)\,dA=\bar x\cdot A+3A=1\cdot\frac\pi2+\frac{3\pi}{2}=2\pi$ (반원판의 $\bar x=1$)",
                  r"$L$: $y=0,\ dy=0$ → $\displaystyle\int_L\mathbf F\cdot d\mathbf r=\int_0^2e^x\,dx=e^2-1$",
                  r"$\displaystyle\int_C=2\pi-(e^2-1)=2\pi+1-e^2$"])],
  check=_c)


SETS.append({"id": "s4", "no": 4, "title": "실전 모의고사 4회", "focus": "2022 중간 스타일 + 16장",
             "lead": "2022학년도 중간고사(블럭 1·2)의 단골 유형을 모았어요 — 2·3변수 극한, 적분 영역 그리고 순서 바꾸기, 합성함수 연쇄법칙과 선형화, 극값, 정보로 그래디언트 복원, 원판 위 최대·최소, 접평면 조건, 판의 질량중심. 마지막 두 문항은 16장(적분으로 정의된 함수, 열린 곡선의 그린 정리)이에요.",
             "problems": S4})


# ════════════════════════════════════════════════════════════════════
# 5회 — 종합 심화 (12–16장 전 범위)
# ════════════════════════════════════════════════════════════════════
S5 = []


def _c():
    n1, n2 = Matrix([1, 1, 1]), Matrix([1, -1, 2])
    d = n1.cross(n2)
    assert d == Matrix([3, -1, -2])
    Q0 = Matrix([R(3, 2), R(1, 2), 0])
    assert Q0.dot(n1) == 2 and Q0.dot(n2) == 1
    P0 = Matrix([1, 2, 3])
    dist = (P0 - Q0).cross(d).norm()/d.norm()
    assert EQ(dist, 2*sqrt(70)/7)
    L = integrate(exp(t) + exp(-t), (t, 0, 1))
    rr = Matrix([exp(t), exp(-t), sqrt(2)*t])
    assert simplify(rr.diff(t).dot(rr.diff(t)) - (exp(t) + exp(-t))**2) == 0
    assert EQ(L, E - exp(-1))
Q(S5, id="q1", no="1", type="직선·평면과 곡선의 길이 (12–13장)", ref="복습 12–13장 · 과제 12.5, 13.3 유형", types=["12-line", "12-dist", "13-arc"],
  stem="",
  parts=[("a", r"두 평면 $x+y+z=2$ 와 $x-y+2z=1$ 의 교선의 매개방정식을 구하시오."),
         ("b", r"점 $P(1,2,3)$ 과 (a)의 직선 사이의 거리를 구하시오."),
         ("c", r"곡선 $\mathbf r(t)=\big\langle e^t,\ e^{-t},\ \sqrt2\,t\big\rangle$ 의 $0\le t\le1$ 부분의 길이를 구하시오.")],
  answer=[("a", r"$x=\tfrac32+3t,\ y=\tfrac12-t,\ z=-2t$"), ("b", r"$\dfrac{2\sqrt{70}}{7}$"), ("c", r"$e-\dfrac1e$")],
  solution=[("a", [r"방향: $\langle1,1,1\rangle\times\langle1,-1,2\rangle=\langle3,-1,-2\rangle$",
                   r"한 점: $z=0$ 이면 $x+y=2,\ x-y=1$ → $\big(\tfrac32,\tfrac12,0\big)$ → $x=\tfrac32+3t,\ y=\tfrac12-t,\ z=-2t$"]),
            ("b", [r"$Q=\big(\tfrac32,\tfrac12,0\big)$, $\overrightarrow{QP}=\big\langle-\tfrac12,\tfrac32,3\big\rangle$, $\overrightarrow{QP}\times\langle3,-1,-2\rangle=\langle0,8,-4\rangle$",
                   r"$d=\dfrac{|\overrightarrow{QP}\times\mathbf d|}{|\mathbf d|}=\dfrac{\sqrt{80}}{\sqrt{14}}=\dfrac{4\sqrt5}{\sqrt{14}}=\dfrac{2\sqrt{70}}{7}$"]),
            ("c", [r"$|\mathbf r'(t)|^2=e^{2t}+e^{-2t}+2=(e^t+e^{-t})^2$",
                   r"$L=\displaystyle\int_0^1(e^t+e^{-t})\,dt=e-e^{-1}$"])],
  check=_c)


def _c():
    f = (2*x**3 - y**5)/(2*x**2 + x**2*y**2 + y**4)
    hh = symbols('hh', nonzero=True)
    assert simplify(f.subs({x: hh, y: 0}) - hh) == 0
    assert simplify(f.subs({x: 0, y: hh}) + hh) == 0
    yq = symbols('yq', nonzero=True)
    fx0y = limit((f.subs({x: hh, y: yq}) - f.subs({x: 0, y: yq}))/hh, hh, 0)
    assert simplify(fx0y) == 0
    import random
    random.seed(5)
    for _ in range(300):
        a, b = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
        val = abs(2*a**3 - b**5)/(2*a*a + a*a*b*b + b**4)
        assert val <= abs(a) + abs(b) + 1e-15
Q(S5, id="q2", no="2", type="연속성 · 정의로 구하는 편도함수", ref="2022 중간 블럭2 2번 유형", types=["14-defpartial"],
  stem=r"$f(x,y)=\begin{cases}\dfrac{2x^3-y^5}{2x^2+x^2y^2+y^4} & (x,y)\ne(0,0)\\[2mm] 0 & (x,y)=(0,0)\end{cases}$ 에 대하여",
  parts=[("a", r"$f$ 가 원점에서 연속임을 보이시오."),
         ("b", r"$f_x(0,0)$ 과 $f_{xx}(0,0)$ 을 구하시오."),
         ("c", r"$y\ne0$ 일 때 $f_x(0,y)$ 를 구하고, $f_{xy}(0,0)$ 이 존재하지 않음을 보이시오.")],
  answer=[("a", r"$|f|\le|x|+|y|\to0$"), ("b", r"$f_x(0,0)=1,\ f_{xx}(0,0)=0$"), ("c", r"$f_x(0,y)=0\ (y\ne0)$ → $\dfrac{f_x(0,k)-f_x(0,0)}{k}=-\dfrac1k$ 발산")],
  solution=[("a", [r"$\Big|\dfrac{2x^3}{2x^2+x^2y^2+y^4}\Big|\le\dfrac{2|x|^3}{2x^2}=|x|$,  $\Big|\dfrac{y^5}{2x^2+x^2y^2+y^4}\Big|\le\dfrac{|y|^5}{y^4}=|y|$",
                   r"$|f(x,y)|\le|x|+|y|\to0=f(0,0)$ → 연속"]),
            ("b", [r"$f(x,0)=\dfrac{2x^3}{2x^2}=x$ ($x\ne0$), $f(0,0)=0$ → 모든 $x$ 에서 $f(x,0)=x$",
                   r"따라서 $f_x(x,0)=1$ (모든 $x$) → $f_x(0,0)=1$, $f_{xx}(0,0)=\displaystyle\lim_{h\to0}\frac{1-1}{h}=0$"]),
            ("c", [r"$y\ne0$: $f(0,y)=-y$, $\dfrac{f(h,y)-f(0,y)}{h}=\dfrac{2h^2+2hy+hy^3}{2h^2+h^2y^2+y^4}\to0$ → $f_x(0,y)=0$",
                   r"$f_{xy}(0,0)=\displaystyle\lim_{k\to0}\frac{f_x(0,k)-f_x(0,0)}{k}=\lim_{k\to0}\frac{0-1}{k}$ → 발산, 존재하지 않음"])],
  check=_c)


def _c():
    f = taylor2(sqrt(3), 1, 5, 2, -1, 1, 0, 3)
    rp = symbols('rp', positive=True)
    Z = f.subs({x: rp*cos(th), y: rp*sin(th)}, simultaneous=True)
    pt = {rp: 2, th: pi/6}
    assert EQ(diff(Z, rp, 2).subs(pt), R(3, 2)) and EQ(diff(Z, rp, th).subs(pt), sqrt(3)/2 - 1)
    F = x**2*y + exp(x)*y**3
    Zf = F.subs({x: rp*cos(th), y: rp*sin(th)}, simultaneous=True)
    lhs = diff(Zf, rp)**2 + (diff(Zf, th)/rp)**2
    rhs = (diff(F, x)**2 + diff(F, y)**2).subs({x: rp*cos(th), y: rp*sin(th)}, simultaneous=True)
    for vals in ({rp: 2, th: R(1, 3)}, {rp: R(1, 2), th: 2}):
        assert EQ(lhs.subs(vals), rhs.subs(vals))
Q(S5, id="q3", no="3", type="극좌표 연쇄법칙 (2계)", ref="강의 14.5 · 2025 중간 5번 응용", types=["14-chain2", "14-chain"],
  stem=r"$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=r\cos\theta,\ y=r\sin\theta$ 이다.",
  parts=[("a", r"$\Big(\dfrac{\partial z}{\partial r}\Big)^2+\dfrac{1}{r^2}\Big(\dfrac{\partial z}{\partial\theta}\Big)^2=\big(f_x\big)^2+\big(f_y\big)^2$ 임을 보이시오."),
         ("b", r"점 $(\sqrt3,1)$ 에서 $f_x=2,\ f_y=-1,\ f_{xx}=1,\ f_{xy}=0,\ f_{yy}=3$ 일 때 $(r,\theta)=\big(2,\tfrac\pi6\big)$ 에서 $z_{rr}$ 와 $z_{r\theta}$ 를 구하시오.")],
  answer=[("a", r"아래 풀이"), ("b", r"$z_{rr}=\dfrac32,\ z_{r\theta}=\dfrac{\sqrt3}{2}-1$")],
  solution=[("a", [r"$z_r=f_x\cos\theta+f_y\sin\theta$, $z_\theta=-r\sin\theta f_x+r\cos\theta f_y$ → $\dfrac{z_\theta}{r}=-f_x\sin\theta+f_y\cos\theta$",
                   r"제곱해 더하면 교차항이 지워지고 $(\cos^2\theta+\sin^2\theta)(f_x^2+f_y^2)=f_x^2+f_y^2$"]),
            ("b", [r"$(r,\theta)=(2,\frac\pi6)$ ↔ $(x,y)=(\sqrt3,1)$, $\cos\theta=\frac{\sqrt3}2,\ \sin\theta=\frac12$, $x_\theta=-r\sin\theta=-1,\ y_\theta=r\cos\theta=\sqrt3$",
                   r"$z_{rr}=f_{xx}\cos^2\theta+2f_{xy}\sin\theta\cos\theta+f_{yy}\sin^2\theta=\tfrac34+0+\tfrac34=\tfrac32$",
                   r"$z_{r\theta}=\dfrac{\partial}{\partial\theta}(f_x\cos\theta+f_y\sin\theta)=-f_x\sin\theta+f_y\cos\theta+\cos\theta\,(f_{xx}x_\theta+f_{xy}y_\theta)+\sin\theta\,(f_{yx}x_\theta+f_{yy}y_\theta)$",
                   r"$=-1-\tfrac{\sqrt3}{2}+\tfrac{\sqrt3}{2}(-1)+\tfrac12(3\sqrt3)=\tfrac{\sqrt3}{2}-1$"])],
  check=_c)


def _c():
    F1 = x**2 + y**2 + z**2
    F2 = x**2 - y**2 - z
    P0 = {x: 2, y: 1, z: 2}
    assert F1.subs(P0) == 9 and F2.subs(P0) == 1
    g1, g2 = grad(F1, (x, y, z)).subs(P0), grad(F2, (x, y, z)).subs(P0)
    assert g1.cross(g2) == Matrix([6, 20, -16])
    assert EQ(abs(g1.dot(g2))/(g1.norm()*g2.norm()), 4*sqrt(21)/63)
    tt_ = symbols('tt_')
    line = Matrix([2, 1, 2]) + tt_*g2
    tz = solve(line[2], tt_)[0]
    assert line.subs(tt_, tz) == Matrix([10, -3, 0])
Q(S5, id="q4", no="4", type="교선의 접선 · 두 곡면 사이의 각", ref="강의 14.6 · 2022 중간 블럭1 7번 응용", types=["14-levelsurf", "13-tplane"],
  stem=r"구 $S_1:\ x^2+y^2+z^2=9$ 와 곡면 $S_2:\ z=x^2-y^2-1$ 이 점 $P(2,1,2)$ 에서 만난다.",
  parts=[("a", r"$P$ 에서 두 곡면의 교선의 접선의 매개방정식을 구하시오."),
         ("b", r"$P$ 에서 두 곡면이 이루는 각 $\theta$ (법선끼리의 예각)에 대해 $\cos\theta$ 를 구하시오."),
         ("c", r"$P$ 에서 $S_2$ 의 법선이 $xy$ 평면과 만나는 점을 구하시오.")],
  answer=[("a", r"$x=2+3t,\ y=1+10t,\ z=2-8t$"), ("b", r"$\dfrac{4\sqrt{21}}{63}$"), ("c", r"$(10,-3,0)$")],
  solution=[("a", [r"$\nabla F_1=\langle2x,2y,2z\rangle=\langle4,2,4\rangle$, $S_2$ 를 $F_2=x^2-y^2-z=1$ 로 보면 $\nabla F_2=\langle2x,-2y,-1\rangle=\langle4,-2,-1\rangle$",
                   r"접선 방향 $\nabla F_1\times\nabla F_2=\langle6,20,-16\rangle\parallel\langle3,10,-8\rangle$ → $x=2+3t,\ y=1+10t,\ z=2-8t$"]),
            ("b", [r"$\cos\theta=\dfrac{|\langle4,2,4\rangle\cdot\langle4,-2,-1\rangle|}{6\cdot\sqrt{21}}=\dfrac{8}{6\sqrt{21}}=\dfrac{4}{3\sqrt{21}}=\dfrac{4\sqrt{21}}{63}$"]),
            ("c", [r"법선: $(2+4t,\ 1-2t,\ 2-t)$, $z=0$ 이면 $t=2$ → $(10,-3,0)$"])],
  check=_c)


def _c():
    f = x**2 + 2*y**2 - x
    lam = symbols('lam')
    sols = solve([2*x - 1 - 2*lam*x, 4*y - 2*lam*y, x**2 + y**2 - 1], [x, y, lam], dict=True)
    vals = sorted({f.subs(q) for q in sols}, key=float)
    assert vals[-1] == R(9, 4) and 0 in vals
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: R(1, 2), y: 0}
    assert f.subs({x: R(1, 2), y: 0}) == R(-1, 4)
Q(S5, id="q5", no="5", type="닫힌 원판에서 최대·최소 (라그랑주)", ref="2022 중간 블럭2 5번 유형", types=["14-absext", "14-lagrange"],
  stem=r"$f(x,y)=x^2+2y^2-x$ 의 닫힌 원판 $x^2+y^2\le1$ 위에서의 최댓값과 최솟값을 구하시오. (경계는 라그랑주 승수법)",
  parts=[],
  answer=[("", r"최댓값 $\dfrac94$ (점 $\big(-\tfrac12,\pm\tfrac{\sqrt3}{2}\big)$), 최솟값 $-\dfrac14$ (점 $\big(\tfrac12,0\big)$)")],
  solution=[("", [r"내부: $f_x=2x-1=0,\ f_y=4y=0$ → $\big(\tfrac12,0\big)$, $f=-\tfrac14$",
                  r"경계: $2x-1=2\lambda x,\ 4y=2\lambda y$ → $y=0$ 또는 $\lambda=2$",
                  r"$y=0$: $(\pm1,0)$ 에서 $f(1,0)=0,\ f(-1,0)=2$.  $\lambda=2$: $2x-1=4x \Rightarrow x=-\tfrac12,\ y^2=\tfrac34$ → $f=\tfrac14+\tfrac32+\tfrac12=\tfrac94$",
                  r"후보 비교 → 최댓값 $\tfrac94$, 최솟값 $-\tfrac14$"])],
  check=_c)


def _c():
    rp = symbols('rp', positive=True)
    inner = integrate(sqrt(4 - rp**2)*rp, (rp, 0, 2*u))      # u = cosθ ≥ 0
    assert simplify(inner - (8 - (4 - 4*u**2)**R(3, 2))/3) == 0
    V = 2*integrate((8 - 8*sin(th)**3)/3, (th, 0, pi/2))      # (4 sin²θ)^{3/2} = 8|sinθ|³, 대칭
    assert EQ(V, 8*pi/3 - R(32, 9))
    num = mp.quad(lambda T: (8 - (4 - 4*mp.cos(T)**2)**1.5)/3, [-mp.pi/2, 0, mp.pi/2])
    assert abs(num - (8*mp.pi/3 - mp.mpf(32)/9)) < 1e-10
Q(S5, id="q6", no="6", type="극좌표로 부피 (구와 원기둥)", ref="2022 중간 블럭1 9번 유형", types=["15-polar"],
  stem="",
  parts=[("a", r"원기둥 $x^2+y^2=2x$ 의 내부에서 $xy$ 평면 위, 구 $x^2+y^2+z^2=4$ 아래에 있는 입체의 부피를 구하시오."),
         ("b", r"구 $x^2+y^2+z^2=4$ 와 원기둥 $x^2+y^2=2x$ 의 공통 내부의 부피를 구하시오.")],
  answer=[("a", r"$\dfrac{8\pi}{3}-\dfrac{32}{9}$"), ("b", r"$\dfrac{16\pi}{3}-\dfrac{64}{9}$")],
  solution=[("a", [r"밑면 $r\le2\cos\theta\ (-\frac\pi2\le\theta\le\frac\pi2)$, 높이 $\sqrt{4-r^2}$",
                   r"$$\begin{aligned}V&=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}\sqrt{4-r^2}\,r\,dr\,d\theta=\int_{-\pi/2}^{\pi/2}\frac{8-(4\sin^2\theta)^{3/2}}{3}\,d\theta\\&=\frac{8\pi}{3}-\frac83\int_{-\pi/2}^{\pi/2}|\sin\theta|^3d\theta=\frac{8\pi}{3}-\frac83\cdot\frac43=\frac{8\pi}3-\frac{32}9\end{aligned}$$",
                   r"주의: $(\sin^2\theta)^{3/2}=|\sin\theta|^3$ — 절댓값을 빼먹으면 $0$ 이 되어 틀려요"]),
            ("b", [r"위아래 대칭이므로 (a)의 2배: $\dfrac{16\pi}{3}-\dfrac{64}{9}$"])],
  check=_c)


def _c():
    test = x + y*z**2 + 1
    orig = integrate(test, (y, 0, 1 - x), (z, 0, 1 - x**2), (x, 0, 1))
    new = (integrate(test, (x, 0, 1 - y), (z, 0, 2*y - y**2), (y, 0, 1))
           + integrate(test, (x, 0, sqrt(1 - z)), (z, 2*y - y**2, 1), (y, 0, 1)))
    assert EQ(orig, new)
    V = integrate(1, (y, 0, 1 - x), (z, 0, 1 - x**2), (x, 0, 1))
    My = integrate(y, (y, 0, 1 - x), (z, 0, 1 - x**2), (x, 0, 1))
    assert EQ(V, R(5, 12)) and EQ(My, R(3, 20))
Q(S5, id="q7", no="7", type="삼중적분 순서 바꾸기", ref="2022 중간 블럭2 8(a) 유형", types=["15-order3", "15-triple"],
  stem=r"$I=\displaystyle\int_0^1\!\!\int_0^{1-x^2}\!\!\int_0^{1-x}f(x,y,z)\,dy\,dz\,dx$ 에 대하여",
  parts=[("a", r"$I$ 를 $dx\,dz\,dy$ 순서로 다시 쓰시오."), ("b", r"$f=1$ 일 때 $I$ (적분 영역의 부피)를 구하시오."), ("c", r"$f=y$ 일 때 $I$ 를 구하시오.")],
  answer=[("a", r"$\displaystyle\int_0^1\!\!\int_0^{2y-y^2}\!\!\int_0^{1-y}f\,dx\,dz\,dy+\int_0^1\!\!\int_{2y-y^2}^{1}\!\!\int_0^{\sqrt{1-z}}f\,dx\,dz\,dy$"), ("b", r"$\dfrac{5}{12}$"), ("c", r"$\dfrac{3}{20}$")],
  solution=[("a", [r"영역: $0\le x\le1,\ 0\le z\le1-x^2,\ 0\le y\le1-x$ → $(y,z)$ 를 고정하면 $x$ 는 $x\le1-y$ 와 $x\le\sqrt{1-z}$ 를 모두 만족",
                   r"$1-y\le\sqrt{1-z} \iff z\le1-(1-y)^2=2y-y^2$ → 그 아래에서는 $x\le1-y$, 위에서는 $x\le\sqrt{1-z}$ (경계가 바뀌는 곡선으로 나눠요)"]),
            ("b", [r"$V=\displaystyle\int_0^1(1-x)(1-x^2)\,dx=\int_0^1(1-x-x^2+x^3)\,dx=1-\frac12-\frac13+\frac14=\frac5{12}$"]),
            ("c", [r"$\displaystyle\int_0^1\!\!\int_0^{1-x^2}\frac{(1-x)^2}{2}\,dz\,dx=\frac12\int_0^1(1-x)^3(1+x)\,dx\overset{w=1-x}{=}\frac12\int_0^1w^3(2-w)\,dw=\frac12\Big(\frac12-\frac15\Big)=\frac{3}{20}$"])],
  check=_c)


def _c():
    V = integrate(rho**2*sin(ph), (rho, 1, 2), (ph, 0, pi/3), (th, 0, 2*pi))
    Mz = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 1, 2), (ph, 0, pi/3), (th, 0, 2*pi))
    assert EQ(V, 7*pi/3) and EQ(Mz, 45*pi/16) and EQ(Mz/V, R(135, 112))
Q(S5, id="q8", no="8", type="구면좌표 (무게중심)", ref="2022 중간 블럭2 10번 유형", types=["15-sph", "15-mass"],
  stem=r"$E$ 가 두 구 $x^2+y^2+z^2=1$, $x^2+y^2+z^2=4$ 사이에 있고 원뿔 $z=\sqrt{\dfrac{x^2+y^2}{3}}$ 위쪽에 있는 밀도가 일정한 입체일 때",
  parts=[("a", r"$E$ 의 부피를 구하시오."), ("b", r"$E$ 의 질량중심을 구하시오.")],
  answer=[("a", r"$\dfrac{7\pi}{3}$"), ("b", r"$\Big(0,\ 0,\ \dfrac{135}{112}\Big)$")],
  solution=[("a", [r"원뿔: $\tan\phi=\dfrac{r}{z}=\sqrt3$ → $\phi=\frac\pi3$. $E=\{1\le\rho\le2,\ 0\le\phi\le\frac\pi3\}$",
                   r"$V=2\pi\cdot\big(1-\cos\tfrac\pi3\big)\cdot\dfrac{8-1}{3}=2\pi\cdot\dfrac12\cdot\dfrac73=\dfrac{7\pi}{3}$"]),
            ("b", [r"대칭 → $\bar x=\bar y=0$",
                   r"$\displaystyle\iiint z\,dV=2\pi\int_0^{\pi/3}\cos\phi\sin\phi\,d\phi\int_1^2\rho^3d\rho=2\pi\cdot\frac38\cdot\frac{15}{4}=\frac{45\pi}{16}$",
                   r"$\bar z=\dfrac{45\pi/16}{7\pi/3}=\dfrac{135}{112}$"])],
  check=_c)


def _c():
    rr = Matrix([t, 2*sqrt(2)/3*t**R(3, 2), t**2/2])
    tp = symbols('tp', positive=True)
    sp2 = simplify(rr.subs(t, tp).diff(tp).dot(rr.subs(t, tp).diff(tp)))
    assert simplify(sp2 - (1 + tp)**2) == 0
    assert EQ(integrate((1 + t)**2, (t, 0, 1)), R(7, 3))
    W = line_int([z, x, y], [cos(t), sin(t), t], 0, 2*pi)
    assert EQ(W, 3*pi)
Q(S5, id="q9", no="9", type="스칼라·벡터 선적분", ref="2022 기말 블럭2 2번 · 2024 기말 2(a) 유형", types=["16-scalar", "16-vector"],
  stem="",
  parts=[("a", r"곡선 $\mathbf r(t)=\Big\langle t,\ \dfrac{2\sqrt2}{3}t^{3/2},\ \dfrac{t^2}{2}\Big\rangle\ (0\le t\le1)$ 모양의 철사의 밀도가 $\delta(x,y,z)=1+x$ 일 때 철사의 질량을 구하시오."),
         ("b", r"$\mathbf F(x,y,z)=\langle z,\ x,\ y\rangle$ 가 나선 $\mathbf r(t)=\langle\cos t,\ \sin t,\ t\rangle\ (0\le t\le2\pi)$ 을 따라 입자를 옮길 때 한 일을 구하시오.")],
  answer=[("a", r"$\dfrac73$"), ("b", r"$3\pi$")],
  solution=[("a", [r"$\mathbf r'=\langle1,\ \sqrt2\,t^{1/2},\ t\rangle$, $|\mathbf r'|^2=1+2t+t^2=(1+t)^2$ → $ds=(1+t)\,dt$",
                   r"$m=\displaystyle\int_0^1(1+t)(1+t)\,dt=\Big[\frac{(1+t)^3}{3}\Big]_0^1=\frac{8-1}{3}=\frac73$"]),
            ("b", [r"$\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)=\langle t,\cos t,\sin t\rangle\cdot\langle-\sin t,\cos t,1\rangle=-t\sin t+\cos^2t+\sin t$",
                   r"$\displaystyle\int_0^{2\pi}(-t\sin t)\,dt=\Big[t\cos t-\sin t\Big]_0^{2\pi}=2\pi$, $\displaystyle\int_0^{2\pi}\cos^2t\,dt=\pi$, $\displaystyle\int_0^{2\pi}\sin t\,dt=0$ → $W=3\pi$"])],
  check=_c)


def _c():
    P_, Q_ = -y/(x**2 + y**2) + y, x/(x**2 + y**2) + 2*x
    na = line_num([P_, Q_], [2 + 3*cos(t), 3*sin(t)], 0, 2*pi, (x, y))
    nb = line_num([P_, Q_], [5 + 2*cos(t), 2*sin(t)], 0, 2*pi, (x, y))
    assert abs(na - 11*mp.pi) < 1e-9 and abs(nb - 4*mp.pi) < 1e-9
Q(S5, id="q10", no="10", type="그린 정리와 특이점", ref="2022 기말 블럭1 3번 · 2024 기말 4번 응용", types=["16-singular", "16-green"],
  stem=r"$\mathbf F(x,y)=\Big\langle\dfrac{-y}{x^2+y^2}+y,\ \dfrac{x}{x^2+y^2}+2x\Big\rangle$ 에 대하여 (모두 반시계 방향)",
  parts=[("a", r"원 $(x-2)^2+y^2=9$ 를 따라 $\displaystyle\oint\mathbf F\cdot d\mathbf r$ 를 구하시오."),
         ("b", r"원 $(x-5)^2+y^2=4$ 를 따라 $\displaystyle\oint\mathbf F\cdot d\mathbf r$ 를 구하시오.")],
  answer=[("a", r"$11\pi$"), ("b", r"$4\pi$")],
  solution=[("a", [r"$\mathbf F=\mathbf F_1+\mathbf F_2$, $\mathbf F_1=\dfrac{\langle-y,x\rangle}{x^2+y^2}$ (원점에서만 정의되지 않음, $Q_x=P_y$), $\mathbf F_2=\langle y,2x\rangle$ ($Q_x-P_y=1$)",
                   r"원 $(x-2)^2+y^2=9$ 는 원점을 감싸요 ($2<3$). $\mathbf F_1$: 원점을 감싸는 곡선을 따라 항상 $2\pi$ (작은 원과 사이 영역에 그린 정리)",
                   r"$\mathbf F_2$: 그린 정리로 넓이 $9\pi$ → 합 $2\pi+9\pi=11\pi$"]),
            ("b", [r"원 $(x-5)^2+y^2=4$ 는 원점을 감싸지 않음 → $\mathbf F_1$ 부분은 그린 정리로 $0$",
                   r"$\mathbf F_2$ 부분은 넓이 $4\pi$ → $4\pi$"])],
  check=_c)


SETS.append({"id": "s5", "no": 5, "title": "실전 모의고사 5회", "focus": "종합 심화 · 12–16장 전 범위",
             "lead": "마지막 점검용 심화 회차예요. 12–13장(교선·거리·곡선 길이)부터 정의로 구하는 편도함수, 극좌표 2계 연쇄법칙, 교선의 접선과 곡면 사이 각, 절댓값 함정이 있는 부피, 경계가 바뀌는 삼중적분 순서, 구면좌표 무게중심, 선적분, 특이점이 있는 그린 정리까지 전 범위를 다뤄요.",
             "problems": S5})


def check_all():
    """모든 회차·문항의 check 를 실행. (이름, 통과 여부, 오류) 목록을 돌려줘요."""
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

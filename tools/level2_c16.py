"""2단계 · 표준 추가분 — Ch.16 벡터 미적분: 2-102 ~ 2-120"""
from bank_lib import *


def line_int(F, rr, a, b, vars_=(x, y, z)):
    sub = dict(zip(vars_, rr))
    integrand = sum(Fi.subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


def seg(p0, p1):
    return [a0 + (a1 - a0)*t for a0, a1 in zip(p0, p1)]


# ───────── 16.1 ─────────
def _c():
    f = log(x**2 + y**2)
    g = grad(f, (x, y))
    assert simplify(g[0] - 2*x/(x**2 + y**2)) == 0 and simplify(g.dot(g) - 4/(x**2 + y**2)) == 0
    assert simplify(g.dot(Matrix([-y, x]))) == 0
P(id="2-102", ch=16, sec="16.1", type="16-field", src="과제 16.1 #25 유형",
  q=r"$f(x,y)=\ln(x^2+y^2)$의 기울기 벡터장 $\nabla f$를 구하라. 또 $\nabla f$가 어느 방향을 가리키는지, 크기는 얼마인지 설명하라.",
  hint=r"$\nabla f$를 위치벡터 $\langle x,y\rangle$로 표현해 보세요.",
  ans=r"$\nabla f=\dfrac{2}{x^2+y^2}\langle x,y\rangle$: 원점에서 바깥쪽(반지름 방향), 크기 $\dfrac{2}{\sqrt{x^2+y^2}}$",
  sol=[r"$f_x=\dfrac{2x}{x^2+y^2},\ f_y=\dfrac{2y}{x^2+y^2}$ → $\nabla f=\dfrac{2}{x^2+y^2}\langle x,y\rangle$",
       r"위치벡터의 양수배이므로 원점에서 멀어지는 방향, 등위곡선(원)에 수직",
       r"$|\nabla f|=\dfrac{2\sqrt{x^2+y^2}}{x^2+y^2}=\dfrac{2}{\sqrt{x^2+y^2}}$ (원점에서 멀수록 작아져요)"],
  check=_c)


# ───────── 16.2 ─────────
def _c():
    F = [x + 2*y, x**2]
    tot = line_int(F, seg((0, 0), (1, 2)), 0, 1, (x, y)) + line_int(F, seg((1, 2), (3, 2)), 0, 1, (x, y))
    assert EQ(tot, R(91, 6))
P(id="2-103", ch=16, sec="16.2", type="16-vector", src="과제 16.2 #7 유형",
  q=r"$C$가 $(0,0)$에서 $(1,2)$로, 다시 $(3,2)$로 가는 두 선분일 때 $\displaystyle\int_C(x+2y)\,dx+x^2\,dy$를 계산하라.",
  hint=r"선분마다 매개화: $C_1:\ x=t,\ y=2t$,  $C_2:\ x=1+2t,\ y=2$ ($0\le t\le1$)",
  ans=r"$\dfrac{91}{6}$",
  sol=[r"$C_1$: $dx=dt,\ dy=2dt$ → $\displaystyle\int_0^1\big((t+4t)+t^2\cdot2\big)dt=\frac52+\frac23=\frac{19}{6}$",
       r"$C_2$: $dx=2dt,\ dy=0$ → $\displaystyle\int_0^1(1+2t+4)\cdot2\,dt=10+2=12$",
       r"합: $\dfrac{19}{6}+12=\dfrac{91}{6}$"],
  check=_c)


def _c():
    assert EQ(line_int([y, z, x], [sqrt(t), t, t**2], 1, 4), R(722, 15))
P(id="2-104", ch=16, sec="16.2", type="16-vector", src="과제 16.2 #15 유형",
  q=r"$C:\ x=\sqrt t,\ y=t,\ z=t^2\ (1\le t\le4)$일 때 $\displaystyle\int_C y\,dx+z\,dy+x\,dz$를 계산하라.",
  hint=r"$dx=\dfrac{1}{2\sqrt t}dt,\ dy=dt,\ dz=2t\,dt$",
  ans=r"$\dfrac{722}{15}$",
  sol=[r"$y\,dx+z\,dy+x\,dz=\Big(\dfrac{t}{2\sqrt t}+t^2+\sqrt t\cdot2t\Big)dt=\Big(\dfrac{\sqrt t}{2}+t^2+2t^{3/2}\Big)dt$",
       r"$\displaystyle\int_1^4\frac{\sqrt t}{2}dt=\frac13(8-1)=\frac73$,  $\displaystyle\int_1^4t^2dt=21$,  $\displaystyle\int_1^42t^{3/2}dt=\frac45(32-1)=\frac{124}{5}$",
       r"합: $\dfrac73+21+\dfrac{124}{5}=\dfrac{35+315+372}{15}=\dfrac{722}{15}$"],
  check=_c)


def _c():
    assert EQ(line_int([y**2, x, z], [exp(t), exp(-t), t], 0, 1), R(1, 2) - exp(-1))
P(id="2-105", ch=16, sec="16.2", type="16-vector", src="과제 16.2 #24 유형",
  q=r"$\mathbf F(x,y,z)=\langle y^2,\ x,\ z\rangle$, $\mathbf r(t)=\langle e^{t},\ e^{-t},\ t\rangle\ (0\le t\le1)$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 계산하라.",
  hint=r"$\mathbf F(\mathbf r(t))=\langle e^{-2t},\ e^{t},\ t\rangle$",
  ans=r"$\dfrac12-\dfrac1e$",
  sol=[r"$\mathbf r'(t)=\langle e^t,\ -e^{-t},\ 1\rangle$",
       r"$\mathbf F\cdot\mathbf r'=e^{-2t}e^{t}+e^{t}(-e^{-t})+t=e^{-t}-1+t$",
       r"$\displaystyle\int_0^1(e^{-t}-1+t)\,dt=(1-e^{-1})-1+\frac12=\frac12-\frac1e$"],
  check=_c)


def _c():
    c1 = integrate(t*sqrt(1 + t**2), (t, 0, 2))
    c2 = integrate(x, (x, 0, 2))
    assert EQ(c1, (5*sqrt(5) - 1)/3) and EQ(c1 + c2, (5*sqrt(5) + 5)/3)
P(id="2-106", ch=16, sec="16.2", type="16-scalar", src="복습 16.1–4 기초1 유형",
  q=r"$C$가 포물선 $y=\tfrac12x^2$을 따라 $(0,0)$에서 $(2,2)$까지 간 뒤, 선분을 따라 $(0,2)$까지 가는 곡선일 때 $\displaystyle\int_C x\,ds$를 계산하라.",
  hint=r"$C_1:\ \mathbf r=\langle t,\ \tfrac12t^2\rangle$, $ds=\sqrt{1+t^2}\,dt$. $C_2$는 $y=2$ 위의 선분으로 $ds=|dx|$",
  ans=r"$\dfrac{5\sqrt5+5}{3}$",
  sol=[r"$C_1$: $\displaystyle\int_0^2t\sqrt{1+t^2}\,dt=\Big[\tfrac13(1+t^2)^{3/2}\Big]_0^2=\frac{5\sqrt5-1}{3}$",
       r"$C_2$: $\mathbf r=\langle2-t,\ 2\rangle\ (0\le t\le2)$, $ds=dt$ → $\displaystyle\int_0^2(2-t)\,dt=2$",
       r"합: $\dfrac{5\sqrt5-1}{3}+2=\dfrac{5\sqrt5+5}{3}$ ($ds$는 방향과 상관없이 양수)"],
  check=_c)


def _c():
    rr = Matrix([2*cos(t), 2*sin(t), t])
    sp = simplify(rr.diff(t).norm())
    assert EQ(sp, sqrt(5)) and EQ(integrate(t*sp, (t, 0, 2*pi)), 2*sqrt(5)*pi**2)
P(id="2-107", ch=16, sec="16.2", type="16-scalar", src="복습 16.1–4 기초2 · 2022 기말(블럭2) 2번 유형",
  q=r"나선 $x=2\cos t,\ y=2\sin t,\ z=t\ (0\le t\le2\pi)$ 모양의 철사의 밀도가 $\delta(x,y,z)=z$일 때 철사의 질량을 구하라.",
  hint=r"질량 $m=\displaystyle\int_C\delta\,ds$, $|\mathbf r'(t)|=\sqrt{4\sin^2t+4\cos^2t+1}$",
  ans=r"$2\sqrt5\,\pi^2$",
  sol=[r"$|\mathbf r'(t)|=\sqrt{4+1}=\sqrt5$",
       r"$m=\displaystyle\int_0^{2\pi}t\cdot\sqrt5\,dt=\sqrt5\cdot\frac{(2\pi)^2}{2}=2\sqrt5\,\pi^2$"],
  check=_c)


# ───────── 16.3 ─────────
def _c():
    Pp, Q = 2*x*exp(y) + y*cos(x), x**2*exp(y) + sin(x)
    f = x**2*exp(y) + y*sin(x)
    assert simplify(diff(Pp, y) - diff(Q, x)) == 0 and simplify(diff(f, x) - Pp) == 0 and simplify(diff(f, y) - Q) == 0
P(id="2-108", ch=16, sec="16.3", type="16-conserv", src="과제 16.3 #7 유형",
  q=r"$\mathbf F(x,y)=\big(2xe^{y}+y\cos x\big)\mathbf i+\big(x^2e^{y}+\sin x\big)\mathbf j$가 보존장인지 판정하고 퍼텐셜 함수를 구하라.",
  hint=r"$P_y=2xe^y+\cos x$, $Q_x=2xe^y+\cos x$",
  ans=r"보존장,  $f(x,y)=x^2e^{y}+y\sin x+K$",
  sol=[r"$P_y=2xe^{y}+\cos x=Q_x$, 정의역 $\mathbb R^2$ → 보존장",
       r"$f=\displaystyle\int(2xe^y+y\cos x)\,dx=x^2e^y+y\sin x+g(y)$",
       r"$f_y=x^2e^y+\sin x+g'(y)=Q \Rightarrow g'(y)=0$",
       r"$f=x^2e^y+y\sin x+K$"],
  check=_c)


def _c():
    F = [2*x*y + exp(x), x**2 + cos(y)]
    f = x**2*y + exp(x) + sin(y)
    assert all(simplify(diff(f, v) - Fi) == 0 for v, Fi in zip((x, y), F))
    assert EQ(line_int(F, [t, t*(2 - t)], 0, 2, (x, y)), exp(2) - 1)
    assert EQ(integrate(exp(x), (x, 0, 2)), exp(2) - 1)
P(id="2-109", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #14 유형",
  q=r"$\mathbf F(x,y)=\langle 2xy+e^{x},\ x^2+\cos y\rangle$, $C:\ x=t,\ y=t(2-t),\ 0\le t\le2$일 때<br>(a) 퍼텐셜 함수 $f$를 구하라.  (b) 선적분의 기본정리로 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.  (c) $C$를 같은 시작·끝점의 선분으로 바꿔 다시 계산하라.",
  hint=r"시작점 $(0,0)$, 끝점 $(2,0)$. (c)의 선분은 $x$축 위라 $y=0,\ dy=0$",
  ans=r"(a) $f=x^2y+e^{x}+\sin y$  (b) $e^2-1$  (c) $e^2-1$",
  sol=[r"(a) $f=\displaystyle\int(2xy+e^x)dx=x^2y+e^x+g(y)$, $f_y=x^2+g'(y)=x^2+\cos y \Rightarrow g=\sin y$",
       r"(b) $f(2,0)-f(0,0)=(0+e^2+0)-(0+1+0)=e^2-1$",
       r"(c) 선분 $y=0,\ 0\le x\le2$: $\displaystyle\int_0^2e^x\,dx=e^2-1$ ✓ (경로와 무관)"],
  check=_c)


def _c():
    f = x**2*y*z + z**2
    rr = [t**3, exp(t - 1), t**2 + t]
    start = [c_.subs(t, 0) for c_ in rr]; end = [c_.subs(t, 1) for c_ in rr]
    assert end == [1, 1, 2] and start[0] == 0 and start[2] == 0
    val = f.subs(dict(zip((x, y, z), end))) - f.subs(dict(zip((x, y, z), start)))
    assert EQ(val, 6)
    assert abs(float(N(line_int([diff(f, v) for v in (x, y, z)], rr, 0, 1))) - 6) < 1e-9
P(id="2-110", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #16 유형",
  q=r"$f(x,y,z)=x^2yz+z^2$이고 $C:\ x=t^3,\ y=e^{t-1},\ z=t^2+t\ (0\le t\le1)$일 때 $\displaystyle\int_C\nabla f\cdot d\mathbf r$를 구하라.",
  hint=r"$\nabla f$의 선적분은 끝점에서의 $f$ 값 차이예요. 곡선 모양은 필요 없어요.",
  ans=r"$6$",
  sol=[r"시작점 $\mathbf r(0)=(0,\ e^{-1},\ 0)$, 끝점 $\mathbf r(1)=(1,1,2)$",
       r"$f(1,1,2)=1\cdot1\cdot2+4=6$,  $f(0,e^{-1},0)=0$",
       r"$\displaystyle\int_C\nabla f\cdot d\mathbf r=6-0=6$"],
  check=_c)


def _c():
    f = x**2*sin(y) - y**3
    assert simplify(diff(f, x) - 2*x*sin(y)) == 0 and simplify(diff(f, y) - (x**2*cos(y) - 3*y**2)) == 0
    assert EQ(f.subs({x: 2, y: pi/2}) - f.subs({x: -1, y: 0}), 4 - pi**3/8)
P(id="2-111", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #25 유형",
  q=r"선적분 $\displaystyle\int_C2x\sin y\,dx+(x^2\cos y-3y^2)\,dy$가 경로와 무관함을 보이고, $C$가 $(-1,0)$에서 $\left(2,\tfrac\pi2\right)$까지 가는 임의의 곡선일 때 값을 구하라.",
  hint=r"$P_y=2x\cos y=Q_x$. 퍼텐셜 $f=x^2\sin y-y^3$",
  ans=r"$4-\dfrac{\pi^3}{8}$",
  sol=[r"$P_y=2x\cos y=Q_x$ → 보존장, 경로와 무관",
       r"$f=x^2\sin y+g(y)$, $f_y=x^2\cos y+g'(y)=x^2\cos y-3y^2 \Rightarrow g=-y^3$",
       r"$f\big(2,\tfrac\pi2\big)-f(-1,0)=\Big(4-\dfrac{\pi^3}{8}\Big)-0=4-\dfrac{\pi^3}{8}$"],
  check=_c)


def _c():
    Pp, Q = x**2 + y, y**2 - x
    assert diff(Pp, y) == 1 and diff(Q, x) == -1
    assert EQ(line_int([Pp, Q], [cos(t), sin(t)], 0, 2*pi, (x, y)), -2*pi)
P(id="2-112", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 (보존장 판정) 유형",
  q=r"$\mathbf F(x,y)=\langle x^2+y,\ y^2-x\rangle$가 보존장이 아님을 보이고, 단위원을 반시계 방향으로 한 바퀴 도는 $C$에 대해 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"보존장이면 닫힌 곡선의 선적분이 $0$이어야 해요.",
  ans=r"$P_y=1\ne-1=Q_x$ → 보존장 아님,  $\displaystyle\oint_C\mathbf F\cdot d\mathbf r=-2\pi$",
  sol=[r"$P_y=1,\ Q_x=-1$ → 다르므로 보존장이 아니에요.",
       r"$x=\cos t,\ y=\sin t$: $\mathbf F\cdot\mathbf r'=(\cos^2t+\sin t)(-\sin t)+(\sin^2t-\cos t)\cos t$",
       r"$=-\cos^2t\sin t+\sin^2t\cos t-1$ → $\displaystyle\int_0^{2\pi}=0+0-2\pi=-2\pi$",
       r"$0$이 아니므로 다시 한 번 보존장이 아님을 확인 (그린 정리: $\iint(-1-1)dA=-2\pi$)"],
  check=_c)


# ───────── 16.4 ─────────
def _c():
    Pp, Q = x**2*y, x*y**2
    green = integrate(integrate(diff(Q, x) - diff(Pp, y), (y, 0, x/2)), (x, 0, 2))
    direct = (line_int([Pp, Q], seg((0, 0), (2, 0)), 0, 1, (x, y)) + line_int([Pp, Q], seg((2, 0), (2, 1)), 0, 1, (x, y))
              + line_int([Pp, Q], seg((2, 1), (0, 0)), 0, 1, (x, y)))
    assert EQ(green, R(-11, 6)) and EQ(direct, R(-11, 6))
P(id="2-113", ch=16, sec="16.4", type="16-green", src="과제 16.4 #3 유형",
  q=r"$C$가 꼭짓점 $(0,0),\ (2,0),\ (2,1)$인 삼각형(반시계 방향)일 때 $\displaystyle\oint_C x^2y\,dx+xy^2\,dy$를 (a) 직접 (b) 그린 정리로 계산하라.",
  hint=r"(b) $Q_x-P_y=y^2-x^2$, 영역 $0\le x\le2,\ 0\le y\le\tfrac x2$",
  ans=r"$-\dfrac{11}{6}$ (두 방법 모두)",
  sol=[r"(a) $(0,0)\to(2,0)$: $y=0$ → $0$.  $(2,0)\to(2,1)$: $dx=0$, $\displaystyle\int_0^12y^2dy=\frac23$",
       r"$(2,1)\to(0,0)$: $x=2-2t,\ y=1-t$: $\displaystyle\int_0^1\big(-8(1-t)^3-2(1-t)^3\big)dt=-\frac{10}{4}=-\frac52$",
       r"합: $0+\dfrac23-\dfrac52=-\dfrac{11}{6}$",
       r"(b) $\displaystyle\int_0^2\!\!\int_0^{x/2}(y^2-x^2)\,dy\,dx=\int_0^2\Big(\frac{x^3}{24}-\frac{x^3}{2}\Big)dx=-\frac{11}{24}\cdot4=-\frac{11}{6}$ ✓"],
  check=_c)


def _c():
    Pp, Q = x**2 + y**2, x**2 - y**2
    assert EQ(integrate(integrate(diff(Q, x) - diff(Pp, y), (y, 0, x/2)), (x, 0, 2)), 2)
P(id="2-114", ch=16, sec="16.4", type="16-green", src="과제 16.4 #8 유형",
  q=r"$C$가 꼭짓점 $(0,0),\ (2,0),\ (2,1)$인 삼각형(반시계 방향)일 때 그린 정리로 $\displaystyle\oint_C(x^2+y^2)\,dx+(x^2-y^2)\,dy$를 계산하라.",
  hint=r"$Q_x-P_y=2x-2y$",
  ans=r"$2$",
  sol=[r"$Q_x-P_y=2x-2y$, 영역 $0\le x\le2,\ 0\le y\le\tfrac x2$",
       r"$\displaystyle\int_0^2\!\!\int_0^{x/2}(2x-2y)\,dy\,dx=\int_0^2\Big(x^2-\frac{x^2}{4}\Big)dx=\frac34\cdot\frac83=2$"],
  check=_c)


def _c():
    Pp, Q = 2*y - y**3, x**3 + exp(y**2)
    integrand = simplify(diff(Q, x) - diff(Pp, y))
    assert simplify(integrand - (3*x**2 + 3*y**2 - 2)) == 0
    assert EQ(integrate(integrate((3*r**2 - 2)*r, (r, 1, 2)), (th, 0, 2*pi)), 33*pi/2)
P(id="2-115", ch=16, sec="16.4", type="16-green", src="과제 16.4 #12 유형",
  q=r"$C$가 두 원 $x^2+y^2=1$과 $x^2+y^2=4$ 사이 영역의 경계(양의 방향)일 때 $\displaystyle\oint_C(2y-y^3)\,dx+\big(x^3+e^{y^2}\big)\,dy$를 계산하라.",
  hint=r"양의 방향: 바깥 원은 반시계, 안쪽 원은 시계 방향 (영역이 항상 왼쪽). $Q_x-P_y=3x^2+3y^2-2$",
  ans=r"$\dfrac{33\pi}{2}$",
  sol=[r"$Q_x-P_y=3x^2-(2-3y^2)=3r^2-2$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_1^2(3r^2-2)r\,dr\,d\theta=2\pi\Big[\tfrac34r^4-r^2\Big]_1^2=2\pi\Big(8+\frac14\Big)=\frac{33\pi}{2}$"],
  check=_c)


def _c():
    Pp, Q = 2*y + sqrt(1 + x**5), 5*x - exp(y**2)
    assert simplify(diff(Q, x) - diff(Pp, y)) == 3
P(id="2-116", ch=16, sec="16.4", type="16-green", src="복습 16.1–4 기초5 유형",
  q=r"$C$가 원 $x^2+y^2=4$ (반시계 방향)일 때 $\displaystyle\oint_C\big(2y+\sqrt{1+x^5}\big)\,dx+\big(5x-e^{y^2}\big)\,dy$를 계산하라.",
  hint=r"직접 적분은 불가능해요. 그린 정리로 넘기면 상수만 남아요.",
  ans=r"$12\pi$",
  sol=[r"$Q_x-P_y=5-2=3$ ($\sqrt{1+x^5}$은 $y$와, $e^{y^2}$은 $x$와 무관)",
       r"$\displaystyle\iint_D3\,dA=3\cdot4\pi=12\pi$"],
  check=_c)


def _c():
    A = -line_int([y, sympify(0)], [t - sin(t), 1 - cos(t)], 2*pi, 0, (x, y))
    assert EQ(A, 3*pi)
P(id="2-117", ch=16, sec="16.4", type="16-greenarea", src="강의 16.4 (넓이 공식) 유형",
  q=r"사이클로이드 $x=t-\sin t,\ y=1-\cos t\ (0\le t\le2\pi)$의 한 아치와 $x$축으로 둘러싸인 영역의 넓이를 넓이 공식 $A=-\displaystyle\oint_C y\,dx$로 구하라.",
  hint=r"경계: $x$축 선분 $(0,0)\to(2\pi,0)$ ($y=0$이라 기여 $0$) + 아치를 거꾸로 ($t$: $2\pi\to0$)",
  ans=r"$3\pi$",
  sol=[r"반시계 방향 경계 = $x$축 선분(오른쪽으로) + 아치(왼쪽으로, $t$가 $2\pi\to0$)",
       r"선분 위에서 $y=0$ → 기여 $0$",
       r"아치: $A=-\displaystyle\int_{2\pi}^{0}(1-\cos t)(1-\cos t)\,dt=\int_0^{2\pi}(1-2\cos t+\cos^2t)\,dt$",
       r"$=2\pi-0+\pi=3\pi$"],
  check=_c)


def _c():
    X, Y = 2*cos(t) - cos(2*t), 2*sin(t) - sin(2*t)
    assert simplify(X*diff(Y, t) - Y*diff(X, t) - (6 - 6*cos(t))) == 0
    A = R(1, 2)*line_int([-y, x], [X, Y], 0, 2*pi, (x, y))
    assert EQ(A, 6*pi)
P(id="2-118", ch=16, sec="16.4", type="16-greenarea", src="강의 16.4 (넓이 공식) 유형",
  q=r"곡선 $x=2\cos t-\cos2t,\ y=2\sin t-\sin2t\ (0\le t\le2\pi)$로 둘러싸인 영역(심장형)의 넓이를 그린 정리의 넓이 공식으로 구하라.",
  hint=r"$A=\dfrac12\displaystyle\oint x\,dy-y\,dx$. 정리하면 $\cos t\cos2t+\sin t\sin2t=\cos(2t-t)=\cos t$가 나와요.",
  ans=r"$6\pi$",
  sol=[r"$x'=-2\sin t+2\sin2t,\ y'=2\cos t-2\cos2t$",
       r"$xy'-yx'=4\cos^2t+4\sin^2t+2\cos^22t+2\sin^22t-6(\cos t\cos2t+\sin t\sin2t)=6-6\cos t$",
       r"$A=\dfrac12\displaystyle\int_0^{2\pi}(6-6\cos t)\,dt=\frac12\cdot12\pi=6\pi$"],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2), x/(x**2 + y**2)]
    sq = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    tot = sum(line_int(F, seg(a, b), 0, 1, (x, y)) for a, b in zip(sq, sq[1:] + sq[:1]))
    assert EQ(tot, 2*pi)
P(id="2-119", ch=16, sec="16.4", type="16-singular", src="강의 16.4 ex5 유형",
  q=r"$C$가 꼭짓점 $(\pm1,\pm1)$인 정사각형(반시계 방향)일 때 $\displaystyle\oint_C\frac{-y\,dx+x\,dy}{x^2+y^2}$를 구하라.",
  hint=r"정사각형 안에 작은 원 $C_a$를 그리고, 사이 영역에 그린 정리를 쓰세요 (원점 밖에서 $Q_x=P_y$).",
  ans=r"$2\pi$",
  sol=[r"원점 밖에서 $Q_x-P_y=0$. 정사각형 안에 반지름 $a$인 원 $C_a$ (반시계)를 잡아요.",
       r"사이 영역 $D$에 그린 정리: $\displaystyle\oint_C-\oint_{C_a}=\iint_D0\,dA=0$",
       r"$\displaystyle\oint_{C_a}=\int_0^{2\pi}\frac{a^2\sin^2t+a^2\cos^2t}{a^2}dt=2\pi$ → $\displaystyle\oint_C=2\pi$"],
  check=_c)


def _c():
    F = [x/(x**2 + y**2), y/(x**2 + y**2)]
    f = log(x**2 + y**2)/2
    assert simplify(diff(f, x) - F[0]) == 0 and simplify(diff(f, y) - F[1]) == 0
    assert EQ(line_int(F, [2*cos(t), 2*sin(t)], 0, 2*pi, (x, y)), 0)
P(id="2-120", ch=16, sec="16.4", type="16-singular", src="강의 16.3 · 16.4 (원점에서 정의되지 않는 보존장) 유형",
  q=r"$\mathbf F(x,y)=\dfrac{x\,\mathbf i+y\,\mathbf j}{x^2+y^2}$에 대해, 원점을 감싸는 원 $x^2+y^2=4$ (반시계)에서 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라. $\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$의 경우($2\pi$)와 무엇이 다른가?",
  hint=r"$\mathbf F=\nabla\Big(\tfrac12\ln(x^2+y^2)\Big)$ — 원점만 빼면 평면 전체에서 퍼텐셜이 있어요.",
  ans=r"$0$ (원점을 뺀 평면 전체에서 퍼텐셜 $\tfrac12\ln(x^2+y^2)$이 존재)",
  sol=[r"$f=\tfrac12\ln(x^2+y^2)$이면 $\nabla f=\dfrac{\langle x,y\rangle}{x^2+y^2}=\mathbf F$ ($(x,y)\ne(0,0)$)",
       r"닫힌 곡선이 원점을 감싸도 $f$가 곡선 위 전체에서 정의되므로 $\displaystyle\oint_C\nabla f\cdot d\mathbf r=0$",
       r"반면 $\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$의 '퍼텐셜' $\theta$는 한 바퀴 돌면 $2\pi$만큼 늘어나 하나의 함수로 정의되지 않아요 → $2\pi$"],
  check=_c)

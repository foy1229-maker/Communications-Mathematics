"""4단계 · 심화 추가분 — Ch.15 중적분: 4-72 ~ 4-101, 변수변환 4-124 ~ 4-126"""
from bank_lib import *
import mpmath as mp


def q2(fn, xa, xb, ya, yb, xpts=None):
    """∫_{xa}^{xb} ∫_{ya(x)}^{yb(x)} fn(x,y) dy dx (mpmath 수치적분)"""
    outer = xpts if xpts else [xa, xb]
    return mp.quad(lambda X: mp.quad(lambda Y: fn(X, Y), [ya(X), yb(X)]), outer)


# ───────── 15.1 ─────────
def _c():
    g = (x - y)/(x + y)**3
    xp, yp = symbols('xp yp', positive=True)
    inner_y = simplify(integrate(g.subs({x: xp, y: yp}), (yp, 0, 1)))
    assert simplify(inner_y - 1/(xp + 1)**2) == 0
    assert EQ(integrate(inner_y, (xp, 0, 1)), R(1, 2))
    inner_x = simplify(integrate(g.subs({x: xp, y: yp}), (xp, 0, 1)))
    assert simplify(inner_x + 1/(yp + 1)**2) == 0
    assert EQ(integrate(inner_x, (yp, 0, 1)), R(-1, 2))
P(id="4-72", ch=15, sec="15.1", type="15-rect", src="교재 15.1 심화형 (푸비니 정리의 가정)",
  q=r"(a) $\displaystyle\int_0^1\!\!\int_0^1\frac{x-y}{(x+y)^3}\,dy\,dx$와 $\displaystyle\int_0^1\!\!\int_0^1\frac{x-y}{(x+y)^3}\,dx\,dy$를 각각 계산하라.<br>(b) 두 값이 다른 것이 푸비니 정리와 모순되지 않는 이유를 설명하라.",
  hint=r"$\dfrac{x-y}{(x+y)^3}=\dfrac{2x-(x+y)}{(x+y)^3}=\dfrac{2x}{(x+y)^3}-\dfrac{1}{(x+y)^2}$. 둘째 적분은 $x$와 $y$를 바꾼 것이고 피적분함수의 부호가 바뀌어요.",
  ans=r"(a) $\dfrac12$, $-\dfrac12$  (b) 피적분함수가 원점 근처에서 유계가 아니어서(연속이 아님) 푸비니 정리의 가정이 깨짐",
  sol=[r"$y$에 대한 부정적분: $-\dfrac{x}{(x+y)^2}+\dfrac{1}{x+y}$",
       r"$\displaystyle\int_0^1\frac{x-y}{(x+y)^3}dy=\Big(-\frac{x}{(x+1)^2}+\frac{1}{x+1}\Big)-\Big(-\frac1x+\frac1x\Big)=\frac{1}{(x+1)^2}$",
       r"$\displaystyle\int_0^1\frac{dx}{(1+x)^2}=\frac12$",
       r"순서를 바꾸면 $x\leftrightarrow y$ 교환 → 피적분함수가 $-1$배 → 같은 계산으로 $-\dfrac12$",
       r"(b) 푸비니 정리는 $f$가 직사각형에서 연속(유계·적분가능)일 때 성립. $y=0$을 따라 $f=\tfrac{1}{x^2}\to\infty$처럼 원점 근처에서 유계가 아니므로 적용할 수 없어요."],
  check=_c)


def _c():
    I1 = integrate(x*sin(x*y), (y, 0, 1), (x, 0, pi))
    I2 = integrate(y*sin(x*y), (x, 0, pi), (y, 0, 1))
    assert EQ(I1, pi) and EQ(I2, 1)
    assert EQ((I1 + I2)/(pi*1), (pi + 1)/pi)
P(id="4-73", ch=15, sec="15.1", type="15-rect", src="교재 15.1 심화형 (적분 순서 선택 · 평균값)",
  q=r"$R=[0,\pi]\times[0,1]$ ($0\le x\le\pi,\ 0\le y\le1$)일 때<br>(a) $\displaystyle\iint_R x\sin(xy)\,dA$  (b) $\displaystyle\iint_R y\sin(xy)\,dA$를 계산하고, (c) $R$에서 $f(x,y)=(x+y)\sin(xy)$의 평균값을 구하라.",
  hint=r"(a)는 $y$로 먼저 적분하면 $\int x\sin(xy)\,dy=-\cos(xy)$로 $x$가 사라지고, (b)는 $x$로 먼저 적분하는 것이 같은 이유로 쉬워요. 평균값 $=\dfrac{1}{\text{넓이}}\iint_R f\,dA$.",
  ans=r"(a) $\pi$  (b) $1$  (c) $\dfrac{\pi+1}{\pi}$",
  sol=[r"(a) $\displaystyle\int_0^1x\sin(xy)\,dy=\Big[-\cos(xy)\Big]_0^1=1-\cos x$ → $\displaystyle\int_0^\pi(1-\cos x)\,dx=\pi$",
       r"(b) $\displaystyle\int_0^\pi y\sin(xy)\,dx=1-\cos(\pi y)$ → $\displaystyle\int_0^1(1-\cos\pi y)\,dy=1-0=1$",
       r"(c) 넓이 $\pi$ → 평균값 $\dfrac{\pi+1}{\pi}$",
       r"반대 순서로 하면 부분적분이 필요하고 계산이 길어져요 — 순서 선택이 핵심!"],
  check=_c)


# ───────── 15.2 ─────────
def _c():
    I = integrate(2*(1 - y)*cos((1 - y)**2), (y, 0, 1))
    assert EQ(I, sin(1))
    num = (mp.quad(lambda X: mp.quad(lambda Y: mp.cos((1 - Y)**2), [0, X]), [0, 1])
           + mp.quad(lambda X: mp.quad(lambda Y: mp.cos((1 - Y)**2), [0, 2 - X]), [1, 2]))
    assert abs(num - mp.sin(1)) < 1e-10
P(id="4-74", ch=15, sec="15.2", type="15-order", src="2022 중간 블럭1 2(a) 유형",
  q=r"적분 영역을 그리고, 적분 순서를 바꾸어 계산하라. $$\int_0^1\!\!\int_0^{x}\cos\big((1-y)^2\big)\,dy\,dx+\int_1^2\!\!\int_0^{2-x}\cos\big((1-y)^2\big)\,dy\,dx$$",
  hint=r"두 영역을 합치면 꼭짓점이 $(0,0),\ (2,0),\ (1,1)$인 삼각형. $y$를 바깥으로 하면 $y\le x\le2-y$, 길이 $2-2y$가 곱해져 치환이 돼요.",
  ans=r"$\sin1$",
  sol=[r"영역: $0\le x\le1$에서 $0\le y\le x$, $1\le x\le2$에서 $0\le y\le2-x$ → 삼각형 $(0,0),(2,0),(1,1)$",
       r"$0\le y\le1,\ y\le x\le2-y$ → $\displaystyle\int_0^1\!\!\int_y^{2-y}\cos\big((1-y)^2\big)\,dx\,dy=\int_0^12(1-y)\cos\big((1-y)^2\big)\,dy$",
       r"$u=(1-y)^2$, $du=-2(1-y)\,dy$: $\displaystyle\int_1^0\cos u\,(-du)=\int_0^1\cos u\,du=\sin1$"],
  check=_c)


def _c():
    assert EQ(2*integrate(x*exp(x**2), (x, 0, 1)), E - 1)
    num = mp.quad(lambda X: mp.quad(lambda Y: mp.e**max(X*X, Y*Y), [0, X, 1]), [0, 1])
    assert abs(num - (mp.e - 1)) < 1e-9
P(id="4-75", ch=15, sec="15.2", type="15-general", src="교재 15.2 심화형 (max 함수 · 영역 분할)",
  q=r"$\displaystyle\int_0^1\!\!\int_0^1e^{\max\{x^2,\ y^2\}}\,dy\,dx$를 계산하라.",
  hint=r"정사각형을 대각선 $y=x$로 나누면 아래쪽 삼각형에서는 $\max=x^2$, 위쪽에서는 $\max=y^2$. 대칭성으로 두 부분의 값은 같아요.",
  ans=r"$e-1$",
  sol=[r"$D_1=\{0\le y\le x\le1\}$: $\max\{x^2,y^2\}=x^2$,  $D_2=\{0\le x\le y\le1\}$: $\max=y^2$",
       r"$x\leftrightarrow y$ 대칭이므로 $\displaystyle\iint_{D_2}e^{y^2}dA=\iint_{D_1}e^{x^2}dA$",
       r"$\displaystyle 2\int_0^1\!\!\int_0^{x}e^{x^2}\,dy\,dx=2\int_0^1xe^{x^2}\,dx=\Big[e^{x^2}\Big]_0^1=e-1$"],
  check=_c)


def _c():
    V8 = integrate(sqrt(1 - x**2), (y, 0, sqrt(1 - x**2)), (x, 0, 1))
    assert EQ(V8, R(2, 3)) and EQ(8*V8, R(16, 3))
P(id="4-76", ch=15, sec="15.2", type="15-general", src="교재 15.2 심화형 (두 원기둥의 공통부분)",
  q=r"두 원기둥 $x^2+y^2=1$과 $x^2+z^2=1$의 공통 내부의 부피를 구하라.",
  hint=r"제1팔분공간 부분을 구해 $8$배. 그 부분은 사분원판 $x^2+y^2\le1\ (x,y\ge0)$ 위, 높이 $z=\sqrt{1-x^2}$ 아래 — $x$를 바깥으로 하면 근호가 사라져요.",
  ans=r"$\dfrac{16}{3}$",
  sol=[r"제1팔분공간: $0\le z\le\sqrt{1-x^2}$, 밑면 $D=\{0\le x\le1,\ 0\le y\le\sqrt{1-x^2}\}$",
       r"$\displaystyle\int_0^1\!\!\int_0^{\sqrt{1-x^2}}\sqrt{1-x^2}\,dy\,dx=\int_0^1(1-x^2)\,dx=\frac23$",
       r"전체 부피 $=8\cdot\dfrac23=\dfrac{16}{3}$ (극좌표로 하면 오히려 복잡 — 순서 선택이 핵심)"],
  check=_c)


def _c():
    p1 = integrate(R(2, 3)*abs_(x)**3, (x, -1, 1))
    tq = symbols('tq', real=True)
    p2 = R(4, 3)*integrate(4*cos(tq)**4, (tq, 0, pi/4))
    assert EQ(p1, R(1, 3)) and EQ(p2, pi/2 + R(4, 3))
    num = mp.quad(lambda X: mp.quad(lambda Y: mp.sqrt(abs(Y - X*X)), [0, X*X, 2]), [-1, 0, 1])
    assert abs(num - (mp.pi/2 + mp.mpf(5)/3)) < 1e-8


def abs_(e):
    from sympy import Abs
    return Abs(e)


P(id="4-77", ch=15, sec="15.2", type="15-general", src="교재 15.2 심화형 (절댓값 · 영역 분할)",
  q=r"$R=[-1,1]\times[0,2]$일 때 $\displaystyle\iint_R\sqrt{|y-x^2|}\,dA$를 계산하라.",
  hint=r"포물선 $y=x^2$으로 $R$을 나누어요. 아래쪽은 $\sqrt{x^2-y}$, 위쪽은 $\sqrt{y-x^2}$. $(x^2)^{3/2}=|x|^3$임에 주의하고, $\int(2-x^2)^{3/2}dx$는 $x=\sqrt2\sin t$로 치환.",
  ans=r"$\dfrac\pi2+\dfrac53$",
  sol=[r"아래 ($0\le y\le x^2$): $\displaystyle\int_0^{x^2}\sqrt{x^2-y}\,dy=\frac23(x^2)^{3/2}=\frac23|x|^3$ → $\displaystyle\int_{-1}^1\frac23|x|^3dx=\frac13$",
       r"위 ($x^2\le y\le2$): $\displaystyle\int_{x^2}^2\sqrt{y-x^2}\,dy=\frac23(2-x^2)^{3/2}$ → $\displaystyle\frac43\int_0^1(2-x^2)^{3/2}dx$",
       r"$x=\sqrt2\sin t$: $\displaystyle\int_0^1(2-x^2)^{3/2}dx=\int_0^{\pi/4}4\cos^4t\,dt=4\Big(\frac{3\pi}{32}+\frac14\Big)=\frac{3\pi}{8}+1$",
       r"위쪽 $=\dfrac43\Big(\dfrac{3\pi}8+1\Big)=\dfrac\pi2+\dfrac43$ → 합 $\dfrac13+\dfrac\pi2+\dfrac43=\dfrac\pi2+\dfrac53$"],
  check=_c)


def _c():
    yp = symbols('yp', positive=True)
    Ia = integrate(integrate(exp(x/yp), (x, 0, yp)), (yp, 0, 1))
    Ib = integrate(integrate(exp(x/yp), (x, 0, yp**2)), (yp, 0, 1))
    assert EQ(Ia, (E - 1)/2) and EQ(Ib, R(1, 2))
    na = mp.quad(lambda X: mp.quad(lambda Y: mp.e**(X/Y), [X, 1]), [0, 1])
    nb = mp.quad(lambda X: mp.quad(lambda Y: mp.e**(X/Y), [mp.sqrt(X), 1]), [0, 1])
    assert abs(na - (mp.e - 1)/2) < 1e-9 and abs(nb - mp.mpf(1)/2) < 1e-9
P(id="4-78", ch=15, sec="15.2", type="15-order", src="교재 15.2 심화형 (순서 변경)",
  q=r"적분 순서를 바꾸어 계산하라.<br>(a) $\displaystyle\int_0^1\!\!\int_x^1e^{x/y}\,dy\,dx$  (b) $\displaystyle\int_0^1\!\!\int_{\sqrt x}^1e^{x/y}\,dy\,dx$",
  hint=r"$e^{x/y}$는 $y$로 적분할 수 없지만 $x$로는 $\int e^{x/y}dx=y\,e^{x/y}$. (a) $x\le y$, (b) $x\le y^2$로 영역을 다시 써요.",
  ans=r"(a) $\dfrac{e-1}{2}$  (b) $\dfrac12$",
  sol=[r"(a) $0\le x\le y\le1$ → $\displaystyle\int_0^1\!\!\int_0^{y}e^{x/y}dx\,dy=\int_0^1y(e-1)\,dy=\frac{e-1}{2}$",
       r"(b) $\sqrt x\le y \iff x\le y^2$ → $\displaystyle\int_0^1\!\!\int_0^{y^2}e^{x/y}dx\,dy=\int_0^1y\big(e^{y}-1\big)dy$",
       r"$\displaystyle\int_0^1ye^y\,dy=\Big[(y-1)e^y\Big]_0^1=1$ → $1-\dfrac12=\dfrac12$"],
  check=_c)


def _c():
    top, bot = 5 - x + 2*y, y - 3
    V = integrate(top - bot, (y, x**2 - 1, 1 - x**2), (x, -1, 1))
    assert EQ(V, R(64, 3))
    assert EQ(integrate(2*(1 - x**2), (x, -1, 1)), R(8, 3))
P(id="4-79", ch=15, sec="15.2", type="15-general", src="교재 15.2 심화형 (대칭성으로 부피)",
  q=r"포물기둥 $y=1-x^2$, $y=x^2-1$과 두 평면 $x-2y+z=5$, $y-z=3$으로 둘러싸인 입체의 부피를 구하라.",
  hint=r"윗면 $z=5-x+2y$, 아랫면 $z=y-3$, 높이 $8-x+y$. 밑면 $D$는 $x\to-x$, $y\to-y$에 대해 대칭이라 $x$, $y$ 항의 적분은 $0$이에요.",
  ans=r"$\dfrac{64}{3}$",
  sol=[r"밑면 $D=\{-1\le x\le1,\ x^2-1\le y\le1-x^2\}$, 높이 $(5-x+2y)-(y-3)=8-x+y>0$",
       r"$D$는 $y$축과 $x$축에 대해 대칭 → $\displaystyle\iint_Dx\,dA=\iint_Dy\,dA=0$",
       r"$V=8\cdot\text{넓이}(D)=8\displaystyle\int_{-1}^{1}2(1-x^2)\,dx=8\cdot\frac83=\frac{64}{3}$"],
  check=_c)


# ───────── 15.3 ─────────
def _c():
    I = integrate(1/r**2, (r, 1, 1/cos(th)), (th, 0, pi/3)) + integrate(1/r**2, (r, 1, 2), (th, pi/3, pi/2))
    assert EQ(I, 5*pi/12 - sqrt(3)/2)
    f = lambda X, Y: (X*X + Y*Y)**(-1.5)
    num = (q2(f, 0, 1, lambda Y: mp.sqrt(1 - Y*Y), lambda Y: 1)
           + q2(f, 1, mp.sqrt(3), lambda Y: 0, lambda Y: 1)
           + q2(f, mp.sqrt(3), 2, lambda Y: 0, lambda Y: mp.sqrt(4 - Y*Y)))
    assert abs(num - (5*mp.pi/12 - mp.sqrt(3)/2)) < 1e-8
P(id="4-80", ch=15, sec="15.3", type="15-polar", src="2025 중간 2(b) 유형",
  q=r"다음 합을 극좌표 적분으로 바꾸고, $f(x,y)=\dfrac{1}{(x^2+y^2)^{3/2}}$일 때 값을 구하라. $$\int_0^1\!\!\int_{\sqrt{1-y^2}}^{1}f\,dx\,dy+\int_1^{\sqrt3}\!\!\int_0^{1}f\,dx\,dy+\int_{\sqrt3}^{2}\!\!\int_0^{\sqrt{4-y^2}}f\,dx\,dy$$",
  hint=r"영역: 제1사분면에서 원 $r=1$ 바깥, 원 $r=2$ 안, 직선 $x=1$ 왼쪽. 직선 $x=1$은 $r=\sec\theta$이고 원 $r=2$와 $\theta=\tfrac\pi3$에서 만나요.",
  ans=r"$\displaystyle\int_0^{\pi/3}\!\!\int_1^{\sec\theta}f\,r\,dr\,d\theta+\int_{\pi/3}^{\pi/2}\!\!\int_1^{2}f\,r\,dr\,d\theta=\frac{5\pi}{12}-\frac{\sqrt3}{2}$",
  sol=[r"세 조각을 합치면 $R=\{x\ge0,\ y\ge0,\ 1\le x^2+y^2\le4,\ x\le1\}$",
       r"$x=1 \iff r=\sec\theta$, $\sec\theta=2 \iff \theta=\tfrac\pi3$ → $0\le\theta\le\tfrac\pi3$: $1\le r\le\sec\theta$, $\tfrac\pi3\le\theta\le\tfrac\pi2$: $1\le r\le2$",
       r"$f\,r=\dfrac{r}{r^3}=\dfrac1{r^2}$, $\displaystyle\int\frac{dr}{r^2}=-\frac1r$",
       r"$\displaystyle\int_0^{\pi/3}(1-\cos\theta)\,d\theta+\int_{\pi/3}^{\pi/2}\Big(1-\frac12\Big)d\theta=\Big(\frac\pi3-\frac{\sqrt3}{2}\Big)+\frac{\pi}{12}=\frac{5\pi}{12}-\frac{\sqrt3}2$"],
  check=_c)


def _c():
    A = integrate(r, (r, 0, 1 + cos(th)), (th, 0, 2*pi))
    Mx = integrate(r*cos(th)*r, (r, 0, 1 + cos(th)), (th, 0, 2*pi))
    My = integrate(r*sin(th)*r, (r, 0, 1 + cos(th)), (th, 0, 2*pi))
    assert EQ(A, 3*pi/2) and EQ(Mx, 5*pi/4) and EQ(My, 0) and EQ(Mx/A, R(5, 6))
P(id="4-81", ch=15, sec="15.3", type="15-mass", src="2025 중간 1번 · 7번 영역 응용 (심장형 무게중심)",
  q=r"심장형 $r=1+\cos\theta$로 둘러싸인 밀도가 일정한 얇은 판의 질량중심(무게중심)을 구하라.",
  hint=r"$\bar x=\dfrac{\iint x\,dA}{\iint dA}$, $x=r\cos\theta$. $\displaystyle\int_0^{2\pi}\cos^2\theta\,d\theta=\pi$, $\displaystyle\int_0^{2\pi}\cos^4\theta\,d\theta=\frac{3\pi}{4}$, 홀수 거듭제곱은 $0$.",
  ans=r"$\Big(\dfrac56,\ 0\Big)$",
  sol=[r"넓이 $A=\dfrac12\displaystyle\int_0^{2\pi}(1+\cos\theta)^2d\theta=\frac12\Big(2\pi+\pi\Big)=\frac{3\pi}{2}$",
       r"$\displaystyle\iint x\,dA=\int_0^{2\pi}\!\!\int_0^{1+\cos\theta}r^2\cos\theta\,dr\,d\theta=\frac13\int_0^{2\pi}\cos\theta(1+\cos\theta)^3d\theta$",
       r"$=\dfrac13\displaystyle\int_0^{2\pi}\big(\cos\theta+3\cos^2\theta+3\cos^3\theta+\cos^4\theta\big)d\theta=\frac13\Big(3\pi+\frac{3\pi}4\Big)=\frac{5\pi}{4}$",
       r"$\bar x=\dfrac{5\pi/4}{3\pi/2}=\dfrac56$, $x$축 대칭이므로 $\bar y=0$"],
  check=_c)


def _c():
    I1 = integrate(r**3, (r, 0, 2), (th, 0, 2*pi))
    I2 = integrate(r**3, (r, 0, 4*cos(th)), (th, -pi/2, pi/2))
    I12 = integrate(r**3, (r, 0, 2), (th, -pi/3, pi/3)) + 2*integrate(r**3, (r, 0, 4*cos(th)), (th, pi/3, pi/2))
    assert EQ(I1, 8*pi) and EQ(I2, 24*pi) and EQ(I12, 32*pi/3 - 14*sqrt(3))
    U = I1 + I2 - I12
    assert EQ(U, 64*pi/3 + 14*sqrt(3))
    num = mp.quad(lambda T: max(2, 4*mp.cos(T))**4/4, [-mp.pi/2, -mp.pi/3, mp.pi/3, mp.pi/2]) + 4*mp.pi
    assert abs(num - (64*mp.pi/3 + 14*mp.sqrt(3))) < 1e-9
P(id="4-82", ch=15, sec="15.3", type="15-polar", src="2024 중간 6번 유형",
  q=r"$D_1$, $D_2$가 각각 원판 $x^2+y^2\le4$와 $(x-2)^2+y^2\le4$일 때 $\displaystyle\iint_{D_1\cup D_2}(x^2+y^2)\,dA$를 계산하라.",
  hint=r"$\iint_{D_1\cup D_2}=\iint_{D_1}+\iint_{D_2}-\iint_{D_1\cap D_2}$. $D_2$는 $r\le4\cos\theta$, 두 원은 $\theta=\pm\tfrac\pi3$에서 만나요.",
  ans=r"$\dfrac{64\pi}{3}+14\sqrt3$",
  sol=[r"$\displaystyle\iint_{D_1}r^2dA=\int_0^{2\pi}\!\!\int_0^2r^3dr\,d\theta=8\pi$,  $\displaystyle\iint_{D_2}=\int_{-\pi/2}^{\pi/2}\frac{(4\cos\theta)^4}{4}d\theta=64\cdot\frac{3\pi}{8}=24\pi$",
       r"$D_1\cap D_2$: $|\theta|\le\tfrac\pi3$에서 $r\le2$, $\tfrac\pi3\le|\theta|\le\tfrac\pi2$에서 $r\le4\cos\theta$",
       r"$\displaystyle\iint_{D_1\cap D_2}=\int_{-\pi/3}^{\pi/3}4\,d\theta+2\int_{\pi/3}^{\pi/2}64\cos^4\theta\,d\theta=\frac{8\pi}3+128\Big(\frac{\pi}{16}-\frac{7\sqrt3}{64}\Big)=\frac{32\pi}{3}-14\sqrt3$",
       r"($\int\cos^4\theta\,d\theta=\tfrac{3\theta}8+\tfrac{\sin2\theta}4+\tfrac{\sin4\theta}{32}$)",
       r"합: $8\pi+24\pi-\Big(\dfrac{32\pi}3-14\sqrt3\Big)=\dfrac{64\pi}{3}+14\sqrt3$"],
  check=_c)


def _c():
    a = symbols('a', positive=True)
    disk = integrate(exp(-r**2)*r, (r, 0, a), (th, 0, 2*pi))
    assert simplify(disk - pi*(1 - exp(-a**2))) == 0 and limit(disk, a, oo) == pi
    assert integrate(exp(-x**2), (x, -oo, oo)) == sqrt(pi)
    assert EQ(integrate(x**2*exp(-x**2), (x, 0, oo)), sqrt(pi)/4)
P(id="4-83", ch=15, sec="15.3", type="15-polar", src="교재 15.3 심화형 (가우스 적분)",
  q=r"(a) $D_a$가 반지름 $a$인 원판일 때 $\displaystyle\iint_{D_a}e^{-(x^2+y^2)}dA$를 구하고 $a\to\infty$인 극한 $\displaystyle\iint_{\mathbb R^2}e^{-(x^2+y^2)}dA$를 구하라.<br>(b) $\displaystyle\iint_{\mathbb R^2}e^{-(x^2+y^2)}dA=\Big(\int_{-\infty}^{\infty}e^{-x^2}dx\Big)^2$임을 이용해 $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}dx$를 구하라.<br>(c) $\displaystyle\int_0^{\infty}x^2e^{-x^2}dx$를 구하라.",
  hint=r"(a) 극좌표: $e^{-r^2}r$은 $u=r^2$ 치환. (b) $e^{-(x^2+y^2)}=e^{-x^2}e^{-y^2}$이라 정사각형 위 적분이 두 1변수 적분의 곱. (c) $x\cdot xe^{-x^2}$로 보고 부분적분.",
  ans=r"(a) $\pi(1-e^{-a^2})$, 극한 $\pi$  (b) $\sqrt\pi$  (c) $\dfrac{\sqrt\pi}{4}$",
  sol=[r"(a) $\displaystyle\int_0^{2\pi}\!\!\int_0^ae^{-r^2}r\,dr\,d\theta=2\pi\cdot\frac12\big(1-e^{-a^2}\big)=\pi\big(1-e^{-a^2}\big)\to\pi$",
       r"(b) 정사각형 $[-a,a]^2$ 위에서 $\displaystyle\iint e^{-x^2}e^{-y^2}dA=\Big(\int_{-a}^ae^{-x^2}dx\Big)^2$, $a\to\infty$이면 같은 값 $\pi$로 수렴",
       r"$\displaystyle\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$ (양수)",
       r"(c) $\displaystyle\int_0^\infty x\cdot xe^{-x^2}dx=\Big[-\frac x2e^{-x^2}\Big]_0^\infty+\frac12\int_0^\infty e^{-x^2}dx=0+\frac12\cdot\frac{\sqrt\pi}{2}=\frac{\sqrt\pi}4$"],
  check=_c)


def _c():
    M = integrate(r*r, (r, 1, 2), (th, -pi/4, pi/4))
    My = integrate(r*cos(th)*r*r, (r, 1, 2), (th, -pi/4, pi/4))
    assert EQ(M, 7*pi/6) and EQ(My, 15*sqrt(2)/4) and EQ(My/M, 45*sqrt(2)/(14*pi))
    f = lambda X, Y: mp.sqrt(X*X + Y*Y)
    s2 = 1/mp.sqrt(2)
    num = (q2(f, s2, 1, lambda X: -X, lambda X: -mp.sqrt(1 - X*X))
           + q2(f, s2, 1, lambda X: mp.sqrt(1 - X*X), lambda X: X)
           + q2(f, 1, mp.sqrt(2), lambda X: -X, lambda X: X)
           + q2(f, mp.sqrt(2), 2, lambda X: -mp.sqrt(4 - X*X), lambda X: mp.sqrt(4 - X*X)))
    assert abs(num - 7*mp.pi/6) < 1e-8
P(id="4-84", ch=15, sec="15.3", type="15-mass", src="2022 중간 블럭2 7번 유형",
  q=r"(a) 극좌표를 이용해 다음 합을 하나의 이중적분으로 나타내라. $$\int_{1/\sqrt2}^{1}\!\!\int_{-x}^{-\sqrt{1-x^2}}f\,dy\,dx+\int_{1/\sqrt2}^{1}\!\!\int_{\sqrt{1-x^2}}^{x}f\,dy\,dx+\int_{1}^{\sqrt2}\!\!\int_{-x}^{x}f\,dy\,dx+\int_{\sqrt2}^{2}\!\!\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}f\,dy\,dx$$ (b) 위 영역을 차지하는 판의 밀도가 $\rho(x,y)=\sqrt{x^2+y^2}$일 때 질량과 질량중심을 구하라.",
  hint=r"네 조각을 합치면 두 원 $r=1$, $r=2$ 사이에서 두 직선 $y=\pm x$ 사이(오른쪽) 부분: $1\le r\le2,\ -\tfrac\pi4\le\theta\le\tfrac\pi4$. $x$축 대칭이라 $\bar y=0$.",
  ans=r"(a) $\displaystyle\int_{-\pi/4}^{\pi/4}\!\!\int_1^2f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$  (b) 질량 $\dfrac{7\pi}{6}$, 질량중심 $\Big(\dfrac{45\sqrt2}{14\pi},\ 0\Big)$",
  sol=[r"(a) $x\in[\tfrac1{\sqrt2},1]$: 원 $r=1$ 바깥 & $|y|\le x$, $x\in[1,\sqrt2]$: $|y|\le x$, $x\in[\sqrt2,2]$: 원 $r=2$ 안 → 합치면 $1\le r\le2,\ |\theta|\le\tfrac\pi4$",
       r"(b) $m=\displaystyle\int_{-\pi/4}^{\pi/4}\!\!\int_1^2r\cdot r\,dr\,d\theta=\frac\pi2\cdot\frac73=\frac{7\pi}6$",
       r"$M_y=\displaystyle\iint x\rho\,dA=\int_{-\pi/4}^{\pi/4}\!\!\int_1^2r^3\cos\theta\,dr\,d\theta=\sqrt2\cdot\frac{15}{4}=\frac{15\sqrt2}{4}$",
       r"$\bar x=\dfrac{15\sqrt2/4}{7\pi/6}=\dfrac{45\sqrt2}{14\pi}$, $\bar y=0$ (대칭)"],
  check=_c)


def _c():
    V = integrate(2*sqrt(4 - r**2)*r, (r, 1, 2), (th, 0, 2*pi))
    assert EQ(V, 4*sqrt(3)*pi) and EQ(V/(R(4, 3)*pi*8), 3*sqrt(3)/8)
P(id="4-85", ch=15, sec="15.3", type="15-polar", src="교재 15.3 심화형 (구멍 뚫린 구)",
  q=r"반지름 $2$인 구의 중심을 지나도록 반지름 $1$인 원기둥 모양의 구멍을 뚫었다. (구멍의 축은 구의 지름과 일치)<br>(a) 남은 입체의 부피를 구하라.  (b) 남은 부분은 처음 구의 부피의 몇 배인가?",
  hint=r"구 $x^2+y^2+z^2\le4$에서 원기둥 $x^2+y^2<1$을 뺀 부분: 극좌표로 $1\le r\le2$에서 높이 $2\sqrt{4-r^2}$.",
  ans=r"(a) $4\sqrt3\,\pi$  (b) $\dfrac{3\sqrt3}{8}$배",
  sol=[r"(a) $V=\displaystyle\int_0^{2\pi}\!\!\int_1^22\sqrt{4-r^2}\,r\,dr\,d\theta=2\pi\cdot\Big[-\frac23(4-r^2)^{3/2}\Big]_1^2=2\pi\cdot\frac23\cdot3\sqrt3=4\sqrt3\pi$",
       r"(b) 구의 부피 $\tfrac43\pi\cdot8=\tfrac{32\pi}{3}$ → $\dfrac{4\sqrt3\pi}{32\pi/3}=\dfrac{3\sqrt3}{8}\approx0.65$배"],
  check=_c)


def _c():
    A = integrate(r, (r, 0, 2), (th, 0, pi)) - integrate(r, (r, 0, 2*cos(th)), (th, 0, pi/2))
    Mx_ = integrate(r*cos(th)*r, (r, 0, 2), (th, 0, pi)) - integrate(r*cos(th)*r, (r, 0, 2*cos(th)), (th, 0, pi/2))
    My_ = integrate(r*sin(th)*r, (r, 0, 2), (th, 0, pi)) - integrate(r*sin(th)*r, (r, 0, 2*cos(th)), (th, 0, pi/2))
    assert EQ(A, 3*pi/2) and EQ(Mx_, -pi/2) and EQ(My_, R(14, 3))
    assert EQ(Mx_/A, R(-1, 3)) and EQ(My_/A, 28/(9*pi))
P(id="4-86", ch=15, sec="15.3", type="15-mass", src="2022 중간 블럭1 8번 유형 (빼서 구하는 무게중심)",
  q=r"영역 $D=\{(x,y)\mid x^2+y^2\le4,\ x^2+y^2\ge2x,\ y\ge0\}$을 차지하는 밀도가 일정한 판의 질량중심을 구하라.",
  hint=r"$D$ = (반지름 $2$인 위쪽 반원판) − (원 $r=2\cos\theta$의 위쪽 반원판). 적분도 빼기로: $\iint_D=\iint_{\text{큰 반원}}-\iint_{\text{작은 반원}}$.",
  ans=r"$\Big(-\dfrac13,\ \dfrac{28}{9\pi}\Big)$",
  sol=[r"넓이: $2\pi-\dfrac\pi2=\dfrac{3\pi}{2}$",
       r"$\displaystyle\iint_Dx\,dA=\underbrace{\int_0^\pi\!\!\int_0^2r^2\cos\theta\,dr\,d\theta}_{0}-\int_0^{\pi/2}\!\!\int_0^{2\cos\theta}r^2\cos\theta\,dr\,d\theta=0-\frac83\cdot\frac{3\pi}{16}=-\frac\pi2$",
       r"$\displaystyle\iint_Dy\,dA=\int_0^\pi\!\!\int_0^2r^2\sin\theta\,dr\,d\theta-\int_0^{\pi/2}\frac{8\cos^3\theta}{3}\sin\theta\,d\theta=\frac{16}3-\frac23=\frac{14}{3}$",
       r"$\bar x=\dfrac{-\pi/2}{3\pi/2}=-\dfrac13$,  $\bar y=\dfrac{14/3}{3\pi/2}=\dfrac{28}{9\pi}$"],
  check=_c)


# ───────── 15.6 ─────────
def _c():
    test = z**2*y + x
    p1 = integrate(test, (z, x, 1), (x, 0, 1 - y), (y, 0, 1))
    p2 = integrate(test, (z, x, 1), (y, 1 - x, 1), (x, 0, 1))
    full = integrate(test, (x, 0, z), (y, 0, 1), (z, 0, 1))
    assert EQ(p1 + p2, full)
    I = integrate(z*exp(z**2), (z, 0, 1)) * integrate(1/(1 + y**2), (y, 0, 1))
    assert EQ(I, pi*(E - 1)/8)
P(id="4-87", ch=15, sec="15.6", type="15-order3", src="2025 중간 9번 유형",
  q=r"다음 값을 구하라. $$\int_0^1\!\!\int_0^{1-y}\!\!\int_x^1\frac{e^{z^2}}{1+y^2}\,dz\,dx\,dy+\int_0^1\!\!\int_{1-x}^{1}\!\!\int_x^1\frac{e^{z^2}}{1+y^2}\,dz\,dy\,dx$$",
  hint=r"첫째는 $x+y\le1$, 둘째는 $x+y\ge1$ 부분 → 합치면 $0\le x\le1,\ 0\le y\le1,\ x\le z\le1$. $e^{z^2}$은 $z$로 적분할 수 없으니 $x$를 가장 안쪽으로!",
  ans=r"$\dfrac{\pi(e-1)}{8}$",
  sol=[r"첫째 영역: $0\le y\le1,\ 0\le x\le1-y,\ x\le z\le1$ / 둘째: $0\le x\le1,\ 1-x\le y\le1,\ x\le z\le1$",
       r"합: $E=\{0\le x\le1,\ 0\le y\le1,\ x\le z\le1\}=\{0\le z\le1,\ 0\le y\le1,\ 0\le x\le z\}$",
       r"$\displaystyle\int_0^1\!\!\int_0^1\!\!\int_0^z\frac{e^{z^2}}{1+y^2}\,dx\,dy\,dz=\Big(\int_0^1ze^{z^2}dz\Big)\Big(\int_0^1\frac{dy}{1+y^2}\Big)$",
       r"$=\dfrac{e-1}{2}\cdot\dfrac\pi4=\dfrac{\pi(e-1)}{8}$"],
  check=_c)


def _c():
    test = x + y**2*z + 1
    orig = integrate(test, (z, 0, 1 - y), (y, sqrt(x), 1), (x, 0, 1))
    a = integrate(test, (y, sqrt(x), 1 - z), (z, 0, 1 - sqrt(x)), (x, 0, 1))
    b = integrate(test, (x, 0, y**2), (y, 0, 1 - z), (z, 0, 1))
    assert EQ(orig, a) and EQ(orig, b)
    assert EQ(integrate(1, (z, 0, 1 - y), (y, sqrt(x), 1), (x, 0, 1)), R(1, 12))
P(id="4-88", ch=15, sec="15.6", type="15-order3", src="2022 중간 블럭2 8(a) 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_{\sqrt x}^{1}\!\!\int_0^{1-y}f(x,y,z)\,dz\,dy\,dx$를<br>(a) $dy\,dz\,dx$ 순서  (b) $dx\,dy\,dz$ 순서로 다시 쓰고, (c) $f=1$일 때 입체의 부피를 구하라.",
  hint=r"영역: $0\le x\le1,\ \sqrt x\le y\le1,\ 0\le z\le1-y$ ⟺ $0\le y\le1,\ 0\le x\le y^2,\ 0\le z\le1-y$. (a)는 $x$를 고정한 $yz$평면의 삼각형, (b)는 $z$를 고정한 $xy$평면의 단면을 그려 보세요.",
  ans=r"(a) $\displaystyle\int_0^1\!\!\int_0^{1-\sqrt x}\!\!\int_{\sqrt x}^{1-z}f\,dy\,dz\,dx$  (b) $\displaystyle\int_0^1\!\!\int_0^{1-z}\!\!\int_0^{y^2}f\,dx\,dy\,dz$  (c) $\dfrac1{12}$",
  sol=[r"(a) $x$ 고정: $yz$평면에서 $\sqrt x\le y\le1,\ 0\le z\le1-y$ (삼각형) → $0\le z\le1-\sqrt x$, $\sqrt x\le y\le1-z$",
       r"(b) $z$ 고정: $y\le1-z$이고 $\sqrt x\le y \iff x\le y^2$ → $0\le y\le1-z,\ 0\le x\le y^2$",
       r"(c) $\displaystyle\int_0^1\!\!\int_0^{1-z}y^2\,dy\,dz=\int_0^1\frac{(1-z)^3}{3}dz=\frac1{12}$ (어느 순서로 해도 같아요)"],
  check=_c)


def _c():
    V = integrate(1, (x, 0, 1 - z), (z, 0, 1 - y**2), (y, -1, 1))
    Mx = integrate(x, (x, 0, 1 - z), (z, 0, 1 - y**2), (y, -1, 1))
    Mz = integrate(z, (x, 0, 1 - z), (z, 0, 1 - y**2), (y, -1, 1))
    My = integrate(y, (x, 0, 1 - z), (z, 0, 1 - y**2), (y, -1, 1))
    assert EQ(V, R(4, 5)) and EQ(Mx, R(2, 7)) and EQ(Mz, R(8, 35)) and My == 0
    assert EQ(Mx/V, R(5, 14)) and EQ(Mz/V, R(2, 7))
P(id="4-89", ch=15, sec="15.6", type="15-mass", src="교재 15.6 심화형 (입체의 무게중심)",
  q=r"포물기둥 $z=1-y^2$과 평면 $x+z=1$, $x=0$, $z=0$으로 둘러싸인 밀도가 일정한 입체의 질량중심을 구하라.",
  hint=r"$yz$평면의 영역 $-1\le y\le1,\ 0\le z\le1-y^2$ 위에서 $0\le x\le1-z$. $y\to-y$ 대칭이라 $\bar y=0$.",
  ans=r"$\Big(\dfrac5{14},\ 0,\ \dfrac27\Big)$",
  sol=[r"$V=\displaystyle\int_{-1}^1\!\!\int_0^{1-y^2}(1-z)\,dz\,dy=\int_{-1}^1\Big(\frac12-\frac{y^4}{2}\Big)dy=\frac45$",
       r"$\displaystyle\iiint x\,dV=\int_{-1}^1\!\!\int_0^{1-y^2}\frac{(1-z)^2}{2}dz\,dy=\int_{-1}^1\frac{1-y^6}{6}dy=\frac27$",
       r"$\displaystyle\iiint z\,dV=\int_{-1}^1\!\!\int_0^{1-y^2}z(1-z)\,dz\,dy=\int_{-1}^1\Big[\frac{(1-y^2)^2}{2}-\frac{(1-y^2)^3}{3}\Big]dy=\frac8{15}-\frac{32}{105}=\frac{8}{35}$",
       r"$\bar x=\dfrac{2/7}{4/5}=\dfrac5{14}$, $\bar y=0$, $\bar z=\dfrac{8/35}{4/5}=\dfrac27$"],
  check=_c)


def _c():
    V = integrate(exp(x + y), (y, 0, 1 - x), (x, 0, 1))
    Ixy = integrate((x + y)*exp(x + y), (y, 0, 1 - x), (x, 0, 1))
    Iz = integrate(exp(2*(x + y))/2, (y, 0, 1 - x), (x, 0, 1))
    assert EQ(V, 1) and EQ(Ixy, E - 2) and EQ(Iz, (E**2 + 1)/8)
P(id="4-90", ch=15, sec="15.6", type="15-triple", src="교재 15.6 심화형",
  q=r"$E$가 제1팔분공간에서 평면 $x+y=1$, 좌표평면들, 곡면 $z=e^{x+y}$으로 둘러싸인 입체일 때<br>(a) $E$의 부피  (b) $\displaystyle\iiint_E(x+y)\,dV$  (c) $\displaystyle\iiint_Ez\,dV$를 구하라.",
  hint=r"밑면 삼각형 $0\le x\le1,\ 0\le y\le1-x$ 위에서 $0\le z\le e^{x+y}$. $y$로 적분할 때 $u=x+y$로 보면 $\int_x^1(\cdots)\,du$.",
  ans=r"(a) $1$  (b) $e-2$  (c) $\dfrac{e^2+1}{8}$",
  sol=[r"(a) $\displaystyle\int_0^1\!\!\int_0^{1-x}e^{x+y}dy\,dx=\int_0^1(e-e^x)\,dx=e-(e-1)=1$",
       r"(b) $\displaystyle\int_0^{1-x}(x+y)e^{x+y}dy=\int_x^1ue^u\,du=\Big[(u-1)e^u\Big]_x^1=(1-x)e^x$ → $\displaystyle\int_0^1(1-x)e^xdx=\Big[(2-x)e^x\Big]_0^1=e-2$",
       r"(c) $\displaystyle\iiint z\,dV=\iint\frac{e^{2(x+y)}}{2}dA=\frac12\int_0^1\frac{e^2-e^{2x}}{2}dx=\frac14\Big(e^2-\frac{e^2-1}{2}\Big)=\frac{e^2+1}{8}$",
       r"(부피가 $1$이므로 무게중심의 $z$좌표가 바로 $\tfrac{e^2+1}{8}$)"],
  check=_c)


def _c():
    test = x*z + y
    orig = integrate(test, (y, x**2, 1), (x, 0, 1), (z, 0, 1))
    re_ = integrate(test, (x, 0, sqrt(y)), (y, 0, 1), (z, 0, 1))
    assert EQ(orig, re_)
    yp = symbols('yp', positive=True)
    inner = integrate(4*x*z*exp(z*yp**2), (x, 0, sqrt(yp)))
    assert simplify(inner - 2*yp*z*exp(z*yp**2)) == 0
    zp = symbols('zp', positive=True)
    step = integrate(2*yp*zp*exp(zp*yp**2), (yp, 0, 1))
    assert simplify(step - (exp(zp) - 1)) == 0
    assert EQ(integrate(exp(zp) - 1, (zp, 0, 1)), E - 2)
P(id="4-91", ch=15, sec="15.6", type="15-order3", src="교재 15.6 심화형 (순서를 두 번 바꾸기)",
  q=r"$\displaystyle\int_0^1\!\!\int_0^1\!\!\int_{x^2}^{1}4xz\,e^{zy^2}\,dy\,dx\,dz$를 계산하라.",
  hint=r"$e^{zy^2}$은 $y$로 바로 적분이 안 돼요. $x^2\le y \iff x\le\sqrt y$로 $x$를 가장 안쪽으로 보내면 $2yz$가 생기고, 그다음은 $y$로 먼저 적분하면 깔끔해요.",
  ans=r"$e-2$",
  sol=[r"영역: $0\le z\le1,\ 0\le x\le1,\ x^2\le y\le1$ ⟺ $0\le z\le1,\ 0\le y\le1,\ 0\le x\le\sqrt y$",
       r"$\displaystyle\int_0^{\sqrt y}4xz\,dx=2yz$ → $\displaystyle\int_0^1\!\!\int_0^1 2yz\,e^{zy^2}\,dy\,dz$",
       r"$y$로 먼저: $\displaystyle\int_0^12yz\,e^{zy^2}dy=\Big[e^{zy^2}\Big]_0^1=e^z-1$",
       r"$\displaystyle\int_0^1(e^z-1)\,dz=e-2$"],
  check=_c)


def _c():
    inner = R(16, 3)*((4 - x**2)/2)**R(3, 2)
    num = mp.quad(lambda X: mp.quad(lambda Y: 8 - 2*X*X - 4*Y*Y, [-mp.sqrt((4 - X*X)/2), mp.sqrt((4 - X*X)/2)]), [-2, 2])
    assert abs(num - 8*mp.sqrt(2)*mp.pi) < 1e-8
    assert EQ(integrate((4 - x**2)**R(3, 2), (x, -2, 2)), 6*pi)
    assert EQ(R(16, 3)*(R(1, 2))**R(3, 2)*6*pi, 8*sqrt(2)*pi)
P(id="4-92", ch=15, sec="15.6", type="15-triple", src="교재 15.6 심화형 (타원 영역의 부피)",
  q=r"두 곡면 $z=x^2+3y^2$과 $z=8-x^2-y^2$으로 둘러싸인 입체의 부피를 구하라.",
  hint=r"교선의 정사영: $x^2+3y^2=8-x^2-y^2 \iff x^2+2y^2=4$ (타원). 높이 $8-2x^2-4y^2$를 타원 위에서 적분 — $y$로 먼저 적분하고 $\int_{-2}^2(4-x^2)^{3/2}dx=6\pi$를 쓰세요.",
  ans=r"$8\sqrt2\,\pi$",
  sol=[r"밑면 $D:\ x^2+2y^2\le4$, 높이 $(8-x^2-y^2)-(x^2+3y^2)=8-2x^2-4y^2$",
       r"$h=\sqrt{\tfrac{4-x^2}{2}}$로 두면 $8-2x^2=4h^2$: $\displaystyle\int_{-h}^{h}(4h^2-4y^2)\,dy=8h^3-\frac83h^3=\frac{16}3h^3$",
       r"$V=\displaystyle\int_{-2}^{2}\frac{16}{3}\Big(\frac{4-x^2}{2}\Big)^{3/2}dx=\frac{16}{3}\cdot\frac{1}{2\sqrt2}\int_{-2}^2(4-x^2)^{3/2}dx$",
       r"$x=2\sin t$: $\displaystyle\int_{-2}^2(4-x^2)^{3/2}dx=16\int_{-\pi/2}^{\pi/2}\cos^4t\,dt=6\pi$ → $V=\dfrac{16}{6\sqrt2}\cdot6\pi=8\sqrt2\,\pi$"],
  check=_c)


# ───────── 15.7 ─────────
def _c():
    I = integrate((r**2*sin(2*th) - r**4)*r**2*r, (r, 0, sqrt(sin(2*th))), (th, 0, pi/2))
    assert EQ(I, pi/128)
P(id="4-93", ch=15, sec="15.7", type="15-cyl", src="2025 중간 4번 유형",
  q=r"$E$가 제1팔분공간에서 두 곡면 $z=(x^2+y^2)^2$과 $z=2xy$로 둘러싸인 입체일 때 $\displaystyle\iiint_E(x^2+y^2)\,dV$를 계산하라.",
  hint=r"원주좌표: $(x^2+y^2)^2=r^4$, $2xy=r^2\sin2\theta$. 두 곡면 사이가 비어 있지 않으려면 $r^4\le r^2\sin2\theta$, 즉 $r\le\sqrt{\sin2\theta}$.",
  ans=r"$\dfrac{\pi}{128}$",
  sol=[r"$E=\{0\le\theta\le\tfrac\pi2,\ 0\le r\le\sqrt{\sin2\theta},\ r^4\le z\le r^2\sin2\theta\}$",
       r"$\displaystyle\iiint_E r^2\,dV=\int_0^{\pi/2}\!\!\int_0^{\sqrt{\sin2\theta}}(r^2\sin2\theta-r^4)\,r^3\,dr\,d\theta$",
       r"$r$ 적분: $\sin2\theta\cdot\dfrac{r^6}{6}-\dfrac{r^8}{8}\Big|_0^{\sqrt{\sin2\theta}}=\Big(\dfrac16-\dfrac18\Big)\sin^42\theta=\dfrac{\sin^42\theta}{24}$",
       r"$\displaystyle\frac1{24}\int_0^{\pi/2}\sin^42\theta\,d\theta=\frac1{24}\cdot\frac{3\pi}{16}=\frac{\pi}{128}$"],
  check=_c)


def _c():
    V = integrate(2*pi*integrate(r, (r, 0, sqrt(1 + z**2))), (z, -1, 1))
    I = integrate(2*pi*integrate(r**3, (r, 0, sqrt(1 + z**2))), (z, -1, 1))
    assert EQ(V, 8*pi/3) and EQ(I, 28*pi/15)
P(id="4-94", ch=15, sec="15.7", type="15-cyl", src="2022 중간 블럭2 9번 응용 (한 장 쌍곡면)",
  q=r"$E$가 한 장 쌍곡면 $x^2+y^2-z^2=1$의 안쪽(축을 포함하는 쪽)에서 두 평면 $z=-1$, $z=1$ 사이에 있는 입체일 때<br>(a) $E$의 부피  (b) $\displaystyle\iiint_E(x^2+y^2)\,dV$를 구하라.",
  hint=r"$E=\{-1\le z\le1,\ 0\le r\le\sqrt{1+z^2}\}$ — 이번에는 $z$를 가장 바깥에 두고 높이 $z$마다 원판 단면을 적분하는 순서 ($dr\,d\theta\,dz$)가 편해요.",
  ans=r"(a) $\dfrac{8\pi}{3}$  (b) $\dfrac{28\pi}{15}$",
  sol=[r"(a) $V=\displaystyle\int_{-1}^1\!\!\int_0^{2\pi}\!\!\int_0^{\sqrt{1+z^2}}r\,dr\,d\theta\,dz=\int_{-1}^1\pi(1+z^2)\,dz=\pi\Big(2+\frac23\Big)=\frac{8\pi}3$",
       r"(b) $\displaystyle\int_{-1}^1\!\!\int_0^{2\pi}\!\!\int_0^{\sqrt{1+z^2}}r^2\cdot r\,dr\,d\theta\,dz=\int_{-1}^1\frac{\pi}{2}(1+z^2)^2dz$",
       r"$=\dfrac\pi2\Big(2+\dfrac43+\dfrac25\Big)=\dfrac\pi2\cdot\dfrac{56}{15}=\dfrac{28\pi}{15}$"],
  check=_c)


def _c():
    V = integrate((2*r*sin(th) - r**2)*r, (r, 0, 2*sin(th)), (th, 0, pi))
    My = integrate((2*r*sin(th) - r**2)*r*sin(th)*r, (r, 0, 2*sin(th)), (th, 0, pi))
    Mz = integrate(((2*r*sin(th))**2 - r**4)/2*r, (r, 0, 2*sin(th)), (th, 0, pi))
    Mx = integrate((2*r*sin(th) - r**2)*r*cos(th)*r, (r, 0, 2*sin(th)), (th, 0, pi))
    assert EQ(V, pi/2) and EQ(My, pi/2) and EQ(Mz, 5*pi/6) and EQ(Mx, 0)
    th_p = symbols('th_p', positive=True)
    assert simplify(integrate((2*r*sin(th_p) - r**2)*r, (r, 0, 2*sin(th_p))) - R(4, 3)*sin(th_p)**4) == 0
    assert simplify(integrate((2*r*sin(th_p) - r**2)*r**2*sin(th_p), (r, 0, 2*sin(th_p))) - R(8, 5)*sin(th_p)**6) == 0
    assert simplify(integrate(((2*r*sin(th_p))**2 - r**4)/2*r, (r, 0, 2*sin(th_p))) - R(8, 3)*sin(th_p)**6) == 0
P(id="4-95", ch=15, sec="15.7", type="15-mass", src="교재 15.7 심화형 (포물면과 평면 사이 입체)",
  q=r"포물면 $z=x^2+y^2$과 평면 $z=2y$로 둘러싸인 밀도가 일정한 입체의 부피와 질량중심을 구하라.",
  hint=r"교선의 정사영: $x^2+y^2=2y \iff r=2\sin\theta$ ($0\le\theta\le\pi$). 높이는 $2r\sin\theta-r^2$. $\int_0^\pi\sin^4\theta\,d\theta=\tfrac{3\pi}8$, $\int_0^\pi\sin^6\theta\,d\theta=\tfrac{5\pi}{16}$.",
  ans=r"부피 $\dfrac\pi2$, 질량중심 $\Big(0,\ 1,\ \dfrac53\Big)$",
  sol=[r"$V=\displaystyle\int_0^\pi\!\!\int_0^{2\sin\theta}(2r\sin\theta-r^2)\,r\,dr\,d\theta=\int_0^\pi\Big(\frac{16}{3}-4\Big)\sin^4\theta\,d\theta=\frac43\cdot\frac{3\pi}8=\frac\pi2$",
       r"$\displaystyle\iiint y\,dV=\int_0^\pi\!\!\int_0^{2\sin\theta}(2r\sin\theta-r^2)r^2\sin\theta\,dr\,d\theta=\int_0^\pi\frac85\sin^6\theta\,d\theta=\frac\pi2$ → $\bar y=1$",
       r"$\displaystyle\iiint z\,dV=\int_0^\pi\!\!\int_0^{2\sin\theta}\frac{4r^2\sin^2\theta-r^4}{2}\,r\,dr\,d\theta=\int_0^\pi\frac{8}{3}\sin^6\theta\,d\theta=\frac{5\pi}{6}$ → $\bar z=\dfrac53$",
       r"$yz$평면 대칭 → $\bar x=0$"],
  check=_c)


def _c():
    I = integrate(r*cos(th)*z*r, (z, 0, r), (r, 0, 2*cos(th)), (th, 0, pi/2))
    assert EQ(I, pi/2)
    num = mp.quad(lambda X: mp.quad(lambda Y: X*(X*X + Y*Y)/2, [0, mp.sqrt(max(0, 2*X - X*X))]), [0, 1, 2])
    assert abs(num - mp.pi/2) < 1e-7
P(id="4-96", ch=15, sec="15.7", type="15-cyl", src="교재 15.7 심화형 (직교좌표 → 원주좌표)",
  q=r"원주좌표로 바꾸어 계산하라. $$\int_0^2\!\!\int_0^{\sqrt{2x-x^2}}\!\!\int_0^{\sqrt{x^2+y^2}}xz\,dz\,dy\,dx$$",
  hint=r"$y=\sqrt{2x-x^2} \iff (x-1)^2+y^2=1,\ y\ge0$ → 극좌표 $0\le r\le2\cos\theta,\ 0\le\theta\le\tfrac\pi2$. $z$의 범위는 $0\le z\le r$.",
  ans=r"$\dfrac\pi2$",
  sol=[r"밑면: 원 $(x-1)^2+y^2=1$의 위쪽 반원판 → $0\le\theta\le\tfrac\pi2,\ 0\le r\le2\cos\theta$",
       r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^{2\cos\theta}\!\!\int_0^{r}(r\cos\theta)\,z\,r\,dz\,dr\,d\theta=\int_0^{\pi/2}\!\!\int_0^{2\cos\theta}\frac{r^4\cos\theta}{2}\,dr\,d\theta$",
       r"$=\displaystyle\int_0^{\pi/2}\frac{\cos\theta\,(2\cos\theta)^5}{10}d\theta=\frac{16}{5}\int_0^{\pi/2}\cos^6\theta\,d\theta=\frac{16}5\cdot\frac{5\pi}{32}=\frac\pi2$"],
  check=_c)


# ───────── 15.8 ─────────
def _c():
    V = integrate(rho**2*sin(ph), (rho, 0, sin(ph)), (ph, 0, pi), (th, 0, 2*pi))
    I = integrate(rho**4*sin(ph), (rho, 0, sin(ph)), (ph, 0, pi), (th, 0, 2*pi))
    assert EQ(V, pi**2/4) and EQ(I, pi**2/8)
P(id="4-97", ch=15, sec="15.8", type="15-sph", src="2024 중간 10번 유형 (곡면을 구면좌표로)",
  q=r"$E$가 곡면 $x^2+y^2+z^2=\sqrt{x^2+y^2}$으로 둘러싸인 입체일 때<br>(a) $E$의 부피  (b) $\displaystyle\iiint_E(x^2+y^2+z^2)\,dV$를 구하라.",
  hint=r"$\rho^2=\rho\sin\phi$ → $\rho=\sin\phi$ ($0\le\phi\le\pi$, 가운데 구멍이 한 점으로 닫힌 도넛 모양). $\int_0^\pi\sin^4\phi\,d\phi=\tfrac{3\pi}8$, $\int_0^\pi\sin^6\phi\,d\phi=\tfrac{5\pi}{16}$.",
  ans=r"(a) $\dfrac{\pi^2}{4}$  (b) $\dfrac{\pi^2}{8}$",
  sol=[r"$\sqrt{x^2+y^2}=\rho\sin\phi$ → 곡면 $\rho=\sin\phi$, $E=\{0\le\theta\le2\pi,\ 0\le\phi\le\pi,\ 0\le\rho\le\sin\phi\}$",
       r"(a) $V=2\pi\displaystyle\int_0^\pi\frac{\sin^3\phi}{3}\sin\phi\,d\phi=\frac{2\pi}{3}\cdot\frac{3\pi}{8}=\frac{\pi^2}4$",
       r"(b) $\displaystyle\iiint\rho^2\,dV=2\pi\int_0^\pi\frac{\sin^5\phi}{5}\sin\phi\,d\phi=\frac{2\pi}5\cdot\frac{5\pi}{16}=\frac{\pi^2}{8}$"],
  check=_c)


def _c():
    V = integrate(rho**2*sin(ph), (rho, 0, 4*cos(ph)), (ph, 0, pi/6), (th, 0, 2*pi))
    Mz = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, 4*cos(ph)), (ph, 0, pi/6), (th, 0, 2*pi))
    assert EQ(V, 14*pi/3) and EQ(Mz, 37*pi/3) and EQ(Mz/V, R(37, 14))
P(id="4-98", ch=15, sec="15.8", type="15-sph", src="2022 중간 블럭2 10번 유형",
  q=r"원뿔 $z=\sqrt3\sqrt{x^2+y^2}$ 위쪽, 구 $x^2+y^2+z^2=4z$ 안쪽에 있는 밀도가 일정한 입체에 대해<br>(a) 부피  (b) 질량중심을 구하라.",
  hint=r"구: $\rho^2=4\rho\cos\phi$ → $\rho=4\cos\phi$. 원뿔: $\tan\phi=\dfrac{r}{z}=\dfrac1{\sqrt3}$ → $\phi=\dfrac\pi6$. 대칭이라 $\bar x=\bar y=0$.",
  ans=r"(a) $\dfrac{14\pi}{3}$  (b) $\Big(0,\ 0,\ \dfrac{37}{14}\Big)$",
  sol=[r"$E=\{0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi6,\ 0\le\rho\le4\cos\phi\}$",
       r"(a) $V=2\pi\displaystyle\int_0^{\pi/6}\frac{64\cos^3\phi}{3}\sin\phi\,d\phi=\frac{128\pi}{3}\cdot\frac{1-\cos^4\frac\pi6}{4}=\frac{32\pi}{3}\cdot\frac{7}{16}=\frac{14\pi}3$",
       r"(b) $\displaystyle\iiint z\,dV=2\pi\int_0^{\pi/6}\!\!\int_0^{4\cos\phi}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi=128\pi\int_0^{\pi/6}\cos^5\phi\sin\phi\,d\phi$",
       r"$=128\pi\cdot\dfrac{1-\cos^6\frac\pi6}{6}=\dfrac{64\pi}{3}\Big(1-\dfrac{27}{64}\Big)=\dfrac{37\pi}{3}$ → $\bar z=\dfrac{37\pi/3}{14\pi/3}=\dfrac{37}{14}$"],
  check=_c)


def _c():
    ell = lambda T: 2/mp.sqrt(mp.cos(T)**2 + 4*mp.sin(T)**2)
    cyl = (mp.quad(lambda T: mp.quad(lambda Rr: mp.sqrt(3)*Rr*mp.sin(T)*Rr, [0, ell(T)]), [0, mp.pi/2])
           + mp.quad(lambda T: mp.quad(lambda Rr: mp.sqrt(4 - Rr*Rr)*Rr, [ell(T), 2]), [0, mp.pi/2]))
    sph = mp.quad(lambda T: mp.mpf(8)/3*mp.cos(mp.acot(mp.sqrt(3)*mp.sin(T))), [0, mp.pi/2])
    assert abs(cyl - 8*mp.pi/9) < 1e-8 and abs(sph - 8*mp.pi/9) < 1e-10
    uq = symbols('uq', positive=True)
    assert EQ(sqrt(3)*integrate(1/sqrt(4 - 3*uq**2), (uq, 0, 1)), pi/3)
P(id="4-99", ch=15, sec="15.8", type="15-sphconv", src="2025 중간 10번 유형",
  q=r"(a) 다음 적분이 나타내는 입체 $E$를 설명하고 구면좌표 적분으로 바꾸어라.<br>(b) (a)의 값을 구하라. $$\int_0^{\pi/2}\!\!\int_0^{\frac{2}{\sqrt{\cos^2\theta+4\sin^2\theta}}}\!\!\int_0^{\sqrt3\,r\sin\theta}r\,dz\,dr\,d\theta+\int_0^{\pi/2}\!\!\int_{\frac{2}{\sqrt{\cos^2\theta+4\sin^2\theta}}}^{2}\!\!\int_0^{\sqrt{4-r^2}}r\,dz\,dr\,d\theta$$",
  hint=r"윗면은 $z=\sqrt3\,y$와 $z=\sqrt{4-r^2}$ 중 낮은 쪽. 두 면은 $3y^2=4-x^2-y^2 \iff x^2+4y^2=4$에서 만나요. 구면좌표로 $z\le\sqrt3y \iff \cot\phi\le\sqrt3\sin\theta$.",
  ans=r"(a) $E=\{x\ge0,\ y\ge0,\ 0\le z\le\sqrt3\,y,\ x^2+y^2+z^2\le4\}$, $\displaystyle\int_0^{\pi/2}\!\!\int_{\cot^{-1}(\sqrt3\sin\theta)}^{\pi/2}\!\!\int_0^2\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$  (b) $\dfrac{8\pi}{9}$",
  sol=[r"(a) 첫 적분: 타원 $x^2+4y^2=4$ 안쪽에서 $0\le z\le\sqrt3\,y$, 둘째: 타원 바깥·원 $r=2$ 안에서 $0\le z\le\sqrt{4-r^2}$ → $E$: 제1팔분공간, 반지름 2인 구 안, 평면 $z=\sqrt3y$ 아래",
       r"구면좌표: $\rho\cos\phi\le\sqrt3\rho\sin\phi\sin\theta \iff \cot\phi\le\sqrt3\sin\theta \iff \phi\ge\cot^{-1}(\sqrt3\sin\theta)$, 그리고 $\phi\le\tfrac\pi2$, $\rho\le2$",
       r"(b) $\displaystyle\int_0^{\pi/2}\frac83\cos\big(\cot^{-1}(\sqrt3\sin\theta)\big)d\theta$, $\cos(\cot^{-1}w)=\dfrac{w}{\sqrt{1+w^2}}$",
       r"$=\dfrac83\displaystyle\int_0^{\pi/2}\frac{\sqrt3\sin\theta}{\sqrt{4-3\cos^2\theta}}d\theta\overset{u=\cos\theta}{=}\frac83\sqrt3\int_0^1\frac{du}{\sqrt{4-3u^2}}=\frac83\Big[\sin^{-1}\frac{\sqrt3u}{2}\Big]_0^1=\frac83\cdot\frac\pi3=\frac{8\pi}9$"],
  check=_c)


def _c():
    I = integrate(rho*rho**2*sin(ph), (rho, 0, 2*cos(ph)), (ph, 0, pi/2), (th, 0, 2*pi))
    assert EQ(I, 8*pi/5)
    num = 2*mp.pi*mp.quad(lambda Rr: mp.quad(lambda Z: mp.sqrt(Rr*Rr + Z*Z)*Rr,
                                             [1 - mp.sqrt(1 - Rr*Rr), 1 + mp.sqrt(1 - Rr*Rr)]), [0, 1])
    assert abs(num - 8*mp.pi/5) < 1e-7
P(id="4-100", ch=15, sec="15.8", type="15-sphconv", src="2022 중간 블럭1 10번 유형 (직교좌표 → 구면좌표)",
  q=r"구면좌표로 바꾸어 계산하라. $$\int_{-1}^{1}\!\!\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\!\!\int_{1-\sqrt{1-x^2-y^2}}^{1+\sqrt{1-x^2-y^2}}\sqrt{x^2+y^2+z^2}\,dz\,dy\,dx$$",
  hint=r"$z=1\pm\sqrt{1-x^2-y^2} \iff x^2+y^2+(z-1)^2=1$ → 영역은 중심 $(0,0,1)$, 반지름 $1$인 구 → $\rho\le2\cos\phi$, $0\le\phi\le\tfrac\pi2$.",
  ans=r"$\dfrac{8\pi}{5}$",
  sol=[r"영역: $x^2+y^2+z^2\le2z \iff \rho^2\le2\rho\cos\phi \iff \rho\le2\cos\phi$ ($0\le\phi\le\tfrac\pi2$)",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{2\cos\phi}\rho\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\int_0^{\pi/2}4\cos^4\phi\sin\phi\,d\phi$",
       r"$=8\pi\Big[-\dfrac{\cos^5\phi}{5}\Big]_0^{\pi/2}=\dfrac{8\pi}{5}$"],
  check=_c)


def _c():
    assert EQ(4*pi*integrate(rho**2*exp(-rho**2), (rho, 0, oo)), pi**R(3, 2))
    assert EQ(integrate(rho**2*exp(-rho**2), (rho, 0, oo)), sqrt(pi)/4)
    assert EQ(4*pi*integrate(rho**3*exp(-rho**2), (rho, 0, oo)), 2*pi)
P(id="4-101", ch=15, sec="15.8", type="15-sph", src="교재 15.8 심화형 (공간 전체의 가우스 적분)",
  q=r"(a) $\displaystyle\iiint_{\mathbb R^3}e^{-(x^2+y^2+z^2)}dV$를 $\Big(\int_{-\infty}^\infty e^{-x^2}dx\Big)^3$으로 계산하라. (4-83 결과 이용)<br>(b) 같은 적분을 구면좌표로 쓰고 비교해 $\displaystyle\int_0^\infty\rho^2e^{-\rho^2}d\rho$를 구하라.<br>(c) $\displaystyle\iiint_{\mathbb R^3}\sqrt{x^2+y^2+z^2}\,e^{-(x^2+y^2+z^2)}dV$를 구하라.",
  hint=r"구면좌표에서 $\theta,\phi$ 적분은 $\int_0^{2\pi}\!\int_0^\pi\sin\phi\,d\phi\,d\theta=4\pi$. (c)는 $\int_0^\infty\rho^3e^{-\rho^2}d\rho$를 $u=\rho^2$로 치환.",
  ans=r"(a) $\pi^{3/2}$  (b) $\dfrac{\sqrt\pi}{4}$  (c) $2\pi$",
  sol=[r"(a) $e^{-(x^2+y^2+z^2)}=e^{-x^2}e^{-y^2}e^{-z^2}$ → $(\sqrt\pi)^3=\pi^{3/2}$",
       r"(b) $\displaystyle\int_0^{2\pi}\!\!\int_0^\pi\!\!\int_0^\infty e^{-\rho^2}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=4\pi\int_0^\infty\rho^2e^{-\rho^2}d\rho=\pi^{3/2}$ → $\dfrac{\sqrt\pi}4$",
       r"(c) $4\pi\displaystyle\int_0^\infty\rho^3e^{-\rho^2}d\rho\overset{u=\rho^2}{=}4\pi\cdot\frac12\int_0^\infty ue^{-u}du=2\pi$"],
  check=_c)


# ───────── 15.9 변수변환 (추가) ─────────
def _c():
    Juv = Matrix([[diff(x*y, x), diff(x*y, y)], [diff(y/x, x), diff(y/x, y)]]).det()
    assert simplify(Juv - 2*y/x) == 0
    assert EQ(integrate(1/(2*v), (v, 1, 2), (u, 1, 3)), log(2))
    assert integrate(u*v/(2*v), (v, 1, 2), (u, 1, 3)) == 2
    up, vp = symbols('up vp', positive=True)
    xs, ys = sqrt(up/vp), sqrt(up*vp)                        # 역변환 (u, v > 0)
    assert simplify(xs*ys - up) == 0 and simplify(ys/xs - vp) == 0
    assert simplify(Matrix([[diff(xs, up), diff(xs, vp)], [diff(ys, up), diff(ys, vp)]]).det() - 1/(2*vp)) == 0
    lo = lambda X: max(X, 1/X)
    hi = lambda X: min(2*X, 3/X)
    pts = [1/mp.sqrt(2), 1, mp.sqrt(mp.mpf(3)/2), mp.sqrt(3)]
    area = q2(lambda X, Y: 1, None, None, lo, hi, xpts=pts)
    I = q2(lambda X, Y: Y*Y, None, None, lo, hi, xpts=pts)
    assert abs(area - mp.log(2)) < 1e-10 and abs(I - 2) < 1e-10
P(id="4-124", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 쌍곡선·직선 영역",
  q=r"$R$ 은 제1사분면에서 곡선 $xy=1,\ xy=3$ 과 직선 $y=x,\ y=2x$ 로 둘러싸인 영역이다. 변환 $u=xy,\ v=\dfrac yx$ 를 이용하여<br>(a) $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 $u,v$ 로 나타내고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하라.<br>(b) $R$ 의 넓이를 구하라.  (c) $\displaystyle\iint_Ry^2\,dA$ 를 구하라.",
  hint=r"역변환을 구하지 않아도 $\dfrac{\partial(x,y)}{\partial(u,v)}=1\Big/\dfrac{\partial(u,v)}{\partial(x,y)}$ 예요. (c)에서는 $y^2=xy\cdot\dfrac yx=uv$",
  ans=r"(a) $\dfrac{1}{2v}$, $\ S=\{1\le u\le3,\ 1\le v\le2\}$  (b) $\ln2$  (c) $2$",
  sol=[r"(a) $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}y&x\\-\dfrac{y}{x^2}&\dfrac1x\end{vmatrix}=\dfrac yx+\dfrac yx=\dfrac{2y}{x}=2v$ → $\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac1{2v}$",
       r"경계: $xy=1,\ 3$ → $u=1,\ 3$;  $y=x,\ y=2x$ → $v=1,\ 2$ → $S=\{1\le u\le3,\ 1\le v\le2\}$ (직사각형)",
       r"(b) $\displaystyle\iint_RdA=\int_1^3\!\!\int_1^2\frac1{2v}\,dv\,du=2\cdot\frac{\ln2}{2}=\ln2$",
       r"(c) $y^2=uv$ → $\displaystyle\iint_Ry^2\,dA=\int_1^3\!\!\int_1^2uv\cdot\frac1{2v}\,dv\,du=\int_1^3\frac u2\,du=\frac12\cdot\frac{9-1}{2}=2$"],
  check=_c)


def _c():
    assert Matrix([[3, 0], [0, 2]]).det() == 6
    assert EQ(integrate(6*r, (r, 0, 1), (th, 0, 2*pi)), 6*pi)
    assert EQ(integrate(54*r**2*cos(th)**2*r, (r, 0, 1), (th, 0, 2*pi)), 27*pi/2)
    assert expand(36 - 4*(3*u)**2 - 9*(2*v)**2 - 36*(1 - u**2 - v**2)) == 0
    assert EQ(integrate(36*sqrt(1 - r**2)*r, (r, 0, 1), (th, 0, 2*pi)), 24*pi)
    hy = lambda X: 2*mp.sqrt(max(0, 1 - X*X/9))
    I2 = mp.quad(lambda X: X*X*2*hy(X), [-3, 3])
    I3 = mp.quad(lambda X: mp.quad(lambda Y: mp.sqrt(max(0, 36 - 4*X*X - 9*Y*Y)), [-hy(X), hy(X)]), [-3, 3])
    assert abs(I2 - 27*mp.pi/2) < 1e-8 and abs(I3 - 24*mp.pi) < 1e-6
P(id="4-125", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 타원 영역 (+ 극좌표)",
  q=r"$R$ 이 타원 영역 $\dfrac{x^2}{9}+\dfrac{y^2}{4}\le1$ 일 때 변환 $x=3u,\ y=2v$ 를 이용하여 다음을 구하라.<br>(a) $R$ 의 넓이  (b) $\displaystyle\iint_Rx^2\,dA$  (c) $\displaystyle\iint_R\sqrt{36-4x^2-9y^2}\,dA$",
  hint=r"$\dfrac{\partial(x,y)}{\partial(u,v)}=6$ 이고 $R$ 은 단위원판 $u^2+v^2\le1$ 로 바뀌어요. 그다음은 극좌표 $u=r\cos\theta,\ v=r\sin\theta$",
  ans=r"(a) $6\pi$  (b) $\dfrac{27\pi}{2}$  (c) $24\pi$",
  sol=[r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}3&0\\0&2\end{vmatrix}=6$, $\ \dfrac{x^2}9+\dfrac{y^2}4\le1\iff u^2+v^2\le1$ (단위원판 $S$)",
       r"(a) $\displaystyle\iint_RdA=\iint_S6\,du\,dv=6\pi$ (타원 넓이 $\pi ab$ 와 같아요)",
       r"(b) $$\begin{aligned}&\iint_Rx^2\,dA=\iint_S54u^2\,du\,dv\\&=54\int_0^{2\pi}\cos^2\theta\,d\theta\int_0^1r^3\,dr\\&=54\cdot\pi\cdot\frac14=\frac{27\pi}{2}\end{aligned}$$",
       r"(c) $36-4x^2-9y^2=36(1-u^2-v^2)$ 이므로 $$\begin{aligned}&\iint_R\sqrt{36-4x^2-9y^2}\,dA\\&=36\iint_S\sqrt{1-u^2-v^2}\,du\,dv\\&=36\int_0^{2\pi}\!\!\int_0^1\sqrt{1-r^2}\,r\,dr\,d\theta\\&=36\cdot2\pi\cdot\frac13=24\pi\end{aligned}$$"],
  check=_c)


def _c():
    xs, ys = (u + v)/2, (v - u)/2                            # u=x-y, v=x+y 의 역변환
    J = Matrix([[diff(xs, u), diff(xs, v)], [diff(ys, u), diff(ys, v)]]).det()
    assert J == R(1, 2)
    I = integrate(cos(u/v)*R(1, 2), (u, -v, v), (v, 1, 2))
    assert EQ(I, R(3, 2)*sin(1))
    num = mp.quad(lambda X: mp.quad(lambda Y: mp.cos((X - Y)/(X + Y)), [max(0, 1 - X), 2 - X]), [0, 1, 2])
    assert abs(num - mp.mpf(3)/2*mp.sin(1)) < 1e-10
P(id="4-126", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 사다리꼴 영역",
  q=r"$R$ 은 네 점 $(1,0),\ (2,0),\ (0,2),\ (0,1)$ 을 꼭짓점으로 하는 사다리꼴이다. 변환 $u=x-y,\ v=x+y$ 를 이용하여 $\displaystyle\iint_R\cos\Big(\frac{x-y}{x+y}\Big)\,dA$ 를 구하라.",
  hint=r"네 변 $x+y=1,\ x+y=2,\ x=0,\ y=0$ 을 $u,v$ 로 바꾸면 $v=1,\ v=2,\ u=-v,\ u=v$. $u$ 로 먼저 적분하면 $\cos\dfrac uv$ 가 바로 적분돼요.",
  ans=r"$\dfrac32\sin1$",
  sol=[r"$x=\dfrac{u+v}{2},\ y=\dfrac{v-u}{2}$ → $\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\frac12&\frac12\\-\frac12&\frac12\end{vmatrix}=\dfrac12$",
       r"경계: $x+y=1,\ 2$ → $v=1,\ 2$;  $x=0$ → $u=-v$;  $y=0$ → $u=v$ → $S:\ 1\le v\le2,\ -v\le u\le v$ (직사각형이 아니에요)",
       r"$$\begin{aligned}&\iint_R\cos\Big(\frac{x-y}{x+y}\Big)dA\\&=\int_1^2\!\!\int_{-v}^{v}\frac12\cos\frac uv\,du\,dv\\&=\int_1^2\frac12\Big[v\sin\frac uv\Big]_{u=-v}^{u=v}dv\\&=\int_1^2v\sin1\,dv=\frac32\sin1\end{aligned}$$"],
  check=_c)

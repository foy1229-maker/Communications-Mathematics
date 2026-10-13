"""2단계 · 표준 추가분 — Ch.15 중적분: 2-72 ~ 2-101"""
from bank_lib import *
from sympy import atan, tan as tan_, sec


# ───────── 15.1 ─────────
def _c():
    assert EQ(integrate(integrate(x/y + y/x, (y, 1, 3)), (x, 1, 2)), R(3, 2)*log(3) + 4*log(2))
P(id="2-72", ch=15, sec="15.1", type="15-rect", src="과제 15.1 #21 유형",
  q=r"$\displaystyle\int_1^2\!\!\int_1^3\Big(\frac{x}{y}+\frac{y}{x}\Big)\,dy\,dx$를 계산하라.",
  hint=r"$y$로 적분할 때 $x$는 상수: $\int\frac{x}{y}dy=x\ln y$, $\int\frac{y}{x}dy=\frac{y^2}{2x}$",
  ans=r"$\dfrac32\ln3+4\ln2$",
  sol=[r"안쪽: $\Big[x\ln y+\dfrac{y^2}{2x}\Big]_1^3=x\ln3+\dfrac{4}{x}$",
       r"바깥: $\displaystyle\int_1^2\Big(x\ln3+\frac4x\Big)dx=\frac32\ln3+4\ln2$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(1 + x**2*sin(y) + y**2*sin(x), (y, -pi, pi)), (x, -pi, pi)), 4*pi**2)
P(id="2-73", ch=15, sec="15.1", type="15-rect", src="과제 15.1 #55 유형 (대칭)",
  q=r"대칭성을 이용해 $\displaystyle\iint_R\big(1+x^2\sin y+y^2\sin x\big)\,dA$를 구하라. 단, $R=[-\pi,\pi]\times[-\pi,\pi]$.",
  hint=r"$x^2\sin y$는 $y$에 대해 홀함수, $y^2\sin x$는 $x$에 대해 홀함수예요.",
  ans=r"$4\pi^2$",
  sol=[r"$\displaystyle\iint_R x^2\sin y\,dA=\int_{-\pi}^{\pi}x^2dx\cdot\int_{-\pi}^{\pi}\sin y\,dy=0$ (홀함수)",
       r"같은 이유로 $\displaystyle\iint_R y^2\sin x\,dA=0$",
       r"남는 것: $\displaystyle\iint_R1\,dA=(2\pi)^2=4\pi^2$"],
  check=_c)


# ───────── 15.2 ─────────
def _c():
    assert EQ(integrate(integrate(y/(x**2 + 1), (y, 0, sqrt(x))), (x, 0, 2)), log(5)/4)
P(id="2-74", ch=15, sec="15.2", type="15-general", src="과제 15.2 #11 유형",
  q=r"$D=\{(x,y)\mid 0\le x\le2,\ 0\le y\le\sqrt x\}$일 때 $\displaystyle\iint_D\frac{y}{x^2+1}\,dA$를 계산하라.",
  hint=r"$y$로 먼저: $\int_0^{\sqrt x}y\,dy=\frac{x}{2}$. 그다음 $u=x^2+1$",
  ans=r"$\dfrac{\ln5}{4}$",
  sol=[r"$\displaystyle\int_0^{\sqrt x}\frac{y}{x^2+1}dy=\frac{x}{2(x^2+1)}$",
       r"$\displaystyle\int_0^2\frac{x}{2(x^2+1)}dx=\frac14\Big[\ln(x^2+1)\Big]_0^2=\frac{\ln5}{4}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(x + 2*y, (y, x**3, x)), (x, 0, 1)), R(34, 105))
P(id="2-75", ch=15, sec="15.2", type="15-general", src="과제 15.2 #27 유형",
  q=r"1사분면에서 곡선 $y=x^3$과 직선 $y=x$로 둘러싸인 영역 $D$에서 $\displaystyle\iint_D(x+2y)\,dA$를 계산하라.",
  hint=r"$0\le x\le1$에서 $x^3\le y\le x$",
  ans=r"$\dfrac{34}{105}$",
  sol=[r"안쪽: $\Big[xy+y^2\Big]_{x^3}^{x}=(x^2+x^2)-(x^4+x^6)=2x^2-x^4-x^6$",
       r"$\displaystyle\int_0^1(2x^2-x^4-x^6)dx=\frac23-\frac15-\frac17=\frac{34}{105}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(x*y, (y, 1, 4 - x)), (x, 1, 3)), R(16, 3))
P(id="2-76", ch=15, sec="15.2", type="15-general", src="과제 15.2 #33 유형",
  q=r"곡면 $z=xy$ 아래, 꼭짓점이 $(1,1),\ (3,1),\ (1,3)$인 삼각형 위에 있는 입체의 부피를 구하라.",
  hint=r"빗변은 $x+y=4$. $1\le x\le3,\ 1\le y\le4-x$",
  ans=r"$\dfrac{16}{3}$",
  sol=[r"$V=\displaystyle\int_1^3\!\!\int_1^{4-x}xy\,dy\,dx=\int_1^3\frac{x\big((4-x)^2-1\big)}{2}dx$",
       r"$=\dfrac12\displaystyle\int_1^3(15x-8x^2+x^3)\,dx=\dfrac12\Big[\tfrac{15x^2}{2}-\tfrac{8x^3}{3}+\tfrac{x^4}{4}\Big]_1^3$",
       r"$=\dfrac12\Big(\dfrac{63}{4}-\dfrac{61}{12}\Big)=\dfrac12\cdot\dfrac{128}{12}=\dfrac{16}{3}$"],
  check=_c)


def _c():
    A1 = integrate(pi/4 - atan(x), (x, 0, 1))
    A2 = integrate(tan_(y), (y, 0, pi/4))
    assert EQ(A1, log(2)/2) and EQ(A2, log(2)/2)
    f = x*y + 1
    I1 = integrate(integrate(f, (y, atan(x), pi/4)), (x, 0, 1))
    I2 = integrate(integrate(f, (x, 0, tan_(y))), (y, 0, pi/4))
    assert abs(float(N(I1 - I2))) < 1e-10
P(id="2-77", ch=15, sec="15.2", type="15-order", src="과제 15.2 #59 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_{\arctan x}^{\pi/4}f(x,y)\,dy\,dx$의 적분 영역을 그리고 적분 순서를 바꾸어라. 또 $f=1$일 때 두 적분이 같은 값(넓이)을 주는지 확인하라.",
  hint=r"$y=\arctan x \iff x=\tan y$. 영역은 곡선 $x=\tan y$의 왼쪽",
  ans=r"$\displaystyle\int_0^{\pi/4}\!\!\int_0^{\tan y}f(x,y)\,dx\,dy$,  넓이 $\dfrac12\ln2$",
  sol=[r"영역: $0\le x\le1$, 곡선 $y=\arctan x$와 직선 $y=\tfrac\pi4$ 사이",
       r"$y$ 기준: $0\le y\le\tfrac\pi4$, $0\le x\le\tan y$",
       r"$f=1$: $\displaystyle\int_0^{\pi/4}\tan y\,dy=\Big[-\ln\cos y\Big]_0^{\pi/4}=\ln\sqrt2=\frac12\ln2$",
       r"원래 순서: $\displaystyle\int_0^1\Big(\frac\pi4-\arctan x\Big)dx=\frac\pi4-\Big(\frac\pi4-\frac12\ln2\Big)=\frac12\ln2$ ✓"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(exp(x**2), (y, 0, 2*x)), (x, 0, 1)), E - 1)
P(id="2-78", ch=15, sec="15.2", type="15-order", src="과제 15.2 #61 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^2\!\!\int_{y/2}^{1}e^{x^2}\,dx\,dy$를 계산하라.",
  hint=r"$\tfrac y2\le x\le1 \iff 0\le y\le2x$ ($0\le x\le1$)",
  ans=r"$e-1$",
  sol=[r"영역: $0\le y\le2,\ \tfrac y2\le x\le1$ $\iff$ $0\le x\le1,\ 0\le y\le2x$",
       r"$\displaystyle\int_0^1\!\!\int_0^{2x}e^{x^2}\,dy\,dx=\int_0^12xe^{x^2}\,dx$",
       r"$=\Big[e^{x^2}\Big]_0^1=e-1$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(exp(x**4), (y, 0, x**3)), (x, 0, 2)), (exp(16) - 1)/4)
P(id="2-79", ch=15, sec="15.2", type="15-order", src="강의 15.2 (순서 바꾸기) 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^8\!\!\int_{\sqrt[3]{y}}^{2}e^{x^4}\,dx\,dy$를 계산하라.",
  hint=r"$\sqrt[3]y\le x \iff y\le x^3$. 바꾼 뒤 $\int x^3e^{x^4}dx$",
  ans=r"$\dfrac{e^{16}-1}{4}$",
  sol=[r"영역: $0\le y\le8,\ \sqrt[3]y\le x\le2$ $\iff$ $0\le x\le2,\ 0\le y\le x^3$",
       r"$\displaystyle\int_0^2\!\!\int_0^{x^3}e^{x^4}\,dy\,dx=\int_0^2x^3e^{x^4}\,dx$",
       r"$=\Big[\tfrac14e^{x^4}\Big]_0^2=\dfrac{e^{16}-1}{4}$"],
  check=_c)


# ───────── 15.3 ─────────
def _c():
    assert EQ(integrate(integrate(cos(r**2)*r, (r, 0, 3)), (th, 0, pi)), pi*sin(9)/2)
P(id="2-80", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #13 유형",
  q=r"$D$가 반원 $y=\sqrt{9-x^2}$과 $x$축으로 둘러싸인 영역일 때 $\displaystyle\iint_D\cos(x^2+y^2)\,dA$를 계산하라.",
  hint=r"위쪽 반원판: $0\le r\le3,\ 0\le\theta\le\pi$. $\int r\cos(r^2)dr$은 $u=r^2$",
  ans=r"$\dfrac{\pi}{2}\sin9$",
  sol=[r"$\displaystyle\int_0^{\pi}\!\!\int_0^3\cos(r^2)\,r\,dr\,d\theta=\pi\Big[\tfrac12\sin(r^2)\Big]_0^3$",
       r"$=\dfrac\pi2\sin9$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(th*r, (r, 1, 3)), (th, 0, pi/4)), pi**2/8)
P(id="2-81", ch=15, sec="15.3", type="15-polar", src="복습 15.1–3 심화1 유형",
  q=r"$D=\{(x,y)\mid 1\le x^2+y^2\le9,\ 0\le y\le x\}$일 때 $\displaystyle\iint_D\arctan\frac{y}{x}\,dA$를 계산하라.",
  hint=r"극좌표에서 $\arctan\frac yx=\theta$. $0\le y\le x$는 $0\le\theta\le\frac\pi4$",
  ans=r"$\dfrac{\pi^2}{8}$",
  sol=[r"$D$: $1\le r\le3,\ 0\le\theta\le\tfrac\pi4$, 피적분함수 $=\theta$",
       r"$\displaystyle\int_0^{\pi/4}\!\!\int_1^3\theta\,r\,dr\,d\theta=\Big[\tfrac{\theta^2}{2}\Big]_0^{\pi/4}\cdot\Big[\tfrac{r^2}{2}\Big]_1^3=\frac{\pi^2}{32}\cdot4=\frac{\pi^2}{8}$"],
  check=_c)


def _c():
    V = integrate(integrate((sqrt(8 - r**2) - r)*r, (r, 0, 2)), (th, 0, 2*pi))
    assert EQ(V, 32*pi/3*(sqrt(2) - 1))
P(id="2-82", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #35 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=8$ 아래에 있는 입체의 부피를 극좌표 이중적분으로 구하라.",
  hint=r"교선: $r^2+r^2=8 \Rightarrow r=2$. 높이 $=\sqrt{8-r^2}-r$",
  ans=r"$\dfrac{32\pi}{3}(\sqrt2-1)$",
  sol=[r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^2\big(\sqrt{8-r^2}-r\big)r\,dr\,d\theta$",
       r"$\displaystyle\int_0^2r\sqrt{8-r^2}\,dr=\Big[-\tfrac13(8-r^2)^{3/2}\Big]_0^2=\frac{16\sqrt2-8}{3}$,  $\displaystyle\int_0^2r^2dr=\frac83$",
       r"$V=2\pi\cdot\dfrac{16\sqrt2-16}{3}=\dfrac{32\pi}{3}(\sqrt2-1)$"],
  check=_c)


def _c():
    A = integrate(integrate(r, (r, 1 + cos(th), 3*cos(th))), (th, -pi/3, pi/3))
    assert EQ(A, pi)
P(id="2-83", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #17 유형 (두 곡선 사이 넓이)",
  q=r"원 $r=3\cos\theta$의 안쪽이면서 심장형 $r=1+\cos\theta$의 바깥쪽인 영역의 넓이를 구하라.",
  hint=r"교점: $3\cos\theta=1+\cos\theta \Rightarrow \cos\theta=\tfrac12$. $A=\iint r\,dr\,d\theta$, $r$은 $1+\cos\theta$부터 $3\cos\theta$까지",
  ans=r"$\pi$",
  sol=[r"교점 $\theta=\pm\tfrac\pi3$",
       r"$A=\displaystyle\int_{-\pi/3}^{\pi/3}\!\!\int_{1+\cos\theta}^{3\cos\theta}r\,dr\,d\theta=\int_0^{\pi/3}\big(9\cos^2\theta-(1+\cos\theta)^2\big)d\theta$",
       r"$=\displaystyle\int_0^{\pi/3}(8\cos^2\theta-2\cos\theta-1)\,d\theta=\Big[3\theta+2\sin2\theta-2\sin\theta\Big]_0^{\pi/3}$",
       r"$=\pi+\sqrt3-\sqrt3=\pi$"],
  check=_c)


def _c():
    cart = (integrate(integrate(x, (y, sqrt(1 - x**2), x)), (x, 1/sqrt(2), 1))
            + integrate(integrate(x, (y, 0, x)), (x, 1, sqrt(2)))
            + integrate(integrate(x, (y, 0, sqrt(4 - x**2))), (x, sqrt(2), 2)))
    pol = integrate(integrate(r*cos(th)*r, (r, 1, 2)), (th, 0, pi/4))
    assert EQ(pol, 7*sqrt(2)/6) and EQ(cart, 7*sqrt(2)/6)
P(id="2-84", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #49 유형",
  q=r"극좌표를 이용해 다음 세 적분의 합을 하나의 이중적분으로 바꾸고 계산하라. $$\int_{1/\sqrt2}^{1}\!\int_{\sqrt{1-x^2}}^{x}x\,dy\,dx+\int_1^{\sqrt2}\!\int_0^{x}x\,dy\,dx+\int_{\sqrt2}^{2}\!\int_0^{\sqrt{4-x^2}}x\,dy\,dx$$",
  hint=r"세 영역을 그려 보면 합쳐서 $1\le r\le2,\ 0\le\theta\le\frac\pi4$ (직선 $y=x$와 $x$축 사이 고리)",
  ans=r"$\displaystyle\int_0^{\pi/4}\!\!\int_1^2 r^2\cos\theta\,dr\,d\theta=\frac{7\sqrt2}{6}$",
  sol=[r"경계: 원 $r=1$ (아래쪽 첫 적분), 원 $r=2$ (셋째 적분), 직선 $y=x$ ($\theta=\tfrac\pi4$), $x$축 ($\theta=0$)",
       r"합친 영역: $1\le r\le2,\ 0\le\theta\le\tfrac\pi4$",
       r"$\displaystyle\int_0^{\pi/4}\!\!\int_1^2(r\cos\theta)\,r\,dr\,d\theta=\sin\frac\pi4\cdot\frac{8-1}{3}=\frac{\sqrt2}{2}\cdot\frac73=\frac{7\sqrt2}{6}$"],
  check=_c)


def _c():
    m = integrate(integrate(r*r, (r, 0, 2*cos(th))), (th, -pi/2, pi/2))
    My = integrate(integrate(r*cos(th)*r*r, (r, 0, 2*cos(th))), (th, -pi/2, pi/2))
    Mx = integrate(integrate(r*sin(th)*r*r, (r, 0, 2*cos(th))), (th, -pi/2, pi/2))
    assert EQ(m, R(32, 9)) and EQ(My, R(64, 15)) and EQ(Mx, 0) and EQ(My/m, R(6, 5))
P(id="2-85", ch=15, sec="15.3", type="15-mass", src="2025 중간 1번 유형",
  q=r"원판 $x^2+y^2\le2x$ 모양의 얇은 판의 밀도가 $\rho(x,y)=\sqrt{x^2+y^2}$일 때, 판의 질량과 질량중심을 구하라.",
  hint=r"$x^2+y^2\le2x \iff r\le2\cos\theta,\ -\tfrac\pi2\le\theta\le\tfrac\pi2$. $\int_{-\pi/2}^{\pi/2}\cos^3\theta\,d\theta=\tfrac43$, $\int_{-\pi/2}^{\pi/2}\cos^5\theta\,d\theta=\tfrac{16}{15}$",
  ans=r"질량 $\dfrac{32}{9}$,  질량중심 $\left(\dfrac65,\ 0\right)$",
  sol=[r"$m=\displaystyle\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}r\cdot r\,dr\,d\theta=\frac83\int_{-\pi/2}^{\pi/2}\cos^3\theta\,d\theta=\frac83\cdot\frac43=\frac{32}{9}$",
       r"$M_y=\displaystyle\iint x\rho\,dA=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}r^3\cos\theta\,dr\,d\theta=4\int_{-\pi/2}^{\pi/2}\cos^5\theta\,d\theta=\frac{64}{15}$",
       r"$x$축 대칭이라 $\bar y=0$,  $\bar x=\dfrac{64/15}{32/9}=\dfrac65$",
       r"질량중심 $\left(\dfrac65,0\right)$ — 원판 중심 $(1,0)$보다 밀도가 큰 바깥쪽으로 치우쳐요."],
  check=_c)


def _c():
    m = integrate(integrate(r*cos(th)*r*sin(th)*r, (r, 0, 2)), (th, 0, pi/2))
    My = integrate(integrate(r*cos(th)*(r*cos(th)*r*sin(th))*r, (r, 0, 2)), (th, 0, pi/2))
    Mx = integrate(integrate(r*sin(th)*(r*cos(th)*r*sin(th))*r, (r, 0, 2)), (th, 0, pi/2))
    assert EQ(m, 2) and EQ(My/m, R(16, 15)) and EQ(Mx/m, R(16, 15))
P(id="2-86", ch=15, sec="15.3", type="15-mass", src="2022 중간(블럭1) 8번 유형",
  q=r"1사분면의 사분원판 $x^2+y^2\le4,\ x\ge0,\ y\ge0$ 모양의 판의 밀도가 $\rho(x,y)=xy$일 때 질량과 질량중심을 구하라.",
  hint=r"$\rho=r^2\cos\theta\sin\theta$. $\int_0^{\pi/2}\cos^2\theta\sin\theta\,d\theta=\tfrac13$",
  ans=r"질량 $2$,  질량중심 $\left(\dfrac{16}{15},\ \dfrac{16}{15}\right)$",
  sol=[r"$m=\displaystyle\int_0^{\pi/2}\!\!\int_0^2r^2\cos\theta\sin\theta\cdot r\,dr\,d\theta=\frac12\cdot\frac{2^4}{4}=2$",
       r"$M_y=\displaystyle\iint x\rho\,dA=\int_0^{\pi/2}\cos^2\theta\sin\theta\,d\theta\int_0^2r^4dr=\frac13\cdot\frac{32}{5}=\frac{32}{15}$",
       r"$\bar x=\dfrac{32/15}{2}=\dfrac{16}{15}$, 직선 $y=x$에 대해 대칭이라 $\bar y=\dfrac{16}{15}$"],
  check=_c)


# ───────── 15.6 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(2*x, (z, 0, y)), (x, 0, sqrt(4 - y**2))), (y, 0, 2)), 4)
P(id="2-87", ch=15, sec="15.6", type="15-triple", src="과제 15.6 #17 유형",
  q=r"$E=\{(x,y,z)\mid 0\le y\le2,\ 0\le x\le\sqrt{4-y^2},\ 0\le z\le y\}$일 때 $\displaystyle\iiint_E2x\,dV$를 계산하라.",
  hint=r"$z$ → $x$ → $y$ 순서로 그대로 적분하면 돼요.",
  ans=r"$4$",
  sol=[r"$\displaystyle\int_0^y2x\,dz=2xy$",
       r"$\displaystyle\int_0^{\sqrt{4-y^2}}2xy\,dx=y(4-y^2)$",
       r"$\displaystyle\int_0^2(4y-y^3)\,dy=8-4=4$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(2*x - y, (x, 0, y - z)), (y, 0, z**2)), (z, 0, 2)), R(16, 15))
P(id="2-88", ch=15, sec="15.6", type="15-triple", src="과제 15.6 #5 유형",
  q=r"$\displaystyle\int_0^2\!\!\int_0^{z^2}\!\!\int_0^{y-z}(2x-y)\,dx\,dy\,dz$를 계산하라.",
  hint=r"안쪽: $\Big[x^2-xy\Big]_0^{y-z}=(y-z)(y-z-y)$",
  ans=r"$\dfrac{16}{15}$",
  sol=[r"안쪽: $(y-z)^2-y(y-z)=-z(y-z)=z^2-yz$",
       r"가운데: $\displaystyle\int_0^{z^2}(z^2-yz)\,dy=z^4-\frac{z^5}{2}$",
       r"바깥: $\displaystyle\int_0^2\Big(z^4-\frac{z^5}{2}\Big)dz=\frac{32}{5}-\frac{16}{3}=\frac{16}{15}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(1, (z, 0, 1 - x)), (x, y**2, 1)), (y, -1, 1)), R(8, 15))
P(id="2-89", ch=15, sec="15.6", type="15-triple", src="강의 15.6 (부피) 유형",
  q=r"포물기둥 $x=y^2$과 평면 $z=0$, $x+z=1$로 둘러싸인 입체의 부피를 구하라.",
  hint=r"밑면: $-1\le y\le1,\ y^2\le x\le1$, 높이 $0\le z\le1-x$",
  ans=r"$\dfrac{8}{15}$",
  sol=[r"$V=\displaystyle\int_{-1}^{1}\!\!\int_{y^2}^{1}\!\!\int_0^{1-x}dz\,dx\,dy=\int_{-1}^1\Big[x-\tfrac{x^2}{2}\Big]_{y^2}^1dy$",
       r"$=\displaystyle\int_{-1}^1\Big(\frac12-y^2+\frac{y^4}{2}\Big)dy=1-\frac23+\frac15=\frac{8}{15}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(z, (x, 0, 1 - z)), (y, 0, 1 - z)), (z, 0, 1)), R(1, 12))
P(id="2-90", ch=15, sec="15.6", type="15-triple", src="강의 15.6 유형",
  q=r"평면 $x=0,\ y=0,\ z=0,\ y+z=1,\ x+z=1$로 둘러싸인 입체 $E$에서 $\displaystyle\iiint_E z\,dV$를 계산하라.",
  hint=r"$z$를 바깥에 두면 $0\le x\le1-z,\ 0\le y\le1-z$ (정사각형 단면)",
  ans=r"$\dfrac{1}{12}$",
  sol=[r"$z$를 고정하면 단면은 $0\le x\le1-z,\ 0\le y\le1-z$인 정사각형",
       r"$\displaystyle\int_0^1z(1-z)^2\,dz=\frac12-\frac23+\frac14=\frac{1}{12}$"],
  check=_c)


def _c():
    f = x + y*z + z**2
    I0 = integrate(integrate(integrate(f, (z, 0, y)), (y, 0, x)), (x, 0, 1))
    I1 = integrate(integrate(integrate(f, (x, y, 1)), (y, z, 1)), (z, 0, 1))
    I2 = integrate(integrate(integrate(f, (y, z, x)), (z, 0, x)), (x, 0, 1))
    assert EQ(I0, I1) and EQ(I0, I2)
P(id="2-91", ch=15, sec="15.6", type="15-order3", src="과제 15.6 #39 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_0^x\!\!\int_0^y f(x,y,z)\,dz\,dy\,dx$를 (a) $dx\,dy\,dz$ 순서 (b) $dy\,dz\,dx$ 순서로 다시 써라.",
  hint=r"영역은 $0\le z\le y\le x\le1$. 바깥 변수의 범위부터 정하고 안쪽으로 들어가요.",
  ans=r"(a) $\displaystyle\int_0^1\!\!\int_z^1\!\!\int_y^1 f\,dx\,dy\,dz$  (b) $\displaystyle\int_0^1\!\!\int_0^x\!\!\int_z^x f\,dy\,dz\,dx$",
  sol=[r"영역: $0\le z\le y\le x\le1$ (세 변수가 크기 순으로 놓임)",
       r"(a) $z$: $0\to1$, $y$: $z\to1$, $x$: $y\to1$",
       r"(b) $x$: $0\to1$, $z$: $0\to x$, $y$: $z\to x$",
       r"($f=1$이면 모두 $\tfrac16$ — 정육면체의 $\tfrac16$인 사면체)"],
  check=_c)


def _c():
    f = x*z + y
    I1 = integrate(integrate(integrate(f, (z, 0, y)), (y, 0, 4 - x**2)), (x, 0, 2))
    I2 = integrate(integrate(integrate(f, (x, 0, sqrt(4 - y))), (z, 0, y)), (y, 0, 4))
    assert EQ(I1, I2)
    assert EQ(integrate(integrate(integrate(1, (z, 0, y)), (y, 0, 4 - x**2)), (x, 0, 2)), R(128, 15))
P(id="2-92", ch=15, sec="15.6", type="15-order3", src="강의 15.6 (순서 바꾸기) 유형",
  q=r"$\displaystyle\int_0^2\!\!\int_0^{4-x^2}\!\!\int_0^{y}f(x,y,z)\,dz\,dy\,dx$를 $dx\,dz\,dy$ 순서로 다시 쓰고, $f=1$일 때의 값을 구하라.",
  hint=r"$y$를 고정하면 $0\le z\le y$, $0\le x\le\sqrt{4-y}$ ($y\le4-x^2$)",
  ans=r"$\displaystyle\int_0^4\!\!\int_0^y\!\!\int_0^{\sqrt{4-y}}f\,dx\,dz\,dy$,  값 $\dfrac{128}{15}$",
  sol=[r"영역: $0\le x\le2,\ 0\le y\le4-x^2,\ 0\le z\le y$",
       r"$y$: $0\to4$, $z$: $0\to y$, $x$: $0\to\sqrt{4-y}$",
       r"$f=1$: $\displaystyle\int_0^4y\sqrt{4-y}\,dy$, $u=4-y$: $\displaystyle\int_0^4(4-u)\sqrt u\,du=\frac{64}{3}-\frac{64}{5}=\frac{128}{15}$"],
  check=_c)


# ───────── 15.7 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(r*r, (z, -1, 3)), (r, 0, 3)), (th, 0, 2*pi)), 72*pi)
P(id="2-93", ch=15, sec="15.7", type="15-cyl", src="과제 15.7 #19 유형",
  q=r"$E$가 원기둥 $x^2+y^2=9$ 안쪽, 평면 $z=-1$과 $z=3$ 사이의 영역일 때 $\displaystyle\iiint_E\sqrt{x^2+y^2}\,dV$를 계산하라.",
  hint=r"$\sqrt{x^2+y^2}=r$, $dV=r\,dz\,dr\,d\theta$",
  ans=r"$72\pi$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^3\!\!\int_{-1}^{3}r\cdot r\,dz\,dr\,d\theta=2\pi\cdot\frac{27}{3}\cdot4=72\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(r**2*sin(th)**2*r, (z, 0, r)), (r, 0, 2)), (th, 0, 2*pi)), 32*pi/5)
P(id="2-94", ch=15, sec="15.7", type="15-cyl", src="과제 15.7 #23 유형",
  q=r"$E$가 원기둥 $x^2+y^2=4$ 안쪽, 평면 $z=0$ 위, 원뿔 $z=\sqrt{x^2+y^2}$ 아래인 입체일 때 $\displaystyle\iiint_Ey^2\,dV$를 계산하라.",
  hint=r"$y^2=r^2\sin^2\theta$, $0\le z\le r$. $\int_0^{2\pi}\sin^2\theta\,d\theta=\pi$",
  ans=r"$\dfrac{32\pi}{5}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^r r^2\sin^2\theta\cdot r\,dz\,dr\,d\theta=\int_0^{2\pi}\sin^2\theta\,d\theta\int_0^2r^4\,dr$",
       r"$=\pi\cdot\dfrac{32}{5}=\dfrac{32\pi}{5}$"],
  check=_c)


def _c():
    cyl = integrate(integrate(integrate(z*r, (z, r, 2)), (r, 0, 2)), (th, 0, 2*pi))
    assert EQ(cyl, 4*pi)
P(id="2-95", ch=15, sec="15.7", type="15-cyl", src="과제 15.7 #31 유형",
  q=r"원주좌표로 바꾸어 계산하라. $$\int_{-2}^{2}\!\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}\!\int_{\sqrt{x^2+y^2}}^{2}z\,dz\,dx\,dy$$",
  hint=r"$xy$ 범위는 원판 $r\le2$, $z$는 원뿔 $z=r$부터 $z=2$까지",
  ans=r"$4\pi$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_r^2z\,r\,dz\,dr\,d\theta=2\pi\int_0^2\frac{4-r^2}{2}r\,dr$",
       r"$=\pi\Big[2r^2-\dfrac{r^4}{4}\Big]_0^2=\pi(8-4)=4\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(r, (z, 1 - r**2, 4)), (r, 0, 1)), (th, 0, pi)), 7*pi/4)
P(id="2-96", ch=15, sec="15.7", type="15-cyl", src="복습 15.6–8 기초2 유형",
  q=r"원기둥 $x^2+y^2=1$ 안쪽, $xz$평면의 오른쪽($y\ge0$), 평면 $z=4$ 아래, 포물면 $z=1-x^2-y^2$ 위에 있는 입체의 부피를 구하라.",
  hint=r"$y\ge0$이면 $0\le\theta\le\pi$. $1-r^2\le z\le4$",
  ans=r"$\dfrac{7\pi}{4}$",
  sol=[r"$V=\displaystyle\int_0^{\pi}\!\!\int_0^1\!\!\int_{1-r^2}^{4}r\,dz\,dr\,d\theta=\pi\int_0^1(3+r^2)r\,dr$",
       r"$=\pi\Big(\dfrac32+\dfrac14\Big)=\dfrac{7\pi}{4}$"],
  check=_c)


# ───────── 15.8 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(rho**2*sin(ph), (rho, 0, 2)), (th, 0, 2*pi)), (ph, 0, pi/3)), 8*pi/3)
P(id="2-97", ch=15, sec="15.8", type="15-sph", src="과제 15.8 #17 유형",
  q=r"$\displaystyle\int_0^{\pi/3}\!\!\int_0^{2\pi}\!\!\int_0^2\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$가 나타내는 입체를 말로 설명하고 값을 구하라.",
  hint=r"$\phi\le\frac\pi3$는 꼭짓점이 원점이고 위로 열린 원뿔의 안쪽, $\rho\le2$는 반지름 $2$인 구의 안쪽",
  ans=r"원뿔 $\phi=\tfrac\pi3$ 안쪽과 구 $\rho=2$ 안쪽의 공통부분 (아이스크림콘 모양),  값 $\dfrac{8\pi}{3}$",
  sol=[r"입체: 원뿔 $z=\tfrac{1}{\sqrt3}\sqrt{x^2+y^2}$ ($\phi=\tfrac\pi3$) 위쪽, 구 $x^2+y^2+z^2=4$ 안쪽",
       r"$\displaystyle\int_0^{\pi/3}\sin\phi\,d\phi\cdot2\pi\cdot\frac{8}{3}=\Big(1-\frac12\Big)\cdot\frac{16\pi}{3}=\frac{8\pi}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(rho*rho**2*sin(ph), (rho, 1, 2)), (ph, 0, pi)), (th, 0, 2*pi)), 15*pi)
P(id="2-98", ch=15, sec="15.8", type="15-sph", src="과제 15.8 #23 유형",
  q=r"$E$가 두 구 $x^2+y^2+z^2=1$과 $x^2+y^2+z^2=4$ 사이의 영역일 때 $\displaystyle\iiint_E\sqrt{x^2+y^2+z^2}\,dV$를 계산하라.",
  hint=r"$1\le\rho\le2$, 피적분함수 $=\rho$",
  ans=r"$15\pi$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_1^2\rho\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot2\cdot\frac{16-1}{4}=15\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(rho**2*sin(ph), (rho, 0, 2*cos(ph))), (ph, 0, pi/4)), (th, 0, 2*pi)), pi)
P(id="2-99", ch=15, sec="15.8", type="15-sph", src="복습 15.6–8 기초4 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=2z$ 아래에 있는 입체의 부피를 구면좌표로 구하라.",
  hint=r"$x^2+y^2+z^2=2z \iff \rho^2=2\rho\cos\phi \iff \rho=2\cos\phi$",
  ans=r"$\pi$",
  sol=[r"$0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi4,\ 0\le\rho\le2\cos\phi$",
       r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\frac{8\cos^3\phi}{3}\sin\phi\,d\phi\,d\theta=\frac{16\pi}{3}\Big[-\frac{\cos^4\phi}{4}\Big]_0^{\pi/4}$",
       r"$=\dfrac{16\pi}{3}\cdot\dfrac14\Big(1-\dfrac14\Big)=\pi$"],
  check=_c)


def _c():
    cyl = integrate(integrate(integrate(r, (z, 1, sqrt(4 - r**2))), (r, 0, sqrt(3))), (th, 0, 2*pi))
    sph = integrate(integrate(integrate(rho**2*sin(ph), (rho, 1/cos(ph), 2)), (ph, 0, pi/3)), (th, 0, 2*pi))
    assert EQ(cyl, 5*pi/3) and EQ(sph, 5*pi/3)
P(id="2-100", ch=15, sec="15.8", type="15-sphconv", src="2022 중간(블럭2) 8(b) 유형",
  q=r"다음 적분이 나타내는 입체를 설명하고, 구면좌표 적분으로 바꾸어 값을 구하라. $$\int_0^{2\pi}\!\!\int_0^{\sqrt3}\!\!\int_1^{\sqrt{4-r^2}}r\,dz\,dr\,d\theta$$",
  hint=r"$z=1$은 $\rho\cos\phi=1$, 즉 $\rho=\sec\phi$. 구 $\rho=2$와 평면 $z=1$이 만나는 곳은 $\phi=\tfrac\pi3$",
  ans=r"구 $\rho=2$ 중 평면 $z=1$ 위쪽 부분(구모자),  $\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/3}\!\!\int_{\sec\phi}^{2}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=\frac{5\pi}{3}$",
  sol=[r"영역: $1\le z\le\sqrt{4-r^2}$ → 평면 $z=1$과 구 $x^2+y^2+z^2=4$ 사이 (교선 $r=\sqrt3$)",
       r"구면좌표: $\sec\phi\le\rho\le2$, 교선에서 $\tan\phi=\sqrt3 \Rightarrow \phi=\tfrac\pi3$",
       r"$V=2\pi\displaystyle\int_0^{\pi/3}\frac{8-\sec^3\phi}{3}\sin\phi\,d\phi=\frac{2\pi}{3}\Big(8\cdot\frac12-\Big[\frac{1}{2\cos^2\phi}\Big]_0^{\pi/3}\Big)$",
       r"$=\dfrac{2\pi}{3}\Big(4-\dfrac32\Big)=\dfrac{5\pi}{3}$ (원주좌표로 직접 해도 같은 값)"],
  check=_c)


def _c():
    sph = integrate(integrate(integrate(rho*cos(ph)*rho*rho**2*sin(ph), (rho, 0, 3)), (ph, 0, pi/2)), (th, 0, pi/2))
    assert EQ(sph, 243*pi/20)
P(id="2-101", ch=15, sec="15.8", type="15-sphconv", src="2022 중간(블럭1) 10번 유형",
  q=r"구면좌표로 바꾸어 계산하라. $$\int_0^3\!\int_0^{\sqrt{9-x^2}}\!\int_0^{\sqrt{9-x^2-y^2}}z\sqrt{x^2+y^2+z^2}\,dz\,dy\,dx$$",
  hint=r"영역은 반지름 $3$인 구의 제1팔분면: $0\le\theta\le\tfrac\pi2,\ 0\le\phi\le\tfrac\pi2,\ 0\le\rho\le3$",
  ans=r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^{\pi/2}\!\!\int_0^3\rho^4\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=\frac{243\pi}{20}$",
  sol=[r"$x\ge0,\ y\ge0$이고 $0\le z\le\sqrt{9-x^2-y^2}$ → 구의 $\tfrac18$ (제1팔분면)",
       r"$z\sqrt{x^2+y^2+z^2}\,dV=\rho\cos\phi\cdot\rho\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=\dfrac\pi2\cdot\Big[\tfrac{\sin^2\phi}{2}\Big]_0^{\pi/2}\cdot\dfrac{3^5}{5}=\dfrac\pi2\cdot\dfrac12\cdot\dfrac{243}{5}=\dfrac{243\pi}{20}$"],
  check=_c)

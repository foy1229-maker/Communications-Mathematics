"""1단계 · 기본 추가분 — Ch.15 중적분: 1-72 ~ 1-101"""
from bank_lib import *


# ───────── 15.1 ─────────
def _c():
    assert EQ(integrate(integrate(x*y**2 + 2, (y, 1, 3)), (x, 0, 2)), R(76, 3))
P(id="1-72", ch=15, sec="15.1", type="15-rect", src="과제 15.1 #21 유형",
  q=r"$\displaystyle\iint_R (xy^2+2)\,dA$를 계산하라. 단, $R=[0,2]\times[1,3]$.",
  hint=r"푸비니 정리: $\displaystyle\int_0^2\!\!\int_1^3 (xy^2+2)\,dy\,dx$",
  ans=r"$\dfrac{76}{3}$",
  sol=[r"안쪽: $\displaystyle\int_1^3(xy^2+2)\,dy=\Big[\tfrac{xy^3}{3}+2y\Big]_1^3=\tfrac{26}{3}x+4$",
       r"바깥: $\displaystyle\int_0^2\Big(\tfrac{26}{3}x+4\Big)dx=\tfrac{26}{3}\cdot2+8=\dfrac{76}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(x*exp(x*y), (y, 0, 2)), (x, 0, 1)), (E**2 - 3) / 2)
P(id="1-73", ch=15, sec="15.1", type="15-rect", src="강의 15.1 (적분 순서 선택) 유형",
  q=r"$\displaystyle\iint_R xe^{xy}\,dA$를 계산하라. 단, $R=[0,1]\times[0,2]$.",
  hint=r"$y$로 먼저 적분하면 $x$가 상수라 바로 $e^{xy}$가 나와요. ($x$로 먼저 하면 부분적분이 필요해요.)",
  ans=r"$\dfrac{e^2-3}{2}$",
  sol=[r"안쪽 ($y$로): $\displaystyle\int_0^2 xe^{xy}\,dy=\Big[e^{xy}\Big]_0^2=e^{2x}-1$",
       r"바깥: $\displaystyle\int_0^1(e^{2x}-1)\,dx=\frac{e^2-1}{2}-1=\frac{e^2-3}{2}$"],
  check=_c)


# ───────── 15.2 ─────────
def _c():
    assert EQ(integrate(integrate(x*y, (y, x**2, 2*x)), (x, 0, 2)), R(8, 3))
P(id="1-74", ch=15, sec="15.2", type="15-general", src="강의 15.2 (Type I) 유형",
  q=r"포물선 $y=x^2$과 직선 $y=2x$로 둘러싸인 영역 $D$에서 $\displaystyle\iint_D xy\,dA$를 계산하라.",
  hint=r"교점 $x=0,\ 2$. $0\le x\le2$에서 $x^2\le y\le 2x$예요.",
  ans=r"$\dfrac83$",
  sol=[r"교점: $x^2=2x \Rightarrow x=0,\ 2$.  $D=\{0\le x\le2,\ x^2\le y\le2x\}$",
       r"안쪽: $\displaystyle\int_{x^2}^{2x}xy\,dy=\frac{x}{2}(4x^2-x^4)$",
       r"바깥: $\displaystyle\frac12\int_0^2(4x^3-x^5)\,dx=\frac12\Big(16-\frac{64}{6}\Big)=\frac83$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(x + y, (x, y**2, 4)), (y, -2, 2)), R(128, 5))
P(id="1-75", ch=15, sec="15.2", type="15-general", src="강의 15.2 (Type II) 유형",
  q=r"포물선 $x=y^2$과 직선 $x=4$로 둘러싸인 영역 $D$에서 $\displaystyle\iint_D (x+y)\,dA$를 계산하라.",
  hint=r"$y$를 바깥 변수로: $-2\le y\le2,\ y^2\le x\le4$",
  ans=r"$\dfrac{128}{5}$",
  sol=[r"$D=\{-2\le y\le2,\ y^2\le x\le4\}$",
       r"안쪽: $\displaystyle\int_{y^2}^{4}(x+y)\,dx=\frac{16-y^4}{2}+y(4-y^2)$",
       r"$y(4-y^2)$는 홀함수라 $[-2,2]$ 적분이 $0$ → $\displaystyle\int_{-2}^{2}\Big(8-\frac{y^4}{2}\Big)dy=32-\frac{32}{5}=\frac{128}{5}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(x + 2*y, (y, 0, 2 - 2*x)), (x, 0, 1)), R(5, 3))
P(id="1-76", ch=15, sec="15.2", type="15-general", src="과제 15.2 #33 유형",
  q=r"꼭짓점이 $(0,0),\ (1,0),\ (0,2)$인 삼각형 위, 곡면 $z=x+2y$ 아래에 있는 입체의 부피를 구하라.",
  hint=r"빗변은 $y=2-2x$. $0\le x\le1,\ 0\le y\le2-2x$",
  ans=r"$\dfrac53$",
  sol=[r"$V=\displaystyle\int_0^1\!\!\int_0^{2-2x}(x+2y)\,dy\,dx$",
       r"안쪽: $x(2-2x)+(2-2x)^2=2x^2-6x+4$",
       r"$\displaystyle\int_0^1(2x^2-6x+4)\,dx=\frac23-3+4=\frac53$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(exp(y**2), (x, 0, y)), (y, 0, 1)), (E - 1) / 2)
P(id="1-77", ch=15, sec="15.2", type="15-order", src="과제 15.2 #61 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^1\!\!\int_x^1 e^{y^2}\,dy\,dx$를 계산하라.",
  hint=r"$e^{y^2}$은 $y$로 바로 적분할 수 없어요. 영역 $0\le x\le y\le1$을 $y$ 기준으로 다시 읽어요.",
  ans=r"$\dfrac{e-1}{2}$",
  sol=[r"영역: $0\le x\le1,\ x\le y\le1$ $\iff$ $0\le y\le1,\ 0\le x\le y$",
       r"$\displaystyle\int_0^1\!\!\int_0^y e^{y^2}\,dx\,dy=\int_0^1 ye^{y^2}\,dy$",
       r"$=\Big[\tfrac12e^{y^2}\Big]_0^1=\dfrac{e-1}{2}$"],
  check=_c)


def _c():
    I = integrate(integrate(sqrt(x**3 + 1), (y, 0, x**2)), (x, 0, 1))
    assert EQ(I, R(2, 9)*(2*sqrt(2) - 1))
P(id="1-78", ch=15, sec="15.2", type="15-order", src="2024 중간 2(a) 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^1\!\!\int_{\sqrt y}^1 \sqrt{x^3+1}\,dx\,dy$를 계산하라.",
  hint=r"$\sqrt y\le x\le1$ $\iff$ $y\le x^2$. 바꾼 뒤 $u=x^3+1$로 치환해요.",
  ans=r"$\dfrac{2}{9}(2\sqrt2-1)$",
  sol=[r"영역: $0\le y\le1,\ \sqrt y\le x\le1$ $\iff$ $0\le x\le1,\ 0\le y\le x^2$",
       r"$\displaystyle\int_0^1\!\!\int_0^{x^2}\sqrt{x^3+1}\,dy\,dx=\int_0^1 x^2\sqrt{x^3+1}\,dx$",
       r"$u=x^3+1$: $\displaystyle\frac13\int_1^2\sqrt u\,du=\frac29\Big[u^{3/2}\Big]_1^2=\frac29(2\sqrt2-1)$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(sin(y) / y, (x, 0, y)), (y, 0, pi)), 2)
P(id="1-79", ch=15, sec="15.2", type="15-order", src="강의 15.2 (순서 바꾸기) 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^{\pi}\!\!\int_x^{\pi}\frac{\sin y}{y}\,dy\,dx$를 계산하라.",
  hint=r"$\dfrac{\sin y}{y}$는 부정적분이 없어요. $x$로 먼저 적분하면 $y$가 곱해져 약분돼요.",
  ans=r"$2$",
  sol=[r"영역: $0\le x\le y\le\pi$ → $\displaystyle\int_0^{\pi}\!\!\int_0^{y}\frac{\sin y}{y}\,dx\,dy$",
       r"안쪽: $\dfrac{\sin y}{y}\cdot y=\sin y$",
       r"$\displaystyle\int_0^{\pi}\sin y\,dy=2$"],
  check=_c)


# ───────── 15.3 ─────────
def _c():
    assert EQ(integrate(integrate(r**2 * r, (r, 0, 2)), (th, 0, 2*pi)), 8*pi)
P(id="1-80", ch=15, sec="15.3", type="15-polar", src="강의 15.3 유형",
  q=r"$D$가 원판 $x^2+y^2\le4$일 때 $\displaystyle\iint_D (x^2+y^2)\,dA$를 극좌표로 계산하라.",
  hint=r"$x^2+y^2=r^2$, $dA=r\,dr\,d\theta$ — $r$을 빠뜨리지 마세요.",
  ans=r"$8\pi$",
  sol=[r"$D$: $0\le r\le2,\ 0\le\theta\le2\pi$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r^2\cdot r\,dr\,d\theta=2\pi\cdot\frac{2^4}{4}=8\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(exp(-r**2)*r, (r, 1, 2)), (th, 0, pi/2)), pi/4*(exp(-1) - exp(-4)))
P(id="1-81", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #13 유형",
  q=r"$D=\{(x,y)\mid 1\le x^2+y^2\le4,\ x\ge0,\ y\ge0\}$일 때 $\displaystyle\iint_D e^{-(x^2+y^2)}\,dA$를 계산하라.",
  hint=r"1사분면 고리: $1\le r\le2,\ 0\le\theta\le\tfrac\pi2$. $re^{-r^2}$은 $u=r^2$ 치환.",
  ans=r"$\dfrac{\pi}{4}\big(e^{-1}-e^{-4}\big)$",
  sol=[r"$\displaystyle\int_0^{\pi/2}\!\!\int_1^2 e^{-r^2}r\,dr\,d\theta=\frac\pi2\Big[-\tfrac12e^{-r^2}\Big]_1^2$",
       r"$=\dfrac\pi2\cdot\dfrac12\big(e^{-1}-e^{-4}\big)=\dfrac\pi4\big(e^{-1}-e^{-4}\big)$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(r*sin(th)*r, (r, 0, 3)), (th, 0, pi)), 18)
    assert EQ(integrate(integrate(y, (y, 0, sqrt(9 - x**2))), (x, -3, 3)), 18)
P(id="1-82", ch=15, sec="15.3", type="15-polar", src="강의 15.3 유형",
  q=r"$D$가 위쪽 반원판 $x^2+y^2\le9,\ y\ge0$일 때 $\displaystyle\iint_D y\,dA$를 계산하라.",
  hint=r"$0\le r\le3,\ 0\le\theta\le\pi$, $y=r\sin\theta$",
  ans=r"$18$",
  sol=[r"$\displaystyle\int_0^{\pi}\!\!\int_0^3 (r\sin\theta)\,r\,dr\,d\theta=\int_0^{\pi}\sin\theta\,d\theta\cdot\int_0^3 r^2\,dr$",
       r"$=2\cdot9=18$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(r, (r, 0, cos(2*th))), (th, -pi/4, pi/4)), pi/8)
P(id="1-83", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #17 유형 (넓이)",
  q=r"장미곡선 $r=\cos2\theta$의 꽃잎 하나 $\left(-\tfrac\pi4\le\theta\le\tfrac\pi4\right)$의 넓이를 이중적분으로 구하라.",
  hint=r"$A=\displaystyle\iint_D 1\,dA=\int\!\!\int_0^{\cos2\theta} r\,dr\,d\theta$, $\cos^22\theta=\tfrac{1+\cos4\theta}{2}$",
  ans=r"$\dfrac{\pi}{8}$",
  sol=[r"$A=\displaystyle\int_{-\pi/4}^{\pi/4}\!\!\int_0^{\cos2\theta}r\,dr\,d\theta=\frac12\int_{-\pi/4}^{\pi/4}\cos^22\theta\,d\theta$",
       r"$=\dfrac14\displaystyle\int_{-\pi/4}^{\pi/4}(1+\cos4\theta)\,d\theta=\dfrac14\cdot\dfrac\pi2=\dfrac\pi8$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(r**3 * r, (r, 0, 1)), (th, 0, pi)), pi/5)
P(id="1-84", ch=15, sec="15.3", type="15-polar", src="복습 15.1–3 기초6 유형",
  q=r"극좌표로 바꾸어 $\displaystyle\int_{-1}^{1}\!\!\int_0^{\sqrt{1-x^2}}(x^2+y^2)^{3/2}\,dy\,dx$를 계산하라.",
  hint=r"$0\le y\le\sqrt{1-x^2}$는 위쪽 반원판. $(x^2+y^2)^{3/2}=r^3$",
  ans=r"$\dfrac{\pi}{5}$",
  sol=[r"영역: 위쪽 반원판 → $0\le r\le1,\ 0\le\theta\le\pi$",
       r"$\displaystyle\int_0^{\pi}\!\!\int_0^1 r^3\cdot r\,dr\,d\theta=\pi\cdot\frac15=\frac\pi5$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(r * r, (r, 0, 2)), (th, 0, 2*pi)), 16*pi/3)
P(id="1-85", ch=15, sec="15.3", type="15-mass", src="2025 중간 1번 · 2022 중간(블럭1) 8번 유형 (기초)",
  q=r"원판 $x^2+y^2\le4$ 모양의 얇은 판의 밀도가 $\rho(x,y)=\sqrt{x^2+y^2}$일 때 판의 질량을 구하라.",
  hint=r"질량 $m=\displaystyle\iint_D\rho\,dA$. 극좌표에서 $\rho=r$이에요.",
  ans=r"$\dfrac{16\pi}{3}$",
  sol=[r"$m=\displaystyle\int_0^{2\pi}\!\!\int_0^2 r\cdot r\,dr\,d\theta$",
       r"$=2\pi\cdot\dfrac{8}{3}=\dfrac{16\pi}{3}$"],
  check=_c)


def _c():
    m = integrate(integrate(r, (r, 0, 1)), (th, 0, pi))
    My = integrate(integrate(r*sin(th)*r, (r, 0, 1)), (th, 0, pi))
    Mx = integrate(integrate(r*cos(th)*r, (r, 0, 1)), (th, 0, pi))
    assert EQ(m, pi/2) and EQ(My, R(2, 3)) and Mx == 0 and EQ(My / m, 4/(3*pi))
P(id="1-86", ch=15, sec="15.3", type="15-mass", src="강의 15.6 ex6 (질량중심) 개념 · 판 버전",
  q=r"밀도가 일정($\rho=1$)한 위쪽 반원판 $x^2+y^2\le1,\ y\ge0$의 질량중심을 구하라.",
  hint=r"$\bar x=\dfrac1m\displaystyle\iint_D x\rho\,dA,\ \ \bar y=\dfrac1m\iint_D y\rho\,dA$. 대칭으로 $\bar x=0$.",
  ans=r"$\left(0,\ \dfrac{4}{3\pi}\right)$",
  sol=[r"$m=\dfrac{\pi}{2}$ (반원 넓이),  $y$축 대칭이라 $\bar x=0$",
       r"$\displaystyle\iint_D y\,dA=\int_0^{\pi}\!\!\int_0^1 r\sin\theta\cdot r\,dr\,d\theta=2\cdot\frac13=\frac23$",
       r"$\bar y=\dfrac{2/3}{\pi/2}=\dfrac{4}{3\pi}$ → 질량중심 $\left(0,\dfrac{4}{3\pi}\right)$"],
  check=_c)


# ───────── 15.6 ─────────
def _c():
    assert integrate(x*y*z**2, (x, 0, 1), (y, 0, 2), (z, 0, 3)) == 9
P(id="1-87", ch=15, sec="15.6", type="15-triple", src="강의 15.6 (직육면체) 유형",
  q=r"$B=[0,1]\times[0,2]\times[0,3]$일 때 $\displaystyle\iiint_B xyz^2\,dV$를 계산하라.",
  hint=r"직육면체에서 피적분함수가 곱으로 분리되면 세 적분의 곱이에요.",
  ans=r"$9$",
  sol=[r"$\displaystyle\int_0^1x\,dx\cdot\int_0^2y\,dy\cdot\int_0^3z^2\,dz=\frac12\cdot2\cdot9=9$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(z, (z, 0, x + y)), (y, 0, x)), (x, 0, 1)), R(7, 24))
P(id="1-88", ch=15, sec="15.6", type="15-triple", src="과제 15.6 #5 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_0^x\!\!\int_0^{x+y} z\,dz\,dy\,dx$를 계산하라.",
  hint=r"안쪽부터 차례로: $\int z\,dz=\tfrac{z^2}{2}$",
  ans=r"$\dfrac{7}{24}$",
  sol=[r"$\displaystyle\int_0^{x+y}z\,dz=\frac{(x+y)^2}{2}$",
       r"$\displaystyle\int_0^x\frac{(x+y)^2}{2}dy=\frac16\Big[(x+y)^3\Big]_0^x=\frac{8x^3-x^3}{6}=\frac{7x^3}{6}$",
       r"$\displaystyle\int_0^1\frac{7x^3}{6}dx=\frac{7}{24}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(x, (z, 0, 1 - x - y)), (y, 0, 1 - x)), (x, 0, 1)), R(1, 24))
P(id="1-89", ch=15, sec="15.6", type="15-triple", src="강의 15.6 (사면체) 유형",
  q=r"$E$가 평면 $x+y+z=1$과 세 좌표평면으로 둘러싸인 사면체일 때 $\displaystyle\iiint_E x\,dV$를 계산하라.",
  hint=r"$0\le x\le1,\ 0\le y\le1-x,\ 0\le z\le1-x-y$",
  ans=r"$\dfrac{1}{24}$",
  sol=[r"$\displaystyle\int_0^{1-x-y}x\,dz=x(1-x-y)$",
       r"$\displaystyle\int_0^{1-x}x(1-x-y)\,dy=x\cdot\frac{(1-x)^2}{2}$",
       r"$\displaystyle\frac12\int_0^1x(1-x)^2dx=\frac12\Big(\frac12-\frac23+\frac14\Big)=\frac12\cdot\frac1{12}=\frac1{24}$"],
  check=_c)


def _c():
    assert integrate(integrate(integrate(1, (z, 0, 4 - x**2)), (x, -2, 2)), (y, 0, 3)) == 32
P(id="1-90", ch=15, sec="15.6", type="15-triple", src="강의 15.6 (부피) 유형",
  q=r"포물기둥 $z=4-x^2$과 평면 $z=0,\ y=0,\ y=3$으로 둘러싸인 입체의 부피를 삼중적분으로 구하라.",
  hint=r"$-2\le x\le2,\ 0\le y\le3,\ 0\le z\le4-x^2$",
  ans=r"$32$",
  sol=[r"$V=\displaystyle\int_0^3\!\!\int_{-2}^{2}\!\!\int_0^{4-x^2}dz\,dx\,dy=3\int_{-2}^2(4-x^2)\,dx$",
       r"$=3\Big(16-\frac{16}{3}\Big)=3\cdot\frac{32}{3}=32$"],
  check=_c)


def _c():
    f = x*y + z**2 + x
    I1 = integrate(integrate(integrate(f, (z, 0, 4 - 2*x - y)), (y, 0, 4 - 2*x)), (x, 0, 2))
    I2 = integrate(integrate(integrate(f, (x, 0, (4 - y - z)/2)), (y, 0, 4 - z)), (z, 0, 4))
    assert EQ(I1, I2)
    assert EQ(integrate(integrate(integrate(1, (z, 0, 4 - 2*x - y)), (y, 0, 4 - 2*x)), (x, 0, 2)), R(16, 3))
P(id="1-91", ch=15, sec="15.6", type="15-order3", src="과제 15.6 #31 · #39 유형",
  q=r"$\displaystyle\int_0^2\!\!\int_0^{4-2x}\!\!\int_0^{4-2x-y} f(x,y,z)\,dz\,dy\,dx$를 $dx\,dy\,dz$ 순서의 적분으로 다시 써라. 또 $f=1$일 때의 값(부피)을 구하라.",
  hint=r"영역은 평면 $2x+y+z=4$ 아래의 사면체(1팔분면). 꼭짓점 $(2,0,0),(0,4,0),(0,0,4)$",
  ans=r"$\displaystyle\int_0^4\!\!\int_0^{4-z}\!\!\int_0^{(4-y-z)/2} f\,dx\,dy\,dz$,  부피 $\dfrac{16}{3}$",
  sol=[r"영역: $x,y,z\ge0,\ 2x+y+z\le4$ (사면체)",
       r"$z$: $0\to4$, 그다음 $yz$평면 삼각형에서 $y$: $0\to4-z$, 마지막 $x$: $0\to\dfrac{4-y-z}{2}$",
       r"$\displaystyle\int_0^4\!\!\int_0^{4-z}\!\!\int_0^{(4-y-z)/2} f\,dx\,dy\,dz$",
       r"부피 $=\dfrac16\cdot2\cdot4\cdot4=\dfrac{16}{3}$ (사면체 공식과 일치)"],
  check=_c)


def _c():
    f = x**2 + y*z + 1
    I1 = integrate(integrate(integrate(f, (z, 0, 1 - y)), (y, x**2, 1)), (x, 0, 1))
    I2 = integrate(integrate(integrate(f, (x, 0, sqrt(y))), (z, 0, 1 - y)), (y, 0, 1))
    assert EQ(I1, I2)
    assert EQ(integrate(integrate(integrate(1, (z, 0, 1 - y)), (y, x**2, 1)), (x, 0, 1)), R(4, 15))
P(id="1-92", ch=15, sec="15.6", type="15-order3", src="강의 15.6 (순서 바꾸기) 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_{x^2}^{1}\!\!\int_0^{1-y} f(x,y,z)\,dz\,dy\,dx$를 $dx\,dz\,dy$ 순서로 다시 쓰고, $f=1$일 때의 값을 구하라.",
  hint=r"$y$를 고정하면 $0\le z\le1-y$, $0\le x\le\sqrt y$ (조건 $x^2\le y$, $x\ge0$)",
  ans=r"$\displaystyle\int_0^1\!\!\int_0^{1-y}\!\!\int_0^{\sqrt y} f\,dx\,dz\,dy$,  값 $\dfrac{4}{15}$",
  sol=[r"영역: $0\le x\le1,\ x^2\le y\le1,\ 0\le z\le1-y$",
       r"$y$를 바깥($0\to1$)으로 두면 $z$: $0\to1-y$, $x$: $0\to\sqrt y$",
       r"$\displaystyle\int_0^1\!\!\int_0^{1-y}\!\!\int_0^{\sqrt y} f\,dx\,dz\,dy$",
       r"$f=1$: $\displaystyle\int_0^1(1-y)\sqrt y\,dy=\frac23-\frac25=\frac{4}{15}$"],
  check=_c)


# ───────── 15.7 ─────────
def _c():
    assert EQ(integrate(integrate((4 - r*sin(th))*r, (r, 0, 2)), (th, 0, 2*pi)), 16*pi)
P(id="1-93", ch=15, sec="15.7", type="15-cyl", src="강의 15.7 유형",
  q=r"원기둥 $x^2+y^2=4$ 안쪽에서 평면 $z=0$과 $z=4-y$ 사이에 있는 입체의 부피를 구하라.",
  hint=r"원주좌표: $0\le z\le 4-r\sin\theta$, $0\le r\le2$. $\sin\theta$ 항은 한 바퀴 적분하면 $0$이에요.",
  ans=r"$16\pi$",
  sol=[r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{4-r\sin\theta}r\,dz\,dr\,d\theta=\int_0^{2\pi}\!\!\int_0^2(4r-r^2\sin\theta)\,dr\,d\theta$",
       r"$\displaystyle\int_0^{2\pi}\Big(8-\frac83\sin\theta\Big)d\theta=16\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(r**2 * r, (z, 0, 3)), (r, 0, 1)), (th, 0, 2*pi)), 3*pi/2)
P(id="1-94", ch=15, sec="15.7", type="15-cyl", src="과제 15.7 #19 유형",
  q=r"$E$가 원기둥 $x^2+y^2\le1$의 $0\le z\le3$ 부분일 때 $\displaystyle\iiint_E (x^2+y^2)\,dV$를 계산하라.",
  hint=r"$x^2+y^2=r^2$, $dV=r\,dz\,dr\,d\theta$",
  ans=r"$\dfrac{3\pi}{2}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1\!\!\int_0^3 r^2\cdot r\,dz\,dr\,d\theta=2\pi\cdot\frac14\cdot3=\frac{3\pi}{2}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(z*r, (z, 0, 4 - r**2)), (r, 0, 2)), (th, 0, 2*pi)), 32*pi/3)
P(id="1-95", ch=15, sec="15.7", type="15-cyl", src="강의 15.7 (포물면) 유형",
  q=r"포물면 $z=4-x^2-y^2$ 아래, $xy$평면 위에 있는 입체 $E$에서 $\displaystyle\iiint_E z\,dV$를 계산하라.",
  hint=r"$0\le z\le4-r^2$, 포물면이 $xy$평면과 만나는 곳은 $r=2$",
  ans=r"$\dfrac{32\pi}{3}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{4-r^2}z\,r\,dz\,dr\,d\theta=2\pi\int_0^2\frac{(4-r^2)^2}{2}r\,dr$",
       r"$u=4-r^2$: $\displaystyle\pi\int_0^2(4-r^2)^2r\,dr=\frac\pi2\int_0^4u^2\,du=\frac\pi2\cdot\frac{64}{3}=\frac{32\pi}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(r, (z, r, 2)), (r, 0, 2)), (th, 0, 2*pi)), 8*pi/3)
P(id="1-96", ch=15, sec="15.7", type="15-cyl", src="강의 15.7 (원뿔) 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$과 평면 $z=2$로 둘러싸인 입체의 부피를 원주좌표로 구하라.",
  hint=r"$r\le z\le2$, 원뿔과 평면은 $r=2$에서 만나요.",
  ans=r"$\dfrac{8\pi}{3}$",
  sol=[r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_r^2 r\,dz\,dr\,d\theta=2\pi\int_0^2(2-r)r\,dr$",
       r"$=2\pi\Big(4-\frac83\Big)=\frac{8\pi}{3}$ (원뿔 부피 공식 $\tfrac13\pi\cdot2^2\cdot2$와 일치)"],
  check=_c)


# ───────── 15.8 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(rho**2*rho**2*sin(ph), (rho, 0, 1)), (ph, 0, pi)), (th, 0, 2*pi)), 4*pi/5)
P(id="1-97", ch=15, sec="15.8", type="15-sph", src="과제 15.8 #23 유형",
  q=r"$B$가 단위 구 $x^2+y^2+z^2\le1$일 때 $\displaystyle\iiint_B (x^2+y^2+z^2)\,dV$를 계산하라.",
  hint=r"$x^2+y^2+z^2=\rho^2$, $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
  ans=r"$\dfrac{4\pi}{5}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^1\rho^2\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=2\pi\cdot2\cdot\dfrac15=\dfrac{4\pi}{5}$"],
  check=_c)


def _c():
    V = integrate(integrate(integrate(rho**2*sin(ph), (rho, 0, 2)), (ph, 0, pi/4)), (th, 0, 2*pi))
    assert EQ(V, 8*pi/3*(2 - sqrt(2)))
P(id="1-98", ch=15, sec="15.8", type="15-sph", src="과제 15.8 #17 · 과제 15.3 #35 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$ 위쪽, 구 $x^2+y^2+z^2=4$ 안쪽에 있는 입체의 부피를 구하라.",
  hint=r"원뿔 $z=\sqrt{x^2+y^2}$ → $\phi=\tfrac\pi4$, 구 → $\rho=2$",
  ans=r"$\dfrac{8\pi}{3}(2-\sqrt2)$",
  sol=[r"$0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi4,\ 0\le\rho\le2$",
       r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^2\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\Big(1-\frac{\sqrt2}{2}\Big)\frac83$",
       r"$=\dfrac{16\pi}{3}\Big(1-\dfrac{\sqrt2}{2}\Big)=\dfrac{8\pi}{3}(2-\sqrt2)$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, 2)), (ph, 0, pi/2)), (th, 0, 2*pi)), 4*pi)
P(id="1-99", ch=15, sec="15.8", type="15-sph", src="강의 15.8 유형",
  q=r"$E$가 위쪽 반구 $x^2+y^2+z^2\le4,\ z\ge0$일 때 $\displaystyle\iiint_E z\,dV$를 계산하라.",
  hint=r"$z=\rho\cos\phi$, 위쪽 반구는 $0\le\phi\le\tfrac\pi2$",
  ans=r"$4\pi$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^2(\rho\cos\phi)\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=2\pi\cdot\Big[\tfrac{\sin^2\phi}{2}\Big]_0^{\pi/2}\cdot\dfrac{2^4}{4}=2\pi\cdot\dfrac12\cdot4=4\pi$"],
  check=_c)


def _c():
    sph = integrate(integrate(integrate(rho**4*sin(ph), (rho, 0, 2)), (ph, 0, pi/2)), (th, 0, 2*pi))
    cyl = integrate(integrate(integrate((r**2 + z**2)*r, (z, 0, sqrt(4 - r**2))), (r, 0, 2)), (th, 0, 2*pi))
    assert EQ(sph, 64*pi/5) and EQ(cyl, 64*pi/5)
P(id="1-100", ch=15, sec="15.8", type="15-sphconv", src="강의 15.8 (구면좌표로 바꾸기) 유형",
  q=r"구면좌표로 바꾸어 계산하라. $$\int_{-2}^{2}\!\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}\!\int_0^{\sqrt{4-x^2-y^2}}(x^2+y^2+z^2)\,dz\,dy\,dx$$",
  hint=r"$xy$ 범위는 원판 $x^2+y^2\le4$, $z$는 $0$부터 위쪽 반구까지 → 위쪽 반구 전체",
  ans=r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^2\rho^4\sin\phi\,d\rho\,d\phi\,d\theta=\frac{64\pi}{5}$",
  sol=[r"영역: 반지름 $2$인 위쪽 반구 → $0\le\rho\le2,\ 0\le\phi\le\tfrac\pi2,\ 0\le\theta\le2\pi$",
       r"$(x^2+y^2+z^2)\,dV=\rho^2\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=2\pi\cdot1\cdot\dfrac{2^5}{5}=\dfrac{64\pi}{5}$"],
  check=_c)


def _c():
    cyl = integrate(integrate(integrate(z*r, (z, r, sqrt(2 - r**2))), (r, 0, 1)), (th, 0, 2*pi))
    sph = integrate(integrate(integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, sqrt(2))), (ph, 0, pi/4)), (th, 0, 2*pi))
    assert EQ(cyl, pi/2) and EQ(sph, pi/2)
P(id="1-101", ch=15, sec="15.8", type="15-sphconv", src="2025 중간 10번 · 2024 중간 8번 유형 (기초)",
  q=r"원주좌표로 주어진 적분을 구면좌표로 바꾸어 계산하라. $$\int_0^{2\pi}\!\!\int_0^1\!\!\int_r^{\sqrt{2-r^2}} z\,r\,dz\,dr\,d\theta$$",
  hint=r"$z=r$은 원뿔 $\phi=\tfrac\pi4$, $z=\sqrt{2-r^2}$은 구 $\rho=\sqrt2$. $r=1$은 둘이 만나는 원이에요.",
  ans=r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^{\sqrt2}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=\frac{\pi}{2}$",
  sol=[r"영역: 원뿔 $\phi=\tfrac\pi4$ 위, 구 $\rho=\sqrt2$ 안 (교선 $r=1,\ z=1$)",
       r"$z\,r\,dz\,dr\,d\theta=z\,dV=\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=2\pi\cdot\Big[\tfrac{\sin^2\phi}{2}\Big]_0^{\pi/4}\cdot\dfrac{(\sqrt2)^4}{4}=2\pi\cdot\dfrac14\cdot1=\dfrac\pi2$"],
  check=_c)

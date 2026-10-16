"""3단계 · 응용 추가분 — Ch.15 중적분: 3-72 ~ 3-101, 변수변환 3-124 ~ 3-126"""
from bank_lib import *
from sympy import asin, sec, csc
import mpmath as mp


def nquad2(f, xa, xb, ya, yb):
    """수치 이중적분 ∫_{xa}^{xb} ∫_{ya(x)}^{yb(x)} f(x,y) dy dx"""
    return mp.quad(lambda X: mp.quad(lambda Y: f(X, Y), [ya(X), yb(X)]), [xa, xb])


# ───────── 15.1 ─────────
def _c():
    f = x**2 + 2*y
    mids = [(R(1, 2), R(1, 2)), (R(1, 2), R(3, 2)), (R(3, 2), R(1, 2)), (R(3, 2), R(3, 2))]
    assert sum(f.subs({x: a, y: b}) for a, b in mids) == 13
    assert EQ(integrate(integrate(f, (y, 0, 2)), (x, 0, 2)), R(40, 3))
P(id="3-72", ch=15, sec="15.1", type="15-rect", src="강의 15.1 (중점법칙) 유형",
  q=r"$R=[0,2]\times[0,2]$를 $m=n=2$로 나누어 중점법칙으로 $\displaystyle\iint_R(x^2+2y)\,dA$를 근사하고, 실제 값과 비교하라.",
  hint=r"작은 정사각형 4개의 중점 $(0.5,0.5),(0.5,1.5),(1.5,0.5),(1.5,1.5)$, $\Delta A=1$",
  ans=r"중점법칙 근삿값 $13$,  실제 값 $\dfrac{40}{3}\approx13.33$",
  sol=[r"함숫값: $f(0.5,0.5)=1.25,\ f(0.5,1.5)=3.25,\ f(1.5,0.5)=3.25,\ f(1.5,1.5)=5.25$",
       r"근삿값 $=(1.25+3.25+3.25+5.25)\cdot1=13$",
       r"실제: $\displaystyle\int_0^2\!\!\int_0^2(x^2+2y)\,dy\,dx=\int_0^2(2x^2+4)\,dx=\frac{16}{3}+8=\frac{40}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(y*exp(-x*y), (x, 0, 2)), (y, 0, 3)), R(5, 2) + exp(-6)/2)
P(id="3-73", ch=15, sec="15.1", type="15-rect", src="강의 15.1 (적분 순서 선택) 유형",
  q=r"$\displaystyle\iint_R ye^{-xy}\,dA$를 계산하라. 단, $R=[0,2]\times[0,3]$ ($0\le x\le2,\ 0\le y\le3$).",
  hint=r"$x$로 먼저 적분하면 $y$가 상수라 $\int ye^{-xy}dx=-e^{-xy}$로 끝나요.",
  ans=r"$\dfrac52+\dfrac{e^{-6}}{2}$",
  sol=[r"안쪽 ($x$): $\displaystyle\int_0^2ye^{-xy}\,dx=\Big[-e^{-xy}\Big]_0^2=1-e^{-2y}$",
       r"바깥: $\displaystyle\int_0^3(1-e^{-2y})\,dy=3-\frac{1-e^{-6}}{2}=\frac52+\frac{e^{-6}}{2}$"],
  check=_c)


# ───────── 15.2 ─────────
def _c():
    I = integrate(integrate(exp(y**2), (x, y, 2*y)), (y, 0, 2))
    assert EQ(I, (exp(4) - 1)/2)
    num = nquad2(lambda X, Y: mp.e**(Y**2), 0, 2, lambda X: X/2, lambda X: X) + nquad2(lambda X, Y: mp.e**(Y**2), 2, 4, lambda X: X/2, lambda X: 2)
    assert abs(num - float((exp(4) - 1)/2)) < 1e-8
P(id="3-74", ch=15, sec="15.2", type="15-order", src="2022 중간(블럭1) 2(a) 유형",
  q=r"적분 영역을 그리고 계산하라. $$\int_0^2\!\int_{x/2}^{x}e^{y^2}\,dy\,dx+\int_2^4\!\int_{x/2}^{2}e^{y^2}\,dy\,dx$$",
  hint=r"두 영역을 합치면 직선 $y=\tfrac x2$와 $y=x$ 사이, $0\le y\le2$. $y$를 바깥으로 하면 하나의 적분",
  ans=r"$\dfrac{e^4-1}{2}$",
  sol=[r"영역: $0\le x\le2$에서 $\tfrac x2\le y\le x$, $2\le x\le4$에서 $\tfrac x2\le y\le2$ → 꼭짓점 $(0,0),(2,2),(4,2)$인 삼각형",
       r"$y$ 기준: $0\le y\le2,\ y\le x\le2y$",
       r"$\displaystyle\int_0^2\!\!\int_y^{2y}e^{y^2}\,dx\,dy=\int_0^2ye^{y^2}\,dy=\frac12\Big[e^{y^2}\Big]_0^2=\frac{e^4-1}{2}$"],
  check=_c)


def _c():
    f = x*y + x + 1
    I1 = integrate(integrate(f, (y, 0, (x + 2)/2)), (x, -2, 0)) + integrate(integrate(f, (y, 0, sqrt(1 - x**2))), (x, 0, 1))
    I2 = integrate(integrate(f, (x, 2*y - 2, sqrt(1 - y**2))), (y, 0, 1))
    assert EQ(I1, I2)
    A = integrate(integrate(1, (x, 2*y - 2, sqrt(1 - y**2))), (y, 0, 1))
    assert EQ(A, 1 + pi/4)
P(id="3-75", ch=15, sec="15.2", type="15-order", src="2022 중간(블럭1) 2(b) · 2022 생명과학대 기말 9번 유형",
  q=r"적분 영역을 그리고 다음 합을 적분 순서가 바뀐 하나의 반복적분으로 나타내라. (계산하지 않아도 됨) $$\int_{-2}^{0}\!\int_0^{(x+2)/2}f(x,y)\,dy\,dx+\int_0^{1}\!\int_0^{\sqrt{1-x^2}}f(x,y)\,dy\,dx$$ 또 $f=1$일 때 영역의 넓이를 구하라.",
  hint=r"경계: $x$축, 직선 $y=\tfrac{x+2}{2}$ (즉 $x=2y-2$), 사분원 $x^2+y^2=1$ ($x\ge0$). 둘은 $(0,1)$에서 만나요.",
  ans=r"$\displaystyle\int_0^1\!\!\int_{2y-2}^{\sqrt{1-y^2}}f(x,y)\,dx\,dy$,  넓이 $1+\dfrac\pi4$",
  sol=[r"첫째: $x\in[-2,0]$에서 $x$축과 직선 $y=\tfrac{x+2}{2}$ 사이 (꼭짓점 $(-2,0),(0,0),(0,1)$인 삼각형)",
       r"둘째: 1사분면의 사분원판. 합친 영역의 왼쪽 경계는 $x=2y-2$, 오른쪽 경계는 $x=\sqrt{1-y^2}$",
       r"$y$ 기준: $0\le y\le1,\ 2y-2\le x\le\sqrt{1-y^2}$ → $\displaystyle\int_0^1\!\!\int_{2y-2}^{\sqrt{1-y^2}}f\,dx\,dy$",
       r"넓이: 삼각형 $1$ + 사분원 $\tfrac\pi4$ $=1+\dfrac\pi4$"],
  check=_c)


def _c():
    I = integrate(integrate(cos(y)*exp(cos(y)**2), (x, 0, sin(y))), (y, 0, pi/2))
    assert EQ(I, (E - 1)/2)
P(id="3-76", ch=15, sec="15.2", type="15-order", src="2022 중간(블럭2) 6번 유형",
  q=r"곡면 $z=\cos y\,e^{\cos^2y}$ 아래, 영역 $D=\left\{(x,y)\ \middle|\ \sin^{-1}x\le y\le\tfrac\pi2,\ 0\le x\le1\right\}$ 위에 있는 입체의 부피를 구하라.",
  hint=r"$y$로 먼저는 불가능. $\sin^{-1}x\le y \iff x\le\sin y$ → $0\le y\le\tfrac\pi2,\ 0\le x\le\sin y$. 그다음 $u=\cos^2y$",
  ans=r"$\dfrac{e-1}{2}$",
  sol=[r"순서 바꾸기: $D=\{0\le y\le\tfrac\pi2,\ 0\le x\le\sin y\}$",
       r"$V=\displaystyle\int_0^{\pi/2}\!\!\int_0^{\sin y}\cos y\,e^{\cos^2y}\,dx\,dy=\int_0^{\pi/2}\sin y\cos y\,e^{\cos^2y}\,dy$",
       r"$u=\cos^2y,\ du=-2\sin y\cos y\,dy$: $\dfrac12\displaystyle\int_0^1e^u\,du=\frac{e-1}{2}$"],
  check=_c)


def _c():
    I = integrate(integrate(exp(cos(x)), (y, 0, sin(x))), (x, 0, pi/2))
    assert EQ(I, E - 1)
P(id="3-77", ch=15, sec="15.2", type="15-order", src="2022 생명과학대 기말 16(b) 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_{\sin^{-1}y}^{\pi/2}e^{\cos x}\,dx\,dy$를 계산하라.",
  hint=r"$e^{\cos x}$는 $x$로 바로 적분할 수 없어요. $\sin^{-1}y\le x \iff y\le\sin x$로 순서를 바꾸면 $\sin x$가 곱해져요.",
  ans=r"$e-1$",
  sol=[r"영역: $0\le y\le1,\ \sin^{-1}y\le x\le\tfrac\pi2$ $\iff$ $0\le x\le\tfrac\pi2,\ 0\le y\le\sin x$",
       r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^{\sin x}e^{\cos x}\,dy\,dx=\int_0^{\pi/2}\sin x\,e^{\cos x}\,dx$",
       r"$u=\cos x$: $\displaystyle\int_0^1e^u\,du=e-1$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(sin(y**2), (x, -y, y)), (y, 0, 1)), 1 - cos(1))
P(id="3-78", ch=15, sec="15.2", type="15-order", src="2022 생명과학대 기말 16(a) 유형",
  q=r"$\displaystyle\int_{-1}^{1}\!\!\int_{|x|}^{1}\sin(y^2)\,dy\,dx$를 계산하라.",
  hint=r"영역은 $|x|\le y\le1$ (V자 아래쪽이 아니라 위쪽 삼각형). $y$를 바깥으로: $-y\le x\le y$",
  ans=r"$1-\cos1$",
  sol=[r"영역: $0\le y\le1,\ -y\le x\le y$ (꼭짓점 $(0,0),(-1,1),(1,1)$)",
       r"$\displaystyle\int_0^1\!\!\int_{-y}^{y}\sin(y^2)\,dx\,dy=\int_0^12y\sin(y^2)\,dy$",
       r"$=\Big[-\cos(y^2)\Big]_0^1=1-\cos1$"],
  check=_c)


def _c():
    V = integrate(integrate(z, (z, x**2, sqrt(2 - x**2))), (x, 0, 1))
    assert EQ(V, R(11, 15))
    assert solve(x**4 + x**2 - 2, x).count(1) == 1
P(id="3-79", ch=15, sec="15.2", type="15-general", src="2022 생명과학대 기말 10번 유형",
  q=r"제1팔분면에서 두 원기둥 $x^2+z^2=2$, $z=x^2$과 평면 $x=0$, $y=0$, $y=z$로 둘러싸인 입체의 부피를 구하라.",
  hint=r"$xz$평면의 밑면: $x^2\le z\le\sqrt{2-x^2}$ ($0\le x\le1$), 높이 방향은 $y$: $0\le y\le z$",
  ans=r"$\dfrac{11}{15}$",
  sol=[r"두 곡선의 교점: $x^2=\sqrt{2-x^2} \Rightarrow x^4+x^2-2=0 \Rightarrow x^2=1$",
       r"$V=\displaystyle\int_0^1\!\!\int_{x^2}^{\sqrt{2-x^2}}\!\!\int_0^z dy\,dz\,dx=\int_0^1\frac{(2-x^2)-x^4}{2}dx$",
       r"$=\dfrac12\Big(2-\dfrac13-\dfrac15\Big)=\dfrac{11}{15}$"],
  check=_c)


# ───────── 15.3 ─────────
def _c():
    A_pol = integrate(integrate(r, (r, 1, sqrt(3)/cos(th))), (th, 0, pi/6)) + integrate(integrate(r, (r, 1, 1/sin(th))), (th, pi/6, pi/2))
    assert EQ(A_pol, sqrt(3) - pi/4)
    A_cart = integrate(integrate(1, (y, sqrt(1 - x**2), 1)), (x, 0, 1)) + integrate(integrate(1, (y, 0, 1)), (x, 1, sqrt(3)))
    assert EQ(A_cart, sqrt(3) - pi/4)
    fn = lambda X, Y: X*Y + 1
    cart = nquad2(fn, 0, 1, lambda X: mp.sqrt(1 - X**2), lambda X: 1) + nquad2(fn, 1, mp.sqrt(3), lambda X: 0, lambda X: 1)
    pol = (mp.quad(lambda T: mp.quad(lambda Rr: fn(Rr*mp.cos(T), Rr*mp.sin(T))*Rr, [1, mp.sqrt(3)/mp.cos(T)]), [0, mp.pi/6])
           + mp.quad(lambda T: mp.quad(lambda Rr: fn(Rr*mp.cos(T), Rr*mp.sin(T))*Rr, [1, 1/mp.sin(T)]), [mp.pi/6, mp.pi/2]))
    assert abs(cart - pol) < 1e-8
P(id="3-80", ch=15, sec="15.3", type="15-polar", src="2025 중간 2(b) 유형",
  q=r"다음 적분의 합을 극좌표 적분으로 바꾸어 나타내라. $$\int_0^1\!\int_{\sqrt{1-x^2}}^{1}f(x,y)\,dy\,dx+\int_1^{\sqrt3}\!\int_0^{1}f(x,y)\,dy\,dx$$ 또 $f=1$일 때 두 표현이 같은 넓이를 주는지 확인하라.",
  hint=r"영역: 직사각형 $[0,\sqrt3]\times[0,1]$에서 단위원 안쪽을 뺀 부분. 직선 $x=\sqrt3$은 $r=\sqrt3\sec\theta$, $y=1$은 $r=\csc\theta$, 꼭짓점 $(\sqrt3,1)$은 $\theta=\tfrac\pi6$",
  ans=r"$\displaystyle\int_0^{\pi/6}\!\!\int_1^{\sqrt3\sec\theta}f\,r\,dr\,d\theta+\int_{\pi/6}^{\pi/2}\!\!\int_1^{\csc\theta}f\,r\,dr\,d\theta$,  넓이 $\sqrt3-\dfrac\pi4$",
  sol=[r"영역: $0\le x\le\sqrt3,\ 0\le y\le1$이면서 $x^2+y^2\ge1$",
       r"$0\le\theta\le\tfrac\pi6$: 바깥 경계가 $x=\sqrt3$ → $1\le r\le\sqrt3\sec\theta$",
       r"$\tfrac\pi6\le\theta\le\tfrac\pi2$: 바깥 경계가 $y=1$ → $1\le r\le\csc\theta$",
       r"$f=1$: $\tfrac12\big[\sqrt3\tan\theta\cdot\sqrt3-\theta\big]$ 계산하면 $\Big(\tfrac{\sqrt3}{2}-\tfrac\pi{12}\Big)+\Big(\tfrac{\sqrt3}{2}-\tfrac\pi6\Big)=\sqrt3-\tfrac\pi4$",
       r"직교좌표: 직사각형 $\sqrt3$ − 사분원 $\tfrac\pi4$ ✓"],
  check=_c)


def _c():
    m = integrate(integrate(r*r, (r, 1, 2)), (th, -pi/4, pi/4))
    My = integrate(integrate(r*cos(th)*r*r, (r, 1, 2)), (th, -pi/4, pi/4))
    assert EQ(m, 7*pi/6) and EQ(My/m, 45*sqrt(2)/(14*pi))
    rho_ = lambda X, Y: mp.sqrt(X**2 + Y**2)
    cart = (nquad2(rho_, 1/mp.sqrt(2), 1, lambda X: mp.sqrt(1 - X**2), lambda X: X)
            + nquad2(rho_, 1/mp.sqrt(2), 1, lambda X: -X, lambda X: -mp.sqrt(1 - X**2))
            + nquad2(rho_, 1, mp.sqrt(2), lambda X: -X, lambda X: X)
            + nquad2(rho_, mp.sqrt(2), 2, lambda X: -mp.sqrt(4 - X**2), lambda X: mp.sqrt(4 - X**2)))
    assert abs(cart - float(7*pi/6)) < 1e-8
P(id="3-81", ch=15, sec="15.3", type="15-mass", src="2022 중간(블럭2) 7번 유형",
  q=r"(a) 다음 합을 극좌표로 하나의 이중적분으로 나타내라. $$\int_{1/\sqrt2}^{1}\!\!\int_{\sqrt{1-x^2}}^{x}f\,dy\,dx+\int_{1/\sqrt2}^{1}\!\!\int_{-x}^{-\sqrt{1-x^2}}f\,dy\,dx+\int_1^{\sqrt2}\!\!\int_{-x}^{x}f\,dy\,dx+\int_{\sqrt2}^{2}\!\!\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}f\,dy\,dx$$ (b) 이 영역 모양의 판의 밀도가 $\rho=\sqrt{x^2+y^2}$일 때 질량중심을 구하라.",
  hint=r"(a) 경계: 원 $r=1$, 원 $r=2$, 직선 $y=\pm x$ → $1\le r\le2,\ -\tfrac\pi4\le\theta\le\tfrac\pi4$. (b) $x$축 대칭이라 $\bar y=0$",
  ans=r"(a) $\displaystyle\int_{-\pi/4}^{\pi/4}\!\!\int_1^2 f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$  (b) $\left(\dfrac{45\sqrt2}{14\pi},\ 0\right)$",
  sol=[r"(a) 네 조각을 합치면 $y=-x$와 $y=x$ 사이의 고리 $1\le r\le2$ ($|\theta|\le\tfrac\pi4$)",
       r"(b) $m=\displaystyle\int_{-\pi/4}^{\pi/4}\!\!\int_1^2r\cdot r\,dr\,d\theta=\frac\pi2\cdot\frac73=\frac{7\pi}{6}$",
       r"$M_y=\displaystyle\iint x\rho\,dA=\int_{-\pi/4}^{\pi/4}\cos\theta\,d\theta\int_1^2r^3\,dr=\sqrt2\cdot\frac{15}{4}$",
       r"$\bar x=\dfrac{15\sqrt2/4}{7\pi/6}=\dfrac{45\sqrt2}{14\pi}\approx1.45$,  $\bar y=0$"],
  check=_c)


def _c():
    I1 = integrate(integrate(r**3, (r, 0, 1)), (th, 0, 2*pi))
    I2 = integrate(integrate(r**3, (r, 1, 2*sin(th))), (th, pi/6, 5*pi/6))
    assert EQ(I1 + I2, 4*pi/3 + 7*sqrt(3)/8)
    num = mp.quad(lambda T: mp.quad(lambda Rr: Rr**3, [0, max(1, 2*mp.sin(T)) if mp.sin(T) > 0 else 1]), [0, mp.pi/6, 5*mp.pi/6, mp.pi, 2*mp.pi])
    assert abs(num - float(4*pi/3 + 7*sqrt(3)/8)) < 1e-6
P(id="3-82", ch=15, sec="15.3", type="15-polar", src="2024 중간 6번 유형",
  q=r"$D_1$, $D_2$가 각각 원판 $x^2+y^2\le1$, $x^2+y^2\le2y$일 때 $\displaystyle\iint_{D_1\cup D_2}(x^2+y^2)\,dA$를 계산하라.",
  hint=r"$D_1\cup D_2=D_1\ \cup\ (D_2$ 중 $D_1$ 밖의 부분$)$. $D_2$: $r\le2\sin\theta$, 두 원은 $2\sin\theta=1$, 즉 $\theta=\tfrac\pi6,\tfrac{5\pi}6$에서 만나요.",
  ans=r"$\dfrac{4\pi}{3}+\dfrac{7\sqrt3}{8}$",
  sol=[r"$D_1$: $\displaystyle\int_0^{2\pi}\!\!\int_0^1r^3\,dr\,d\theta=\frac\pi2$",
       r"$D_2\setminus D_1$: $\tfrac\pi6\le\theta\le\tfrac{5\pi}{6},\ 1\le r\le2\sin\theta$ → $\displaystyle\int_{\pi/6}^{5\pi/6}\frac{16\sin^4\theta-1}{4}d\theta$",
       r"$\displaystyle\int_{\pi/6}^{5\pi/6}\sin^4\theta\,d\theta=\Big[\tfrac{3\theta}{8}-\tfrac{\sin2\theta}{4}+\tfrac{\sin4\theta}{32}\Big]_{\pi/6}^{5\pi/6}=\frac\pi4+\frac{7\sqrt3}{32}$",
       r"$D_2\setminus D_1$ 부분 $=4\Big(\dfrac\pi4+\dfrac{7\sqrt3}{32}\Big)-\dfrac14\cdot\dfrac{2\pi}{3}=\dfrac{5\pi}{6}+\dfrac{7\sqrt3}{8}$",
       r"합: $\dfrac\pi2+\dfrac{5\pi}{6}+\dfrac{7\sqrt3}{8}=\dfrac{4\pi}{3}+\dfrac{7\sqrt3}{8}$"],
  check=_c)


def _c():
    A = 2*integrate(integrate(r, (r, sqrt(2), 2*sqrt(cos(2*th)))), (th, -pi/6, pi/6))
    assert EQ(A, 2*sqrt(3) - 2*pi/3)
P(id="3-83", ch=15, sec="15.3", type="15-polar", src="2022 생명과학대 중간 13번 유형",
  q=r"렘니스케이트 $r^2=4\cos2\theta$의 안쪽이면서 원 $r=\sqrt2$의 바깥쪽인 영역의 넓이를 구하라.",
  hint=r"$4\cos2\theta\ge2 \iff |\theta|\le\tfrac\pi6$ (오른쪽 고리). 고리가 두 개예요.",
  ans=r"$2\sqrt3-\dfrac{2\pi}{3}$",
  sol=[r"교점: $4\cos2\theta=2 \Rightarrow \theta=\pm\tfrac\pi6$",
       r"오른쪽 고리: $\displaystyle\int_{-\pi/6}^{\pi/6}\!\!\int_{\sqrt2}^{2\sqrt{\cos2\theta}}r\,dr\,d\theta=\int_0^{\pi/6}(4\cos2\theta-2)\,d\theta$",
       r"$=\Big[2\sin2\theta-2\theta\Big]_0^{\pi/6}=\sqrt3-\dfrac\pi3$",
       r"고리 두 개: $2\sqrt3-\dfrac{2\pi}{3}$"],
  check=_c)


def _c():
    I = integrate(integrate(r**3, (r, 0, 1/cos(th))), (th, 0, pi/4)) + integrate(integrate(r**3, (r, 0, 1/sin(th))), (th, pi/4, pi/2))
    assert EQ(I, R(2, 3))
    assert EQ(integrate(integrate(x**2 + y**2, (y, 0, 1)), (x, 0, 1)), R(2, 3))
P(id="3-84", ch=15, sec="15.3", type="15-polar", src="복습 15.1–3 심화2 유형",
  q=r"다음 극좌표 적분의 합이 나타내는 영역과 피적분함수를 직교좌표로 해석해 값을 구하라. $$\int_0^{\pi/4}\!\!\int_0^{\sec\theta}r^3\,dr\,d\theta+\int_{\pi/4}^{\pi/2}\!\!\int_0^{\csc\theta}r^3\,dr\,d\theta$$",
  hint=r"$r=\sec\theta \iff x=1$, $r=\csc\theta \iff y=1$. $r^3\,dr\,d\theta=r^2\cdot r\,dr\,d\theta=(x^2+y^2)\,dA$",
  ans=r"$\displaystyle\iint_{[0,1]^2}(x^2+y^2)\,dA=\frac23$",
  sol=[r"첫째: $0\le\theta\le\tfrac\pi4$에서 원점부터 직선 $x=1$까지 → 정사각형의 아래 삼각형",
       r"둘째: $\tfrac\pi4\le\theta\le\tfrac\pi2$에서 직선 $y=1$까지 → 위 삼각형. 합치면 정사각형 $[0,1]^2$",
       r"$\displaystyle\int_0^1\!\!\int_0^1(x^2+y^2)\,dy\,dx=\frac13+\frac13=\frac23$"],
  check=_c)


def _c():
    m = integrate(integrate(1, (r, 1, 2*cos(th))), (th, -pi/3, pi/3))
    My = integrate(integrate(r*cos(th), (r, 1, 2*cos(th))), (th, -pi/3, pi/3))
    assert EQ(m, 2*sqrt(3) - 2*pi/3) and EQ(My, sqrt(3))
    assert EQ(My/m, 3*sqrt(3)/(6*sqrt(3) - 2*pi))
P(id="3-85", ch=15, sec="15.3", type="15-mass", src="2025 중간 1번 유형",
  q=r"원 $x^2+y^2=2x$의 안쪽이면서 원 $x^2+y^2=1$의 바깥쪽인 영역을 차지하는 판의 밀도가 $\rho(x,y)=\dfrac{1}{\sqrt{x^2+y^2}}$일 때 질량중심을 구하라.",
  hint=r"$1\le r\le2\cos\theta$, 교점 $2\cos\theta=1 \Rightarrow \theta=\pm\tfrac\pi3$. $\rho\,dA=\tfrac1r\cdot r\,dr\,d\theta=dr\,d\theta$",
  ans=r"$\left(\dfrac{3\sqrt3}{6\sqrt3-2\pi},\ 0\right)$ ($\bar x\approx1.31$)",
  sol=[r"$m=\displaystyle\int_{-\pi/3}^{\pi/3}\!\!\int_1^{2\cos\theta}dr\,d\theta=\int_{-\pi/3}^{\pi/3}(2\cos\theta-1)\,d\theta=2\sqrt3-\frac{2\pi}{3}$",
       r"$M_y=\displaystyle\int_{-\pi/3}^{\pi/3}\!\!\int_1^{2\cos\theta}r\cos\theta\,dr\,d\theta=\int_{-\pi/3}^{\pi/3}\frac{4\cos^3\theta-\cos\theta}{2}d\theta$",
       r"$\displaystyle\int_{-\pi/3}^{\pi/3}\cos^3\theta\,d\theta=2\Big[\sin\theta-\tfrac{\sin^3\theta}{3}\Big]_0^{\pi/3}=\frac{3\sqrt3}{4}$ → $M_y=\dfrac{3\sqrt3}{2}-\dfrac{\sqrt3}{2}=\sqrt3$",
       r"$\bar x=\dfrac{\sqrt3}{2\sqrt3-2\pi/3}=\dfrac{3\sqrt3}{6\sqrt3-2\pi}$, $x$축 대칭으로 $\bar y=0$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(r*r, (r, 0, 1 + cos(th))), (th, 0, 2*pi)), 5*pi/3)
P(id="3-86", ch=15, sec="15.3", type="15-polar", src="2025 중간 7번의 영역 (심장형)",
  q=r"심장형 $r=1+\cos\theta$로 둘러싸인 영역 $D$에서 $\displaystyle\iint_D\sqrt{x^2+y^2}\,dA$를 계산하라.",
  hint=r"$\sqrt{x^2+y^2}=r$이라 $r\cdot r\,dr$. $(1+\cos\theta)^3$을 전개해 한 주기 적분",
  ans=r"$\dfrac{5\pi}{3}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{1+\cos\theta}r^2\,dr\,d\theta=\frac13\int_0^{2\pi}(1+\cos\theta)^3\,d\theta$",
       r"$(1+\cos\theta)^3=1+3\cos\theta+3\cos^2\theta+\cos^3\theta$ → 한 주기 적분 $2\pi+0+3\pi+0=5\pi$",
       r"$\dfrac13\cdot5\pi=\dfrac{5\pi}{3}$"],
  check=_c)


# ───────── 15.6 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(x**2, (z, 0, y)), (y, x**2, 1)), (x, -1, 1)), R(4, 21))
P(id="3-87", ch=15, sec="15.6", type="15-triple", src="2024 중간 2(b) 유형",
  q=r"$E$가 곡면 $y=x^2$, $y=1$, $z=0$, $z=y$로 둘러싸인 입체일 때 $\displaystyle\iiint_E x^2\,dV$를 계산하라.",
  hint=r"밑면 $D$: $-1\le x\le1,\ x^2\le y\le1$, 높이 $0\le z\le y$",
  ans=r"$\dfrac{4}{21}$",
  sol=[r"$\displaystyle\int_{-1}^{1}\!\!\int_{x^2}^{1}\!\!\int_0^{y}x^2\,dz\,dy\,dx=\int_{-1}^1\!\!\int_{x^2}^1x^2y\,dy\,dx$",
       r"$=\displaystyle\int_{-1}^1x^2\cdot\frac{1-x^4}{2}\,dx=\frac12\Big(\frac23-\frac27\Big)=\frac{4}{21}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(z, (z, 0, 1 - x**2)), (y, 0, 1 - x)), (x, 0, 1)), R(11, 60))
P(id="3-88", ch=15, sec="15.6", type="15-triple", src="과제 15.6 #17 유형",
  q=r"$E=\{(x,y,z)\mid 0\le x\le1,\ 0\le y\le1-x,\ 0\le z\le1-x^2\}$일 때 $\displaystyle\iiint_E z\,dV$를 계산하라.",
  hint=r"$\int_0^{1-x^2}z\,dz=\tfrac{(1-x^2)^2}{2}$, 그다음 $y$ 적분은 길이 $1-x$를 곱하는 것",
  ans=r"$\dfrac{11}{60}$",
  sol=[r"$\displaystyle\int_0^1(1-x)\frac{(1-x^2)^2}{2}dx=\frac12\int_0^1(1-x-2x^2+2x^3+x^4-x^5)\,dx$",
       r"$=\dfrac12\Big(1-\dfrac12-\dfrac23+\dfrac12+\dfrac15-\dfrac16\Big)=\dfrac12\cdot\dfrac{11}{30}=\dfrac{11}{60}$"],
  check=_c)


def _c():
    I_new = integrate(6*exp(z**3)*z**2/2, (z, 0, 1))
    assert EQ(I_new, E - 1)
    g = z**5 + 3*z**2      # 순서 바꾸기 확인용 다항식
    assert EQ(integrate(integrate(integrate(g, (z, x + y, 1)), (y, 0, 1 - x)), (x, 0, 1)), integrate(g*z**2/2, (z, 0, 1)))
P(id="3-89", ch=15, sec="15.6", type="15-order3", src="2025 중간 9번 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^1\!\!\int_0^{1-x}\!\!\int_{x+y}^{1}6e^{z^3}\,dz\,dy\,dx$를 계산하라.",
  hint=r"영역: $x,y\ge0,\ x+y\le z\le1$. $z$를 바깥으로 두면 단면은 넓이 $\tfrac{z^2}{2}$인 삼각형",
  ans=r"$e-1$",
  sol=[r"$z$를 고정하면 $x\ge0,\ y\ge0,\ x+y\le z$ → 직각이등변삼각형, 넓이 $\tfrac{z^2}{2}$",
       r"$\displaystyle\int_0^1\!\!\int_0^z\!\!\int_0^{z-x}6e^{z^3}\,dy\,dx\,dz=\int_0^16e^{z^3}\cdot\frac{z^2}{2}\,dz$",
       r"$=\displaystyle\int_0^13z^2e^{z^3}\,dz=\Big[e^{z^3}\Big]_0^1=e-1$"],
  check=_c)


def _c():
    f = y*z + 1
    I1 = integrate(integrate(2*sqrt(1 - z)*f, (z, 0, 1 - y)), (y, 0, 1))
    I2 = integrate(integrate(integrate(f, (z, 0, 1 - x**2)), (y, 0, x**2)) + integrate(integrate(f, (z, 0, 1 - y)), (y, x**2, 1)), (x, -1, 1))
    assert EQ(I1, I2)
    V = integrate(integrate(integrate(1, (x, -sqrt(1 - z), sqrt(1 - z))), (z, 0, 1 - y)), (y, 0, 1))
    assert EQ(V, R(4, 5))
P(id="3-90", ch=15, sec="15.6", type="15-order3", src="2022 중간(블럭2) 8(a) 유형",
  q=r"$\displaystyle\int_0^1\!\!\int_0^{1-y}\!\!\int_{-\sqrt{1-z}}^{\sqrt{1-z}}f(x,y,z)\,dx\,dz\,dy$를 $dz\,dy\,dx$ 순서의 적분으로 다시 쓰고, $f=1$일 때의 값을 구하라.",
  hint=r"영역: $0\le y\le1,\ 0\le z\le1-y,\ x^2\le1-z$. $x$를 고정하면 $z\le\min(1-x^2,\ 1-y)$ → $y$가 $x^2$보다 작은지 큰지로 나눠요.",
  ans=r"$\displaystyle\int_{-1}^{1}\Big[\int_0^{x^2}\!\!\int_0^{1-x^2}f\,dz\,dy+\int_{x^2}^{1}\!\!\int_0^{1-y}f\,dz\,dy\Big]dx$,  값 $\dfrac45$",
  sol=[r"$x$의 범위: $x^2\le1-z\le1$ → $-1\le x\le1$",
       r"$x$ 고정: $z\le1-x^2$이고 $z\le1-y$. $0\le y\le x^2$이면 $1-x^2\le1-y$ → $z\le1-x^2$",
       r"$x^2\le y\le1$이면 $z\le1-y$ → 두 적분의 합",
       r"$f=1$: $\displaystyle\int_{-1}^1\Big[x^2(1-x^2)+\frac{(1-x^2)^2}{2}\Big]dx=\int_{-1}^1\frac{1-x^4}{2}dx=\frac45$"],
  check=_c)


def _c():
    V_pol = 2*(integrate(integrate((R(4, 3) - r**2)*r, (r, 0, 1/cos(th))), (th, 0, pi/6))
               + integrate(integrate((R(4, 3) - r**2)*r, (r, 0, 2/sqrt(3))), (th, pi/6, pi/4)))
    assert EQ(V_pol, (7*sqrt(3) + 2*pi)/27)
    num = mp.quad(lambda X: mp.quad(lambda Y: max(0, mp.mpf(4)/3 - X**2 - Y**2), [0, mp.sqrt(max(0, mp.mpf(4)/3 - X**2)), 1]), [0, 1])
    assert abs(num - float((7*sqrt(3) + 2*pi)/27)) < 1e-7
P(id="3-91", ch=15, sec="15.6", type="15-triple", src="2024 중간 9번 유형",
  q=r"포물면 $z=x^2+y^2$ 위쪽이면서 상자 $B=\{(x,y,z)\mid0\le x\le1,\ 0\le y\le1,\ 0\le z\le\tfrac43\}$ 안에 있는 입체의 부피를 구하라.",
  hint=r"$x^2+y^2\le\tfrac43$인 곳에서만 높이 $\tfrac43-(x^2+y^2)$. 원 $r=\tfrac{2}{\sqrt3}$과 직선 $x=1$은 $\theta=\tfrac\pi6$에서 만나요. 직선 $y=x$ 대칭을 쓰면 편해요.",
  ans=r"$\dfrac{7\sqrt3+2\pi}{27}$",
  sol=[r"$y=x$에 대해 대칭 → $0\le\theta\le\tfrac\pi4$ 부분의 2배",
       r"$0\le\theta\le\tfrac\pi6$: $r\le\sec\theta$ (정사각형 변이 먼저) → $\displaystyle\int_0^{\pi/6}\Big(\tfrac23\sec^2\theta-\tfrac14\sec^4\theta\Big)d\theta=\frac{2}{3\sqrt3}-\frac14\cdot\frac{10}{9\sqrt3}=\frac{7}{18\sqrt3}$",
       r"$\tfrac\pi6\le\theta\le\tfrac\pi4$: $r\le\tfrac{2}{\sqrt3}$ → $\displaystyle\int_0^{2/\sqrt3}\Big(\tfrac43-r^2\Big)r\,dr=\frac49$, 각도 폭 $\tfrac{\pi}{12}$ → $\dfrac{\pi}{27}$",
       r"$V=2\Big(\dfrac{7}{18\sqrt3}+\dfrac{\pi}{27}\Big)=\dfrac{7\sqrt3}{27}+\dfrac{2\pi}{27}$"],
  check=_c)


def _c():
    V = integrate(integrate(integrate(1, (z, 0, 1 - x - y)), (y, 0, 1 - x)), (x, 0, 1))
    Mz = integrate(integrate(integrate(x, (z, 0, 1 - x - y)), (y, 0, 1 - x)), (x, 0, 1))
    assert EQ(V, R(1, 6)) and EQ(Mz/V, R(1, 4))
P(id="3-92", ch=15, sec="15.6", type="15-mass", src="강의 15.6 ex6 (질량중심) 유형",
  q=r"밀도가 일정한 사면체 $E$ (평면 $x+y+z=1$과 세 좌표평면으로 둘러싸인 입체)의 질량중심을 구하라.",
  hint=r"$\bar x=\dfrac{1}{V}\displaystyle\iiint_Ex\,dV$, 세 좌표에 대해 대칭이라 $\bar x=\bar y=\bar z$",
  ans=r"$\left(\dfrac14,\ \dfrac14,\ \dfrac14\right)$",
  sol=[r"부피 $V=\dfrac16$",
       r"$\displaystyle\iiint_Ex\,dV=\frac{1}{24}$ (1-89와 같은 계산)",
       r"$\bar x=\dfrac{1/24}{1/6}=\dfrac14$, 대칭으로 $\bar y=\bar z=\dfrac14$ (꼭짓점 평균과 같아요)"],
  check=_c)


# ───────── 15.7 ─────────
def _c():
    I = integrate(integrate(integrate(r*sin(th)*r, (z, r**2, 2*r*cos(th))), (r, 0, 2*cos(th))), (th, 0, pi/2))
    assert EQ(I, R(4, 15))
P(id="3-93", ch=15, sec="15.7", type="15-cyl", src="2025 중간 4번 유형",
  q=r"$E$가 포물면 $z=x^2+y^2$과 평면 $z=2x$로 둘러싸인 입체 중 $y\ge0$인 부분일 때 $\displaystyle\iiint_E y\,dV$를 계산하라.",
  hint=r"교선: $x^2+y^2=2x \iff r=2\cos\theta$. $y\ge0$이면 $0\le\theta\le\tfrac\pi2$, $r^2\le z\le2r\cos\theta$",
  ans=r"$\dfrac{4}{15}$",
  sol=[r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^{2\cos\theta}\!\!\int_{r^2}^{2r\cos\theta}r\sin\theta\cdot r\,dz\,dr\,d\theta=\int_0^{\pi/2}\sin\theta\int_0^{2\cos\theta}(2r^3\cos\theta-r^4)\,dr\,d\theta$",
       r"안쪽: $2\cos\theta\cdot\dfrac{16\cos^4\theta}{4}-\dfrac{32\cos^5\theta}{5}=\dfrac{8\cos^5\theta}{5}$",
       r"$\displaystyle\frac85\int_0^{\pi/2}\cos^5\theta\sin\theta\,d\theta=\frac85\cdot\frac16=\frac{4}{15}$"],
  check=_c)


def _c():
    num = mp.quad(lambda T: mp.quad(lambda Rr: (Rr + mp.sqrt(4 - Rr**2))*Rr, [0, 2*mp.cos(T)]), [-mp.pi/2, 0, mp.pi/2])
    assert abs(num - float(8*pi/3)) < 1e-8
P(id="3-94", ch=15, sec="15.7", type="15-cyl", src="2022 중간(블럭1) 9번 유형",
  q=r"원기둥 $x^2+y^2=2x$ 안쪽에서, 반구 $z=-\sqrt{4-x^2-y^2}$ 위, 원뿔 $z=\sqrt{x^2+y^2}$ 아래에 있는 입체의 부피를 구하라.",
  hint=r"높이 $=r-\big(-\sqrt{4-r^2}\big)$, 밑면 $r\le2\cos\theta$. $(4-4\cos^2\theta)^{3/2}=8|\sin\theta|^3$에 주의",
  ans=r"$\dfrac{8\pi}{3}$",
  sol=[r"$V=\displaystyle\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}\big(r+\sqrt{4-r^2}\big)r\,dr\,d\theta$",
       r"$\displaystyle\int_0^{2\cos\theta}r^2dr=\frac{8\cos^3\theta}{3}$,  $\displaystyle\int_0^{2\cos\theta}r\sqrt{4-r^2}\,dr=\frac{8-8|\sin\theta|^3}{3}$",
       r"$V=\dfrac83\displaystyle\int_{-\pi/2}^{\pi/2}\big(\cos^3\theta+1-|\sin\theta|^3\big)d\theta=\frac83\Big(\frac43+\pi-\frac43\Big)=\frac{8\pi}{3}$"],
  check=_c)


def _c():
    V = 2*pi*(integrate((7 - r**2)*r, (r, 0, 1)) + integrate((7 - r**2 - sqrt(r**2 - 1))*r, (r, 1, sqrt(5))))
    assert EQ(V, 103*pi/6)
    assert solve(1 + z**2 - (7 - z), z) == [-3, 2]
P(id="3-95", ch=15, sec="15.7", type="15-cyl", src="2022 중간(블럭2) 9번 유형",
  q=r"$E$가 한 장 쌍곡면 $x^2+y^2-z^2=1$의 안쪽에서, 평면 $z=0$ 위, 포물면 $z=7-x^2-y^2$ 아래에 있는 입체일 때 $\displaystyle\iiint_E(2+x+y)\,dV$를 계산하라.",
  hint=r"쌍곡면 안쪽: $r^2\le1+z^2$. 포물면과 만나는 곳: $1+z^2=7-z \Rightarrow z=2,\ r=\sqrt5$. $x,y$ 항은 대칭으로 $0$",
  ans=r"$\dfrac{103\pi}{3}$",
  sol=[r"$x$, $y$는 원점 대칭인 영역에서 홀함수 → $\displaystyle\iiint(x+y)\,dV=0$, 남는 것 $2V$",
       r"$0\le r\le1$: $0\le z\le7-r^2$.  $1\le r\le\sqrt5$: $\sqrt{r^2-1}\le z\le7-r^2$",
       r"$V=2\pi\Big[\displaystyle\int_0^1(7-r^2)r\,dr+\int_1^{\sqrt5}\big(7-r^2-\sqrt{r^2-1}\big)r\,dr\Big]=2\pi\Big[\frac{13}{4}+\Big(8-\frac83\Big)\Big]=\frac{103\pi}{6}$",
       r"$\displaystyle\iiint_E(2+x+y)\,dV=2\cdot\frac{103\pi}{6}=\frac{103\pi}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(r*r, (z, 1 - r**2, 4)), (r, 0, 1)), (th, 0, pi)), 6*pi/5)
P(id="3-96", ch=15, sec="15.7", type="15-mass", src="복습 15.6–8 기초2 유형",
  q=r"원기둥 $x^2+y^2=1$ 안쪽, $xz$평면의 오른쪽($y\ge0$), 평면 $z=4$ 아래, 포물면 $z=1-x^2-y^2$ 위에 있는 입체의 밀도가 원기둥의 축($z$축)까지의 거리와 같을 때 질량을 구하라.",
  hint=r"밀도 $=r$, $dV=r\,dz\,dr\,d\theta$ → 피적분함수 $r^2$",
  ans=r"$\dfrac{6\pi}{5}$",
  sol=[r"$m=\displaystyle\int_0^{\pi}\!\!\int_0^1\!\!\int_{1-r^2}^{4}r\cdot r\,dz\,dr\,d\theta=\pi\int_0^1r^2(3+r^2)\,dr$",
       r"$=\pi\Big(1+\dfrac15\Big)=\dfrac{6\pi}{5}$"],
  check=_c)


# ───────── 15.8 ─────────
def _c():
    assert EQ(integrate(integrate(integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, cos(ph)**3)), (ph, 0, pi/2)), (th, 0, 2*pi)), pi/28)
P(id="3-97", ch=15, sec="15.8", type="15-sph", src="2024 중간 10번 유형",
  q=r"$E$가 곡면 $(x^2+y^2+z^2)^2=z^3$으로 둘러싸인 입체일 때 $\displaystyle\iiint_E z\,dV$를 계산하라.",
  hint=r"구면좌표: $\rho^4=\rho^3\cos^3\phi \Rightarrow \rho=\cos^3\phi$ ($0\le\phi\le\tfrac\pi2$)",
  ans=r"$\dfrac{\pi}{28}$",
  sol=[r"$\rho=\cos^3\phi\ge0$이려면 $0\le\phi\le\tfrac\pi2$, $0\le\theta\le2\pi$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{\cos^3\phi}\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\int_0^{\pi/2}\cos\phi\sin\phi\frac{\cos^{12}\phi}{4}d\phi$",
       r"$=\dfrac\pi2\displaystyle\int_0^{\pi/2}\cos^{13}\phi\sin\phi\,d\phi=\frac\pi2\cdot\frac{1}{14}=\frac{\pi}{28}$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(rho**2*sin(ph), (rho, 0, 2*(1 - cos(ph)))), (ph, 0, pi/3)), (th, 0, 2*pi)), pi/12)
P(id="3-98", ch=15, sec="15.8", type="15-sph", src="2022 중간(블럭2) 10번 유형",
  q=r"원뿔 $z=\sqrt{\dfrac{x^2+y^2}{3}}$ 위쪽, 곡면 $x^2+y^2+z^2=2\sqrt{x^2+y^2+z^2}-2z$ 안쪽에 있는 입체의 부피를 구하라.",
  hint=r"곡면: $\rho^2=2\rho-2\rho\cos\phi \Rightarrow \rho=2(1-\cos\phi)$. 원뿔: $\tan\phi=\sqrt3 \Rightarrow \phi=\tfrac\pi3$",
  ans=r"$\dfrac{\pi}{12}$",
  sol=[r"$0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi3,\ 0\le\rho\le2(1-\cos\phi)$",
       r"$V=2\pi\displaystyle\int_0^{\pi/3}\frac{8(1-\cos\phi)^3}{3}\sin\phi\,d\phi=\frac{16\pi}{3}\Big[\frac{(1-\cos\phi)^4}{4}\Big]_0^{\pi/3}$",
       r"$=\dfrac{16\pi}{3}\cdot\dfrac{(1/2)^4}{4}=\dfrac{\pi}{12}$"],
  check=_c)


def _c():
    A = integrate(integrate(integrate(z*r, (z, 1, 3)), (r, 0, 1)), (th, 0, 2*pi)) + integrate(integrate(integrate(z*r, (z, r, 3)), (r, 1, 3)), (th, 0, 2*pi))
    B = integrate(integrate(integrate(z*r, (z, 1, 3)), (r, 0, 1/sqrt(3))), (th, 0, 2*pi)) + integrate(integrate(integrate(z*r, (z, sqrt(3)*r, 3)), (r, 1/sqrt(3), sqrt(3))), (th, 0, 2*pi))
    sph = integrate(integrate(integrate(rho**3*cos(ph)*sin(ph), (rho, 1/cos(ph), 3/cos(ph))), (ph, pi/6, pi/4)), (th, 0, 2*pi))
    assert EQ(A - B, 40*pi/3) and EQ(sph, 40*pi/3)
P(id="3-99", ch=15, sec="15.8", type="15-sphconv", src="2024 중간 8번 유형",
  q=r"구면좌표로 바꾸어 계산하라. $$\Big(\int_0^{2\pi}\!\!\int_0^{1}\!\!\int_1^3zr\,dz\,dr\,d\theta+\int_0^{2\pi}\!\!\int_1^{3}\!\!\int_r^3zr\,dz\,dr\,d\theta\Big)-\Big(\int_0^{2\pi}\!\!\int_0^{1/\sqrt3}\!\!\int_1^3zr\,dz\,dr\,d\theta+\int_0^{2\pi}\!\!\int_{1/\sqrt3}^{\sqrt3}\!\!\int_{\sqrt3r}^3zr\,dz\,dr\,d\theta\Big)$$",
  hint=r"첫 괄호: 평면 $z=1$, $z=3$ 사이이면서 원뿔 $z=r$ ($\phi=\tfrac\pi4$) 안쪽. 둘째 괄호: 같은 높이에서 원뿔 $z=\sqrt3r$ ($\phi=\tfrac\pi6$) 안쪽. 차는 두 원뿔 사이",
  ans=r"$\displaystyle\int_0^{2\pi}\!\!\int_{\pi/6}^{\pi/4}\!\!\int_{\sec\phi}^{3\sec\phi}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=\frac{40\pi}{3}$",
  sol=[r"첫 괄호 영역 $=\{1\le z\le3,\ z\ge r\}$, 둘째 $=\{1\le z\le3,\ z\ge\sqrt3r\}$ ⊂ 첫째 → 차는 $\tfrac\pi6\le\phi\le\tfrac\pi4$인 원뿔 껍질",
       r"$z=1 \iff \rho=\sec\phi$, $z=3 \iff \rho=3\sec\phi$; $zr\,dz\,dr\,d\theta=z\,dV=\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=2\pi\displaystyle\int_{\pi/6}^{\pi/4}\cos\phi\sin\phi\cdot\frac{81-1}{4}\sec^4\phi\,d\phi=40\pi\int_{\pi/6}^{\pi/4}\frac{\sin\phi}{\cos^3\phi}d\phi$",
       r"$=40\pi\Big[\dfrac{1}{2\cos^2\phi}\Big]_{\pi/6}^{\pi/4}=40\pi\Big(1-\dfrac23\Big)=\dfrac{40\pi}{3}$"],
  check=_c)


def _c():
    sph = integrate(integrate(integrate(rho**3*cos(ph)*sin(ph), (rho, 0, 2)), (ph, 0, pi/4)), (th, 0, pi/3))
    assert EQ(sph, pi/3)
    zf = lambda X, Y: (4 - X**2 - Y**2 - (X**2 + Y**2))/2   # ∫_{r}^{sqrt(4-r^2)} z dz
    cart = nquad2(zf, 0, mp.sqrt(2)/2, lambda X: 0, lambda X: mp.sqrt(3)*X) + nquad2(zf, mp.sqrt(2)/2, mp.sqrt(2), lambda X: 0, lambda X: mp.sqrt(2 - X**2))
    assert abs(cart - float(pi/3)) < 1e-8
P(id="3-100", ch=15, sec="15.8", type="15-sphconv", src="2022 중간(블럭1) 10번 유형",
  q=r"구면좌표로 바꾸어 계산하라. $$\int_0^{\sqrt2/2}\!\!\int_0^{\sqrt3x}\!\!\int_{\sqrt{x^2+y^2}}^{\sqrt{4-x^2-y^2}}z\,dz\,dy\,dx+\int_{\sqrt2/2}^{\sqrt2}\!\!\int_0^{\sqrt{2-x^2}}\!\!\int_{\sqrt{x^2+y^2}}^{\sqrt{4-x^2-y^2}}z\,dz\,dy\,dx$$",
  hint=r"$z$: 원뿔 $z=r$부터 구 $\rho=2$까지. $xy$ 범위: $0\le\theta\le\tfrac\pi3$ (직선 $y=\sqrt3x$), $r\le\sqrt2$ (원뿔과 구의 교선)",
  ans=r"$\displaystyle\int_0^{\pi/3}\!\!\int_0^{\pi/4}\!\!\int_0^2\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=\frac{\pi}{3}$",
  sol=[r"$xy$ 영역: 두 적분을 합치면 $0\le\theta\le\tfrac\pi3,\ 0\le r\le\sqrt2$ (직선 $y=\sqrt3x$와 원 $r=\sqrt2$는 $x=\tfrac{\sqrt2}{2}$에서 만나요)",
       r"입체: 원뿔 $\phi=\tfrac\pi4$ 안쪽, 구 $\rho=2$ 안쪽, $0\le\theta\le\tfrac\pi3$",
       r"$z\,dV=\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$",
       r"$=\dfrac\pi3\cdot\Big[\tfrac{\sin^2\phi}{2}\Big]_0^{\pi/4}\cdot\dfrac{2^4}{4}=\dfrac\pi3\cdot\dfrac14\cdot4=\dfrac\pi3$"],
  check=_c)


def _c():
    assert EQ(integrate(integrate(integrate(exp(rho**3)*rho**2*sin(ph), (rho, 0, 1)), (ph, 0, pi)), (th, 0, 2*pi)), 4*pi*(E - 1)/3)
P(id="3-101", ch=15, sec="15.8", type="15-sph", src="강의 15.8 (구면좌표 치환) 유형",
  q=r"$B$가 단위 구 $x^2+y^2+z^2\le1$일 때 $\displaystyle\iiint_Be^{(x^2+y^2+z^2)^{3/2}}\,dV$를 계산하라.",
  hint=r"$(x^2+y^2+z^2)^{3/2}=\rho^3$, 그리고 $\rho^2\,d\rho$가 함께 있으니 $u=\rho^3$ 치환",
  ans=r"$\dfrac{4\pi}{3}(e-1)$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^1e^{\rho^3}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot2\cdot\int_0^1\rho^2e^{\rho^3}d\rho$",
       r"$=4\pi\cdot\dfrac13\Big[e^{\rho^3}\Big]_0^1=\dfrac{4\pi}{3}(e-1)$"],
  check=_c)


# ───────── 15.9 변수변환 (추가) ─────────
def _c():
    J1 = Matrix([[diff(u**2 - v**2, u), diff(u**2 - v**2, v)], [diff(2*u*v, u), diff(2*u*v, v)]]).det()
    assert expand(J1 - 4*(u**2 + v**2)) == 0
    J2 = Matrix([[2, 1], [1, -3]]).det()
    assert J2 == -7 and integrate(abs(J2), (u, 0, 1), (v, 0, 1)) == 7
    assert abs(Matrix([2, 1, 0]).cross(Matrix([1, -3, 0]))[2]) == 7
P(id="3-124", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 야코비안",
  q=r"(a) 변환 $x=u^2-v^2,\ y=2uv$ 의 야코비안 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 를 구하라.<br>(b) 변환 $x=2u+v,\ y=u-3v$ 가 정사각형 $S=[0,1]\times[0,1]$ 을 옮긴 평행사변형 $R$ 의 넓이를 $\displaystyle\iint_RdA=\iint_S\Big|\frac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv$ 로 구하라.",
  hint=r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}x_u&x_v\\y_u&y_v\end{vmatrix}$. 넓이에는 절댓값을 써요.",
  ans=r"(a) $4(u^2+v^2)$  (b) $7$",
  sol=[r"(a) $\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}2u&-2v\\2v&2u\end{vmatrix}=4u^2+4v^2=4(u^2+v^2)$",
       r"(b) $\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}2&1\\1&-3\end{vmatrix}=-6-1=-7$ → 절댓값 $7$",
       r"$\displaystyle\iint_RdA=\int_0^1\!\!\int_0^1 7\,du\,dv=7$ (확인: 두 변 벡터 $\langle2,1\rangle,\ \langle1,-3\rangle$ 로 만든 평행사변형의 넓이 $|2\cdot(-3)-1\cdot1|=7$)"],
  check=_c)


def _c():
    xs, ys = (u + v)/3, (2*v - u)/3          # u=2x-y, v=x+y 의 역변환
    assert simplify(2*xs - ys - u) == 0 and simplify(xs + ys - v) == 0
    J = Matrix([[diff(xs, u), diff(xs, v)], [diff(ys, u), diff(ys, v)]]).det()
    assert J == R(1, 3)
    assert expand(((2*x - y)*(x + y)**2).subs({x: xs, y: ys}, simultaneous=True) - u*v**2) == 0
    assert integrate(u*v**2*R(1, 3), (u, 0, 4), (v, 0, 3)) == 24
    num = mp.quad(lambda Y: mp.quad(lambda X: (2*X - Y)*(X + Y)**2, [max(Y/2, -Y), min((Y + 4)/2, 3 - Y)]),
                  [-mp.mpf(4)/3, 0, mp.mpf(2)/3, 2])
    assert abs(num - 24) < 1e-9
P(id="3-125", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 평행사변형 영역",
  q=r"$R$ 은 네 직선 $y=2x,\ y=2x-4,\ y=-x,\ y=-x+3$ 으로 둘러싸인 평행사변형이다. 변환 $u=2x-y,\ v=x+y$ 를 이용하여 $\displaystyle\iint_R(2x-y)(x+y)^2\,dA$ 를 구하라.",
  hint=r"$\dfrac{\partial(u,v)}{\partial(x,y)}$ 를 먼저 구하면 $\dfrac{\partial(x,y)}{\partial(u,v)}$ 는 그 역수예요. 네 직선은 $u=0,\ 4$ 와 $v=0,\ 3$ 이 돼요.",
  ans=r"$24$",
  sol=[r"$\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}2&-1\\1&1\end{vmatrix}=3$ → $\dfrac{\partial(x,y)}{\partial(u,v)}=\dfrac13$, $\ dA=\dfrac13\,du\,dv$ (역변환을 풀지 않아도 돼요)",
       r"$y=2x,\ y=2x-4$ → $u=0,\ u=4$;  $y=-x,\ y=-x+3$ → $v=0,\ v=3$ → $S=[0,4]\times[0,3]$",
       r"$$\begin{aligned}&\iint_R(2x-y)(x+y)^2\,dA\\&=\frac13\int_0^3\!\!\int_0^4uv^2\,du\,dv\\&=\frac13\cdot\frac{4^2}{2}\cdot\frac{3^3}{3}=\frac13\cdot8\cdot9=24\end{aligned}$$"],
  check=_c)


def _c():
    J = Matrix([[2*u, -2*v], [2*v, 2*u]]).det()
    assert expand(J - 4*(u**2 + v**2)) == 0
    assert expand((u**2 - v**2)**2 + (2*u*v)**2 - (u**2 + v**2)**2) == 0
    assert integrate(J, (u, 0, 1), (v, 0, 1)) == R(8, 3)
    assert integrate((u**2 + v**2)*J, (u, 0, 1), (v, 0, 1)) == R(112, 45)
    # 원래 영역 R: 0 ≤ y ≤ 2, y²/4 - 1 ≤ x ≤ 1 - y²/4 에서 직접 수치적분
    area = mp.quad(lambda Y: 2 - Y*Y/2, [0, 2])
    num = mp.quad(lambda Y: mp.quad(lambda X: mp.sqrt(X*X + Y*Y), [Y*Y/4 - 1, 0, 1 - Y*Y/4]), [0, 2])
    assert abs(area - mp.mpf(8)/3) < 1e-12 and abs(num - mp.mpf(112)/45) < 1e-9
P(id="3-126", ch=15, sec="15.9", type="15-change", src="수업 자료 밖 · 교재 15.9 포물선 영역",
  q=r"변환 $x=u^2-v^2,\ y=2uv$ 는 정사각형 $S=\{(u,v)\mid0\le u\le1,\ 0\le v\le1\}$ 을, $x$축과 두 포물선 $y^2=4-4x,\ y^2=4+4x$ 로 둘러싸인 영역 $R\ (y\ge0)$ 로 옮긴다.<br>(a) $R$ 의 넓이를 구하라.  (b) $\displaystyle\iint_R\sqrt{x^2+y^2}\,dA$ 를 구하라.",
  hint=r"야코비안은 $4(u^2+v^2)$ ($S$ 위에서 $0$ 이상). $x^2+y^2=(u^2+v^2)^2$ 이에요.",
  ans=r"(a) $\dfrac83$  (b) $\dfrac{112}{45}$",
  sol=[r"$\dfrac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}2u&-2v\\2v&2u\end{vmatrix}=4(u^2+v^2)\ \ge0$",
       r"(a) $\displaystyle A=\int_0^1\!\!\int_0^14(u^2+v^2)\,du\,dv=4\Big(\frac13+\frac13\Big)=\frac83$",
       r"(b) $x^2+y^2=(u^2-v^2)^2+4u^2v^2=(u^2+v^2)^2$ → $\sqrt{x^2+y^2}=u^2+v^2$",
       r"$$\begin{aligned}&\iint_R\sqrt{x^2+y^2}\,dA\\&=\int_0^1\!\!\int_0^14(u^2+v^2)^2\,du\,dv\\&=4\Big(\frac15+\frac29+\frac15\Big)=\frac{112}{45}\end{aligned}$$"],
  check=_c)

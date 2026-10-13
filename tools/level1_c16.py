"""1단계 · 기본 추가분 — Ch.16 벡터 미적분: 1-102 ~ 1-120"""
from bank_lib import *


def line_int(F, rr, a, b, vars_=(x, y, z)):
    """벡터 선적분 ∫ F·dr (F 는 vars_ 의 식들, rr 은 t 의 매개화)"""
    sub = dict(zip(vars_, rr))
    integrand = sum(Fi.subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


# ───────── 16.1 ─────────
def _c():
    f = x*y**2 + exp(x*z)
    g = grad(f, (x, y, z))
    assert simplify(g[0] - (y**2 + z*exp(x*z))) == 0 and EQ(g.subs({x: 0, y: 1, z: 2}), [3, 0, 0])
P(id="1-102", ch=16, sec="16.1", type="16-field", src="과제 16.1 #25 유형",
  q=r"$f(x,y,z)=xy^2+e^{xz}$의 기울기 벡터장 $\nabla f$를 구하고, 점 $(0,1,2)$에서의 값을 구하라.",
  hint=r"$\nabla f=\langle f_x,\ f_y,\ f_z\rangle$",
  ans=r"$\nabla f=\langle y^2+ze^{xz},\ 2xy,\ xe^{xz}\rangle$,  $\nabla f(0,1,2)=\langle3,0,0\rangle$",
  sol=[r"$f_x=y^2+ze^{xz},\ f_y=2xy,\ f_z=xe^{xz}$",
       r"$(0,1,2)$: $\langle 1+2e^0,\ 0,\ 0\rangle=\langle3,0,0\rangle$"],
  check=_c)


# ───────── 16.2 ─────────
def _c():
    rr = Matrix([3*t, 4*t])
    sp = simplify(rr.diff(t).norm())
    assert sp == 5 and EQ(integrate((rr[0] + rr[1])*sp, (t, 0, 1)), R(35, 2))
P(id="1-103", ch=16, sec="16.2", type="16-scalar", src="강의 16.2 (호의 길이에 대한 선적분) 유형",
  q=r"$C$가 $(0,0)$에서 $(3,4)$까지의 선분일 때 $\displaystyle\int_C (x+y)\,ds$를 계산하라.",
  hint=r"$\mathbf r(t)=\langle3t,4t\rangle,\ 0\le t\le1$, $ds=|\mathbf r'(t)|\,dt$",
  ans=r"$\dfrac{35}{2}$",
  sol=[r"$\mathbf r(t)=\langle3t,\ 4t\rangle$, $|\mathbf r'(t)|=\sqrt{9+16}=5$",
       r"$\displaystyle\int_0^1(3t+4t)\cdot5\,dt=35\int_0^1t\,dt=\frac{35}{2}$"],
  check=_c)


def _c():
    rr = Matrix([2*cos(t), 2*sin(t)])
    sp = simplify(rr.diff(t).norm())
    assert sp == 2 and EQ(integrate(rr[0]*rr[1]*sp, (t, 0, pi/2)), 4)
P(id="1-104", ch=16, sec="16.2", type="16-scalar", src="복습 16.1–4 기초2 유형",
  q=r"$C$가 원 $x^2+y^2=4$의 1사분면 부분일 때 $\displaystyle\int_C xy\,ds$를 계산하라.",
  hint=r"$x=2\cos t,\ y=2\sin t,\ 0\le t\le\tfrac\pi2$, $|\mathbf r'(t)|=2$",
  ans=r"$4$",
  sol=[r"$\mathbf r(t)=\langle2\cos t,\ 2\sin t\rangle$, $ds=2\,dt$",
       r"$\displaystyle\int_0^{\pi/2}4\sin t\cos t\cdot2\,dt=8\cdot\Big[\tfrac{\sin^2t}{2}\Big]_0^{\pi/2}=4$"],
  check=_c)


def _c():
    assert EQ(line_int([x*y, y**2], [t, t**2], 0, 1, (x, y)), R(7, 12))
P(id="1-105", ch=16, sec="16.2", type="16-vector", src="강의 16.2 (벡터장의 선적분) 유형",
  q=r"$\mathbf F(x,y)=\langle xy,\ y^2\rangle$, $C:\ \mathbf r(t)=\langle t,\ t^2\rangle,\ 0\le t\le1$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 계산하라.",
  hint=r"$\displaystyle\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$",
  ans=r"$\dfrac{7}{12}$",
  sol=[r"$\mathbf F(\mathbf r(t))=\langle t^3,\ t^4\rangle$,  $\mathbf r'(t)=\langle1,\ 2t\rangle$",
       r"$\displaystyle\int_0^1(t^3+2t^5)\,dt=\frac14+\frac13=\frac{7}{12}$"],
  check=_c)


def _c():
    assert EQ(line_int([y, -x], [cos(t), sin(t)], 0, 2*pi, (x, y)), -2*pi)
P(id="1-106", ch=16, sec="16.2", type="16-vector", src="강의 16.2 유형 · 16.4 준비",
  q=r"$C$가 단위원 $x^2+y^2=1$을 반시계 방향으로 한 바퀴 도는 곡선일 때 $\displaystyle\oint_C y\,dx-x\,dy$를 계산하라.",
  hint=r"$x=\cos t,\ y=\sin t$: $dx=-\sin t\,dt,\ dy=\cos t\,dt$",
  ans=r"$-2\pi$",
  sol=[r"$y\,dx-x\,dy=\big(\sin t(-\sin t)-\cos t\cos t\big)dt=-dt$",
       r"$\displaystyle\int_0^{2\pi}(-1)\,dt=-2\pi$ (그린 정리로도 $\iint(-1-1)\,dA=-2\pi$)"],
  check=_c)


def _c():
    assert EQ(line_int([z, x, y], [cos(t), sin(t), t], 0, 2*pi), 3*pi)
P(id="1-107", ch=16, sec="16.2", type="16-vector", src="강의 16.2 (일) 유형",
  q=r"힘 $\mathbf F(x,y,z)=\langle z,\ x,\ y\rangle$가 나선 $\mathbf r(t)=\langle\cos t,\ \sin t,\ t\rangle,\ 0\le t\le2\pi$을 따라 입자를 움직일 때 한 일을 구하라.",
  hint=r"$W=\displaystyle\int_C\mathbf F\cdot d\mathbf r$. $\int_0^{2\pi}t\sin t\,dt$는 부분적분.",
  ans=r"$3\pi$",
  sol=[r"$\mathbf F(\mathbf r(t))=\langle t,\ \cos t,\ \sin t\rangle$,  $\mathbf r'(t)=\langle-\sin t,\ \cos t,\ 1\rangle$",
       r"$\mathbf F\cdot\mathbf r'=-t\sin t+\cos^2t+\sin t$",
       r"$\displaystyle\int_0^{2\pi}-t\sin t\,dt=\Big[t\cos t-\sin t\Big]_0^{2\pi}=2\pi$,  $\displaystyle\int_0^{2\pi}\cos^2t\,dt=\pi$,  $\displaystyle\int_0^{2\pi}\sin t\,dt=0$",
       r"$W=2\pi+\pi=3\pi$"],
  check=_c)


# ───────── 16.3 ─────────
def _c():
    Pp, Q = 2*x*y + 3, x**2 - 4*y**3
    f = x**2*y + 3*x - y**4
    assert diff(Pp, y) == diff(Q, x) and simplify(diff(f, x) - Pp) == 0 and simplify(diff(f, y) - Q) == 0
P(id="1-108", ch=16, sec="16.3", type="16-conserv", src="과제 16.3 #7 유형",
  q=r"$\mathbf F(x,y)=\langle 2xy+3,\ x^2-4y^3\rangle$이 보존장인지 판정하고, 보존장이면 $\mathbf F=\nabla f$인 $f$를 구하라.",
  hint=r"$P_y=Q_x$인지 확인한 뒤 $f=\int P\,dx+g(y)$",
  ans=r"보존장,  $f(x,y)=x^2y+3x-y^4+K$",
  sol=[r"$P_y=2x,\ Q_x=2x$ → 같고 정의역이 $\mathbb R^2$ → 보존장",
       r"$f=\displaystyle\int(2xy+3)\,dx=x^2y+3x+g(y)$",
       r"$f_y=x^2+g'(y)=x^2-4y^3 \Rightarrow g(y)=-y^4+K$",
       r"$f(x,y)=x^2y+3x-y^4+K$"],
  check=_c)


def _c():
    Pp, Q = y*exp(x*y), x*exp(x*y) + 2*y
    f = exp(x*y) + y**2
    assert simplify(diff(Pp, y) - diff(Q, x)) == 0 and simplify(diff(f, x) - Pp) == 0 and simplify(diff(f, y) - Q) == 0
P(id="1-109", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 (퍼텐셜 함수) 유형",
  q=r"$\mathbf F(x,y)=\langle ye^{xy},\ xe^{xy}+2y\rangle$의 퍼텐셜 함수 $f$를 구하라.",
  hint=r"$P_y=e^{xy}+xye^{xy}=Q_x$. $\int ye^{xy}\,dx=e^{xy}$",
  ans=r"$f(x,y)=e^{xy}+y^2+K$",
  sol=[r"$P_y=e^{xy}+xye^{xy}=Q_x$ → 보존장",
       r"$f=\displaystyle\int ye^{xy}\,dx=e^{xy}+g(y)$",
       r"$f_y=xe^{xy}+g'(y)=xe^{xy}+2y \Rightarrow g(y)=y^2+K$",
       r"$f=e^{xy}+y^2+K$"],
  check=_c)


def _c():
    F = [y*z, x*z + 2*y, x*y + 1]
    curl = [diff(F[2], y) - diff(F[1], z), diff(F[0], z) - diff(F[2], x), diff(F[1], x) - diff(F[0], y)]
    assert all(simplify(c_) == 0 for c_ in curl)
    f = x*y*z + y**2 + z
    assert all(simplify(diff(f, v) - Fi) == 0 for v, Fi in zip((x, y, z), F))
P(id="1-110", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 · 과제 16.5 #17 유형 (3차원)",
  q=r"$\mathbf F(x,y,z)=\langle yz,\ xz+2y,\ xy+1\rangle$이 보존장임을 보이고 퍼텐셜 함수를 구하라.",
  hint=r"3차원: $P_y=Q_x,\ Q_z=R_y,\ R_x=P_z$ (즉 $\operatorname{curl}\mathbf F=\mathbf 0$)",
  ans=r"$f(x,y,z)=xyz+y^2+z+K$",
  sol=[r"$P_y=z=Q_x$,  $Q_z=x=R_y$,  $R_x=y=P_z$ → 보존장",
       r"$f=\displaystyle\int yz\,dx=xyz+g(y,z)$",
       r"$f_y=xz+g_y=xz+2y \Rightarrow g=y^2+h(z)$,  $f_z=xy+h'(z)=xy+1 \Rightarrow h=z$",
       r"$f=xyz+y^2+z+K$"],
  check=_c)


def _c():
    f = x**2*y + 3*x - y**4
    assert f.subs({x: 2, y: 1}) - f.subs({x: 0, y: 0}) == 9
    assert EQ(line_int([2*x*y + 3, x**2 - 4*y**3], [2*t, t], 0, 1, (x, y)), 9)
P(id="1-111", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #25 유형",
  q=r"$C$가 $(0,0)$에서 $(2,1)$로 가는 임의의 곡선일 때 $\displaystyle\int_C(2xy+3)\,dx+(x^2-4y^3)\,dy$를 구하라.",
  hint=r"1-108의 퍼텐셜 $f=x^2y+3x-y^4$를 쓰면 끝점 값의 차예요.",
  ans=r"$9$",
  sol=[r"$\mathbf F=\nabla f$, $f=x^2y+3x-y^4$ (경로와 무관)",
       r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r=f(2,1)-f(0,0)=(4+6-1)-0=9$"],
  check=_c)


def _c():
    F = [y*z, x*z + 2*y, x*y + 1]
    assert EQ(line_int(F, [t, t**2, t**3], 0, 1), 3)
P(id="1-112", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #16 유형",
  q=r"$\mathbf F=\langle yz,\ xz+2y,\ xy+1\rangle$, $C:\ \mathbf r(t)=\langle t,\ t^2,\ t^3\rangle,\ 0\le t\le1$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"1-110의 퍼텐셜 $f=xyz+y^2+z$. 시작점 $\mathbf r(0)$, 끝점 $\mathbf r(1)$만 필요해요.",
  ans=r"$3$",
  sol=[r"시작점 $(0,0,0)$, 끝점 $(1,1,1)$",
       r"$f(1,1,1)-f(0,0,0)=(1+1+1)-0=3$"],
  check=_c)


# ───────── 16.4 ─────────
def _c():
    Pp, Q = x - y, x + y
    assert EQ(integrate(integrate((diff(Q, x) - diff(Pp, y))*r, (r, 0, 2)), (th, 0, 2*pi)), 8*pi)
    assert EQ(line_int([Pp, Q], [2*cos(t), 2*sin(t)], 0, 2*pi, (x, y)), 8*pi)
P(id="1-113", ch=16, sec="16.4", type="16-green", src="복습 16.1–4 기초5 유형",
  q=r"$C$가 원 $x^2+y^2=4$ (반시계 방향)일 때 그린 정리로 $\displaystyle\oint_C (x-y)\,dx+(x+y)\,dy$를 계산하라.",
  hint=r"$\displaystyle\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)dA$",
  ans=r"$8\pi$",
  sol=[r"$Q_x-P_y=1-(-1)=2$",
       r"$\displaystyle\iint_D2\,dA=2\cdot(\pi\cdot2^2)=8\pi$"],
  check=_c)


def _c():
    Pp, Q = x*y, x**2
    assert integrate(integrate(diff(Q, x) - diff(Pp, y), (y, 0, 1)), (x, 0, 2)) == 2
    direct = (line_int([Pp, Q], [t, 0], 0, 2, (x, y)) + line_int([Pp, Q], [2, t], 0, 1, (x, y))
              + line_int([Pp, Q], [2 - t, 1], 0, 2, (x, y)) + line_int([Pp, Q], [0, 1 - t], 0, 1, (x, y)))
    assert direct == 2
P(id="1-114", ch=16, sec="16.4", type="16-green", src="과제 16.4 #3 유형",
  q=r"$C$가 직사각형 $[0,2]\times[0,1]$의 경계(반시계 방향)일 때 $\displaystyle\oint_C xy\,dx+x^2\,dy$를 그린 정리로 계산하라.",
  hint=r"$Q_x-P_y=2x-x=x$",
  ans=r"$2$",
  sol=[r"$Q_x-P_y=2x-x=x$",
       r"$\displaystyle\int_0^2\!\!\int_0^1x\,dy\,dx=\int_0^2x\,dx=2$"],
  check=_c)


def _c():
    Pp, Q = y + exp(x), 2*x + cos(y)
    assert simplify(diff(Q, x) - diff(Pp, y)) == 1
    assert integrate(integrate(1, (y, 0, 3 - R(3, 2)*x)), (x, 0, 2)) == 3
P(id="1-115", ch=16, sec="16.4", type="16-green", src="과제 16.4 #8 유형",
  q=r"$C$가 꼭짓점 $(0,0),\ (2,0),\ (0,3)$인 삼각형(반시계 방향)일 때 $\displaystyle\oint_C (y+e^x)\,dx+(2x+\cos y)\,dy$를 계산하라.",
  hint=r"직접 계산하면 $e^x,\ \cos y$ 때문에 복잡해요. $Q_x-P_y$를 먼저 보세요.",
  ans=r"$3$",
  sol=[r"$Q_x-P_y=2-1=1$",
       r"$\displaystyle\oint_C=\iint_D1\,dA=$ 삼각형 넓이 $=\dfrac12\cdot2\cdot3=3$"],
  check=_c)


def _c():
    Pp, Q = x**2*y, -x*y**2
    assert EQ(integrate(integrate((diff(Q, x) - diff(Pp, y)).subs({x: r*cos(th), y: r*sin(th)})*r, (r, 0, 1)), (th, 0, 2*pi)), -pi/2)
    assert EQ(line_int([Pp, Q], [cos(t), sin(t)], 0, 2*pi, (x, y)), -pi/2)
P(id="1-116", ch=16, sec="16.4", type="16-green", src="강의 16.4 (극좌표와 결합) 유형",
  q=r"$C$가 단위원 $x^2+y^2=1$ (반시계 방향)일 때 $\displaystyle\oint_C x^2y\,dx-xy^2\,dy$를 계산하라.",
  hint=r"$Q_x-P_y=-y^2-x^2=-r^2$, 그다음 극좌표",
  ans=r"$-\dfrac{\pi}{2}$",
  sol=[r"$Q_x-P_y=-y^2-x^2$",
       r"$\displaystyle\iint_D-(x^2+y^2)\,dA=-\int_0^{2\pi}\!\!\int_0^1r^3\,dr\,d\theta=-2\pi\cdot\frac14=-\frac\pi2$"],
  check=_c)


def _c():
    A = R(1, 2)*line_int([-y, x], [3*cos(t), 2*sin(t)], 0, 2*pi, (x, y))
    assert EQ(A, 6*pi)
P(id="1-117", ch=16, sec="16.4", type="16-greenarea", src="강의 16.4 (넓이 공식) 유형",
  q=r"그린 정리의 넓이 공식 $A=\dfrac12\displaystyle\oint_C x\,dy-y\,dx$를 이용해 타원 $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$의 넓이를 구하라.",
  hint=r"$x=3\cos t,\ y=2\sin t,\ 0\le t\le2\pi$ (반시계)",
  ans=r"$6\pi$",
  sol=[r"$x\,dy-y\,dx=\big(3\cos t\cdot2\cos t-2\sin t\cdot(-3\sin t)\big)dt=6\,dt$",
       r"$A=\dfrac12\displaystyle\int_0^{2\pi}6\,dt=6\pi$ (공식 $\pi ab=6\pi$와 일치)"],
  check=_c)


def _c():
    pts = [(0, 0), (4, 0), (1, 3)]
    tot = 0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]):
        tot += line_int([-y, x], [x0 + (x1 - x0)*t, y0 + (y1 - y0)*t], 0, 1, (x, y))
    assert EQ(R(1, 2)*tot, 6)
P(id="1-118", ch=16, sec="16.4", type="16-greenarea", src="2024 기말 1(b) 유형 (기초)",
  q=r"넓이 공식 $A=\dfrac12\displaystyle\oint_C x\,dy-y\,dx$로 꼭짓점이 $(0,0),\ (4,0),\ (1,3)$인 삼각형의 넓이를 구하라.",
  hint=r"$(x_1,y_1)\to(x_2,y_2)$ 선분에서 $\displaystyle\int x\,dy-y\,dx=x_1y_2-x_2y_1$ (매개화해서 확인해 보세요)",
  ans=r"$6$",
  sol=[r"선분 하나: $x=x_1+(x_2-x_1)t,\ y=y_1+(y_2-y_1)t$ → $\displaystyle\int_0^1(x\,dy-y\,dx)=x_1y_2-x_2y_1$",
       r"$(0,0)\to(4,0)$: $0$,  $(4,0)\to(1,3)$: $12-0=12$,  $(1,3)\to(0,0)$: $0$",
       r"$A=\dfrac12(0+12+0)=6$ (밑변 $4$, 높이 $3$으로 확인 ✓)"],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2), x/(x**2 + y**2)]
    assert simplify(diff(F[1], x) - diff(F[0], y)) == 0
    assert EQ(line_int(F, [2*cos(t), 2*sin(t)], 0, 2*pi, (x, y)), 2*pi)
P(id="1-119", ch=16, sec="16.4", type="16-singular", src="강의 16.4 ex5 유형",
  q=r"$C$가 원 $x^2+y^2=4$ (반시계 방향)일 때 $\displaystyle\oint_C\frac{-y\,dx+x\,dy}{x^2+y^2}$를 직접 계산하라. 또 $Q_x-P_y=0$인데 그린 정리로 $0$이라고 할 수 없는 이유를 말하라.",
  hint=r"$x=2\cos t,\ y=2\sin t$를 대입하면 분자가 $4\,dt$, 분모가 $4$예요.",
  ans=r"$2\pi$ (원점에서 $\mathbf F$가 정의되지 않아 그린 정리를 쓸 수 없다)",
  sol=[r"$-y\,dx+x\,dy=(4\sin^2t+4\cos^2t)\,dt=4\,dt$,  $x^2+y^2=4$",
       r"$\displaystyle\oint_C=\int_0^{2\pi}\frac{4}{4}\,dt=2\pi$",
       r"원점 밖에서는 $Q_x-P_y=0$이지만 원점이 $C$ 안에 있고 그곳에서 $\mathbf F$가 정의되지 않으므로 그린 정리의 조건을 만족하지 않아요."],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2), x/(x**2 + y**2)]
    num = line_int(F, [3 + cos(t), sin(t)], 0, 2*pi, (x, y))
    assert EQ(num, 0)
P(id="1-120", ch=16, sec="16.4", type="16-singular", src="강의 16.4 ex5 유형 (원점을 감싸지 않는 곡선)",
  q=r"$C$가 원 $(x-3)^2+y^2=1$ (반시계 방향)일 때 $\displaystyle\oint_C\frac{-y\,dx+x\,dy}{x^2+y^2}$를 구하라.",
  hint=r"이 원은 원점을 감싸지 않아요. 그 안에서는 $\mathbf F$가 매끄러워요.",
  ans=r"$0$",
  sol=[r"$P=\dfrac{-y}{x^2+y^2},\ Q=\dfrac{x}{x^2+y^2}$: 원점 밖에서 $Q_x-P_y=\dfrac{y^2-x^2}{(x^2+y^2)^2}-\dfrac{y^2-x^2}{(x^2+y^2)^2}=0$",
       r"원판 $(x-3)^2+y^2\le1$은 원점을 포함하지 않으므로 그린 정리를 쓸 수 있어요.",
       r"$\displaystyle\oint_C=\iint_D0\,dA=0$"],
  check=_c)

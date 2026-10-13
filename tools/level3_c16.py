"""3단계 · 응용 추가분 — Ch.16 벡터 미적분: 3-102 ~ 3-120"""
from bank_lib import *
from sympy import atan
import mpmath as mp


def line_int(F, rr, a, b, vars_=(x, y, z)):
    sub = dict(zip(vars_, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


def line_num(F, rr, a, b, vars_=(x, y, z)):
    sub = dict(zip(vars_, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    fn = lambdify(t, integrand, 'mpmath')
    return mp.quad(fn, [mp.mpf(float(N(a, 30))), mp.mpf(float(N(b, 30)))])


def seg(p0, p1):
    return [a0 + (a1 - a0)*t for a0, a1 in zip(p0, p1)]


from sympy import lambdify


# ───────── 16.1 ─────────
def _c():
    c1, c2 = symbols('c1 c2', real=True)
    X, Y = c1*exp(t), c2*exp(-t)
    assert simplify(diff(X, t) - X) == 0 and simplify(diff(Y, t) + Y) == 0 and simplify(X*Y - c1*c2) == 0
    f = (x**2 - y**2)/2
    assert grad(f, (x, y)) == Matrix([x, -y])
P(id="3-102", ch=16, sec="16.1", type="16-field", src="강의 16.1 (유선) 유형",
  q=r"벡터장 $\mathbf F(x,y)=\langle x,\ -y\rangle$에 대해 (a) $\mathbf F=\nabla f$인 $f$를 구하고 (b) 유선(흐름선) $x'(t)=x,\ y'(t)=-y$의 방정식을 구하라. 유선과 $f$의 등위곡선은 어떤 관계인가?",
  hint=r"(b) $x=c_1e^t,\ y=c_2e^{-t}$ → $xy$가 일정. 기울기장의 유선은 등위곡선과 수직으로 만나요.",
  ans=r"(a) $f=\tfrac12(x^2-y^2)$  (b) $xy=C$ (쌍곡선). 등위곡선 $x^2-y^2=c$와 수직으로 만난다.",
  sol=[r"(a) $f_x=x,\ f_y=-y$ → $f=\tfrac12(x^2-y^2)+K$",
       r"(b) $x'=x \Rightarrow x=c_1e^t$, $y'=-y \Rightarrow y=c_2e^{-t}$ → $xy=c_1c_2$: 유선은 쌍곡선 $xy=C$",
       r"$\mathbf F=\nabla f$는 등위곡선 $x^2-y^2=c$에 수직이므로 유선(접선이 $\mathbf F$)은 등위곡선과 직교해요."],
  check=_c)


# ───────── 16.2 ─────────
def _c():
    rr = Matrix([2*cos(t), 2*sin(t), t])
    sp = simplify(rr.diff(t).norm())
    assert EQ(sp, sqrt(5))
    assert EQ(integrate((rr[0]**2*rr[1] + rr[2])*sp, (t, 0, pi/2)), sqrt(5)*(R(8, 3) + pi**2/8))
P(id="3-103", ch=16, sec="16.2", type="16-scalar", src="2022 기말(블럭1) 5(2) 유형",
  q=r"$C:\ x=2\cos t,\ y=2\sin t,\ z=t\ \left(0\le t\le\tfrac\pi2\right)$일 때 $\displaystyle\int_C(x^2y+z)\,ds$를 계산하라.",
  hint=r"$|\mathbf r'(t)|=\sqrt5$로 상수. $\int\cos^2t\sin t\,dt=-\tfrac{\cos^3t}{3}$",
  ans=r"$\sqrt5\left(\dfrac83+\dfrac{\pi^2}{8}\right)$",
  sol=[r"$|\mathbf r'(t)|=\sqrt{4\sin^2t+4\cos^2t+1}=\sqrt5$",
       r"$x^2y+z=8\cos^2t\sin t+t$",
       r"$\displaystyle\sqrt5\int_0^{\pi/2}(8\cos^2t\sin t+t)\,dt=\sqrt5\Big(\frac83+\frac{\pi^2}{8}\Big)$"],
  check=_c)


def _c():
    rr = Matrix([1 - t**2, 0, 2*t])
    sp2 = rr.diff(t).dot(rr.diff(t))
    assert simplify(sp2 - 4*(1 + t**2)) == 0
    dens_ds = 3*sqrt(1 + t**2) * 2*sqrt(1 + t**2)
    m = integrate(expand(dens_ds), (t, -1, 1))
    Mx = integrate(expand(rr[0]*dens_ds), (t, -1, 1)); Mz = integrate(expand(rr[2]*dens_ds), (t, -1, 1))
    assert m == 16 and EQ(Mx/m, R(3, 5)) and Mz == 0
P(id="3-104", ch=16, sec="16.2", type="16-scalar", src="2022 기말(블럭2) 2번 유형",
  q=r"곡선 $\mathbf r(t)=(1-t^2)\,\mathbf i+2t\,\mathbf k\ (-1\le t\le1)$을 따라 놓인 철사의 밀도가 $\delta(x,y,z)=3\sqrt{2-x}$일 때 철사의 질량과 질량중심을 구하라.",
  hint=r"$|\mathbf r'(t)|=2\sqrt{1+t^2}$, $2-x=1+t^2$ → $\delta\,ds=6(1+t^2)\,dt$",
  ans=r"질량 $16$,  질량중심 $\left(\dfrac35,\ 0,\ 0\right)$",
  sol=[r"$\mathbf r'(t)=\langle-2t,0,2\rangle$, $|\mathbf r'|=2\sqrt{1+t^2}$, $\delta=3\sqrt{1+t^2}$ → $\delta\,ds=6(1+t^2)\,dt$",
       r"$m=\displaystyle\int_{-1}^{1}6(1+t^2)\,dt=6\Big(2+\frac23\Big)=16$",
       r"$\bar x=\dfrac1{16}\displaystyle\int_{-1}^1(1-t^2)\cdot6(1+t^2)\,dt=\frac{6}{16}\Big(2-\frac25\Big)=\frac35$",
       r"$y=0$이라 $\bar y=0$, $z=2t$는 홀함수라 $\bar z=0$"],
  check=_c)


def _c():
    F = [z, x, y]
    pts = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    parts = [line_int(F, seg(a, b), 0, 1) for a, b in zip(pts, pts[1:] + pts[:1])]
    assert parts == [R(1, 2), R(1, 2), R(1, 2)]
P(id="3-105", ch=16, sec="16.2", type="16-vector", src="2022 기말(블럭2) 5번 유형",
  q=r"$C$가 $(1,0,0)\to(0,1,0)\to(0,0,1)\to(1,0,0)$으로 가는 세 선분일 때 $\displaystyle\oint_C z\,dx+x\,dy+y\,dz$를 계산하라.",
  hint=r"선분마다 매개화: 예를 들어 첫 선분은 $x=1-t,\ y=t,\ z=0$",
  ans=r"$\dfrac32$",
  sol=[r"$(1,0,0)\to(0,1,0)$: $x=1-t,\ y=t,\ z=0$ → $x\,dy=(1-t)dt$ → $\tfrac12$",
       r"$(0,1,0)\to(0,0,1)$: $x=0,\ y=1-t,\ z=t$ → $y\,dz=(1-t)dt$ → $\tfrac12$",
       r"$(0,0,1)\to(1,0,0)$: $x=t,\ y=0,\ z=1-t$ → $z\,dx=(1-t)dt$ → $\tfrac12$",
       r"합 $\dfrac32$ (닫힌 곡선인데 $0$이 아니므로 $\langle z,x,y\rangle$은 보존장이 아니에요)"],
  check=_c)


def _c():
    assert EQ(line_int([x + z, x*y, y**2], [t**2, t**3, -t], 0, 1), R(11, 168))
P(id="3-106", ch=16, sec="16.2", type="16-vector", src="2024 기말 2(a) 유형",
  q=r"$\mathbf F(x,y,z)=(x+z)\,\mathbf i+xy\,\mathbf j+y^2\,\mathbf k$, $C:\ \mathbf r(t)=t^2\,\mathbf i+t^3\,\mathbf j-t\,\mathbf k\ (0\le t\le1)$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 계산하라.",
  hint=r"$\mathbf F(\mathbf r(t))=\langle t^2-t,\ t^5,\ t^6\rangle$,  $\mathbf r'(t)=\langle2t,\ 3t^2,\ -1\rangle$",
  ans=r"$\dfrac{11}{168}$",
  sol=[r"$\mathbf F\cdot\mathbf r'=2t^3-2t^2+3t^7-t^6$",
       r"$\displaystyle\int_0^1=\frac12-\frac23+\frac38-\frac17=\frac{84-112+63-24}{168}=\frac{11}{168}$"],
  check=_c)


def _c():
    uu = symbols('uu', real=True)
    f = 10 - 12*uu                       # ∫f=4, ∫u f=1 을 만족하는 예
    assert integrate(f, (uu, 0, 1)) == 4 and integrate(uu*f, (uu, 0, 1)) == 1
    G = integrate(f, (uu, 0, t))         # g(r(t)) = ∫_0^t f
    rr = Matrix([1 + 2*t, 1 + t, 0])
    assert simplify(rr[0] - rr[1] + rr[2] - t) == 0
    assert EQ(integrate(G*sqrt(5), (t, 0, 1)), 3*sqrt(5))
    assert EQ(G.subs(t, 1) - G.subs(t, 0), 4)
P(id="3-107", ch=16, sec="16.2", type="16-scalar", src="2024 기말 3번 유형",
  q=r"연속함수 $f$가 $\displaystyle\int_0^1f(u)\,du=4,\ \int_0^1uf(u)\,du=1$을 만족하고 $g(x,y,z)=\displaystyle\int_0^{x-y+z}f(u)\,du$이다. $C$가 $(1,1,0)$에서 $(3,2,0)$까지의 선분일 때<br>(a) $\displaystyle\int_Cf(x-y+z)\,dx-f(x-y+z)\,dy+f(x-y+z)\,dz$  (b) $\displaystyle\int_Cg(x,y,z)\,ds$를 구하라.",
  hint=r"(a) 피적분 벡터장은 $\nabla g$예요. (b) $\mathbf r(t)=\langle1+2t,1+t,0\rangle$이면 $x-y+z=t$, $ds=\sqrt5\,dt$. 적분 순서를 바꾸면 $\int_0^1\!\int_0^tf(u)\,du\,dt=\int_0^1(1-u)f(u)\,du$",
  ans=r"(a) $4$  (b) $3\sqrt5$",
  sol=[r"(a) $\nabla g=f(x-y+z)\langle1,-1,1\rangle$ → 선적분의 기본정리: $g(3,2,0)-g(1,1,0)=\displaystyle\int_0^1f-\int_0^0f=4$",
       r"(b) $\mathbf r(t)=\langle1+2t,\ 1+t,\ 0\rangle$: $x-y+z=t$, $|\mathbf r'|=\sqrt5$",
       r"$\displaystyle\int_Cg\,ds=\sqrt5\int_0^1\!\!\int_0^tf(u)\,du\,dt=\sqrt5\int_0^1(1-u)f(u)\,du$",
       r"$=\sqrt5(4-1)=3\sqrt5$"],
  check=_c)


# ───────── 16.3 ─────────
def _c():
    F = [exp(z)/(1 + x**2), sin(y)**2, atan(x)*exp(z)]
    f = atan(x)*exp(z) + y/2 - sin(2*y)/4
    assert all(simplify(diff(f, v) - Fi) == 0 for v, Fi in zip((x, y, z), F))
    assert EQ(f.subs({x: 1, y: pi, z: 2}) - f.subs({x: 0, y: 0, z: 0}), pi*exp(2)/4 + pi/2)
P(id="3-108", ch=16, sec="16.3", type="16-ftli", src="2022 기말(블럭1) 5(1) 유형",
  q=r"$\mathbf F(x,y,z)=\Big\langle\dfrac{e^z}{1+x^2},\ \sin^2y,\ e^z\tan^{-1}x\Big\rangle$가 보존장임을 보이고, $C$가 $(0,0,0)$에서 $(1,\pi,2)$까지 가는 곡선일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\int\sin^2y\,dy=\tfrac y2-\tfrac{\sin2y}{4}$. $P_z=R_x=\tfrac{e^z}{1+x^2}$",
  ans=r"$\dfrac{\pi e^2}{4}+\dfrac\pi2$",
  sol=[r"$P_y=0=Q_x$, $Q_z=0=R_y$, $R_x=\dfrac{e^z}{1+x^2}=P_z$ → 보존장",
       r"$f=\displaystyle\int\frac{e^z}{1+x^2}dx=e^z\tan^{-1}x+g(y,z)$, $g_y=\sin^2y$, $g_z=0$ → $g=\dfrac y2-\dfrac{\sin2y}{4}$",
       r"$f(1,\pi,2)-f(0,0,0)=e^2\cdot\dfrac\pi4+\dfrac\pi2-0=\dfrac{\pi e^2}{4}+\dfrac\pi2$"],
  check=_c)


def _c():
    F = [exp(y), x*exp(y) + z**2, 2*y*z]
    f = x*exp(y) + y*z**2
    assert all(simplify(diff(f, v) - Fi) == 0 for v, Fi in zip((x, y, z), F))
    assert EQ(line_num(F, [t**2, t**3, t], 0, 1), E + 1)
P(id="3-109", ch=16, sec="16.3", type="16-ftli", src="2024 기말 2(b) 유형",
  q=r"$C:\ \mathbf r(t)=\langle t^2,\ t^3,\ t\rangle\ (0\le t\le1)$일 때 $\displaystyle\int_Ce^{y}\,dx+(xe^{y}+z^2)\,dy+2yz\,dz$를 구하라.",
  hint=r"직접 대입하면 $e^{t^3}$이 나와 막혀요. 퍼텐셜 함수를 찾아보세요.",
  ans=r"$e+1$",
  sol=[r"$P_y=e^y=Q_x$, $Q_z=2z=R_y$, $R_x=0=P_z$ → 보존장",
       r"$f=xe^y+g(y,z)$, $f_y=xe^y+g_y=xe^y+z^2 \Rightarrow g=yz^2+h(z)$, $f_z=2yz+h'=2yz \Rightarrow h=0$",
       r"$f(1,1,1)-f(0,0,0)=(e+1)-0=e+1$"],
  check=_c)


def _c():
    uu = symbols('uu', real=True)
    f = 6*uu                               # ∫_0^1 f = 3
    assert integrate(f, (uu, 0, 1)) == 3
    rr = [1 + t, 2 - 2*t, -t]              # (1,2,0) → (2,0,-1) 의 한 경로
    w = 2*rr[0] - rr[1] + 3*rr[2]
    assert simplify(w.subs(t, 0)) == 0 and simplify(w.subs(t, 1)) == 1
    Fz = f.subs(uu, 2*x - y + 3*z)
    assert EQ(line_int([2*Fz, -Fz, 3*Fz], rr, 0, 1), 3)
P(id="3-110", ch=16, sec="16.3", type="16-ftli", src="2024 기말 3(a) 유형",
  q=r"연속함수 $f$가 $\displaystyle\int_0^1f(u)\,du=3$을 만족한다. $C$가 $(1,2,0)$에서 $(2,0,-1)$까지 가는 임의의 매끄러운 곡선일 때 $$\int_C2f(2x-y+3z)\,dx-f(2x-y+3z)\,dy+3f(2x-y+3z)\,dz$$를 구하라.",
  hint=r"$G(x,y,z)=\displaystyle\int_0^{2x-y+3z}f(u)\,du$로 두면 $\nabla G$가 피적분 벡터장 (미적분학의 기본정리 + 연쇄법칙)",
  ans=r"$3$",
  sol=[r"$G=\displaystyle\int_0^{2x-y+3z}f(u)\,du$ → $\nabla G=f(2x-y+3z)\langle2,-1,3\rangle$",
       r"시작점: $2-2+0=0$, 끝점: $4-0-3=1$",
       r"$\displaystyle\int_C\nabla G\cdot d\mathbf r=G(\text{끝})-G(\text{시작})=\int_0^1f-\int_0^0f=3$"],
  check=_c)


def _c():
    F = [2*x*y + exp(x), x**2 + cos(y), y + z]
    rr = [cos(t), sin(t), cos(t)]
    assert EQ(line_int(F, rr, 0, 2*pi), -pi)
    assert EQ(line_int([0, 0, y], rr, 0, 2*pi), -pi)
P(id="3-111", ch=16, sec="16.3", type="16-ftli", src="2022 기말(블럭1) 2번 유형",
  q=r"$\mathbf F=(2xy+e^{x})\,\mathbf i+(x^2+\cos y)\,\mathbf j+(y+z)\,\mathbf k$, $C:\ \mathbf r(t)=\langle\cos t,\ \sin t,\ \cos t\rangle\ (0\le t\le2\pi)$일 때 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\mathbf F=\nabla\Big(x^2y+e^x+\sin y+\tfrac{z^2}{2}\Big)+\langle0,0,y\rangle$. 닫힌 곡선이라 보존장 부분은 $0$",
  ans=r"$-\pi$",
  sol=[r"$\mathbf F=\nabla\phi+\langle0,0,y\rangle$, $\phi=x^2y+e^x+\sin y+\tfrac12z^2$",
       r"$C$는 닫힌 곡선 ($\mathbf r(0)=\mathbf r(2\pi)$) → $\displaystyle\oint_C\nabla\phi\cdot d\mathbf r=0$",
       r"남는 부분: $\displaystyle\oint_Cy\,dz=\int_0^{2\pi}\sin t\cdot(-\sin t)\,dt=-\pi$"],
  check=_c)


def _c():
    a = symbols('a', real=True)
    Pp, Q = a*x*y + y**2, x**2 + 2*x*y
    assert solve(diff(Pp, y) - diff(Q, x), a) == [2]
    f = x**2*y + x*y**2
    assert simplify(diff(f, x) - Pp.subs(a, 2)) == 0 and simplify(diff(f, y) - Q) == 0
    assert f.subs({x: 2, y: -1}) - f.subs({x: 1, y: 1}) == -4
P(id="3-112", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 (보존장 조건) 유형",
  q=r"$\mathbf F(x,y)=\langle axy+y^2,\ x^2+2xy\rangle$가 보존장이 되는 상수 $a$를 구하고, 그때 $(1,1)$에서 $(2,-1)$까지 가는 임의의 곡선 $C$에 대해 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$P_y=ax+2y$, $Q_x=2x+2y$",
  ans=r"$a=2$,  $\displaystyle\int_C\mathbf F\cdot d\mathbf r=-4$",
  sol=[r"$P_y=Q_x \iff ax+2y=2x+2y \iff a=2$",
       r"$f=\displaystyle\int(2xy+y^2)\,dx=x^2y+xy^2+g(y)$, $f_y=x^2+2xy+g'=Q \Rightarrow g=K$",
       r"$f(2,-1)-f(1,1)=(-4+2)-(1+1)=-4$"],
  check=_c)


# ───────── 16.4 ─────────
def _c():
    Pp, Q = x**2*y - y, x**3/3 + exp(y**2)
    assert simplify(diff(Q, x) - diff(Pp, y)) == 1
P(id="3-113", ch=16, sec="16.4", type="16-green", src="2024 기말 1(a) 유형",
  q=r"$\mathbf F(x,y)=\Big\langle x^2y-y,\ \dfrac{x^3}{3}+e^{y^2}\Big\rangle$이고 $C$가 원 $(x-2)^2+(y+1)^2=9$ (반시계 방향)일 때 그린 정리로 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$Q_x-P_y$를 계산하면 $x^2$ 항이 지워져요. 원의 중심이 원점이 아니어도 넓이만 필요해요.",
  ans=r"$9\pi$",
  sol=[r"$Q_x-P_y=x^2-(x^2-1)=1$",
       r"$\displaystyle\oint_C\mathbf F\cdot d\mathbf r=\iint_D1\,dA=$ 원의 넓이 $=9\pi$"],
  check=_c)


def _c():
    pts = [(0, 0), (3, 0), (4, 2), (1, 4), (-1, 2)]
    tot = sum(line_int([-y, x], seg(a, b), 0, 1, (x, y)) for a, b in zip(pts, pts[1:] + pts[:1]))
    assert EQ(tot/2, 13)
P(id="3-114", ch=16, sec="16.4", type="16-greenarea", src="2024 기말 1(b) 유형",
  q=r"그린 정리를 이용해 꼭짓점이 $(0,0),\ (3,0),\ (4,2),\ (1,4),\ (-1,2)$인 오각형의 넓이를 구하라.",
  hint=r"$A=\dfrac12\displaystyle\oint x\,dy-y\,dx$. 선분 $(x_1,y_1)\to(x_2,y_2)$에서 $\int x\,dy-y\,dx=x_1y_2-x_2y_1$",
  ans=r"$13$",
  sol=[r"각 변의 $x_1y_2-x_2y_1$: $(0,0)\to(3,0)$: $0$,  $(3,0)\to(4,2)$: $6$,  $(4,2)\to(1,4)$: $16-2=14$",
       r"$(1,4)\to(-1,2)$: $2+4=6$,  $(-1,2)\to(0,0)$: $0$",
       r"$A=\dfrac12(0+6+14+6+0)=13$"],
  check=_c)


def _c():
    Pp, Q = sin(x) + 2*y, x**2 + 3*x + exp(y)
    green = integrate(integrate((diff(Q, x) - diff(Pp, y)).subs({x: r*cos(th), y: r*sin(th)})*r, (r, 0, 2*cos(th))), (th, 0, pi/2))
    assert EQ(green, 3*pi/2)
    segv = integrate(Pp.subs(y, 0), (x, 0, 2))
    assert EQ(segv, 1 - cos(2))
    arc = line_num([Pp, Q], [1 + cos(t), sin(t)], 0, pi, (x, y))
    assert abs(arc - float(3*pi/2 - 1 + cos(2))) < 1e-9
P(id="3-115", ch=16, sec="16.4", type="16-green", src="2022 기말(블럭2) 4번 유형 (곡선 닫기)",
  q=r"$C$가 원 $(x-1)^2+y^2=1$의 위쪽 반원을 $(2,0)$에서 $(0,0)$까지 가는 곡선일 때, 그린 정리를 이용해 $$\int_C(\sin x+2y)\,dx+(x^2+3x+e^{y})\,dy$$를 구하라.",
  hint=r"선분 $L:(0,0)\to(2,0)$을 붙이면 $C\cup L$은 위쪽 반원판의 경계(반시계). $Q_x-P_y=2x+1$, 반원판에서 $\bar x=1$",
  ans=r"$\dfrac{3\pi}{2}-1+\cos2$",
  sol=[r"$C\cup L$이 반원판 $D$의 경계(반시계): $\displaystyle\oint_{C\cup L}=\iint_D(2x+1)\,dA$",
       r"$\displaystyle\iint_D(2x+1)\,dA=2\bar x\cdot A+A=2\cdot1\cdot\frac\pi2+\frac\pi2=\frac{3\pi}{2}$ (극좌표 $r\le2\cos\theta$로 계산해도 같음)",
       r"$L$: $y=0,\ dy=0$ → $\displaystyle\int_0^2\sin x\,dx=1-\cos2$",
       r"$\displaystyle\int_C=\frac{3\pi}{2}-(1-\cos2)=\frac{3\pi}{2}-1+\cos2$"],
  check=_c)


def _c():
    Pp, Q = exp(x**2) - y**2, 2*x*y + atan(y)
    integrand = simplify(diff(Q, x) - diff(Pp, y))
    assert simplify(integrand - 4*y) == 0
    assert EQ(integrate(integrate(integrand, (y, x**2, 2*x)), (x, 0, 2)), R(128, 15))
P(id="3-116", ch=16, sec="16.4", type="16-green", src="과제 16.4 · 2024 기말 1(a) 유형",
  q=r"$C$가 포물선 $y=x^2$과 직선 $y=2x$로 둘러싸인 영역의 경계(반시계 방향)일 때 $\displaystyle\oint_C\big(e^{x^2}-y^2\big)\,dx+\big(2xy+\tan^{-1}y\big)\,dy$를 계산하라.",
  hint=r"$e^{x^2}$, $\tan^{-1}y$는 $Q_x-P_y$에서 사라져요. $Q_x-P_y=2y+2y$",
  ans=r"$\dfrac{128}{15}$",
  sol=[r"$Q_x-P_y=2y-(-2y)=4y$",
       r"$\displaystyle\int_0^2\!\!\int_{x^2}^{2x}4y\,dy\,dx=\int_0^22(4x^2-x^4)\,dx=2\Big(\frac{32}{3}-\frac{32}{5}\Big)=\frac{128}{15}$"],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2) + y, x/(x**2 + y**2) + 2*x]
    val = line_num(F, [1 + 2*cos(t), 2*sin(t)], 0, 2*pi, (x, y))
    assert abs(val - float(6*pi)) < 1e-9
P(id="3-117", ch=16, sec="16.4", type="16-singular", src="2022 기말(블럭1) 3번 · 2024 기말 4번 종합",
  q=r"$\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}+\big(y\,\mathbf i+2x\,\mathbf j\big)$이고 $C$가 원 $(x-1)^2+y^2=4$ (반시계 방향)일 때 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"두 부분으로 나눠요. 앞부분은 원점을 감싸는지가 핵심, 뒷부분은 보통의 그린 정리.",
  ans=r"$6\pi$",
  sol=[r"원 $(x-1)^2+y^2=4$는 원점을 감싸요 (중심까지 거리 $1<2$)",
       r"앞부분 $\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$: 원점을 한 번 반시계로 감는 닫힌 곡선 → $2\pi$",
       r"뒷부분 $\langle y,2x\rangle$: $Q_x-P_y=2-1=1$ → 원의 넓이 $4\pi$",
       r"합 $2\pi+4\pi=6\pi$"],
  check=_c)


def _c():
    F = [(x + y)/(x**2 + y**2), (y - x)/(x**2 + y**2)]
    val = line_int(F, [t, 2 - t**2], -2, 2, (x, y))
    assert EQ(val, 3*pi/2)
P(id="3-118", ch=16, sec="16.4", type="16-singular", src="2024 기말 4번 유형",
  q=r"$\mathbf F=\dfrac{x+y}{x^2+y^2}\,\mathbf i+\dfrac{y-x}{x^2+y^2}\,\mathbf j$이고 $C:\ \mathbf r(t)=t\,\mathbf i+(2-t^2)\,\mathbf j\ (-2\le t\le2)$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\mathbf F=\dfrac{\langle x,y\rangle}{x^2+y^2}-\dfrac{\langle-y,x\rangle}{x^2+y^2}=\nabla\big(\ln\sqrt{x^2+y^2}\big)-\nabla\theta$. 곡선이 원점 위쪽을 지나며 각이 얼마나 변하는지 보세요.",
  ans=r"$\dfrac{3\pi}{2}$",
  sol=[r"시작점 $(-2,-2)$, 끝점 $(2,-2)$, $t=0$에서 $(0,2)$ → 원점 위로 넘어가는 곡선 (시계 방향)",
       r"$\ln\sqrt{x^2+y^2}$ 부분: $\ln\sqrt8-\ln\sqrt8=0$",
       r"각 $\theta$: $\tfrac{5\pi}{4}$에서 시작해 $\tfrac\pi2$를 지나 $-\tfrac\pi4$에서 끝 → $\Delta\theta=-\tfrac{3\pi}{2}$",
       r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r=0-\Delta\theta=\frac{3\pi}{2}$"],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2), x/(x**2 + y**2)]
    p1 = line_int(F, [-2 + cos(t), sin(t)], pi, 0, (x, y))      # (-3,0)→(-1,0) 위쪽
    p2 = line_int(F, [cos(t), sin(t)], pi, 2*pi, (x, y))        # (-1,0)→(1,0) 아래쪽
    p3 = line_int(F, [2 + cos(t), sin(t)], pi, 0, (x, y))       # (1,0)→(3,0) 위쪽
    assert EQ(p1, 0) and EQ(p2, pi) and EQ(p3, 0)
P(id="3-119", ch=16, sec="16.4", type="16-singular", src="2022 기말(블럭1) 3번 유형",
  q=r"$\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$이고 $C$는 $(-3,0)$에서 $(3,0)$까지 세 반원으로 이루어진 곡선이다: 중심 $(-2,0)$ 반지름 $1$인 위쪽 반원 ($(-3,0)\to(-1,0)$), 중심 원점 반지름 $1$인 아래쪽 반원 ($(-1,0)\to(1,0)$), 중심 $(2,0)$ 반지름 $1$인 위쪽 반원 ($(1,0)\to(3,0)$). $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\mathbf F\cdot d\mathbf r=d\theta$ (원점 기준 각). 각 조각에서 원점에서 본 각이 얼마나 변하는지만 세면 돼요.",
  ans=r"$\pi$",
  sol=[r"첫 반원: 왼쪽 위에서만 움직여 $(-3,0)$과 $(-1,0)$ 모두 각 $\pi$ → 변화 $0$",
       r"둘째 반원: 원점을 아래로 돌아 각이 $\pi\to\tfrac{3\pi}{2}\to2\pi$ → 변화 $+\pi$",
       r"셋째 반원: 오른쪽 위에서만 움직여 시작·끝 각이 같음 → 변화 $0$",
       r"합 $\pi$ (직접 매개화해서 적분해도 $0,\ \pi,\ 0$)"],
  check=_c)


def _c():
    F = [-y/(x**2 + y**2), x/(x**2 + y**2), exp(z)]
    val = line_num(F, [cos(t)**3, sin(t), t], 0, pi)
    assert abs(val - float(pi + exp(pi) - 1)) < 1e-9
P(id="3-120", ch=16, sec="16.4", type="16-singular", src="2022 기말(블럭2) 3번 유형",
  q=r"$\mathbf F(x,y,z)=\dfrac{-y}{x^2+y^2}\,\mathbf i+\dfrac{x}{x^2+y^2}\,\mathbf j+e^{z}\,\mathbf k$, $C:\ \mathbf r(t)=\cos^3t\,\mathbf i+\sin t\,\mathbf j+t\,\mathbf k\ (0\le t\le\pi)$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$xy$ 부분은 원점에서 본 각의 변화, $e^z\,dz$ 부분은 $e^{z}$의 끝점 차예요. $y=\sin t\ge0$이라 위쪽 반평면만 지나요.",
  ans=r"$\pi+e^{\pi}-1$",
  sol=[r"$xy$평면 사영: $(1,0)$에서 $(-1,0)$까지 위쪽 반평면($y\ge0$)을 지남 → 각 변화 $\pi$",
       r"$\displaystyle\int\frac{-y\,dx+x\,dy}{x^2+y^2}=\pi$",
       r"$\displaystyle\int e^z\,dz=e^{\pi}-e^{0}=e^\pi-1$",
       r"합 $\pi+e^\pi-1$"],
  check=_c)

"""2단계 · 표준 추가분 — Ch.14 편도함수: 2-35 ~ 2-71"""
from bank_lib import *

lam = symbols('lambda', real=True)
k = symbols('k', real=True)
F = Function('f')


# ───────── 14.1 ─────────
def _c():
    f = sqrt(4 - x**2 - y**2) + log(x*y)
    assert EQ(f.subs({x: 1, y: 1}), sqrt(2)) and EQ(f.subs({x: -1, y: -1}), sqrt(2))
P(id="2-35", ch=14, sec="14.1", type="14-domain", src="과제 14.1 #10 · #13 유형",
  q=r"$f(x,y)=\sqrt{4-x^2-y^2}+\ln(xy)$의 정의역을 구하고 그림으로 설명하라.",
  hint=r"두 조건을 동시에: 근호 안 $\ge0$, 로그 안 $>0$",
  ans=r"$\{(x,y)\mid x^2+y^2\le4,\ xy>0\}$: 반지름 $2$인 원판 중 1사분면과 3사분면 부분 (좌표축 제외, 원주는 포함)",
  sol=[r"$4-x^2-y^2\ge0 \iff x^2+y^2\le4$ (원판, 경계 포함)",
       r"$xy>0 \iff$ $x,y$가 같은 부호 → 1사분면 또는 3사분면 (축 위는 제외)",
       r"정의역: 두 조건의 교집합 — 원판의 1·3사분면 조각 두 개"],
  check=_c)


# ───────── 14.2 ─────────
def _c():
    g = (x**2*y + x*y**2) / (x**2 - y**2)
    assert simplify(g - x*y/(x - y)) == 0 and EQ((x*y/(x - y)).subs({x: 1, y: -1}), R(-1, 2))
P(id="2-36", ch=14, sec="14.2", type="14-limit", src="과제 14.2 #8 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(1,-1)}\frac{x^2y+xy^2}{x^2-y^2}$를 구하라.",
  hint=r"분자 $=xy(x+y)$, 분모 $=(x-y)(x+y)$. 공통인수가 보여요.",
  ans=r"$-\dfrac12$",
  sol=[r"대입하면 $\tfrac00$ → $\dfrac{xy(x+y)}{(x-y)(x+y)}=\dfrac{xy}{x-y}$ ($x+y\ne0$)",
       r"$\dfrac{xy}{x-y}$은 $(1,-1)$에서 연속: $\dfrac{1\cdot(-1)}{1-(-1)}=-\dfrac12$"],
  check=_c)


def _c():
    f = (x**3 + x*y**2 + 2*y**3) / (x**2 + y**2)
    assert simplify(f - (x + 2*y**3/(x**2 + y**2))) == 0
    for th0 in (0, 1, 2):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0) == 0
P(id="2-37", ch=14, sec="14.2", type="14-limit", src="과제 14.2 #51 유형 (극좌표)",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3+xy^2+2y^3}{x^2+y^2}$를 구하라.",
  hint=r"$x^3+xy^2=x(x^2+y^2)$로 정리하거나 극좌표로 $r\to0^+$을 보세요.",
  ans=r"$0$",
  sol=[r"$\dfrac{x^3+xy^2+2y^3}{x^2+y^2}=x+\dfrac{2y^3}{x^2+y^2}$",
       r"$\left|\dfrac{2y^3}{x^2+y^2}\right|=2|y|\cdot\dfrac{y^2}{x^2+y^2}\le2|y|\to0$",
       r"따라서 극한은 $0+0=0$ (극좌표: $r(\cos^3\theta+\cos\theta\sin^2\theta+2\sin^3\theta)$, 크기 $\le4r\to0$)"],
  check=_c)


def _c():
    assert limit((exp(-u) - 1)/u, u, 0) == -1
P(id="2-38", ch=14, sec="14.2", type="14-limit", src="강의 14.2 (한 변수로 바꾸기) 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{e^{-x^2-y^2}-1}{x^2+y^2}$를 구하라.",
  hint=r"$u=x^2+y^2\to0^+$. $\displaystyle\lim_{u\to0}\frac{e^{-u}-1}{u}$는 로피탈 또는 미분의 정의.",
  ans=r"$-1$",
  sol=[r"$u=x^2+y^2$로 두면 $(x,y)\to(0,0)\iff u\to0^+$",
       r"$\displaystyle\lim_{u\to0^+}\frac{e^{-u}-1}{u}=\lim_{u\to0^+}\frac{-e^{-u}}{1}=-1$ (로피탈)"],
  check=_c)


def _c():
    f = (x**2 + sin(y)**2) / (2*x**2 + y**2)
    assert limit(f.subs(y, 0), x, 0) == R(1, 2) and limit(f.subs(x, 0), y, 0) == 1
P(id="2-39", ch=14, sec="14.2", type="14-dne", src="과제 14.2 #15 · #18 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2+\sin^2y}{2x^2+y^2}$가 존재하지 않음을 보여라.",
  hint=r"$x$축과 $y$축 두 경로를 비교해 보세요. $\displaystyle\lim_{y\to0}\frac{\sin y}{y}=1$",
  ans=r"$x$축을 따라 $\tfrac12$, $y$축을 따라 $1$ → 극한은 존재하지 않는다.",
  sol=[r"$x$축 ($y=0$): $\dfrac{x^2}{2x^2}=\dfrac12$",
       r"$y$축 ($x=0$): $\dfrac{\sin^2y}{y^2}=\Big(\dfrac{\sin y}{y}\Big)^2\to1$",
       r"두 값이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    f = x*y**4 / (x**2 + y**8)
    assert limit(f.subs(x, 0), y, 0) == 0
    assert simplify(f.subs(x, k*y**4) - k/(k**2 + 1)) == 0
    m = symbols('m', real=True)
    assert limit(f.subs(y, m*x), x, 0) == 0
P(id="2-40", ch=14, sec="14.2", type="14-dne", src="복습 14.1–3 기초1 · 심화1 유형 (곡선 경로)",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy^4}{x^2+y^8}$가 존재하지 않음을 보여라.",
  hint=r"직선 $y=mx$로는 모두 $0$이에요. $x^2$과 $y^8$의 차수를 맞추는 곡선 $x=ky^4$을 써 보세요.",
  ans=r"곡선 $x=ky^4$을 따라 $\dfrac{k}{k^2+1}$ ($k$마다 다름) → 극한은 존재하지 않는다.",
  sol=[r"직선 $y=mx$: $\dfrac{m^4x^5}{x^2+m^8x^8}=\dfrac{m^4x^3}{1+m^8x^6}\to0$ (판정 불가)",
       r"곡선 $x=ky^4$: $\dfrac{ky^8}{k^2y^8+y^8}=\dfrac{k}{k^2+1}$",
       r"$k=0$이면 $0$, $k=1$이면 $\tfrac12$ → 경로에 따라 달라 극한은 존재하지 않는다."],
  check=_c)


def _c():
    h = symbols('h', real=True)
    f = (x**3 + 2*y**3) / (x**2 + y**2)
    assert limit(f.subs({x: h, y: 0}) / h, h, 0) == 1 and limit(f.subs({x: 0, y: h}) / h, h, 0) == 2
    for th0 in (0, 1, 2.5):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0) == 0
P(id="2-41", ch=14, sec="14.3", type="14-defpartial", src="2022 중간(블럭2) 2번 유형",
  q=r"$f(x,y)=\dfrac{x^3+2y^3}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $f(0,0)=0$일 때<br>(a) $f$가 원점에서 연속임을 보여라.  (b) $f_x(0,0)$, $f_y(0,0)$을 구하라.",
  hint=r"(a) 극좌표: $f=r(\cos^3\theta+2\sin^3\theta)$. (b) 원점에서는 정의 $\displaystyle\lim_{h\to0}\frac{f(h,0)-f(0,0)}{h}$로.",
  ans=r"(a) $|f|\le3r\to0=f(0,0)$ → 연속  (b) $f_x(0,0)=1,\ f_y(0,0)=2$",
  sol=[r"(a) $x=r\cos\theta,\ y=r\sin\theta$: $f=\dfrac{r^3(\cos^3\theta+2\sin^3\theta)}{r^2}=r(\cos^3\theta+2\sin^3\theta)$",
       r"$|f|\le r(1+2)=3r\to0$ → $\displaystyle\lim_{(x,y)\to(0,0)}f=0=f(0,0)$, 연속",
       r"(b) $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{h^3/h^2}{h}=1$,  $f_y(0,0)=\displaystyle\lim_{h\to0}\frac{2h^3/h^2}{h}=2$"],
  check=_c)


# ───────── 14.3 ─────────
def _c():
    T = 80 / (1 + x**2 + 2*y**2)
    assert diff(T, x).subs({x: 1, y: 1}) == -10 and diff(T, y).subs({x: 1, y: 1}) == -20
P(id="2-42", ch=14, sec="14.3", type="14-partial", src="과제 14.3 #82 유형",
  q=r"평평한 금속판 위 점 $(x,y)$의 온도가 $T(x,y)=\dfrac{80}{1+x^2+2y^2}$ (°C, 단위 m)일 때, 점 $(1,1)$에서 (a) $x$방향 (b) $y$방향으로의 온도 변화율을 구하라.",
  hint=r"$T_x=-\dfrac{80\cdot2x}{(1+x^2+2y^2)^2}$",
  ans=r"(a) $T_x(1,1)=-10$ °C/m  (b) $T_y(1,1)=-20$ °C/m",
  sol=[r"분모 $1+x^2+2y^2=4$ (점 $(1,1)$)",
       r"$T_x=-\dfrac{160x}{(1+x^2+2y^2)^2}=-\dfrac{160}{16}=-10$",
       r"$T_y=-\dfrac{320y}{(1+x^2+2y^2)^2}=-\dfrac{320}{16}=-20$"],
  check=_c)


def _c():
    f = (x - y) / (x + 2*y)
    assert simplify(diff(f, x) - 3*y/(x + 2*y)**2) == 0 and simplify(diff(f, y) + 3*x/(x + 2*y)**2) == 0
    assert EQ(diff(f, x).subs({x: 1, y: 1}), R(1, 3)) and EQ(diff(f, y).subs({x: 1, y: 1}), R(-1, 3))
P(id="2-43", ch=14, sec="14.3", type="14-partial", src="과제 14.3 #19 유형",
  q=r"$f(x,y)=\dfrac{x-y}{x+2y}$의 편도함수 $f_x,\ f_y$를 구하고 $f_x(1,1),\ f_y(1,1)$을 구하라.",
  hint=r"몫의 미분: $\Big(\dfrac{u}{v}\Big)'=\dfrac{u'v-uv'}{v^2}$",
  ans=r"$f_x=\dfrac{3y}{(x+2y)^2},\ f_y=-\dfrac{3x}{(x+2y)^2}$;  $f_x(1,1)=\dfrac13,\ f_y(1,1)=-\dfrac13$",
  sol=[r"$f_x=\dfrac{1\cdot(x+2y)-(x-y)\cdot1}{(x+2y)^2}=\dfrac{3y}{(x+2y)^2}$",
       r"$f_y=\dfrac{(-1)(x+2y)-(x-y)\cdot2}{(x+2y)^2}=\dfrac{-3x}{(x+2y)^2}$",
       r"$(1,1)$: $\dfrac{3}{9}=\dfrac13$,  $-\dfrac{3}{9}=-\dfrac13$"],
  check=_c)


def _c():
    Fz = x**2 + y*z + z**3 - 3
    pt = {x: 1, y: 1, z: 1}
    assert Fz.subs(pt) == 0
    assert EQ((-diff(Fz, x)/diff(Fz, z)).subs(pt), R(-1, 2)) and EQ((-diff(Fz, y)/diff(Fz, z)).subs(pt), R(-1, 4))
P(id="2-44", ch=14, sec="14.3", type="14-implicit", src="강의 14.3 (음함수 미분) 유형",
  q=r"$x^2+yz+z^3=3$이 $z=z(x,y)$를 정할 때 점 $(1,1,1)$에서 $\dfrac{\partial z}{\partial x},\ \dfrac{\partial z}{\partial y}$를 구하라.",
  hint=r"$y$로 미분할 때 $yz$는 곱의 미분: $z+y\,z_y$",
  ans=r"$z_x=-\dfrac12,\ \ z_y=-\dfrac14$",
  sol=[r"$x$로 미분: $2x+y\,z_x+3z^2z_x=0 \Rightarrow z_x=-\dfrac{2x}{y+3z^2}=-\dfrac{2}{4}=-\dfrac12$",
       r"$y$로 미분: $z+y\,z_y+3z^2z_y=0 \Rightarrow z_y=-\dfrac{z}{y+3z^2}=-\dfrac14$",
       r"(공식 $z_x=-F_x/F_z$로 계산해도 같아요)"],
  check=_c)


def _c():
    uu = log(x**2 + y**2)
    assert simplify(diff(uu, x, 2) + diff(uu, y, 2)) == 0
    assert simplify(diff(uu, x, 2) - (2*y**2 - 2*x**2)/(x**2 + y**2)**2) == 0
P(id="2-45", ch=14, sec="14.3", type="14-higher", src="강의 14.3 (라플라스 방정식) 유형",
  q=r"$u(x,y)=\ln(x^2+y^2)$이 라플라스 방정식 $u_{xx}+u_{yy}=0$을 만족함을 보여라.",
  hint=r"$u_x=\dfrac{2x}{x^2+y^2}$를 몫의 미분으로 한 번 더 미분해요. $x$와 $y$의 역할이 대칭이에요.",
  ans=r"$u_{xx}=\dfrac{2y^2-2x^2}{(x^2+y^2)^2},\ u_{yy}=\dfrac{2x^2-2y^2}{(x^2+y^2)^2}$ → 합 $0$",
  sol=[r"$u_x=\dfrac{2x}{x^2+y^2}$,  $u_{xx}=\dfrac{2(x^2+y^2)-2x\cdot2x}{(x^2+y^2)^2}=\dfrac{2y^2-2x^2}{(x^2+y^2)^2}$",
       r"대칭으로 $u_{yy}=\dfrac{2x^2-2y^2}{(x^2+y^2)^2}$",
       r"$u_{xx}+u_{yy}=0$ ✓ (조화함수)"],
  check=_c)


# ───────── 14.4 ─────────
def _c():
    f = (x - 1)**2 + 3*(y + 2)**2 - 4
    pt = {x: 2, y: -1}
    assert f.subs(pt) == 0
    L = diff(f, x).subs(pt)*(x - 2) + diff(f, y).subs(pt)*(y + 1)
    assert simplify(L - (2*x + 6*y + 2)) == 0
P(id="2-46", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 #4 유형",
  q=r"곡면 $z=(x-1)^2+3(y+2)^2-4$ 위의 점 $(2,-1,0)$에서 접평면의 방정식을 구하라.",
  hint=r"$f_x=2(x-1),\ f_y=6(y+2)$",
  ans=r"$z=2x+6y+2$",
  sol=[r"$f_x(2,-1)=2(1)=2$,  $f_y(2,-1)=6(1)=6$",
       r"$z-0=2(x-2)+6(y+1)$",
       r"$z=2x+6y+2$ (검산: $(2,-1)$에서 $4-6+2=0$ ✓)"],
  check=_c)


def _c():
    f = x*log(x - 2*y) + 3
    pt = {x: 5, y: 2}
    assert f.subs(pt) == 3 and diff(f, x).subs(pt) == 5 and diff(f, y).subs(pt) == -10
    L = 3 + 5*(x - 5) - 10*(y - 2)
    assert EQ(L.subs({x: R(502, 100), y: R(199, 100)}), R(16, 5))
    assert abs(float(f.subs({x: 5.02, y: 1.99})) - 3.2) < 0.01
P(id="2-47", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 #17 유형",
  q=r"$f(x,y)=x\ln(x-2y)+3$의 점 $(5,2)$에서의 선형화 $L(x,y)$를 구하고 $f(5.02,\ 1.99)$의 근삿값을 구하라.",
  hint=r"$x-2y=1$이라 $\ln1=0$. $f_x=\ln(x-2y)+\dfrac{x}{x-2y}$",
  ans=r"$L(x,y)=3+5(x-5)-10(y-2)$,  $f(5.02,1.99)\approx3.2$",
  sol=[r"$f(5,2)=5\ln1+3=3$",
       r"$f_x=\ln(x-2y)+\dfrac{x}{x-2y}=0+5=5$,  $f_y=\dfrac{-2x}{x-2y}=-10$",
       r"$L(x,y)=3+5(x-5)-10(y-2)$",
       r"$L(5.02,1.99)=3+5(0.02)-10(-0.01)=3+0.1+0.1=3.2$"],
  check=_c)


def _c():
    w = x**2*exp(y*z)
    pt = {x: 1, y: 0, z: 2}
    dw = diff(w, x).subs(pt)*R(1, 10) + diff(w, y).subs(pt)*R(5, 100) + diff(w, z).subs(pt)*R(-1, 10)
    assert EQ(dw, R(3, 10))
P(id="2-48", ch=14, sec="14.4", type="14-diff", src="과제 14.4 #33 유형",
  q=r"$w=x^2e^{yz}$의 전미분 $dw$를 구하고, 점 $(1,0,2)$에서 $dx=0.1,\ dy=0.05,\ dz=-0.1$일 때 $dw$의 값을 구하라.",
  hint=r"$dw=w_x\,dx+w_y\,dy+w_z\,dz$",
  ans=r"$dw=2xe^{yz}dx+x^2ze^{yz}dy+x^2ye^{yz}dz$,  값 $0.3$",
  sol=[r"$w_x=2xe^{yz},\ w_y=x^2ze^{yz},\ w_z=x^2ye^{yz}$",
       r"$(1,0,2)$에서 $e^{0}=1$: $w_x=2,\ w_y=2,\ w_z=0$",
       r"$dw=2(0.1)+2(0.05)+0(-0.1)=0.3$"],
  check=_c)


def _c():
    rr, hh = symbols('rr hh', positive=True)
    V = pi*rr**2*hh
    dV = (diff(V, rr)*R(1, 10) + diff(V, hh)*R(1, 10)).subs({rr: 10, hh: 25})
    assert EQ(dV, 60*pi)
P(id="2-49", ch=14, sec="14.4", type="14-diff", src="강의 14.4 (오차 추정) 유형",
  q=r"원기둥의 반지름과 높이를 재었더니 $r=10$ cm, $h=25$ cm이고, 각 측정의 오차는 최대 $0.1$ cm이다. 전미분으로 부피 계산의 최대 오차를 추정하라.",
  hint=r"$V=\pi r^2h$, $dV=2\pi rh\,dr+\pi r^2\,dh$에 $|dr|,|dh|\le0.1$",
  ans=r"$60\pi\ \text{cm}^3$ (약 $188$ cm³)",
  sol=[r"$dV=V_r\,dr+V_h\,dh=2\pi rh\,dr+\pi r^2\,dh$",
       r"$=2\pi(10)(25)(0.1)+\pi(100)(0.1)=50\pi+10\pi=60\pi$",
       r"최대 오차 약 $60\pi\approx188$ cm³ (부피 $2500\pi$의 약 $2.4\%$)"],
  check=_c)


# ───────── 14.5 ─────────
def _c():
    zz = (x - y) / (x + 2*y)
    Z = zz.subs({x: exp(t), y: exp(-t)})
    assert EQ(diff(Z, t).subs(t, 0), R(2, 3))
P(id="2-50", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #4 유형",
  q=r"$z=\dfrac{x-y}{x+2y}$, $x=e^{t}$, $y=e^{-t}$일 때 $t=0$에서 $\dfrac{dz}{dt}$를 구하라.",
  hint=r"2-43의 $z_x=\dfrac{3y}{(x+2y)^2},\ z_y=-\dfrac{3x}{(x+2y)^2}$를 쓰면 빨라요.",
  ans=r"$\dfrac23$",
  sol=[r"$t=0$: $x=y=1$. $z_x=\dfrac{3}{9}=\dfrac13$, $z_y=-\dfrac13$",
       r"$\dfrac{dx}{dt}=e^{t}=1$, $\dfrac{dy}{dt}=-e^{-t}=-1$",
       r"$\dfrac{dz}{dt}=\dfrac13\cdot1+\Big(-\dfrac13\Big)(-1)=\dfrac23$"],
  check=_c)


def _c():
    zz = sqrt(x)*exp(x*y)
    Z = zz.subs({x: 1 + s*t, y: s**2 - t**2})
    assert EQ(diff(Z, s).subs({s: 1, t: 1}), 17*sqrt(2)/4) and EQ(diff(Z, t).subs({s: 1, t: 1}), -15*sqrt(2)/4)
P(id="2-51", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #14 유형",
  q=r"$z=\sqrt{x}\,e^{xy}$, $x=1+st$, $y=s^2-t^2$일 때 $(s,t)=(1,1)$에서 $\dfrac{\partial z}{\partial s}$, $\dfrac{\partial z}{\partial t}$를 구하라.",
  hint=r"$(s,t)=(1,1)$이면 $(x,y)=(2,0)$. $z_x=\dfrac{e^{xy}}{2\sqrt x}+\sqrt x\,ye^{xy}$",
  ans=r"$z_s=\dfrac{17\sqrt2}{4},\ \ z_t=-\dfrac{15\sqrt2}{4}$",
  sol=[r"$(x,y)=(2,0)$: $z_x=\dfrac{1}{2\sqrt2}=\dfrac{\sqrt2}{4}$,  $z_y=\sqrt x\cdot xe^{xy}=2\sqrt2$",
       r"$x_s=t=1,\ y_s=2s=2,\ x_t=s=1,\ y_t=-2t=-2$",
       r"$z_s=\dfrac{\sqrt2}{4}+2\sqrt2\cdot2=\dfrac{17\sqrt2}{4}$",
       r"$z_t=\dfrac{\sqrt2}{4}-4\sqrt2=-\dfrac{15\sqrt2}{4}$"],
  check=_c)


def _c():
    xt, yt = sqrt(1 + t), 2 + t/3
    assert xt.subs(t, 3) == 2 and yt.subs(t, 3) == 3
    assert EQ(5*diff(xt, t).subs(t, 3) + (-6)*diff(yt, t).subs(t, 3), R(-3, 4))
P(id="2-52", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #39 유형",
  q=r"벌레가 $t$초 후 위치 $x=\sqrt{1+t},\ y=2+\tfrac13t$ (cm)로 기어간다. 온도 $T(x,y)$가 $T_x(2,3)=5,\ T_y(2,3)=-6$을 만족할 때, $3$초 후 벌레가 느끼는 온도의 변화율을 구하라.",
  hint=r"$t=3$이면 $(x,y)=(2,3)$. $\dfrac{dT}{dt}=T_x\dfrac{dx}{dt}+T_y\dfrac{dy}{dt}$",
  ans=r"$-\dfrac34$ °C/s (온도가 내려간다)",
  sol=[r"$t=3$: $x=\sqrt4=2,\ y=2+1=3$",
       r"$\dfrac{dx}{dt}=\dfrac{1}{2\sqrt{1+t}}=\dfrac14$,  $\dfrac{dy}{dt}=\dfrac13$",
       r"$\dfrac{dT}{dt}=5\cdot\dfrac14+(-6)\cdot\dfrac13=\dfrac54-2=-\dfrac34$"],
  check=_c)


def _c():
    w = x*y + y*z + z*x
    W = w.subs({x: r*cos(th), y: r*sin(th), z: r*th})
    assert EQ(diff(W, r).subs({r: 1, th: pi/4}), 1 + sqrt(2)*pi/2) and EQ(diff(W, th).subs({r: 1, th: pi/4}), sqrt(2))
P(id="2-53", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #27 유형",
  q=r"$w=xy+yz+zx$, $x=r\cos\theta,\ y=r\sin\theta,\ z=r\theta$일 때 $r=1,\ \theta=\dfrac\pi4$에서 $\dfrac{\partial w}{\partial r}$, $\dfrac{\partial w}{\partial\theta}$를 구하라.",
  hint=r"점에서 $x=y=\tfrac{\sqrt2}{2},\ z=\tfrac\pi4$. $w_x=y+z,\ w_y=x+z,\ w_z=x+y$",
  ans=r"$w_r=1+\dfrac{\sqrt2\,\pi}{2},\ \ w_\theta=\sqrt2$",
  sol=[r"$w_x=w_y=\tfrac{\sqrt2}{2}+\tfrac\pi4$, $w_z=\sqrt2$",
       r"$w_r=w_x\cos\theta+w_y\sin\theta+w_z\theta=2\Big(\tfrac{\sqrt2}{2}+\tfrac\pi4\Big)\tfrac{\sqrt2}{2}+\sqrt2\cdot\tfrac\pi4=1+\dfrac{\sqrt2\pi}{2}$",
       r"$w_\theta=w_x(-r\sin\theta)+w_y(r\cos\theta)+w_z\cdot r=0+\sqrt2=\sqrt2$ ($w_x=w_y$이라 앞 두 항이 상쇄)"],
  check=_c)


def _c():
    f = x**2*y + exp(x)*y**3
    zr = (diff(f, x)*cos(th) + diff(f, y)*sin(th))
    zth = (-diff(f, x)*r*sin(th) + diff(f, y)*r*cos(th))
    expr = (zr**2 + zth**2/r**2) - (diff(f, x)**2 + diff(f, y)**2)
    assert simplify(expr) == 0
    Z = f.subs({x: r*cos(th), y: r*sin(th)}, simultaneous=True)
    assert simplify(diff(Z, r) - zr.subs({x: r*cos(th), y: r*sin(th)}, simultaneous=True)) == 0
P(id="2-54", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #49 유형",
  q=r"$z=f(x,y)$, $x=r\cos\theta,\ y=r\sin\theta$일 때 (a) $z_r,\ z_\theta$를 $f_x,\ f_y$로 나타내고 (b) $\Big(\dfrac{\partial z}{\partial x}\Big)^2+\Big(\dfrac{\partial z}{\partial y}\Big)^2=\Big(\dfrac{\partial z}{\partial r}\Big)^2+\dfrac{1}{r^2}\Big(\dfrac{\partial z}{\partial\theta}\Big)^2$임을 보여라.",
  hint=r"(b)는 오른쪽을 전개해서 $\sin^2\theta+\cos^2\theta=1$을 써요. 교차항이 지워져요.",
  ans=r"(a) $z_r=f_x\cos\theta+f_y\sin\theta,\ z_\theta=-f_xr\sin\theta+f_yr\cos\theta$  (b) 아래 풀이",
  sol=[r"(a) $z_r=f_x\,x_r+f_y\,y_r=f_x\cos\theta+f_y\sin\theta$,  $z_\theta=f_x(-r\sin\theta)+f_y(r\cos\theta)$",
       r"(b) $z_r^2=f_x^2\cos^2\theta+2f_xf_y\sin\theta\cos\theta+f_y^2\sin^2\theta$",
       r"$\dfrac{z_\theta^2}{r^2}=f_x^2\sin^2\theta-2f_xf_y\sin\theta\cos\theta+f_y^2\cos^2\theta$",
       r"더하면 $f_x^2+f_y^2$ ✓"],
  check=_c)


def _c():
    f = x**3*y + x*y**2 + exp(x)
    X, Y = r**2 - s**2, 2*r*s
    Z = f.subs({x: X, y: Y}, simultaneous=True)
    rhs = (2*diff(f, x) + 4*r**2*diff(f, x, 2) + 8*r*s*diff(f, x, y) + 4*s**2*diff(f, y, 2)).subs({x: X, y: Y}, simultaneous=True)
    assert simplify(diff(Z, r, 2) - rhs) == 0
P(id="2-55", ch=14, sec="14.5", type="14-chain2", src="복습 14.4–6 기초1 유형",
  q=r"$z=f(x,y)$의 2계 편도함수가 연속이고 $x=r^2-s^2$, $y=2rs$일 때 (a) $\dfrac{\partial z}{\partial r}$ (b) $\dfrac{\partial^2z}{\partial r^2}$를 $f$의 편도함수로 나타내라.",
  hint=r"$z_r=2r\,f_x+2s\,f_y$. 다시 $r$로 미분할 때 $2r\,f_x$는 곱의 미분, $f_x$ 자신은 연쇄법칙.",
  ans=r"(a) $z_r=2rf_x+2sf_y$  (b) $z_{rr}=2f_x+4r^2f_{xx}+8rs\,f_{xy}+4s^2f_{yy}$",
  sol=[r"(a) $x_r=2r,\ y_r=2s$ → $z_r=2rf_x+2sf_y$",
       r"(b) $(f_x)_r=f_{xx}\cdot2r+f_{xy}\cdot2s$,  $(f_y)_r=f_{yx}\cdot2r+f_{yy}\cdot2s$",
       r"$z_{rr}=2f_x+2r(2rf_{xx}+2sf_{xy})+2s(2rf_{xy}+2sf_{yy})$",
       r"$=2f_x+4r^2f_{xx}+8rs\,f_{xy}+4s^2f_{yy}$"],
  check=_c)


# ───────── 14.6 ─────────
def _c():
    f = y*cos(x*y)
    g = grad(f, (x, y)).subs({x: 0, y: 2})
    assert EQ(g, [0, 1]) and EQ(g.dot(Matrix([cos(pi/6), sin(pi/6)])), R(1, 2))
P(id="2-56", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #5 유형",
  q=r"$f(x,y)=y\cos(xy)$의 점 $(0,2)$에서 각 $\theta=\dfrac\pi6$ 방향으로의 방향도함수를 구하라.",
  hint=r"각 $\theta$ 방향의 단위벡터는 $\mathbf u=\langle\cos\theta,\ \sin\theta\rangle$",
  ans=r"$\dfrac12$",
  sol=[r"$f_x=-y^2\sin(xy)\Rightarrow0$,  $f_y=\cos(xy)-xy\sin(xy)\Rightarrow1$ (점 $(0,2)$)",
       r"$\mathbf u=\left\langle\tfrac{\sqrt3}{2},\ \tfrac12\right\rangle$",
       r"$D_{\mathbf u}f=0\cdot\tfrac{\sqrt3}{2}+1\cdot\tfrac12=\dfrac12$"],
  check=_c)


def _c():
    f = x*y**2*z - x**2*z**3
    g = grad(f, (x, y, z)).subs({x: 1, y: 2, z: -1})
    assert EQ(g, [-2, -4, 1]) and EQ(g.dot(Matrix([R(2, 3), R(-2, 3), R(1, 3)])), R(5, 3))
P(id="2-57", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #11 유형",
  q=r"$f(x,y,z)=xy^2z-x^2z^3$에 대해 (a) $\nabla f(1,2,-1)$을 구하고 (b) 점 $(1,2,-1)$에서 $\mathbf u=\left\langle\tfrac23,-\tfrac23,\tfrac13\right\rangle$ 방향의 변화율을 구하라.",
  hint=r"$f_x=y^2z-2xz^3,\ f_y=2xyz,\ f_z=xy^2-3x^2z^2$",
  ans=r"(a) $\langle-2,-4,1\rangle$  (b) $\dfrac53$",
  sol=[r"$f_x=4(-1)-2(1)(-1)=-2$,  $f_y=2(1)(2)(-1)=-4$,  $f_z=4-3=1$",
       r"(b) $\mathbf u$는 이미 단위벡터 ($\tfrac49+\tfrac49+\tfrac19=1$)",
       r"$D_{\mathbf u}f=-\tfrac43+\tfrac83+\tfrac13=\dfrac53$"],
  check=_c)


def _c():
    f = 4*x*y**3
    g = grad(f, (x, y)).subs({x: 1, y: -1})
    assert EQ(g, [-4, 12]) and EQ(g.norm(), 4*sqrt(10))
P(id="2-58", ch=14, sec="14.6", type="14-maxrate", src="과제 14.6 #27 유형",
  q=r"$f(x,y)=4xy^3$의 점 $(1,-1)$에서 최대 변화율과 그 방향을 구하라.",
  hint=r"최대 변화율 $=|\nabla f|$, 방향은 $\nabla f$",
  ans=r"최대 변화율 $4\sqrt{10}$, 방향 $\tfrac{1}{\sqrt{10}}\langle-1,3\rangle$",
  sol=[r"$\nabla f=\langle4y^3,\ 12xy^2\rangle \Rightarrow \nabla f(1,-1)=\langle-4,\ 12\rangle$",
       r"$|\nabla f|=\sqrt{16+144}=\sqrt{160}=4\sqrt{10}$",
       r"방향: $\dfrac{\langle-4,12\rangle}{4\sqrt{10}}=\dfrac{1}{\sqrt{10}}\langle-1,3\rangle$"],
  check=_c)


def _c():
    a_, b_ = symbols('a_ b_', real=True)
    sol = solve([(3*a_ + 4*b_)/5 - 4, b_ - 2], [a_, b_])
    assert sol == {a_: 4, b_: 2}
    assert EQ((5*4 + 12*2) / R(13), R(44, 13))
P(id="2-59", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #41 유형",
  q=r"$f$의 편도함수가 연속이고 네 점 $A(1,2),\ B(4,6),\ C(1,5),\ D(6,14)$가 있다. $A$에서 $\overrightarrow{AB}$ 방향의 방향도함수가 $4$, $\overrightarrow{AC}$ 방향의 방향도함수가 $2$일 때, $A$에서 $\overrightarrow{AD}$ 방향의 방향도함수를 구하라.",
  hint=r"$\nabla f(A)=\langle a,b\rangle$로 두고 두 조건으로 연립방정식을 세워요.",
  ans=r"$\dfrac{44}{13}$",
  sol=[r"$\overrightarrow{AB}=\langle3,4\rangle$ (길이 $5$), $\overrightarrow{AC}=\langle0,3\rangle$ (길이 $3$), $\overrightarrow{AD}=\langle5,12\rangle$ (길이 $13$)",
       r"$\dfrac{3a+4b}{5}=4,\ \ \dfrac{3b}{3}=2$ → $b=2,\ a=4$",
       r"$D_{\overrightarrow{AD}}f=\dfrac{5\cdot4+12\cdot2}{13}=\dfrac{44}{13}$"],
  check=_c)


def _c():
    Fz = x**2 + 2*y**2 + 3*z**2
    pt = {x: 4, y: -1, z: 1}
    assert Fz.subs(pt) == 21
    assert EQ(grad(Fz, (x, y, z)).subs(pt), [8, -4, 6]) and 4*4 - 2*(-1) + 3*1 == 21
P(id="2-60", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 (타원면의 접평면) 유형",
  q=r"타원면 $x^2+2y^2+3z^2=21$ 위의 점 $(4,-1,1)$에서 접평면과 법선의 방정식을 구하라.",
  hint=r"$\nabla F=\langle2x,\ 4y,\ 6z\rangle$",
  ans=r"접평면 $4x-2y+3z=21$,  법선 $\dfrac{x-4}{4}=\dfrac{y+1}{-2}=\dfrac{z-1}{3}$",
  sol=[r"$\nabla F(4,-1,1)=\langle8,-4,6\rangle\parallel\langle4,-2,3\rangle$",
       r"접평면: $4(x-4)-2(y+1)+3(z-1)=0 \Rightarrow 4x-2y+3z=21$",
       r"법선: $\dfrac{x-4}{4}=\dfrac{y+1}{-2}=\dfrac{z-1}{3}$"],
  check=_c)


def _c():
    sols = solve([x - t, y - 2*t, z - t, x**2 + y**2 + z**2 - 6], [x, y, z, t], dict=True)
    pts = sorted((s_[x], s_[y], s_[z]) for s_ in sols)
    assert pts == [(-1, -2, -1), (1, 2, 1)]
P(id="2-61", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 응용 (평행한 접평면)",
  q=r"구면 $x^2+y^2+z^2=6$ 위에서 접평면이 평면 $x+2y+z=1$과 평행한 점을 모두 구하고, 그 점에서의 접평면을 구하라.",
  hint=r"평행 $\iff$ 법선벡터 $\nabla F=\langle2x,2y,2z\rangle$가 $\langle1,2,1\rangle$의 실수배",
  ans=r"$(1,2,1)$에서 $x+2y+z=6$,  $(-1,-2,-1)$에서 $x+2y+z=-6$",
  sol=[r"$\langle2x,2y,2z\rangle=k\langle1,2,1\rangle$ → $(x,y,z)=(t,2t,t)$ 꼴",
       r"구면에 대입: $t^2+4t^2+t^2=6 \Rightarrow t=\pm1$ → $(1,2,1),\ (-1,-2,-1)$",
       r"접평면: $(x-1)+2(y-2)+(z-1)=0 \Rightarrow x+2y+z=6$, 다른 점에서는 $x+2y+z=-6$"],
  check=_c)


# ───────── 14.7 ─────────
def _c():
    f = x*y*exp(-(x**2 + y**2)/2)
    fx, fy = diff(f, x), diff(f, y)
    for p_ in [(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        assert simplify(fx.subs({x: p_[0], y: p_[1]})) == 0 and simplify(fy.subs({x: p_[0], y: p_[1]})) == 0
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert simplify(D.subs({x: 0, y: 0})) == -1
    assert simplify(D.subs({x: 1, y: 1}) - 4*exp(-2)) == 0 and simplify(diff(f, x, 2).subs({x: 1, y: 1}) + 2*exp(-1)) == 0
    assert simplify(diff(f, x, 2).subs({x: 1, y: -1}) - 2*exp(-1)) == 0
P(id="2-62", ch=14, sec="14.7", type="14-crit", src="강의 14.7 · 과제 14.7 #19 유형 (지수함수)",
  q=r"$f(x,y)=xye^{-(x^2+y^2)/2}$의 극댓값, 극솟값, 안장점을 구하라.",
  hint=r"$f_x=y(1-x^2)e^{-(x^2+y^2)/2}$, $f_y=x(1-y^2)e^{-(x^2+y^2)/2}$. 지수 부분은 $0$이 아니에요.",
  ans=r"$(0,0)$ 안장점,  $(1,1),(-1,-1)$에서 극댓값 $e^{-1}$,  $(1,-1),(-1,1)$에서 극솟값 $-e^{-1}$",
  sol=[r"$y(1-x^2)=0,\ x(1-y^2)=0$ → $(0,0)$ 또는 $x=\pm1,\ y=\pm1$",
       r"$f_{xx}=xy(x^2-3)e^{g},\ f_{yy}=xy(y^2-3)e^{g},\ f_{xy}=(1-x^2)(1-y^2)e^{g}$ ($g=-\tfrac{x^2+y^2}{2}$)",
       r"$(0,0)$: $D=0\cdot0-1^2=-1<0$ → 안장점",
       r"$(1,1),(-1,-1)$: $f_{xx}=-2e^{-1}<0,\ D=4e^{-2}>0$ → 극댓값 $e^{-1}$",
       r"$(1,-1),(-1,1)$: $f_{xx}=2e^{-1}>0,\ D>0$ → 극솟값 $-e^{-1}$"],
  check=_c)


def _c():
    f = x**3 + y**3 - 3*x*y
    sols = [s_ for s_ in solve([diff(f, x), diff(f, y)], [x, y], dict=True) if s_[x].is_real]
    assert sorted((s_[x], s_[y]) for s_ in sols) == [(0, 0), (1, 1)]
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert D.subs({x: 0, y: 0}) == -9 and D.subs({x: 1, y: 1}) == 27 and f.subs({x: 1, y: 1}) == -1
P(id="2-63", ch=14, sec="14.7", type="14-crit", src="강의 14.7 유형",
  q=r"$f(x,y)=x^3+y^3-3xy$의 임계점을 구하고 분류하라.",
  hint=r"$f_x=0$에서 $y=x^2$을 $f_y=0$에 넣으면 $x^4=x$",
  ans=r"$(0,0)$ 안장점,  $(1,1)$에서 극솟값 $-1$",
  sol=[r"$f_x=3x^2-3y=0 \Rightarrow y=x^2$,  $f_y=3y^2-3x=0 \Rightarrow x^4=x$",
       r"$x=0$ 또는 $x=1$ → $(0,0),\ (1,1)$",
       r"$f_{xx}=6x,\ f_{yy}=6y,\ f_{xy}=-3$. $(0,0)$: $D=-9<0$ → 안장점",
       r"$(1,1)$: $D=36-9=27>0,\ f_{xx}=6>0$ → 극솟값 $1+1-3=-1$"],
  check=_c)


def _c():
    f = 2*x**3 + 6*x*y**2 - 3*y**3 - 150*x
    sols = [s_ for s_ in solve([diff(f, x), diff(f, y)], [x, y], dict=True) if s_[x].is_real]
    assert sorted((s_[x], s_[y]) for s_ in sols) == [(-5, 0), (-3, -4), (3, 4), (5, 0)]
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert D.subs({x: 5, y: 0}) > 0 and diff(f, x, 2).subs({x: 5, y: 0}) > 0 and f.subs({x: 5, y: 0}) == -500
    assert D.subs({x: -5, y: 0}) > 0 and diff(f, x, 2).subs({x: -5, y: 0}) < 0 and f.subs({x: -5, y: 0}) == 500
    assert D.subs({x: 3, y: 4}) < 0 and D.subs({x: -3, y: -4}) < 0
P(id="2-64", ch=14, sec="14.7", type="14-crit", src="2025 중간 2(a) 유형",
  q=r"$f(x,y)=2x^3+6xy^2-3y^3-150x$의 극댓값, 극솟값, 안장점을 구하라.",
  hint=r"$f_x=0 \iff x^2+y^2=25$, $f_y=3y(4x-3y)=0$. 경우를 나눠요.",
  ans=r"$(5,0)$에서 극솟값 $-500$,  $(-5,0)$에서 극댓값 $500$,  안장점 $(3,4),\ (-3,-4)$",
  sol=[r"$f_x=6x^2+6y^2-150=0 \Rightarrow x^2+y^2=25$,  $f_y=12xy-9y^2=3y(4x-3y)=0$",
       r"$y=0$: $x=\pm5$.  $y=\tfrac43x$: $x^2+\tfrac{16}{9}x^2=25 \Rightarrow x=\pm3$ → $(3,4),\ (-3,-4)$",
       r"$f_{xx}=12x,\ f_{yy}=12x-18y,\ f_{xy}=12y$",
       r"$(5,0)$: $f_{xx}=60,\ D=3600>0$ → 극솟값 $-500$.  $(-5,0)$: $f_{xx}=-60,\ D=3600>0$ → 극댓값 $500$",
       r"$(3,4)$: $D=36\cdot(-36)-48^2<0$,  $(-3,-4)$: $D=(-36)(36)-48^2<0$ → 둘 다 안장점"],
  check=_c)


def _c():
    f = x**2 + y**2 - x**2*y + 2
    cands = [(0, 0), (1, -1), (-1, -1), (1, 1), (-1, 1), (1, R(1, 2)), (-1, R(1, 2)), (0, -1)]
    vals = [f.subs({x: a, y: b}) for a, b in cands]
    assert max(vals) == 5 and min(vals) == 2
    assert f.subs(y, 1) == 3
P(id="2-65", ch=14, sec="14.7", type="14-absext", src="과제 14.7 #35 유형",
  q=r"$f(x,y)=x^2+y^2-x^2y+2$의 정사각형 $D=\{(x,y)\mid|x|\le1,\ |y|\le1\}$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"내부: $f_x=2x(1-y)$, $f_y=2y-x^2$. 경계는 네 변을 따로 봐요.",
  ans=r"최댓값 $5$ (점 $(\pm1,-1)$),  최솟값 $2$ (점 $(0,0)$)",
  sol=[r"내부: $2x(1-y)=0,\ 2y=x^2$ → $(0,0)$만 ($y=1$이면 $x^2=2$로 밖), $f=2$",
       r"$y=1$: $f=3$ (일정).  $y=-1$: $f=2x^2+3\in[3,5]$",
       r"$x=\pm1$: $f=y^2-y+3$, $y\in[-1,1]$ → 최소 $\tfrac{11}{4}$ ($y=\tfrac12$), 최대 $5$ ($y=-1$)",
       r"비교: 최댓값 $5$ (점 $(\pm1,-1)$), 최솟값 $2$ (점 $(0,0)$)"],
  check=_c)


def _c():
    f = 2*x**2 - 4*x + y**2 - 4*y + 1
    vals = {(0, 0): f.subs({x: 0, y: 0}), (0, 2): f.subs({x: 0, y: 2}), (1, 2): f.subs({x: 1, y: 2})}
    assert vals[(0, 0)] == 1 and vals[(1, 2)] == -5 and vals[(0, 2)] == -3
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: 1, y: 2}
    g = f.subs(y, 2*x)
    assert solve(diff(g, x), x) == [1]
P(id="2-66", ch=14, sec="14.7", type="14-absext", src="강의 14.7 (닫힌 삼각형 영역) 유형",
  q=r"$f(x,y)=2x^2-4x+y^2-4y+1$의, 직선 $x=0$, $y=2$, $y=2x$로 둘러싸인 닫힌 삼각형 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"꼭짓점은 $(0,0),\ (0,2),\ (1,2)$. 내부 임계점 $(1,2)$는 사실 꼭짓점이에요.",
  ans=r"최댓값 $1$ (점 $(0,0)$),  최솟값 $-5$ (점 $(1,2)$)",
  sol=[r"$f_x=4x-4=0,\ f_y=2y-4=0$ → $(1,2)$ (꼭짓점, 내부에는 임계점 없음)",
       r"$x=0$: $y^2-4y+1$ ($0\le y\le2$) → $1$에서 $-3$ 사이",
       r"$y=2$: $2x^2-4x-3$ ($0\le x\le1$) → $-3$에서 $-5$ 사이",
       r"$y=2x$: $6x^2-12x+1$ ($0\le x\le1$) → $1$에서 $-5$ 사이",
       r"최댓값 $1$ (점 $(0,0)$), 최솟값 $-5$ (점 $(1,2)$)"],
  check=_c)


def _c():
    d2 = x**2 + y**2 + (x*y + 1)
    assert solve([diff(d2, x), diff(d2, y)], [x, y]) == {x: 0, y: 0}
    D = diff(d2, x, 2)*diff(d2, y, 2) - diff(d2, x, y)**2
    assert D == 3 and d2.subs({x: 0, y: 0}) == 1
P(id="2-67", ch=14, sec="14.7", type="14-optim", src="과제 14.7 #45 유형",
  q=r"곡면 $z^2=xy+1$ 위에서 원점에 가장 가까운 점과 그 거리를 구하라.",
  hint=r"거리의 제곱 $d^2=x^2+y^2+z^2=x^2+y^2+xy+1$을 $x,y$의 함수로 최소화해요.",
  ans=r"$(0,0,1),\ (0,0,-1)$,  거리 $1$",
  sol=[r"$g(x,y)=x^2+y^2+xy+1$ (곡면에서 $z^2=xy+1$)",
       r"$g_x=2x+y=0,\ g_y=2y+x=0$ → $(0,0)$",
       r"$D=2\cdot2-1=3>0,\ g_{xx}>0$ → 최소 $g=1$, 이때 $z^2=1$",
       r"가장 가까운 점 $(0,0,\pm1)$, 거리 $1$"],
  check=_c)


# ───────── 14.8 ─────────
def _c():
    f = x**2 + y**2
    sols = solve([2*x - lam*(2*x + y), 2*y - lam*(x + 2*y), x**2 + x*y + y**2 - 3], [x, y, lam], dict=True)
    vals = sorted(set(simplify(f.subs(s_)) for s_ in sols))
    assert vals == [2, 6]
P(id="2-68", ch=14, sec="14.8", type="14-lagrange", src="과제 14.8 #12 유형",
  q=r"곡선 $x^2+xy+y^2=3$ 위에서 $f(x,y)=x^2+y^2$의 최댓값과 최솟값을 구하라.",
  hint=r"$2x=\lambda(2x+y),\ 2y=\lambda(x+2y)$. 두 식을 빼거나 나눠서 $y=x$ 또는 $y=-x$를 얻어요.",
  ans=r"최댓값 $6$ (점 $(\sqrt3,-\sqrt3),(-\sqrt3,\sqrt3)$),  최솟값 $2$ (점 $(1,1),(-1,-1)$)",
  sol=[r"두 식을 빼면 $2(x-y)=\lambda(x-y)$ → $x=y$ 또는 $\lambda=2$",
       r"$x=y$: $3x^2=3$ → $(1,1),(-1,-1)$, $f=2$",
       r"$\lambda=2$: $2x=2(2x+y) \Rightarrow y=-x$ → $x^2=3$ → $(\sqrt3,-\sqrt3),(-\sqrt3,\sqrt3)$, $f=6$",
       r"최댓값 $6$, 최솟값 $2$"],
  check=_c)


def _c():
    sols = solve([y - lam*2*x, x - lam*8*y, x**2 + 4*y**2 - 2], [x, y, lam], dict=True)
    vals = sorted(set(simplify(x*y).subs(s_) for s_ in sols))
    assert vals == [R(-1, 2), R(1, 2)]
P(id="2-69", ch=14, sec="14.8", type="14-lagrange", src="과제 14.8 #29 유형",
  q=r"$f(x,y)=e^{xy}$의 영역 $x^2+4y^2\le2$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"$e^{t}$는 증가함수라 $xy$의 최대·최소를 찾으면 돼요. 내부 임계점 + 경계에서 라그랑주.",
  ans=r"최댓값 $e^{1/2}$ (점 $(1,\tfrac12),(-1,-\tfrac12)$),  최솟값 $e^{-1/2}$ (점 $(1,-\tfrac12),(-1,\tfrac12)$)",
  sol=[r"내부: $f_x=ye^{xy}=0,\ f_y=xe^{xy}=0$ → $(0,0)$, $f=1$",
       r"경계 $x^2+4y^2=2$에서 $xy$: $y=2\lambda x,\ x=8\lambda y$ → $y=16\lambda^2y$ → $\lambda=\pm\tfrac14$, $y=\pm\tfrac x2$",
       r"$x^2+x^2=2 \Rightarrow x=\pm1$ → $xy=\pm\tfrac12$",
       r"최댓값 $e^{1/2}$, 최솟값 $e^{-1/2}$ (내부의 $1$은 그 사이)"],
  check=_c)


def _c():
    sols = solve([y*z - lam*2*(y + z), x*z - lam*2*(x + z), x*y - lam*2*(x + y), 2*(x*y + y*z + z*x) - 24], [x, y, z, lam], dict=True)
    pos = [s_ for s_ in sols if all(s_[v].is_positive for v in (x, y, z))]
    assert pos and all((s_[x], s_[y], s_[z]) == (2, 2, 2) for s_ in pos)
P(id="2-70", ch=14, sec="14.8", type="14-lagrange", src="과제 14.8 #39 유형",
  q=r"겉넓이가 $24$인 (뚜껑 있는) 직육면체 상자 중 부피가 최대인 것의 치수와 최대 부피를 라그랑주 승수법으로 구하라.",
  hint=r"$V=xyz$, 제약 $2(xy+yz+zx)=24$. 식을 서로 빼서 $x=y=z$를 이끌어내요.",
  ans=r"$2\times2\times2$ 정육면체, 최대 부피 $8$",
  sol=[r"$yz=2\lambda(y+z),\ xz=2\lambda(x+z),\ xy=2\lambda(x+y)$",
       r"첫 식×$x$, 둘째 식×$y$: $xyz=2\lambda(xy+xz)=2\lambda(xy+yz) \Rightarrow xz=yz \Rightarrow x=y$",
       r"같은 방법으로 $y=z$ → $6x^2=24 \Rightarrow x=2$",
       r"최대 부피 $8$ (정육면체)"],
  check=_c)


def _c():
    sols = solve([y*z - lam, x*z - 2*lam, x*y - 3*lam, x + 2*y + 3*z - 6], [x, y, z, lam], dict=True)
    pos = [s_ for s_ in sols if all(s_[v].is_positive for v in (x, y, z))]
    assert len(pos) == 1 and (pos[0][x], pos[0][y], pos[0][z]) == (2, 1, R(2, 3))
    assert EQ((x*y*z).subs(pos[0]), R(4, 3))
P(id="2-71", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 유형 (변수 3개)",
  q=r"$x,y,z>0$이고 $x+2y+3z=6$일 때 $f(x,y,z)=xyz$의 최댓값을 구하라.",
  hint=r"$yz=\lambda,\ xz=2\lambda,\ xy=3\lambda$ → 비율로 $x=2y=3z$",
  ans=r"점 $\left(2,\ 1,\ \tfrac23\right)$에서 최댓값 $\dfrac43$",
  sol=[r"$\nabla f=\lambda\nabla g$: $yz=\lambda,\ xz=2\lambda,\ xy=3\lambda$",
       r"$\dfrac{xz}{yz}=2 \Rightarrow x=2y$,  $\dfrac{xy}{yz}=3 \Rightarrow x=3z$",
       r"$x+x+x=6 \Rightarrow x=2,\ y=1,\ z=\tfrac23$",
       r"최댓값 $2\cdot1\cdot\tfrac23=\dfrac43$ (경계에서는 $f\to0$이라 최대)"],
  check=_c)

"""1단계 · 기본 추가분 — Ch.14 편도함수: 1-35 ~ 1-71"""
from bank_lib import *

k = symbols('k', positive=True)


# ───────── 14.1 ─────────
def _c():
    f = sqrt(y - x**2)
    assert EQ(f.subs({x: 1, y: 1 + k**2}), k)
    assert EQ(f.subs({x: 0, y: 0}), 0)
P(id="1-35", ch=14, sec="14.1", type="14-domain", src="과제 14.1 #10 · #49 유형",
  q=r"$f(x,y)=\sqrt{y-x^2}$의 정의역과 치역을 구하고, 등위곡선 $f(x,y)=k\ (k\ge0)$이 어떤 곡선인지 말하라.",
  hint=r"근호 안이 $0$ 이상이어야 해요. $f=k$의 양변을 제곱해 보세요.",
  ans=r"정의역 $\{(x,y)\mid y\ge x^2\}$ (포물선과 그 위쪽),  치역 $[0,\infty)$,  등위곡선 $y=x^2+k^2$ (위로 $k^2$만큼 올린 포물선)",
  sol=[r"$y-x^2\ge0 \iff y\ge x^2$: 포물선 $y=x^2$ 위와 그 위쪽 영역",
       r"근호의 값은 $0$ 이상이고, $x=0$에서 $y$를 키우면 어떤 값이든 나오므로 치역은 $[0,\infty)$",
       r"$\sqrt{y-x^2}=k \iff y=x^2+k^2$: $k$가 커질수록 위로 올라가는 포물선들"],
  check=_c)


# ───────── 14.2 ─────────
def _c():
    g = (x**2 - 4*y**2) / (x - 2*y)
    assert simplify(g - (x + 2*y)) == 0 and EQ((x + 2*y).subs({x: 2, y: 1}), 4)
P(id="1-36", ch=14, sec="14.2", type="14-limit", src="과제 14.2 #8 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(2,1)}\frac{x^2-4y^2}{x-2y}$를 구하라.",
  hint=r"대입하면 $\tfrac00$ 꼴이에요. 분자를 인수분해해 약분해 보세요.",
  ans=r"$4$",
  sol=[r"대입하면 분자·분모 모두 $0$ → 인수분해: $x^2-4y^2=(x-2y)(x+2y)$",
       r"$x\ne2y$인 점에서 $\dfrac{x^2-4y^2}{x-2y}=x+2y$",
       r"$x+2y$는 연속이므로 $\displaystyle\lim_{(x,y)\to(2,1)}(x+2y)=2+2=4$"],
  check=_c)


def _c():
    f = x**2*y**2 / (x**2 + y**2)
    for th0 in (0, pi/6, pi/4, 1):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0) == 0
    assert simplify(y**2 - f - y**4/(x**2 + y**2)) == 0   # y^2 - f = y^4/(x^2+y^2) >= 0
P(id="1-37", ch=14, sec="14.2", type="14-limit", src="과제 14.2 #51 유형 (조임정리·극좌표)",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y^2}{x^2+y^2}$를 구하라.",
  hint=r"$\dfrac{x^2}{x^2+y^2}\le1$이에요. 또는 극좌표 $x=r\cos\theta,\ y=r\sin\theta$로 바꿔 보세요.",
  ans=r"$0$",
  sol=[r"$0\le\dfrac{x^2y^2}{x^2+y^2}=y^2\cdot\dfrac{x^2}{x^2+y^2}\le y^2$",
       r"$(x,y)\to(0,0)$이면 $y^2\to0$이므로 조임정리로 극한은 $0$",
       r"(극좌표: $\dfrac{r^4\cos^2\theta\sin^2\theta}{r^2}=r^2\cos^2\theta\sin^2\theta\le r^2\to0$)"],
  check=_c)


def _c():
    assert limit(sin(u) / u, u, 0) == 1
    f = sin(x**2 + y**2) / (x**2 + y**2)
    assert EQ(limit(f.subs({x: r*cos(1), y: r*sin(1)}), r, 0), 1)
P(id="1-38", ch=14, sec="14.2", type="14-limit", src="강의 14.2 (치환으로 한 변수 극한) 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{\sin(x^2+y^2)}{x^2+y^2}$를 구하라.",
  hint=r"$u=x^2+y^2$로 두면 $(x,y)\to(0,0)$일 때 $u\to0^+$예요.",
  ans=r"$1$",
  sol=[r"$u=x^2+y^2$로 두면 $(x,y)\to(0,0) \iff u\to0^+$",
       r"$\displaystyle\lim_{u\to0^+}\frac{\sin u}{u}=1$이므로 극한은 $1$"],
  check=_c)


def _c():
    f = (x**2 - y**2) / (x**2 + y**2)
    assert limit(f.subs(y, 0), x, 0) == 1 and limit(f.subs(x, 0), y, 0) == -1
P(id="1-39", ch=14, sec="14.2", type="14-dne", src="과제 14.2 #15 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2-y^2}{x^2+y^2}$가 존재하지 않음을 보여라.",
  hint=r"$x$축과 $y$축을 따라 각각 다가가 보세요.",
  ans=r"$x$축을 따라 $1$, $y$축을 따라 $-1$ → 극한은 존재하지 않는다.",
  sol=[r"$x$축 ($y=0$): $\dfrac{x^2}{x^2}=1 \to 1$",
       r"$y$축 ($x=0$): $\dfrac{-y^2}{y^2}=-1 \to -1$",
       r"두 경로의 극한값이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    f = x**2*y / (x**4 + y**2)
    assert limit(f.subs(y, 0), x, 0) == 0
    assert limit(f.subs(y, x**2), x, 0) == R(1, 2)
    m = symbols('m', real=True)
    assert limit(f.subs(y, m*x), x, 0) == 0
P(id="1-40", ch=14, sec="14.2", type="14-dne", src="복습 14.1–3 기초1 유형 (곡선 경로)",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^4+y^2}$가 존재하지 않음을 보여라.",
  hint=r"직선 $y=mx$로는 모두 $0$이 나와요. 분모의 $x^4$과 $y^2$의 차수가 같아지는 곡선 $y=x^2$을 써 보세요.",
  ans=r"직선 경로는 모두 $0$, 곡선 $y=x^2$을 따라 $\tfrac12$ → 극한은 존재하지 않는다.",
  sol=[r"$y=mx$: $\dfrac{mx^3}{x^4+m^2x^2}=\dfrac{mx}{x^2+m^2}\to0$ (모든 직선에서 $0$ → 판정 불가)",
       r"$y=x^2$: $\dfrac{x^4}{x^4+x^4}=\dfrac12\to\dfrac12$",
       r"경로에 따라 극한값이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    h = symbols('h', real=True)
    f = (x**3 - y**3) / (x**2 + y**2)
    assert limit(f.subs({x: h, y: 0}) / h, h, 0) == 1
    assert limit(f.subs({x: 0, y: h}) / h, h, 0) == -1
    for th0 in (0, pi/3, 2):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0) == 0
P(id="1-41", ch=14, sec="14.3", type="14-defpartial", src="2022 중간(블럭2) 2번 유형",
  q=r"$f(x,y)=\begin{cases}\dfrac{x^3-y^3}{x^2+y^2} & (x,y)\ne(0,0)\\ 0 & (x,y)=(0,0)\end{cases}$<br>(a) $f$가 원점에서 연속임을 보여라.  (b) 정의를 이용해 $f_x(0,0)$, $f_y(0,0)$을 구하라.",
  hint=r"(a) $\dfrac{|x|^3}{x^2+y^2}\le|x|$. (b) $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{f(h,0)-f(0,0)}{h}$",
  ans=r"(a) $\displaystyle\lim_{(x,y)\to(0,0)}f=0=f(0,0)$ → 연속  (b) $f_x(0,0)=1,\ f_y(0,0)=-1$",
  sol=[r"(a) $\dfrac{x^2}{x^2+y^2}\le1$이므로 $\left|\dfrac{x^3}{x^2+y^2}\right|\le|x|$, 같은 방법으로 $\left|\dfrac{y^3}{x^2+y^2}\right|\le|y|$",
       r"$|f(x,y)|\le|x|+|y|\to0$ → 조임정리로 $\displaystyle\lim_{(x,y)\to(0,0)}f(x,y)=0=f(0,0)$, 연속",
       r"(b) $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{h^3/h^2-0}{h}=\lim_{h\to0}1=1$",
       r"$f_y(0,0)=\displaystyle\lim_{h\to0}\frac{-h^3/h^2-0}{h}=-1$  (원점에서는 공식 대신 정의로!)"],
  check=_c)


# ───────── 14.3 ─────────
def _c():
    f = x**2*y + y*z**3 - exp(x*z)
    pt = {x: 0, y: 1, z: 2}
    assert [diff(f, v).subs(pt) for v in (x, y, z)] == [-2, 8, 12]
P(id="1-42", ch=14, sec="14.3", type="14-partial", src="과제 14.3 #29 유형",
  q=r"$f(x,y,z)=x^2y+yz^3-e^{xz}$일 때 $f_x,\ f_y,\ f_z$를 구하고 점 $(0,1,2)$에서의 값을 구하라.",
  hint=r"한 변수로 미분할 때 나머지 두 변수는 상수로 봐요. $e^{xz}$를 $x$로 미분하면 $ze^{xz}$예요.",
  ans=r"$f_x(0,1,2)=-2,\ f_y(0,1,2)=8,\ f_z(0,1,2)=12$",
  sol=[r"$f_x=2xy-ze^{xz}$ → $0-2=-2$",
       r"$f_y=x^2+z^3$ → $0+8=8$",
       r"$f_z=3yz^2-xe^{xz}$ → $12-0=12$"],
  check=_c)


def _c():
    f = x**y
    assert EQ(diff(f, x).subs({x: 2, y: 3}), 12) and EQ(diff(f, y).subs({x: 2, y: 3}), 8*log(2))
P(id="1-43", ch=14, sec="14.3", type="14-partial", src="과제 14.3 유형 (지수·거듭제곱 구분)",
  q=r"$f(x,y)=x^{y}\ (x>0)$일 때 $f_x(2,3)$, $f_y(2,3)$을 구하라.",
  hint=r"$y$가 상수면 $x^y$는 거듭제곱 함수, $x$가 상수면 지수함수예요.",
  ans=r"$f_x(2,3)=12,\ \ f_y(2,3)=8\ln2$",
  sol=[r"$f_x=y\,x^{y-1}$ (거듭제곱 미분) → $3\cdot2^2=12$",
       r"$f_y=x^{y}\ln x$ (지수함수 미분) → $2^3\ln2=8\ln2$"],
  check=_c)


def _c():
    F = x**2 + 2*y**2 + 3*z**2 - 6
    pt = {x: 1, y: 1, z: 1}
    assert F.subs(pt) == 0
    assert EQ((-diff(F, x) / diff(F, z)).subs(pt), R(-1, 3)) and EQ((-diff(F, y) / diff(F, z)).subs(pt), R(-2, 3))
P(id="1-44", ch=14, sec="14.3", type="14-implicit", src="강의 14.3 (음함수 편미분) 유형",
  q=r"방정식 $x^2+2y^2+3z^2=6$이 $z$를 $x,y$의 함수로 정할 때 점 $(1,1,1)$에서 $\dfrac{\partial z}{\partial x}$, $\dfrac{\partial z}{\partial y}$를 구하라.",
  hint=r"$F=x^2+2y^2+3z^2-6$이라 두면 $z_x=-\dfrac{F_x}{F_z},\ z_y=-\dfrac{F_y}{F_z}$",
  ans=r"$z_x=-\dfrac13,\ \ z_y=-\dfrac23$",
  sol=[r"$F_x=2x,\ F_y=4y,\ F_z=6z$ → 점 $(1,1,1)$에서 $2,\ 4,\ 6$",
       r"$z_x=-\dfrac{2}{6}=-\dfrac13$,  $z_y=-\dfrac{4}{6}=-\dfrac23$",
       r"(직접 미분: $2x+6z\,z_x=0 \Rightarrow z_x=-\dfrac{x}{3z}$과 같은 결과)"],
  check=_c)


def _c():
    f = x**3*y**2 + x*exp(y)
    assert simplify(diff(f, x, x) - 6*x*y**2) == 0
    assert simplify(diff(f, x, y) - (6*x**2*y + exp(y))) == 0 and simplify(diff(f, y, x) - diff(f, x, y)) == 0
    assert simplify(diff(f, y, y) - (2*x**3 + x*exp(y))) == 0
P(id="1-45", ch=14, sec="14.3", type="14-higher", src="강의 14.3 (Clairaut 정리) 유형",
  q=r"$f(x,y)=x^3y^2+xe^{y}$의 2계 편도함수 $f_{xx},\ f_{xy},\ f_{yx},\ f_{yy}$를 모두 구하고 $f_{xy}=f_{yx}$임을 확인하라.",
  hint=r"$f_{xy}=(f_x)_y$: 먼저 $x$로, 다음에 $y$로 미분해요.",
  ans=r"$f_{xx}=6xy^2,\ f_{xy}=f_{yx}=6x^2y+e^{y},\ f_{yy}=2x^3+xe^{y}$",
  sol=[r"$f_x=3x^2y^2+e^{y}$,  $f_y=2x^3y+xe^{y}$",
       r"$f_{xx}=6xy^2$,  $f_{xy}=(f_x)_y=6x^2y+e^{y}$",
       r"$f_{yx}=(f_y)_x=6x^2y+e^{y}$,  $f_{yy}=2x^3+xe^{y}$",
       r"$f_{xy}=f_{yx}$ ✓ (2계 편도함수가 연속이면 Clairaut 정리로 항상 같아요)"],
  check=_c)


# ───────── 14.4 ─────────
def _c():
    f = x**2 + 3*y**2
    L = f.subs({x: 1, y: 1}) + diff(f, x).subs({x: 1, y: 1})*(x - 1) + diff(f, y).subs({x: 1, y: 1})*(y - 1)
    assert simplify(L - (2*x + 6*y - 4)) == 0
P(id="1-46", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 #4 · 복습 14.4–6 기초3 유형",
  q=r"곡면 $z=x^2+3y^2$ 위의 점 $(1,1,4)$에서 접평면의 방정식을 구하라.",
  hint=r"$z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$",
  ans=r"$z=2x+6y-4$",
  sol=[r"$f_x=2x \Rightarrow f_x(1,1)=2$,  $f_y=6y \Rightarrow f_y(1,1)=6$",
       r"$z-4=2(x-1)+6(y-1)$",
       r"$z=2x+6y-4$"],
  check=_c)


def _c():
    f = x*exp(x*y)
    assert f.subs({x: 1, y: 0}) == 1
    assert diff(f, x).subs({x: 1, y: 0}) == 1 and diff(f, y).subs({x: 1, y: 0}) == 1
P(id="1-47", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 유형",
  q=r"곡면 $z=xe^{xy}$ 위의 점 $(1,0,1)$에서 접평면의 방정식을 구하라.",
  hint=r"$f_x$는 곱의 미분이에요: $(x)'e^{xy}+x\,(e^{xy})_x$",
  ans=r"$z=x+y$",
  sol=[r"$f_x=e^{xy}+xye^{xy} \Rightarrow f_x(1,0)=1$",
       r"$f_y=x^2e^{xy} \Rightarrow f_y(1,0)=1$",
       r"$z-1=1\cdot(x-1)+1\cdot(y-0) \Rightarrow z=x+y$"],
  check=_c)


def _c():
    f = sqrt(x**2 + y**2)
    L = 5 + R(3, 5)*(x - 3) + R(4, 5)*(y - 4)
    assert EQ(f.subs({x: 3, y: 4}), 5) and EQ(diff(f, x).subs({x: 3, y: 4}), R(3, 5)) and EQ(diff(f, y).subs({x: 3, y: 4}), R(4, 5))
    assert EQ(L.subs({x: R(303, 100), y: R(396, 100)}), R(4986, 1000))
    assert abs(N(f.subs({x: 3.03, y: 3.96})) - 4.986) < 1e-3
P(id="1-48", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 #17 유형 (선형근사)",
  q=r"$f(x,y)=\sqrt{x^2+y^2}$의 점 $(3,4)$에서의 선형화 $L(x,y)$를 구하고, 이를 이용해 $\sqrt{(3.03)^2+(3.96)^2}$의 근삿값을 구하라.",
  hint=r"$L(x,y)=f(3,4)+f_x(3,4)(x-3)+f_y(3,4)(y-4)$",
  ans=r"$L(x,y)=5+\tfrac35(x-3)+\tfrac45(y-4)$,  근삿값 $4.986$",
  sol=[r"$f(3,4)=5$,  $f_x=\dfrac{x}{\sqrt{x^2+y^2}}\Rightarrow\dfrac35$,  $f_y=\dfrac{y}{\sqrt{x^2+y^2}}\Rightarrow\dfrac45$",
       r"$L(x,y)=5+\tfrac35(x-3)+\tfrac45(y-4)$",
       r"$L(3.03,\,3.96)=5+\tfrac35(0.03)+\tfrac45(-0.04)=5+0.018-0.032=4.986$"],
  check=_c)


def _c():
    f = x**2*y**3
    dz = diff(f, x).subs({x: 2, y: 1})*R(1, 100) + diff(f, y).subs({x: 2, y: 1})*R(-2, 100)
    assert EQ(dz, R(-1, 5))
    dZ = f.subs({x: R(201, 100), y: R(98, 100)}) - 4
    assert abs(float(dZ) - (-0.1975)) < 1e-4
P(id="1-49", ch=14, sec="14.4", type="14-diff", src="과제 14.4 #39 유형",
  q=r"$z=x^2y^3$에서 $(x,y)$가 $(2,1)$에서 $(2.01,\ 0.98)$로 바뀔 때 전미분 $dz$를 구하고, 실제 변화량 $\Delta z$와 비교하라.",
  hint=r"$dz=z_x\,dx+z_y\,dy$, $dx=0.01,\ dy=-0.02$",
  ans=r"$dz=-0.2$,  $\Delta z\approx-0.1975$ (거의 같다)",
  sol=[r"$z_x=2xy^3=4$,  $z_y=3x^2y^2=12$ (점 $(2,1)$에서)",
       r"$dz=4(0.01)+12(-0.02)=0.04-0.24=-0.2$",
       r"$\Delta z=(2.01)^2(0.98)^3-4\approx3.8025-4=-0.1975$ → $dz$가 좋은 근사"],
  check=_c)


# ───────── 14.5 ─────────
def _c():
    zz = x**2*y - y**2
    sub = {x: t**2, y: 2*t}
    direct = diff(zz.subs(sub), t).subs(t, 1)
    chain = (diff(zz, x)*diff(t**2, t) + diff(zz, y)*diff(2*t, t)).subs(sub).subs(t, 1)
    assert direct == 2 and chain == 2
P(id="1-50", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #1 유형",
  q=r"$z=x^2y-y^2$, $x=t^2$, $y=2t$일 때 연쇄법칙으로 $t=1$에서의 $\dfrac{dz}{dt}$를 구하고, 직접 대입한 결과와 비교하라.",
  hint=r"$\dfrac{dz}{dt}=\dfrac{\partial z}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial z}{\partial y}\dfrac{dy}{dt}$",
  ans=r"$\dfrac{dz}{dt}\Big|_{t=1}=2$",
  sol=[r"$t=1$이면 $(x,y)=(1,2)$. $z_x=2xy=4$,  $z_y=x^2-2y=-3$",
       r"$\dfrac{dx}{dt}=2t=2$,  $\dfrac{dy}{dt}=2$",
       r"$\dfrac{dz}{dt}=4\cdot2+(-3)\cdot2=2$",
       r"직접: $z=2t^5-4t^2 \Rightarrow z'=10t^4-8t=2$ ✓"],
  check=_c)


def _c():
    w = x*y*z
    sub = {x: cos(t), y: sin(t), z: t}
    assert EQ(diff(w.subs(sub), t).subs(t, pi/4), R(1, 2))
P(id="1-51", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #4 유형",
  q=r"$w=xyz$, $x=\cos t$, $y=\sin t$, $z=t$일 때 $t=\dfrac{\pi}{4}$에서 $\dfrac{dw}{dt}$를 구하라.",
  hint=r"$\dfrac{dw}{dt}=w_x x'+w_y y'+w_z z'$",
  ans=r"$\dfrac12$",
  sol=[r"$\dfrac{dw}{dt}=yz(-\sin t)+xz(\cos t)+xy\cdot1=t(\cos^2t-\sin^2t)+\sin t\cos t$",
       r"$t=\dfrac\pi4$: $\cos^2t-\sin^2t=0$,  $\sin t\cos t=\dfrac12$",
       r"$\therefore\ \dfrac{dw}{dt}=\dfrac12$"],
  check=_c)


def _c():
    zz = x*log(y)
    sub = {x: s**2*t, y: s + t}
    Z = zz.subs(sub)
    assert EQ(diff(Z, s).subs({s: 1, t: 1}), 2*log(2) + R(1, 2))
    assert EQ(diff(Z, t).subs({s: 1, t: 1}), log(2) + R(1, 2))
P(id="1-52", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #14 유형",
  q=r"$z=x\ln y$, $x=s^2t$, $y=s+t$일 때 $(s,t)=(1,1)$에서 $\dfrac{\partial z}{\partial s}$, $\dfrac{\partial z}{\partial t}$를 구하라.",
  hint=r"$z_s=z_x x_s+z_y y_s$,  $z_t=z_x x_t+z_y y_t$",
  ans=r"$z_s=2\ln2+\dfrac12,\ \ z_t=\ln2+\dfrac12$",
  sol=[r"$(s,t)=(1,1)$이면 $(x,y)=(1,2)$.  $z_x=\ln y=\ln2$,  $z_y=\dfrac{x}{y}=\dfrac12$",
       r"$x_s=2st=2,\ x_t=s^2=1,\ y_s=1,\ y_t=1$",
       r"$z_s=\ln2\cdot2+\dfrac12\cdot1=2\ln2+\dfrac12$",
       r"$z_t=\ln2\cdot1+\dfrac12\cdot1=\ln2+\dfrac12$"],
  check=_c)


def _c():
    w = x**2*y + z
    W = w.subs({x: r + s, y: r*s, z: r - s})
    assert diff(W, r).subs({r: 1, s: 2}) == 31 and diff(W, s).subs({r: 1, s: 2}) == 20
P(id="1-53", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #27 유형",
  q=r"$w=x^2y+z$, $x=r+s$, $y=rs$, $z=r-s$일 때 $(r,s)=(1,2)$에서 $\dfrac{\partial w}{\partial r}$, $\dfrac{\partial w}{\partial s}$를 구하라.",
  hint=r"수형도: $w$ → $x,y,z$ → 각각 $r,s$. 경로 세 개의 곱을 더해요.",
  ans=r"$w_r=31,\ \ w_s=20$",
  sol=[r"$(r,s)=(1,2)$이면 $(x,y,z)=(3,2,-1)$.  $w_x=2xy=12,\ w_y=x^2=9,\ w_z=1$",
       r"$w_r=w_x\cdot1+w_y\cdot s+w_z\cdot1=12+18+1=31$",
       r"$w_s=w_x\cdot1+w_y\cdot r+w_z\cdot(-1)=12+9-1=20$"],
  check=_c)


def _c():
    F = x**3 + y**3 - 6*x*y
    assert F.subs({x: 3, y: 3}) == 0
    assert EQ((-diff(F, x) / diff(F, y)).subs({x: 3, y: 3}), -1)
P(id="1-54", ch=14, sec="14.5", type="14-implicit", src="강의 14.5 (음함수 미분 공식) 유형",
  q=r"곡선 $x^3+y^3=6xy$ 위의 점 $(3,3)$에서 $\dfrac{dy}{dx}$를 구하고 접선의 방정식을 구하라.",
  hint=r"$F(x,y)=x^3+y^3-6xy$라 두면 $\dfrac{dy}{dx}=-\dfrac{F_x}{F_y}$",
  ans=r"$\dfrac{dy}{dx}=-1$, 접선 $x+y=6$",
  sol=[r"$F_x=3x^2-6y=27-18=9$,  $F_y=3y^2-6x=27-18=9$",
       r"$\dfrac{dy}{dx}=-\dfrac{9}{9}=-1$",
       r"접선: $y-3=-(x-3) \Rightarrow x+y=6$"],
  check=_c)


def _c():
    f = x**3*y + exp(x)*cos(y)
    Z = f.subs({x: s + t, y: s - t}, simultaneous=True)
    fxx, fyy = diff(f, x, x), diff(f, y, y)
    assert simplify(diff(Z, s, t) - (fxx - fyy).subs({x: s + t, y: s - t}, simultaneous=True)) == 0
P(id="1-55", ch=14, sec="14.5", type="14-chain2", src="복습 14.4–6 기초1 유형 (2계 연쇄법칙 입문)",
  q=r"$z=f(x,y)$의 2계 편도함수가 연속이고 $x=s+t$, $y=s-t$일 때, $z_s,\ z_t$를 $f_x,\ f_y$로 나타내고 $z_{st}=f_{xx}-f_{yy}$임을 보여라.",
  hint=r"$z_{st}=(z_s)_t$. $f_x,\ f_y$도 $x,y$를 거쳐 $t$에 의존하므로 연쇄법칙을 한 번 더 써요.",
  ans=r"$z_s=f_x+f_y,\ \ z_t=f_x-f_y,\ \ z_{st}=f_{xx}-f_{yy}$",
  sol=[r"$x_s=1,\ y_s=1,\ x_t=1,\ y_t=-1$ → $z_s=f_x+f_y$,  $z_t=f_x-f_y$",
       r"$(f_x)_t=f_{xx}x_t+f_{xy}y_t=f_{xx}-f_{xy}$,  $(f_y)_t=f_{yx}-f_{yy}$",
       r"$z_{st}=(f_{xx}-f_{xy})+(f_{yx}-f_{yy})=f_{xx}-f_{yy}$  ($f_{xy}=f_{yx}$로 지워져요)"],
  check=_c)


# ───────── 14.6 ─────────
def _c():
    f = x**2*y - 3*y
    g = grad(f, (x, y)).subs({x: 2, y: 1})
    assert EQ(g, [4, 1]) and EQ(g.dot(Matrix([3, 4])) / 5, R(16, 5))
P(id="1-56", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #13 유형",
  q=r"$f(x,y)=x^2y-3y$의 점 $(2,1)$에서 벡터 $\mathbf v=\langle3,4\rangle$ 방향으로의 방향도함수를 구하라.",
  hint=r"$D_{\mathbf u}f=\nabla f\cdot\mathbf u$, $\mathbf u$는 단위벡터여야 해요.",
  ans=r"$\dfrac{16}{5}$",
  sol=[r"$\nabla f=\langle 2xy,\ x^2-3\rangle \Rightarrow \nabla f(2,1)=\langle4,1\rangle$",
       r"$\mathbf u=\dfrac{\mathbf v}{|\mathbf v|}=\left\langle\tfrac35,\tfrac45\right\rangle$",
       r"$D_{\mathbf u}f(2,1)=4\cdot\tfrac35+1\cdot\tfrac45=\dfrac{16}{5}$"],
  check=_c)


def _c():
    f = x**2*y + y*z**3
    g = grad(f, (x, y, z)).subs({x: 1, y: 1, z: 1})
    d = Matrix([1, 2, 2])
    assert EQ(g, [2, 2, 3]) and EQ(g.dot(d) / d.norm(), 4)
P(id="1-57", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #23 유형",
  q=r"$f(x,y,z)=x^2y+yz^3$의 점 $P(1,1,1)$에서 점 $Q(2,3,3)$을 향하는 방향으로의 방향도함수를 구하라.",
  hint=r"방향은 $\overrightarrow{PQ}$를 단위벡터로 만든 것이에요.",
  ans=r"$4$",
  sol=[r"$\nabla f=\langle 2xy,\ x^2+z^3,\ 3yz^2\rangle \Rightarrow \nabla f(1,1,1)=\langle2,2,3\rangle$",
       r"$\overrightarrow{PQ}=\langle1,2,2\rangle$, $|\overrightarrow{PQ}|=3$ → $\mathbf u=\tfrac13\langle1,2,2\rangle$",
       r"$D_{\mathbf u}f(P)=\dfrac{2+4+6}{3}=4$"],
  check=_c)


def _c():
    f = x*exp(y)
    g = grad(f, (x, y)).subs({x: 2, y: 0})
    assert EQ(g, [1, 2]) and EQ(g.norm(), sqrt(5))
P(id="1-58", ch=14, sec="14.6", type="14-maxrate", src="과제 14.6 #27 · #29 유형",
  q=r"$f(x,y)=xe^{y}$의 점 $(2,0)$에서 최대 변화율과 그 방향, 최소 변화율과 그 방향을 구하라.",
  hint=r"최대 변화율 $|\nabla f|$는 $\nabla f$ 방향, 최소는 $-|\nabla f|$이고 $-\nabla f$ 방향이에요.",
  ans=r"최대 $\sqrt5$ (방향 $\tfrac{1}{\sqrt5}\langle1,2\rangle$),  최소 $-\sqrt5$ (방향 $-\tfrac{1}{\sqrt5}\langle1,2\rangle$)",
  sol=[r"$\nabla f=\langle e^{y},\ xe^{y}\rangle \Rightarrow \nabla f(2,0)=\langle1,2\rangle$",
       r"최대 변화율 $|\nabla f(2,0)|=\sqrt5$, 방향 $\dfrac{\langle1,2\rangle}{\sqrt5}$",
       r"최소 변화율 $-\sqrt5$, 방향 $-\dfrac{\langle1,2\rangle}{\sqrt5}$"],
  check=_c)


def _c():
    T = 100 - x**2 - 2*y**2 - z**2
    g = grad(T, (x, y, z)).subs({x: 1, y: 1, z: 1})
    assert EQ(g, [-2, -4, -2]) and EQ(g.norm(), 2*sqrt(6))
    assert EQ(g / g.norm(), [-1/sqrt(6), -2/sqrt(6), -1/sqrt(6)])
P(id="1-59", ch=14, sec="14.6", type="14-maxrate", src="복습 14.4–6 기초2 유형",
  q=r"공간의 온도가 $T(x,y,z)=100-x^2-2y^2-z^2$일 때, 점 $(1,1,1)$에서 온도가 가장 빠르게 올라가는 방향(단위벡터)과 그 최대 증가율을 구하라.",
  hint=r"가장 빠르게 증가하는 방향은 $\nabla T$ 방향, 증가율은 $|\nabla T|$예요.",
  ans=r"방향 $\tfrac{1}{\sqrt6}\langle-1,-2,-1\rangle$,  최대 증가율 $2\sqrt6$",
  sol=[r"$\nabla T=\langle-2x,\ -4y,\ -2z\rangle \Rightarrow \nabla T(1,1,1)=\langle-2,-4,-2\rangle$",
       r"$|\nabla T|=\sqrt{4+16+4}=\sqrt{24}=2\sqrt6$",
       r"방향: $\dfrac{\langle-2,-4,-2\rangle}{2\sqrt6}=\dfrac{1}{\sqrt6}\langle-1,-2,-1\rangle$ (원점 쪽으로 갈수록 따뜻해져요)"],
  check=_c)


def _c():
    F = x**2 + y**2 + z**2
    g = grad(F, (x, y, z)).subs({x: 1, y: 2, z: 2})
    assert EQ(g, [2, 4, 4]) and 1 + 2*2 + 2*2 == 9
P(id="1-60", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 (등위곡면의 접평면) 유형",
  q=r"구면 $x^2+y^2+z^2=9$ 위의 점 $(1,2,2)$에서 접평면과 법선의 방정식을 구하라.",
  hint=r"$F=x^2+y^2+z^2$의 기울기 $\nabla F$가 법선벡터예요.",
  ans=r"접평면 $x+2y+2z=9$,  법선 $x=1+t,\ y=2+2t,\ z=2+2t$",
  sol=[r"$\nabla F=\langle2x,2y,2z\rangle \Rightarrow \nabla F(1,2,2)=\langle2,4,4\rangle\parallel\langle1,2,2\rangle$",
       r"접평면: $(x-1)+2(y-2)+2(z-2)=0 \Rightarrow x+2y+2z=9$",
       r"법선: $x=1+t,\ y=2+2t,\ z=2+2t$ (구의 중심 $t=-1$을 지나요)"],
  check=_c)


def _c():
    F = x*y + y*z + z*x
    pt = {x: 1, y: 2, z: 3}
    assert F.subs(pt) == 11
    g = grad(F, (x, y, z)).subs(pt)
    assert EQ(g, [5, 4, 3]) and 5 + 8 + 9 == 22
P(id="1-61", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 (등위곡면의 접평면) 유형",
  q=r"곡면 $xy+yz+zx=11$ 위의 점 $(1,2,3)$에서 접평면과 법선의 방정식을 구하라.",
  hint=r"$\nabla F=\langle y+z,\ x+z,\ x+y\rangle$",
  ans=r"접평면 $5x+4y+3z=22$,  법선 $\dfrac{x-1}{5}=\dfrac{y-2}{4}=\dfrac{z-3}{3}$",
  sol=[r"$\nabla F(1,2,3)=\langle 2+3,\ 1+3,\ 1+2\rangle=\langle5,4,3\rangle$",
       r"접평면: $5(x-1)+4(y-2)+3(z-3)=0 \Rightarrow 5x+4y+3z=22$",
       r"법선: $\dfrac{x-1}{5}=\dfrac{y-2}{4}=\dfrac{z-3}{3}$"],
  check=_c)


# ───────── 14.7 ─────────
def _c():
    f = x**2 + x*y + y**2 - 3*x
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: 2, y: -1}
    assert diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2 == 3 and f.subs({x: 2, y: -1}) == -3
P(id="1-62", ch=14, sec="14.7", type="14-crit", src="강의 14.7 (2계 판정법) 유형",
  q=r"$f(x,y)=x^2+xy+y^2-3x$의 임계점을 구하고 2계 판정법으로 분류하라.",
  hint=r"$f_x=f_y=0$을 풀고 $D=f_{xx}f_{yy}-f_{xy}^2$의 부호를 봐요.",
  ans=r"임계점 $(2,-1)$에서 극솟값 $-3$",
  sol=[r"$f_x=2x+y-3=0$,  $f_y=x+2y=0$ → $x=2,\ y=-1$",
       r"$f_{xx}=2,\ f_{yy}=2,\ f_{xy}=1$ → $D=4-1=3>0$, $f_{xx}>0$",
       r"극솟값 $f(2,-1)=4-2+1-6=-3$"],
  check=_c)


def _c():
    f = x**3 - 3*x + y**2 - 2*y
    sols = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    assert sorted((s_[x], s_[y]) for s_ in sols) == [(-1, 1), (1, 1)]
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert D.subs({x: 1, y: 1}) == 12 and D.subs({x: -1, y: 1}) == -12 and f.subs({x: 1, y: 1}) == -3
P(id="1-63", ch=14, sec="14.7", type="14-crit", src="2025 중간 2(a) 유형 (기초형)",
  q=r"$f(x,y)=x^3-3x+y^2-2y$의 극댓값, 극솟값, 안장점을 구하라.",
  hint=r"$f_x=3x^2-3$, $f_y=2y-2$. 임계점마다 $D$를 계산해요.",
  ans=r"$(1,1)$에서 극솟값 $-3$,  $(-1,1)$은 안장점 (극댓값 없음)",
  sol=[r"$f_x=3x^2-3=0 \Rightarrow x=\pm1$,  $f_y=2y-2=0 \Rightarrow y=1$ → 임계점 $(1,1),\ (-1,1)$",
       r"$f_{xx}=6x,\ f_{yy}=2,\ f_{xy}=0$ → $D=12x$",
       r"$(1,1)$: $D=12>0,\ f_{xx}=6>0$ → 극솟값 $f(1,1)=1-3+1-2=-3$",
       r"$(-1,1)$: $D=-12<0$ → 안장점"],
  check=_c)


def _c():
    f = x**4 + y**4 - 16*x*y
    sols = [s_ for s_ in solve([diff(f, x), diff(f, y)], [x, y], dict=True) if s_[x].is_real and s_[y].is_real]
    assert sorted((s_[x], s_[y]) for s_ in sols) == [(-2, -2), (0, 0), (2, 2)]
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert D.subs({x: 0, y: 0}) == -256 and D.subs({x: 2, y: 2}) == 2048 and f.subs({x: 2, y: 2}) == -32
P(id="1-64", ch=14, sec="14.7", type="14-crit", src="강의 14.7 ($x^4+y^4-4xy$ 예제) 유형",
  q=r"$f(x,y)=x^4+y^4-16xy$의 임계점을 모두 구하고 분류하라.",
  hint=r"$f_x=0$에서 $y=\tfrac{x^3}{4}$을 $f_y=0$에 대입해요.",
  ans=r"$(0,0)$ 안장점,  $(2,2)$와 $(-2,-2)$에서 극솟값 $-32$",
  sol=[r"$f_x=4x^3-16y=0 \Rightarrow y=\dfrac{x^3}{4}$,  $f_y=4y^3-16x=0 \Rightarrow y^3=4x$",
       r"$\dfrac{x^9}{64}=4x \Rightarrow x(x^8-256)=0 \Rightarrow x=0,\ \pm2$ → $(0,0),\ (2,2),\ (-2,-2)$",
       r"$f_{xx}=12x^2,\ f_{yy}=12y^2,\ f_{xy}=-16$. $(0,0)$: $D=-256<0$ → 안장점",
       r"$(\pm2,\pm2)$: $D=48\cdot48-256=2048>0,\ f_{xx}>0$ → 극솟값 $16+16-64=-32$"],
  check=_c)


def _c():
    f = x**2 + y**2 - 2*x - 4*y
    cands = [(1, 2), (0, 0), (3, 0), (0, 3), (3, 3), (1, 0), (0, 2), (1, 3), (3, 2)]
    vals = {c: f.subs({x: c[0], y: c[1]}) for c in cands}
    assert max(vals.values()) == 3 and vals[(3, 0)] == 3 and min(vals.values()) == -5 and vals[(1, 2)] == -5
P(id="1-65", ch=14, sec="14.7", type="14-absext", src="과제 14.7 #35 · 복습 14.7–8 심화1 유형",
  q=r"$f(x,y)=x^2+y^2-2x-4y$의 정사각형 $D=\{(x,y)\mid 0\le x\le3,\ 0\le y\le3\}$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"① 내부 임계점 ② 네 변 위에서 한 변수 함수로 최대·최소 ③ 꼭짓점 — 후보를 모두 비교해요.",
  ans=r"최댓값 $3$ (점 $(3,0)$),  최솟값 $-5$ (점 $(1,2)$)",
  sol=[r"내부: $f_x=2x-2=0,\ f_y=2y-4=0$ → $(1,2)$, $f=-5$",
       r"변 $y=0$: $x^2-2x$ → $x=1$에서 $-1$.  변 $x=0$: $y^2-4y$ → $y=2$에서 $-4$",
       r"변 $y=3$: $x^2-2x-3$ → $x=1$에서 $-4$.  변 $x=3$: $y^2-4y+3$ → $y=2$에서 $-1$",
       r"꼭짓점: $f(0,0)=0,\ f(3,0)=3,\ f(0,3)=-3,\ f(3,3)=0$",
       r"비교하면 최댓값 $3$ (점 $(3,0)$), 최솟값 $-5$ (점 $(1,2)$)"],
  check=_c)


def _c():
    f = x*y
    ft = f.subs({x: sqrt(2)*cos(t), y: sqrt(2)*sin(t)})
    assert simplify(ft - sin(2*t)) == 0
    assert f.subs({x: 1, y: 1}) == 1 and f.subs({x: 1, y: -1}) == -1 and 1**2 + 1**2 == 2
P(id="1-66", ch=14, sec="14.7", type="14-absext", src="복습 14.7–8 기초4 유형",
  q=r"$f(x,y)=xy$의 닫힌 원판 $x^2+y^2\le2$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"경계는 $x=\sqrt2\cos t,\ y=\sqrt2\sin t$로 매개화하면 $f=\sin2t$가 돼요.",
  ans=r"최댓값 $1$ (점 $(1,1),(-1,-1)$),  최솟값 $-1$ (점 $(1,-1),(-1,1)$)",
  sol=[r"내부: $f_x=y=0,\ f_y=x=0$ → $(0,0)$, $f=0$",
       r"경계: $f=2\sin t\cos t=\sin2t$ → 최대 $1$ ($t=\tfrac\pi4,\tfrac{5\pi}{4}$), 최소 $-1$ ($t=\tfrac{3\pi}{4},\tfrac{7\pi}{4}$)",
       r"$t=\tfrac\pi4$ → $(1,1)$ 등. 비교하면 최댓값 $1$, 최솟값 $-1$"],
  check=_c)


def _c():
    Pf = x*y*(12 - x - y)
    sols = [s_ for s_ in solve([diff(Pf, x), diff(Pf, y)], [x, y], dict=True) if s_[x] > 0 and s_[y] > 0]
    assert sols == [{x: 4, y: 4}] and Pf.subs({x: 4, y: 4}) == 64
    D = diff(Pf, x, 2)*diff(Pf, y, 2) - diff(Pf, x, y)**2
    assert D.subs({x: 4, y: 4}) > 0 and diff(Pf, x, 2).subs({x: 4, y: 4}) < 0
P(id="1-67", ch=14, sec="14.7", type="14-optim", src="강의 14.7 (최적화 응용) 유형",
  q=r"합이 $12$인 세 양수 중에서 곱이 최대가 되는 세 수와 그 최댓값을 구하라.",
  hint=r"세 수를 $x,\ y,\ 12-x-y$로 두고 $P=xy(12-x-y)$의 임계점을 구해요.",
  ans=r"$4,\ 4,\ 4$일 때 최댓값 $64$",
  sol=[r"$P=12xy-x^2y-xy^2$",
       r"$P_x=y(12-2x-y)=0,\ P_y=x(12-x-2y)=0$ ($x,y>0$) → $2x+y=12,\ x+2y=12$ → $x=y=4$",
       r"$P_{xx}=-2y=-8,\ P_{yy}=-8,\ P_{xy}=12-2x-2y=-4$ → $D=64-16>0$, 극대",
       r"세 수 $4,4,4$, 최댓값 $64$"],
  check=_c)


# ───────── 14.8 ─────────
lam = symbols('lambda', real=True)


def _c():
    f = x + 2*y
    sols = solve([1 - lam*2*x, 2 - lam*2*y, x**2 + y**2 - 5], [x, y, lam], dict=True)
    vals = sorted(f.subs(s_) for s_ in sols)
    assert vals == [-5, 5]
P(id="1-68", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 (라그랑주 승수법) 유형",
  q=r"원 $x^2+y^2=5$ 위에서 $f(x,y)=x+2y$의 최댓값과 최솟값을 라그랑주 승수법으로 구하라.",
  hint=r"$\nabla f=\lambda\nabla g$: $\langle1,2\rangle=\lambda\langle2x,2y\rangle$",
  ans=r"최댓값 $5$ (점 $(1,2)$),  최솟값 $-5$ (점 $(-1,-2)$)",
  sol=[r"$1=2\lambda x,\ 2=2\lambda y$ → $y=2x$",
       r"제약식: $x^2+4x^2=5 \Rightarrow x=\pm1$ → $(1,2),\ (-1,-2)$",
       r"$f(1,2)=5$, $f(-1,-2)=-5$ → 최댓값 $5$, 최솟값 $-5$"],
  check=_c)


def _c():
    f = x**2*y
    sols = solve([2*x*y - lam*2*x, x**2 - lam*4*y, x**2 + 2*y**2 - 6], [x, y, lam], dict=True)
    vals = sorted(set(f.subs(s_) for s_ in sols))
    assert vals == [-4, 0, 4]
P(id="1-69", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 유형",
  q=r"타원 $x^2+2y^2=6$ 위에서 $f(x,y)=x^2y$의 최댓값과 최솟값을 구하라.",
  hint=r"$2xy=2\lambda x$에서 $x=0$인 경우와 $y=\lambda$인 경우로 나눠요.",
  ans=r"최댓값 $4$ (점 $(\pm2,1)$),  최솟값 $-4$ (점 $(\pm2,-1)$)",
  sol=[r"$\nabla f=\langle 2xy,\ x^2\rangle,\ \nabla g=\langle 2x,\ 4y\rangle$: $2xy=2\lambda x,\ x^2=4\lambda y$",
       r"$x=0$: $y=\pm\sqrt3$, $f=0$",
       r"$x\ne0$: $\lambda=y$ → $x^2=4y^2$ → $4y^2+2y^2=6 \Rightarrow y=\pm1,\ x=\pm2$",
       r"$f(\pm2,1)=4$, $f(\pm2,-1)=-4$ → 최댓값 $4$, 최솟값 $-4$"],
  check=_c)


def _c():
    f = x**2 + y**2
    sols = solve([2*x - lam*y, 2*y - lam*x, x*y - 4], [x, y, lam], dict=True)
    vals = sorted(set(f.subs(s_) for s_ in sols if s_[x].is_real))
    assert vals == [8]
P(id="1-70", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 유형 (최솟값만 존재)",
  q=r"쌍곡선 $xy=4$ 위에서 $f(x,y)=x^2+y^2$의 최솟값을 구하라. (원점에서 가장 가까운 점)",
  hint=r"$2x=\lambda y,\ 2y=\lambda x$에서 $x^2=y^2$이 나와요.",
  ans=r"최솟값 $8$ (점 $(2,2),\ (-2,-2)$)",
  sol=[r"$\langle2x,2y\rangle=\lambda\langle y,x\rangle$ → $2x\cdot x=\lambda xy=2y\cdot y$ → $x^2=y^2$",
       r"$xy=4>0$이라 $x=y$ → $x^2=4 \Rightarrow (2,2),\ (-2,-2)$",
       r"$f=8$. 곡선이 무한히 뻗어 있어 최댓값은 없고, 최솟값은 $8$ (거리로는 $2\sqrt2$)"],
  check=_c)


def _c():
    f = x + y + z
    sols = solve([1 - 2*lam*x, 1 - 2*lam*y, 1 - 2*lam*z, x**2 + y**2 + z**2 - 12], [x, y, z, lam], dict=True)
    vals = sorted(f.subs(s_) for s_ in sols)
    assert vals == [-6, 6]
P(id="1-71", ch=14, sec="14.8", type="14-lagrange", src="과제 14.8 #12 유형",
  q=r"구면 $x^2+y^2+z^2=12$ 위에서 $f(x,y,z)=x+y+z$의 최댓값과 최솟값을 구하라.",
  hint=r"$\langle1,1,1\rangle=\lambda\langle2x,2y,2z\rangle$이면 $x=y=z$예요.",
  ans=r"최댓값 $6$ (점 $(2,2,2)$),  최솟값 $-6$ (점 $(-2,-2,-2)$)",
  sol=[r"$1=2\lambda x=2\lambda y=2\lambda z$ → $x=y=z$",
       r"$3x^2=12 \Rightarrow x=\pm2$ → $(2,2,2),\ (-2,-2,-2)$",
       r"최댓값 $6$, 최솟값 $-6$"],
  check=_c)

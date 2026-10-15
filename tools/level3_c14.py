"""3단계 · 응용 추가분 — Ch.14 편도함수: 3-35 ~ 3-71"""
from bank_lib import *

lam, mu = symbols('lambda mu', real=True)
k = symbols('k', real=True)


def path_lim(f, sub, var):
    return limit(simplify(f.subs(sub)), var, 0)


# ───────── 14.1 ─────────
def _c():
    w = x**2 + y**2 - z**2
    assert w.subs({x: 1, y: 0, z: 0}) == 1 and w.subs({x: 0, y: 0, z: 1}) == -1 and w.subs({x: 1, y: 0, z: 1}) == 0
P(id="3-35", ch=14, sec="14.1", type="14-domain", src="강의 14.1 (등위곡면) 유형",
  q=r"(a) $w=x^2+y^2-z^2$의 등위곡면 $w=k$가 $k>0$, $k=0$, $k<0$일 때 각각 어떤 곡면인지 말하라.<br>(b) $g(x,y,z)=\ln(1-x^2-y^2+z^2)$의 정의역을 (a)의 곡면으로 설명하라.",
  hint=r"$x^2+y^2=k+z^2$: $z$를 고정한 단면은 원이에요. $k$의 부호에 따라 $z=0$ 단면이 원·점·없음",
  ans=r"(a) $k>0$: 한 장 쌍곡면, $k=0$: 원뿔, $k<0$: 두 장 쌍곡면  (b) $x^2+y^2-z^2<1$: 한 장 쌍곡면 $x^2+y^2-z^2=1$의 안쪽($z$축을 포함하는 쪽), 경계 제외",
  sol=[r"(a) $z=c$ 단면: $x^2+y^2=k+c^2$ (원). $k>0$이면 모든 높이에서 원 → 한 장 쌍곡면",
       r"$k=0$: $x^2+y^2=z^2$ → 원뿔.  $k<0$: $|z|\ge\sqrt{-k}$에서만 단면이 있음 → 두 장 쌍곡면",
       r"(b) $1-x^2-y^2+z^2>0 \iff x^2+y^2-z^2<1$ → $w=1$인 한 장 쌍곡면의 안쪽 (예: $z$축 위의 점은 모두 포함)"],
  check=_c)


# ───────── 14.2 ─────────
def _c():
    f = x**2*sin(2*y)**2 / (x**2 + y**2)**R(3, 2)
    for th0 in (R(1, 3), 1, 2):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0, '+') == 0
    assert simplify((x**2 + y**2)**2 - 4*x**2*y**2 - (x**2 - y**2)**2) == 0
P(id="3-36", ch=14, sec="14.2", type="14-limit", src="2025 중간 3(a) · 2024 중간 3(a) 유형 (조임정리)",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2\sin^2(2y)}{(x^2+y^2)^{3/2}}$를 구하라.",
  hint=r"$|\sin2y|\le2|y|$, $x^2y^2\le\dfrac{(x^2+y^2)^2}{4}$",
  ans=r"$0$",
  sol=[r"$0\le\dfrac{x^2\sin^2(2y)}{(x^2+y^2)^{3/2}}\le\dfrac{4x^2y^2}{(x^2+y^2)^{3/2}}$",
       r"$(x^2+y^2)^2-4x^2y^2=(x^2-y^2)^2\ge0$이므로 $4x^2y^2\le(x^2+y^2)^2$",
       r"$\le\dfrac{(x^2+y^2)^2}{(x^2+y^2)^{3/2}}=\sqrt{x^2+y^2}\to0$ → 조임정리로 극한 $0$"],
  check=_c)


def _c():
    num = sin(x*y**2)*cos(2*y**2) - cos(x*y**2)*sin(2*y**2)
    assert simplify(num - sin((x - 2)*y**2)) == 0
    g = sin((x - 2)*y**2) / ((x - 2)**2 + y**4)
    assert simplify(path_lim(g, {x: 2 + k*y**2}, y) - k/(k**2 + 1)) == 0
    assert path_lim(g, {x: 2}, y) == 0
P(id="3-37", ch=14, sec="14.2", type="14-dne", src="2025 중간 3(b) 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(2,0)}\frac{\sin(xy^2)\cos(2y^2)-\cos(xy^2)\sin(2y^2)}{(x-2)^2+y^4}$가 존재하는지 판정하라.",
  hint=r"분자는 사인의 차 공식 $\sin A\cos B-\cos A\sin B=\sin(A-B)$. 그다음 $x-2=ky^2$ 경로",
  ans=r"존재하지 않는다 (곡선 $x-2=ky^2$을 따라 $\dfrac{k}{k^2+1}$)",
  sol=[r"분자 $=\sin(xy^2-2y^2)=\sin\big((x-2)y^2\big)$",
       r"$X=x-2$로 두면 $\displaystyle\lim_{(X,y)\to(0,0)}\frac{\sin(Xy^2)}{X^2+y^4}$",
       r"$X=ky^2$: $\dfrac{\sin(ky^4)}{(k^2+1)y^4}=\dfrac{\sin(ky^4)}{ky^4}\cdot\dfrac{k}{k^2+1}\to\dfrac{k}{k^2+1}$ ($k\ne0$), $X=0$이면 $0$",
       r"$k=1$이면 $\tfrac12$, $k=0$이면 $0$ → 극한은 존재하지 않는다."],
  check=_c)


def _c():
    f = (exp(x) - 1)*(exp(y) - 1) / (x**2 + y**2)
    assert path_lim(f, {y: 0}, x) == 0 and path_lim(f, {y: x}, x) == R(1, 2)
P(id="3-38", ch=14, sec="14.2", type="14-dne", src="2022 중간(블럭1) 1(a) 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{(e^{x}-1)(e^{y}-1)}{x^2+y^2}$가 존재하는지 판정하라.",
  hint=r"$e^{x}-1\approx x$ (즉 $\lim\frac{e^x-1}{x}=1$). $x$축과 $y=x$를 비교해 보세요.",
  ans=r"존재하지 않는다 ($x$축: $0$, $y=x$: $\tfrac12$)",
  sol=[r"$x$축 ($y=0$): 분자 $=0$ → $0$",
       r"$y=x$: $\dfrac{(e^x-1)^2}{2x^2}=\dfrac12\Big(\dfrac{e^x-1}{x}\Big)^2\to\dfrac12$",
       r"경로에 따라 값이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    f = (x**2*y + y**2*z + z**2*x) / (x**2 + y**2 + z**2)
    for (a, b, c_) in ((1, 2, 3), (1, -1, 0), (2, 1, -1)):
        assert limit(f.subs({x: a*t, y: b*t, z: c_*t}), t, 0) == 0
P(id="3-39", ch=14, sec="14.2", type="14-limit", src="2022 중간(블럭1) 1(b) 유형 (변수 3개)",
  q=r"$\displaystyle\lim_{(x,y,z)\to(0,0,0)}\frac{x^2y+y^2z+z^2x}{x^2+y^2+z^2}$를 구하라.",
  hint=r"$\rho=\sqrt{x^2+y^2+z^2}$로 두면 $|x|,|y|,|z|\le\rho$",
  ans=r"$0$",
  sol=[r"$|x^2y|\le\rho^2\cdot\rho=\rho^3$, 같은 방법으로 $|y^2z|,\ |z^2x|\le\rho^3$",
       r"$\left|\dfrac{x^2y+y^2z+z^2x}{x^2+y^2+z^2}\right|\le\dfrac{3\rho^3}{\rho^2}=3\rho\to0$",
       r"조임정리로 극한은 $0$"],
  check=_c)


def _c():
    f = x**2*y**2/(x**2 + y**2)*log(x**2 + y**2)
    for th0 in (R(1, 2), 1):
        assert limit(f.subs({x: r*cos(th0), y: r*sin(th0)}), r, 0, '+') == 0
    assert limit(r**2*log(r), r, 0, '+') == 0
P(id="3-40", ch=14, sec="14.2", type="14-limit", src="2022 중간(블럭2) 1(b) 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y^2}{x^2+y^2}\ln(x^2+y^2)$를 구하라.",
  hint=r"극좌표: $r^2\cos^2\theta\sin^2\theta\cdot2\ln r$. 한 변수 극한 $\lim_{r\to0^+}r^2\ln r=0$ (로피탈)",
  ans=r"$0$",
  sol=[r"극좌표: $\dfrac{r^4\cos^2\theta\sin^2\theta}{r^2}\ln r^2=2r^2\ln r\cdot\cos^2\theta\sin^2\theta$",
       r"$|\cdot|\le2r^2|\ln r|$,  $\displaystyle\lim_{r\to0^+}r^2\ln r=\lim\frac{\ln r}{r^{-2}}=\lim\frac{1/r}{-2r^{-3}}=\lim\Big(-\frac{r^2}{2}\Big)=0$",
       r"조임정리로 극한은 $0$"],
  check=_c)


def _c():
    h = symbols('h', real=True)
    f = (2*x**3 - y**5) / (x**2 + y**4)
    assert limit(f.subs({x: h, y: 0})/h, h, 0) == 2 and limit(f.subs({x: 0, y: h})/h, h, 0) == -1
    assert simplify(diff(f, x).subs(y, 0) - 2) == 0
    for (a, b) in ((1, 1), (1, 2), (-1, 3)):
        assert limit(f.subs({x: a*t, y: b*t}), t, 0) == 0 and limit(f.subs({x: a*t**2, y: b*t}), t, 0) == 0
P(id="3-41", ch=14, sec="14.3", type="14-defpartial", src="2022 중간(블럭2) 2번 유형",
  q=r"$f(x,y)=\dfrac{2x^3-y^5}{x^2+y^4}\ \big((x,y)\ne(0,0)\big)$, $f(0,0)=0$일 때<br>(a) $f$가 원점에서 연속임을 보여라.  (b) $f_x(0,0)$, $f_y(0,0)$을 구하라.  (c) $f_{xx}(0,0)$을 구하라.",
  hint=r"(a) $\dfrac{x^2}{x^2+y^4}\le1$, $\dfrac{y^4}{x^2+y^4}\le1$. (c) $x$축 위에서 $f(x,0)=2x$이므로 $f_x(x,0)$부터 구해요.",
  ans=r"(a) $|f|\le2|x|+|y|\to0$  (b) $f_x(0,0)=2,\ f_y(0,0)=-1$  (c) $f_{xx}(0,0)=0$",
  sol=[r"(a) $\left|\dfrac{2x^3}{x^2+y^4}\right|\le2|x|$,  $\left|\dfrac{y^5}{x^2+y^4}\right|\le|y|$ → $|f|\le2|x|+|y|\to0=f(0,0)$",
       r"(b) $f(h,0)=2h$ → $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{2h}{h}=2$.  $f(0,h)=-h$ → $f_y(0,0)=-1$",
       r"(c) $x$축 위에서 $f(x,0)=2x$ (원점 포함)이므로 모든 $a$에서 $f_x(a,0)=2$",
       r"$f_{xx}(0,0)=\displaystyle\lim_{h\to0}\frac{f_x(h,0)-f_x(0,0)}{h}=\lim\frac{2-2}{h}=0$"],
  check=_c)


# ───────── 14.3 ─────────
def _c():
    F = x*z**2 + y*exp(x - y*z) - 2
    pt = {x: 1, y: 1, z: 1}
    assert F.subs(pt) == 0
    assert [diff(F, v).subs(pt) for v in (x, y, z)] == [2, 0, 1]
P(id="3-42", ch=14, sec="14.3", type="14-implicit", src="2024 중간 1(b) 유형",
  q=r"$xz^2+ye^{x-yz}=2$일 때 점 $(1,1,1)$에서 $\dfrac{\partial z}{\partial x}$, $\dfrac{\partial z}{\partial y}$를 구하라.",
  hint=r"$F=xz^2+ye^{x-yz}-2$. $F_y$는 곱의 미분: $e^{x-yz}+ye^{x-yz}\cdot(-z)$",
  ans=r"$z_x=-2,\ \ z_y=0$",
  sol=[r"$F_x=z^2+ye^{x-yz}=1+1=2$",
       r"$F_y=e^{x-yz}-yze^{x-yz}=1-1=0$",
       r"$F_z=2xz-y^2e^{x-yz}=2-1=1$",
       r"$z_x=-\dfrac{F_x}{F_z}=-2$,  $z_y=-\dfrac{F_y}{F_z}=0$"],
  check=_c)


def _c():
    F = exp(x*y*z) - log(x*z*(y + 2))
    pt = {x: 1, y: 0, z: E/2}
    assert simplify(F.subs(pt)) == 0
    zx = simplify((-diff(F, x)/diff(F, z)).subs(pt)); zy = simplify((-diff(F, y)/diff(F, z)).subs(pt))
    assert EQ(zx, -E/2) and EQ(zy, E*(E - 1)/4)
P(id="3-43", ch=14, sec="14.3", type="14-implicit", src="2022 생명과학대 기말 6번 유형",
  q=r"$z$가 방정식 $e^{xyz}=\ln\big(xz(y+2)\big)$에 의해 $x,y$의 함수로 정해질 때, $(x,y)=(1,0)$에서 $z$의 값과 $\dfrac{\partial z}{\partial x}$, $\dfrac{\partial z}{\partial y}$를 구하라.",
  hint=r"$(1,0)$을 대입하면 $1=\ln(2z)$. $\ln\big(xz(y+2)\big)=\ln x+\ln z+\ln(y+2)$로 나누면 미분이 쉬워요.",
  ans=r"$z=\dfrac e2$,  $z_x=-\dfrac e2$,  $z_y=\dfrac{e(e-1)}{4}$",
  sol=[r"$(1,0)$: $e^0=1=\ln(2z) \Rightarrow z=\dfrac e2$",
       r"$F=e^{xyz}-\ln x-\ln z-\ln(y+2)$: $F_x=yze^{xyz}-\dfrac1x=-1$,  $F_y=xze^{xyz}-\dfrac{1}{y+2}=\dfrac e2-\dfrac12$",
       r"$F_z=xye^{xyz}-\dfrac1z=-\dfrac2e$",
       r"$z_x=-\dfrac{-1}{-2/e}=-\dfrac e2$,  $z_y=-\dfrac{(e-1)/2}{-2/e}=\dfrac{e(e-1)}{4}$"],
  check=_c)


def _c():
    a = symbols('a', positive=True)
    uu = sin(x - a*t) + log(x + a*t)
    assert simplify(diff(uu, t, 2) - a**2*diff(uu, x, 2)) == 0
P(id="3-44", ch=14, sec="14.3", type="14-higher", src="강의 14.3 (파동방정식) 유형",
  q=r"$u(x,t)=\sin(x-at)+\ln(x+at)$이 파동방정식 $u_{tt}=a^2u_{xx}$를 만족함을 보여라.",
  hint=r"$t$로 미분할 때마다 연쇄법칙으로 $\mp a$가 곱해져요.",
  ans=r"$u_{tt}=-a^2\sin(x-at)-\dfrac{a^2}{(x+at)^2}=a^2u_{xx}$",
  sol=[r"$u_x=\cos(x-at)+\dfrac{1}{x+at}$,  $u_{xx}=-\sin(x-at)-\dfrac{1}{(x+at)^2}$",
       r"$u_t=-a\cos(x-at)+\dfrac{a}{x+at}$,  $u_{tt}=-a^2\sin(x-at)-\dfrac{a^2}{(x+at)^2}$",
       r"$u_{tt}=a^2u_{xx}$ ✓"],
  check=_c)


def _c():
    Pp, V, T, n, Rr = symbols('P V T n R', positive=True)
    PV = n*Rr*T/V; VV = n*Rr*T/Pp; TT = Pp*V/(n*Rr)
    prod = diff(PV, V) * diff(VV, T) * diff(TT, Pp)
    assert simplify(prod.subs(T, Pp*V/(n*Rr))) == -1
P(id="3-45", ch=14, sec="14.3", type="14-partial", src="강의 14.3 (이상기체) 유형",
  q=r"이상기체 법칙 $PV=nRT$ ($n,R$은 상수)에 대해 $\dfrac{\partial P}{\partial V}\cdot\dfrac{\partial V}{\partial T}\cdot\dfrac{\partial T}{\partial P}=-1$임을 보여라.",
  hint=r"$P=\dfrac{nRT}{V}$, $V=\dfrac{nRT}{P}$, $T=\dfrac{PV}{nR}$로 각각 풀어서 편미분해요.",
  ans=r"$\Big(-\dfrac{nRT}{V^2}\Big)\Big(\dfrac{nR}{P}\Big)\Big(\dfrac{V}{nR}\Big)=-\dfrac{nRT}{PV}=-1$",
  sol=[r"$\dfrac{\partial P}{\partial V}=-\dfrac{nRT}{V^2}$,  $\dfrac{\partial V}{\partial T}=\dfrac{nR}{P}$,  $\dfrac{\partial T}{\partial P}=\dfrac{V}{nR}$",
       r"곱: $-\dfrac{nRT}{V^2}\cdot\dfrac{nR}{P}\cdot\dfrac{V}{nR}=-\dfrac{nRT}{PV}=-1$ ($PV=nRT$)",
       r"편미분을 분수처럼 약분하면 $+1$이 나올 것 같지만 실제로는 $-1$ — 편도함수는 분수가 아니에요."],
  check=_c)


# ───────── 14.4 ─────────
def _c():
    E_ = x**2 + y**2/4 + z**2/2
    pt = {x: R(1, 2), y: 1, z: 1}
    assert E_.subs(pt) == 1
    g = grad(E_, (x, y, z)).subs(pt)
    assert EQ(g * 2, [2, 1, 2])
    p_, q_ = R(-1, 2), R(-1, 4)
    zz = (4 - 2*p_ - q_) / 2
    kk = zz - p_**2 - q_**2
    assert EQ(kk, R(37, 16))
    assert EQ(Matrix([2*p_, 2*q_, -1]).cross(Matrix([2, 1, 2])), [0, 0, 0])
P(id="3-46", ch=14, sec="14.4", type="14-tangent", src="2022 중간(블럭1) 7번 유형",
  q=r"(a) 평면 $2x+y+mz=4$가 타원면 $x^2+\dfrac{y^2}{4}+\dfrac{z^2}{2}=1$에 접할 때 양수 $m$을 구하라.<br>(b) (a)의 $m$에 대해 이 평면이 포물면 $z=x^2+y^2+k$에도 접할 때 실수 $k$를 구하라.",
  hint=r"(a) 접점 $(a,b,c)$에서 접평면 $ax+\tfrac b4y+\tfrac c2z=1$과 주어진 평면의 계수를 비교. (b) 포물면의 법선 $\langle2p,2q,-1\rangle$이 $\langle2,1,m\rangle$과 평행",
  ans=r"(a) $m=2$ (접점 $\left(\tfrac12,1,1\right)$)  (b) $k=\dfrac{37}{16}$",
  sol=[r"(a) 접점 $(a,b,c)$에서 접평면: $ax+\tfrac{b}{4}y+\tfrac{c}{2}z=1$. 주어진 평면을 $4$로 나누면 $\tfrac12x+\tfrac14y+\tfrac m4z=1$",
       r"비교: $a=\tfrac12,\ b=1,\ c=\tfrac m2$ → 타원면에 대입 $\tfrac14+\tfrac14+\tfrac{m^2}{8}=1 \Rightarrow m=2$",
       r"(b) 포물면 위 점 $(p,q)$의 법선 $\langle2p,2q,-1\rangle\parallel\langle2,1,2\rangle$ → $2p=-1,\ 2q=-\tfrac12$ → $p=-\tfrac12,\ q=-\tfrac14$",
       r"접점의 $z$는 평면에서 $z=\dfrac{4-2p-q}{2}=\dfrac{21}{8}$, 포물면에서 $z=p^2+q^2+k=\dfrac{5}{16}+k$",
       r"$k=\dfrac{21}{8}-\dfrac{5}{16}=\dfrac{37}{16}$"],
  check=_c)


def _c():
    rr_, ss_, tt_ = symbols('rr ss tt', real=True)
    g = rr_**2 + ss_**2 - 2*tt_
    f = g.subs({rr_: x**2 + y, ss_: exp(x + y) - 2, tt_: x*y}, simultaneous=True)
    pt = {x: 1, y: -1}
    assert f.subs(pt) == 3 and diff(f, x).subs(pt) == 0 and diff(f, y).subs(pt) == -4
    L = 3 - 4*(y + 1)
    assert EQ(L.subs(y, R(-97, 100)), R(288, 100))
P(id="3-47", ch=14, sec="14.4", type="14-tangent", src="2022 중간(블럭1) 3번 유형",
  q=r"$f(x,y)=g\big(x^2+y,\ e^{x+y}-2,\ xy\big)$, $g(r,s,t)=r^2+s^2-2t$일 때<br>(a) 연쇄법칙으로 $f_x(1,-1)$, $f_y(1,-1)$을 구하라.  (b) $(1,-1)$에서 $f$의 선형화를 구하라.  (c) $f(1.02,\ -0.97)$의 근삿값을 구하라.",
  hint=r"$(1,-1)$에서 $(r,s,t)=(0,-1,-1)$. $f_x=g_r\cdot2x+g_s\cdot e^{x+y}+g_t\cdot y$",
  ans=r"(a) $f_x(1,-1)=0,\ f_y(1,-1)=-4$  (b) $L(x,y)=3-4(y+1)$  (c) $2.88$",
  sol=[r"$(r,s,t)=(0,-1,-1)$, $g_r=2r=0,\ g_s=2s=-2,\ g_t=-2$, $f(1,-1)=0+1+2=3$",
       r"(a) $f_x=g_r(2x)+g_s e^{x+y}+g_t\,y=0+(-2)(1)+(-2)(-1)=0$",
       r"$f_y=g_r(1)+g_se^{x+y}+g_t\,x=0-2-2=-4$",
       r"(b) $L(x,y)=3+0\cdot(x-1)-4(y+1)$",
       r"(c) $L(1.02,-0.97)=3-4(0.03)=2.88$"],
  check=_c)


def _c():
    F = x**2*z + y*z**3 - x*y
    pt = {x: 2, y: 1, z: 1}
    assert F.subs(pt) == 3
    gx = (-diff(F, x)/diff(F, z)).subs(pt); gy = (-diff(F, y)/diff(F, z)).subs(pt)
    assert gx == R(-3, 7) and gy == R(1, 7) and EQ(sqrt(gx**2 + gy**2), sqrt(10)/7)
    assert EQ(1 + gx*R(1, 10) + gy*R(-2, 10), R(13, 14))
P(id="3-48", ch=14, sec="14.4", type="14-tangent", src="2022 중간(블럭2) 3번 유형",
  q=r"$f(x,y,z)=x^2z+yz^3-xy$이고 미분가능한 함수 $g(x,y)$가 $g(2,1)=1$, $f\big(x,y,g(x,y)\big)=3$을 만족한다.<br>(a) $(2,1)$에서 $g$가 가장 빠르게 증가하는 방향의 방향도함수를 구하라.  (b) 선형근사로 $g(2.1,\ 0.8)$의 근삿값을 구하라.",
  hint=r"$f(x,y,g)=3$을 음함수로 보면 $g_x=-\dfrac{f_x}{f_z},\ g_y=-\dfrac{f_y}{f_z}$ (점 $(2,1,1)$). 최대 방향도함수 $=|\nabla g|$",
  ans=r"(a) $\dfrac{\sqrt{10}}{7}$  (b) $\dfrac{13}{14}\approx0.929$",
  sol=[r"점 $(2,1,1)$: $f_x=2xz-y=3$,  $f_y=z^3-x=-1$,  $f_z=x^2+3yz^2=7$",
       r"$g_x=-\dfrac37$,  $g_y=\dfrac17$ → (a) $|\nabla g(2,1)|=\dfrac{\sqrt{9+1}}{7}=\dfrac{\sqrt{10}}{7}$",
       r"(b) $g(2.1,0.8)\approx1-\dfrac37(0.1)+\dfrac17(-0.2)=1-\dfrac{0.5}{7}=\dfrac{13}{14}$"],
  check=_c)


def _c():
    zz = 4 - 3*x + 2*y
    assert zz.subs({x: 2, y: 1}) == 0
    assert EQ(Matrix([-3, 2]).dot(Matrix([3, -4]))/5, R(-17, 5))
    assert EQ(zz.subs({x: R(19, 10), y: R(12, 10)}), R(7, 10))
P(id="3-49", ch=14, sec="14.4", type="14-tangent", src="2025 중간 6번 유형",
  q=r"미분가능한 $F(x,y,z)$에 대해 $F_z\ne0$이고, $z=z(x,y)$가 $F\big(x,y,z(x,y)\big)=0$으로 정해진다. 곡면 $F=0$의 점 $(2,1)$ 위에서의 접평면이 $3x-2y+z=4$일 때<br>(a) $(2,1)$에서 $\mathbf v=\langle3,-4\rangle$ 방향으로의 $z$의 변화율을 구하라.  (b) 선형근사로 $z(1.9,\ 1.2)$를 추정하라.",
  hint=r"접평면을 $z=4-3x+2y$로 풀면 $z(2,1)$, $z_x$, $z_y$를 바로 읽을 수 있어요.",
  ans=r"(a) $-\dfrac{17}{5}$  (b) $0.7$",
  sol=[r"접평면 $z=4-3x+2y$ → $z(2,1)=0$, $z_x(2,1)=-3$, $z_y(2,1)=2$",
       r"(a) $\mathbf u=\left\langle\tfrac35,-\tfrac45\right\rangle$: $D_{\mathbf u}z=-3\cdot\tfrac35+2\cdot\big(-\tfrac45\big)=-\dfrac{17}{5}$",
       r"(b) $z(1.9,1.2)\approx0-3(-0.1)+2(0.2)=0.7$"],
  check=_c)


# ───────── 14.5 ─────────
def _c():
    f = x**2*y + x*y**3 + exp(x)*y
    X, Y = s*t, s/t
    Z = f.subs({x: X, y: Y}, simultaneous=True)
    lhs = s**2*diff(Z, s, 2) - t**2*diff(Z, t, 2)
    rhs = (4*x*y*diff(f, x, y) - 2*y*diff(f, y)).subs({x: X, y: Y}, simultaneous=True)
    assert simplify(lhs - rhs) == 0
    assert 4*1*1*3 - 2*1*2 == 8
P(id="3-50", ch=14, sec="14.5", type="14-chain2", src="2025 중간 5번 유형",
  q=r"$z=f(x,y)$의 2계 편도함수가 연속이고 $x=st,\ y=\dfrac st$이다. $f_{xy}(1,1)=3,\ f_y(1,1)=2$일 때 $(s,t)=(1,1)$에서 $s^2\dfrac{\partial^2z}{\partial s^2}-t^2\dfrac{\partial^2z}{\partial t^2}$의 값을 구하라.",
  hint=r"$z_s=tf_x+\tfrac1tf_y$, $z_t=sf_x-\tfrac{s}{t^2}f_y$. 두 번 미분한 뒤 빼면 $f_{xx},f_{yy}$ 항이 지워져요.",
  ans=r"$8$  (일반식 $s^2z_{ss}-t^2z_{tt}=4xy\,f_{xy}-2y\,f_y$)",
  sol=[r"$z_{ss}=t^2f_{xx}+2f_{xy}+\tfrac{1}{t^2}f_{yy}$ → $s^2z_{ss}=s^2t^2f_{xx}+2s^2f_{xy}+\tfrac{s^2}{t^2}f_{yy}$",
       r"$z_{tt}=s^2f_{xx}-\tfrac{2s^2}{t^2}f_{xy}+\tfrac{2s}{t^3}f_y+\tfrac{s^2}{t^4}f_{yy}$ → $t^2z_{tt}=s^2t^2f_{xx}-2s^2f_{xy}+\tfrac{2s}{t}f_y+\tfrac{s^2}{t^2}f_{yy}$",
       r"빼면 $s^2z_{ss}-t^2z_{tt}=4s^2f_{xy}-\tfrac{2s}{t}f_y=4xy\,f_{xy}-2y\,f_y$ ($s^2=xy,\ \tfrac st=y$)",
       r"$(s,t)=(1,1)$이면 $(x,y)=(1,1)$: $4\cdot3-2\cdot2=8$"],
  check=_c)


def _c():
    uu, vv = symbols('uu vv', real=True)
    fcon = uu**2 + vv - 2                      # 예시 f: f(2,1)=3
    assert fcon.subs({uu: 2, vv: 1}) == 3
    g = x**2*fcon.subs({uu: y/x, vv: z/x}, simultaneous=True)
    assert simplify(x*diff(g, x) + y*diff(g, y) + z*diff(g, z) - 2*g) == 0
    pt = {x: 1, y: 2, z: 1}
    dg = sum(diff(g, v).subs(pt)*dv for v, dv in zip((x, y, z), (R(1, 10), R(2, 10), R(1, 10))))
    assert EQ(g.subs(pt) + dg, R(36, 10))
P(id="3-51", ch=14, sec="14.5", type="14-chain", src="2024 중간 5번 유형 (동차함수)",
  q=r"$f(u,v)$가 미분가능하고 $g(x,y,z)=x^2f\Big(\dfrac yx,\ \dfrac zx\Big)$이다.<br>(a) $xg_x+yg_y+zg_z-2g$를 구하라.  (b) $f(2,1)=3$일 때 점 $(1,2,1)$에서 $g$의 선형근사로 $g(1.1,\ 2.2,\ 1.1)$을 추정하라.",
  hint=r"$u=\tfrac yx,\ v=\tfrac zx$: $g_x=2xf+x^2\big(f_u\cdot(-\tfrac{y}{x^2})+f_v\cdot(-\tfrac{z}{x^2})\big)$. (b)의 이동량 $\langle0.1,0.2,0.1\rangle$은 $0.1\langle1,2,1\rangle$이에요.",
  ans=r"(a) $0$  (b) $3.6$",
  sol=[r"(a) $g_x=2xf-yf_u-zf_v$,  $g_y=xf_u$,  $g_z=xf_v$",
       r"$xg_x+yg_y+zg_z=2x^2f-xyf_u-xzf_v+xyf_u+xzf_v=2x^2f=2g$ → 값 $0$",
       r"(b) $g(1,2,1)=1\cdot f(2,1)=3$. $\Delta g\approx g_x(0.1)+g_y(0.2)+g_z(0.1)=0.1\,(xg_x+yg_y+zg_z)=0.1\cdot2g=0.6$",
       r"$g(1.1,2.2,1.1)\approx3.6$ (실제로는 $1.1^2\cdot3=3.63$)"],
  check=_c)


def _c():
    f = 3*(x - 1) - (y - 2) + R(1, 2)*(x - 1)**2 + 2*(x - 1)*(y - 2) - R(1, 2)*(y - 2)**2
    pt = {x: 1, y: 2}
    assert [diff(f, x).subs(pt), diff(f, y).subs(pt), diff(f, x, 2).subs(pt), diff(f, x, y).subs(pt), diff(f, y, 2).subs(pt)] == [3, -1, 1, 2, -1]
    G = f.subs({x: s - t, y: s*t}, simultaneous=True)
    p2 = {s: 2, t: 1}
    assert diff(G, s).subs(p2) == 2 and diff(G, t).subs(p2) == -5 and diff(G, s, t).subs(p2) == -2
P(id="3-52", ch=14, sec="14.5", type="14-chain", src="2022 중간(블럭2) 4번 유형",
  q=r"$g(s,t)=f(s-t,\ st)$이고 $f$는 2계 편도함수가 연속이며 $f_x(1,2)=3,\ f_y(1,2)=-1,\ f_{xx}(1,2)=1,\ f_{xy}(1,2)=2,\ f_{yy}(1,2)=-1$이다. $(s,t)=(2,1)$에서 $g_s,\ g_t,\ g_{st}$를 구하라.",
  hint=r"$(s,t)=(2,1)$이면 $(x,y)=(1,2)$. $g_s=f_x+tf_y$를 $t$로 미분할 때 $f_x,f_y$에도 연쇄법칙",
  ans=r"$g_s=2,\ \ g_t=-5,\ \ g_{st}=-2$",
  sol=[r"$x=s-t,\ y=st$: $x_s=1,\ x_t=-1,\ y_s=t,\ y_t=s$",
       r"$g_s=f_x+tf_y=3+1\cdot(-1)=2$,  $g_t=-f_x+sf_y=-3+2(-1)=-5$",
       r"$g_{st}=\big(-f_{xx}+sf_{xy}\big)+f_y+t\big(-f_{yx}+sf_{yy}\big)$",
       r"$=(-1+4)+(-1)+1\cdot(-2-2)=-2$"],
  check=_c)


def _c():
    F3 = Function('F')
    w = F3(x - y, y - z, z - x)
    assert simplify(diff(w, x) + diff(w, y) + diff(w, z)) == 0
P(id="3-53", ch=14, sec="14.5", type="14-chain", src="복습 14.1–3 기초2 유형",
  q=r"$f$가 미분가능하고 $w=f(x-y,\ y-z,\ z-x)$일 때 $\dfrac{\partial w}{\partial x}+\dfrac{\partial w}{\partial y}+\dfrac{\partial w}{\partial z}=0$임을 보여라.",
  hint=r"$u=x-y,\ v=y-z,\ s=z-x$로 두고 각 편도함수를 $f_u,f_v,f_s$로 써요.",
  ans=r"$w_x=f_u-f_s,\ w_y=-f_u+f_v,\ w_z=-f_v+f_s$ → 합 $0$",
  sol=[r"$w_x=f_u\cdot1+f_v\cdot0+f_s\cdot(-1)=f_u-f_s$",
       r"$w_y=f_u\cdot(-1)+f_v\cdot1=-f_u+f_v$,  $w_z=f_v\cdot(-1)+f_s\cdot1=-f_v+f_s$",
       r"더하면 $0$ ✓"],
  check=_c)


def _c():
    rr_, hh = symbols('rr hh', positive=True)
    V = pi*rr_**2*hh
    dV = (diff(V, rr_)*R(1, 2) + diff(V, hh)*(-1)).subs({rr_: 4, hh: 10})
    assert EQ(dV, 24*pi)
P(id="3-54", ch=14, sec="14.5", type="14-chain", src="강의 14.5 (관련 변화율) 유형",
  q=r"원기둥의 반지름이 $0.5$ cm/s로 늘어나고 높이가 $1$ cm/s로 줄어든다. 반지름이 $4$ cm, 높이가 $10$ cm인 순간 부피의 변화율을 구하라.",
  hint=r"$V=\pi r^2h$, $\dfrac{dV}{dt}=V_r\dfrac{dr}{dt}+V_h\dfrac{dh}{dt}$",
  ans=r"$24\pi$ cm³/s (증가)",
  sol=[r"$\dfrac{dV}{dt}=2\pi rh\dfrac{dr}{dt}+\pi r^2\dfrac{dh}{dt}$",
       r"$=2\pi(4)(10)(0.5)+\pi(16)(-1)=40\pi-16\pi=24\pi$"],
  check=_c)


def _c():
    f = x**3*y + x*y**2 + exp(x)
    Z = f.subs({x: exp(s)*cos(t), y: exp(s)*sin(t)}, simultaneous=True)
    rhs = (exp(2*s)*(diff(f, x, 2) + diff(f, y, 2))).subs({x: exp(s)*cos(t), y: exp(s)*sin(t)}, simultaneous=True)
    assert simplify(diff(Z, s, 2) + diff(Z, t, 2) - rhs) == 0
P(id="3-55", ch=14, sec="14.5", type="14-chain2", src="복습 14.4–6 기초1 · 과제 14.5 #49 종합",
  q=r"$z=f(x,y)$의 2계 편도함수가 연속이고 $x=e^{s}\cos t,\ y=e^{s}\sin t$일 때 $z_{ss}+z_{tt}=e^{2s}\big(f_{xx}+f_{yy}\big)$임을 보여라.",
  hint=r"$x_s=x,\ y_s=y,\ x_t=-y,\ y_t=x$를 이용하면 식이 깔끔해요.",
  ans=r"$z_{ss}=xf_x+yf_y+x^2f_{xx}+2xyf_{xy}+y^2f_{yy}$, $z_{tt}=-xf_x-yf_y+y^2f_{xx}-2xyf_{xy}+x^2f_{yy}$ → 합 $(x^2+y^2)(f_{xx}+f_{yy})$",
  sol=[r"$x_s=x,\ y_s=y,\ x_t=-y,\ y_t=x$ → $z_s=xf_x+yf_y$,  $z_t=-yf_x+xf_y$",
       r"$z_{ss}=x f_x+x(xf_{xx}+yf_{xy})+yf_y+y(xf_{yx}+yf_{yy})=xf_x+yf_y+x^2f_{xx}+2xyf_{xy}+y^2f_{yy}$",
       r"$z_{tt}=-xf_x-y(-yf_{xx}+xf_{xy})-yf_y+x(-yf_{yx}+xf_{yy})=-xf_x-yf_y+y^2f_{xx}-2xyf_{xy}+x^2f_{yy}$",
       r"더하면 $(x^2+y^2)(f_{xx}+f_{yy})=e^{2s}(f_{xx}+f_{yy})$ ✓"],
  check=_c)


# ───────── 14.6 ─────────
def _c():
    g = 6*Matrix([1, 2, -2])/3
    assert EQ(g, [2, 4, -4])
    assert EQ(g.dot(Matrix([2, -1, 2]))/3, R(-8, 3))
    gh = 2*3*g
    assert EQ(gh.dot(Matrix([0, 3, 4]))/5, R(-24, 5))
P(id="3-56", ch=14, sec="14.6", type="14-dir", src="2022 중간(블럭1) 5번 유형",
  q=r"미분가능한 $f$가 점 $P$에서 벡터 $\langle1,2,-2\rangle$ 방향으로 최대 변화율 $6$을 가진다. 또 $f(P)=3$이다.<br>(a) $\nabla f(P)$를 구하라.  (b) $P$에서 $\langle2,-1,2\rangle$ 방향의 방향도함수를 구하라.  (c) $h=f^2$의 $P$에서 $\langle0,3,4\rangle$ 방향의 변화율을 구하라.",
  hint=r"최대 변화율의 방향이 $\nabla f$의 방향이고 크기가 $|\nabla f|$예요. (c) $\nabla(f^2)=2f\nabla f$",
  ans=r"(a) $\langle2,4,-4\rangle$  (b) $-\dfrac83$  (c) $-\dfrac{24}{5}$",
  sol=[r"(a) $\nabla f(P)=6\cdot\dfrac{\langle1,2,-2\rangle}{3}=\langle2,4,-4\rangle$",
       r"(b) $\mathbf u=\tfrac13\langle2,-1,2\rangle$: $D_{\mathbf u}f=\dfrac{4-4-8}{3}=-\dfrac83$",
       r"(c) $\nabla h(P)=2f(P)\nabla f(P)=6\langle2,4,-4\rangle=\langle12,24,-24\rangle$",
       r"$\mathbf u=\left\langle0,\tfrac35,\tfrac45\right\rangle$: $D_{\mathbf u}h=\dfrac{72-96}{5}=-\dfrac{24}{5}$"],
  check=_c)


def _c():
    f = x**2 + x*y + 2*y**2
    uvec = Matrix([R(3, 5), R(4, 5)])
    Du = grad(f, (x, y)).dot(uvec)
    Du2 = grad(Du, (x, y)).dot(uvec)
    assert EQ(Du.subs({x: 1, y: 1}), R(29, 5)) and EQ(simplify(Du2), R(106, 25))
P(id="3-57", ch=14, sec="14.6", type="14-dir", src="2024 중간 7번 유형 (2계 방향도함수)",
  q=r"$f(x,y)=x^2+xy+2y^2$, $\mathbf u=\left\langle\tfrac35,\tfrac45\right\rangle$일 때 점 $(1,1)$에서 $D_{\mathbf u}f$와 2계 방향도함수 $D_{\mathbf u}^2f=D_{\mathbf u}(D_{\mathbf u}f)$를 구하라.",
  hint=r"$D_{\mathbf u}^2f=f_{xx}u_1^2+2f_{xy}u_1u_2+f_{yy}u_2^2$",
  ans=r"$D_{\mathbf u}f(1,1)=\dfrac{29}{5}$,  $D_{\mathbf u}^2f=\dfrac{106}{25}$ (모든 점에서)",
  sol=[r"$\nabla f=\langle2x+y,\ x+4y\rangle \Rightarrow \nabla f(1,1)=\langle3,5\rangle$, $D_{\mathbf u}f=\tfrac{9}{5}+4=\dfrac{29}{5}$",
       r"$D_{\mathbf u}f=\tfrac35(2x+y)+\tfrac45(x+4y)=2x+\tfrac{19}{5}y$",
       r"$D_{\mathbf u}^2f=\nabla(D_{\mathbf u}f)\cdot\mathbf u=\langle2,\tfrac{19}{5}\rangle\cdot\langle\tfrac35,\tfrac45\rangle=\dfrac65+\dfrac{76}{25}=\dfrac{106}{25}$",
       r"(공식: $2\cdot\tfrac{9}{25}+2\cdot1\cdot\tfrac{12}{25}+4\cdot\tfrac{16}{25}=\tfrac{106}{25}$)"],
  check=_c)


def _c():
    T = 120/(1 + x**2 + 2*y**2 + 3*z**2)
    g = grad(T, (x, y, z)).subs({x: 1, y: -1, z: 1})
    assert EQ(g, [R(-240, 49), R(480, 49), R(-720, 49)]) and EQ(g.norm(), 240*sqrt(14)/49)
P(id="3-58", ch=14, sec="14.6", type="14-maxrate", src="복습 14.4–6 기초2 유형",
  q=r"$T(x,y,z)=\dfrac{120}{1+x^2+2y^2+3z^2}$ (°C)일 때 점 $(1,-1,1)$에서 온도가 가장 빨리 올라가는 방향과 최대 증가율을 구하라.",
  hint=r"분모 $=7$. $\nabla T=-\dfrac{120}{7^2}\langle2x,4y,6z\rangle$",
  ans=r"방향 $\dfrac{1}{\sqrt{14}}\langle-1,2,-3\rangle$,  최대 증가율 $\dfrac{240\sqrt{14}}{49}$",
  sol=[r"$\nabla T=-\dfrac{120}{(1+x^2+2y^2+3z^2)^2}\langle2x,4y,6z\rangle=-\dfrac{120}{49}\langle2,-4,6\rangle$",
       r"방향: $\langle-2,4,-6\rangle\parallel\langle-1,2,-3\rangle$ → 단위벡터 $\dfrac{1}{\sqrt{14}}\langle-1,2,-3\rangle$",
       r"최대 증가율: $|\nabla T|=\dfrac{120}{49}\sqrt{4+16+36}=\dfrac{120\cdot2\sqrt{14}}{49}=\dfrac{240\sqrt{14}}{49}$"],
  check=_c)


def _c():
    F1, F2 = x**2 + 2*y**2 + z**2 - 7, x**2 + y**2 - z
    pt = {x: 1, y: -1, z: 2}
    assert F1.subs(pt) == 0 and F2.subs(pt) == 0
    d = grad(F1, (x, y, z)).subs(pt).cross(grad(F2, (x, y, z)).subs(pt))
    assert EQ(d, [12, 10, 4])
P(id="3-59", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 (두 곡면의 교선) · 2022 생명과학대 기말 5번 유형",
  q=r"타원면 $x^2+2y^2+z^2=7$과 포물면 $z=x^2+y^2$의 교선 위의 점 $(1,-1,2)$에서 교선의 접선의 매개방정식을 구하라.",
  hint=r"접선은 두 곡면의 법선 $\nabla F_1$, $\nabla F_2$에 모두 수직 → 방향 $=\nabla F_1\times\nabla F_2$",
  ans=r"$x=1+6t,\ y=-1+5t,\ z=2+2t$",
  sol=[r"$\nabla F_1=\langle2x,4y,2z\rangle=\langle2,-4,4\rangle$,  $F_2=x^2+y^2-z$: $\nabla F_2=\langle2,-2,-1\rangle$",
       r"$\langle2,-4,4\rangle\times\langle2,-2,-1\rangle=\langle4+8,\ 8+2,\ -4+8\rangle=\langle12,10,4\rangle\parallel\langle6,5,2\rangle$",
       r"접선: $x=1+6t,\ y=-1+5t,\ z=2+2t$"],
  check=_c)


def _c():
    a, b, d, c_ = symbols('a b d c', positive=True)
    # 접평면 x/sqrt(a)+y/sqrt(b)+z/sqrt(d)=sqrt(a)+sqrt(b)+sqrt(d) 의 절편 합
    S = sqrt(a)*(sqrt(a) + sqrt(b) + sqrt(d)) + sqrt(b)*(sqrt(a) + sqrt(b) + sqrt(d)) + sqrt(d)*(sqrt(a) + sqrt(b) + sqrt(d))
    assert simplify(S - (sqrt(a) + sqrt(b) + sqrt(d))**2) == 0
    F = sqrt(x) + sqrt(y) + sqrt(z)
    g = grad(F, (x, y, z)).subs({x: a, y: b, z: d})
    plane = g[0]*(x - a) + g[1]*(y - b) + g[2]*(z - d)
    assert simplify(plane*2 - ((x - a)/sqrt(a) + (y - b)/sqrt(b) + (z - d)/sqrt(d))) == 0
P(id="3-60", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 응용 (접평면의 절편)",
  q=r"곡면 $\sqrt x+\sqrt y+\sqrt z=\sqrt c$ ($c>0$) 위의 임의의 점에서 그은 접평면의 세 좌표축 절편의 합이 항상 $c$임을 보여라.",
  hint=r"점 $(a,b,d)$에서 $\nabla F=\left\langle\tfrac{1}{2\sqrt a},\tfrac{1}{2\sqrt b},\tfrac{1}{2\sqrt d}\right\rangle$",
  ans=r"접평면 $\dfrac{x}{\sqrt a}+\dfrac{y}{\sqrt b}+\dfrac{z}{\sqrt d}=\sqrt c$ → 절편 합 $\sqrt c(\sqrt a+\sqrt b+\sqrt d)=c$",
  sol=[r"접평면: $\dfrac{x-a}{\sqrt a}+\dfrac{y-b}{\sqrt b}+\dfrac{z-d}{\sqrt d}=0 \Rightarrow \dfrac{x}{\sqrt a}+\dfrac{y}{\sqrt b}+\dfrac{z}{\sqrt d}=\sqrt a+\sqrt b+\sqrt d=\sqrt c$",
       r"$x$절편 $\sqrt a\sqrt c$, $y$절편 $\sqrt b\sqrt c$, $z$절편 $\sqrt d\sqrt c$",
       r"합: $\sqrt c(\sqrt a+\sqrt b+\sqrt d)=\sqrt c\cdot\sqrt c=c$ ✓"],
  check=_c)


def _c():
    kk = symbols('kk', real=True)
    sols = solve((kk/2)**2 - kk**2 + 2*(3*kk/4)**2 - 1, kk)
    assert sorted(sols, key=float) == [-2*sqrt(6)/3, 2*sqrt(6)/3]
    k0 = 2*sqrt(6)/3
    pt = (k0/2, -k0, 3*k0/4)
    assert EQ(pt[0], sqrt(6)/3) and EQ(pt[1], -2*sqrt(6)/3) and EQ(pt[2], sqrt(6)/2)
    assert EQ(pt[0]**2 - pt[1]**2 + 2*pt[2]**2, 1)
P(id="3-61", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 응용 (평행한 법선)",
  q=r"쌍곡면 $x^2-y^2+2z^2=1$ 위에서 법선이 두 점 $(3,-1,0)$, $(5,3,6)$을 잇는 직선과 평행한 점을 모두 구하라.",
  hint=r"직선의 방향 $\langle2,4,6\rangle\parallel\langle1,2,3\rangle$. $\nabla F=\langle2x,-2y,4z\rangle=k\langle1,2,3\rangle$",
  ans=r"$\left(\dfrac{\sqrt6}{3},\ -\dfrac{2\sqrt6}{3},\ \dfrac{\sqrt6}{2}\right)$,  $\left(-\dfrac{\sqrt6}{3},\ \dfrac{2\sqrt6}{3},\ -\dfrac{\sqrt6}{2}\right)$",
  sol=[r"$2x=k,\ -2y=2k,\ 4z=3k$ → $x=\tfrac k2,\ y=-k,\ z=\tfrac{3k}{4}$",
       r"곡면에 대입: $\tfrac{k^2}{4}-k^2+\tfrac{9k^2}{8}=\tfrac38k^2=1 \Rightarrow k=\pm\tfrac{2\sqrt6}{3}$",
       r"$k=\tfrac{2\sqrt6}{3}$: $\left(\tfrac{\sqrt6}{3},-\tfrac{2\sqrt6}{3},\tfrac{\sqrt6}{2}\right)$, $k=-\tfrac{2\sqrt6}{3}$: 부호가 모두 반대"],
  check=_c)


# ───────── 14.7 ─────────
def _c():
    f = x**2*exp(-x) + y**3 - 3*y
    for p_ in [(0, 1), (0, -1), (2, 1), (2, -1)]:
        assert simplify(diff(f, x).subs({x: p_[0], y: p_[1]})) == 0 and diff(f, y).subs({x: p_[0], y: p_[1]}) == 0
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    v = lambda e, a, b: simplify(e.subs({x: a, y: b}))
    assert v(D, 0, 1) > 0 and v(diff(f, x, 2), 0, 1) > 0 and v(f, 0, 1) == -2
    assert v(D, 0, -1) < 0 and v(D, 2, 1) < 0
    assert v(D, 2, -1) > 0 and v(diff(f, x, 2), 2, -1) < 0 and EQ(v(f, 2, -1), 4*exp(-2) + 2)
P(id="3-62", ch=14, sec="14.7", type="14-crit", src="2022 중간(블럭2) 5(a) 유형",
  q=r"$f(x,y)=x^2e^{-x}+y^3-3y$의 임계점을 모두 구하고 분류하라.",
  hint=r"$f_x=(2x-x^2)e^{-x}$, $f_{xx}=(2-4x+x^2)e^{-x}$. 임계점은 $x\in\{0,2\},\ y\in\{1,-1\}$의 네 조합",
  ans=r"$(0,1)$ 극솟값 $-2$,  $(2,-1)$ 극댓값 $4e^{-2}+2$,  $(0,-1)$과 $(2,1)$ 안장점",
  sol=[r"$f_x=x(2-x)e^{-x}=0 \Rightarrow x=0,2$;  $f_y=3y^2-3=0 \Rightarrow y=\pm1$",
       r"$f_{xx}=(2-4x+x^2)e^{-x}$: $x=0$에서 $2$, $x=2$에서 $-2e^{-2}$.  $f_{yy}=6y$, $f_{xy}=0$",
       r"$(0,1)$: $D=12>0,\ f_{xx}>0$ → 극솟값 $f=-2$.  $(0,-1)$: $D=-12<0$ → 안장점",
       r"$(2,1)$: $D=-12e^{-2}<0$ → 안장점.  $(2,-1)$: $D=12e^{-2}>0,\ f_{xx}<0$ → 극댓값 $4e^{-2}-1+3=4e^{-2}+2$"],
  check=_c)


def _c():
    f = 6*x**3 - 3*x**2*y + 9*x**2 + y**2 + 3*y
    sols = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    assert sorted((s_[x], s_[y]) for s_ in sols) == [(-1, 0), (0, R(-3, 2)), (3, 12)]
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    assert D.subs({x: 0, y: R(-3, 2)}) == 54 and f.subs({x: 0, y: R(-3, 2)}) == R(-9, 4)
    assert D.subs({x: -1, y: 0}) < 0 and D.subs({x: 3, y: 12}) < 0
P(id="3-63", ch=14, sec="14.7", type="14-crit", src="2022 중간(블럭1) 4번 유형",
  q=r"$f(x,y)=6x^3-3x^2y+9x^2+y^2+3y$의 극댓값, 극솟값, 안장점을 구하라.",
  hint=r"$f_y=0$에서 $y=\tfrac{3x^2-3}{2}$. $f_x=6x(3x-y+3)$이므로 $x=0$ 또는 $y=3x+3$",
  ans=r"$\left(0,-\tfrac32\right)$에서 극솟값 $-\dfrac94$,  안장점 $(-1,0)$, $(3,12)$ (극댓값 없음)",
  sol=[r"$f_x=18x^2-6xy+18x=6x(3x-y+3)$,  $f_y=-3x^2+2y+3$",
       r"$x=0$: $y=-\tfrac32$.  $y=3x+3$: $3x^2-3=6x+6 \Rightarrow x^2-2x-3=0 \Rightarrow x=3,-1$ → $(3,12),\ (-1,0)$",
       r"$f_{xx}=36x-6y+18,\ f_{yy}=2,\ f_{xy}=-6x$",
       r"$\left(0,-\tfrac32\right)$: $f_{xx}=27,\ D=54>0$ → 극솟값 $\tfrac94-\tfrac92=-\tfrac94$",
       r"$(-1,0)$: $f_{xx}=-18,\ D=-36-36<0$;  $(3,12)$: $f_{xx}=54,\ D=108-324<0$ → 둘 다 안장점"],
  check=_c)


def _c():
    uu = x**2 + y**2 - 2*x
    assert solve([diff(uu, x), diff(uu, y)], [x, y]) == {x: 1, y: 0} and uu.subs({x: 1, y: 0}) == -1
    b = (x**2 + y**2 - 2*x).subs(y**2, 4 - x**2)
    assert simplify(b - (4 - 2*x)) == 0
    assert uu.subs({x: -2, y: 0}) == 8
P(id="3-64", ch=14, sec="14.7", type="14-absext", src="2025 중간 7번 유형",
  q=r"$f(x,y)=e^{-(x^2+y^2-2x)}$의 원판 $D=\{(x,y)\mid x^2+y^2\le4\}$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"$e^{-u}$는 $u$에 대해 감소함수 → $u=x^2+y^2-2x=(x-1)^2+y^2-1$의 최솟값·최댓값을 찾으면 돼요.",
  ans=r"최댓값 $e$ (점 $(1,0)$),  최솟값 $e^{-8}$ (점 $(-2,0)$)",
  sol=[r"$u=(x-1)^2+y^2-1$: 점 $(1,0)$까지 거리의 제곱 $-1$",
       r"$u$의 최솟값: 내부 점 $(1,0)$에서 $-1$ → $f$의 최댓값 $e^{1}=e$",
       r"$u$의 최댓값: 경계 $x^2+y^2=4$에서 $u=4-2x$, $x=-2$일 때 $8$ (점 $(1,0)$에서 가장 먼 점 $(-2,0)$)",
       r"$f$의 최솟값 $e^{-8}$"],
  check=_c)


def _c():
    f = x**2*exp(-x) + y**2 - 4*y
    cands = {(0, 2): -4, (1, 2): exp(-1) - 4, (-1, 2): E - 4, (0, 1): -3, (0, 3): -3}
    for (a, b), val in cands.items():
        assert simplify(f.subs({x: a, y: b}) - val) == 0
    gfun = (2 - x)*exp(-x) - 2
    assert diff(gfun, x).subs(x, 0) < 0
P(id="3-65", ch=14, sec="14.7", type="14-absext", src="2022 중간(블럭2) 5(b) 유형",
  q=r"$f(x,y)=x^2e^{-x}+y^2-4y$의 영역 $D=\{(x,y)\mid x^2+(y-2)^2\le1\}$ 위에서의 최댓값과 최솟값을 구하라. (경계에서는 라그랑주 승수법)",
  hint=r"경계 $g=x^2+(y-2)^2=1$: $(2x-x^2)e^{-x}=2\lambda x$, $2y-4=2\lambda(y-2)$ → $y=2$ 또는 $\lambda=1$",
  ans=r"최댓값 $e-4$ (점 $(-1,2)$),  최솟값 $-4$ (점 $(0,2)$)",
  sol=[r"내부: $f_x=x(2-x)e^{-x}=0,\ f_y=2y-4=0$ → $(0,2)$ ($(2,2)$는 $D$ 밖), $f=-4$",
       r"경계, $y=2$: $x=\pm1$ → $f(1,2)=e^{-1}-4$, $f(-1,2)=e-4$",
       r"경계, $\lambda=1$: $(2-x)e^{-x}=2$ 또는 $x=0$ → $x=0$ ($(2-x)e^{-x}$는 감소, $x=0$에서 $2$) → $(0,1),(0,3)$, $f=-3$",
       r"비교: 최댓값 $e-4\approx-1.28$ (점 $(-1,2)$), 최솟값 $-4$ (점 $(0,2)$)"],
  check=_c)


def _c():
    d2 = (x - 2)**2 + (y - 1)**2 + (x + y - 1 + 1)**2
    sol = solve([diff(d2, x), diff(d2, y)], [x, y])
    assert sol == {x: 1, y: 0} and d2.subs(sol) == 3
    assert EQ(abs(2 + 1 - (-1) - 1)/sqrt(3), sqrt(3))
P(id="3-66", ch=14, sec="14.7", type="14-optim", src="복습 14.7–8 기초2 유형",
  q=r"점 $(2,1,-1)$에서 평면 $x+y-z=1$까지의 최단 거리를 극값 판정(편미분)으로 구하고, 점과 평면 사이 거리 공식과 비교하라.",
  hint=r"평면 위의 점 $(x,y,x+y-1)$까지 거리의 제곱 $d^2=(x-2)^2+(y-1)^2+(x+y)^2$을 최소화",
  ans=r"최단 거리 $\sqrt3$ (가장 가까운 점 $(1,0,0)$)",
  sol=[r"$d^2=(x-2)^2+(y-1)^2+(x+y)^2$",
       r"$\partial_x$: $2(x-2)+2(x+y)=0 \Rightarrow 2x+y=2$,  $\partial_y$: $2(y-1)+2(x+y)=0 \Rightarrow x+2y=1$",
       r"$x=1,\ y=0$ → 점 $(1,0,0)$, $d^2=1+1+1=3$, $d=\sqrt3$",
       r"공식: $\dfrac{|2+1+1-1|}{\sqrt3}=\dfrac{3}{\sqrt3}=\sqrt3$ ✓"],
  check=_c)


def _c():
    f = x**2 - x*y + y**2 - 3*y
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: 1, y: 2} and f.subs({x: 1, y: 2}) == -3
    cands = [(1, 2), (0, 0), (3, 0), (0, 3), (3, 3), (0, R(3, 2)), (R(3, 2), 3)]
    vals = [f.subs({x: a, y: b}) for a, b in cands]
    assert max(vals) == 9 and f.subs({x: 3, y: 0}) == 9 and min(vals) == -3
P(id="3-67", ch=14, sec="14.7", type="14-absext", src="복습 14.7–8 심화1 유형",
  q=r"$f(x,y)=x^2-xy+y^2-3y$의 정사각형 $D=[0,3]\times[0,3]$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"내부 임계점 $(1,2)$. 네 변을 한 변수 함수로: 예를 들어 $x=3$이면 $f=(y-3)^2$",
  ans=r"최댓값 $9$ (점 $(3,0)$),  최솟값 $-3$ (점 $(1,2)$)",
  sol=[r"내부: $f_x=2x-y=0,\ f_y=-x+2y-3=0$ → $(1,2)$, $f=-3$",
       r"$x=0$: $y^2-3y\in[-\tfrac94,0]$.  $x=3$: $(y-3)^2\in[0,9]$",
       r"$y=0$: $x^2\in[0,9]$.  $y=3$: $x^2-3x\in[-\tfrac94,0]$",
       r"최댓값 $9$ (점 $(3,0)$), 최솟값 $-3$ (점 $(1,2)$)"],
  check=_c)


# ───────── 14.8 ─────────
def _c():
    f = x**3 + y**3
    sols = solve([3*x**2 - 2*lam*x, 3*y**2 - 2*lam*y, x**2 + y**2 - 2], [x, y, lam], dict=True)
    vals = sorted(set(simplify(f.subs(s_)) for s_ in sols), key=float)
    assert vals == [-2*sqrt(2), -2, 2, 2*sqrt(2)]
P(id="3-68", ch=14, sec="14.8", type="14-lagrange", src="2022 중간(블럭1) 6번 유형",
  q=r"원 $x^2+y^2=2$ 위에서 $f(x,y)=x^3+y^3$의 최댓값과 최솟값을 라그랑주 승수법으로 구하라.",
  hint=r"$3x^2=2\lambda x,\ 3y^2=2\lambda y$. $x=0$, $y=0$, 둘 다 $0$이 아닌 경우를 모두 따져요.",
  ans=r"최댓값 $2\sqrt2$ (점 $(\sqrt2,0),(0,\sqrt2)$),  최솟값 $-2\sqrt2$ (점 $(-\sqrt2,0),(0,-\sqrt2)$)",
  sol=[r"$x=0$: $y=\pm\sqrt2$, $f=\pm2\sqrt2$.  $y=0$: $x=\pm\sqrt2$, $f=\pm2\sqrt2$",
       r"$x,y\ne0$: $3x=2\lambda=3y \Rightarrow x=y$ → $x^2=1$ → $(1,1),(-1,-1)$, $f=\pm2$",
       r"후보 값 $\pm2\sqrt2,\ \pm2$ 중 최댓값 $2\sqrt2$, 최솟값 $-2\sqrt2$"],
  check=_c)


def _c():
    a, b, c_ = symbols('a b c', positive=True)
    sols = solve([b*c_ - 2*lam*a, a*c_ - 4*lam*b, a*b - 8*lam*c_, a**2 + 2*b**2 + 4*c_**2 - 3], [a, b, c_, lam], dict=True)
    assert len(sols) == 1
    s0 = sols[0]
    assert EQ(s0[a], 1) and EQ(s0[b], 1/sqrt(2)) and EQ(s0[c_], R(1, 2))
    assert EQ(1/(6*s0[a]*s0[b]*s0[c_]), sqrt(2)/3)
P(id="3-69", ch=14, sec="14.8", type="14-lagrange", src="2024 중간 4번 유형",
  q=r"양수 $a,b,c$가 $a^2+2b^2+4c^2=3$을 만족한다. 평면 $ax+by+cz=1$과 세 좌표평면으로 둘러싸인 사면체의 부피의 최솟값을 라그랑주 승수법으로 구하라.",
  hint=r"절편은 $\tfrac1a,\tfrac1b,\tfrac1c$ → $V=\dfrac{1}{6abc}$. $V$ 최소 $\iff abc$ 최대",
  ans=r"$\dfrac{\sqrt2}{3}$ ($a=1,\ b=\tfrac{1}{\sqrt2},\ c=\tfrac12$일 때)",
  sol=[r"$V=\dfrac16\cdot\dfrac1a\cdot\dfrac1b\cdot\dfrac1c=\dfrac{1}{6abc}$ → $h=abc$를 최대화",
       r"$bc=2\lambda a,\ ac=4\lambda b,\ ab=8\lambda c$. 각각 $a,b,c$를 곱하면 $abc=2\lambda a^2=4\lambda b^2=8\lambda c^2$",
       r"→ $a^2=2b^2=4c^2$, 제약식에서 각 항이 $1$: $a=1,\ b=\tfrac{1}{\sqrt2},\ c=\tfrac12$",
       r"$abc=\dfrac{1}{2\sqrt2}$ → $V_{\min}=\dfrac{2\sqrt2}{6}=\dfrac{\sqrt2}{3}$"],
  check=_c)


def _c():
    f = x + 2*y + z
    sols = solve([1 - lam - mu*2*x, 2 + lam - mu*2*y, 1 - lam, x - y + z - 1, x**2 + y**2 - 1], [x, y, z, lam, mu], dict=True)
    vals = sorted(f.subs(s_) for s_ in sols)
    assert vals == [-2, 4]
P(id="3-70", ch=14, sec="14.8", type="14-lagrange2", src="2025 중간 8번 유형 (제약 2개)",
  q=r"평면 $x-y+z=1$과 원기둥 $x^2+y^2=1$의 교선 위에서 $f(x,y,z)=x+2y+z$의 최댓값과 최솟값을 구하라.",
  hint=r"$\nabla f=\lambda\nabla g+\mu\nabla h$: $\langle1,2,1\rangle=\lambda\langle1,-1,1\rangle+\mu\langle2x,2y,0\rangle$. $z$성분부터 보세요.",
  ans=r"최댓값 $4$ (점 $(0,1,2)$),  최솟값 $-2$ (점 $(0,-1,0)$)",
  sol=[r"$z$성분: $1=\lambda$. $x$성분: $1=\lambda+2\mu x \Rightarrow \mu x=0$",
       r"$y$성분: $2=-\lambda+2\mu y=-1+2\mu y \Rightarrow \mu y=\tfrac32$ → $\mu\ne0$ → $x=0$",
       r"$x=0$이면 $y=\pm1$, $z=1-x+y=1+y$ → $(0,1,2)$, $(0,-1,0)$",
       r"$f(0,1,2)=4$ (최대), $f(0,-1,0)=-2$ (최소)"],
  check=_c)


def _c():
    sols = solve([y*z - 2*lam*x, x*z - 2*lam*y, x*y - 2*lam*z, x**2 + y**2 + z**2 - 1], [x, y, z, lam], dict=True)
    vals = sorted(set(simplify(x*y*z).subs(s_) for s_ in sols), key=float)
    assert vals[0] == -sqrt(3)/9 and vals[-1] == sqrt(3)/9
P(id="3-71", ch=14, sec="14.8", type="14-lagrange", src="2022 생명과학대 기말 14번 유형",
  q=r"$f(x,y,z)=xyz$의 닫힌 구 $x^2+y^2+z^2\le1$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"내부 임계점 ($f_x=yz=0$ 등)에서는 $f=0$. 경계 구면에서 라그랑주: $yz=2\lambda x,\ xz=2\lambda y,\ xy=2\lambda z$",
  ans=r"최댓값 $\dfrac{\sqrt3}{9}$,  최솟값 $-\dfrac{\sqrt3}{9}$ ($x^2=y^2=z^2=\tfrac13$인 점들)",
  sol=[r"내부: $yz=xz=xy=0$ → 두 좌표 이상이 $0$ → $f=0$",
       r"경계: 세 식에 각각 $x,y,z$를 곱하면 $xyz=2\lambda x^2=2\lambda y^2=2\lambda z^2$",
       r"$xyz\ne0$인 경우 $x^2=y^2=z^2=\tfrac13$ → $f=\pm\dfrac{1}{3\sqrt3}=\pm\dfrac{\sqrt3}{9}$",
       r"최댓값 $\dfrac{\sqrt3}{9}$ (부호가 $+$인 점, 예: $(\tfrac1{\sqrt3},\tfrac1{\sqrt3},\tfrac1{\sqrt3})$), 최솟값 $-\dfrac{\sqrt3}{9}$"],
  check=_c)

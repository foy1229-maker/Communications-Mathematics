"""4단계 · 심화 추가분 — Ch.14 편도함수: 4-35 ~ 4-71, 미분가능성의 정의 4-121 ~ 4-123"""
from bank_lib import *
import mpmath as mp
from sympy import lambdify, Abs


def taylor2(x0, y0, val, fx, fy, fxx, fxy, fyy):
    """주어진 값·편도함수를 그 점에서 그대로 갖는 2차 다항식 (일반 f 대신 검산용)"""
    X, Y = x - x0, y - y0
    return val + fx*X + fy*Y + R(1, 2)*fxx*X**2 + fxy*X*Y + R(1, 2)*fyy*Y**2


# ───────── 14.1 ─────────
def _c():
    area = R(1, 2) * (3*pi/4 - pi/4) * (3 - 1)
    assert EQ(area, pi/2)
    assert EQ(integrate(r, (r, 1, sqrt(3)), (th, pi/4, 3*pi/4)), pi/2)
    best_max, best_min = -10.0, 10.0
    for i in range(0, 201):
        rr_ = 1 + (float(sqrt(3)) - 1) * i / 200
        for j in range(0, 201):
            tq = float(pi/4) + float(pi/2) * j / 200
            inner = rr_ * (mp.sin(tq) - abs(mp.cos(tq)))
            val = float(mp.asin(min(1.0, rr_**2 - 2)) + mp.sqrt(max(0.0, inner)))
            best_max = max(best_max, val); best_min = min(best_min, val)
    assert abs(best_min - float(-pi/2)) < 1e-9
    assert abs(best_max - float(pi/2 + 3**R(1, 4))) < 1e-6
P(id="4-35", ch=14, sec="14.1", type="14-domain", src="교재 14.1 심화형 (정의역 + 극좌표 넓이)",
  q=r"$f(x,y)=\sin^{-1}(x^2+y^2-2)+\sqrt{y-|x|}$에 대해<br>(a) $f$의 정의역 $D$를 구하고 그림으로 설명하라.  (b) $D$의 넓이를 구하라.  (c) $D$에서 $f$의 최솟값과 최댓값을 구하라.",
  hint=r"$\sin^{-1}u$는 $-1\le u\le1$에서만 정의되고 증가함수예요. 극좌표로 쓰면 $y-|x|=r(\sin\theta-|\cos\theta|)$.",
  ans=r"(a) $1\le x^2+y^2\le3$이고 $y\ge|x|$ (두 원 사이, $\tfrac\pi4\le\theta\le\tfrac{3\pi}4$인 부채꼴 띠)  (b) $\dfrac\pi2$  (c) 최솟값 $-\dfrac\pi2$ (점 $(\pm\tfrac{\sqrt2}{2},\tfrac{\sqrt2}{2})$), 최댓값 $\dfrac\pi2+\sqrt[4]3$ (점 $(0,\sqrt3)$)",
  sol=[r"(a) $-1\le x^2+y^2-2\le1 \iff 1\le x^2+y^2\le3$, 그리고 $y-|x|\ge0 \iff y\ge|x|$ → 반지름 $1$과 $\sqrt3$인 두 원 사이에서 두 반직선 $y=\pm x\ (y\ge0)$ 사이 부분",
       r"(b) 중심각 $\tfrac\pi2$인 부채꼴 띠: $\displaystyle\int_{\pi/4}^{3\pi/4}\!\!\int_1^{\sqrt3}r\,dr\,d\theta=\frac\pi2\cdot\frac{3-1}{2}=\frac\pi2$",
       r"(c) 극좌표로 $f=\sin^{-1}(r^2-2)+\sqrt{r(\sin\theta-|\cos\theta|)}$. 두 항 모두 $r$에 대해 증가하고 둘째 항 $\ge0$",
       r"최소: 첫 항 최소 $-\tfrac\pi2$ ($r=1$)이고 둘째 항 $0$ ($y=|x|$)이 동시에 되는 점 $(\pm\tfrac{\sqrt2}2,\tfrac{\sqrt2}2)$ → $-\tfrac\pi2$",
       r"최대: $r=\sqrt3$에서 첫 항 $\tfrac\pi2$, $\sin\theta-|\cos\theta|$는 $\theta=\tfrac\pi2$에서 최대 $1$ → $\tfrac\pi2+\sqrt{\sqrt3}=\tfrac\pi2+\sqrt[4]3$"],
  check=_c)


# ───────── 14.2 ─────────
def _c():
    N = sin(x)*sin(y) - x*y
    assert EQ(limit((N/(x**2 + y**2)).subs(y, x), x, 0), 0)
    assert EQ(limit((N/(x**4 + y**4)).subs(y, x), x, 0), R(-1, 6))
    assert simplify((N/(x**4 + y**4)).subs(y, 0)) == 0
    import random
    random.seed(1)
    for _ in range(300):
        a, b = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
        rr2 = a*a + b*b
        assert abs(mp.sin(a)*mp.sin(b) - a*b) <= rr2**2/3 + 1e-15
P(id="4-36", ch=14, sec="14.2", type="14-dne", src="2024 중간 3번 유형 (테일러 근사)",
  q=r"다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보여라.<br>(a) $\displaystyle\lim_{(x,y)\to(0,0)}\frac{\sin x\sin y-xy}{x^2+y^2}$  (b) $\displaystyle\lim_{(x,y)\to(0,0)}\frac{\sin x\sin y-xy}{x^4+y^4}$",
  hint=r"$|\sin u-u|\le\dfrac{|u|^3}{6}$이고 $\sin x\sin y-xy=(\sin x-x)\sin y+x(\sin y-y)$. 분자는 대략 $-\tfrac{xy(x^2+y^2)}{6}$ 정도로 $4$차예요.",
  ans=r"(a) $0$  (b) 존재하지 않는다 ($y=x$를 따라 $-\tfrac16$, $y=0$을 따라 $0$)",
  sol=[r"(a) $|\sin x\sin y-xy|\le|\sin x-x||\sin y|+|x||\sin y-y|\le\dfrac{|x|^3|y|}{6}+\dfrac{|x||y|^3}{6}\le\dfrac{r^4}{3}$  ($r^2=x^2+y^2$)",
       r"$\Big|\dfrac{\sin x\sin y-xy}{x^2+y^2}\Big|\le\dfrac{r^2}{3}\to0$ → 조임정리로 극한 $0$",
       r"(b) $y=0$: 분자 $=0$ → 극한 $0$",
       r"$y=x$: $\dfrac{\sin^2x-x^2}{2x^4}$, $\sin^2x=x^2-\tfrac{x^4}{3}+\cdots$ → $\dfrac{-x^4/3}{2x^4}\to-\dfrac16$",
       r"두 경로의 극한이 다르므로 (b)는 존재하지 않는다. 같은 분자라도 분모의 차수에 따라 결론이 달라져요."],
  check=_c)


def _c():
    N = cos(x*y)*cos(y) + sin(x*y)*sin(y) - 1
    assert simplify(expand_trig_safe(N) - (cos((x - 1)*y) - 1)) == 0
    u_ = symbols('u_', real=True)
    Nu = cos(u_*y) - 1
    assert EQ(limit((Nu/(u_**4 + y**4)).subs(u_, y), y, 0), R(-1, 4))
    assert simplify((Nu/(u_**4 + y**4)).subs(y, 0)) == 0
    import random
    random.seed(2)
    for _ in range(300):
        a, b = random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6)
        assert abs(mp.cos(a*b) - 1) <= (a*a + b*b)**2/8 + 1e-15


def expand_trig_safe(e):
    from sympy import expand_trig
    return expand_trig(e)


P(id="4-37", ch=14, sec="14.2", type="14-dne", src="2025 중간 3(b) 유형",
  q=r"다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보여라.<br>(a) $\displaystyle\lim_{(x,y)\to(1,0)}\frac{\cos(xy)\cos y+\sin(xy)\sin y-1}{(x-1)^4+y^4}$  (b) $\displaystyle\lim_{(x,y)\to(1,0)}\frac{\cos(xy)\cos y+\sin(xy)\sin y-1}{(x-1)^2+y^2}$",
  hint=r"$\cos A\cos B+\sin A\sin B=\cos(A-B)$ → 분자 $=\cos\big((x-1)y\big)-1$. $u=x-1$로 두면 원점 근처 문제가 돼요. $1-\cos w\approx\tfrac{w^2}{2}$.",
  ans=r"(a) 존재하지 않는다 ($u=y$를 따라 $-\tfrac14$, $y=0$을 따라 $0$)  (b) $0$",
  sol=[r"분자 $=\cos(xy-y)-1=\cos(uy)-1$ ($u=x-1$), $(x,y)\to(1,0) \iff (u,y)\to(0,0)$",
       r"(a) $y=0$: 분자 $=0$ → $0$.  $u=y$: $\dfrac{\cos(y^2)-1}{2y^4}\to\dfrac{-\tfrac12y^4}{2y^4}=-\dfrac14$ → 존재하지 않는다",
       r"(b) $|\cos w-1|\le\dfrac{w^2}{2}$ → $|\cos(uy)-1|\le\dfrac{u^2y^2}{2}\le\dfrac{(u^2+y^2)^2}{8}$  ($u^2y^2\le\tfrac{(u^2+y^2)^2}{4}$)",
       r"$\Big|\dfrac{\cos(uy)-1}{u^2+y^2}\Big|\le\dfrac{u^2+y^2}{8}\to0$ → 극한 $0$"],
  check=_c)


def _c():
    m = symbols('m', real=True, nonzero=True)
    f1 = x**3*y/(x**6 + y**2)
    assert limit(f1.subs(y, m*x), x, 0) == 0
    assert EQ(limit(f1.subs(y, x**3), x, 0), R(1, 2))
    f2 = x**3*y/(x**4 + y**2)
    import random
    random.seed(3)
    for _ in range(300):
        a, b = random.uniform(-1, 1), random.uniform(-1, 1)
        assert abs(a**3*b) / (a**4 + b**2) <= abs(a)/2 + 1e-15
    assert limit(f2.subs(y, x**2), x, 0) == 0
P(id="4-38", ch=14, sec="14.2", type="14-dne", src="교재 14.2 심화형 (곡선 경로 · 산술기하)",
  q=r"(a) $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3y}{x^6+y^2}$가 존재하지 않음을 보여라.<br>(b) $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3y}{x^4+y^2}$를 구하라.",
  hint=r"(a) 직선 $y=mx$로는 모두 $0$이 나와요. 분모의 두 항이 같은 차수가 되는 곡선 $y=x^3$을 써 보세요.  (b) 산술·기하 평균: $x^4+y^2\ge2x^2|y|$",
  ans=r"(a) $y=mx$를 따라 $0$, $y=x^3$을 따라 $\tfrac12$ → 존재하지 않는다  (b) $0$",
  sol=[r"(a) $y=mx$: $\dfrac{mx^4}{x^6+m^2x^2}=\dfrac{mx^2}{x^4+m^2}\to0$ ($m=0$이나 $x=0$ 축 위에서도 $0$)",
       r"$y=x^3$: $\dfrac{x^6}{x^6+x^6}=\dfrac12$ → 경로마다 극한이 달라 존재하지 않는다",
       r"(b) $xy\ne0$일 때 $x^4+y^2\ge2x^2|y|$이므로 $\Big|\dfrac{x^3y}{x^4+y^2}\Big|\le\dfrac{|x|^3|y|}{2x^2|y|}=\dfrac{|x|}{2}$ ($xy=0$이면 값이 $0$)",
       r"$\dfrac{|x|}{2}\to0$ → 조임정리로 극한 $0$"],
  check=_c)


def _c():
    al = symbols('alpha', positive=True)
    g1 = Abs_safe(x*y)/(x**2 + y**2)
    assert EQ(limit((x*x)/(2*x**2), x, 0), R(1, 2))
    assert limit(((x**2)**R(1, 2))/(2*x**2), x, 0, '+') == oo
    for a_ in (R(3, 2), 2, 3):
        # r^(2a-2) |cos sin|^a <= r^(2a-2) -> 0
        assert 2*a_ - 2 > 0
    assert limit((x**2)**R(1, 3)/(2*x**2), x, 0, '+') == oo


def Abs_safe(e):
    from sympy import Abs
    return Abs(e)


P(id="4-39", ch=14, sec="14.2", type="14-limit", src="교재 14.2 심화형 (지수에 따른 판정)",
  q=r"양수 $\alpha$에 대해 $\displaystyle\lim_{(x,y)\to(0,0)}\frac{|xy|^{\alpha}}{x^2+y^2}$가 존재하도록 하는 $\alpha$의 범위와 그때의 극한값을 구하라.",
  hint=r"극좌표: $\dfrac{|xy|^\alpha}{x^2+y^2}=r^{2\alpha-2}\,|\cos\theta\sin\theta|^\alpha$. $r$의 지수 $2\alpha-2$의 부호로 나눠 보세요.",
  ans=r"$\alpha>1$일 때만 존재하고 극한값은 $0$",
  sol=[r"$x=r\cos\theta,\ y=r\sin\theta$: 식 $=r^{2\alpha-2}|\cos\theta\sin\theta|^\alpha$",
       r"$\alpha>1$: $0\le r^{2\alpha-2}|\cos\theta\sin\theta|^\alpha\le r^{2\alpha-2}\to0$ → 극한 $0$",
       r"$\alpha=1$: $y=x$를 따라 $\dfrac{x^2}{2x^2}=\dfrac12$, $y=0$을 따라 $0$ → 존재하지 않음",
       r"$0<\alpha<1$: $y=x$를 따라 $\dfrac{x^{2\alpha}}{2x^2}=\dfrac{1}{2x^{2-2\alpha}}\to\infty$ → 존재하지 않음",
       r"따라서 $\alpha>1$일 때만 극한이 존재하고 값은 $0$"],
  check=_c)


def _c():
    tq = symbols('tq', positive=True)
    f1 = (x*y + y*z + z*x)/(x**2 + y**2 + z**2)
    assert EQ(limit(f1.subs({y: x, z: x}), x, 0), 1)
    assert simplify(f1.subs({y: 0, z: 0})) == 0
    assert limit(tq**2*exp(-tq), tq, oo) == 0
    s_ = symbols('s_', positive=True)
    assert limit(exp(-1/s_)/s_**2, s_, 0, '+') == 0
P(id="4-40", ch=14, sec="14.2", type="14-limit", src="2022 중간 블럭1 1(b) 유형 (3변수)",
  q=r"다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보여라.<br>(a) $\displaystyle\lim_{(x,y,z)\to(0,0,0)}\frac{xy+yz+zx}{x^2+y^2+z^2}$  (b) $\displaystyle\lim_{(x,y,z)\to(0,0,0)}\frac{e^{-1/(x^2+y^2+z^2)}}{(x^2+y^2+z^2)^2}$",
  hint=r"(a) 좌표축 위와 직선 $x=y=z$ 위를 비교.  (b) $s=x^2+y^2+z^2\to0^+$인 1변수 극한이에요. $t=\tfrac1s$로 바꾸면 $\displaystyle\lim_{t\to\infty}t^2e^{-t}$.",
  ans=r"(a) 존재하지 않는다 ($x$축을 따라 $0$, $x=y=z$를 따라 $1$)  (b) $0$",
  sol=[r"(a) $x$축 ($y=z=0$): $\dfrac{0}{x^2}=0$",
       r"$x=y=z=t$: $\dfrac{3t^2}{3t^2}=1$ → 다른 값 → 존재하지 않는다",
       r"(b) 식은 $s=x^2+y^2+z^2$만의 함수 $\dfrac{e^{-1/s}}{s^2}$이고 $(x,y,z)\to\mathbf 0 \iff s\to0^+$",
       r"$t=\tfrac1s\to\infty$: $\dfrac{e^{-t}}{t^{-2}}=t^2e^{-t}=\dfrac{t^2}{e^t}\to0$ (로피탈 두 번) → 극한 $0$"],
  check=_c)


def _c():
    m = symbols('m', real=True, nonzero=True)
    f = x**4*y**4/(x**2 + y**4)**3
    assert limit(f.subs(y, m*x), x, 0) == 0
    assert simplify(f.subs(x, 0)) == 0 and simplify(f.subs(y, 0)) == 0
    assert EQ(limit(f.subs(x, y**2), y, 0), R(1, 8))
P(id="4-41", ch=14, sec="14.2", type="14-dne", src="교재 14.2 심화형 (모든 직선 → 0이지만 발산)",
  q=r"$f(x,y)=\dfrac{x^4y^4}{(x^2+y^4)^3}$에 대해<br>(a) 원점을 지나는 모든 직선을 따라 $(x,y)\to(0,0)$일 때 $f\to0$임을 보여라.  (b) 그럼에도 $\displaystyle\lim_{(x,y)\to(0,0)}f(x,y)$가 존재하지 않음을 보여라.",
  hint=r"분모의 $x^2$과 $y^4$이 같은 크기가 되는 곡선 $x=y^2$을 따라가 보세요.",
  ans=r"(a) $y=mx$를 따라 $\dfrac{m^4x^2}{(1+m^4x^2)^3}\to0$, 두 축 위에서도 $0$  (b) $x=y^2$을 따라 $\tfrac18$ → 존재하지 않는다",
  sol=[r"(a) $y=mx$: $\dfrac{m^4x^8}{(x^2+m^4x^4)^3}=\dfrac{m^4x^8}{x^6(1+m^4x^2)^3}=\dfrac{m^4x^2}{(1+m^4x^2)^3}\to0$",
       r"축 $x=0$ 또는 $y=0$ 위에서는 $f=0$ → 모든 직선에서 극한 $0$",
       r"(b) $x=y^2$: $\dfrac{y^8\cdot y^4}{(y^4+y^4)^3}=\dfrac{y^{12}}{8y^{12}}=\dfrac18$",
       r"$\tfrac18\ne0$ → 극한은 존재하지 않는다. 직선만 확인하는 것으로는 존재를 증명할 수 없다는 대표 예예요."],
  check=_c)


# ───────── 14.3 ─────────
def _c():
    f = x*y*(x**2 - y**2)/(x**2 + y**2)
    fx = simplify(diff(f, x))
    assert simplify(fx - y*(x**4 + 4*x**2*y**2 - y**4)/(x**2 + y**2)**2) == 0
    hh = symbols('hh', nonzero=True)
    assert simplify((f.subs({x: hh, y: 0}) - 0)/hh) == 0
    assert simplify(limit((f.subs(x, hh) - 0)/hh, hh, 0) + y) == 0
    assert simplify(limit((f.subs(y, hh) - 0)/hh, hh, 0) - x) == 0
P(id="4-42", ch=14, sec="14.3", type="14-defpartial", src="교재 14.3 심화형 (클레로 정리가 성립하지 않는 예)",
  q=r"$f(x,y)=\begin{cases}\dfrac{xy(x^2-y^2)}{x^2+y^2} & (x,y)\ne(0,0)\\[2mm] 0 & (x,y)=(0,0)\end{cases}$에 대해<br>(a) 모든 $y$에 대해 $f_x(0,y)=-y$, 모든 $x$에 대해 $f_y(x,0)=x$임을 보여라.  (b) $f_{xy}(0,0)$과 $f_{yx}(0,0)$을 구하라.  (c) (b)의 결과가 클레로 정리와 모순되지 않는 이유를 설명하라.",
  hint=r"$f_x(0,y)=\displaystyle\lim_{h\to0}\frac{f(h,y)-f(0,y)}{h}$를 정의로 계산하세요. $f_{xy}=(f_x)_y$이므로 $f_{xy}(0,0)=\dfrac{d}{dy}f_x(0,y)\Big|_{y=0}$.",
  ans=r"(b) $f_{xy}(0,0)=-1$, $f_{yx}(0,0)=1$  (c) $f_{xy}$가 원점에서 연속이 아니어서 클레로 정리의 가정이 깨짐",
  sol=[r"(a) $y\ne0$: $f(0,y)=0$, $f_x(0,y)=\displaystyle\lim_{h\to0}\frac{1}{h}\cdot\frac{hy(h^2-y^2)}{h^2+y^2}=\frac{y(-y^2)}{y^2}=-y$",
       r"$y=0$: $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{f(h,0)-0}{h}=0=-0$ → 모든 $y$에서 $f_x(0,y)=-y$",
       r"같은 방법으로 $f_y(x,0)=\displaystyle\lim_{k\to0}\frac1k\cdot\frac{xk(x^2-k^2)}{x^2+k^2}=x$",
       r"(b) $f_{xy}(0,0)=\dfrac{\partial}{\partial y}\big(f_x(0,y)\big)\Big|_{y=0}=-1$,  $f_{yx}(0,0)=\dfrac{\partial}{\partial x}\big(f_y(x,0)\big)\Big|_{x=0}=1$",
       r"(c) 클레로 정리는 $f_{xy},f_{yx}$가 그 점 근방에서 연속일 때 성립. 여기서는 원점에서 연속이 아니므로 두 값이 달라도 모순이 아니에요."],
  check=_c)


def _c():
    Z = Function('Z')(x, y)
    F = Z**3 + x*Z - y
    zx = -diff(F, x)/diff(F, Z)
    zy = -diff(F, y)/diff(F, Z)
    pt = {x: 1, y: 2}
    assert EQ((1**3 + 1*1 - 2), 0)
    zx_v = zx.subs(Z, 1).subs(pt); zy_v = zy.subs(Z, 1).subs(pt)
    assert EQ(zx_v, R(-1, 4)) and EQ(zy_v, R(1, 4))
    # 2계: z_x = -z/(3z^2+x) 를 다시 미분 (z_x, z_y 대입)
    zs = symbols('zs'); zxs, zys = symbols('zxs zys')
    g = -zs/(3*zs**2 + x)
    gx = diff(g, x) + diff(g, zs)*zxs
    gy = diff(g, zs)*zys
    vals = {zs: 1, x: 1, zxs: R(-1, 4), zys: R(1, 4)}
    assert EQ(gx.subs(vals), R(1, 32)) and EQ(gy.subs(vals), R(1, 32))
    h = 1/(3*zs**2 + x)
    assert EQ((diff(h, zs)*zys).subs(vals), R(-3, 32))
    # 수치 확인: 실제 z(x,y)를 뉴턴법으로 풀어 2계 차분
    def zfun(a, b):
        return mp.findroot(lambda q: q**3 + a*q - b, 1)
    mp.mp.dps = 30
    hstep = mp.mpf('1e-6')
    zxx_num = (zfun(1 + hstep, 2) - 2*zfun(1, 2) + zfun(1 - hstep, 2)) / hstep**2
    assert abs(zxx_num - mp.mpf(1)/32) < 1e-6
    mp.mp.dps = 15
P(id="4-43", ch=14, sec="14.3", type="14-implicit", src="2024 중간 1(b) 확장 (2계 음함수 미분)",
  q=r"방정식 $z^3+xz-y=0$이 점 $(1,2,1)$ 근처에서 $z$를 $x,y$의 함수로 정한다.<br>(a) 점 $(x,y)=(1,2)$에서 $z_x,\ z_y$를 구하라.  (b) 같은 점에서 $z_{xx},\ z_{xy},\ z_{yy}$를 구하라.",
  hint=r"$z_x=-\dfrac{F_x}{F_z}=-\dfrac{z}{3z^2+x}$, $z_y=\dfrac{1}{3z^2+x}$. 2계는 이 식을 다시 미분하되 $z$도 $x,y$의 함수임을 잊지 마세요.",
  ans=r"(a) $z_x=-\dfrac14,\ z_y=\dfrac14$  (b) $z_{xx}=\dfrac1{32},\ z_{xy}=\dfrac1{32},\ z_{yy}=-\dfrac3{32}$",
  sol=[r"$F=z^3+xz-y$: $F_x=z,\ F_y=-1,\ F_z=3z^2+x$ → 점에서 $F_z=4$",
       r"(a) $z_x=-\dfrac{z}{3z^2+x}=-\dfrac14$,  $z_y=\dfrac{1}{3z^2+x}=\dfrac14$",
       r"(b) $z_{xx}=-\dfrac{z_x(3z^2+x)-z(6zz_x+1)}{(3z^2+x)^2}=-\dfrac{(-\tfrac14)(4)-1\cdot(-\tfrac32+1)}{16}=-\dfrac{-\tfrac12}{16}=\dfrac1{32}$",
       r"$z_{xy}=\dfrac{\partial}{\partial y}\Big(-\dfrac{z}{3z^2+x}\Big)=-\dfrac{z_y(3z^2+x)-z\cdot6zz_y}{(3z^2+x)^2}=-\dfrac{1-\tfrac32}{16}=\dfrac1{32}$",
       r"$z_{yy}=\dfrac{\partial}{\partial y}\Big(\dfrac{1}{3z^2+x}\Big)=-\dfrac{6zz_y}{(3z^2+x)^2}=-\dfrac{3/2}{16}=-\dfrac3{32}$"],
  check=_c)


def _c():
    k = symbols('k', real=True)
    u = (x**2 + y**2 + z**2)**k
    lap = diff(u, x, 2) + diff(u, y, 2) + diff(u, z, 2)
    target = 2*k*(2*k + 1)*(x**2 + y**2 + z**2)**(k - 1)
    for vals in ({x: 1, y: 2, z: -1, k: R(3, 7)}, {x: R(1, 2), y: -3, z: 2, k: -R(5, 3)}, {x: 2, y: 1, z: 1, k: 3}):
        assert EQ(lap.subs(vals), target.subs(vals))
    assert set(solve(2*k*(2*k + 1), k)) == {0, R(-1, 2)}
    tp = symbols('tp', positive=True); kk = symbols('kk', positive=True)
    U = exp(-x**2/(4*kk*tp))/sqrt(tp)
    res = simplify((diff(U, tp) - diff(U, x, 2))/U)
    assert simplify(res.subs(kk, 1)) == 0
    assert solve(res.subs(x, 0), kk) == [1]
P(id="4-44", ch=14, sec="14.3", type="14-higher", src="교재 14.3 심화형 (라플라스·열방정식)",
  q=r"(a) $u=(x^2+y^2+z^2)^k$가 3차원 라플라스 방정식 $u_{xx}+u_{yy}+u_{zz}=0$을 만족하도록 하는 상수 $k$를 모두 구하라.<br>(b) $u(x,t)=\dfrac{1}{\sqrt t}\,e^{-x^2/(4kt)}$ ($t>0$, $k>0$)이 열방정식 $u_t=u_{xx}$를 만족하도록 하는 $k$를 구하라.",
  hint=r"(a) $s=x^2+y^2+z^2$로 두면 $u_x=2kx\,s^{k-1}$, $u_{xx}=2ks^{k-1}+4k(k-1)x^2s^{k-2}$. (b) $u_t,\ u_{xx}$를 각각 $u\times(\cdots)$ 꼴로 정리해 비교.",
  ans=r"(a) $k=0$ 또는 $k=-\dfrac12$  (b) $k=1$",
  sol=[r"(a) $u_{xx}=2ks^{k-1}+4k(k-1)x^2s^{k-2}$, $y,z$도 같은 꼴",
       r"합: $6ks^{k-1}+4k(k-1)(x^2+y^2+z^2)s^{k-2}=(4k^2+2k)s^{k-1}=2k(2k+1)s^{k-1}$",
       r"$=0$이려면 $k=0$ 또는 $k=-\tfrac12$ (즉 상수함수 또는 $u=\dfrac{1}{\sqrt{x^2+y^2+z^2}}$)",
       r"(b) $u_t=u\Big(-\dfrac{1}{2t}+\dfrac{x^2}{4kt^2}\Big)$,  $u_x=-\dfrac{x}{2kt}u$,  $u_{xx}=u\Big(-\dfrac{1}{2kt}+\dfrac{x^2}{4k^2t^2}\Big)$",
       r"모든 $x,t$에서 같으려면 $\dfrac1{2t}=\dfrac1{2kt}$, $\dfrac{1}{4k}=\dfrac{1}{4k^2}$ → $k=1$"],
  check=_c)


def _c():
    fx_, fy_ = 3, -1
    n = Matrix([1, 0, fx_]).cross(Matrix([0, 1, fy_]))
    assert EQ(n, [-3, 1, 1])
    plane = 5 + fx_*(x - 1) + fy_*(y - 2)
    assert EQ(expand(plane), 3*x - y + 4)
    assert EQ(R(3, 5)*fx_ + R(4, 5)*fy_, 1)
    assert EQ(plane.subs({x: R(11, 10), y: R(19, 10)}), R(27, 5))
P(id="4-45", ch=14, sec="14.3", type="14-partial", src="강의 14.3 편도함수의 기하적 의미 응용",
  q=r"미분가능한 함수 $z=f(x,y)$의 그래프와 평면 $y=2$의 교선은 점 $(1,2,5)$에서 접선의 기울기가 $3$이고, 평면 $x=1$과의 교선은 같은 점에서 접선의 기울기가 $-1$이다.<br>(a) $f_x(1,2),\ f_y(1,2)$를 구하라.  (b) 점 $(1,2,5)$에서의 접평면을 구하라.  (c) $(1,2)$에서 $\langle3,4\rangle$ 방향의 방향도함수를 구하라.  (d) $f(1.1,\ 1.9)$의 근삿값을 구하라.",
  hint=r"평면 $y=2$와의 교선의 기울기 = $y$를 고정하고 $x$로 미분한 값 = $f_x$. 두 교선의 접벡터 $\langle1,0,f_x\rangle$, $\langle0,1,f_y\rangle$가 접평면을 펼쳐요.",
  ans=r"(a) $f_x=3,\ f_y=-1$  (b) $z=3x-y+4$  (c) $1$  (d) $5.4$",
  sol=[r"(a) $y=2$ 단면의 기울기 $=f_x(1,2)=3$, $x=1$ 단면의 기울기 $=f_y(1,2)=-1$",
       r"(b) $z-5=3(x-1)-(y-2)$ → $z=3x-y+4$ (법선 $\langle1,0,3\rangle\times\langle0,1,-1\rangle=\langle-3,1,1\rangle$과도 일치)",
       r"(c) $\mathbf u=\langle\tfrac35,\tfrac45\rangle$: $D_{\mathbf u}f=3\cdot\tfrac35-1\cdot\tfrac45=1$",
       r"(d) $f(1.1,1.9)\approx5+3(0.1)-1(-0.1)=5.4$"],
  check=_c)


# ───────── 14.4 ─────────
def _c():
    f = x**2*y/(x**2 + y**2)
    hh = symbols('hh', nonzero=True)
    assert limit(f.subs({x: hh, y: 0})/hh, hh, 0) == 0
    assert limit(f.subs({x: 0, y: hh})/hh, hh, 0) == 0
    Du = limit(f.subs({x: hh/sqrt(2), y: hh/sqrt(2)})/hh, hh, 0)
    assert EQ(Du, sqrt(2)/4)
    tq = symbols('tq', real=True)
    gen = simplify(f.subs({x: hh*cos(tq), y: hh*sin(tq)})/hh)
    assert simplify(gen - cos(tq)**2*sin(tq)) == 0
P(id="4-46", ch=14, sec="14.4", type="14-defpartial", src="교재 14.4 심화형 (미분가능성 판정)",
  q=r"$f(x,y)=\begin{cases}\dfrac{x^2y}{x^2+y^2} & (x,y)\ne(0,0)\\[2mm] 0 & (x,y)=(0,0)\end{cases}$에 대해<br>(a) $f$가 원점에서 연속임을 보여라.  (b) $f_x(0,0),\ f_y(0,0)$을 구하라.  (c) $\mathbf u=\big\langle\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big\rangle$ 방향의 방향도함수 $D_{\mathbf u}f(0,0)$을 정의로 구하라.  (d) $f$가 원점에서 미분가능하지 않음을 보여라.",
  hint=r"$D_{\mathbf u}f(0,0)=\displaystyle\lim_{h\to0}\frac{f(hu_1,hu_2)-f(0,0)}{h}$. 미분가능하다면 반드시 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$여야 해요.",
  ans=r"(a) $|f|\le|y|\to0$  (b) $0,\ 0$  (c) $\dfrac{\sqrt2}{4}$  (d) $\nabla f(0,0)\cdot\mathbf u=0\ne\dfrac{\sqrt2}4$",
  sol=[r"(a) $\dfrac{x^2}{x^2+y^2}\le1$ → $|f(x,y)|\le|y|\to0=f(0,0)$ → 연속",
       r"(b) $f(h,0)=0,\ f(0,h)=0$ → $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{0-0}{h}=0$, $f_y(0,0)=0$",
       r"(c) $f\big(\tfrac{h}{\sqrt2},\tfrac{h}{\sqrt2}\big)=\dfrac{\tfrac{h^2}{2}\cdot\tfrac{h}{\sqrt2}}{h^2}=\dfrac{h}{2\sqrt2}$ → $D_{\mathbf u}f(0,0)=\dfrac{1}{2\sqrt2}=\dfrac{\sqrt2}{4}$",
       r"(일반 방향 $\langle\cos\theta,\sin\theta\rangle$이면 $D_{\mathbf u}f(0,0)=\cos^2\theta\sin\theta$)",
       r"(d) 미분가능하면 $D_{\mathbf u}f(0,0)=\nabla f(0,0)\cdot\mathbf u=0$이어야 하는데 $\tfrac{\sqrt2}{4}\ne0$ → 미분가능하지 않다. 연속이고 편도함수가 있어도 미분가능하지 않을 수 있어요."],
  check=_c)


def _c():
    a, b = symbols('a b', real=True)
    T = a**2 + b**2 + 2*a*(x - a) + 2*b*(y - b)
    assert EQ(expand(T), expand(2*a*x + 2*b*y - (a**2 + b**2)))
    assert EQ(T.subs({x: 0, y: 0}), -(a**2 + b**2))
    c = symbols('c', positive=True)
    f = sqrt(x**2 + y**2)
    pa, pb = symbols('pa pb', positive=True)
    cc = sqrt(pa**2 + pb**2)
    Tc = cc + diff(f, x).subs({x: pa, y: pb})*(x - pa) + diff(f, y).subs({x: pa, y: pb})*(y - pb)
    assert simplify(Tc.subs({x: 0, y: 0})) == 0
P(id="4-47", ch=14, sec="14.4", type="14-tangent", src="교재 14.4 심화형 (접평면의 자취)",
  q=r"(a) 포물면 $z=x^2+y^2$ 위의 점 $(a,b,a^2+b^2)$에서 접평면의 방정식을 구하라.<br>(b) 점 $(0,0,-4)$를 지나는 포물면의 접평면들의 접점은 어떤 곡선 위에 있는가?<br>(c) 원뿔 $z=\sqrt{x^2+y^2}$ 위의 (원점이 아닌) 모든 점에서의 접평면이 원점을 지남을 보여라.",
  hint=r"$z=f(x,y)$의 접평면: $z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$. (b)는 이 식에 $(0,0,-4)$를 대입한 조건이에요.",
  ans=r"(a) $z=2ax+2by-(a^2+b^2)$  (b) 원 $x^2+y^2=4,\ z=4$  (c) 접평면이 $z=\dfrac{ax+by}{\sqrt{a^2+b^2}}$ 꼴 → 원점을 지남",
  sol=[r"(a) $f_x=2x,\ f_y=2y$ → $z=a^2+b^2+2a(x-a)+2b(y-b)=2ax+2by-(a^2+b^2)$",
       r"(b) $(0,0,-4)$ 대입: $-4=-(a^2+b^2)$ → $a^2+b^2=4$, 접점의 높이 $z=a^2+b^2=4$ → 원 $x^2+y^2=4,\ z=4$ 위",
       r"(c) $f=\sqrt{x^2+y^2}$, 점 $(a,b,c)$ ($c=\sqrt{a^2+b^2}$)에서 $f_x=\tfrac ac,\ f_y=\tfrac bc$",
       r"접평면 $z=c+\tfrac ac(x-a)+\tfrac bc(y-b)=\dfrac{ax+by}{c}+c-\dfrac{a^2+b^2}{c}=\dfrac{ax+by}{c}$ → $(0,0,0)$ 대입 시 성립"],
  check=_c)


def _c():
    a, b, C = symbols('a b C', positive=True)
    A = R(1, 2)*a*b*sin(C)
    vals = {a: 10, b: 15, C: pi/6}
    dA = (abs(diff(A, a).subs(vals))*R(1, 10) + abs(diff(A, b).subs(vals))*R(1, 10)
          + abs(diff(A, C).subs(vals))*pi/180)
    assert EQ(dA, R(5, 8) + 5*sqrt(3)*pi/24)
    assert abs(float(dA) - 1.7586) < 1e-3 and EQ(A.subs(vals), R(75, 2))
P(id="4-48", ch=14, sec="14.4", type="14-diff", src="교재 14.4 심화형 (전미분 오차 · 각도 단위)",
  q=r"삼각형의 두 변의 길이를 재었더니 $a=10$ cm, $b=15$ cm이고 그 끼인각은 $C=30^\circ$였다. 길이의 측정 오차는 각각 최대 $0.1$ cm, 각의 측정 오차는 최대 $1^\circ$이다. 넓이 $A=\tfrac12ab\sin C$의 최대 오차를 전미분으로 추정하라.",
  hint=r"$dA=A_a\,da+A_b\,db+A_C\,dC$에서 각의 오차는 반드시 라디안으로: $1^\circ=\dfrac{\pi}{180}$.",
  ans=r"$|dA|\le\dfrac58+\dfrac{5\sqrt3\pi}{24}\approx1.76\ \mathrm{cm^2}$ (넓이 $37.5\ \mathrm{cm^2}$의 약 $4.7\%$)",
  sol=[r"$A_a=\tfrac12b\sin C=\tfrac{15}{4}$, $A_b=\tfrac12a\sin C=\tfrac{10}{4}$, $A_C=\tfrac12ab\cos C=75\cdot\tfrac{\sqrt3}{2}$",
       r"$|da|,|db|\le0.1$, $|dC|\le\tfrac{\pi}{180}$ (라디안!)",
       r"$|dA|\le\tfrac{15}{4}(0.1)+\tfrac{10}{4}(0.1)+\tfrac{75\sqrt3}{2}\cdot\tfrac{\pi}{180}=0.375+0.25+\dfrac{5\sqrt3\pi}{24}$",
       r"$=\dfrac58+\dfrac{5\sqrt3\pi}{24}\approx0.625+1.134\approx1.76\ \mathrm{cm^2}$  ($A=\tfrac12\cdot150\cdot\tfrac12=37.5$)",
       r"각도 오차를 $1$로 두고 계산하면 엉뚱하게 큰 값이 나오니 주의!"],
  check=_c)


def _c():
    f = taylor2(3, 2, 3, 1, 2, 5, -1, 4)
    g = f.subs({x: u + v, y: u*v}, simultaneous=True)
    pt = {u: 1, v: 2}
    assert EQ(g.subs(pt), 3) and EQ(diff(g, u).subs(pt), 5) and EQ(diff(g, v).subs(pt), 3)
    plane = 3 + 5*(u - 1) + 3*(v - 2)
    assert EQ(expand(plane), 5*u + 3*v - 8)
    assert EQ(plane.subs({u: R(11, 10), v: R(19, 10)}), R(16, 5))
P(id="4-49", ch=14, sec="14.4", type="14-tangent", src="2022 중간 블럭1 3번 유형 (연쇄법칙 + 접평면)",
  q=r"미분가능한 함수 $z=f(x,y)$의 그래프의 점 $(3,2,f(3,2))$에서의 접평면이 $x+2y-z=4$이다. $g(u,v)=f(u+v,\ uv)$라 할 때<br>(a) $f(3,2),\ f_x(3,2),\ f_y(3,2)$를 구하라.  (b) 곡면 $z=g(u,v)$의 점 $(1,2,g(1,2))$에서의 접평면을 구하라.  (c) $g(1.1,\ 1.9)$의 근삿값을 구하라.",
  hint=r"접평면 $z=x+2y-4$에서 기울기가 곧 $f_x,f_y$. $(u,v)=(1,2)$이면 $(x,y)=(u+v,uv)=(3,2)$이고 $g_u=f_x\cdot1+f_y\cdot v$.",
  ans=r"(a) $3,\ 1,\ 2$  (b) $z=5u+3v-8$  (c) $3.2$",
  sol=[r"(a) $z=x+2y-4$ → $f(3,2)=3+4-4=3$, $f_x(3,2)=1$, $f_y(3,2)=2$",
       r"(b) $g_u=f_x\,x_u+f_y\,y_u=f_x+v f_y$, $g_v=f_x+u f_y$ → $(1,2)$에서 $g_u=1+2\cdot2=5$, $g_v=1+1\cdot2=3$, $g(1,2)=f(3,2)=3$",
       r"접평면: $z=3+5(u-1)+3(v-2)=5u+3v-8$",
       r"(c) $g(1.1,1.9)\approx3+5(0.1)+3(-0.1)=3.2$"],
  check=_c)


# ───────── 14.5 ─────────
def _c():
    f = taylor2(2, 3, 0, 1, -1, 2, -1, 3)
    g = f.subs({x: s*t, y: s**2 - t**2}, simultaneous=True)
    pt = {s: 2, t: 1}
    assert EQ(diff(g, s).subs(pt), -3) and EQ(diff(g, s, 2).subs(pt), 40)
    sp_, tp_ = symbols('sp_ tp_', positive=True)
    F = sin(x)*y**2 + exp(x*y/5)
    G = F.subs({x: sp_*tp_, y: sp_**2 - tp_**2}, simultaneous=True)
    lhs = tp_*diff(G, sp_) + sp_*diff(G, tp_)
    hx = sqrt(4*x**2 + y**2) * diff(F, x)
    rhs = hx.subs({x: sp_*tp_, y: sp_**2 - tp_**2}, simultaneous=True)
    for vals in ({sp_: 2, tp_: 1}, {sp_: R(3, 2), tp_: R(1, 3)}):
        assert EQ(lhs.subs(vals), rhs.subs(vals))
P(id="4-50", ch=14, sec="14.5", type="14-chain2", src="2022 중간 블럭2 4번 유형",
  q=r"$f$는 2계 편도함수가 연속인 $x,y$의 함수이고 $g(s,t)=f\big(st,\ s^2-t^2\big)$이다. $f_x(2,3)=1,\ f_y(2,3)=-1,\ f_{xx}(2,3)=2,\ f_{xy}(2,3)=-1,\ f_{yy}(2,3)=3$일 때<br>(a) $g_s(2,1)$과 $g_{ss}(2,1)$을 구하라.  (b) $s>0,\ t>0$에서 $t\,\dfrac{\partial g}{\partial s}+s\,\dfrac{\partial g}{\partial t}=h(x,y)\,\dfrac{\partial f}{\partial x}$를 만족하는 함수 $h(x,y)$를 구하라.",
  hint=r"$x=st,\ y=s^2-t^2$: $x_s=t,\ y_s=2s$. $g_s=t\,f_x+2s\,f_y$를 다시 $s$로 미분할 때 $f_x,f_y$ 안에도 $s$가 숨어 있어요. (b)에서는 $(s^2+t^2)^2=(s^2-t^2)^2+4s^2t^2$.",
  ans=r"(a) $g_s(2,1)=-3,\ g_{ss}(2,1)=40$  (b) $h(x,y)=\sqrt{4x^2+y^2}$",
  sol=[r"$(s,t)=(2,1)$ ↔ $(x,y)=(2,3)$, $x_s=t=1,\ y_s=2s=4$",
       r"(a) $g_s=t\,f_x+2s\,f_y=1\cdot1+4\cdot(-1)=-3$",
       r"$g_{ss}=t\,(f_{xx}x_s+f_{xy}y_s)+2f_y+2s\,(f_{yx}x_s+f_{yy}y_s)=1\cdot(2-4)+2(-1)+4\cdot(-1+12)=40$",
       r"(b) $g_t=s\,f_x-2t\,f_y$ → $t\,g_s+s\,g_t=t^2f_x+2st\,f_y+s^2f_x-2st\,f_y=(s^2+t^2)f_x$",
       r"$(s^2+t^2)^2=(s^2-t^2)^2+4s^2t^2=y^2+4x^2$ → $s^2+t^2=\sqrt{4x^2+y^2}$, 즉 $h(x,y)=\sqrt{4x^2+y^2}$"],
  check=_c)


def _c():
    rp = symbols('rp', positive=True)
    F = x**3*y - exp(x)*sin(y) + x**2*y**4
    Z = F.subs({x: rp*cos(th), y: rp*sin(th)}, simultaneous=True)
    lhs = diff(Z, rp, 2) + diff(Z, rp)/rp + diff(Z, th, 2)/rp**2
    rhs = (diff(F, x, 2) + diff(F, y, 2)).subs({x: rp*cos(th), y: rp*sin(th)}, simultaneous=True)
    for vals in ({rp: 2, th: R(1, 3)}, {rp: R(1, 2), th: 2}):
        assert EQ(lhs.subs(vals), rhs.subs(vals))
    A, B = symbols('A B')
    g = A*log(rp) + B
    assert simplify(diff(g, rp, 2) + diff(g, rp)/rp) == 0
    U = A*log(sqrt(x**2 + y**2)) + B
    assert simplify(diff(U, x, 2) + diff(U, y, 2)) == 0
P(id="4-51", ch=14, sec="14.5", type="14-chain2", src="강의 14.5 극좌표 연쇄법칙 심화",
  q=r"$z=f(x,y)$의 2계 편도함수가 연속이고 $x=r\cos\theta,\ y=r\sin\theta$이다.<br>(a) $f_{xx}+f_{yy}=z_{rr}+\dfrac1r\,z_r+\dfrac1{r^2}\,z_{\theta\theta}$임을 보여라.<br>(b) $u=g\big(\sqrt{x^2+y^2}\big)$ 꼴이면서 라플라스 방정식 $u_{xx}+u_{yy}=0$ ($(x,y)\ne(0,0)$)을 만족하는 함수를 모두 구하라.",
  hint=r"$z_r=f_x\cos\theta+f_y\sin\theta$, $z_\theta=-r\sin\theta\,f_x+r\cos\theta\,f_y$. 각각 한 번 더 미분하면 $z_{\theta\theta}$에 $-r(f_x\cos\theta+f_y\sin\theta)=-r\,z_r$ 항이 생겨요. (b)는 $u$가 $\theta$에 무관 → $g''+\tfrac1r g'=0$.",
  ans=r"(a) 아래 풀이  (b) $u=A\ln\sqrt{x^2+y^2}+B$ ($A,B$ 상수)",
  sol=[r"$z_{rr}=f_{xx}\cos^2\theta+2f_{xy}\sin\theta\cos\theta+f_{yy}\sin^2\theta$",
       r"$z_{\theta\theta}=-r\cos\theta\,f_x-r\sin\theta\,f_y+r^2\big(f_{xx}\sin^2\theta-2f_{xy}\sin\theta\cos\theta+f_{yy}\cos^2\theta\big)$",
       r"$\dfrac{1}{r^2}z_{\theta\theta}=-\dfrac1r z_r+\big(f_{xx}\sin^2\theta-2f_{xy}\sin\theta\cos\theta+f_{yy}\cos^2\theta\big)$",
       r"(a) $z_{rr}+\dfrac1r z_r+\dfrac1{r^2}z_{\theta\theta}=f_{xx}(\cos^2\theta+\sin^2\theta)+f_{yy}(\sin^2\theta+\cos^2\theta)=f_{xx}+f_{yy}$",
       r"(b) $u=g(r)$이면 $u_{xx}+u_{yy}=g''+\dfrac1r g'=\dfrac1r\big(rg'\big)'=0$ → $rg'=A$ → $g=A\ln r+B$"],
  check=_c)


def _c():
    f = x**3*log(y/x)
    xp, yp = symbols('xp yp', positive=True)
    fp = f.subs({x: xp, y: yp})
    assert simplify(xp*diff(fp, xp) + yp*diff(fp, yp) - 3*fp) == 0
    second = xp**2*diff(fp, xp, 2) + 2*xp*yp*diff(fp, xp, yp) + yp**2*diff(fp, yp, 2)
    assert simplify(second - 6*fp) == 0
    zp = symbols('zp', positive=True)
    Fuv = sin(u) + u*v**2 + exp(v)
    gg = xp**3*Fuv.subs({u: yp/xp, v: zp/xp}, simultaneous=True)
    expr = xp*diff(gg, xp) + yp*diff(gg, yp) + zp*diff(gg, zp) - 3*gg
    assert simplify(expr) == 0
P(id="4-52", ch=14, sec="14.5", type="14-chain", src="2024 중간 5번 배경 (동차함수의 오일러 정리)",
  q=r"모든 $t>0$에 대해 $f(tx,ty)=t^nf(x,y)$를 만족하는 미분가능한 함수 $f$를 $n$차 동차함수라 한다.<br>(a) $x\,f_x+y\,f_y=n\,f$임을 보여라. (힌트: $t$로 미분)<br>(b) 미분가능한 $F(u,v)$에 대해 $g(x,y,z)=x^3F\big(\tfrac yx,\tfrac zx\big)$일 때 $x\,g_x+y\,g_y+z\,g_z-3g$를 구하라.<br>(c) $f$의 2계 편도함수가 연속이면 $x^2f_{xx}+2xy\,f_{xy}+y^2f_{yy}=n(n-1)f$임을 보여라.",
  hint=r"$\phi(t)=f(tx,ty)=t^nf(x,y)$의 양변을 $t$로 미분하면 연쇄법칙으로 $x f_x(tx,ty)+y f_y(tx,ty)=nt^{n-1}f(x,y)$. 한 번 더 미분하면 (c).",
  ans=r"(a) 아래 풀이  (b) $0$  (c) 아래 풀이",
  sol=[r"(a) $\dfrac{d}{dt}f(tx,ty)=x\,f_x(tx,ty)+y\,f_y(tx,ty)=nt^{n-1}f(x,y)$ → $t=1$ 대입",
       r"(b) $g(tx,ty,tz)=t^3x^3F\big(\tfrac yx,\tfrac zx\big)=t^3g$ → $g$는 3차 동차, 같은 방법으로 $xg_x+yg_y+zg_z=3g$ → 답 $0$",
       r"(c) (a)의 식 $x f_x(tx,ty)+y f_y(tx,ty)=nt^{n-1}f$를 다시 $t$로 미분: $x\big(xf_{xx}+yf_{xy}\big)+y\big(xf_{yx}+yf_{yy}\big)=n(n-1)t^{n-2}f$",
       r"$t=1$, $f_{xy}=f_{yx}$ → $x^2f_{xx}+2xyf_{xy}+y^2f_{yy}=n(n-1)f$",
       r"예: $f=x^3\ln\tfrac yx$ (3차 동차)는 $xf_x+yf_y=3f$, 2계 식 $=6f$를 만족"],
  check=_c)


def _c():
    ux, vx, uy, vy = symbols('ux vx uy vy')
    U, V = 2, 1
    assert (U**2 - V**2, 2*U*V) == (3, 4)
    s1 = solve([2*U*ux - 2*V*vx - 1, 2*V*ux + 2*U*vx], [ux, vx])
    s2 = solve([2*U*uy - 2*V*vy, 2*V*uy + 2*U*vy - 1], [uy, vy])
    assert s1 == {ux: R(1, 5), vx: R(-1, 10)} and s2 == {uy: R(1, 10), vy: R(1, 5)}
    w = 1/(2*(2 + sympify('I')))
    assert EQ(sympify(w).as_real_imag()[0], R(1, 5)) and EQ(sympify(w).as_real_imag()[1], R(-1, 10))
P(id="4-53", ch=14, sec="14.5", type="14-implicit", src="교재 14.5 심화형 (연립 음함수 미분)",
  q=r"$x=u^2-v^2,\ y=2uv$가 점 $(u,v)=(2,1)$ 근처에서 $u,v$를 $x,y$의 함수로 정한다. 점 $(x,y)=(3,4)$에서 $\dfrac{\partial u}{\partial x},\ \dfrac{\partial v}{\partial x},\ \dfrac{\partial u}{\partial y},\ \dfrac{\partial v}{\partial y}$를 구하라.",
  hint=r"두 식을 각각 $x$로 미분하면 $1=2u\,u_x-2v\,v_x$, $0=2v\,u_x+2u\,v_x$ — $u_x, v_x$에 대한 연립일차방정식이에요. $y$로 미분해도 마찬가지.",
  ans=r"$u_x=\dfrac15,\ v_x=-\dfrac1{10},\ u_y=\dfrac1{10},\ v_y=\dfrac15$",
  sol=[r"$(u,v)=(2,1)$이면 $(x,y)=(4-1,\ 4)=(3,4)$ ✓",
       r"$x$로 미분: $1=4u_x-2v_x$, $0=2u_x+4v_x$ → $u_x=-2v_x$ → $1=-10v_x$ → $v_x=-\tfrac1{10},\ u_x=\tfrac15$",
       r"$y$로 미분: $0=4u_y-2v_y$, $1=2u_y+4v_y$ → $v_y=2u_y$ → $1=10u_y$ → $u_y=\tfrac1{10},\ v_y=\tfrac15$",
       r"확인: $u_x=v_y,\ u_y=-v_x$가 성립해요 ($u+iv=\sqrt{x+iy}$의 성질)"],
  check=_c)


def _c():
    tt = symbols('tt')
    a = Function('a')(tt); b = Function('b')(tt); C = Function('C')(tt)
    A = R(1, 2)*a*b*sin(C)
    c2 = a**2 + b**2 - 2*a*b*cos(C)
    subsd = {a.diff(tt): 1, b.diff(tt): R(-1, 2), C.diff(tt): R(1, 10)}
    vals = {a: 10, b: 6, C: pi/3}
    dA = A.diff(tt).subs(subsd).subs(vals)
    assert EQ(dA, sqrt(3)/4 + R(3, 2))
    cval = sqrt(c2.subs(vals))
    assert EQ(cval, 2*sqrt(19))
    dc = (c2.diff(tt).subs(subsd).subs(vals)) / (2*cval)
    assert EQ(dc, (13 + 6*sqrt(3))/(4*sqrt(19)))
P(id="4-54", ch=14, sec="14.5", type="14-chain", src="교재 14.5 심화형 (관련 변화율)",
  q=r"삼각형의 두 변 $a,b$와 그 끼인각 $\theta$가 시간에 따라 변한다. $a=10$ cm, $b=6$ cm, $\theta=\dfrac\pi3$인 순간 $a$는 $1$ cm/s로 늘고, $b$는 $0.5$ cm/s로 줄며, $\theta$는 $0.1$ rad/s로 커진다. 이 순간<br>(a) 넓이 $A$의 변화율  (b) 셋째 변 $c$의 길이의 변화율을 구하라.",
  hint=r"$A=\tfrac12ab\sin\theta$, $c^2=a^2+b^2-2ab\cos\theta$ (코사인 법칙)를 $t$로 미분: $\dfrac{dA}{dt}=A_a\dfrac{da}{dt}+A_b\dfrac{db}{dt}+A_\theta\dfrac{d\theta}{dt}$",
  ans=r"(a) $\dfrac{\sqrt3}{4}+\dfrac32\approx1.93\ \mathrm{cm^2/s}$  (b) $\dfrac{13+6\sqrt3}{4\sqrt{19}}\approx1.34$ cm/s",
  sol=[r"(a) $\dfrac{dA}{dt}=\tfrac12\big(b\sin\theta\,a'+a\sin\theta\,b'+ab\cos\theta\,\theta'\big)=\tfrac12\big(3\sqrt3-\tfrac{5\sqrt3}{2}+3\big)=\dfrac{\sqrt3}{4}+\dfrac32$",
       r"(b) $c^2=100+36-60\cdot\tfrac12=76$ → $c=2\sqrt{19}$",
       r"$2cc'=2aa'+2bb'-2(a'b+ab')\cos\theta+2ab\sin\theta\,\theta'$",
       r"$cc'=10-3-(6-5)\cdot\tfrac12+60\cdot\tfrac{\sqrt3}{2}\cdot0.1=\tfrac{13}{2}+3\sqrt3$",
       r"$c'=\dfrac{13/2+3\sqrt3}{2\sqrt{19}}=\dfrac{13+6\sqrt3}{4\sqrt{19}}\approx1.34$ cm/s"],
  check=_c)


def _c():
    f = taylor2(1, 1, 4, 2, -1, 1, 2, -3)
    g = f.subs({x: t**2, y: t**3}, simultaneous=True)
    assert EQ(diff(g, t).subs(t, 1), 1) and EQ(diff(g, t, 2).subs(t, 1), -1)
P(id="4-55", ch=14, sec="14.5", type="14-chain2", src="2024 중간 7번 배경 (곡선 위 2계 도함수)",
  q=r"$f$는 2계 편도함수가 연속이고 점 $(1,1)$에서 $f_x=2,\ f_y=-1,\ f_{xx}=1,\ f_{xy}=2,\ f_{yy}=-3$이다. $g(t)=f(t^2,\ t^3)$일 때 $g'(1)$과 $g''(1)$을 구하라.",
  hint=r"$\mathbf r(t)=\langle t^2,t^3\rangle$이면 $g'=f_x x'+f_y y'$, $g''=f_{xx}(x')^2+2f_{xy}x'y'+f_{yy}(y')^2+f_x x''+f_y y''$ — 마지막 두 항을 빠뜨리기 쉬워요.",
  ans=r"$g'(1)=1,\ g''(1)=-1$",
  sol=[r"$t=1$: $x'=2t=2,\ y'=3t^2=3,\ x''=2,\ y''=6t=6$",
       r"$g'(1)=f_x x'+f_y y'=2\cdot2+(-1)\cdot3=1$",
       r"$g''=\dfrac{d}{dt}\big(f_x x'+f_y y'\big)=(f_{xx}x'+f_{xy}y')x'+f_x x''+(f_{yx}x'+f_{yy}y')y'+f_y y''$",
       r"$=1\cdot4+2\cdot2\cdot2\cdot3+(-3)\cdot9+2\cdot2+(-1)\cdot6=4+24-27+4-6=-1$"],
  check=_c)


# ───────── 14.6 ─────────
def _c():
    f = taylor2(0, 0, 2, 1, -2, 3, 1, -1)
    g = 1/f
    uu = (R(3, 5), R(4, 5))
    ph_ = g.subs({x: uu[0]*t, y: uu[1]*t}, simultaneous=True)
    pf = f.subs({x: uu[0]*t, y: uu[1]*t}, simultaneous=True)
    assert EQ(diff(pf, t).subs(t, 0), -1) and EQ(diff(pf, t, 2).subs(t, 0), R(7, 5))
    assert EQ(diff(ph_, t).subs(t, 0), R(1, 4)) and EQ(diff(ph_, t, 2).subs(t, 0), R(-1, 10))
P(id="4-56", ch=14, sec="14.6", type="14-dir", src="2024 중간 7번 유형 (2계 방향도함수)",
  q=r"$f$는 2계 편도함수가 연속이고, 점 $(a,b)$에서 $f=2,\ \nabla f=\langle1,-2\rangle,\ f_{xx}=3,\ f_{xy}=1,\ f_{yy}=-1$이다. $\mathbf u=\big\langle\tfrac35,\tfrac45\big\rangle$, $g(x,y)=\dfrac{1}{f(x,y)}$일 때<br>(a) $D_{\mathbf u}f(a,b)$와 $D_{\mathbf u}^2f(a,b)$를 구하라.  (b) $D_{\mathbf u}g(a,b)$와 $D_{\mathbf u}^2g(a,b)$를 구하라.<br>(단, $D_{\mathbf u}^2f=D_{\mathbf u}(D_{\mathbf u}f)$)",
  hint=r"$D_{\mathbf u}^2f=f_{xx}u_1^2+2f_{xy}u_1u_2+f_{yy}u_2^2$. $g=\phi(f)$이면 $D_{\mathbf u}g=\phi'(f)D_{\mathbf u}f$, $D_{\mathbf u}^2g=\phi''(f)(D_{\mathbf u}f)^2+\phi'(f)D_{\mathbf u}^2f$ (1변수 합성함수 미분과 같아요).",
  ans=r"(a) $D_{\mathbf u}f=-1,\ D_{\mathbf u}^2f=\dfrac75$  (b) $D_{\mathbf u}g=\dfrac14,\ D_{\mathbf u}^2g=-\dfrac1{10}$",
  sol=[r"(a) $D_{\mathbf u}f=\tfrac35-\tfrac85=-1$,  $D_{\mathbf u}^2f=3\cdot\tfrac9{25}+2\cdot1\cdot\tfrac{12}{25}-\tfrac{16}{25}=\tfrac{35}{25}=\tfrac75$",
       r"(b) $\phi(w)=\tfrac1w$: $\phi'=-\tfrac1{w^2},\ \phi''=\tfrac2{w^3}$, $w=f=2$",
       r"$D_{\mathbf u}g=-\dfrac{D_{\mathbf u}f}{f^2}=-\dfrac{-1}{4}=\dfrac14$",
       r"$D_{\mathbf u}^2g=\dfrac{2(D_{\mathbf u}f)^2}{f^3}-\dfrac{D_{\mathbf u}^2f}{f^2}=\dfrac{2}{8}-\dfrac{7/5}{4}=\dfrac14-\dfrac7{20}=-\dfrac1{10}$"],
  check=_c)


def _c():
    gf = 6*Matrix([1, 2, -2])/3
    assert EQ(gf, [2, 4, -4])
    k = symbols('k')
    gg = k*Matrix([2, -1, 2])
    ksol = solve(gg.dot(Matrix([1, -2, 2])/3) - 8, k)
    assert ksol == [3]
    gg = gg.subs(k, 3)
    fP, gP = 1, 2
    gh = (gP*gf - fP*gg)/gP**2
    assert EQ(gh, Matrix([-2, 11, -14])/4)
    vv = Matrix([2, 1, -2])/3
    assert EQ(gh.dot(vv), R(35, 12))
P(id="4-57", ch=14, sec="14.6", type="14-dir", src="2022 중간 블럭1 5번 유형",
  q=r"미분가능한 함수 $f,g$가 점 $P$에서 다음을 만족한다.<br>① $f$는 $P$에서 벡터 $\langle1,2,-2\rangle$ 방향으로 최대 변화율 $6$을 가진다.<br>② 곡면 $g(x,y,z)=2$의 $P$에서의 접평면이 평면 $2x-y+2z=5$와 평행하다.<br>③ $\mathbf u=\tfrac13\langle1,-2,2\rangle$에 대해 $D_{\mathbf u}g(P)=8$이다.  ④ $f(P)=1,\ g(P)=2$<br>(a) $\nabla f(P)$  (b) $\nabla g(P)$  (c) $h=\dfrac fg$의 $P$에서 $\langle2,1,-2\rangle$ 방향의 변화율을 구하라.",
  hint=r"① 최대 변화율 방향 = $\nabla f$ 방향, 크기 = $|\nabla f|$. ② 접평면의 법선 = $\nabla g$ → $\nabla g=k\langle2,-1,2\rangle$. ③으로 $k$ 결정. (c) $\nabla h=\dfrac{g\nabla f-f\nabla g}{g^2}$.",
  ans=r"(a) $\langle2,4,-4\rangle$  (b) $\langle6,-3,6\rangle$  (c) $\dfrac{35}{12}$",
  sol=[r"(a) $\nabla f(P)=6\cdot\dfrac{\langle1,2,-2\rangle}{3}=\langle2,4,-4\rangle$",
       r"(b) $\nabla g(P)=k\langle2,-1,2\rangle$, $D_{\mathbf u}g=k\cdot\dfrac{2+2+4}{3}=\dfrac{8k}{3}=8$ → $k=3$ → $\langle6,-3,6\rangle$",
       r"(c) $\nabla h=\dfrac{2\langle2,4,-4\rangle-1\cdot\langle6,-3,6\rangle}{4}=\dfrac14\langle-2,11,-14\rangle$",
       r"단위벡터 $\tfrac13\langle2,1,-2\rangle$: $D h=\dfrac{1}{12}(-4+11+28)=\dfrac{35}{12}$"],
  check=_c)


def _c():
    T = 50 - x**2 - 3*y**2
    gT = grad(T, [x, y]).subs({x: 3, y: 1})
    assert EQ(gT, [-6, -6]) and EQ(gT.norm(), 6*sqrt(2))
    path = x**3/27
    assert EQ(path.subs(x, 3), 1)
    assert simplify(diff(path, x) - 3*path/x) == 0
    assert simplify(diff(path, x) - (diff(T, y)/diff(T, x)).subs(y, path)) == 0
P(id="4-58", ch=14, sec="14.6", type="14-maxrate", src="교재 14.6 심화형 (최대 증가 방향을 따라가는 경로)",
  q=r"금속판 위의 온도가 $T(x,y)=50-x^2-3y^2$이다.<br>(a) 점 $(3,1)$에서 온도가 가장 빨리 올라가는 방향과 그 최대 증가율을 구하라.<br>(b) 열을 찾는 입자가 $(3,1)$에서 출발해 매 순간 온도가 가장 빨리 올라가는 방향으로 움직인다. 입자가 지나는 경로의 방정식을 구하라.",
  hint=r"(b) 경로의 접선이 항상 $\nabla T=\langle-2x,-6y\rangle$와 평행 → $\dfrac{dy}{dx}=\dfrac{T_y}{T_x}=\dfrac{3y}{x}$ (변수분리형 미분방정식)",
  ans=r"(a) $\langle-1,-1\rangle$ 방향 (단위벡터 $\tfrac1{\sqrt2}\langle-1,-1\rangle$), 최대 증가율 $6\sqrt2$  (b) $y=\dfrac{x^3}{27}$ ($0<x\le3$, 원점 쪽으로)",
  sol=[r"(a) $\nabla T=\langle-2x,-6y\rangle$, $\nabla T(3,1)=\langle-6,-6\rangle$ → 방향 $\langle-1,-1\rangle$, 크기 $6\sqrt2$",
       r"(b) $\dfrac{dy}{dx}=\dfrac{-6y}{-2x}=\dfrac{3y}{x}$ → $\dfrac{dy}{y}=\dfrac{3\,dx}{x}$ → $\ln|y|=3\ln|x|+C$ → $y=kx^3$",
       r"$(3,1)$을 지나므로 $k=\tfrac1{27}$ → $y=\dfrac{x^3}{27}$",
       r"$\nabla T$가 원점(최고 온도점) 쪽을 가리키므로 입자는 이 곡선을 따라 원점으로 다가가요."],
  check=_c)


def _c():
    F = x**2 + 2*y**2 + 3*z**2
    G = x*y - z
    pt = {x: 1, y: 1, z: 1}
    assert F.subs(pt) == 6 and G.subs(pt) == 0
    gF = grad(F, [x, y, z]).subs(pt); gG = grad(G, [x, y, z]).subs(pt)
    assert gF.dot(gG) == 0
    assert EQ(gF.cross(gG), [-10, 8, -2])
P(id="4-59", ch=14, sec="14.6", type="14-levelsurf", src="교재 14.6 심화형 (두 곡면의 수직 · 교선의 접선)",
  q=r"타원면 $x^2+2y^2+3z^2=6$과 곡면 $z=xy$에 대해<br>(a) 두 곡면이 점 $(1,1,1)$에서 수직으로 만남(법선끼리 수직)을 보여라.<br>(b) 두 곡면의 교선의 점 $(1,1,1)$에서의 접선의 매개방정식을 구하라.",
  hint=r"$F=x^2+2y^2+3z^2$, $G=xy-z$로 두면 법선은 $\nabla F$, $\nabla G$. 교선의 접선은 두 법선에 모두 수직 → $\nabla F\times\nabla G$ 방향.",
  ans=r"(a) $\nabla F\cdot\nabla G=0$  (b) $x=1+5t,\ y=1-4t,\ z=1+t$",
  sol=[r"점 확인: $1+2+3=6$, $1\cdot1=1$ ✓",
       r"(a) $\nabla F=\langle2x,4y,6z\rangle=\langle2,4,6\rangle$, $\nabla G=\langle y,x,-1\rangle=\langle1,1,-1\rangle$, 내적 $2+4-6=0$ → 수직",
       r"(b) $\nabla F\times\nabla G=\langle4(-1)-6\cdot1,\ 6\cdot1-2(-1),\ 2\cdot1-4\cdot1\rangle=\langle-10,8,-2\rangle\parallel\langle5,-4,1\rangle$",
       r"접선: $x=1+5t,\ y=1-4t,\ z=1+t$"],
  check=_c)


def _c():
    a, b = symbols('a b', positive=True)
    c = 1/(a*b)
    F = x*y*z
    n = grad(F, [x, y, z]).subs({x: a, y: b, z: c})
    plane_rhs = n.dot(Matrix([a, b, c]))
    assert simplify(plane_rhs - 3) == 0
    xi, yi, zi = plane_rhs/n[0], plane_rhs/n[1], plane_rhs/n[2]
    assert simplify(xi - 3*a) == 0 and simplify(yi - 3*b) == 0 and simplify(zi - 3*c) == 0
    assert simplify(xi*yi*zi/6 - R(9, 2)) == 0
P(id="4-60", ch=14, sec="14.6", type="14-levelsurf", src="교재 14.6 심화형 (접평면이 만드는 사면체)",
  q=r"곡면 $xyz=1$ 위의 제1팔분공간의 점 $(a,b,c)$ ($a,b,c>0$)에서의 접평면과 세 좌표평면으로 둘러싸인 사면체의 부피가 점의 위치와 관계없이 일정함을 보이고, 그 값을 구하라.",
  hint=r"$\nabla(xyz)=\langle yz,xz,xy\rangle$ → 접평면 $bc\,x+ac\,y+ab\,z=3abc$. $abc=1$을 이용하면 절편이 깔끔해져요.",
  ans=r"부피 $\dfrac92$ (항상 일정)",
  sol=[r"접평면: $bc(x-a)+ac(y-b)+ab(z-c)=0$ → $bc\,x+ac\,y+ab\,z=3abc=3$",
       r"$x$절편 $\dfrac{3}{bc}=3a$ ($\because\ \tfrac1{bc}=a$), 같은 방법으로 $y$절편 $3b$, $z$절편 $3c$",
       r"부피 $=\dfrac16(3a)(3b)(3c)=\dfrac{27abc}{6}=\dfrac92$ — $(a,b,c)$에 관계없이 일정"],
  check=_c)


def _c():
    f = log(x**2 + y**2)
    P0 = {x: R(1, 2), y: sqrt(3)/2}
    gf = grad(f, [x, y]).subs(P0)
    assert EQ(gf, [1, sqrt(3)]) and EQ(gf.norm(), 2)
    tq = symbols('tq', real=True)
    sols = solve(cos(tq) + sqrt(3)*sin(tq) - 1, tq)
    angs = sorted([float(q % (2*pi)) for q in sols])
    assert abs(angs[0] - 0) < 1e-12 and abs(angs[1] - float(2*pi/3)) < 1e-12
    assert EQ(gf.dot(Matrix([-sqrt(3)/2, R(1, 2)])), 0)
P(id="4-61", ch=14, sec="14.6", type="14-dir", src="교재 14.6 심화형 (주어진 변화율의 방향 찾기)",
  q=r"$f(x,y)=\ln(x^2+y^2)$, 점 $P\big(\tfrac12,\tfrac{\sqrt3}{2}\big)$에 대해<br>(a) $P$에서 최대 변화율과 그 방향을 구하라.  (b) $D_{\mathbf u}f(P)=1$이 되는 단위벡터 $\mathbf u$를 모두 구하라.  (c) $D_{\mathbf u}f(P)=0$이 되는 $\mathbf u$를 모두 구하고, 그 의미를 설명하라.",
  hint=r"$\nabla f(P)=\langle1,\sqrt3\rangle$, $\mathbf u=\langle\cos\theta,\sin\theta\rangle$로 두면 $D_{\mathbf u}f=\cos\theta+\sqrt3\sin\theta=2\cos\big(\theta-\tfrac\pi3\big)$.",
  ans=r"(a) 최대 변화율 $2$, 방향 $\big\langle\tfrac12,\tfrac{\sqrt3}2\big\rangle$  (b) $\langle1,0\rangle$, $\big\langle-\tfrac12,\tfrac{\sqrt3}2\big\rangle$  (c) $\pm\big\langle-\tfrac{\sqrt3}2,\tfrac12\big\rangle$ — 등위곡선(원)의 접선 방향",
  sol=[r"$\nabla f=\dfrac{\langle2x,2y\rangle}{x^2+y^2}$ → $\nabla f(P)=\langle1,\sqrt3\rangle$ ($x^2+y^2=1$)",
       r"(a) $|\nabla f(P)|=2$, 방향 $\tfrac12\langle1,\sqrt3\rangle$",
       r"(b) $2\cos\big(\theta-\tfrac\pi3\big)=1$ → $\theta-\tfrac\pi3=\pm\tfrac\pi3$ → $\theta=0,\ \tfrac{2\pi}3$ → $\mathbf u=\langle1,0\rangle,\ \big\langle-\tfrac12,\tfrac{\sqrt3}2\big\rangle$",
       r"(c) $\cos\big(\theta-\tfrac\pi3\big)=0$ → $\theta=\tfrac{5\pi}6,\ \tfrac{11\pi}6$ → $\pm\big\langle-\tfrac{\sqrt3}2,\tfrac12\big\rangle$",
       r"$\nabla f$에 수직인 방향 = 등위곡선 $x^2+y^2=1$의 접선 방향 (그 방향으로는 값이 순간적으로 변하지 않음)"],
  check=_c)


# ───────── 14.7 ─────────
def _c():
    f = 3*x**4 - 4*x**2*y + y**2
    assert expand((y - x**2)*(y - 3*x**2) - f) == 0
    assert solve([diff(f, x), diff(f, y)], [x, y], dict=True) == [{x: 0, y: 0}]
    H = (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2).subs({x: 0, y: 0})
    assert H == 0
    m = symbols('m', real=True)
    along = expand(f.subs(y, m*x))
    assert expand(along - x**2*(3*x**2 - 4*m*x + m**2)) == 0
    assert expand(f.subs(y, 2*x**2) + x**4) == 0
    assert f.subs({x: 0, y: t}) == t**2
P(id="4-62", ch=14, sec="14.7", type="14-crit", src="교재 14.7 심화형 (판별식 D=0인 임계점)",
  q=r"$f(x,y)=3x^4-4x^2y+y^2$에 대해<br>(a) 원점이 유일한 임계점이고 그곳에서 $D=f_{xx}f_{yy}-f_{xy}^2=0$임을 보여라.<br>(b) 원점을 지나는 모든 직선 위로 제한하면 $f$는 원점에서 극소임을 보여라.<br>(c) 그러나 원점은 $f$의 극소점이 아님을 보이고, 원점이 무엇인지 판정하라.",
  hint=r"$f=(y-x^2)(y-3x^2)$로 인수분해돼요. 두 포물선 $y=x^2$과 $y=3x^2$ 사이에서 $f$의 부호는?",
  ans=r"(a) $D=0$ (판정 불가)  (b) $y=mx$ 위에서 $f=x^2(3x^2-4mx+m^2)\ge0$ 근처  (c) $y=2x^2$ 위에서 $f=-x^4<0$ → 원점은 안장점",
  sol=[r"(a) $f_x=12x^3-8xy=4x(3x^2-2y)$, $f_y=-4x^2+2y$ → $y=2x^2$ 대입 시 $f_x=-4x^3=0$ → $(0,0)$뿐. $f_{xx}=0,\ f_{yy}=2,\ f_{xy}=0$ → $D=0$",
       r"(b) $y=mx$ ($m\ne0$): $f=x^2(3x^2-4mx+m^2)$, $x\to0$이면 괄호 $\to m^2>0$ → 원점 근처에서 $f\ge0=f(0,0)$. $y=0$: $3x^4\ge0$, $x=0$: $y^2\ge0$",
       r"(c) $f=(y-x^2)(y-3x^2)$이므로 $x^2<y<3x^2$에서 음수. 예: $y=2x^2$ 위에서 $f=(x^2)(-x^2)=-x^4<0$",
       r"원점 근처에 $f>0$인 점(예 $y=0$)과 $f<0$인 점이 모두 있음 → 극소도 극대도 아닌 안장점"],
  check=_c)


def _c():
    f = sin(x) + sin(y) + sin(x + y)
    cands = [(pi/3, pi/3), (5*pi/3, 5*pi/3), (pi, pi)]
    for (a, b) in cands:
        assert EQ(diff(f, x).subs({x: a, y: b}), 0) and EQ(diff(f, y).subs({x: a, y: b}), 0)
    def D(a, b):
        return (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2).subs({x: a, y: b})
    assert EQ(D(pi/3, pi/3), R(9, 4)) and EQ(diff(f, x, 2).subs({x: pi/3, y: pi/3}), -sqrt(3))
    assert EQ(f.subs({x: pi/3, y: pi/3}), 3*sqrt(3)/2) and EQ(f.subs({x: 5*pi/3, y: 5*pi/3}), -3*sqrt(3)/2)
    assert EQ(D(pi, pi), 0)
    hh = symbols('hh', real=True)
    along = simplify(f.subs({x: pi + hh, y: pi + hh}))
    assert simplify(along - 2*sin(hh)*(cos(hh) - 1)) == 0
    # 열린 정사각형 안의 임계점이 이 셋뿐인지: 여러 시작점에서 뉴턴법으로 근을 찾아 비교
    found = 0
    for i in range(1, 12):
        for j in range(1, 12):
            a0, b0 = 2*mp.pi*i/12, 2*mp.pi*j/12
            try:
                sol = mp.findroot([lambda a, b: mp.cos(a) + mp.cos(a + b),
                                   lambda a, b: mp.cos(b) + mp.cos(a + b)], (a0, b0))
            except Exception:
                continue
            a1, b1 = float(sol[0]), float(sol[1])
            if 1e-6 < a1 < 2*float(pi) - 1e-6 and 1e-6 < b1 < 2*float(pi) - 1e-6:
                found += 1
                assert min(abs(a1 - float(p_)) + abs(b1 - float(q_)) for p_, q_ in cands) < 1e-3
    assert found > 20


P(id="4-63", ch=14, sec="14.7", type="14-crit", src="교재 14.7 심화형 (삼각함수 · D=0)",
  q=r"$f(x,y)=\sin x+\sin y+\sin(x+y)$의 열린 정사각형 $0<x<2\pi,\ 0<y<2\pi$에서의 임계점을 모두 구하고 분류하라.",
  hint=r"$f_x=\cos x+\cos(x+y)=0,\ f_y=\cos y+\cos(x+y)=0$에서 $\cos x=\cos y$ → $y=x$ 또는 $y=2\pi-x$. $D=0$인 점은 직선 $y=x$를 따라 부호를 조사해 보세요.",
  ans=r"$\big(\tfrac\pi3,\tfrac\pi3\big)$: 극댓값 $\tfrac{3\sqrt3}{2}$,  $\big(\tfrac{5\pi}3,\tfrac{5\pi}3\big)$: 극솟값 $-\tfrac{3\sqrt3}{2}$,  $(\pi,\pi)$: $D=0$이지만 안장점",
  sol=[r"$y=2\pi-x$: $\cos x+\cos2\pi=0$ → $x=\pi$ → $(\pi,\pi)$",
       r"$y=x$: $\cos x+\cos2x=2\cos^2x+\cos x-1=(2\cos x-1)(\cos x+1)=0$ → $x=\tfrac\pi3,\ \tfrac{5\pi}3,\ \pi$",
       r"$f_{xx}=-\sin x-\sin(x+y),\ f_{yy}=-\sin y-\sin(x+y),\ f_{xy}=-\sin(x+y)$",
       r"$\big(\tfrac\pi3,\tfrac\pi3\big)$: $f_{xx}=f_{yy}=-\sqrt3,\ f_{xy}=-\tfrac{\sqrt3}2$ → $D=3-\tfrac34=\tfrac94>0$, 극대 $f=\tfrac{3\sqrt3}{2}$;  $\big(\tfrac{5\pi}3,\tfrac{5\pi}3\big)$: 부호가 모두 반대 → 극소 $-\tfrac{3\sqrt3}{2}$",
       r"$(\pi,\pi)$: 모든 2계 도함수 $0$ → $D=0$. $f(\pi+h,\pi+h)=-2\sin h+\sin2h=2\sin h(\cos h-1)$은 $h>0$이면 음, $h<0$이면 양 → $f(\pi,\pi)=0$ 근처에서 부호가 바뀜 → 안장점"],
  check=_c)


def _c():
    gfun = (x - 1)**2 + y**2
    rq = symbols('rq', nonnegative=True)
    on_bd = simplify(gfun.subs({x: rq*cos(th), y: rq*sin(th)}).subs(cos(th), rq - 1))
    assert simplify(expand(gfun.subs({x: rq*cos(th), y: rq*sin(th)})) - (rq**2 - 2*rq*cos(th) + 1)) == 0
    assert simplify((rq**2 - 2*rq*(rq - 1) + 1) - (-rq**2 + 2*rq + 1)) == 0
    best_max, best_min = -1.0, 2.0
    for i in range(0, 361):
        tq = 2*mp.pi*i/360
        rmax = 1 + mp.cos(tq)
        for j in range(0, 61):
            rr_ = rmax*j/60
            xv, yv = rr_*mp.cos(tq), rr_*mp.sin(tq)
            val = float(mp.e**(-((xv - 1)**2 + yv**2)))
            best_max = max(best_max, val); best_min = min(best_min, val)
    assert abs(best_max - 1) < 1e-3 and abs(best_min - float(exp(-2))) < 1e-6
P(id="4-64", ch=14, sec="14.7", type="14-absext", src="2025 중간 7번 유형",
  q=r"$f(x,y)=e^{-(x-1)^2-y^2}$의 영역 $D=\big\{(x,y)\ \big|\ x^2+y^2\le\sqrt{x^2+y^2}+x\big\}$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"$D$는 극좌표로 $r\le1+\cos\theta$ (심장형). $f=e^{-g}$, $g=(x-1)^2+y^2$이므로 $f$의 최대·최소는 $g$의 최소·최대에서. 경계에서는 $\cos\theta=r-1$을 대입하면 $g$가 $r$만의 함수가 돼요.",
  ans=r"최댓값 $1$ (점 $(1,0)$),  최솟값 $e^{-2}$ (점 $(0,\pm1)$)",
  sol=[r"$x^2+y^2\le\sqrt{x^2+y^2}+x \iff r^2\le r+r\cos\theta \iff r\le1+\cos\theta$",
       r"$g=(x-1)^2+y^2=r^2-2r\cos\theta+1$. 내부 임계점은 $(1,0)$ ($r=1\le2$이므로 $D$ 안) → $g=0$, $f=1$",
       r"경계 $r=1+\cos\theta$ ($0\le r\le2$): $\cos\theta=r-1$ → $g=r^2-2r(r-1)+1=-r^2+2r+1$",
       r"$0\le r\le2$에서 최댓값 $g(1)=2$ ($\cos\theta=0$ → 점 $(0,\pm1)$), 최솟값 $g(0)=g(2)=1$",
       r"따라서 $g$의 최소 $0$, 최대 $2$ → $f$의 최댓값 $e^0=1$ ($(1,0)$), 최솟값 $e^{-2}$ ($(0,\pm1)$)"],
  check=_c)


def _c():
    f = x**2 - x*y + y**2 - 2*y
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: R(2, 3), y: R(4, 3)}
    assert EQ(f.subs({x: R(2, 3), y: R(4, 3)}), R(-4, 3))
    arc = expand(f.subs({x: 2*cos(t), y: 2*sin(t)}))
    assert EQ(arc.subs(t, pi/3), 4 - 3*sqrt(3))
    vals = []
    for i in range(0, 201):
        for j in range(0, 101):
            a, b = -2 + 4*i/200, 2*j/100
            if a*a + b*b <= 4 + 1e-12:
                vals.append(a*a - a*b + b*b - 2*b)
    for k in range(0, 2001):
        tq = mp.pi*k/2000
        a, b = 2*mp.cos(tq), 2*mp.sin(tq)
        vals.append(float(a*a - a*b + b*b - 2*b))
    assert abs(max(vals) - 4) < 1e-9 and min(vals) >= float(R(-4, 3)) - 1e-9
    assert float(4 - 3*sqrt(3)) > float(R(-4, 3))
P(id="4-65", ch=14, sec="14.7", type="14-absext", src="교재 14.7 심화형 (반원판 · 경계 매개화)",
  q=r"$f(x,y)=x^2-xy+y^2-2y$의 반원판 $D=\{(x,y)\mid x^2+y^2\le4,\ y\ge0\}$ 위에서의 최댓값과 최솟값을 구하라.",
  hint=r"후보: 내부 임계점, 지름 ($y=0$), 반원호 ($x=2\cos t,\ y=2\sin t,\ 0\le t\le\pi$). 호에서는 $f=4-2\sin2t-4\sin t$.",
  ans=r"최댓값 $4$ (점 $(\pm2,0)$),  최솟값 $-\dfrac43$ (점 $\big(\tfrac23,\tfrac43\big)$)",
  sol=[r"내부: $f_x=2x-y=0,\ f_y=-x+2y-2=0$ → $\big(\tfrac23,\tfrac43\big)$ ($D$ 안), $f=-\tfrac43$",
       r"지름 $y=0,\ -2\le x\le2$: $f=x^2$ → 최소 $0$ ($(0,0)$), 최대 $4$ ($(\pm2,0)$)",
       r"호: $f(t)=4-2\sin2t-4\sin t$, $f'(t)=-4\cos2t-4\cos t=0$ → $2\cos^2t+\cos t-1=0$ → $\cos t=\tfrac12$ 또는 $-1$",
       r"$t=\tfrac\pi3$ (점 $(1,\sqrt3)$): $f=4-\sqrt3-2\sqrt3=4-3\sqrt3\approx-1.20$;  $t=0,\pi$: $f=4$",
       r"비교: $-\tfrac43<4-3\sqrt3$ ($\iff 9\sqrt3<16 \iff 243<256$) → 최솟값 $-\tfrac43$, 최댓값 $4$"],
  check=_c)


def _c():
    m, b = symbols('m b', real=True)
    pts = [(0, 1), (1, 3), (2, 4), (3, 4)]
    S = sum((yi - (m*xi + b))**2 for xi, yi in pts)
    sol = solve([diff(S, m), diff(S, b)], [m, b])
    assert sol == {m: 1, b: R(3, 2)}
    D = (diff(S, m, 2)*diff(S, b, 2) - diff(S, m, b)**2)
    assert D == 80 and diff(S, m, 2) > 0
    assert EQ(S.subs(sol), 1)
P(id="4-66", ch=14, sec="14.7", type="14-optim", src="교재 14.7 심화형 (최소제곱 직선)",
  q=r"네 점 $(0,1),\ (1,3),\ (2,4),\ (3,4)$에 가장 가까운 직선 $y=mx+b$를 찾으려 한다. 오차제곱합 $S(m,b)=\displaystyle\sum_{i=1}^{4}\big(y_i-(mx_i+b)\big)^2$을 최소로 하는 $m,b$와 그때의 $S$를 구하고, 최소임을 2계 판정법으로 확인하라.",
  hint=r"$S_m=-2\sum x_i(y_i-mx_i-b)=0$, $S_b=-2\sum(y_i-mx_i-b)=0$ → $m\sum x_i^2+b\sum x_i=\sum x_iy_i$, $m\sum x_i+4b=\sum y_i$",
  ans=r"$y=x+\dfrac32$ ($m=1,\ b=\tfrac32$), 최소 $S=1$",
  sol=[r"$\sum x_i=6,\ \sum y_i=12,\ \sum x_i^2=14,\ \sum x_iy_i=0+3+8+12=23$",
       r"$14m+6b=23,\ 6m+4b=12$ → $b=3-\tfrac32m$ → $14m+18-9m=23$ → $m=1,\ b=\tfrac32$",
       r"$S_{mm}=2\sum x_i^2=28,\ S_{bb}=2\cdot4=8,\ S_{mb}=2\sum x_i=12$ → $D=224-144=80>0,\ S_{mm}>0$ → 극소 (이차함수라 최소)",
       r"잔차 $-\tfrac12,\ \tfrac12,\ \tfrac12,\ -\tfrac12$ → $S=4\cdot\tfrac14=1$"],
  check=_c)


def _c():
    Pm = Matrix([2 + s, -1 - s, 0]); Qm = Matrix([t, 1, 3 - t])
    Dst = expand((Pm - Qm).dot(Pm - Qm))
    sol = solve([diff(Dst, s), diff(Dst, t)], [s, t])
    assert sol == {s: -1, t: 2}
    assert EQ(Dst.subs(sol), 3)
    H = diff(Dst, s, 2)*diff(Dst, t, 2) - diff(Dst, s, t)**2
    assert H == 12 and diff(Dst, s, 2) > 0
    A_, B_ = Pm.subs(sol), Qm.subs(sol)
    assert EQ(A_, [1, 0, 0]) and EQ(B_, [2, 1, 1])
    d1, d2 = Matrix([1, -1, 0]), Matrix([1, 0, -1])
    assert (B_ - A_).dot(d1) == 0 and (B_ - A_).dot(d2) == 0
    n = d1.cross(d2)
    assert EQ(abs(n.dot(Matrix([0, 1, 3]) - Matrix([2, -1, 0])))/n.norm(), sqrt(3))
P(id="4-67", ch=14, sec="14.7", type="14-optim", src="교재 14.7 심화형 (꼬인 직선 사이 최단거리)",
  q=r"두 직선 $L_1:\ x=2+s,\ y=-1-s,\ z=0$과 $L_2:\ x=t,\ y=1,\ z=3-t$에 대해<br>(a) $L_1$ 위의 점 $P(s)$와 $L_2$ 위의 점 $Q(t)$ 사이 거리의 제곱 $D(s,t)$의 임계점을 구하고, 그것이 최솟값임을 보여 두 직선 사이의 거리를 구하라.<br>(b) 최단 거리를 이루는 두 점을 잇는 선분이 두 직선에 모두 수직임을 확인하라.",
  hint=r"$D(s,t)=(s-t+2)^2+(s+2)^2+(t-3)^2$. 연립방정식 $D_s=D_t=0$을 풀고 2계 판정법으로 확인. (12.5의 외적 공식과 비교해 보세요.)",
  ans=r"(a) $(s,t)=(-1,2)$에서 최솟값 $D=3$ → 거리 $\sqrt3$  (b) 두 점 $(1,0,0)$, $(2,1,1)$, $\langle1,1,1\rangle$은 두 방향벡터와 수직",
  sol=[r"$P(s)-Q(t)=\langle2+s-t,\ -2-s,\ t-3\rangle$ → $D=(s-t+2)^2+(s+2)^2+(t-3)^2$",
       r"$D_s=2(s-t+2)+2(s+2)=0$ → $2s-t+4=0$;  $D_t=-2(s-t+2)+2(t-3)=0$ → $-s+2t-5=0$",
       r"$\Rightarrow s=-1,\ t=2$. $D_{ss}=4,\ D_{tt}=4,\ D_{st}=-2$ → $D=16-4=12>0$, $D_{ss}>0$ → 최소, $D(-1,2)=1+1+1=3$ → 거리 $\sqrt3$",
       r"(b) $P(-1)=(1,0,0),\ Q(2)=(2,1,1)$, $\overrightarrow{PQ}=\langle1,1,1\rangle$: $\langle1,1,1\rangle\cdot\langle1,-1,0\rangle=0$, $\langle1,1,1\rangle\cdot\langle1,0,-1\rangle=0$",
       r"외적 공식: $\mathbf n=\langle1,-1,0\rangle\times\langle1,0,-1\rangle=\langle1,1,1\rangle$, $\dfrac{|\mathbf n\cdot\langle-2,2,3\rangle|}{\sqrt3}=\dfrac{3}{\sqrt3}=\sqrt3$ ✓"],
  check=_c)


# ───────── 14.8 ─────────
def _c():
    a, b, c = 3, 6, 9
    assert R(1, a) + R(2, b) + R(3, c) == 1
    lam_ = -a**2*b*c                      # bc = -λ/a²
    assert a*c == R(-2*lam_, b**2) and a*b == R(-3*lam_, c**2)
    assert EQ(R(3*6*9, 6), 27)
    import random
    random.seed(5)
    for _ in range(500):
        p1, p2 = random.uniform(0.01, 0.98), random.uniform(0.01, 0.98)
        if p1 + p2 >= 0.99:
            continue
        p3 = 1 - p1 - p2
        aa, bb, cc = 1/p1, 2/p2, 3/p3
        assert aa*bb*cc/6 >= 27 - 1e-9
P(id="4-68", ch=14, sec="14.8", type="14-lagrange", src="2024 중간 4번 유형 (사면체 부피 최소)",
  q=r"점 $(1,2,3)$을 지나는 평면이 제1팔분공간에서 세 좌표평면과 함께 사면체를 만든다. 라그랑주 승수법으로 이 사면체의 부피의 최솟값과 그때의 평면의 방정식을 구하라.",
  hint=r"평면 $\dfrac xa+\dfrac yb+\dfrac zc=1$ ($a,b,c>0$)이 $(1,2,3)$을 지나므로 제약조건 $\dfrac1a+\dfrac2b+\dfrac3c=1$, 목적함수 $V=\dfrac{abc}{6}$.",
  ans=r"최소 부피 $27$, 평면 $\dfrac x3+\dfrac y6+\dfrac z9=1$ (즉 $6x+3y+2z=18$)",
  sol=[r"$\nabla(abc)=\lambda\nabla\big(\tfrac1a+\tfrac2b+\tfrac3c\big)$: $bc=-\dfrac{\lambda}{a^2},\ ac=-\dfrac{2\lambda}{b^2},\ ab=-\dfrac{3\lambda}{c^2}$",
       r"각 식에 $a,\ b,\ c$를 곱하면 $abc=-\dfrac{\lambda}{a}=-\dfrac{2\lambda}{b}=-\dfrac{3\lambda}{c}$ → $\dfrac1a=\dfrac2b=\dfrac3c$",
       r"제약조건: 세 값의 합이 $1$ → 각각 $\tfrac13$ → $a=3,\ b=6,\ c=9$",
       r"$V=\dfrac{3\cdot6\cdot9}{6}=27$ (경계로 갈수록 $V\to\infty$이므로 최소), 평면 $\dfrac x3+\dfrac y6+\dfrac z9=1$"],
  check=_c)


def _c():
    for k in (1, 2, 3):
        s2 = 1/sqrt(k)
        assert EQ(k*s2, sqrt(k)) and EQ(k*s2**2, 1)
    import random
    random.seed(6)
    lo, hi = 10.0, 0.0
    for _ in range(4000):
        v = [random.gauss(0, 1) for _ in range(3)]
        nrm = sum(q**4 for q in v)**0.25
        v = [q/nrm for q in v]
        val = sum(q*q for q in v)
        lo, hi = min(lo, val), max(hi, val)
    assert lo >= 1 - 1e-12 and hi <= float(sqrt(3)) + 1e-12
P(id="4-69", ch=14, sec="14.8", type="14-lagrange", src="교재 14.8 심화형 (경우 나누기)",
  q=r"곡면 $x^4+y^4+z^4=1$ 위에서 $f(x,y,z)=x^2+y^2+z^2$의 최댓값과 최솟값을 구하라.",
  hint=r"$2x=4\lambda x^3$ → $x=0$ 또는 $x^2=\dfrac1{2\lambda}$. $y,z$도 마찬가지 → $0$이 아닌 좌표들은 제곱이 모두 같아요. $0$이 아닌 좌표의 개수 $k$로 나누어 보세요.",
  ans=r"최솟값 $1$ (예: $(\pm1,0,0)$), 최댓값 $\sqrt3$ ($x^2=y^2=z^2=\tfrac1{\sqrt3}$)",
  sol=[r"$\nabla f=\lambda\nabla g$: $2x=4\lambda x^3,\ 2y=4\lambda y^3,\ 2z=4\lambda z^3$",
       r"각 좌표는 $0$이거나 제곱이 $\dfrac{1}{2\lambda}=:c$. $0$이 아닌 좌표가 $k$개 ($k=1,2,3$)면 제약 $kc^2=1$ → $c=\dfrac1{\sqrt k}$",
       r"$f=kc=\dfrac{k}{\sqrt k}=\sqrt k$ → $k=1$: $1$, $k=2$: $\sqrt2$, $k=3$: $\sqrt3$",
       r"닫힌 유계 곡면이므로 최댓값 $\sqrt3$, 최솟값 $1$ (예: $(\pm1,0,0)$, $\big(\pm3^{-1/4},\pm3^{-1/4},\pm3^{-1/4}\big)$)"],
  check=_c)


def _c():
    lam, mu = symbols('lam mu')
    eqs = [0 - (lam*2*x + mu), 0 - (lam*2*y + mu), 1 - (-lam + mu), x**2 + y**2 - z, x + y + z - 4]
    sols = solve(eqs, [x, y, z, lam, mu], dict=True)
    pts = sorted([(q[x], q[y], q[z]) for q in sols], key=lambda p: p[2])
    assert pts == [(1, 1, 2), (-2, -2, 8)]
P(id="4-70", ch=14, sec="14.8", type="14-lagrange2", src="교재 14.8 심화형 (제약 2개: 가장 높은·낮은 점)",
  q=r"포물면 $z=x^2+y^2$과 평면 $x+y+z=4$의 교선(타원) 위에서 가장 높은 점과 가장 낮은 점을 라그랑주 승수법으로 구하라.",
  hint=r"목적함수 $f=z$, 제약 $g=x^2+y^2-z=0$, $h=x+y+z-4=0$. $\langle0,0,1\rangle=\lambda\langle2x,2y,-1\rangle+\mu\langle1,1,1\rangle$의 첫 두 성분을 비교하면 $x=y$.",
  ans=r"가장 높은 점 $(-2,-2,8)$, 가장 낮은 점 $(1,1,2)$",
  sol=[r"$0=2\lambda x+\mu,\ 0=2\lambda y+\mu,\ 1=-\lambda+\mu$",
       r"$\lambda=0$이면 $\mu=0$인데 셋째 식 모순 → $\lambda\ne0$ → $x=y$",
       r"$z=2x^2$, $2x+2x^2=4$ → $x^2+x-2=0$ → $x=1$ 또는 $-2$",
       r"점 $(1,1,2)$, $(-2,-2,8)$ → 가장 낮은 점 $(1,1,2)$, 가장 높은 점 $(-2,-2,8)$"],
  check=_c)


def _c():
    f = x**3 + y**3 + 3*x*y
    assert EQ(f.subs({x: 1, y: 1}), 5) and EQ(f.subs({x: -1, y: -1}), 1)
    s_ = 1 - sqrt(3)
    assert EQ(s_**2 - 2*s_, 2) and EQ(s_**3 - 3*s_*s_ + 3*s_, 1 - 3*sqrt(3))
    disc = s_**2 - 4*s_
    assert float(disc) > 0
    xa = (s_ + sqrt(disc))/2; ya = (s_ - sqrt(disc))/2
    assert EQ(xa**2 + ya**2, 2) and EQ(f.subs({x: xa, y: ya}), 1 - 3*sqrt(3))
    fl = lambdify((x, y), f, 'mpmath')
    vals = [float(fl(mp.sqrt(2)*mp.cos(tq), mp.sqrt(2)*mp.sin(tq))) for tq in [2*mp.pi*k/4000 for k in range(4000)]]
    assert abs(max(vals) - 5) < 1e-6 and abs(min(vals) - float(1 - 3*sqrt(3))) < 1e-5
P(id="4-71", ch=14, sec="14.8", type="14-lagrange", src="2022 중간 블럭1 6번 유형",
  q=r"원 $x^2+y^2=2$ 위에서 $f(x,y)=x^3+y^3+3xy$의 최댓값과 최솟값을 라그랑주 승수법으로 구하라.",
  hint=r"$3x^2+3y=2\lambda x,\ 3y^2+3x=2\lambda y$. 첫 식에 $y$, 둘째 식에 $x$를 곱해 빼면 $(x-y)(xy-x-y)=0$. 둘째 경우는 $s=x+y,\ p=xy$로 두면 $f=s^3-3ps+3p$.",
  ans=r"최댓값 $5$ (점 $(1,1)$),  최솟값 $1-3\sqrt3$ ($x+y=xy=1-\sqrt3$인 두 점)",
  sol=[r"$3x^2y+3y^2=2\lambda xy=3xy^2+3x^2$ → $3xy(x-y)-3(x-y)(x+y)=0$ → $(x-y)(xy-x-y)=0$",
       r"$x=y$: $2x^2=2$ → $(1,1)$: $f=5$,  $(-1,-1)$: $f=1$",
       r"$xy=x+y=s$: $x^2+y^2=s^2-2s=2$ → $s=1\pm\sqrt3$. 실근 조건 $s^2-4s\ge0$ → $s=1-\sqrt3$만 가능",
       r"$f=s^3-3ps+3p=s^3-3s^2+3s=(s-1)^3+1=(-\sqrt3)^3+1=1-3\sqrt3\approx-4.20$",
       r"후보 $5,\ 1,\ 1-3\sqrt3$ 비교 → 최댓값 $5$, 최솟값 $1-3\sqrt3$"],
  check=_c)


# ───────── 14.4 미분가능성의 정의 (추가) ─────────
def _c():
    import random
    f = x*y*(x + y)/(x**2 + y**2)
    hh = symbols('hh', nonzero=True, real=True)
    assert f.subs({x: hh, y: 0}) == 0 and f.subs({x: 0, y: hh}) == 0
    assert simplify(f.subs({x: hh, y: hh}) - hh) == 0          # Δy=Δx 이면 Δz=Δx → ε1+ε2=1
    tt = symbols('tt', positive=True)
    assert simplify(f.subs({x: tt/sqrt(2), y: tt/sqrt(2)})/tt - 1/sqrt(2)) == 0
    fn = lambdify((x, y), f)
    rnd = random.Random(3)
    for _ in range(400):
        X, Y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        assert abs(fn(X, Y)) <= abs(X + Y)/2 + 1e-12        # 연속: |f| ≤ |x+y|/2
P(id="4-121", ch=14, sec="14.4", type="14-differentiable", src="수업 자료 밖 · 교재 14.4 정의 7 반례",
  q=r"$f(x,y)=\dfrac{xy(x+y)}{x^2+y^2}\ \big((x,y)\ne(0,0)\big)$, $f(0,0)=0$ 일 때<br>(a) $f$ 가 원점에서 연속임을 보여라.  (b) $f_x(0,0),\ f_y(0,0)$ 을 구하라.<br>(c) $f$ 가 원점에서 미분가능하지 않음을 정의를 이용해 보여라.<br>(d) $\mathbf u=\big\langle\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big\rangle$ 방향의 방향도함수 $D_{\mathbf u}f(0,0)$ 을 정의로 구하고 $\nabla f(0,0)\cdot\mathbf u$ 와 비교하라.",
  hint=r"(a) $|xy|\le\tfrac12(x^2+y^2)$. (c) 미분가능하다고 가정하고 $\Delta y=\Delta x$ 를 넣어 모순을 찾아요. (d) $D_{\mathbf u}f(0,0)=\displaystyle\lim_{t\to0}\frac{f(t/\sqrt2,\ t/\sqrt2)-f(0,0)}{t}$",
  ans=r"(a) $|f|\le\tfrac12|x+y|\to0$  (b) $0,\ 0$  (c) $\Delta y=\Delta x$ 이면 $\varepsilon_1+\varepsilon_2=1$ → 모순  (d) $D_{\mathbf u}f(0,0)=\dfrac1{\sqrt2}\ne0=\nabla f(0,0)\cdot\mathbf u$",
  sol=[r"(a) $|xy|\le\tfrac12(x^2+y^2)$ 이므로 $|f(x,y)|\le\tfrac12|x+y|\to0=f(0,0)$ → 원점에서 연속",
       r"(b) $f(h,0)=0,\ f(0,h)=0$ → $f_x(0,0)=\displaystyle\lim_{h\to0}\frac{0-0}{h}=0$, 같은 방법으로 $f_y(0,0)=0$",
       r"(c) 미분가능하다면 (b)에 의해 $\Delta z=f(\Delta x,\Delta y)=\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 이고 $\varepsilon_1,\varepsilon_2\to0$ 이어야 해요. $\Delta y=\Delta x\ne0$ 이면 $f(\Delta x,\Delta x)=\dfrac{(\Delta x)^2\cdot2\Delta x}{2(\Delta x)^2}=\Delta x$ 이므로 $\Delta x=(\varepsilon_1+\varepsilon_2)\Delta x$, 즉 $\varepsilon_1+\varepsilon_2=1$",
       r"$\Delta x\to0$ 이면 $(\Delta x,\Delta y)\to(0,0)$ 이라 $\varepsilon_1+\varepsilon_2\to0$ 이어야 하는데 늘 $1$ → 모순. 원점에서 <b>미분가능하지 않아요</b>.",
       r"(d) $f\big(\tfrac{t}{\sqrt2},\tfrac{t}{\sqrt2}\big)=\dfrac{\frac{t^2}{2}\cdot\sqrt2\,t}{t^2}=\dfrac{t}{\sqrt2}$ → $D_{\mathbf u}f(0,0)=\dfrac1{\sqrt2}$. 그런데 $\nabla f(0,0)\cdot\mathbf u=0$ — 공식 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ 는 미분가능할 때만 쓸 수 있어요."],
  check=_c)


def _c():
    import random
    hp = symbols('hp', positive=True)
    f, g = sqrt(Abs(x*y)), Abs(x*y)
    for F in (f, g):
        assert F.subs({x: hp, y: 0}) == 0 and F.subs({x: 0, y: hp}) == 0
    assert simplify(f.subs({x: hp, y: hp})/hp) == 1 and simplify(f.subs({x: -hp, y: -hp})/(-hp)) == -1
    rnd = random.Random(5)
    for _ in range(400):                                      # (b) ε1 = sgn(Δx)|Δy| 이면 ε1Δx = |ΔxΔy|, |ε1| ≤ |Δy|
        X, Y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        e1 = (1 if X > 0 else -1)*abs(Y)
        assert abs(e1*X - abs(X*Y)) < 1e-14 and abs(e1) <= abs(Y)
P(id="4-122", ch=14, sec="14.4", type="14-differentiable", src="수업 자료 밖 · 교재 14.4 정의 7 심화",
  q=r"다음 두 함수가 원점에서 미분가능한지 정의를 이용해 판정하라.<br>(a) $f(x,y)=\sqrt{|xy|}$  (b) $g(x,y)=|xy|$",
  hint=r"두 함수 모두 $x$축·$y$축 위에서 $0$ 이라 편도함수는 모두 $0$ 이에요. (a)는 $\Delta y=\Delta x$ 를 넣어 보고, (b)는 $|\Delta x\Delta y|=\Big(\dfrac{|\Delta x|}{\Delta x}|\Delta y|\Big)\Delta x$ 로 써 보세요.",
  ans=r"(a) 미분가능하지 않음 ($\Delta y=\Delta x$ 이면 $\varepsilon_1+\varepsilon_2=\pm1$)  (b) 미분가능 ($\varepsilon_1=\pm|\Delta y|,\ \varepsilon_2=0$)",
  sol=[r"두 함수 모두 축 위에서 $0$ 이므로 $f_x(0,0)=f_y(0,0)=0$, $\ g_x(0,0)=g_y(0,0)=0$ → 미분가능하다면 $\Delta z=\varepsilon_1\Delta x+\varepsilon_2\Delta y$, $\ \varepsilon_1,\varepsilon_2\to0$",
       r"(a) $\Delta y=\Delta x\ne0$ 이면 $\Delta z=\sqrt{(\Delta x)^2}=|\Delta x|=(\varepsilon_1+\varepsilon_2)\Delta x$ → $\varepsilon_1+\varepsilon_2=\dfrac{|\Delta x|}{\Delta x}=\pm1$ 이라 $0$ 으로 갈 수 없어요 → <b>미분가능하지 않음</b> (연속이고 편도함수도 있지만 미분불가능한 예)",
       r"(b) $\Delta x\ne0$ 이면 $\varepsilon_1=\dfrac{|\Delta x|}{\Delta x}\,|\Delta y|$, $\ \Delta x=0$ 이면 $\varepsilon_1=0$, 그리고 $\varepsilon_2=0$ 으로 두면 $\varepsilon_1\Delta x+\varepsilon_2\Delta y=|\Delta x||\Delta y|=\Delta z$",
       r"$|\varepsilon_1|\le|\Delta y|\to0$ 이므로 정의를 만족 → $g$ 는 원점에서 <b>미분가능</b> (접평면 $z=0$). 절댓값이 있어도 미분가능할 수 있어요."],
  check=_c)


def _c():
    hh = symbols('hh', real=True)
    ft = 4*(x - 1) - (y - 2) + (x - 1)**2*(y - 2) + 3*(y - 2)**2   # f_x(1,2)=4, f_y(1,2)=-1 인 함수로 확인
    assert diff(ft, x).subs({x: 1, y: 2}) == 4 and diff(ft, y).subs({x: 1, y: 2}) == -1
    F0 = ft.subs({x: 1, y: 2})
    assert limit((ft.subs({x: 1 + 3*hh, y: 2 + 4*hh}) - F0)/hh, hh, 0) == 8
    assert limit((ft.subs({x: 1 + hh**2, y: 2 - hh}) - F0)/hh, hh, 0) == 1
    assert limit((ft.subs({x: 1 + R(3, 5)*hh, y: 2 + R(4, 5)*hh}) - F0)/hh, hh, 0) == R(8, 5)
P(id="4-123", ch=14, sec="14.4", type="14-differentiable", src="수업 자료 밖 · 교재 14.5·14.6 증명 방식 (정의 7 이용)",
  q=r"$f$ 는 점 $(1,2)$ 에서 미분가능하고 $f_x(1,2)=4,\ f_y(1,2)=-1$ 이다. 미분가능성의 정의 $\Delta z=f_x\Delta x+f_y\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 를 이용하여 다음을 구하라.<br>(a) $\displaystyle\lim_{h\to0}\frac{f(1+3h,\ 2+4h)-f(1,2)}{h}$  (b) $\displaystyle\lim_{h\to0}\frac{f(1+h^2,\ 2-h)-f(1,2)}{h}$<br>(c) (a)를 이용해 $\mathbf u=\big\langle\tfrac35,\tfrac45\big\rangle$ 방향의 방향도함수 $D_{\mathbf u}f(1,2)$",
  hint=r"$\Delta x,\ \Delta y$ 를 $h$ 로 나타내 정의에 넣고 $h$ 로 나누세요. $h\to0$ 이면 $(\Delta x,\Delta y)\to(0,0)$ 이라 $\varepsilon_1,\varepsilon_2\to0$ 이에요.",
  ans=r"(a) $8$  (b) $1$  (c) $\dfrac85$",
  sol=[r"(a) $\Delta x=3h,\ \Delta y=4h$ 이면 $\Delta z=4(3h)+(-1)(4h)+\varepsilon_1(3h)+\varepsilon_2(4h)$ 이므로 $$\frac{\Delta z}{h}=8+3\varepsilon_1+4\varepsilon_2\to8$$",
       r"(b) $\Delta x=h^2,\ \Delta y=-h$ 이면 $\Delta z=4h^2+h+\varepsilon_1h^2-\varepsilon_2h$ 이므로 $$\frac{\Delta z}{h}=4h+1+\varepsilon_1h-\varepsilon_2\to1$$ 곡선을 따라가도 정의만 있으면 계산돼요.",
       r"(c) $D_{\mathbf u}f(1,2)=\displaystyle\lim_{t\to0}\frac{f(1+\frac35t,\ 2+\frac45t)-f(1,2)}{t}$ 에서 $t=5h$ 로 두면 (a) 극한의 $\dfrac15$ → $\dfrac85$ (확인: $\nabla f\cdot\mathbf u=\dfrac{4\cdot3-1\cdot4}{5}=\dfrac85$)"],
  check=_c)

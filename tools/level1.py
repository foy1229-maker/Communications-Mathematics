"""1단계 · 기본 (30문제) — 공식 바로 적용"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    assert EQ((4 - 2)**2 + (1 + 1)**2 + (2 - 3)**2, 9)
P(id="1-01", ch=12, sec="12.1", type="12-sphere", src="과제 12.1 #17 유형",
  q=r"중심이 $(2,-1,3)$이고 점 $(4,1,2)$를 지나는 구의 방정식을 구하라.",
  hint=r"반지름은 중심과 주어진 점 사이의 거리예요.",
  ans=r"$(x-2)^2+(y+1)^2+(z-3)^2=9$",
  sol=[r"반지름: $r=\sqrt{(4-2)^2+(1+1)^2+(2-3)^2}=\sqrt{4+4+1}=3$",
       r"구의 방정식 $(x-h)^2+(y-k)^2+(z-l)^2=r^2$에 대입하면 $(x-2)^2+(y+1)^2+(z-3)^2=9$"],
  check=_c)


def _c():
    vv = Matrix([2, -6, 3])
    assert EQ(vv / vv.norm(), [R(2, 7), R(-6, 7), R(3, 7)])
    sol = solve([s + 3*t - 5, 2*s - t - 3], [s, t])
    assert sol[s] == 2 and sol[t] == 1
P(id="1-02", ch=12, sec="12.2", type="12-vec", src="과제 12.2 #25 · #45 유형",
  q=r"(a) $\mathbf v=\langle 2,-6,3\rangle$와 같은 방향의 단위벡터를 구하라.<br>(b) $\mathbf a=\langle 1,2\rangle$, $\mathbf b=\langle 3,-1\rangle$일 때 $\mathbf c=\langle 5,3\rangle$을 $\mathbf c=s\mathbf a+t\mathbf b$로 나타내는 $s,\,t$를 구하라.",
  hint=r"(a) $\mathbf u=\dfrac{\mathbf v}{|\mathbf v|}$  (b) 성분끼리 비교해 연립방정식을 세워요.",
  ans=r"(a) $\left\langle \tfrac27,\,-\tfrac67,\,\tfrac37\right\rangle$  (b) $s=2,\ t=1$",
  sol=[r"(a) $|\mathbf v|=\sqrt{4+36+9}=7$이므로 $\mathbf u=\tfrac17\langle 2,-6,3\rangle=\left\langle \tfrac27,-\tfrac67,\tfrac37\right\rangle$",
       r"(b) $s\langle1,2\rangle+t\langle3,-1\rangle=\langle5,3\rangle \Rightarrow s+3t=5,\ \ 2s-t=3$",
       r"두 번째 식에서 $t=2s-3$을 첫 식에 넣으면 $7s-9=5$, 즉 $s=2,\ t=1$"],
  check=_c)


def _c():
    a = Matrix([2, 1, -1]); b = Matrix([1, 2, 1])
    assert EQ(acos(a.dot(b) / (a.norm() * b.norm())), pi / 3)
    assert EQ(a / a.norm(), [2 / sqrt(6), 1 / sqrt(6), -1 / sqrt(6)])
P(id="1-03", ch=12, sec="12.3", type="12-dot", src="복습 12장 기초1 · 강의 12.3 ex5 유형",
  q=r"$\mathbf a=\langle 2,1,-1\rangle$, $\mathbf b=\langle 1,2,1\rangle$ 사이의 각 $\theta$를 구하고, $\mathbf a$의 방향코사인 $\cos\alpha,\ \cos\beta,\ \cos\gamma$를 구하라.",
  hint=r"$\cos\theta=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf a||\mathbf b|}$, 방향코사인은 $\dfrac{\mathbf a}{|\mathbf a|}$의 성분이에요.",
  ans=r"$\theta=\dfrac{\pi}{3}$,  $(\cos\alpha,\cos\beta,\cos\gamma)=\left(\tfrac{2}{\sqrt6},\ \tfrac{1}{\sqrt6},\ -\tfrac{1}{\sqrt6}\right)$",
  sol=[r"$\mathbf a\cdot\mathbf b=2+2-1=3$,  $|\mathbf a|=|\mathbf b|=\sqrt6$",
       r"$\cos\theta=\dfrac{3}{\sqrt6\,\sqrt6}=\dfrac12 \Rightarrow \theta=\dfrac{\pi}{3}$",
       r"$\dfrac{\mathbf a}{|\mathbf a|}=\left\langle\tfrac{2}{\sqrt6},\tfrac{1}{\sqrt6},-\tfrac{1}{\sqrt6}\right\rangle$ (확인: 제곱의 합 $=\tfrac{4+1+1}{6}=1$)"],
  check=_c)


def _c():
    a = Matrix([1, 2, 2]); b = Matrix([3, -1, 4])
    assert EQ(a.dot(b) / a.norm(), 3)
    assert EQ(a.dot(b) / a.dot(a) * a, [1, 2, 2])
P(id="1-04", ch=12, sec="12.3", type="12-proj", src="강의 12.3 ex6 · 복습 12장 기초2 유형",
  q=r"$\mathbf a=\langle 1,2,2\rangle$, $\mathbf b=\langle 3,-1,4\rangle$일 때 스칼라 사영 $\operatorname{comp}_{\mathbf a}\mathbf b$와 벡터 사영 $\operatorname{proj}_{\mathbf a}\mathbf b$를 구하라.",
  hint=r"$\operatorname{comp}_{\mathbf a}\mathbf b=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf a|}$,  $\operatorname{proj}_{\mathbf a}\mathbf b=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\,\mathbf a$",
  ans=r"$\operatorname{comp}_{\mathbf a}\mathbf b=3$,  $\operatorname{proj}_{\mathbf a}\mathbf b=\langle 1,2,2\rangle$",
  sol=[r"$\mathbf a\cdot\mathbf b=3-2+8=9$,  $|\mathbf a|=\sqrt{1+4+4}=3$",
       r"$\operatorname{comp}_{\mathbf a}\mathbf b=\dfrac{9}{3}=3$",
       r"$\operatorname{proj}_{\mathbf a}\mathbf b=\dfrac{9}{9}\langle1,2,2\rangle=\langle1,2,2\rangle$"],
  check=_c)


def _c():
    a = Matrix([1, 3, -2]); b = Matrix([2, -1, 1])
    c = a.cross(b)
    assert EQ(c, [1, -5, -7]) and EQ(c.norm(), 5 * sqrt(3))
    assert c.dot(a) == 0 and c.dot(b) == 0
P(id="1-05", ch=12, sec="12.4", type="12-cross", src="강의 12.4 ex1 · 과제 12.4 #31 유형",
  q=r"$\mathbf a=\langle 1,3,-2\rangle$, $\mathbf b=\langle 2,-1,1\rangle$에 대해 $\mathbf a\times\mathbf b$를 구하고, 두 벡터가 만드는 평행사변형의 넓이를 구하라.",
  hint=r"행렬식 $\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}$을 전개하고, 넓이는 $|\mathbf a\times\mathbf b|$예요.",
  ans=r"$\mathbf a\times\mathbf b=\langle 1,-5,-7\rangle$,  넓이 $=5\sqrt3$",
  sol=[r"$\mathbf a\times\mathbf b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ 1&3&-2\\ 2&-1&1\end{vmatrix}=(3-2)\mathbf i-(1+4)\mathbf j+(-1-6)\mathbf k=\langle 1,-5,-7\rangle$",
       r"검산: $\mathbf a\cdot(\mathbf a\times\mathbf b)=1-15+14=0$, $\mathbf b\cdot(\mathbf a\times\mathbf b)=2+5-7=0$",
       r"넓이 $=|\mathbf a\times\mathbf b|=\sqrt{1+25+49}=\sqrt{75}=5\sqrt3$"],
  check=_c)


def _c():
    Pp = Matrix([1, -2, 4]); Q = Matrix([3, 1, 2]); d = Q - Pp
    assert EQ(d, [2, 3, -2])
    tt = solve(4 - 2*t, t)[0]
    assert EQ(Pp + tt * d, [5, 4, 0])
P(id="1-06", ch=12, sec="12.5", type="12-line", src="강의 12.5 ex1 · 과제 12.5 #7 유형",
  q=r"두 점 $P(1,-2,4)$, $Q(3,1,2)$를 지나는 직선의 매개방정식과 대칭방정식을 구하라. 또 이 직선이 $xy$평면과 만나는 점을 구하라.",
  hint=r"방향벡터 $\mathbf v=\overrightarrow{PQ}$, $xy$평면은 $z=0$이에요.",
  ans=r"$x=1+2t,\ y=-2+3t,\ z=4-2t$;  $\dfrac{x-1}{2}=\dfrac{y+2}{3}=\dfrac{z-4}{-2}$;  교점 $(5,4,0)$",
  sol=[r"$\mathbf v=\overrightarrow{PQ}=\langle 2,3,-2\rangle$",
       r"매개방정식: $x=1+2t,\ y=-2+3t,\ z=4-2t$",
       r"대칭방정식: $\dfrac{x-1}{2}=\dfrac{y+2}{3}=\dfrac{z-4}{-2}$",
       r"$z=0 \Rightarrow 4-2t=0 \Rightarrow t=2$, 교점 $(1+4,\,-2+6,\,0)=(5,4,0)$"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    assert limit(sin(3*t) / t, t, 0) == 3
    assert EQ(log(0 + 1), 0) and EQ(sqrt(4 - 0), 2)
P(id="1-07", ch=13, sec="13.1", type="13-func", src="강의 13.1 ex1 · ex3 유형",
  q=r"$\mathbf r(t)=\left\langle \dfrac{\sin 3t}{t},\ \ln(t+1),\ \sqrt{4-t}\right\rangle$의 정의역을 구하고 $\displaystyle\lim_{t\to0}\mathbf r(t)$를 구하라.",
  hint=r"정의역은 세 성분 함수 정의역의 교집합, 극한은 성분별로 구해요.",
  ans=r"정의역 $(-1,0)\cup(0,4]$,  $\displaystyle\lim_{t\to0}\mathbf r(t)=\langle 3,0,2\rangle$",
  sol=[r"성분별 조건: $t\neq0$,  $t+1>0$,  $4-t\ge0$ $\Rightarrow$ $(-1,0)\cup(0,4]$",
       r"$\displaystyle\lim_{t\to0}\frac{\sin3t}{t}=\lim_{t\to0}3\cdot\frac{\sin3t}{3t}=3$,  $\ln1=0$,  $\sqrt4=2$",
       r"$\therefore\ \displaystyle\lim_{t\to0}\mathbf r(t)=\langle 3,0,2\rangle$"],
  check=_c)


def _c():
    rr = Matrix([2*t, t**2, log(t)]); d = rr.diff(t).subs(t, 1)
    assert EQ(d / d.norm(), [R(2, 3), R(2, 3), R(1, 3)])
P(id="1-08", ch=13, sec="13.2", type="13-deriv", src="강의 13.2 ex1 · 과제 13.2 #19 유형",
  q=r"$\mathbf r(t)=\langle 2t,\ t^2,\ \ln t\rangle$에 대해 $\mathbf r'(t)$와 $t=1$에서의 단위접선벡터 $\mathbf T(1)$을 구하라.",
  hint=r"$\mathbf T(t)=\dfrac{\mathbf r'(t)}{|\mathbf r'(t)|}$",
  ans=r"$\mathbf r'(t)=\left\langle 2,\ 2t,\ \tfrac1t\right\rangle$,  $\mathbf T(1)=\left\langle \tfrac23,\tfrac23,\tfrac13\right\rangle$",
  sol=[r"$\mathbf r'(t)=\left\langle 2,\ 2t,\ \tfrac1t\right\rangle$",
       r"$\mathbf r'(1)=\langle2,2,1\rangle$,  $|\mathbf r'(1)|=\sqrt{4+4+1}=3$",
       r"$\mathbf T(1)=\tfrac13\langle 2,2,1\rangle=\left\langle\tfrac23,\tfrac23,\tfrac13\right\rangle$"],
  check=_c)


def _c():
    assert EQ(integrate(cos(t), (t, 0, pi/2)), 1)
    assert EQ(integrate(sin(2*t), (t, 0, pi/2)), 1)
    assert EQ(integrate(t, (t, 0, pi/2)), pi**2 / 8)
P(id="1-09", ch=13, sec="13.2", type="13-integ", src="강의 13.2 ex5 · 과제 13.2 #40 유형",
  q=r"$\displaystyle\int_0^{\pi/2}\big(\cos t\,\mathbf i+\sin 2t\,\mathbf j+t\,\mathbf k\big)\,dt$를 계산하라.",
  hint=r"벡터함수의 적분은 성분별로 해요.",
  ans=r"$\mathbf i+\mathbf j+\dfrac{\pi^2}{8}\mathbf k$",
  sol=[r"$\displaystyle\int_0^{\pi/2}\cos t\,dt=\Big[\sin t\Big]_0^{\pi/2}=1$",
       r"$\displaystyle\int_0^{\pi/2}\sin2t\,dt=\Big[-\tfrac12\cos2t\Big]_0^{\pi/2}=\tfrac12+\tfrac12=1$",
       r"$\displaystyle\int_0^{\pi/2}t\,dt=\Big[\tfrac{t^2}{2}\Big]_0^{\pi/2}=\dfrac{\pi^2}{8}$",
       r"$\therefore\ \mathbf i+\mathbf j+\dfrac{\pi^2}{8}\mathbf k$"],
  check=_c)


def _c():
    rr = Matrix([3*cos(t), 3*sin(t), 4*t])
    sp = simplify(rr.diff(t).norm())
    assert EQ(sp, 5) and EQ(integrate(sp, (t, 0, 2*pi)), 10*pi)
P(id="1-10", ch=13, sec="13.3", type="13-arc", src="강의 13.3 ex1 · 복습 13장 기초2 유형",
  q=r"나선 $\mathbf r(t)=\langle 3\cos t,\ 3\sin t,\ 4t\rangle$의 $0\le t\le 2\pi$ 부분의 길이를 구하라.",
  hint=r"$L=\displaystyle\int_a^b|\mathbf r'(t)|\,dt$",
  ans=r"$10\pi$",
  sol=[r"$\mathbf r'(t)=\langle -3\sin t,\ 3\cos t,\ 4\rangle$",
       r"$|\mathbf r'(t)|=\sqrt{9\sin^2t+9\cos^2t+16}=\sqrt{25}=5$",
       r"$L=\displaystyle\int_0^{2\pi}5\,dt=10\pi$"],
  check=_c)


# ───────── Ch.14 ─────────
def _c():
    g = 4 - x**2 - 4*y**2
    assert EQ(g.subs({x: 0, y: 0}), 4)
    assert solve([diff(g, x), diff(g, y)], [x, y]) == {x: 0, y: 0}
P(id="1-11", ch=14, sec="14.1", type="14-domain", src="강의 14.1 ex1 · ex2 · 과제 14.1 #10 유형",
  q=r"$f(x,y)=\ln(4-x^2-4y^2)$의 정의역과 치역을 구하라.",
  hint=r"로그 안은 양수여야 해요. 로그 안의 식이 가질 수 있는 값의 범위를 먼저 구해요.",
  ans=r"정의역 $\left\{(x,y)\ \middle|\ \dfrac{x^2}{4}+y^2<1\right\}$ (타원의 내부),  치역 $(-\infty,\ \ln 4]$",
  sol=[r"$4-x^2-4y^2>0 \iff \dfrac{x^2}{4}+y^2<1$ : 경계를 제외한 타원 내부",
       r"정의역에서 $0<4-x^2-4y^2\le 4$ (최댓값 4는 원점에서)",
       r"$\ln$은 증가함수이므로 $f$의 치역은 $(-\infty,\ \ln4]$"],
  check=_c)


def _c():
    f = (x**2*y - 3*x*y**2 + 4) / (x + y)
    assert EQ(f.subs({x: 1, y: 2}), -2)
P(id="1-12", ch=14, sec="14.2", type="14-limit", src="강의 14.2 ex4 · ex5 · 과제 14.2 #8 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(1,2)}\frac{x^2y-3xy^2+4}{x+y}$를 구하라.",
  hint=r"분모가 0이 아니면 유리함수는 연속이라 대입하면 돼요.",
  ans=r"$-2$",
  sol=[r"분모 $x+y\to3\neq0$이므로 유리함수는 $(1,2)$에서 연속",
       r"대입: $\dfrac{1\cdot2-3\cdot1\cdot4+4}{1+2}=\dfrac{2-12+4}{3}=-2$"],
  check=_c)


def _c():
    f = 2*x*y / (x**2 + 3*y**2)
    assert EQ(limit(f.subs(y, 0), x, 0), 0)
    assert EQ(limit(f.subs(y, x), x, 0), R(1, 2))
P(id="1-13", ch=14, sec="14.2", type="14-dne", src="강의 14.2 ex1 · ex2 · 과제 14.2 #15 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{2xy}{x^2+3y^2}$가 존재하지 않음을 보여라.",
  hint=r"$x$축과 직선 $y=x$, 두 경로를 비교해 보세요.",
  ans=r"$x$축을 따라 $0$, $y=x$를 따라 $\tfrac12$ → 극한은 존재하지 않는다.",
  sol=[r"$x$축($y=0$)을 따라: $\dfrac{0}{x^2}=0 \to 0$",
       r"$y=x$를 따라: $\dfrac{2x^2}{x^2+3x^2}=\dfrac{2}{4}=\dfrac12 \to \dfrac12$",
       r"두 경로의 극한이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    f = x**2*y**3 - 3*x + log(y)
    assert EQ(diff(f, x).subs({x: 2, y: 1}), 1) and EQ(diff(f, y).subs({x: 2, y: 1}), 13)
P(id="1-14", ch=14, sec="14.3", type="14-partial", src="강의 14.3 ex1 유형",
  q=r"$f(x,y)=x^2y^3-3x+\ln y$일 때 $f_x(2,1)$, $f_y(2,1)$을 구하라.",
  hint=r"$f_x$는 $y$를 상수로, $f_y$는 $x$를 상수로 보고 미분해요.",
  ans=r"$f_x(2,1)=1$,  $f_y(2,1)=13$",
  sol=[r"$f_x=2xy^3-3 \Rightarrow f_x(2,1)=4-3=1$",
       r"$f_y=3x^2y^2+\dfrac1y \Rightarrow f_y(2,1)=12+1=13$"],
  check=_c)


def _c():
    f = x * exp(x*y)
    fxy = diff(f, x, y); fyx = diff(f, y, x)
    assert EQ(fxy, fyx) and EQ(fxy, exp(x*y) * (2*x + x**2*y))
P(id="1-15", ch=14, sec="14.3", type="14-higher", src="강의 14.3 ex7 (Clairaut 정리) 유형",
  q=r"$f(x,y)=xe^{xy}$의 $f_{xy}$와 $f_{yx}$를 구하고 두 값이 같음을 확인하라.",
  hint=r"$f_{xy}=(f_x)_y$: 먼저 $x$로, 그다음 $y$로 미분해요.",
  ans=r"$f_{xy}=f_{yx}=(2x+x^2y)\,e^{xy}$",
  sol=[r"$f_x=e^{xy}+xy\,e^{xy}=(1+xy)e^{xy}$",
       r"$f_{xy}=x\,e^{xy}+(1+xy)\,x\,e^{xy}=(2x+x^2y)e^{xy}$",
       r"$f_y=x^2e^{xy}$,  $f_{yx}=2x\,e^{xy}+x^2y\,e^{xy}=(2x+x^2y)e^{xy}$",
       r"두 혼합 편도함수가 연속이므로 Clairaut 정리대로 $f_{xy}=f_{yx}$"],
  check=_c)


def _c():
    f = x**2 + 3*y**2
    L = f.subs({x: 1, y: 1}) + diff(f, x).subs({x: 1, y: 1})*(x - 1) + diff(f, y).subs({x: 1, y: 1})*(y - 1)
    assert EQ(L, 2*x + 6*y - 4)
P(id="1-16", ch=14, sec="14.4", type="14-tangent", src="과제 14.4 #4 · 복습 14.4–6 기초3 유형",
  q=r"곡면 $z=x^2+3y^2$ 위의 점 $(1,1,4)$에서의 접평면의 방정식을 구하라.",
  hint=r"$z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$",
  ans=r"$z=2x+6y-4$",
  sol=[r"$f_x=2x,\ f_y=6y \Rightarrow f_x(1,1)=2,\ f_y(1,1)=6$",
       r"$z-4=2(x-1)+6(y-1)$",
       r"$\therefore\ z=2x+6y-4$"],
  check=_c)


def _c():
    zz = (x**2*y - y**2).subs({x: 1 + t**2, y: 3*t})
    assert EQ(diff(zz, t).subs(t, 1), 18)
P(id="1-17", ch=14, sec="14.5", type="14-chain", src="강의 14.5 ex1 · 과제 14.5 #1 유형",
  q=r"$z=x^2y-y^2$, $x=1+t^2$, $y=3t$일 때 $t=1$에서 $\dfrac{dz}{dt}$를 구하라.",
  hint=r"$\dfrac{dz}{dt}=\dfrac{\partial z}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial z}{\partial y}\dfrac{dy}{dt}$",
  ans=r"$18$",
  sol=[r"$z_x=2xy,\ \ z_y=x^2-2y,\ \ \dfrac{dx}{dt}=2t,\ \ \dfrac{dy}{dt}=3$",
       r"$t=1$일 때 $x=2,\ y=3$",
       r"$\dfrac{dz}{dt}=(2\cdot2\cdot3)(2)+(4-6)(3)=24-6=18$"],
  check=_c)


def _c():
    f = x**2*y + 2*y**2
    g = grad(f, [x, y]).subs({x: 1, y: 2})
    assert EQ(g.dot(Matrix([R(3, 5), R(4, 5)])), R(48, 5))
P(id="1-18", ch=14, sec="14.6", type="14-dir", src="강의 14.6 ex4 · 과제 14.6 #13 유형",
  q=r"$f(x,y)=x^2y+2y^2$의 점 $(1,2)$에서 벡터 $\mathbf v=\langle 3,4\rangle$ 방향으로의 방향도함수를 구하라.",
  hint=r"$D_{\mathbf u}f=\nabla f\cdot\mathbf u$, 이때 $\mathbf u$는 반드시 단위벡터!",
  ans=r"$\dfrac{48}{5}$",
  sol=[r"$\nabla f=\langle 2xy,\ x^2+4y\rangle \Rightarrow \nabla f(1,2)=\langle 4,9\rangle$",
       r"$\mathbf u=\dfrac{\mathbf v}{|\mathbf v|}=\left\langle\tfrac35,\tfrac45\right\rangle$",
       r"$D_{\mathbf u}f(1,2)=4\cdot\tfrac35+9\cdot\tfrac45=\dfrac{12+36}{5}=\dfrac{48}{5}$"],
  check=_c)


def _c():
    f = x**2 + x*y + y**2 - 3*x
    cp = solve([diff(f, x), diff(f, y)], [x, y])
    assert cp == {x: 2, y: -1}
    D = (diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2)
    assert D == 3 and diff(f, x, 2) == 2 and EQ(f.subs(cp), -3)
P(id="1-19", ch=14, sec="14.7", type="14-crit", src="강의 14.7 ex1 유형",
  q=r"$f(x,y)=x^2+xy+y^2-3x$의 임계점을 구하고 2계 도함수 판정법으로 분류하라.",
  hint=r"$f_x=f_y=0$을 풀고 $D=f_{xx}f_{yy}-(f_{xy})^2$의 부호를 봐요.",
  ans=r"임계점 $(2,-1)$에서 극소, 극솟값 $f(2,-1)=-3$",
  sol=[r"$f_x=2x+y-3=0,\ \ f_y=x+2y=0 \Rightarrow (x,y)=(2,-1)$",
       r"$f_{xx}=2,\ f_{yy}=2,\ f_{xy}=1 \Rightarrow D=4-1=3>0$, $f_{xx}>0$",
       r"$\therefore$ 극소, $f(2,-1)=4-2+1-6=-3$"],
  check=_c)


# ───────── Ch.15 ─────────
def _c():
    f = x**2 + y
    mids = [R(1, 2), R(3, 2)]
    approx = sum(f.subs({x: a, y: b}) for a in mids for b in mids) * 1
    assert approx == 9
    assert EQ(integrate(f, (y, 0, 2), (x, 0, 2)), R(28, 3))
P(id="1-20", ch=15, sec="15.1", type="15-rect", src="강의 15.1 ex3 (중점법칙) · ex4 유형",
  q=r"$R=[0,2]\times[0,2]$에서 $\displaystyle\iint_R (x^2+y)\,dA$를 (a) $m=n=2$인 중점법칙으로 근사하고 (b) 정확한 값을 구하라.",
  hint=r"(a) 작은 정사각형 4개의 중심 $(\tfrac12,\tfrac12),(\tfrac12,\tfrac32),(\tfrac32,\tfrac12),(\tfrac32,\tfrac32)$에서 함숫값, $\Delta A=1$  (b) 푸비니 정리.",
  ans=r"(a) $9$  (b) $\dfrac{28}{3}$",
  sol=[r"(a) 중점에서의 값: $0.75,\ 1.75,\ 2.75,\ 3.75$ $\Rightarrow$ 합 $9$, $\Delta A=1$ 이므로 근삿값 $9$",
       r"(b) $\displaystyle\int_0^2\!\!\int_0^2(x^2+y)\,dy\,dx=\int_0^2\Big[x^2y+\tfrac{y^2}{2}\Big]_0^2dx=\int_0^2(2x^2+2)\,dx$",
       r"$=\dfrac{16}{3}+4=\dfrac{28}{3}$ (근삿값 $9$와 비교)"],
  check=_c)


def _c():
    assert EQ(integrate(x*y, (y, x**2, x), (x, 0, 1)), R(1, 24))
P(id="1-21", ch=15, sec="15.2", type="15-general", src="강의 15.2 ex1 유형 (Type I)",
  q=r"$D=\{(x,y)\mid 0\le x\le1,\ x^2\le y\le x\}$에서 $\displaystyle\iint_D xy\,dA$를 구하라.",
  hint=r"Type I 영역: 안쪽을 $y$로 $x^2$부터 $x$까지 적분해요.",
  ans=r"$\dfrac{1}{24}$",
  sol=[r"$\displaystyle\int_0^1\!\!\int_{x^2}^{x}xy\,dy\,dx=\int_0^1 x\Big[\tfrac{y^2}{2}\Big]_{x^2}^{x}dx=\int_0^1\frac{x^3-x^5}{2}\,dx$",
       r"$=\dfrac12\left(\dfrac14-\dfrac16\right)=\dfrac{1}{24}$"],
  check=_c)


def _c():
    assert EQ(integrate(r**2 * r, (r, 0, 2), (th, 0, 2*pi)), 8*pi)
P(id="1-22", ch=15, sec="15.3", type="15-polar", src="강의 15.3 ex1 · 복습 15.1–3 기초6 유형",
  q=r"$D$가 원판 $x^2+y^2\le4$일 때 $\displaystyle\iint_D (x^2+y^2)\,dA$를 극좌표로 계산하라.",
  hint=r"$x^2+y^2=r^2$, $dA=r\,dr\,d\theta$ — $r$을 빠뜨리지 마세요.",
  ans=r"$8\pi$",
  sol=[r"$D: 0\le r\le2,\ 0\le\theta\le2\pi$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r^2\cdot r\,dr\,d\theta=2\pi\Big[\tfrac{r^4}{4}\Big]_0^2=2\pi\cdot4=8\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(x + 2*y*z, (x, 0, 2), (y, 0, 1), (z, 0, 3)), 15)
P(id="1-23", ch=15, sec="15.6", type="15-triple", src="강의 15.6 ex1 유형",
  q=r"$B=[0,2]\times[0,1]\times[0,3]$에서 $\displaystyle\iiint_B (x+2yz)\,dV$를 구하라.",
  hint=r"직육면체에서는 순서와 상관없이 푸비니 정리로 차례로 적분해요. 곱으로 분리되는 항은 따로 계산하면 편해요.",
  ans=r"$15$",
  sol=[r"$\displaystyle\iiint_B x\,dV=\Big(\int_0^2x\,dx\Big)\Big(\int_0^1dy\Big)\Big(\int_0^3dz\Big)=2\cdot1\cdot3=6$",
       r"$\displaystyle\iiint_B 2yz\,dV=2\Big(\int_0^2dx\Big)\Big(\int_0^1y\,dy\Big)\Big(\int_0^3z\,dz\Big)=2\cdot2\cdot\tfrac12\cdot\tfrac92=9$",
       r"합: $6+9=15$"],
  check=_c)


def _c():
    assert EQ([4*cos(2*pi/3), 4*sin(2*pi/3)], [-2, 2*sqrt(3)])
    assert EQ(sqrt(1 + 1), sqrt(2)) and EQ(atan2(-1, 1) + 2*pi, 7*pi/4)
P(id="1-24", ch=15, sec="15.7", type="15-cyl", src="강의 15.7 ex1 유형",
  q=r"(a) 원주좌표 $\left(4,\ \tfrac{2\pi}{3},\ -1\right)$을 직교좌표로 나타내라.<br>(b) 직교좌표 $(1,-1,5)$를 원주좌표로 나타내라.",
  hint=r"$x=r\cos\theta,\ y=r\sin\theta,\ z=z$ / $r=\sqrt{x^2+y^2},\ \tan\theta=\dfrac yx$ (사분면 확인!)",
  ans=r"(a) $(-2,\ 2\sqrt3,\ -1)$  (b) $\left(\sqrt2,\ \tfrac{7\pi}{4},\ 5\right)$",
  sol=[r"(a) $x=4\cos\tfrac{2\pi}{3}=-2$,  $y=4\sin\tfrac{2\pi}{3}=2\sqrt3$,  $z=-1$",
       r"(b) $r=\sqrt{1+1}=\sqrt2$,  $\tan\theta=-1$이고 점이 제4사분면 위에 있으므로 $\theta=\tfrac{7\pi}{4}$ (또는 $-\tfrac{\pi}{4}$),  $z=5$"],
  check=_c)


def _c():
    assert EQ(integrate(rho**2 * rho**2 * sin(ph), (rho, 0, 1), (th, 0, 2*pi), (ph, 0, pi)), 4*pi/5)
P(id="1-25", ch=15, sec="15.8", type="15-sph", src="강의 15.8 ex3 · 과제 15.8 #23 유형",
  q=r"$B$가 단위구 $x^2+y^2+z^2\le1$일 때 $\displaystyle\iiint_B (x^2+y^2+z^2)\,dV$를 구면좌표로 계산하라.",
  hint=r"$x^2+y^2+z^2=\rho^2$, $dV=\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$",
  ans=r"$\dfrac{4\pi}{5}$",
  sol=[r"$B: 0\le\rho\le1,\ 0\le\theta\le2\pi,\ 0\le\phi\le\pi$",
       r"$\displaystyle\int_0^{\pi}\!\!\int_0^{2\pi}\!\!\int_0^1\rho^2\cdot\rho^2\sin\phi\,d\rho\,d\theta\,d\phi=\Big[-\cos\phi\Big]_0^{\pi}\cdot2\pi\cdot\frac15$",
       r"$=2\cdot2\pi\cdot\dfrac15=\dfrac{4\pi}{5}$"],
  check=_c)


# ───────── Ch.16 ─────────
def _c():
    f = x**2*y + y*z**3
    assert EQ(grad(f, [x, y, z]), [2*x*y, x**2 + z**3, 3*y*z**2])
    assert EQ(grad(f, [x, y, z]).subs({x: 1, y: 2, z: -1}), [4, 0, 6])
P(id="1-26", ch=16, sec="16.1", type="16-field", src="강의 16.1 ex6 · 과제 16.1 #25 유형",
  q=r"$f(x,y,z)=x^2y+yz^3$의 기울기 벡터장 $\nabla f$를 구하고 $\nabla f(1,2,-1)$을 구하라.",
  hint=r"$\nabla f=\langle f_x,\ f_y,\ f_z\rangle$",
  ans=r"$\nabla f=\langle 2xy,\ x^2+z^3,\ 3yz^2\rangle$,  $\nabla f(1,2,-1)=\langle 4,0,6\rangle$",
  sol=[r"$f_x=2xy,\ \ f_y=x^2+z^3,\ \ f_z=3yz^2$",
       r"$(1,2,-1)$ 대입: $\langle 4,\ 1-1,\ 6\rangle=\langle4,0,6\rangle$"],
  check=_c)


def _c():
    xx, yy = 3*t, 4*t
    assert EQ(integrate((xx + yy) * sqrt(diff(xx, t)**2 + diff(yy, t)**2), (t, 0, 1)), R(35, 2))
P(id="1-27", ch=16, sec="16.2", type="16-scalar", src="강의 16.2 ex1 유형",
  q=r"$C$가 $(0,0)$에서 $(3,4)$까지의 선분일 때 $\displaystyle\int_C (x+y)\,ds$를 구하라.",
  hint=r"$\mathbf r(t)=\langle 3t,4t\rangle$, $0\le t\le1$이면 $ds=|\mathbf r'(t)|\,dt$",
  ans=r"$\dfrac{35}{2}$",
  sol=[r"$\mathbf r(t)=\langle3t,4t\rangle,\ 0\le t\le1$,  $|\mathbf r'(t)|=\sqrt{9+16}=5$",
       r"$\displaystyle\int_C(x+y)\,ds=\int_0^1 7t\cdot5\,dt=35\cdot\frac12=\frac{35}{2}$"],
  check=_c)


def _c():
    assert EQ(integrate(t**2 * 1 + t**2 * 2*t, (t, 0, 1)), R(5, 6))
P(id="1-28", ch=16, sec="16.2", type="16-vector", src="강의 16.2 ex7 유형",
  q=r"$\mathbf F(x,y)=y\,\mathbf i+x^2\,\mathbf j$이고 $C:\ \mathbf r(t)=\langle t,\ t^2\rangle,\ 0\le t\le1$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$",
  ans=r"$\dfrac56$",
  sol=[r"$\mathbf F(\mathbf r(t))=\langle t^2,\ t^2\rangle$,  $\mathbf r'(t)=\langle 1,\ 2t\rangle$",
       r"$\mathbf F\cdot\mathbf r'=t^2+2t^3$",
       r"$\displaystyle\int_0^1(t^2+2t^3)\,dt=\frac13+\frac12=\frac56$"],
  check=_c)


def _c():
    Pf, Qf = 2*x + y, x + 3*y**2
    assert EQ(diff(Pf, y), diff(Qf, x))
    f = x**2 + x*y + y**3
    assert EQ(diff(f, x), Pf) and EQ(diff(f, y), Qf)
P(id="1-29", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 ex2 · ex3 유형",
  q=r"$\mathbf F(x,y)=(2x+y)\,\mathbf i+(x+3y^2)\,\mathbf j$가 보존장인지 판정하고, 보존장이면 $\mathbf F=\nabla f$인 $f$를 구하라.",
  hint=r"$\dfrac{\partial P}{\partial y}=\dfrac{\partial Q}{\partial x}$인지 확인 → $f_x=P$를 $x$로 적분",
  ans=r"보존장,  $f(x,y)=x^2+xy+y^3+K$",
  sol=[r"$P_y=1,\ Q_x=1 \Rightarrow P_y=Q_x$ (정의역 $\mathbb R^2$) 이므로 보존장",
       r"$f_x=2x+y \Rightarrow f=x^2+xy+g(y)$",
       r"$f_y=x+g'(y)=x+3y^2 \Rightarrow g(y)=y^3+K$",
       r"$\therefore\ f(x,y)=x^2+xy+y^3+K$"],
  check=_c)


def _c():
    assert EQ(integrate(2 * r, (r, 0, 2), (th, 0, 2*pi)), 8*pi)
    xx, yy = 2*cos(t), 2*sin(t)
    assert EQ(integrate((xx - yy)*diff(xx, t) + (xx + yy)*diff(yy, t), (t, 0, 2*pi)), 8*pi)
P(id="1-30", ch=16, sec="16.4", type="16-green", src="강의 16.4 ex1 · 복습 16.1–4 기초5 유형",
  q=r"$C$가 원 $x^2+y^2=4$ (반시계 방향)일 때 $\displaystyle\oint_C (x-y)\,dx+(x+y)\,dy$를 그린 정리로 구하라.",
  hint=r"$\displaystyle\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)dA$",
  ans=r"$8\pi$",
  sol=[r"$P=x-y,\ Q=x+y \Rightarrow Q_x-P_y=1-(-1)=2$",
       r"$\displaystyle\oint_C=\iint_D 2\,dA=2\cdot4\pi=8\pi$ (원의 넓이 $=4\pi$)"],
  check=_c)

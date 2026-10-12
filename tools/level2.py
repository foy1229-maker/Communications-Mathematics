"""2단계 · 표준 (30문제) — 강의 예제·과제 유형"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    Pp, Q, Rr = Matrix([1, 0, 2]), Matrix([2, 1, 0]), Matrix([0, 3, 1])
    n = (Q - Pp).cross(Rr - Pp)
    assert EQ(n, [5, 3, 4])
    for pt in (Pp, Q, Rr):
        assert 5*pt[0] + 3*pt[1] + 4*pt[2] == 13
P(id="2-01", ch=12, sec="12.5", type="12-plane", src="강의 12.5 ex5 · 과제 12.5 #31 유형",
  q=r"세 점 $P(1,0,2)$, $Q(2,1,0)$, $R(0,3,1)$을 지나는 평면의 방정식을 구하라.",
  hint=r"법선벡터 $\mathbf n=\overrightarrow{PQ}\times\overrightarrow{PR}$",
  ans=r"$5x+3y+4z=13$",
  sol=[r"$\overrightarrow{PQ}=\langle1,1,-2\rangle,\ \ \overrightarrow{PR}=\langle-1,3,-1\rangle$",
       r"$\mathbf n=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\1&1&-2\\-1&3&-1\end{vmatrix}=(-1+6)\mathbf i-(-1-2)\mathbf j+(3+1)\mathbf k=\langle5,3,4\rangle$",
       r"$5(x-1)+3(y-0)+4(z-2)=0 \Rightarrow 5x+3y+4z=13$",
       r"검산: $Q$: $10+3+0=13$, $R$: $0+9+4=13$ ✓"],
  check=_c)


def _c():
    sol = solve([2 + t - (1 + 2*s), 1 - t - (-4 + 4*s)], [t, s])
    assert sol == {t: 1, s: 1}
    assert EQ(3*sol[t], 2 + sol[s])
    assert EQ([2 + 1, 1 - 1, 3], [3, 0, 3])
P(id="2-02", ch=12, sec="12.5", type="12-line", src="과제 12.5 #19 유형",
  q=r"두 직선 $L_1:\ x=2+t,\ y=1-t,\ z=3t$ 와 $L_2:\ x=1+2s,\ y=-4+4s,\ z=2+s$가 평행한지, 한 점에서 만나는지, 꼬인 위치인지 판정하고, 만나면 교점을 구하라.",
  hint=r"방향벡터가 평행한지 먼저 보고, 아니면 $x,y$ 식으로 $t,s$를 구해 $z$에서 일치하는지 확인해요.",
  ans=r"한 점에서 만난다. 교점 $(3,0,3)$",
  sol=[r"방향벡터 $\langle1,-1,3\rangle$과 $\langle2,4,1\rangle$은 스칼라배가 아니므로 평행하지 않다.",
       r"$2+t=1+2s,\ \ 1-t=-4+4s$ 를 더하면 $3=-3+6s \Rightarrow s=1,\ t=1$",
       r"$z$ 확인: $3t=3,\ \ 2+s=3$ 로 일치 → 두 직선은 만난다.",
       r"교점: $t=1$ 대입 → $(3,0,3)$"],
  check=_c)


def _c():
    n1, n2 = Matrix([1, 2, -1]), Matrix([2, -1, 1])
    assert EQ(abs(n1.dot(n2)) / (n1.norm() * n2.norm()), R(1, 6))
    vdir = n1.cross(n2)
    assert EQ(vdir, [1, -3, -5])
    pt = solve([x + 2*y - 3, 2*x - y - 1], [x, y])
    assert pt == {x: 1, y: 1}
P(id="2-03", ch=12, sec="12.5", type="12-plane", src="강의 12.5 ex7 · 과제 12.5 #51 유형",
  q=r"두 평면 $x+2y-z=3$, $2x-y+z=1$ 사이의 각 $\theta$를 구하고, 두 평면의 교선의 대칭방정식을 구하라.",
  hint=r"$\cos\theta=\dfrac{|\mathbf n_1\cdot\mathbf n_2|}{|\mathbf n_1||\mathbf n_2|}$, 교선의 방향은 $\mathbf n_1\times\mathbf n_2$, 교선 위의 한 점은 $z=0$을 넣어 찾아요.",
  ans=r"$\theta=\cos^{-1}\!\left(\tfrac16\right)$,  $\dfrac{x-1}{1}=\dfrac{y-1}{-3}=\dfrac{z}{-5}$",
  sol=[r"$\mathbf n_1=\langle1,2,-1\rangle,\ \mathbf n_2=\langle2,-1,1\rangle$,  $\mathbf n_1\cdot\mathbf n_2=2-2-1=-1$,  $|\mathbf n_1|=|\mathbf n_2|=\sqrt6$",
       r"$\cos\theta=\dfrac{|-1|}{6}=\dfrac16 \Rightarrow \theta=\cos^{-1}\tfrac16$ (두 평면의 각은 예각으로)",
       r"$\mathbf v=\mathbf n_1\times\mathbf n_2=\langle 2-1,\ -2-1,\ -1-4\rangle=\langle1,-3,-5\rangle$",
       r"$z=0$: $x+2y=3,\ 2x-y=1 \Rightarrow (1,1,0)$",
       r"교선: $\dfrac{x-1}{1}=\dfrac{y-1}{-3}=\dfrac{z}{-5}$"],
  check=_c)


def _c():
    assert Matrix([[1, 2, 0], [0, 1, 3], [2, 0, 1]]).det() == 13
    assert Matrix([[1, 2, 3], [2, 1, 0], [0, 3, 6]]).det() == 0
P(id="2-04", ch=12, sec="12.4", type="12-triple", src="강의 12.4 ex5 유형",
  q=r"(a) $\mathbf a=\langle1,2,0\rangle$, $\mathbf b=\langle0,1,3\rangle$, $\mathbf c=\langle2,0,1\rangle$이 만드는 평행육면체의 부피를 구하라.<br>(b) $\mathbf u=\langle1,2,3\rangle$, $\mathbf v=\langle2,1,0\rangle$, $\mathbf w=\langle0,3,6\rangle$이 한 평면 위에 있음(공면)을 보여라.",
  hint=r"$V=|\mathbf a\cdot(\mathbf b\times\mathbf c)|$ = 행렬식의 절댓값, 삼중적이 $0$이면 공면.",
  ans=r"(a) $13$  (b) $\mathbf u\cdot(\mathbf v\times\mathbf w)=0$ 이므로 공면",
  sol=[r"(a) $\begin{vmatrix}1&2&0\\0&1&3\\2&0&1\end{vmatrix}=1(1-0)-2(0-6)+0=13 \Rightarrow V=13$",
       r"(b) $\mathbf v\times\mathbf w=\langle 6,-12,6\rangle$",
       r"$\mathbf u\cdot(\mathbf v\times\mathbf w)=6-24+18=0$ → 부피가 0인 평행육면체, 즉 세 벡터는 공면"],
  check=_c)


def _c():
    assert Matrix([4, -1, 2]).dot(Matrix([4, 2, 1]) - Matrix([1, 0, 2])) == 8
    assert EQ(10 * 20 * cos(pi/6), 100*sqrt(3))
P(id="2-05", ch=12, sec="12.3", type="12-proj", src="강의 12.3 ex8 (일) 유형",
  q=r"(a) 힘 $\mathbf F=\langle4,-1,2\rangle$ (N)이 물체를 점 $P(1,0,2)$에서 $Q(4,2,1)$까지 옮길 때 한 일을 구하라 (거리 단위 m).<br>(b) 크기 $10\,\mathrm N$의 힘으로 수평면과 $30^\circ$를 이루는 방향으로 끌어 물체를 수평으로 $20\,\mathrm m$ 옮겼을 때 한 일을 구하라.",
  hint=r"$W=\mathbf F\cdot\mathbf D=|\mathbf F||\mathbf D|\cos\theta$",
  ans=r"(a) $8\,\mathrm J$  (b) $100\sqrt3\,\mathrm J$",
  sol=[r"(a) $\mathbf D=\overrightarrow{PQ}=\langle3,2,-1\rangle$,  $W=\mathbf F\cdot\mathbf D=12-2-2=8\ \mathrm J$",
       r"(b) $W=|\mathbf F||\mathbf D|\cos30^\circ=10\cdot20\cdot\dfrac{\sqrt3}{2}=100\sqrt3\ \mathrm J$"],
  check=_c)


def _c():
    assert EQ(abs(2*2 - (-1) + 2*3 - 5) / 3, 2)
    assert EQ(abs(10 - 1) / sqrt(1 + 4 + 4), 3)
P(id="2-06", ch=12, sec="12.5", type="12-dist", src="강의 12.5 ex8 · ex9 · 과제 12.5 #75 유형",
  q=r"(a) 점 $(2,-1,3)$에서 평면 $2x-y+2z=5$까지의 거리를 구하라.<br>(b) 평행한 두 평면 $x-2y+2z=1$, $2x-4y+4z=20$ 사이의 거리를 구하라.",
  hint=r"$D=\dfrac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$, (b)는 먼저 두 평면의 계수를 같게 맞춰요.",
  ans=r"(a) $2$  (b) $3$",
  sol=[r"(a) $D=\dfrac{|2\cdot2-(-1)+2\cdot3-5|}{\sqrt{4+1+4}}=\dfrac{6}{3}=2$",
       r"(b) 두 번째 평면을 2로 나누면 $x-2y+2z=10$",
       r"$D=\dfrac{|10-1|}{\sqrt{1+4+4}}=\dfrac93=3$ (첫 평면 위의 점 $(1,0,0)$에서 둘째 평면까지의 거리와 같다)"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    rr = Matrix([1 + 2*sin(t), exp(2*t), t**3 + t])
    assert EQ(rr.subs(t, 0), [1, 1, 0]) and EQ(rr.diff(t).subs(t, 0), [2, 2, 1])
P(id="2-07", ch=13, sec="13.2", type="13-deriv", src="과제 13.2 #27 유형",
  q=r"곡선 $x=1+2\sin t,\ y=e^{2t},\ z=t^3+t$ 위의 점 $(1,1,0)$에서의 접선의 매개방정식을 구하라.",
  hint=r"먼저 점 $(1,1,0)$에 대응하는 $t$를 찾고, 접선의 방향은 $\mathbf r'(t)$예요.",
  ans=r"$x=1+2u,\ \ y=1+2u,\ \ z=u$",
  sol=[r"$(1,1,0)$은 $t=0$에 대응 ($1+2\sin0=1,\ e^0=1,\ 0$)",
       r"$\mathbf r'(t)=\langle 2\cos t,\ 2e^{2t},\ 3t^2+1\rangle \Rightarrow \mathbf r'(0)=\langle2,2,1\rangle$",
       r"접선: $x=1+2u,\ y=1+2u,\ z=u$"],
  check=_c)


def _c():
    rr = Matrix([(exp(2*t) + 1) / 2, 2*sin(t), 3*t**2 - 1])
    assert EQ(rr.diff(t), [exp(2*t), 2*cos(t), 6*t]) and EQ(rr.subs(t, 0), [1, 0, -1])
P(id="2-08", ch=13, sec="13.2", type="13-integ", src="강의 13.2 (부정적분·상수벡터) 유형",
  q=r"$\mathbf r'(t)=\langle e^{2t},\ 2\cos t,\ 6t\rangle$이고 $\mathbf r(0)=\langle 1,0,-1\rangle$일 때 $\mathbf r(t)$를 구하라.",
  hint=r"성분별로 적분하면 상수벡터 $\mathbf C$가 생기고, $\mathbf r(0)$으로 $\mathbf C$를 정해요.",
  ans=r"$\mathbf r(t)=\left\langle \dfrac{e^{2t}+1}{2},\ 2\sin t,\ 3t^2-1\right\rangle$",
  sol=[r"$\mathbf r(t)=\left\langle \tfrac12e^{2t},\ 2\sin t,\ 3t^2\right\rangle+\mathbf C$",
       r"$\mathbf r(0)=\left\langle\tfrac12,0,0\right\rangle+\mathbf C=\langle1,0,-1\rangle \Rightarrow \mathbf C=\left\langle\tfrac12,0,-1\right\rangle$",
       r"$\therefore\ \mathbf r(t)=\left\langle \tfrac{e^{2t}+1}{2},\ 2\sin t,\ 3t^2-1\right\rangle$"],
  check=_c)


def _c():
    rr = Matrix([2*t, t**2, t**3/3])
    sp2 = rr.diff(t).dot(rr.diff(t))
    assert EQ(sp2, (t**2 + 2)**2) and EQ(integrate(t**2 + 2, (t, 0, 1)), R(7, 3))
P(id="2-09", ch=13, sec="13.3", type="13-arc", src="과제 13.3 #5 유형",
  q=r"$\mathbf r(t)=\left\langle 2t,\ t^2,\ \tfrac13t^3\right\rangle$, $0\le t\le1$의 길이를 구하라.",
  hint=r"$|\mathbf r'(t)|$의 근호 안이 완전제곱이 되는지 보세요.",
  ans=r"$\dfrac73$",
  sol=[r"$\mathbf r'(t)=\langle2,\ 2t,\ t^2\rangle$",
       r"$|\mathbf r'(t)|=\sqrt{4+4t^2+t^4}=\sqrt{(t^2+2)^2}=t^2+2$",
       r"$L=\displaystyle\int_0^1(t^2+2)\,dt=\frac13+2=\frac73$"],
  check=_c)


def _c():
    rr = Matrix([1 + 2*t, 3 - t, 2*t])
    assert EQ(rr.diff(t).norm(), 3)
    assert EQ(rr.subs(t, 2), [5, 1, 4])
P(id="2-10", ch=13, sec="13.3", type="13-arcfn", src="과제 13.3 #15 유형",
  q=r"$\mathbf r(t)=(1+2t)\,\mathbf i+(3-t)\,\mathbf j+2t\,\mathbf k$에 대해<br>(a) 점 $P(1,3,0)$에서 $t$가 증가하는 방향으로 잰 호의 길이 함수 $s(t)$를 구하고, 곡선을 $s$로 재매개화하라.<br>(b) $P$에서 곡선을 따라 $6$만큼 이동한 점을 구하라.",
  hint=r"$s(t)=\displaystyle\int_0^t|\mathbf r'(u)|\,du$, 이후 $t$를 $s$에 대한 식으로 바꿔 대입해요.",
  ans=r"(a) $s=3t$,  $\mathbf r(s)=\left\langle 1+\tfrac{2s}{3},\ 3-\tfrac{s}{3},\ \tfrac{2s}{3}\right\rangle$  (b) $(5,1,4)$",
  sol=[r"$P$는 $t=0$,  $|\mathbf r'(t)|=|\langle2,-1,2\rangle|=3$",
       r"$s(t)=\displaystyle\int_0^t3\,du=3t \Rightarrow t=\dfrac s3$",
       r"$\mathbf r(s)=\left\langle 1+\tfrac{2s}{3},\ 3-\tfrac{s}{3},\ \tfrac{2s}{3}\right\rangle$",
       r"(b) $s=6$ 대입: $(1+4,\ 3-2,\ 4)=(5,1,4)$"],
  check=_c)


# ───────── Ch.14 ─────────
def _c():
    f = (x - y)**2 / (x**2 + y**2)
    assert EQ(limit(f.subs(y, 0), x, 0), 1) and EQ(limit(f.subs(y, x), x, 0), 0)
P(id="2-11", ch=14, sec="14.2", type="14-dne", src="과제 14.2 #15 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{(x-y)^2}{x^2+y^2}$이 존재하지 않음을 보여라.",
  hint=r"$x$축과 $y=x$ 두 경로에서의 값을 비교해요.",
  ans=r"$x$축을 따라 $1$, $y=x$를 따라 $0$ → 존재하지 않는다.",
  sol=[r"$x$축($y=0$): $\dfrac{x^2}{x^2}=1\to1$",
       r"$y=x$: $\dfrac{0}{2x^2}=0\to0$",
       r"경로에 따라 극한이 다르므로 존재하지 않는다."],
  check=_c)


def _c():
    T = 100 / (1 + x**2 + 2*y**2)
    assert EQ(diff(T, x).subs({x: 1, y: 1}), R(-25, 2)) and EQ(diff(T, y).subs({x: 1, y: 1}), -25)
P(id="2-12", ch=14, sec="14.3", type="14-partial", src="과제 14.3 #82 유형",
  q=r"금속판 위 점 $(x,y)$의 온도가 $T(x,y)=\dfrac{100}{1+x^2+2y^2}$ (°C, $x,y$는 m)일 때, 점 $(1,1)$에서 (a) $x$방향 (b) $y$방향으로의 온도 변화율을 구하라.",
  hint=r"방향별 변화율 = 편도함수 $T_x,\ T_y$",
  ans=r"(a) $-\dfrac{25}{2}\ ^\circ\mathrm C/\mathrm m$  (b) $-25\ ^\circ\mathrm C/\mathrm m$",
  sol=[r"$T_x=\dfrac{-200x}{(1+x^2+2y^2)^2},\ \ T_y=\dfrac{-400y}{(1+x^2+2y^2)^2}$",
       r"$(1,1)$에서 분모 $=(1+1+2)^2=16$",
       r"$T_x(1,1)=-\dfrac{200}{16}=-\dfrac{25}{2}$,  $T_y(1,1)=-\dfrac{400}{16}=-25$"],
  check=_c)


def _c():
    F = x**3 + y**3 + z**3 + 2*x*y*z - 4
    pt = {x: 1, y: -1, z: 2}
    assert EQ(F.subs(pt), 0)
    assert EQ((-diff(F, x) / diff(F, z)).subs(pt), R(1, 10))
    assert EQ((-diff(F, y) / diff(F, z)).subs(pt), R(-7, 10))
P(id="2-13", ch=14, sec="14.3", type="14-implicit", src="강의 14.3 ex5 · 14.5 ex9 유형",
  q=r"방정식 $x^3+y^3+z^3+2xyz=4$가 $z$를 $x,y$의 함수로 정할 때, 점 $(1,-1,2)$에서 $\dfrac{\partial z}{\partial x}$, $\dfrac{\partial z}{\partial y}$를 구하라.",
  hint=r"$F(x,y,z)=x^3+y^3+z^3+2xyz-4$로 두면 $\dfrac{\partial z}{\partial x}=-\dfrac{F_x}{F_z}$",
  ans=r"$\dfrac{\partial z}{\partial x}=\dfrac{1}{10}$,  $\dfrac{\partial z}{\partial y}=-\dfrac{7}{10}$",
  sol=[r"$F_x=3x^2+2yz,\ \ F_y=3y^2+2xz,\ \ F_z=3z^2+2xy$",
       r"$(1,-1,2)$에서 $F_x=3-4=-1,\ \ F_y=3+4=7,\ \ F_z=12-2=10$",
       r"$\dfrac{\partial z}{\partial x}=-\dfrac{-1}{10}=\dfrac1{10}$,  $\dfrac{\partial z}{\partial y}=-\dfrac{7}{10}$"],
  check=_c)


def _c():
    f = sqrt(x**2 + y**2)
    L = 5 + R(3, 5)*(x - 3) + R(4, 5)*(y - 4)
    assert EQ(diff(f, x).subs({x: 3, y: 4}), R(3, 5)) and EQ(diff(f, y).subs({x: 3, y: 4}), R(4, 5))
    assert EQ(L, (3*x + 4*y) / 5)
    assert EQ(L.subs({x: R(303, 100), y: R(396, 100)}), R(4986, 1000))
P(id="2-14", ch=14, sec="14.4", type="14-tangent", src="강의 14.4 ex2 · 과제 14.4 #17 유형",
  q=r"$f(x,y)=\sqrt{x^2+y^2}$의 점 $(3,4)$에서의 선형화 $L(x,y)$를 구하고, 이를 이용해 $f(3.03,\ 3.96)$의 근삿값을 구하라.",
  hint=r"$L(x,y)=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$",
  ans=r"$L(x,y)=\dfrac{3x+4y}{5}$,  $f(3.03,\,3.96)\approx4.986$",
  sol=[r"$f(3,4)=5$,  $f_x=\dfrac{x}{\sqrt{x^2+y^2}},\ f_y=\dfrac{y}{\sqrt{x^2+y^2}} \Rightarrow f_x(3,4)=\tfrac35,\ f_y(3,4)=\tfrac45$",
       r"$L(x,y)=5+\tfrac35(x-3)+\tfrac45(y-4)=\dfrac{3x+4y}{5}$",
       r"$f(3.03,3.96)\approx 5+\tfrac35(0.03)+\tfrac45(-0.04)=5+0.018-0.032=4.986$"],
  check=_c)


def _c():
    f = x**2 - x*y + 2*y**2
    dz = diff(f, x).subs({x: 2, y: 1})*R(1, 10) + diff(f, y).subs({x: 2, y: 1})*R(-1, 10)
    Dz = f.subs({x: R(21, 10), y: R(9, 10)}) - f.subs({x: 2, y: 1})
    assert EQ(dz, R(1, 10)) and EQ(Dz, R(14, 100))
P(id="2-15", ch=14, sec="14.4", type="14-diff", src="과제 14.4 #33 · #39 유형",
  q=r"$z=x^2-xy+2y^2$에서 $(x,y)$가 $(2,1)$에서 $(2.1,\ 0.9)$로 변할 때 $\Delta z$와 $dz$를 구해 비교하라.",
  hint=r"$dz=f_x\,dx+f_y\,dy$ ($dx=0.1,\ dy=-0.1$), $\Delta z=f(2.1,0.9)-f(2,1)$",
  ans=r"$\Delta z=0.14$,  $dz=0.1$",
  sol=[r"$f_x=2x-y,\ f_y=-x+4y \Rightarrow f_x(2,1)=3,\ f_y(2,1)=2$",
       r"$dz=3(0.1)+2(-0.1)=0.1$",
       r"$f(2,1)=4-2+2=4$,  $f(2.1,0.9)=4.41-1.89+1.62=4.14$ $\Rightarrow \Delta z=0.14$",
       r"$dz$는 $\Delta z$의 1차 근사 (차이는 2차 항)"],
  check=_c)


def _c():
    zz = (x**2 + x*y + y**2).subs({x: s + t, y: s*t})
    assert EQ(diff(zz, s).subs({s: 1, t: 2}), 22) and EQ(diff(zz, t).subs({s: 1, t: 2}), 15)
P(id="2-16", ch=14, sec="14.5", type="14-chain", src="강의 14.5 ex3 · 과제 14.5 #14 유형",
  q=r"$z=x^2+xy+y^2$, $x=s+t$, $y=st$일 때 $(s,t)=(1,2)$에서 $\dfrac{\partial z}{\partial s}$, $\dfrac{\partial z}{\partial t}$를 구하라.",
  hint=r"$\dfrac{\partial z}{\partial s}=z_x\dfrac{\partial x}{\partial s}+z_y\dfrac{\partial y}{\partial s}$ (나무 그림)",
  ans=r"$\dfrac{\partial z}{\partial s}=22$,  $\dfrac{\partial z}{\partial t}=15$",
  sol=[r"$z_x=2x+y,\ z_y=x+2y$;  $x_s=1,\ x_t=1,\ y_s=t,\ y_t=s$",
       r"$(s,t)=(1,2)$이면 $x=3,\ y=2$ → $z_x=8,\ z_y=7$",
       r"$\dfrac{\partial z}{\partial s}=8\cdot1+7\cdot2=22$,  $\dfrac{\partial z}{\partial t}=8\cdot1+7\cdot1=15$"],
  check=_c)


def _c():
    f = x*y + y*z**2
    g = grad(f, [x, y, z]).subs({x: 2, y: 1, z: 1})
    assert EQ(g, [1, 3, 2]) and EQ(g.norm(), sqrt(14))
P(id="2-17", ch=14, sec="14.6", type="14-maxrate", src="강의 14.6 ex6 · 과제 14.6 #27 유형",
  q=r"$f(x,y,z)=xy+yz^2$의 점 $(2,1,1)$에서의 최대 변화율과 그 방향을 구하라.",
  hint=r"최대 변화율은 $|\nabla f|$, 방향은 $\nabla f$",
  ans=r"최대 변화율 $\sqrt{14}$, 방향 $\langle1,3,2\rangle$ (단위벡터 $\tfrac{1}{\sqrt{14}}\langle1,3,2\rangle$)",
  sol=[r"$\nabla f=\langle y,\ x+z^2,\ 2yz\rangle$",
       r"$\nabla f(2,1,1)=\langle1,3,2\rangle$",
       r"최대 변화율 $|\nabla f|=\sqrt{1+9+4}=\sqrt{14}$, 방향은 $\nabla f$와 같은 방향"],
  check=_c)


def _c():
    f = x**3 - 3*x + y**2 - 4*y
    cps = solve([diff(f, x), diff(f, y)], [x, y], dict=True)
    D = diff(f, x, 2)*diff(f, y, 2) - diff(f, x, y)**2
    vals = {(c[x], c[y]): (D.subs(c), diff(f, x, 2).subs(c), f.subs(c)) for c in cps}
    assert vals[(1, 2)] == (12, 6, -6) and vals[(-1, 2)][0] < 0
P(id="2-18", ch=14, sec="14.7", type="14-crit", src="강의 14.7 ex3 · 과제 14.7 #19 유형",
  q=r"$f(x,y)=x^3-3x+y^2-4y$의 극댓값, 극솟값, 안장점을 구하라.",
  hint=r"$f_x=f_y=0$에서 임계점, $D=f_{xx}f_{yy}-f_{xy}^2$",
  ans=r"$(1,2)$에서 극솟값 $-6$, $(-1,2)$는 안장점 (극댓값 없음)",
  sol=[r"$f_x=3x^2-3=0 \Rightarrow x=\pm1$,  $f_y=2y-4=0 \Rightarrow y=2$",
       r"$f_{xx}=6x,\ f_{yy}=2,\ f_{xy}=0 \Rightarrow D=12x$",
       r"$(1,2)$: $D=12>0,\ f_{xx}=6>0$ → 극소, $f(1,2)=1-3+4-8=-6$",
       r"$(-1,2)$: $D=-12<0$ → 안장점"],
  check=_c)


def _c():
    lam = symbols('lam')
    sols = solve([y - lam*2*x, x - lam*8*y, x**2 + 4*y**2 - 8], [x, y, lam], dict=True)
    vals = sorted(set(simplify((x*y).subs(c)) for c in sols))
    assert vals == [-2, 2]
P(id="2-19", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 ex1 · 과제 14.8 #12 유형",
  q=r"제약조건 $x^2+4y^2=8$ 아래에서 $f(x,y)=xy$의 최댓값과 최솟값을 라그랑주 승수법으로 구하라.",
  hint=r"$\nabla f=\lambda\nabla g$: $\ y=2\lambda x,\ \ x=8\lambda y$",
  ans=r"최댓값 $2$ (점 $(2,1),(-2,-1)$), 최솟값 $-2$ (점 $(2,-1),(-2,1)$)",
  sol=[r"$y=2\lambda x,\ \ x=8\lambda y \Rightarrow y=16\lambda^2y$",
       r"$y=0$이면 $x=0$인데 제약조건을 만족하지 않으므로 $\lambda^2=\tfrac1{16}$, 즉 $\lambda=\pm\tfrac14$",
       r"$\lambda=\tfrac14$: $x=2y$ → $8y^2=8$ → $(2,1),(-2,-1)$, $f=2$",
       r"$\lambda=-\tfrac14$: $x=-2y$ → $(-2,1),(2,-1)$, $f=-2$",
       r"최댓값 $2$, 최솟값 $-2$"],
  check=_c)


# ───────── Ch.15 ─────────
def _c():
    assert EQ(integrate(y, (x, y**2, y + 2), (y, -1, 2)), R(9, 4))
P(id="2-20", ch=15, sec="15.2", type="15-general", src="강의 15.2 ex3 유형 (Type II)",
  q=r"$D$가 곡선 $x=y^2$과 직선 $x=y+2$로 둘러싸인 영역일 때 $\displaystyle\iint_D y\,dA$를 구하라.",
  hint=r"교점은 $y^2=y+2$에서 $y=-1,\,2$. Type II로 ($x$를 먼저) 적분하면 한 번에 끝나요.",
  ans=r"$\dfrac94$",
  sol=[r"교점: $y^2=y+2 \Rightarrow y=-1,\ 2$",
       r"$\displaystyle\int_{-1}^{2}\!\!\int_{y^2}^{y+2}y\,dx\,dy=\int_{-1}^{2}y(y+2-y^2)\,dy=\int_{-1}^{2}(y^2+2y-y^3)\,dy$",
       r"$=\Big[\tfrac{y^3}{3}+y^2-\tfrac{y^4}{4}\Big]_{-1}^{2}=\tfrac83-\left(-\tfrac13+1-\tfrac14\right)=\dfrac94$"],
  check=_c)


def _c():
    assert EQ(integrate(exp(x**3), (y, 0, x**2), (x, 0, 1)), (E - 1) / 3)
P(id="2-21", ch=15, sec="15.2", type="15-order", src="강의 15.2 ex5 · 과제 15.2 #61 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^1\!\!\int_{\sqrt y}^{1} e^{x^3}\,dx\,dy$를 계산하라.",
  hint=r"영역: $0\le y\le1,\ \sqrt y\le x\le1$ ⇔ $0\le x\le1,\ 0\le y\le x^2$",
  ans=r"$\dfrac{e-1}{3}$",
  sol=[r"영역을 그리면 $0\le x\le1,\ 0\le y\le x^2$",
       r"$\displaystyle\int_0^1\!\!\int_0^{x^2}e^{x^3}\,dy\,dx=\int_0^1x^2e^{x^3}\,dx$",
       r"$u=x^3$로 치환: $\dfrac13\Big[e^{x^3}\Big]_0^1=\dfrac{e-1}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(r*cos(th) * r, (r, 1, 3), (th, 0, pi/2)), R(26, 3))
P(id="2-22", ch=15, sec="15.3", type="15-polar", src="강의 15.3 ex1 · 과제 15.3 #13 유형",
  q=r"$D$가 제1사분면에서 원 $x^2+y^2=1$과 $x^2+y^2=9$ 사이의 영역일 때 $\displaystyle\iint_D x\,dA$를 구하라.",
  hint=r"$D: 1\le r\le3,\ 0\le\theta\le\tfrac\pi2$, $x=r\cos\theta$, $dA=r\,dr\,d\theta$",
  ans=r"$\dfrac{26}{3}$",
  sol=[r"$\displaystyle\int_0^{\pi/2}\!\!\int_1^3 r\cos\theta\cdot r\,dr\,d\theta=\Big[\sin\theta\Big]_0^{\pi/2}\Big[\tfrac{r^3}{3}\Big]_1^3$",
       r"$=1\cdot\dfrac{27-1}{3}=\dfrac{26}{3}$"],
  check=_c)


def _c():
    assert EQ(integrate(z, (z, 0, 1 - x - y), (y, 0, 1 - x), (x, 0, 1)), R(1, 24))
P(id="2-23", ch=15, sec="15.6", type="15-triple", src="강의 15.6 ex2 · ex5 유형",
  q=r"$E$가 평면 $x+y+z=1$과 세 좌표평면으로 둘러싸인 사면체일 때 $\displaystyle\iiint_E z\,dV$를 구하라.",
  hint=r"$0\le x\le1,\ 0\le y\le1-x,\ 0\le z\le1-x-y$",
  ans=r"$\dfrac{1}{24}$",
  sol=[r"$\displaystyle\int_0^1\!\!\int_0^{1-x}\!\!\int_0^{1-x-y}z\,dz\,dy\,dx=\int_0^1\!\!\int_0^{1-x}\frac{(1-x-y)^2}{2}\,dy\,dx$",
       r"$=\displaystyle\int_0^1\frac{(1-x)^3}{6}\,dx=\frac16\cdot\frac14=\frac1{24}$"],
  check=_c)


def _c():
    assert EQ(integrate(r * r, (z, 0, 3), (r, 0, 2), (th, 0, 2*pi)), 16*pi)
P(id="2-24", ch=15, sec="15.7", type="15-cyl", src="과제 15.7 #19 유형",
  q=r"$E$가 원기둥 $x^2+y^2=4$ 내부에서 평면 $z=0$과 $z=3$ 사이의 영역일 때 $\displaystyle\iiint_E\sqrt{x^2+y^2}\,dV$를 구하라.",
  hint=r"원주좌표: $\sqrt{x^2+y^2}=r$, $dV=r\,dz\,dr\,d\theta$",
  ans=r"$16\pi$",
  sol=[r"$E: 0\le r\le2,\ 0\le\theta\le2\pi,\ 0\le z\le3$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^3 r\cdot r\,dz\,dr\,d\theta=2\pi\cdot3\cdot\Big[\tfrac{r^3}{3}\Big]_0^2=2\pi\cdot3\cdot\tfrac83=16\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(rho*cos(ph) * rho**2*sin(ph), (rho, 0, 2), (ph, 0, pi/2), (th, 0, 2*pi)), 4*pi)
P(id="2-25", ch=15, sec="15.8", type="15-sph", src="강의 15.8 ex3 · 과제 15.8 #23 유형",
  q=r"$E$가 구 $x^2+y^2+z^2\le4$의 위쪽 절반 ($z\ge0$)일 때 $\displaystyle\iiint_E z\,dV$를 구하라.",
  hint=r"$z=\rho\cos\phi$, 위쪽 반구는 $0\le\phi\le\tfrac\pi2$",
  ans=r"$4\pi$",
  sol=[r"$E: 0\le\rho\le2,\ 0\le\theta\le2\pi,\ 0\le\phi\le\tfrac\pi2$",
       r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^2\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot\Big[\tfrac{\sin^2\phi}{2}\Big]_0^{\pi/2}\cdot\Big[\tfrac{\rho^4}{4}\Big]_0^2$",
       r"$=2\pi\cdot\tfrac12\cdot4=4\pi$"],
  check=_c)


# ───────── Ch.16 ─────────
def _c():
    xx, yy = 2*cos(t), 2*sin(t)
    assert EQ(integrate(xx*yy**2 * 2, (t, 0, pi/2)), R(16, 3))
P(id="2-26", ch=16, sec="16.2", type="16-scalar", src="강의 16.2 ex1 유형",
  q=r"$C$가 원 $x^2+y^2=4$의 제1사분면 부분일 때 $\displaystyle\int_C xy^2\,ds$를 구하라.",
  hint=r"$\mathbf r(t)=\langle2\cos t,2\sin t\rangle,\ 0\le t\le\tfrac\pi2$, $ds=2\,dt$",
  ans=r"$\dfrac{16}{3}$",
  sol=[r"$|\mathbf r'(t)|=|\langle-2\sin t,2\cos t\rangle|=2$",
       r"$\displaystyle\int_0^{\pi/2}(2\cos t)(4\sin^2t)\cdot2\,dt=16\int_0^{\pi/2}\sin^2t\cos t\,dt$",
       r"$=16\Big[\tfrac{\sin^3t}{3}\Big]_0^{\pi/2}=\dfrac{16}{3}$"],
  check=_c)


def _c():
    I1 = integrate((t + 4*t)*1 + t**2*2, (t, 0, 1))
    I2 = integrate((1 + 2*t + 4)*2, (t, 0, 1))
    assert EQ(I1, R(19, 6)) and EQ(I2, 12) and EQ(I1 + I2, R(91, 6))
P(id="2-27", ch=16, sec="16.2", type="16-vector", src="과제 16.2 #7 유형",
  q=r"$C$가 $(0,0)\to(1,2)\to(3,2)$로 가는 두 선분일 때 $\displaystyle\int_C (x+2y)\,dx+x^2\,dy$를 구하라.",
  hint=r"선분마다 따로 매개화해서 더해요. $C_1:\ \langle t,2t\rangle$, $C_2:\ \langle1+2t,\ 2\rangle$ ($0\le t\le1$)",
  ans=r"$\dfrac{91}{6}$",
  sol=[r"$C_1$: $x=t,\ y=2t$, $dx=dt,\ dy=2dt$ → $\displaystyle\int_0^1\big[(t+4t)+t^2\cdot2\big]dt=\frac52+\frac23=\frac{19}{6}$",
       r"$C_2$: $x=1+2t,\ y=2$, $dx=2dt,\ dy=0$ → $\displaystyle\int_0^1(1+2t+4)\cdot2\,dt=\int_0^1(10+4t)\,dt=12$",
       r"합: $\dfrac{19}{6}+12=\dfrac{91}{6}$"],
  check=_c)


def _c():
    Fv = Matrix([y*z, x*z + 2*y, x*y + 3*z**2])
    f = x*y*z + y**2 + z**3
    assert EQ(grad(f, [x, y, z]), Fv)
    assert EQ(f.subs({x: 1, y: 2, z: 1}) - f.subs({x: 0, y: 0, z: 0}), 7)
P(id="2-28", ch=16, sec="16.3", type="16-conserv", src="강의 16.3 ex5 · 복습 16.1–4 기초3 유형",
  q=r"$\mathbf F=\langle yz,\ xz+2y,\ xy+3z^2\rangle$이 보존장임을 보이고 퍼텐셜 함수 $f$를 구한 뒤, $(0,0,0)$에서 $(1,2,1)$까지의 임의의 경로 $C$를 따라 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$P_y=Q_x,\ Q_z=R_y,\ R_x=P_z$ 확인 → $f_x=P$를 적분해 나머지 성분과 비교",
  ans=r"$f=xyz+y^2+z^3+K$,  $\displaystyle\int_C\mathbf F\cdot d\mathbf r=7$",
  sol=[r"$P_y=z=Q_x,\ \ Q_z=x=R_y,\ \ R_x=y=P_z$ → 보존장",
       r"$f_x=yz \Rightarrow f=xyz+g(y,z)$;  $f_y=xz+g_y=xz+2y \Rightarrow g=y^2+h(z)$",
       r"$f_z=xy+h'(z)=xy+3z^2 \Rightarrow h=z^3+K$ → $f=xyz+y^2+z^3+K$",
       r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r=f(1,2,1)-f(0,0,0)=(2+4+1)-0=7$"],
  check=_c)


def _c():
    Pf, Qf = 2*x*y + exp(x), x**2 + 2*y
    assert EQ(diff(Pf, y), diff(Qf, x))
    f = x**2*y + exp(x) + y**2
    assert EQ(diff(f, x), Pf) and EQ(diff(f, y), Qf)
    st = (sin(0), 1 + 0); en = (sin(pi/2), 2)
    assert EQ(f.subs({x: en[0], y: en[1]}) - f.subs({x: st[0], y: st[1]}), 4 + E)
P(id="2-29", ch=16, sec="16.3", type="16-ftli", src="강의 16.3 ex4 · 과제 16.3 #25 유형",
  q=r"$\mathbf F=\langle 2xy+e^x,\ x^2+2y\rangle$이고 $C:\ \mathbf r(t)=\left\langle \sin\tfrac{\pi t}{2},\ 1+t^2\right\rangle,\ 0\le t\le1$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"직접 매개화하면 복잡해요. 보존장인지 먼저 확인하고 퍼텐셜의 끝점 값 차이를 구해요.",
  ans=r"$4+e$",
  sol=[r"$P_y=2x=Q_x$ → 보존장, $f=x^2y+e^x+y^2$",
       r"시작점 $\mathbf r(0)=(0,1)$, 끝점 $\mathbf r(1)=(1,2)$",
       r"$\displaystyle\int_C\mathbf F\cdot d\mathbf r=f(1,2)-f(0,1)=(2+e+4)-(0+1+1)=4+e$"],
  check=_c)


def _c():
    assert EQ(integrate(3*y - 2*y, (x, 0, 2), (y, 0, 3)), 9)
P(id="2-30", ch=16, sec="16.4", type="16-green", src="과제 16.4 #3 · #8 유형",
  q=r"$C$가 직사각형 $[0,2]\times[0,3]$의 경계(반시계 방향)일 때 $\displaystyle\oint_C y^2\,dx+3xy\,dy$를 구하라.",
  hint=r"$Q_x-P_y$를 직사각형에서 이중적분해요.",
  ans=r"$9$",
  sol=[r"$P=y^2,\ Q=3xy \Rightarrow Q_x-P_y=3y-2y=y$",
       r"$\displaystyle\iint_D y\,dA=\int_0^2\!\!\int_0^3y\,dy\,dx=2\cdot\frac92=9$"],
  check=_c)

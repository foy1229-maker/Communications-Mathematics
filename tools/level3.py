"""3단계 · 응용 (30문제) — 복습문제(연습) 유형"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    S = Matrix([2, 1, -1]); Pp = Matrix([1, 0, 3]); vv = Matrix([2, -1, 2])
    c = (S - Pp).cross(vv)
    assert EQ(c, [-2, -10, -3]) and EQ(c.norm() / vv.norm(), sqrt(113) / 3)
P(id="3-01", ch=12, sec="12.5", type="12-dist", src="강의 12.5 (점과 직선 사이 거리) · 과제 12.4 #45 유형",
  q=r"점 $S(2,1,-1)$에서 직선 $L:\ x=1+2t,\ y=-t,\ z=3+2t$까지의 거리를 구하라.",
  hint=r"직선 위의 점 $P$와 방향벡터 $\mathbf v$에 대해 $d=\dfrac{|\overrightarrow{PS}\times\mathbf v|}{|\mathbf v|}$",
  ans=r"$\dfrac{\sqrt{113}}{3}$",
  sol=[r"$P=(1,0,3)$ ($t=0$),  $\mathbf v=\langle2,-1,2\rangle$,  $\overrightarrow{PS}=\langle1,1,-4\rangle$",
       r"$\overrightarrow{PS}\times\mathbf v=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\1&1&-4\\2&-1&2\end{vmatrix}=(2-4)\mathbf i-(2+8)\mathbf j+(-1-2)\mathbf k=\langle-2,-10,-3\rangle$",
       r"$d=\dfrac{\sqrt{4+100+9}}{\sqrt{4+1+4}}=\dfrac{\sqrt{113}}{3}$"],
  check=_c)


def _c():
    Pp, Q, Rr = Matrix([1, 0, 1]), Matrix([-2, 1, 3]), Matrix([4, 2, 5])
    c = (Q - Pp).cross(Rr - Pp)
    assert EQ(c, [0, 18, -9]) and EQ(c.norm() / 2, 9*sqrt(5) / 2)
    for pt in (Pp, Q, Rr):
        assert 2*pt[1] - pt[2] + 1 == 0
P(id="3-02", ch=12, sec="12.4", type="12-cross", src="강의 12.4 ex3 · 복습 12장 기초3 유형",
  q=r"세 점 $P(1,0,1)$, $Q(-2,1,3)$, $R(4,2,5)$에 대해 (a) 삼각형 $PQR$의 넓이 (b) 세 점을 지나는 평면의 방정식을 구하라.",
  hint=r"$\overrightarrow{PQ}\times\overrightarrow{PR}$ 하나로 넓이($\tfrac12|\cdot|$)와 법선벡터를 모두 얻어요.",
  ans=r"(a) $\dfrac{9\sqrt5}{2}$  (b) $2y-z+1=0$",
  sol=[r"$\overrightarrow{PQ}=\langle-3,1,2\rangle,\ \overrightarrow{PR}=\langle3,2,4\rangle$",
       r"$\overrightarrow{PQ}\times\overrightarrow{PR}=\langle 4-4,\ 6+12,\ -6-3\rangle=\langle0,18,-9\rangle$",
       r"(a) 넓이 $=\tfrac12\sqrt{0+324+81}=\tfrac12\sqrt{405}=\dfrac{9\sqrt5}{2}$",
       r"(b) $\mathbf n\parallel\langle0,2,-1\rangle$: $2(y-0)-(z-1)=0 \Rightarrow 2y-z+1=0$ (검산: $Q$: $2-3+1=0$, $R$: $4-5+1=0$)"],
  check=_c)


def _c():
    eq = expand((x - 1)**2 + (y + 2)**2 + (z - 3)**2 - (x - 5)**2 - (y - 4)**2 - (z + 1)**2)
    assert EQ(eq, 4*(2*x + 3*y - 2*z - 7))
P(id="3-03", ch=12, sec="12.1", type="12-sphere", src="과제 12.1 #49 유형",
  q=r"두 점 $A(1,-2,3)$, $B(5,4,-1)$에서 같은 거리에 있는 점 $(x,y,z)$ 전체의 집합의 방정식을 구하고, 어떤 도형인지 설명하라.",
  hint=r"$|PA|^2=|PB|^2$를 전개하면 이차항이 모두 지워져요.",
  ans=r"$2x+3y-2z=7$ — 선분 $AB$의 수직이등분 평면",
  sol=[r"$(x-1)^2+(y+2)^2+(z-3)^2=(x-5)^2+(y-4)^2+(z+1)^2$",
       r"전개 후 정리: $8x+12y-8z-28=0 \Rightarrow 2x+3y-2z=7$",
       r"법선 $\langle2,3,-2\rangle\parallel\overrightarrow{AB}=\langle4,6,-4\rangle$이고 중점 $(3,1,1)$을 지나므로 $AB$의 수직이등분 평면"],
  check=_c)


def _c():
    a = Matrix([3, 0, 4]); b = Matrix([2, 1, -2])
    p = a.dot(b) / a.dot(a) * a; o = b - p
    assert EQ(p, [R(-6, 25), 0, R(-8, 25)]) and EQ(o, [R(56, 25), 1, R(-42, 25)]) and o.dot(a) == 0
P(id="3-04", ch=12, sec="12.3", type="12-proj", src="과제 12.3 #45 유형",
  q=r"$\mathbf b=\langle 2,1,-2\rangle$를 $\mathbf a=\langle3,0,4\rangle$에 평행한 벡터와 $\mathbf a$에 수직인 벡터의 합으로 나타내라.",
  hint=r"평행 성분 $=\operatorname{proj}_{\mathbf a}\mathbf b$, 수직 성분 $=\mathbf b-\operatorname{proj}_{\mathbf a}\mathbf b$",
  ans=r"$\mathbf b=\left\langle-\tfrac{6}{25},0,-\tfrac{8}{25}\right\rangle+\left\langle\tfrac{56}{25},1,-\tfrac{42}{25}\right\rangle$",
  sol=[r"$\mathbf a\cdot\mathbf b=6+0-8=-2$,  $|\mathbf a|^2=25$",
       r"$\operatorname{proj}_{\mathbf a}\mathbf b=-\dfrac{2}{25}\langle3,0,4\rangle=\left\langle-\tfrac{6}{25},0,-\tfrac{8}{25}\right\rangle$",
       r"수직 성분: $\mathbf b-\operatorname{proj}_{\mathbf a}\mathbf b=\left\langle\tfrac{56}{25},1,-\tfrac{42}{25}\right\rangle$",
       r"검산: $\left\langle\tfrac{56}{25},1,-\tfrac{42}{25}\right\rangle\cdot\langle3,0,4\rangle=\tfrac{168-168}{25}=0$ ✓"],
  check=_c)


def _c():
    tt = solve((2 + t) + (1 - 2*t) + 3*t - 9, t)[0]
    pt = Matrix([2 + tt, 1 - 2*tt, 3*tt])
    assert EQ(pt, [5, -5, 9]) and pt[0] - 2*pt[1] + 3*pt[2] == 42
P(id="3-05", ch=12, sec="12.5", type="12-plane", src="강의 12.5 (직선·평면 종합) 유형",
  q=r"직선 $x=2+t,\ y=1-2t,\ z=3t$가 평면 $x+y+z=9$와 만나는 점을 구하고, 그 점을 지나며 이 직선에 수직인 평면의 방정식을 구하라.",
  hint=r"직선의 매개식을 평면에 대입 → $t$. 직선에 수직인 평면의 법선은 직선의 방향벡터예요.",
  ans=r"교점 $(5,-5,9)$,  평면 $x-2y+3z=42$",
  sol=[r"$(2+t)+(1-2t)+3t=9 \Rightarrow 3+2t=9 \Rightarrow t=3$ → 교점 $(5,-5,9)$",
       r"법선 $\mathbf n=\langle1,-2,3\rangle$ (직선의 방향벡터)",
       r"$(x-5)-2(y+5)+3(z-9)=0 \Rightarrow x-2y+3z=42$"],
  check=_c)


def _c():
    assert Matrix([2, 1, -1]).dot(Matrix([1, -1, 1])) == 0
    assert EQ(abs(1 - (-1) + 3 - 10) / sqrt(3), 5*sqrt(3) / 3)
P(id="3-06", ch=12, sec="12.5", type="12-dist", src="복습 12장 심화1(b) · 과제 12.5 #75 유형",
  q=r"직선 $L:\ x=1+2t,\ y=-1+t,\ z=3-t$가 평면 $x-y+z=10$과 평행함을 보이고, 직선과 평면 사이의 거리를 구하라.",
  hint=r"$\mathbf v\cdot\mathbf n=0$이면 평행. 거리는 직선 위 아무 점에서 평면까지의 거리예요.",
  ans=r"$\mathbf v\cdot\mathbf n=0$ 이므로 평행,  거리 $\dfrac{5\sqrt3}{3}$",
  sol=[r"$\mathbf v=\langle2,1,-1\rangle,\ \mathbf n=\langle1,-1,1\rangle$,  $\mathbf v\cdot\mathbf n=2-1-1=0$ → 직선은 평면과 평행 (점 $(1,-1,3)$은 평면 위에 있지 않음: $1+1+3=5\ne10$)",
       r"$D=\dfrac{|1-(-1)+3-10|}{\sqrt{1+1+1}}=\dfrac{5}{\sqrt3}=\dfrac{5\sqrt3}{3}$"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    rr = Matrix([3*cos(t), 3*sin(t), 5 - 3*cos(t)])
    assert EQ(rr[0]**2 + rr[1]**2, 9) and EQ(rr[0] + rr[2], 5)
    assert EQ(rr.subs(t, pi), [-3, 0, 8])
P(id="3-07", ch=13, sec="13.1", type="13-curve", src="복습 13장 기초1 유형",
  q=r"원기둥 $x^2+y^2=9$와 평면 $x+z=5$의 교선을 나타내는 벡터함수를 구하고, 교선 위에서 $z$의 최댓값을 구하라.",
  hint=r"원기둥은 $x=3\cos t,\ y=3\sin t$로, $z$는 평면 식에서 구해요.",
  ans=r"$\mathbf r(t)=\langle3\cos t,\ 3\sin t,\ 5-3\cos t\rangle$ $(0\le t\le2\pi)$,  $z$의 최댓값 $8$ (점 $(-3,0,8)$)",
  sol=[r"$x=3\cos t,\ y=3\sin t$ ($x^2+y^2=9$ 만족)",
       r"$z=5-x=5-3\cos t$",
       r"$z=5-3\cos t$는 $\cos t=-1$ ($t=\pi$)일 때 최대 $8$, 그 점은 $(-3,0,8)$"],
  check=_c)


def _c():
    rr = Matrix([4*sin(t), 3*t, 4*cos(t)])
    assert EQ(rr.diff(t).norm(), 5) and EQ(rr.subs(t, 0), [0, 0, 4])
    assert EQ(rr.subs(t, 2), [4*sin(2), 6, 4*cos(2)])
P(id="3-08", ch=13, sec="13.3", type="13-arcfn", src="과제 13.3 #17 유형",
  q=r"점 $(0,0,4)$에서 출발하여 곡선 $x=4\sin t,\ y=3t,\ z=4\cos t$를 따라 $t$가 증가하는 방향으로 길이 $10$만큼 이동하면 어느 점에 도착하는가?",
  hint=r"출발점의 $t$와 속력 $|\mathbf r'(t)|$를 구하면 $s=5t$ 꼴이 돼요.",
  ans=r"$(4\sin2,\ 6,\ 4\cos2)$",
  sol=[r"$(0,0,4)$는 $t=0$에 대응",
       r"$|\mathbf r'(t)|=\sqrt{16\cos^2t+9+16\sin^2t}=5 \Rightarrow s(t)=5t$",
       r"$s=10 \Rightarrow t=2$ → $(4\sin2,\ 6,\ 4\cos2)$"],
  check=_c)


def _c():
    rr = Matrix([t**2, exp(t), t*exp(t)])
    vv = rr.diff(t).subs(t, 0); aa = rr.diff(t, 2).subs(t, 0)
    assert EQ(vv, [0, 1, 1]) and EQ(vv.norm(), sqrt(2)) and EQ(aa, [2, 1, 2])
P(id="3-09", ch=13, sec="13.2", type="13-motion", src="강의 13.2 (속도·속력·가속도) 유형",
  q=r"입자의 위치가 $\mathbf r(t)=\langle t^2,\ e^t,\ te^t\rangle$일 때 $t=0$에서의 속도, 속력, 가속도를 구하라.",
  hint=r"$\mathbf v=\mathbf r'$, 속력 $=|\mathbf v|$, $\mathbf a=\mathbf r''$",
  ans=r"$\mathbf v(0)=\langle0,1,1\rangle$,  속력 $\sqrt2$,  $\mathbf a(0)=\langle2,1,2\rangle$",
  sol=[r"$\mathbf v(t)=\langle2t,\ e^t,\ (1+t)e^t\rangle \Rightarrow \mathbf v(0)=\langle0,1,1\rangle$, 속력 $|\mathbf v(0)|=\sqrt2$",
       r"$\mathbf a(t)=\langle2,\ e^t,\ (2+t)e^t\rangle \Rightarrow \mathbf a(0)=\langle2,1,2\rangle$"],
  check=_c)


def _c():
    rr = Matrix([exp(t)*cos(t), exp(t)*sin(t), exp(t)])
    sp2 = simplify(rr.diff(t).dot(rr.diff(t)))
    assert EQ(sp2, 3*exp(2*t))
    assert EQ(integrate(sqrt(3)*exp(t), (t, 0, log(2))), sqrt(3))
P(id="3-10", ch=13, sec="13.3", type="13-arc", src="과제 13.3 #5 유형",
  q=r"$\mathbf r(t)=\langle e^t\cos t,\ e^t\sin t,\ e^t\rangle$, $0\le t\le\ln2$의 길이를 구하라.",
  hint=r"$\mathbf r'(t)=e^t\langle\cos t-\sin t,\ \sin t+\cos t,\ 1\rangle$로 묶어 보세요.",
  ans=r"$\sqrt3$",
  sol=[r"$\mathbf r'(t)=e^t\langle\cos t-\sin t,\ \sin t+\cos t,\ 1\rangle$",
       r"$(\cos t-\sin t)^2+(\sin t+\cos t)^2+1=2+1=3 \Rightarrow |\mathbf r'(t)|=\sqrt3\,e^t$",
       r"$L=\displaystyle\int_0^{\ln2}\sqrt3\,e^t\,dt=\sqrt3\,(2-1)=\sqrt3$"],
  check=_c)


# ───────── Ch.14 ─────────
def _c():
    f = x**2*y / (x**4 + 3*y**2)
    m = symbols('m', real=True, nonzero=True)
    assert EQ(limit(f.subs(y, m*x), x, 0), 0)
    assert EQ(limit(f.subs(y, x**2), x, 0), R(1, 4))
P(id="3-11", ch=14, sec="14.2", type="14-dne", src="복습 14.1–3 기초1 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^4+3y^2}$가 존재하지 않음을 보여라.",
  hint=r"모든 직선 $y=mx$에서는 같은 값이 나와요. 포물선 $y=x^2$을 시도해 보세요.",
  ans=r"직선 $y=mx$를 따라 $0$, 포물선 $y=x^2$을 따라 $\tfrac14$ → 존재하지 않는다.",
  sol=[r"$y=mx$: $\dfrac{mx^3}{x^4+3m^2x^2}=\dfrac{mx}{x^2+3m^2}\to0$ (축 방향도 0)",
       r"$y=x^2$: $\dfrac{x^4}{x^4+3x^4}=\dfrac14\to\dfrac14$",
       r"경로에 따라 극한이 다르므로 존재하지 않는다. (직선 경로만 확인하면 안 되는 대표 예)"],
  check=_c)


def _c():
    f = (2*x**3 + 3*y**3) / (x**2 + y**2)
    pol = simplify(f.subs({x: r*cos(th), y: r*sin(th)}))
    assert EQ(pol, r*(2*cos(th)**3 + 3*sin(th)**3))
    assert limit(pol, r, 0) == 0
P(id="3-12", ch=14, sec="14.2", type="14-limit", src="강의 14.2 ex6 · 과제 14.2 #51 · 복습 14.1–3 심화1 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{2x^3+3y^3}{x^2+y^2}$를 구하라.",
  hint=r"극좌표 $x=r\cos\theta,\ y=r\sin\theta$로 바꾸면 $r\to0^+$만 보면 돼요 (또는 조임정리).",
  ans=r"$0$",
  sol=[r"$\dfrac{2r^3\cos^3\theta+3r^3\sin^3\theta}{r^2}=r\,(2\cos^3\theta+3\sin^3\theta)$",
       r"$\big|r(2\cos^3\theta+3\sin^3\theta)\big|\le 5r\to0$ ($\theta$와 무관)",
       r"조임정리에 의해 극한은 $0$"],
  check=_c)


def _c():
    uu = log(x**2 + y**2)
    assert EQ(diff(uu, x, 2) + diff(uu, y, 2), 0)
    assert EQ(diff(uu, x, 2), 2*(y**2 - x**2) / (x**2 + y**2)**2)
P(id="3-13", ch=14, sec="14.3", type="14-higher", src="강의 14.3 ex9 (라플라스 방정식) 유형",
  q=r"$u(x,y)=\ln(x^2+y^2)$가 라플라스 방정식 $u_{xx}+u_{yy}=0$을 만족함을 보여라.",
  hint=r"$u_x=\dfrac{2x}{x^2+y^2}$를 몫의 미분법으로 한 번 더 미분해요.",
  ans=r"$u_{xx}=\dfrac{2(y^2-x^2)}{(x^2+y^2)^2},\ u_{yy}=\dfrac{2(x^2-y^2)}{(x^2+y^2)^2}$ → 합이 $0$",
  sol=[r"$u_x=\dfrac{2x}{x^2+y^2}$,  $u_{xx}=\dfrac{2(x^2+y^2)-2x\cdot2x}{(x^2+y^2)^2}=\dfrac{2(y^2-x^2)}{(x^2+y^2)^2}$",
       r"대칭적으로 $u_{yy}=\dfrac{2(x^2-y^2)}{(x^2+y^2)^2}$",
       r"$u_{xx}+u_{yy}=0$ → 조화함수"],
  check=_c)


def _c():
    rr_, hh_ = symbols('rr hh', positive=True)
    V = pi*rr_**2*hh_/3
    dV = (diff(V, rr_)*R(1, 10) + diff(V, hh_)*R(1, 10)).subs({rr_: 6, hh_: 12})
    assert EQ(dV, 6*pi)
P(id="3-14", ch=14, sec="14.4", type="14-diff", src="강의 14.4 ex5 (원뿔 오차) 유형",
  q=r"원뿔의 밑면 반지름을 $6\,\mathrm{cm}$, 높이를 $12\,\mathrm{cm}$로 측정했고 각 측정의 오차가 최대 $0.1\,\mathrm{cm}$일 때, 미분을 이용해 부피 계산의 최대 오차를 추정하라.",
  hint=r"$V=\tfrac13\pi r^2h$,  $dV=V_r\,dr+V_h\,dh$에 $|dr|,|dh|\le0.1$을 넣어요.",
  ans=r"약 $6\pi\ \mathrm{cm}^3$",
  sol=[r"$dV=\dfrac{2\pi rh}{3}\,dr+\dfrac{\pi r^2}{3}\,dh$",
       r"$r=6,\ h=12$: $dV=48\pi\,dr+12\pi\,dh$",
       r"$dr=dh=0.1$일 때 최대: $4.8\pi+1.2\pi=6\pi\ \mathrm{cm}^3$"],
  check=_c)


def _c():
    xt, yt = t**2 + 1, sqrt(t + 1)
    assert EQ([xt.subs(t, 3), yt.subs(t, 3)], [10, 2])
    assert EQ(2*diff(xt, t).subs(t, 3) + (-3)*diff(yt, t).subs(t, 3), R(45, 4))
P(id="3-15", ch=14, sec="14.5", type="14-chain", src="과제 14.5 #39 유형",
  q=r"점 $(x,y)$의 온도 $T(x,y)$ (°C)에 대해 $T_x(10,2)=2$, $T_y(10,2)=-3$이다. 벌레가 $x=t^2+1,\ y=\sqrt{t+1}$ (cm, $t$는 초)을 따라 움직일 때, $t=3$초에서 벌레가 느끼는 온도의 변화율을 구하라.",
  hint=r"$\dfrac{dT}{dt}=T_x\dfrac{dx}{dt}+T_y\dfrac{dy}{dt}$, $t=3$일 때 위치부터 확인해요.",
  ans=r"$\dfrac{45}{4}\ ^\circ\mathrm C/\mathrm s$",
  sol=[r"$t=3$: $x=10,\ y=2$",
       r"$\dfrac{dx}{dt}=2t=6,\ \ \dfrac{dy}{dt}=\dfrac{1}{2\sqrt{t+1}}=\dfrac14$",
       r"$\dfrac{dT}{dt}=2\cdot6+(-3)\cdot\dfrac14=12-\dfrac34=\dfrac{45}{4}$"],
  check=_c)


def _c():
    uu = (x**2*y + y*z**2).subs({x: r*s, y: r + s, z: r - s})
    assert EQ(diff(uu, r).subs({r: 1, s: 2}), 23)
P(id="3-16", ch=14, sec="14.5", type="14-chain", src="강의 14.5 ex5 · 과제 14.5 #27 유형",
  q=r"$u=x^2y+yz^2$, $x=rs$, $y=r+s$, $z=r-s$일 때 $(r,s)=(1,2)$에서 $\dfrac{\partial u}{\partial r}$를 구하라.",
  hint=r"$\dfrac{\partial u}{\partial r}=u_x x_r+u_y y_r+u_z z_r$",
  ans=r"$23$",
  sol=[r"$(r,s)=(1,2)$: $x=2,\ y=3,\ z=-1$",
       r"$u_x=2xy=12,\ \ u_y=x^2+z^2=5,\ \ u_z=2yz=-6$",
       r"$x_r=s=2,\ \ y_r=1,\ \ z_r=1$",
       r"$\dfrac{\partial u}{\partial r}=12\cdot2+5\cdot1+(-6)\cdot1=23$"],
  check=_c)


def _c():
    F = x**2 + 2*y**2 + 3*z**2
    assert F.subs({x: 1, y: 2, z: 2}) == 21
    assert EQ(grad(F, [x, y, z]).subs({x: 1, y: 2, z: 2}), [2, 8, 12])
P(id="3-17", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 ex8 유형",
  q=r"타원면 $x^2+2y^2+3z^2=21$ 위의 점 $(1,2,2)$에서의 접평면과 법선의 방정식을 구하라.",
  hint=r"$F(x,y,z)=x^2+2y^2+3z^2$로 두면 $\nabla F(1,2,2)$가 법선벡터예요.",
  ans=r"접평면 $x+4y+6z=21$,  법선 $\dfrac{x-1}{1}=\dfrac{y-2}{4}=\dfrac{z-2}{6}$",
  sol=[r"$\nabla F=\langle2x,4y,6z\rangle \Rightarrow \nabla F(1,2,2)=\langle2,8,12\rangle\parallel\langle1,4,6\rangle$",
       r"접평면: $(x-1)+4(y-2)+6(z-2)=0 \Rightarrow x+4y+6z=21$",
       r"법선: $\dfrac{x-1}{1}=\dfrac{y-2}{4}=\dfrac{z-2}{6}$"],
  check=_c)


def _c():
    f = x**2 + 2*y**2 - 2*x
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: 1, y: 0}
    g = (f.subs(y**2, 4 - x**2)).subs(y, sqrt(4 - x**2))
    g = x**2 + 2*(4 - x**2) - 2*x
    cands = [f.subs({x: 1, y: 0}), g.subs(x, -1), g.subs(x, 2), g.subs(x, -2)]
    assert max(cands) == 9 and min(cands) == -1
    import random
    random.seed(1)
    best_hi, best_lo = -1e9, 1e9
    for _ in range(20000):
        a = random.uniform(-2, 2); b = random.uniform(-2, 2)
        if a*a + b*b <= 4:
            val = a*a + 2*b*b - 2*a; best_hi = max(best_hi, val); best_lo = min(best_lo, val)
    assert best_hi <= 9 + 1e-9 and best_lo >= -1 - 1e-9 and best_hi > 8.9 and best_lo < -0.99
P(id="3-18", ch=14, sec="14.7", type="14-absext", src="복습 14.7–8 기초4 · 심화1 · 강의 14.7 ex7 유형",
  q=r"닫힌 원판 $D=\{(x,y)\mid x^2+y^2\le4\}$에서 $f(x,y)=x^2+2y^2-2x$의 최댓값과 최솟값을 구하라.",
  hint=r"① 내부 임계점 ② 경계에서는 $y^2=4-x^2$을 대입해 $-2\le x\le2$인 1변수 함수로 ③ 모두 비교.",
  ans=r"최댓값 $9$ (점 $(-1,\pm\sqrt3)$),  최솟값 $-1$ (점 $(1,0)$)",
  sol=[r"내부: $f_x=2x-2=0,\ f_y=4y=0 \Rightarrow (1,0)$, $f(1,0)=-1$",
       r"경계: $y^2=4-x^2$ → $g(x)=x^2+2(4-x^2)-2x=-x^2-2x+8,\ -2\le x\le2$",
       r"$g'(x)=-2x-2=0 \Rightarrow x=-1$: $g(-1)=9$ (점 $(-1,\pm\sqrt3)$);  끝점 $g(2)=0,\ g(-2)=8$",
       r"후보 비교: 최댓값 $9$, 최솟값 $-1$"],
  check=_c)


def _c():
    lam = symbols('lam')
    sols = solve([1 - 2*lam*x, 2 - 2*lam*y, 2 - 2*lam*z, x**2 + y**2 + z**2 - 9], [x, y, z, lam], dict=True)
    vals = sorted(simplify((x + 2*y + 2*z).subs(c)) for c in sols)
    assert vals == [-9, 9]
P(id="3-19", ch=14, sec="14.8", type="14-lagrange", src="강의 14.8 ex3 유형",
  q=r"구 $x^2+y^2+z^2=9$ 위에서 $f(x,y,z)=x+2y+2z$의 최댓값과 최솟값을 구하라.",
  hint=r"$\langle1,2,2\rangle=\lambda\langle2x,2y,2z\rangle$ → $(x,y,z)$는 $\langle1,2,2\rangle$에 평행해요.",
  ans=r"최댓값 $9$ (점 $(1,2,2)$),  최솟값 $-9$ (점 $(-1,-2,-2)$)",
  sol=[r"$1=2\lambda x,\ 2=2\lambda y,\ 2=2\lambda z \Rightarrow (x,y,z)=\dfrac{1}{2\lambda}\langle1,2,2\rangle$",
       r"제약: $\dfrac{1+4+4}{4\lambda^2}=9 \Rightarrow \lambda=\pm\dfrac12$",
       r"$\lambda=\tfrac12$: $(1,2,2)$, $f=9$;  $\lambda=-\tfrac12$: $(-1,-2,-2)$, $f=-9$"],
  check=_c)


# ───────── Ch.15 ─────────
def _c():
    assert EQ(integrate(x**2 + y**2, (y, x**2, x), (x, 0, 1)), R(3, 35))
P(id="3-20", ch=15, sec="15.2", type="15-general", src="복습 15.1–3 기초4 유형",
  q=r"곡선 $y=x$와 $y=x^2$으로 둘러싸인 영역 위, 포물면 $z=x^2+y^2$ 아래에 있는 입체의 부피를 구하라.",
  hint=r"$0\le x\le1$에서 $x^2\le y\le x$ (직선이 위쪽)",
  ans=r"$\dfrac{3}{35}$",
  sol=[r"$V=\displaystyle\int_0^1\!\!\int_{x^2}^{x}(x^2+y^2)\,dy\,dx=\int_0^1\Big[x^2y+\tfrac{y^3}{3}\Big]_{x^2}^{x}dx$",
       r"$=\displaystyle\int_0^1\Big(\tfrac43x^3-x^4-\tfrac{x^6}{3}\Big)dx=\frac13-\frac15-\frac1{21}=\frac{3}{35}$"],
  check=_c)


def _c():
    assert EQ(integrate(cos(y**2), (x, 0, 2*y), (y, 0, 1)), sin(1))
P(id="3-21", ch=15, sec="15.2", type="15-order", src="강의 15.2 ex5 유형",
  q=r"$\displaystyle\int_0^2\!\!\int_{x/2}^{1}\cos(y^2)\,dy\,dx$를 계산하라.",
  hint=r"$\cos(y^2)$은 $y$로 바로 적분할 수 없어요. 영역 $0\le x\le2,\ \tfrac x2\le y\le1$을 Type II로 바꿔요.",
  ans=r"$\sin1$",
  sol=[r"영역: $0\le y\le1,\ 0\le x\le2y$",
       r"$\displaystyle\int_0^1\!\!\int_0^{2y}\cos(y^2)\,dx\,dy=\int_0^1 2y\cos(y^2)\,dy$",
       r"$=\Big[\sin(y^2)\Big]_0^1=\sin1$"],
  check=_c)


def _c():
    A = integrate(R(1, 2)*((3*cos(th))**2 - (1 + cos(th))**2), (th, -pi/3, pi/3))
    assert EQ(A, pi)
P(id="3-22", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #17 · 강의 15.3 ex4 유형",
  q=r"원 $r=3\cos\theta$의 내부이면서 심장형 곡선 $r=1+\cos\theta$의 외부인 영역의 넓이를 구하라.",
  hint=r"교점: $3\cos\theta=1+\cos\theta \Rightarrow \cos\theta=\tfrac12$. 넓이 $=\displaystyle\int\tfrac12\left(r_{\rm out}^2-r_{\rm in}^2\right)d\theta$ (out: 바깥 곡선, in: 안쪽 곡선)",
  ans=r"$\pi$",
  sol=[r"교점 $\theta=\pm\dfrac{\pi}{3}$",
       r"$A=\displaystyle\int_{-\pi/3}^{\pi/3}\frac12\big[9\cos^2\theta-(1+\cos\theta)^2\big]d\theta=\int_{-\pi/3}^{\pi/3}\Big(4\cos^2\theta-\cos\theta-\tfrac12\Big)d\theta$",
       r"$4\cos^2\theta=2+2\cos2\theta$ 이므로 $\displaystyle\int_{-\pi/3}^{\pi/3}\Big(\tfrac32+2\cos2\theta-\cos\theta\Big)d\theta=\pi+\sqrt3-\sqrt3=\pi$"],
  check=_c)


def _c():
    assert EQ(integrate(4 - y, (y, x**2, 4), (x, -2, 2)), R(256, 15))
P(id="3-23", ch=15, sec="15.6", type="15-triple", src="강의 15.6 ex5 · 과제 15.6 #17 유형",
  q=r"포물기둥 $y=x^2$과 평면 $z=0$, $z=4-y$로 둘러싸인 입체의 부피를 구하라.",
  hint=r"밑면: $x^2\le y\le4$ ($-2\le x\le2$), 높이: $0\le z\le4-y$",
  ans=r"$\dfrac{256}{15}$",
  sol=[r"$V=\displaystyle\int_{-2}^{2}\!\!\int_{x^2}^{4}\!\!\int_0^{4-y}dz\,dy\,dx=\int_{-2}^{2}\!\!\int_{x^2}^{4}(4-y)\,dy\,dx$",
       r"$=\displaystyle\int_{-2}^{2}\Big(8-4x^2+\tfrac{x^4}{2}\Big)dx=2\Big(16-\tfrac{32}{3}+\tfrac{16}{5}\Big)=\frac{256}{15}$"],
  check=_c)


def _c():
    assert EQ(integrate(r**2 * r, (z, r**2, 4), (r, 0, 2), (th, 0, 2*pi)), 32*pi/3)
P(id="3-24", ch=15, sec="15.7", type="15-cyl", src="강의 15.7 ex3 · 복습 15.6–8 기초3 유형",
  q=r"$E$가 포물면 $z=x^2+y^2$과 평면 $z=4$로 둘러싸인 입체일 때 $\displaystyle\iiint_E(x^2+y^2)\,dV$를 구하라.",
  hint=r"원주좌표: $r^2\le z\le4$, $0\le r\le2$, $dV=r\,dz\,dr\,d\theta$",
  ans=r"$\dfrac{32\pi}{3}$",
  sol=[r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2\!\!\int_{r^2}^{4}r^2\cdot r\,dz\,dr\,d\theta=2\pi\int_0^2 r^3(4-r^2)\,dr$",
       r"$=2\pi\Big(16-\dfrac{64}{6}\Big)=2\pi\cdot\dfrac{16}{3}=\dfrac{32\pi}{3}$"],
  check=_c)


def _c():
    V = integrate(rho**2*sin(ph), (rho, 0, 2), (ph, 0, pi/4), (th, 0, 2*pi))
    assert EQ(V, 8*pi/3*(2 - sqrt(2)))
P(id="3-25", ch=15, sec="15.8", type="15-sph", src="과제 15.3 #35 · 복습 15.6–8 기초4 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=4$ 아래에 있는 입체의 부피를 구면좌표로 구하라.",
  hint=r"원뿔 $z=\sqrt{x^2+y^2}$ ⇔ $\phi=\tfrac\pi4$, 구 ⇔ $\rho=2$",
  ans=r"$\dfrac{8\pi}{3}\left(2-\sqrt2\right)$",
  sol=[r"$E: 0\le\rho\le2,\ 0\le\phi\le\tfrac\pi4,\ 0\le\theta\le2\pi$",
       r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^2\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\Big(1-\tfrac{\sqrt2}{2}\Big)\cdot\tfrac83$",
       r"$=\dfrac{16\pi}{3}\cdot\dfrac{2-\sqrt2}{2}=\dfrac{8\pi}{3}(2-\sqrt2)$"],
  check=_c)


# ───────── Ch.16 ─────────
def _c():
    rr = Matrix([2*cos(t), 2*sin(t), t])
    sp = simplify(rr.diff(t).norm())
    assert EQ(sp, sqrt(5)) and EQ(integrate(t*sqrt(5), (t, 0, pi)), sqrt(5)*pi**2/2)
P(id="3-26", ch=16, sec="16.2", type="16-scalar", src="강의 16.2 ex3 · ex5 유형",
  q=r"나선 모양의 철사 $\mathbf r(t)=\langle 2\cos t,\ 2\sin t,\ t\rangle$, $0\le t\le\pi$의 밀도가 $\rho(x,y,z)=z$일 때 철사의 질량을 구하라.",
  hint=r"질량 $m=\displaystyle\int_C\rho\,ds$,  $ds=|\mathbf r'(t)|\,dt$",
  ans=r"$\dfrac{\sqrt5\,\pi^2}{2}$",
  sol=[r"$|\mathbf r'(t)|=\sqrt{4\sin^2t+4\cos^2t+1}=\sqrt5$",
       r"$m=\displaystyle\int_0^{\pi}t\cdot\sqrt5\,dt=\sqrt5\cdot\frac{\pi^2}{2}$"],
  check=_c)


def _c():
    rr = Matrix([t, t**2, t**3]); Fv = Matrix([rr[1], rr[2], rr[0]])
    assert EQ(integrate(Fv.dot(rr.diff(t)), (t, 0, 1)), R(89, 60))
P(id="3-27", ch=16, sec="16.2", type="16-vector", src="복습 16.1–4 기초4 · 과제 16.2 #24 유형",
  q=r"힘 $\mathbf F(x,y,z)=\langle y,\ z,\ x\rangle$가 꼬인 3차 곡선 $\mathbf r(t)=\langle t,t^2,t^3\rangle$, $0\le t\le1$을 따라 입자를 움직일 때 한 일을 구하라.",
  hint=r"$W=\displaystyle\int_0^1\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$",
  ans=r"$\dfrac{89}{60}$",
  sol=[r"$\mathbf F(\mathbf r(t))=\langle t^2,\ t^3,\ t\rangle$,  $\mathbf r'(t)=\langle1,\ 2t,\ 3t^2\rangle$",
       r"$\mathbf F\cdot\mathbf r'=t^2+2t^4+3t^3$",
       r"$W=\dfrac13+\dfrac25+\dfrac34=\dfrac{20+24+45}{60}=\dfrac{89}{60}$"],
  check=_c)


def _c():
    Fv = Matrix([2*x*z + y**2, 2*x*y, x**2 + 3*z**2])
    f = x**2*z + x*y**2 + z**3
    assert EQ(grad(f, [x, y, z]), Fv)
    assert EQ(f.subs({x: 2, y: -1, z: 1}) - f.subs({x: 1, y: 1, z: 0}), 6)
P(id="3-28", ch=16, sec="16.3", type="16-ftli", src="강의 16.3 ex5 · 과제 16.3 #16 유형",
  q=r"$\mathbf F=\langle 2xz+y^2,\ 2xy,\ x^2+3z^2\rangle$의 퍼텐셜 함수를 구하고, $(1,1,0)$에서 $(2,-1,1)$까지의 임의의 경로 $C$를 따라 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$f_x=2xz+y^2$을 $x$로 적분 → $f_y,\ f_z$와 비교",
  ans=r"$f=x^2z+xy^2+z^3+K$,  $\displaystyle\int_C\mathbf F\cdot d\mathbf r=6$",
  sol=[r"보존장 확인: $P_y=2y=Q_x,\ Q_z=0=R_y,\ R_x=2x=P_z$",
       r"$f=x^2z+xy^2+g(y,z)$, $f_y=2xy+g_y=2xy\Rightarrow g=h(z)$, $f_z=x^2+h'(z)=x^2+3z^2 \Rightarrow h=z^3$",
       r"$f(2,-1,1)-f(1,1,0)=(4+2+1)-(0+1+0)=6$"],
  check=_c)


def _c():
    Pf, Qf = 2*x*cos(y) - y*cos(x), -x**2*sin(y) - sin(x)
    assert EQ(diff(Pf, y), diff(Qf, x))
    f = x**2*cos(y) - y*sin(x)
    assert EQ(diff(f, x), Pf) and EQ(diff(f, y), Qf)
    assert EQ(f.subs({x: pi/2, y: pi}) - f.subs({x: 0, y: 0}), -pi**2/4 - pi)
P(id="3-29", ch=16, sec="16.3", type="16-conserv", src="과제 16.3 #7 · #14 유형",
  q=r"$\mathbf F=\langle 2x\cos y-y\cos x,\ -x^2\sin y-\sin x\rangle$가 보존장임을 보이고, $(0,0)$에서 $\left(\tfrac{\pi}{2},\ \pi\right)$까지 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$P_y$와 $Q_x$를 비교한 뒤 $f_x=P$를 $x$로 적분해요.",
  ans=r"보존장, $f=x^2\cos y-y\sin x+K$,  값 $-\dfrac{\pi^2}{4}-\pi$",
  sol=[r"$P_y=-2x\sin y-\cos x,\ \ Q_x=-2x\sin y-\cos x$ → 같으므로 보존장 ($\mathbb R^2$)",
       r"$f=x^2\cos y-y\sin x+g(y)$,  $f_y=-x^2\sin y-\sin x+g'(y)=Q \Rightarrow g'=0$",
       r"$f\!\left(\tfrac\pi2,\pi\right)-f(0,0)=\tfrac{\pi^2}{4}(-1)-\pi\cdot1-0=-\dfrac{\pi^2}{4}-\pi$"],
  check=_c)


def _c():
    assert EQ(integrate((3*x**2 + 3*y**2).subs({x: r*cos(th), y: r*sin(th)}) * r, (r, 1, 2), (th, 0, 2*pi)), 45*pi/2)
P(id="3-30", ch=16, sec="16.4", type="16-green", src="과제 16.4 #12 · 강의 16.4 ex4 유형",
  q=r"$C$가 두 원 $x^2+y^2=1$과 $x^2+y^2=4$ 사이 영역의 경계(양의 방향)일 때 $\displaystyle\oint_C -y^3\,dx+x^3\,dy$를 구하라.",
  hint=r"양의 방향 = 영역이 항상 왼쪽 (바깥 원 반시계, 안쪽 원 시계). 그린 정리 후 극좌표.",
  ans=r"$\dfrac{45\pi}{2}$",
  sol=[r"$Q_x-P_y=3x^2+3y^2=3r^2$",
       r"$\displaystyle\iint_D 3r^2\,dA=\int_0^{2\pi}\!\!\int_1^2 3r^3\,dr\,d\theta=2\pi\cdot\frac34(16-1)=\frac{45\pi}{2}$"],
  check=_c)

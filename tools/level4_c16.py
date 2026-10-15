"""4단계 · 심화 추가분 — Ch.16 벡터 미적분: 4-102 ~ 4-120"""
from bank_lib import *
from sympy import atan, lambdify
import mpmath as mp


def line_int(F, rr, a, b, vars_=(x, y, z)):
    sub = dict(zip(vars_, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    return integrate(simplify(integrand), (t, a, b))


def line_num(F, rr, a, b, vars_=(x, y, z), pts=None):
    sub = dict(zip(vars_, rr))
    integrand = sum(sympify(Fi).subs(sub, simultaneous=True) * diff(ri, t) for Fi, ri in zip(F, rr))
    fn = lambdify(t, integrand, 'mpmath')
    nodes = pts if pts else [a, b]
    return mp.quad(fn, [mp.mpf(float(N(q, 30))) for q in nodes])


def seg(p0, p1):
    return [a0 + (a1 - a0)*t for a0, a1 in zip(p0, p1)]


# ───────── 16.1 ─────────
def _c():
    rr = sqrt(x**2 + y**2 + z**2)
    F = -Matrix([x, y, z])/rr**3
    f = 1/rr
    assert all(simplify(a - b) == 0 for a, b in zip(grad(f, [x, y, z]), F))
    assert simplify(F.norm()**2 - 1/rr**4) == 0
    assert EQ(f.subs({x: 0, y: 3, z: 4}) - f.subs({x: 1, y: 2, z: 2}), R(-2, 15))
    W = line_num(list(F), seg((1, 2, 2), (0, 3, 4)), 0, 1)
    assert abs(W + mp.mpf(2)/15) < 1e-12
P(id="4-102", ch=16, sec="16.1", type="16-field", src="강의 16.1 역제곱 법칙 벡터장 확장",
  q=r"$\mathbf r=\langle x,y,z\rangle$, $\mathbf F(x,y,z)=-\dfrac{\mathbf r}{|\mathbf r|^3}$ (원점으로 끌어당기는 역제곱 법칙 힘)에 대해<br>(a) $|\mathbf F|$와 $\mathbf F$의 방향을 말하라.  (b) $\mathbf F=\nabla f$, $f(x,y,z)=\dfrac{1}{\sqrt{x^2+y^2+z^2}}$임을 보여라.  (c) 입자를 $(1,2,2)$에서 $(0,3,4)$까지 옮길 때 $\mathbf F$가 한 일을 구하라. (경로는 원점을 지나지 않음)",
  hint=r"$\dfrac{\partial}{\partial x}(x^2+y^2+z^2)^{-1/2}=-x(x^2+y^2+z^2)^{-3/2}$. (c)는 선적분의 기본정리: $W=f(\text{끝})-f(\text{시작})$.",
  ans=r"(a) $|\mathbf F|=\dfrac1{|\mathbf r|^2}$, 원점을 향함  (b) 아래 풀이  (c) $-\dfrac{2}{15}$",
  sol=[r"(a) $|\mathbf F|=\dfrac{|\mathbf r|}{|\mathbf r|^3}=\dfrac{1}{x^2+y^2+z^2}$, 방향은 $-\mathbf r$ (원점 쪽)",
       r"(b) $f_x=-\tfrac12(x^2+y^2+z^2)^{-3/2}\cdot2x=-\dfrac{x}{|\mathbf r|^3}$, $f_y,f_z$도 같은 꼴 → $\nabla f=-\dfrac{\mathbf r}{|\mathbf r|^3}=\mathbf F$",
       r"(c) $|(1,2,2)|=3,\ |(0,3,4)|=5$ → $W=f(0,3,4)-f(1,2,2)=\dfrac15-\dfrac13=-\dfrac2{15}$ (원점에서 멀어지므로 끌어당기는 힘이 음의 일)"],
  check=_c)


# ───────── 16.2 ─────────
def _c():
    rr = [cos(t), sin(t), t]
    sp = sqrt(2)
    M = integrate(t*sp, (t, 0, pi))
    Mx = integrate(cos(t)*t*sp, (t, 0, pi)); My = integrate(sin(t)*t*sp, (t, 0, pi)); Mz = integrate(t*t*sp, (t, 0, pi))
    assert EQ(M, sqrt(2)*pi**2/2)
    assert EQ(Mx/M, -4/pi**2) and EQ(My/M, 2/pi) and EQ(Mz/M, 2*pi/3)
    v = Matrix(rr).diff(t)
    assert simplify(v.norm() - sqrt(2)) == 0
P(id="4-103", ch=16, sec="16.2", type="16-scalar", src="2022 기말 블럭2 2번 유형 (철사의 질량중심)",
  q=r"나선 $\mathbf r(t)=\langle\cos t,\ \sin t,\ t\rangle\ (0\le t\le\pi)$ 모양의 철사의 밀도가 $\delta(x,y,z)=z$일 때 철사의 질량과 질량중심을 구하라.",
  hint=r"$ds=|\mathbf r'(t)|dt=\sqrt2\,dt$. $\bar x=\dfrac1m\displaystyle\int_Cx\,\delta\,ds$ 등. $\int t\cos t\,dt$, $\int t\sin t\,dt$는 부분적분.",
  ans=r"질량 $\dfrac{\sqrt2\pi^2}{2}$, 질량중심 $\Big(-\dfrac{4}{\pi^2},\ \dfrac2\pi,\ \dfrac{2\pi}{3}\Big)$",
  sol=[r"$|\mathbf r'|=|\langle-\sin t,\cos t,1\rangle|=\sqrt2$, $\delta=t$",
       r"$m=\displaystyle\int_0^\pi t\sqrt2\,dt=\frac{\sqrt2\pi^2}{2}$",
       r"$\displaystyle\int_0^\pi t\cos t\,dt=\Big[t\sin t+\cos t\Big]_0^\pi=-2$, $\displaystyle\int_0^\pi t\sin t\,dt=\Big[-t\cos t+\sin t\Big]_0^\pi=\pi$, $\displaystyle\int_0^\pi t^2dt=\frac{\pi^3}3$",
       r"$\bar x=\dfrac{-2\sqrt2}{\sqrt2\pi^2/2}=-\dfrac4{\pi^2}$, $\bar y=\dfrac{\sqrt2\pi}{\sqrt2\pi^2/2}=\dfrac2\pi$, $\bar z=\dfrac{\sqrt2\pi^3/3}{\sqrt2\pi^2/2}=\dfrac{2\pi}3$"],
  check=_c)


def _c():
    e1 = Matrix([1, -1, 0])/sqrt(2); e2 = Matrix([1, 1, -2])/sqrt(6)
    rr = 2*cos(t)*e1 + 2*sin(t)*e2
    assert simplify(rr.dot(rr) - 4) == 0 and simplify(sum(rr)) == 0
    sp = simplify(rr.diff(t).norm())
    assert sp == 2
    assert EQ(integrate(rr.dot(rr)*2, (t, 0, 2*pi)), 16*pi)
    assert EQ(integrate(rr[0]**2*2, (t, 0, 2*pi)), 16*pi/3)
    assert EQ(integrate(rr[0]*rr[1]*2, (t, 0, 2*pi)), -8*pi/3)
P(id="4-104", ch=16, sec="16.2", type="16-scalar", src="교재 16.2 심화형 (대칭성 이용)",
  q=r"$C$가 구 $x^2+y^2+z^2=4$와 평면 $x+y+z=0$의 교선일 때<br>(a) $\displaystyle\int_C(x^2+y^2+z^2)\,ds$  (b) $\displaystyle\int_Cx^2\,ds$  (c) $\displaystyle\int_Cxy\,ds$를 구하라.",
  hint=r"$C$는 중심이 원점인 반지름 $2$의 원(대원) → 길이 $4\pi$. (b) $x,y,z$의 역할이 대칭이라 $\int x^2ds=\int y^2ds=\int z^2ds$. (c) $(x+y+z)^2=0$을 전개해 보세요.",
  ans=r"(a) $16\pi$  (b) $\dfrac{16\pi}{3}$  (c) $-\dfrac{8\pi}{3}$",
  sol=[r"평면이 원점을 지나므로 $C$는 반지름 $2$인 원, 길이 $4\pi$",
       r"(a) $C$ 위에서 $x^2+y^2+z^2=4$ → $\displaystyle\int_C4\,ds=4\cdot4\pi=16\pi$",
       r"(b) 대칭성: $\int x^2=\int y^2=\int z^2$ → 각각 $\dfrac{16\pi}3$",
       r"(c) $0=(x+y+z)^2=(x^2+y^2+z^2)+2(xy+yz+zx)$ → $C$ 위에서 $xy+yz+zx=-2$",
       r"$\displaystyle\int_C(xy+yz+zx)\,ds=-2\cdot4\pi=-8\pi$, 대칭으로 셋이 같으니 $\displaystyle\int_Cxy\,ds=-\frac{8\pi}3$"],
  check=_c)


def _c():
    rr = [cos(t), sin(t), cos(t) + sin(t)]
    assert EQ(line_int([y, z, x], rr, 0, 2*pi), pi)
P(id="4-105", ch=16, sec="16.2", type="16-vector", src="2024 기말 2(a) 유형 (공간곡선 위 선적분)",
  q=r"$C$가 원기둥 $x^2+y^2=1$과 평면 $z=x+y$의 교선(위에서 볼 때 반시계 방향)일 때 $\displaystyle\oint_Cy\,dx+z\,dy+x\,dz$를 계산하라.",
  hint=r"$\mathbf r(t)=\langle\cos t,\ \sin t,\ \cos t+\sin t\rangle,\ 0\le t\le2\pi$. $\sin t\cos t$ 항은 한 주기에서 적분이 $0$.",
  ans=r"$\pi$",
  sol=[r"$dx=-\sin t\,dt,\ dy=\cos t\,dt,\ dz=(\cos t-\sin t)\,dt$",
       r"$y\,dx=-\sin^2t$, $z\,dy=\cos^2t+\sin t\cos t$, $x\,dz=\cos^2t-\sin t\cos t$",
       r"합 $=-\sin^2t+2\cos^2t$ → $\displaystyle\int_0^{2\pi}(-\sin^2t+2\cos^2t)\,dt=-\pi+2\pi=\pi$"],
  check=_c)


def _c():
    F = [-y, x, z]
    W1 = line_int(F, [cos(t), sin(t), t], 0, 2*pi)
    W2 = line_int(F, [1, 0, t], 0, 2*pi)
    assert EQ(W1, 2*pi + 2*pi**2) and EQ(W2, 2*pi**2)
P(id="4-106", ch=16, sec="16.2", type="16-vector", src="교재 16.2 심화형 (경로에 따라 다른 일)",
  q=r"$\mathbf F(x,y,z)=\langle-y,\ x,\ z\rangle$가 입자를 $(1,0,0)$에서 $(1,0,2\pi)$까지 옮길 때 한 일을<br>(a) 나선 $C_1:\ \mathbf r(t)=\langle\cos t,\sin t,t\rangle\ (0\le t\le2\pi)$  (b) 선분 $C_2$를 따라 각각 구하라.  (c) $\mathbf F$는 보존장인가?",
  hint=r"(a) $\mathbf F\cdot\mathbf r'=\sin^2t+\cos^2t+t$. (b) 선분은 $\langle1,0,t\rangle$. 같은 두 점을 잇는 두 경로의 값이 다르면?",
  ans=r"(a) $2\pi+2\pi^2$  (b) $2\pi^2$  (c) 아니다 (경로에 따라 값이 다름)",
  sol=[r"(a) $\mathbf F(\mathbf r(t))=\langle-\sin t,\cos t,t\rangle$, $\mathbf r'=\langle-\sin t,\cos t,1\rangle$ → $\mathbf F\cdot\mathbf r'=1+t$",
       r"$\displaystyle\int_0^{2\pi}(1+t)\,dt=2\pi+2\pi^2$",
       r"(b) $\mathbf r=\langle1,0,t\rangle$, $\mathbf r'=\langle0,0,1\rangle$, $\mathbf F=\langle0,1,t\rangle$ → $\displaystyle\int_0^{2\pi}t\,dt=2\pi^2$",
       r"(c) 같은 시작점·끝점인데 값이 다름 → 선적분이 경로에 의존 → 보존장이 아니다 (실제로 $x,y$ 성분 $\langle-y,x\rangle$에서 $Q_x-P_y=2\ne0$)"],
  check=_c)


def _c():
    integrand = 2*cos(t)*sin(t)*sqrt(4*sin(t)**2 + cos(t)**2)
    w = symbols('w', positive=True)
    assert EQ(integrate(sqrt(1 + 3*w), (w, 0, 1)), R(14, 9))
    num = mp.quad(lambdify(t, integrand, 'mpmath'), [0, mp.pi/2])
    assert abs(num - mp.mpf(14)/9) < 1e-12
P(id="4-107", ch=16, sec="16.2", type="16-scalar", src="교재 16.2 심화형 (타원 위 스칼라 선적분)",
  q=r"$C$가 제1사분면에 있는 타원 $\dfrac{x^2}{4}+y^2=1$의 부분일 때 $\displaystyle\int_Cxy\,ds$를 계산하라.",
  hint=r"$x=2\cos t,\ y=\sin t\ (0\le t\le\tfrac\pi2)$, $ds=\sqrt{4\sin^2t+\cos^2t}\,dt=\sqrt{1+3\sin^2t}\,dt$. $w=\sin^2t$로 치환하면 $dw=2\sin t\cos t\,dt$.",
  ans=r"$\dfrac{14}{9}$",
  sol=[r"$\displaystyle\int_Cxy\,ds=\int_0^{\pi/2}2\cos t\sin t\sqrt{1+3\sin^2t}\,dt$",
       r"$w=\sin^2t$: $\displaystyle\int_0^1\sqrt{1+3w}\,dw=\Big[\frac{2}{9}(1+3w)^{3/2}\Big]_0^1=\frac29(8-1)=\frac{14}{9}$"],
  check=_c)


# ───────── 16.3 ─────────
def _c():
    a, b, c = symbols('a b c')
    P_, Q_, R_ = y**2 + a*x*z, b*x*y + z**2, 3*x**2 + c*y*z
    sol = solve([diff(P_, y) - diff(Q_, x), diff(P_, z) - diff(R_, x), diff(Q_, z) - diff(R_, y)], [a, b, c], dict=True)
    sol = [q for q in sol if all(v.is_number for v in q.values())]
    assert sol == [{a: 6, b: 2, c: 2}]
    f = x*y**2 + 3*x**2*z + y*z**2
    F = [P_.subs(sol[0]), Q_.subs(sol[0]), R_.subs(sol[0])]
    assert all(simplify(g - h) == 0 for g, h in zip(grad(f, [x, y, z]), F))
    rr = [cos(pi*t), t, t**2]
    assert EQ(line_int(F, rr, 0, 1), 3)
P(id="4-108", ch=16, sec="16.3", type="16-conserv", src="2024 기말 2(b) 유형 (상수 결정 + 퍼텐셜)",
  q=r"$\mathbf F(x,y,z)=\big\langle y^2+axz,\ bxy+z^2,\ 3x^2+cyz\big\rangle$가 보존장이 되도록 상수 $a,b,c$를 정하고, 그때 퍼텐셜 함수 $f$를 구하라. 또 $C:\ \mathbf r(t)=\langle\cos\pi t,\ t,\ t^2\rangle\ (0\le t\le1)$를 따라 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"교차 편도함수 조건 $P_y=Q_x,\ P_z=R_x,\ Q_z=R_y$. 퍼텐셜은 $f=\int P\,dx$에서 시작해 $y,z$ 항을 맞춰요.",
  ans=r"$a=6,\ b=2,\ c=2$, $f=xy^2+3x^2z+yz^2$, 선적분 $3$",
  sol=[r"$P_y=2y=Q_x=by \Rightarrow b=2$;  $P_z=ax=R_x=6x \Rightarrow a=6$;  $Q_z=2z=R_y=cz \Rightarrow c=2$",
       r"$f=\displaystyle\int(y^2+6xz)\,dx=xy^2+3x^2z+g(y,z)$, $f_y=2xy+g_y=2xy+z^2 \Rightarrow g=yz^2+h(z)$, $f_z=3x^2+2yz+h'=3x^2+2yz \Rightarrow h$ 상수",
       r"$f=xy^2+3x^2z+yz^2$",
       r"$\mathbf r(0)=(1,0,0)$, $\mathbf r(1)=(-1,1,1)$ → $\displaystyle\int_C\mathbf F\cdot d\mathbf r=f(-1,1,1)-f(1,0,0)=(-1+3+1)-0=3$"],
  check=_c)


def _c():
    F = [2*x*y + y, x**2 + 2*y]
    rr = [2*cos(t), 2*sin(t)]
    assert EQ(line_int(F, rr, 0, pi/2, (x, y)), 4 - pi)
    f = x**2*y + y**2
    assert EQ(f.subs({x: 0, y: 2}) - f.subs({x: 2, y: 0}), 4)
    assert EQ(line_int([y, 0], rr, 0, pi/2, (x, y)), -pi)
P(id="4-109", ch=16, sec="16.3", type="16-ftli", src="교재 16.3 심화형 (보존장 + 나머지로 분리)",
  q=r"$C$가 원 $x^2+y^2=4$ 위를 $(2,0)$에서 $(0,2)$까지 반시계 방향으로 가는 호일 때 $\displaystyle\int_C(2xy+y)\,dx+(x^2+2y)\,dy$를 계산하라.",
  hint=r"$\mathbf F=\langle2xy,\ x^2+2y\rangle+\langle y,\ 0\rangle$로 나누면 앞부분은 $\nabla(x^2y+y^2)$ — 기본정리로, 뒷부분 $\int_Cy\,dx$만 직접 계산해요.",
  ans=r"$4-\pi$",
  sol=[r"$\langle2xy,\ x^2+2y\rangle=\nabla f$, $f=x^2y+y^2$ → 그 부분의 적분 $=f(0,2)-f(2,0)=4-0=4$",
       r"$\displaystyle\int_Cy\,dx$: $x=2\cos t,\ y=2\sin t\ (0\le t\le\tfrac\pi2)$ → $\displaystyle\int_0^{\pi/2}2\sin t(-2\sin t)\,dt=-4\cdot\frac\pi4=-\pi$",
       r"합: $4-\pi$"],
  check=_c)


def _c():
    P_, Q_ = -y/(x**2 + y**2), x/(x**2 + y**2)
    assert simplify(diff(P_, y) - diff(Q_, x)) == 0
    assert EQ(line_int([P_, Q_], [cos(t), sin(t)], 0, 2*pi, (x, y)), 2*pi)
    xp = symbols('xp', positive=True)
    f = atan(y/xp)
    assert simplify(diff(f, xp) - P_.subs(x, xp)) == 0 and simplify(diff(f, y) - Q_.subs(x, xp)) == 0
    assert EQ(f.subs({xp: 1, y: 1}) - f.subs({xp: 1, y: -1}), pi/2)
    rr = [sqrt(2)*cos(t), sqrt(2)*sin(t)]
    assert EQ(line_int([P_, Q_], rr, -pi/4, -7*pi/4, (x, y)), -3*pi/2)
P(id="4-110", ch=16, sec="16.3", type="16-conserv", src="교재 16.3 심화형 (정의역과 보존장)",
  q=r"$\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$에 대해<br>(a) $P_y=Q_x$임을 확인하라.  (b) 단위원을 반시계 방향으로 한 바퀴 도는 선적분을 구하고, $\mathbf F$가 $\mathbb R^2\setminus\{(0,0)\}$에서 보존장이 아님을 설명하라.<br>(c) 오른쪽 반평면 $x>0$에서는 $\mathbf F=\nabla\big(\tan^{-1}\tfrac yx\big)$임을 보이고, 이 반평면 안의 경로로 $(1,-1)$에서 $(1,1)$까지 가는 선적분을 구하라.<br>(d) 원 $x^2+y^2=2$를 따라 시계 방향으로 (왼쪽을 돌아) $(1,-1)$에서 $(1,1)$까지 가면 값은?",
  hint=r"(b) $\cos t,\sin t$ 대입하면 피적분함수가 $1$. (c) $\tfrac{\partial}{\partial x}\tan^{-1}\tfrac yx=\dfrac{-y}{x^2+y^2}$. (d) $\mathbf F\cdot d\mathbf r=d\theta$ — 각이 얼마나 변했는지 세어 보세요.",
  ans=r"(b) $2\pi\ne0$ → 보존장 아님  (c) $\dfrac\pi2$  (d) $-\dfrac{3\pi}{2}$",
  sol=[r"(a) $P_y=\dfrac{-(x^2+y^2)+2y^2}{(x^2+y^2)^2}=\dfrac{y^2-x^2}{(x^2+y^2)^2}=Q_x$",
       r"(b) $\displaystyle\oint=\int_0^{2\pi}(\sin^2t+\cos^2t)\,dt=2\pi\ne0$ → 닫힌 곡선 적분이 $0$이 아니므로 보존장이 아님. ($\mathbb R^2\setminus\{0\}$은 단순연결이 아니라 $P_y=Q_x$만으로는 부족)",
       r"(c) $x>0$에서 $f=\tan^{-1}\tfrac yx$: $f_x=\dfrac{-y}{x^2+y^2},\ f_y=\dfrac{x}{x^2+y^2}$ → $\mathbf F=\nabla f$. 값 $=f(1,1)-f(1,-1)=\tfrac\pi4-(-\tfrac\pi4)=\tfrac\pi2$",
       r"(d) 각 $\theta$가 $-\tfrac\pi4$에서 시계 방향으로 $-\tfrac{7\pi}4$까지 변함 → $\displaystyle\int d\theta=-\frac{7\pi}{4}+\frac\pi4=-\frac{3\pi}{2}$ (이 경로는 반평면을 벗어나 원점을 돌아가요)"],
  check=_c)


def _c():
    F = [y*z + 2*x, x*z, x*y + y]
    f = x*y*z + x**2
    G = [F[0] - diff(f, x), F[1] - diff(f, y), F[2] - diff(f, z)]
    assert [simplify(g) for g in G] == [0, 0, y]
    rr = [cos(t), sin(t), cos(t) + sin(3*t)]
    assert EQ(line_int(F, rr, 0, 2*pi), -pi)
P(id="4-111", ch=16, sec="16.3", type="16-ftli", src="2022 기말 블럭1 2번 유형 (거의 보존장)",
  q=r"$\mathbf F(x,y,z)=\big\langle yz+2x,\ xz,\ xy+y\big\rangle$이고 $C:\ \mathbf r(t)=\langle\cos t,\ \sin t,\ \cos t+\sin3t\rangle\ (0\le t\le2\pi)$일 때 $\displaystyle\oint_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\mathbf F=\nabla(xyz+x^2)+\langle0,0,y\rangle$. $C$는 닫힌 곡선이라 기울기장 부분은 $0$이고 $\oint y\,dz$만 남아요.",
  ans=r"$-\pi$",
  sol=[r"$\nabla(xyz+x^2)=\langle yz+2x,\ xz,\ xy\rangle$ → $\mathbf F=\nabla(xyz+x^2)+\langle0,0,y\rangle$",
       r"$\mathbf r(0)=\mathbf r(2\pi)$ (닫힌 곡선) → 기울기장 부분의 적분 $=0$",
       r"$\displaystyle\oint_Cy\,dz=\int_0^{2\pi}\sin t\,(-\sin t+3\cos3t)\,dt=-\pi+3\int_0^{2\pi}\sin t\cos3t\,dt=-\pi+0=-\pi$"],
  check=_c)


def _c():
    A_, B_ = 3, 1
    tq = symbols('tq', real=True)
    rr = Matrix([cos(tq), sin(tq), 1 - tq])
    assert simplify(rr[0]**2 + rr[1]**2 - rr[2] - tq) == 0
    assert simplify(rr.diff(tq).norm() - sqrt(2)) == 0
    for fexpr in (6 - 6*u, 12*u**2 - 18*u + 8):
        assert EQ(integrate(fexpr, (u, 0, 1)), A_) and EQ(integrate(u*fexpr, (u, 0, 1)), B_)
        G = integrate(fexpr, (u, 0, tq))
        assert EQ(integrate(G*sqrt(2), (tq, 0, 1)), 2*sqrt(2))


P(id="4-112", ch=16, sec="16.3", type="16-ftli", src="2024 기말 3번 유형",
  q=r"연속함수 $f$가 $\displaystyle\int_0^1f(u)\,du=3,\ \int_0^1uf(u)\,du=1$을 만족하고 $g(x,y,z)=\displaystyle\int_0^{x^2+y^2-z}f(u)\,du$이다.<br>(a) $C_1$이 $(0,0,0)$에서 $(1,1,1)$까지 가는 임의의 매끄러운 곡선일 때 $\displaystyle\int_{C_1}2xf(x^2+y^2-z)\,dx+2yf(x^2+y^2-z)\,dy-f(x^2+y^2-z)\,dz$를 구하라.<br>(b) $C_2:\ \mathbf r(t)=\langle\cos t,\ \sin t,\ 1-t\rangle\ (0\le t\le1)$일 때 $\displaystyle\int_{C_2}g(x,y,z)\,ds$를 구하라.",
  hint=r"(a) 피적분 벡터장은 $\nabla g$ (미적분학의 기본정리 + 연쇄법칙). (b) $C_2$ 위에서 $x^2+y^2-z=t$이므로 $g=G(t)=\int_0^tf$. $\int_0^1G(t)\,dt$는 부분적분.",
  ans=r"(a) $3$  (b) $2\sqrt2$",
  sol=[r"(a) $g_x=f(x^2+y^2-z)\cdot2x$, $g_y=f(\cdot)\cdot2y$, $g_z=-f(\cdot)$ → 피적분장 $=\nabla g$",
       r"값 $=g(1,1,1)-g(0,0,0)=\displaystyle\int_0^{1}f\,du-0=3$ ($1+1-1=1$)",
       r"(b) $C_2$ 위: $x^2+y^2-z=1-(1-t)=t$, $|\mathbf r'|=|\langle-\sin t,\cos t,-1\rangle|=\sqrt2$",
       r"$\displaystyle\int_{C_2}g\,ds=\sqrt2\int_0^1G(t)\,dt=\sqrt2\Big(\big[tG(t)\big]_0^1-\int_0^1tf(t)\,dt\Big)=\sqrt2(3-1)=2\sqrt2$"],
  check=_c)


# ───────── 16.4 ─────────
def _c():
    F = [y**2 + x*exp(x), 2*x*y + 2*x + cos(y)]
    assert simplify(diff(F[1], x) - diff(F[0], y)) == 2
    A_half = integrate(r, (r, 0, 1 + cos(th)), (th, 0, pi))
    assert EQ(A_half, 3*pi/4)
    seg_int = integrate(x*exp(x), (x, 0, 2))
    assert EQ(seg_int, E**2 + 1)
    rr = [(1 + cos(t))*cos(t), (1 + cos(t))*sin(t)]
    num = line_num(F, rr, 0, pi, (x, y))
    assert abs(num - (3*mp.pi/2 - mp.e**2 - 1)) < 1e-10
P(id="4-113", ch=16, sec="16.4", type="16-green", src="2022 기말 블럭2 4번 유형 (열린 곡선을 닫아서)",
  q=r"$\mathbf F(x,y)=\big\langle y^2+xe^{x},\ 2xy+2x+\cos y\big\rangle$이고 $C$가 극곡선 $r=1+\cos\theta\ (0\le\theta\le\pi)$를 $\theta$가 커지는 방향으로 따라가는 곡선일 때, 그린 정리를 이용해 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$C$는 $(2,0)$에서 $(0,0)$까지 가는 열린 곡선 → $x$축 선분 $L$: $(0,0)\to(2,0)$을 붙이면 위쪽 반 심장형 영역의 양의 방향 경계. $Q_x-P_y=2$.",
  ans=r"$\dfrac{3\pi}{2}-e^2-1$",
  sol=[r"$C+L$은 $D=\{0\le\theta\le\pi,\ 0\le r\le1+\cos\theta\}$의 양의 방향 경계, $Q_x-P_y=(2y+2)-2y=2$",
       r"$\displaystyle\oint_{C+L}=\iint_D2\,dA=2\cdot\frac12\int_0^\pi(1+\cos\theta)^2d\theta=\pi+\frac\pi2=\frac{3\pi}{2}$",
       r"$L$: $y=0,\ dy=0$ → $\displaystyle\int_L\mathbf F\cdot d\mathbf r=\int_0^2xe^x\,dx=\Big[(x-1)e^x\Big]_0^2=e^2+1$",
       r"$\displaystyle\int_C=\frac{3\pi}{2}-(e^2+1)$"],
  check=_c)


def _c():
    P_, Q_ = y**3/3 - 2*y, 2*x - x**3/3
    curl = simplify(diff(Q_, x) - diff(P_, y))
    assert simplify(curl - (4 - x**2 - y**2)) == 0
    assert EQ(integrate((4 - r**2)*r, (r, 0, 2), (th, 0, 2*pi)), 8*pi)
    assert EQ(line_int([P_, Q_], [2*cos(t), 2*sin(t)], 0, 2*pi, (x, y)), 8*pi)
    assert float(integrate((4 - r**2)*r, (r, 0, 1), (th, 0, 2*pi))) < float(8*pi)
P(id="4-114", ch=16, sec="16.4", type="16-green", src="교재 16.4 심화형 (선적분을 최대로 하는 곡선)",
  q=r"양의 방향을 갖는 단순 닫힌 곡선 $C$ 중에서 $\displaystyle\oint_C\Big(\frac{y^3}{3}-2y\Big)dx+\Big(2x-\frac{x^3}{3}\Big)dy$의 값을 최대로 하는 $C$와 그 최댓값을 구하라.",
  hint=r"그린 정리로 $\oint_C=\iint_D(4-x^2-y^2)\,dA$. 피적분함수가 양수인 곳만 모두 포함하고 음수인 곳은 빼야 최대예요.",
  ans=r"$C$: 원 $x^2+y^2=4$ (반시계), 최댓값 $8\pi$",
  sol=[r"$Q_x-P_y=(2-x^2)-(y^2-2)=4-x^2-y^2$ → $\displaystyle\oint_C=\iint_D(4-x^2-y^2)\,dA$",
       r"$4-x^2-y^2>0 \iff x^2+y^2<4$ → $D$가 정확히 원판 $x^2+y^2\le4$일 때 최대",
       r"최댓값 $=\displaystyle\int_0^{2\pi}\!\!\int_0^2(4-r^2)\,r\,dr\,d\theta=2\pi(8-4)=8\pi$"],
  check=_c)


def _c():
    tp = symbols('tp', positive=True)
    X = 3*tp/(1 + tp**3); Y = 3*tp**2/(1 + tp**3)
    assert simplify(X**3 + Y**3 - 3*X*Y) == 0
    integrand = simplify(X*diff(Y, tp) - Y*diff(X, tp))
    assert simplify(integrand - X**2) == 0
    assert EQ(R(1, 2)*integrate(9*tp**2/(1 + tp**3)**2, (tp, 0, oo)), R(3, 2))
P(id="4-115", ch=16, sec="16.4", type="16-greenarea", src="교재 16.4 심화형 (데카르트 엽선)",
  q=r"데카르트 엽선 $x^3+y^3=3xy$의 고리 부분은 $x=\dfrac{3t}{1+t^3},\ y=\dfrac{3t^2}{1+t^3}\ (0\le t<\infty)$로 매개화된다. 그린 정리의 넓이 공식으로 고리로 둘러싸인 영역의 넓이를 구하라.",
  hint=r"$y=tx$이므로 $x\,dy-y\,dx=x^2\,d\!\left(\tfrac yx\right)=x^2\,dt$. $A=\tfrac12\oint x\,dy-y\,dx$.",
  ans=r"$\dfrac32$",
  sol=[r"$t$가 $0\to\infty$일 때 원점에서 출발해 $(\tfrac32,\tfrac32)$를 지나 다시 원점으로 (반시계 방향)",
       r"$\dfrac yx=t$ → $x\,dy-y\,dx=x^2\,d\!\left(\dfrac yx\right)=x^2\,dt=\dfrac{9t^2}{(1+t^3)^2}dt$",
       r"$A=\dfrac12\displaystyle\int_0^\infty\frac{9t^2}{(1+t^3)^2}dt=\frac12\Big[-\frac{3}{1+t^3}\Big]_0^\infty=\frac12\cdot3=\frac32$"],
  check=_c)


def _c():
    X, Y = t - sin(t), 1 - cos(t)
    A = -(-integrate(Y*diff(X, t), (t, 0, 2*pi)))   # A = -∮y dx, 아치는 t: 2π→0
    assert EQ(A, 3*pi)
    ix2dy = -integrate(X**2*diff(Y, t), (t, 0, 2*pi))
    iy2dx = -integrate(Y**2*diff(X, t), (t, 0, 2*pi))
    assert EQ(ix2dy, 6*pi**2) and EQ(iy2dx, -5*pi)
    assert EQ(ix2dy/(2*A), pi) and EQ(-iy2dx/(2*A), R(5, 6))
P(id="4-116", ch=16, sec="16.4", type="16-greenarea", src="교재 16.4 심화형 (그린 정리로 무게중심)",
  q=r"(a) 그린 정리를 이용해, 양의 방향 경계 $C$를 갖는 영역 $D$의 무게중심이 $\bar x=\dfrac{1}{2A}\displaystyle\oint_Cx^2\,dy,\ \ \bar y=-\dfrac{1}{2A}\oint_Cy^2\,dx$임을 보여라. ($A$는 $D$의 넓이)<br>(b) 사이클로이드 $x=t-\sin t,\ y=1-\cos t\ (0\le t\le2\pi)$의 한 아치와 $x$축으로 둘러싸인 영역의 무게중심을 구하라.",
  hint=r"(a) $\oint x^2dy$에서 $P=0,\ Q=x^2$ → $\iint2x\,dA$. (b) 양의 방향 = $x$축을 왼→오, 아치는 $t$: $2\pi\to0$. $x$축 위에서는 $y=0$, $dy=0$이라 기여 $0$.",
  ans=r"(b) $\Big(\pi,\ \dfrac56\Big)$ (넓이 $3\pi$)",
  sol=[r"(a) $\displaystyle\oint_Cx^2dy=\iint_D2x\,dA$, $\displaystyle\oint_Cy^2dx=\iint_D(-2y)\,dA$ → $\bar x=\dfrac{\iint x\,dA}{A}=\dfrac{1}{2A}\oint x^2dy$, $\bar y=-\dfrac{1}{2A}\oint y^2dx$",
       r"(b) 넓이 $A=-\displaystyle\oint y\,dx=\int_0^{2\pi}(1-\cos t)^2dt=3\pi$ ($x$축 위 기여 $0$, 아치는 역방향)",
       r"$\displaystyle\oint y^2dx=-\int_0^{2\pi}(1-\cos t)^3dt=-5\pi$ → $\bar y=-\dfrac{-5\pi}{6\pi}=\dfrac56$",
       r"$\displaystyle\oint x^2dy=-\int_0^{2\pi}(t-\sin t)^2\sin t\,dt=6\pi^2$ → $\bar x=\dfrac{6\pi^2}{6\pi}=\pi$ (대칭으로도 바로 $\pi$)"],
  check=_c)


def _c():
    P_, Q_ = (2*x - y)/(x**2 + y**2), (x + 2*y)/(x**2 + y**2)
    assert simplify(P_ - (diff(log(x**2 + y**2), x) - y/(x**2 + y**2))) == 0
    assert simplify(Q_ - (diff(log(x**2 + y**2), y) + x/(x**2 + y**2))) == 0
    num = line_num([P_, Q_], [t, t**2 - 2], -2, 2, (x, y), pts=[-2, -sqrt(2), 0, sqrt(2), 2])
    assert abs(num - 3*mp.pi/2) < 1e-10
P(id="4-117", ch=16, sec="16.4", type="16-singular", src="2024 기말 4번 유형",
  q=r"$\mathbf F(x,y)=\dfrac{2x-y}{x^2+y^2}\,\mathbf i+\dfrac{x+2y}{x^2+y^2}\,\mathbf j$이고 $C:\ \mathbf r(t)=t\,\mathbf i+(t^2-2)\,\mathbf j\ (-2\le t\le2)$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"$\mathbf F=\nabla\ln(x^2+y^2)+\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$. 둘째 부분의 적분은 원점에 대한 각 $\theta$의 총 변화량이에요. $C$는 원점 아래 $(0,-2)$를 지나요.",
  ans=r"$\dfrac{3\pi}{2}$",
  sol=[r"$\nabla\ln(x^2+y^2)=\dfrac{\langle2x,2y\rangle}{x^2+y^2}$ → $\mathbf F=\nabla\ln(x^2+y^2)+\dfrac{\langle-y,x\rangle}{x^2+y^2}$",
       r"시작 $(-2,2)$, 끝 $(2,2)$: $x^2+y^2$가 둘 다 $8$ → 첫 부분의 적분 $=\ln8-\ln8=0$",
       r"둘째 부분 $=\int d\theta$: $(-2,2)$ ($\theta=\tfrac{3\pi}4$) → $(-\sqrt2,0)$ ($\pi$) → $(0,-2)$ ($\tfrac{3\pi}2$) → $(\sqrt2,0)$ ($2\pi$) → $(2,2)$ ($\tfrac{9\pi}4$)",
       r"$\Delta\theta=\dfrac{9\pi}{4}-\dfrac{3\pi}{4}=\dfrac{3\pi}{2}$ (원점 아래로 돌아가며 반시계 방향으로 $\tfrac34$바퀴)"],
  check=_c)


def _c():
    P_, Q_ = -y/(x**2 + 4*y**2), x/(x**2 + 4*y**2)
    assert simplify(diff(P_, y) - diff(Q_, x)) == 0
    assert EQ(line_int([P_, Q_], [2*cos(t), sin(t)], 0, 2*pi, (x, y)), pi)
    num = line_num([P_, Q_], [3*cos(t), 3*sin(t)], 0, 2*pi, (x, y))
    assert abs(num - mp.pi) < 1e-10
P(id="4-118", ch=16, sec="16.4", type="16-singular", src="교재 16.4 심화형 (적분하기 쉬운 곡선으로 바꾸기)",
  q=r"$\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+4y^2}$에 대해<br>(a) 원점을 제외한 곳에서 $Q_x=P_y$임을 보여라.  (b) 타원 $x^2+4y^2=4$ (반시계)를 따라 $\displaystyle\oint\mathbf F\cdot d\mathbf r$를 구하라.  (c) 원 $x^2+y^2=9$ (반시계)를 따라 $\displaystyle\oint\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"(b) $x=2\cos t,\ y=\sin t$이면 분모가 상수 $4$. (c) 원 위에서 직접 하면 어렵지만, 원과 타원 사이 영역(원점 제외)에서 그린 정리를 쓰면 $\oint_{\text{원}}=\oint_{\text{타원}}$.",
  ans=r"(a) $Q_x=P_y=\dfrac{4y^2-x^2}{(x^2+4y^2)^2}$  (b) $\pi$  (c) $\pi$",
  sol=[r"(a) $P_y=\dfrac{-(x^2+4y^2)+8y^2}{(x^2+4y^2)^2}=\dfrac{4y^2-x^2}{(x^2+4y^2)^2}$, $Q_x=\dfrac{(x^2+4y^2)-2x^2}{(x^2+4y^2)^2}=\dfrac{4y^2-x^2}{(x^2+4y^2)^2}$",
       r"(b) $x=2\cos t,\ y=\sin t$: $\mathbf F\cdot\mathbf r'=\dfrac{-\sin t(-2\sin t)+2\cos t\cos t}{4}=\dfrac12$ → $\displaystyle\int_0^{2\pi}\frac12dt=\pi$",
       r"(c) 타원은 원 안에 있고, 그 사이 영역 $D$에는 원점이 없음 → $\displaystyle\oint_{\text{원}}-\oint_{\text{타원}}=\iint_D(Q_x-P_y)\,dA=0$",
       r"따라서 원을 따른 값도 $\pi$"],
  check=_c)


def _c():
    cc = (3 - 2*pi)/(2*pi)
    P_ = -y + cc*(-y)/(x**2 + y**2); Q_ = x + cc*x/(x**2 + y**2)
    assert simplify(diff(Q_, x) - diff(P_, y) - 2) == 0
    assert EQ(line_int([P_, Q_], [cos(t), sin(t)], 0, 2*pi, (x, y)), 3)
    sq = 0
    for p0, p1 in [((-2, -2), (2, -2)), ((2, -2), (2, 2)), ((2, 2), (-2, 2)), ((-2, 2), (-2, -2))]:
        sq += line_num([P_, Q_], seg(p0, p1), 0, 1, (x, y))
    assert abs(sq - (35 - 2*mp.pi)) < 1e-9
    off = line_num([P_, Q_], [3 + cos(t), sin(t)], 0, 2*pi, (x, y))
    assert abs(off - 2*mp.pi) < 1e-9
    cw = line_num([P_, Q_], [2*cos(t), -2*sin(t)], 0, 2*pi, (x, y))
    assert abs(cw - (-3 - 6*mp.pi)) < 1e-9
P(id="4-119", ch=16, sec="16.4", type="16-green", src="교재 16.4 심화형 (특이점이 있는 영역의 그린 정리)",
  q=r"벡터장 $\mathbf F=\langle P,Q\rangle$는 원점을 제외한 평면에서 연속인 편도함수를 갖고 $Q_x-P_y=2$이다. 또 단위원 (반시계)을 따라 $\displaystyle\oint\mathbf F\cdot d\mathbf r=3$이다. 다음 (양의 방향은 반시계) 선적분을 구하라.<br>(a) 정사각형 $|x|\le2,\ |y|\le2$의 경계 (반시계)  (b) 원 $(x-3)^2+y^2=1$ (반시계)  (c) 원 $x^2+y^2=4$ (시계 방향)",
  hint=r"원점을 감싸는 곡선: (그 곡선) − (단위원) $=\iint_{\text{사이}}2\,dA$. 원점을 감싸지 않는 곡선은 그린 정리를 바로 적용.",
  ans=r"(a) $35-2\pi$  (b) $2\pi$  (c) $-3-6\pi$",
  sol=[r"(a) 정사각형과 단위원 사이 영역의 넓이 $16-\pi$ → $\displaystyle\oint_{\square}=3+2(16-\pi)=35-2\pi$",
       r"(b) 원판 $(x-3)^2+y^2\le1$에는 원점이 없음 → $\displaystyle\iint2\,dA=2\pi$",
       r"(c) 반시계 방향이면 $3+2(4\pi-\pi)=3+6\pi$ → 시계 방향은 부호 반대: $-3-6\pi$"],
  check=_c)


def _c():
    P_, Q_ = -x**2*y, x*y**2 + x
    assert simplify(diff(Q_, x) - diff(P_, y) - (x**2 + y**2 + 1)) == 0
    I = integrate((r**2 + 1)*r, (r, 0, 2*cos(th)), (th, -pi/2, pi/2))
    assert EQ(I, 5*pi/2)
    assert EQ(line_int([P_, Q_], [1 + cos(t), sin(t)], 0, 2*pi, (x, y)), 5*pi/2)
P(id="4-120", ch=16, sec="16.4", type="16-green", src="2024 기말 1(a) 유형 (그린 정리 + 극좌표)",
  q=r"입자가 원 $(x-1)^2+y^2=1$을 반시계 방향으로 한 바퀴 돌 때 힘 $\mathbf F(x,y)=\big\langle-x^2y,\ xy^2+x\big\rangle$가 한 일을 그린 정리로 구하라.",
  hint=r"$Q_x-P_y=y^2+1+x^2$. 원판 $(x-1)^2+y^2\le1$은 극좌표로 $r\le2\cos\theta,\ -\tfrac\pi2\le\theta\le\tfrac\pi2$.",
  ans=r"$\dfrac{5\pi}{2}$",
  sol=[r"$Q_x-P_y=(y^2+1)-(-x^2)=x^2+y^2+1$",
       r"$W=\displaystyle\iint_D(r^2+1)\,dA=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}(r^3+r)\,dr\,d\theta=\int_{-\pi/2}^{\pi/2}\big(4\cos^4\theta+2\cos^2\theta\big)d\theta$",
       r"$=4\cdot\dfrac{3\pi}{8}+2\cdot\dfrac\pi2=\dfrac{3\pi}{2}+\pi=\dfrac{5\pi}{2}$"],
  check=_c)

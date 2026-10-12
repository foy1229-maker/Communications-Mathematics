"""4단계 · 심화 (30문제) — 복습문제(심화)·실전형"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    # 일반 항등식: proj_a b × proj_b a = (a·b)^2/(|a|^2|b|^2) (a×b)
    a1, a2, a3, b1, b2, b3 = symbols('a1 a2 a3 b1 b2 b3', real=True)
    A = Matrix([a1, a2, a3]); B = Matrix([b1, b2, b3])
    lhs = (A.dot(B) / A.dot(A) * A).cross(A.dot(B) / B.dot(B) * B)
    rhs = A.dot(B)**2 / (A.dot(A) * B.dot(B)) * A.cross(B)
    assert all(simplify(p - q) == 0 for p, q in zip(lhs, rhs))
    # 조건을 만족하는 구체적인 예로 수치 확인
    A0 = Matrix([2, 1, 0]); B0 = Matrix([R(4, 5), R(7, 5), 1])
    assert A0.dot(B0) == 3 and EQ(A0.cross(B0), [1, -2, 2])
    assert EQ(A0.dot(A0) * B0.dot(B0), 18)
    assert EQ(acos(A0.dot(B0) / sqrt(18)), pi/4)
    assert EQ((A0.dot(B0) / A0.dot(A0) * A0).cross(A0.dot(B0) / B0.dot(B0) * B0), [R(1, 2), -1, 1])
P(id="4-01", ch=12, sec="12.4", type="12-identity", src="복습 12장 심화1 유형",
  q=r"두 벡터가 $\mathbf a\cdot\mathbf b=3$, $\mathbf a\times\mathbf b=\langle 1,-2,2\rangle$를 만족할 때 다음을 구하라.<br>(a) $|\mathbf a|^2|\mathbf b|^2$  (b) 두 벡터 사이의 각 $\theta$  (c) $\operatorname{proj}_{\mathbf a}\mathbf b\times\operatorname{proj}_{\mathbf b}\mathbf a$",
  hint=r"$|\mathbf a\times\mathbf b|^2+(\mathbf a\cdot\mathbf b)^2=|\mathbf a|^2|\mathbf b|^2(\sin^2\theta+\cos^2\theta)$. (c)는 두 사영이 각각 $\mathbf a$, $\mathbf b$의 스칼라배라는 점을 이용해요.",
  ans=r"(a) $18$  (b) $\theta=\dfrac{\pi}{4}$  (c) $\left\langle\tfrac12,\,-1,\,1\right\rangle$",
  sol=[r"(a) $|\mathbf a\times\mathbf b|^2=1+4+4=9$ 이므로 $|\mathbf a|^2|\mathbf b|^2=9+3^2=18$",
       r"(b) $\tan\theta=\dfrac{|\mathbf a\times\mathbf b|}{\mathbf a\cdot\mathbf b}=\dfrac33=1 \Rightarrow \theta=\dfrac\pi4$",
       r"(c) $\operatorname{proj}_{\mathbf a}\mathbf b=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\mathbf a,\ \ \operatorname{proj}_{\mathbf b}\mathbf a=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|^2}\mathbf b$",
       r"외적: $\dfrac{(\mathbf a\cdot\mathbf b)^2}{|\mathbf a|^2|\mathbf b|^2}\,(\mathbf a\times\mathbf b)=\dfrac{9}{18}\langle1,-2,2\rangle=\left\langle\tfrac12,-1,1\right\rangle$"],
  check=_c)


def _c():
    v1, v2 = Matrix([1, -1, 2]), Matrix([2, 1, 1])
    n = v1.cross(v2); P1, P2 = Matrix([1, 2, 3]), Matrix([0, 1, -1])
    assert EQ(n, [-3, 3, 3])
    sol = solve([1 + t - 2*s, 2 - t - 1 - s], [t, s])
    assert sol == {t: R(1, 3), s: R(2, 3)} and (3 + 2*sol[t]) != (-1 + sol[s])
    assert EQ(abs(n.dot(P2 - P1)) / n.norm(), 4*sqrt(3) / 3)
P(id="4-02", ch=12, sec="12.5", type="12-dist", src="강의 12.5 거리 공식 확장 (꼬인 직선)",
  q=r"두 직선 $L_1:\ x=1+t,\ y=2-t,\ z=3+2t$ 와 $L_2:\ x=2s,\ y=1+s,\ z=-1+s$가 꼬인 위치에 있음을 보이고, 두 직선 사이의 (최단) 거리를 구하라.",
  hint=r"$\mathbf n=\mathbf v_1\times\mathbf v_2$는 두 직선에 모두 수직. 두 직선 위의 점을 잇는 벡터를 $\mathbf n$ 방향으로 사영한 길이가 거리예요.",
  ans=r"꼬인 위치,  거리 $\dfrac{4\sqrt3}{3}$",
  sol=[r"방향 $\mathbf v_1=\langle1,-1,2\rangle,\ \mathbf v_2=\langle2,1,1\rangle$ → 평행 아님",
       r"$x,y$에서 $1+t=2s,\ 2-t=1+s \Rightarrow s=\tfrac23,\ t=\tfrac13$; 이때 $z$는 $\tfrac{11}{3}\ne-\tfrac13$ → 만나지 않음 → 꼬인 위치",
       r"$\mathbf n=\mathbf v_1\times\mathbf v_2=\langle-3,3,3\rangle$,  $P_1=(1,2,3),\ P_2=(0,1,-1)$,  $\overrightarrow{P_1P_2}=\langle-1,-1,-4\rangle$",
       r"$d=\dfrac{|\mathbf n\cdot\overrightarrow{P_1P_2}|}{|\mathbf n|}=\dfrac{|3-3-12|}{3\sqrt3}=\dfrac{4}{\sqrt3}=\dfrac{4\sqrt3}{3}$"],
  check=_c)


def _c():
    P0 = Matrix([1, 0, 3]); vv = Matrix([2, -1, 1]); Q = Matrix([2, 1, 0])
    n = vv.cross(Q - P0)
    assert EQ(n, [2, 7, 3])
    for tt in (0, 1, -2):
        pt = P0 + tt*vv
        assert 2*pt[0] + 7*pt[1] + 3*pt[2] == 11
    assert 2*2 + 7*1 + 3*0 == 11
P(id="4-03", ch=12, sec="12.5", type="12-plane", src="강의 12.5 ex5 확장",
  q=r"직선 $x=1+2t,\ y=-t,\ z=3+t$를 포함하고 점 $(2,1,0)$을 지나는 평면의 방정식을 구하라.",
  hint=r"평면 위의 두 벡터: 직선의 방향벡터, 그리고 직선 위의 점에서 $(2,1,0)$으로 가는 벡터.",
  ans=r"$2x+7y+3z=11$",
  sol=[r"직선 위의 점 $P_0=(1,0,3)$, 방향 $\mathbf v=\langle2,-1,1\rangle$, $\overrightarrow{P_0Q}=\langle1,1,-3\rangle$",
       r"$\mathbf n=\mathbf v\times\overrightarrow{P_0Q}=\langle 3-1,\ 1+6,\ 2+1\rangle=\langle2,7,3\rangle$",
       r"$2(x-1)+7y+3(z-3)=0 \Rightarrow 2x+7y+3z=11$ (검산: $(2,1,0)$ → $4+7=11$ ✓)"],
  check=_c)


def _c():
    Pp = Matrix([4, 3, 3]); n = Matrix([1, 2, 2])
    tt = solve((Pp + t*n).dot(n) - 7, t)[0]
    H = Pp + tt*n
    assert tt == -1 and EQ(H, [3, 1, 1]) and EQ((H - Pp).norm(), 3) and EQ(Pp + 2*tt*n, [2, -1, -1])
P(id="4-04", ch=12, sec="12.5", type="12-dist", src="강의 12.5 ex8 확장 (수선의 발)",
  q=r"점 $P(4,3,3)$에서 평면 $x+2y+2z=7$에 내린 수선의 발 $H$, 점 $P$와 평면 사이의 거리, 평면에 대한 $P$의 대칭점 $P'$을 구하라.",
  hint=r"$P$를 지나고 법선 $\mathbf n=\langle1,2,2\rangle$ 방향인 직선 $P+t\mathbf n$을 평면에 대입해요.",
  ans=r"$H(3,1,1)$,  거리 $3$,  $P'(2,-1,-1)$",
  sol=[r"직선 $(4+t,\ 3+2t,\ 3+2t)$를 평면에 대입: $4+t+6+4t+6+4t=7 \Rightarrow 16+9t=7 \Rightarrow t=-1$",
       r"$H=(3,1,1)$,  거리 $=|t|\,|\mathbf n|=1\cdot3=3$ (공식 $\tfrac{|4+6+6-7|}{3}=3$과 일치)",
       r"대칭점: $t=-2$ → $P'=(2,-1,-1)$"],
  check=_c)


def _c():
    A, B, C, D = Matrix([1, 0, 0]), Matrix([0, 2, 0]), Matrix([0, 0, 3]), Matrix([1, 1, 1])
    vol = abs((B - A).dot((C - A).cross(D - A))) / 6
    assert EQ(vol, R(5, 6))
P(id="4-05", ch=12, sec="12.4", type="12-triple", src="강의 12.4 ex5 확장",
  q=r"네 점 $A(1,0,0)$, $B(0,2,0)$, $C(0,0,3)$, $D(1,1,1)$을 꼭짓점으로 하는 사면체의 부피를 구하라.",
  hint=r"사면체 부피 $=\dfrac16\,\big|\overrightarrow{AB}\cdot(\overrightarrow{AC}\times\overrightarrow{AD})\big|$",
  ans=r"$\dfrac56$",
  sol=[r"$\overrightarrow{AB}=\langle-1,2,0\rangle,\ \overrightarrow{AC}=\langle-1,0,3\rangle,\ \overrightarrow{AD}=\langle0,1,1\rangle$",
       r"$\overrightarrow{AC}\times\overrightarrow{AD}=\langle0-3,\ 0+1,\ -1-0\rangle=\langle-3,1,-1\rangle$",
       r"$\overrightarrow{AB}\cdot\langle-3,1,-1\rangle=3+2+0=5 \Rightarrow V=\dfrac56$"],
  check=_c)


def _c():
    n1, n2 = Matrix([1, 1, 1]), Matrix([1, -1, 1])
    vv = n1.cross(n2)
    assert EQ(vv, [2, 0, -2])
    pt = solve([x + y - 3, x - y - 1], [x, y]); P0 = Matrix([pt[x], pt[y], 0])
    assert EQ(P0, [2, 1, 0])
    assert EQ(P0.cross(vv).norm() / vv.norm(), sqrt(3))
P(id="4-06", ch=12, sec="12.5", type="12-line", src="강의 12.5 ex7 + 점과 직선 사이 거리 종합",
  q=r"두 평면 $x+y+z=3$, $x-y+z=1$의 교선 $L$의 대칭방정식을 구하고, 원점에서 $L$까지의 거리를 구하라.",
  hint=r"방향 $\mathbf n_1\times\mathbf n_2$에 $0$인 성분이 있으면 대칭방정식은 그 좌표를 따로 써요 (강의 12.5 참고).",
  ans=r"$x-2=\dfrac{z}{-1},\ \ y=1$  (즉 $x-2=-z,\ y=1$),  거리 $\sqrt3$",
  sol=[r"$\mathbf n_1\times\mathbf n_2=\langle1\cdot1-1\cdot(-1),\ 1\cdot1-1\cdot1,\ 1\cdot(-1)-1\cdot1\rangle=\langle2,0,-2\rangle\parallel\langle1,0,-1\rangle$",
       r"$z=0$: $x+y=3,\ x-y=1 \Rightarrow (2,1,0)$",
       r"대칭방정식: $\dfrac{x-2}{1}=\dfrac{z}{-1},\ y=1$",
       r"$\overrightarrow{OP}=\langle2,1,0\rangle$,  $\overrightarrow{OP}\times\langle1,0,-1\rangle=\langle-1,2,-1\rangle$",
       r"$d=\dfrac{\sqrt6}{\sqrt2}=\sqrt3$"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    r1 = Matrix([1 + 2*t, 1 - t**2, 2 + t + t**2]); r2 = Matrix([s**2, 2*s - 1, 1 + s**3])
    assert EQ(r1.subs(t, 0), [1, 1, 2]) and EQ(r2.subs(s, 1), [1, 1, 2])
    n = r1.diff(t).subs(t, 0).cross(r2.diff(s).subs(s, 1))
    assert EQ(n, [-2, -4, 4])
    assert 1 + 2*1 - 2*2 == -1
P(id="4-07", ch=13, sec="13.2", type="13-tplane", src="복습 13장 심화1 유형",
  q=r"곡면 $S$ 위에 두 곡선 $\mathbf r_1(t)=\langle 1+2t,\ 1-t^2,\ 2+t+t^2\rangle$, $\mathbf r_2(s)=\langle s^2,\ 2s-1,\ 1+s^3\rangle$이 놓여 있고, 둘 다 점 $P(1,1,2)$를 지난다. $P$에서 $S$의 접평면의 방정식을 구하라.",
  hint=r"두 곡선의 접벡터는 모두 접평면 안에 있어요 → 법선 $=\mathbf r_1'\times\mathbf r_2'$",
  ans=r"$x+2y-2z=-1$",
  sol=[r"$P$에 대응: $\mathbf r_1$은 $t=0$, $\mathbf r_2$는 $s=1$",
       r"$\mathbf r_1'(0)=\langle2,0,1\rangle$,  $\mathbf r_2'(1)=\langle2s,2,3s^2\rangle\big|_{s=1}=\langle2,2,3\rangle$",
       r"$\mathbf n=\langle2,0,1\rangle\times\langle2,2,3\rangle=\langle0-2,\ 2-6,\ 4-0\rangle=\langle-2,-4,4\rangle\parallel\langle1,2,-2\rangle$",
       r"$(x-1)+2(y-1)-2(z-2)=0 \Rightarrow x+2y-2z=-1$"],
  check=_c)


def _c():
    rs = Matrix([3*cos(s/5), 3*sin(s/5), 4*s/5])
    assert EQ(simplify(rs.diff(s).norm()), 1)
    assert EQ(rs.subs(s, 5*pi), [-3, 0, 4*pi])
P(id="4-08", ch=13, sec="13.3", type="13-arcfn", src="과제 13.3 #15 · #17 종합",
  q=r"나선 $\mathbf r(t)=\langle 3\cos t,\ 3\sin t,\ 4t\rangle$을 점 $(3,0,0)$에서 시작하는 호의 길이 $s$로 재매개화하고, 곡선을 따라 $5\pi$만큼 이동한 점을 구하라. 또한 재매개화된 곡선에서 $\left|\tfrac{d\mathbf r}{ds}\right|=1$임을 확인하라.",
  hint=r"$|\mathbf r'(t)|=5$ 이므로 $s=5t$",
  ans=r"$\mathbf r(s)=\left\langle 3\cos\tfrac s5,\ 3\sin\tfrac s5,\ \tfrac{4s}{5}\right\rangle$,  도착점 $(-3,\ 0,\ 4\pi)$",
  sol=[r"$(3,0,0)$은 $t=0$, $|\mathbf r'(t)|=\sqrt{9+16}=5 \Rightarrow s=5t,\ t=\tfrac s5$",
       r"$\mathbf r(s)=\left\langle3\cos\tfrac s5,\ 3\sin\tfrac s5,\ \tfrac{4s}{5}\right\rangle$",
       r"$\dfrac{d\mathbf r}{ds}=\left\langle-\tfrac35\sin\tfrac s5,\ \tfrac35\cos\tfrac s5,\ \tfrac45\right\rangle$, 크기 $\sqrt{\tfrac{9}{25}+\tfrac{16}{25}}=1$ ✓",
       r"$s=5\pi$ → $(3\cos\pi,\ 3\sin\pi,\ 4\pi)=(-3,0,4\pi)$"],
  check=_c)


def _c():
    rr = Matrix([2*cos(t), 2*sin(t), 4*sin(t)*cos(t)])
    assert EQ(rr[0]**2 + rr[1]**2, 4) and EQ(rr[2], rr[0]*rr[1])
    assert EQ(rr.subs(t, pi/4), [sqrt(2), sqrt(2), 2])
    assert EQ(rr.diff(t).subs(t, pi/4), [-sqrt(2), sqrt(2), 0])
P(id="4-09", ch=13, sec="13.2", type="13-curve", src="복습 13장 기초1 + 과제 13.2 #27 종합",
  q=r"원기둥 $x^2+y^2=4$와 곡면 $z=xy$의 교선을 벡터함수로 나타내고, 점 $(\sqrt2,\sqrt2,2)$에서 교선의 접선의 매개방정식을 구하라.",
  hint=r"$x=2\cos t,\ y=2\sin t$로 두면 $z=xy=2\sin2t$. 주어진 점은 $t=\tfrac\pi4$.",
  ans=r"$\mathbf r(t)=\langle2\cos t,\ 2\sin t,\ 2\sin2t\rangle$,  접선 $x=\sqrt2-u,\ y=\sqrt2+u,\ z=2$",
  sol=[r"$\mathbf r(t)=\langle 2\cos t,\ 2\sin t,\ 4\sin t\cos t\rangle=\langle2\cos t,\ 2\sin t,\ 2\sin2t\rangle$",
       r"$t=\tfrac\pi4$에서 $(\sqrt2,\sqrt2,2)$",
       r"$\mathbf r'(t)=\langle-2\sin t,\ 2\cos t,\ 4\cos2t\rangle \Rightarrow \mathbf r'\!\left(\tfrac\pi4\right)=\langle-\sqrt2,\sqrt2,0\rangle\parallel\langle-1,1,0\rangle$",
       r"접선: $x=\sqrt2-u,\ y=\sqrt2+u,\ z=2$"],
  check=_c)


def _c():
    rr = Matrix([t, t**2, t**3]); n = Matrix([1, -2, 1])
    ts = solve(rr.diff(t).dot(n), t)
    assert sorted(ts) == [R(1, 3), 1]
    for tt in ts:
        pt = rr.subs(t, tt)
        assert pt[0] - 2*pt[1] + pt[2] != 4
P(id="4-10", ch=13, sec="13.2", type="13-deriv", src="강의 13.1 ex7 (꼬인 3차 곡선) 확장",
  q=r"꼬인 3차 곡선 $\mathbf r(t)=\langle t,\ t^2,\ t^3\rangle$ 위에서 접선이 평면 $x-2y+z=4$와 평행한 점을 모두 구하라.",
  hint=r"접선이 평면과 평행 ⇔ 접벡터 $\mathbf r'(t)$가 평면의 법선 $\mathbf n$과 수직: $\mathbf r'(t)\cdot\mathbf n=0$",
  ans=r"$\left(\tfrac13,\ \tfrac19,\ \tfrac1{27}\right)$,  $(1,1,1)$",
  sol=[r"$\mathbf r'(t)=\langle1,2t,3t^2\rangle$,  $\mathbf n=\langle1,-2,1\rangle$",
       r"$\mathbf r'(t)\cdot\mathbf n=1-4t+3t^2=(3t-1)(t-1)=0 \Rightarrow t=\tfrac13,\ 1$",
       r"점: $\left(\tfrac13,\tfrac19,\tfrac1{27}\right)$, $(1,1,1)$ (두 점 모두 평면 위에 있지 않으므로 접선은 평면과 평행)"],
  check=_c)


# ───────── Ch.14 ─────────
def _c():
    f = (x*y + 4) / (x**2 - y**2)
    assert EQ(limit(f.subs(x, 2), y, -2), R(1, 2))
    assert EQ(limit(f.subs(y, -2), x, 2), R(-1, 2))
P(id="4-11", ch=14, sec="14.2", type="14-dne", src="복습 14.1–3 심화2 유형",
  q=r"$\displaystyle\lim_{(x,y)\to(2,-2)}\frac{xy+4}{x^2-y^2}$가 존재하지 않음을 보여라.",
  hint=r"원점이 아닌 점에서는 그 점을 지나는 직선 $x=2$, $y=-2$를 경로로 써 보세요.",
  ans=r"$x=2$를 따라 $\tfrac12$, $y=-2$를 따라 $-\tfrac12$ → 존재하지 않는다.",
  sol=[r"$x=2$ 고정: $\dfrac{2y+4}{4-y^2}=\dfrac{2(y+2)}{(2-y)(2+y)}=\dfrac{2}{2-y}\to\dfrac24=\dfrac12$",
       r"$y=-2$ 고정: $\dfrac{-2x+4}{x^2-4}=\dfrac{-2(x-2)}{(x-2)(x+2)}=\dfrac{-2}{x+2}\to-\dfrac12$",
       r"두 경로의 극한이 다르므로 극한은 존재하지 않는다."],
  check=_c)


def _c():
    X = r**2 - s**2; Y = 2*r*s
    tests = [x**3*y**2 + sin(x)*y, exp(x*y) + x*y**3, cos(x + 2*y) + x**4]
    for f in tests:
        Z = f.subs({x: X, y: Y}, simultaneous=True)
        lhs = diff(Z, r, s)
        fx, fy = diff(f, x), diff(f, y)
        fxx, fxy, fyy = diff(f, x, 2), diff(f, x, y), diff(f, y, 2)
        rhs = (2*fy - 4*r*s*fxx + 4*(r**2 - s**2)*fxy + 4*r*s*fyy).subs({x: X, y: Y}, simultaneous=True)
        assert simplify(lhs - rhs) == 0
P(id="4-12", ch=14, sec="14.5", type="14-chain2", src="복습 14.4–6 기초1 유형 (2계 연쇄법칙)",
  q=r"$z=f(x,y)$이고 $x=r^2-s^2$, $y=2rs$일 때 $\dfrac{\partial^2 z}{\partial r\,\partial s}$를 $z_x,\ z_y,\ z_{xx},\ z_{xy},\ z_{yy}$로 나타내라. (2계 편도함수는 연속)",
  hint=r"$z_s=-2s\,z_x+2r\,z_y$를 $r$로 미분할 때, $z_x,\ z_y$도 $(x,y)$를 거쳐 $r$에 의존하므로 다시 연쇄법칙을 써요.",
  ans=r"$\dfrac{\partial^2 z}{\partial r\,\partial s}=2z_y-4rs\,z_{xx}+4(r^2-s^2)\,z_{xy}+4rs\,z_{yy}$",
  sol=[r"$x_r=2r,\ x_s=-2s,\ y_r=2s,\ y_s=2r$ → $z_s=-2s\,z_x+2r\,z_y$",
       r"$\dfrac{\partial}{\partial r}z_x=z_{xx}(2r)+z_{xy}(2s)$,  $\dfrac{\partial}{\partial r}z_y=z_{yx}(2r)+z_{yy}(2s)$",
       r"$\dfrac{\partial}{\partial r}(z_s)=-2s(2r\,z_{xx}+2s\,z_{xy})+2z_y+2r(2r\,z_{xy}+2s\,z_{yy})$",
       r"정리 ($z_{xy}=z_{yx}$): $2z_y-4rs\,z_{xx}+4(r^2-s^2)z_{xy}+4rs\,z_{yy}$"],
  check=_c)


def _c():
    fx_, fy_ = symbols('fx fy')
    sol = solve([R(3, 5)*fx_ + R(4, 5)*fy_ - 2, fy_ + 1], [fx_, fy_])
    assert sol == {fx_: R(14, 3), fy_: -1}
    assert EQ(R(5, 13)*sol[fx_] + R(12, 13)*sol[fy_], R(34, 39))
P(id="4-13", ch=14, sec="14.6", type="14-dir", src="과제 14.6 #41 유형",
  q=r"$f$는 연속인 편도함수를 갖는다. 점 $A(1,1)$에서 $B(4,5)$ 방향의 방향도함수가 $2$이고, $C(1,4)$ 방향의 방향도함수가 $-1$이다. $A$에서 $D(6,13)$ 방향의 방향도함수를 구하라.",
  hint=r"$\nabla f(A)=\langle a,b\rangle$로 두고 두 방향도함수로 연립방정식을 세워요. 방향은 모두 단위벡터로!",
  ans=r"$\dfrac{34}{39}$",
  sol=[r"$\overrightarrow{AB}=\langle3,4\rangle\to\mathbf u_1=\left\langle\tfrac35,\tfrac45\right\rangle$,  $\overrightarrow{AC}=\langle0,3\rangle\to\mathbf u_2=\langle0,1\rangle$",
       r"$\tfrac35a+\tfrac45b=2,\ \ b=-1 \Rightarrow a=\tfrac{14}{3}$",
       r"$\overrightarrow{AD}=\langle5,12\rangle\to\mathbf u_3=\left\langle\tfrac5{13},\tfrac{12}{13}\right\rangle$",
       r"$D_{\mathbf u_3}f=\tfrac{5}{13}\cdot\tfrac{14}{3}-\tfrac{12}{13}=\dfrac{70-36}{39}=\dfrac{34}{39}$"],
  check=_c)


def _c():
    T = 120 / (1 + x**2 + y**2 + 2*z**2)
    g = grad(T, [x, y, z]).subs({x: 1, y: 2, z: -1})
    assert EQ(g, R(15, 4) * Matrix([-1, -2, 2])) and EQ(g.norm(), R(45, 4))
    uu = Matrix([-1, -2, 1]) / sqrt(6)
    assert EQ(g.dot(uu), 35*sqrt(6)/8)
P(id="4-14", ch=14, sec="14.6", type="14-maxrate", src="복습 14.4–6 기초2 유형",
  q=r"공간에서 온도가 $T(x,y,z)=\dfrac{120}{1+x^2+y^2+2z^2}$일 때, 점 $(1,2,-1)$에서<br>(a) 온도가 가장 빨리 증가하는 방향 (b) 그 최대 증가율 (c) 원점을 향하는 방향으로의 온도 변화율을 구하라.",
  hint=r"$\nabla T=\dfrac{-120\langle2x,\ 2y,\ 4z\rangle}{(1+x^2+y^2+2z^2)^2}$",
  ans=r"(a) $\langle-1,-2,2\rangle$ 방향  (b) $\dfrac{45}{4}$  (c) $\dfrac{35\sqrt6}{8}$",
  sol=[r"$(1,2,-1)$에서 분모 $=(1+1+4+2)^2=64$",
       r"$\nabla T=\dfrac{-120}{64}\langle2,4,-4\rangle=\dfrac{15}{4}\langle-1,-2,2\rangle$",
       r"(a) $\nabla T$ 방향, 즉 $\langle-1,-2,2\rangle$  (b) $|\nabla T|=\dfrac{15}{4}\cdot3=\dfrac{45}{4}$",
       r"(c) 원점 방향 $\mathbf u=\dfrac{\langle-1,-2,1\rangle}{\sqrt6}$,  $D_{\mathbf u}T=\dfrac{15}{4}\cdot\dfrac{1+4+2}{\sqrt6}=\dfrac{105}{4\sqrt6}=\dfrac{35\sqrt6}{8}$"],
  check=_c)


def _c():
    S = x*y + 64/x + 64/y
    sol = solve([diff(S, x), diff(S, y)], [x, y], dict=True)
    sol = [c for c in sol if c[x].is_real and c[x] > 0]
    assert sol == [{x: 4, y: 4}]
    D = (diff(S, x, 2)*diff(S, y, 2) - diff(S, x, y)**2).subs(sol[0])
    assert D > 0 and diff(S, x, 2).subs(sol[0]) > 0 and S.subs(sol[0]) == 48
    assert R(32, 16) == 2
P(id="4-15", ch=14, sec="14.7", type="14-optim", src="강의 14.7 ex6 · 복습 14.7–8 기초3 유형",
  q=r"뚜껑이 없는 직육면체 상자의 부피가 $32\,\mathrm m^3$이다. 겉넓이를 최소로 하는 상자의 치수와 그때의 겉넓이를 구하라.",
  hint=r"밑면 $x\times y$, 높이 $z=\dfrac{32}{xy}$ → $S=xy+2xz+2yz=xy+\dfrac{64}{y}+\dfrac{64}{x}$",
  ans=r"가로 $4$, 세로 $4$, 높이 $2$ (m), 최소 겉넓이 $48\,\mathrm m^2$",
  sol=[r"$S(x,y)=xy+\dfrac{64}{x}+\dfrac{64}{y}$  ($x,y>0$)",
       r"$S_x=y-\dfrac{64}{x^2}=0,\ \ S_y=x-\dfrac{64}{y^2}=0 \Rightarrow x^2y=xy^2=64 \Rightarrow x=y=4$",
       r"$D=S_{xx}S_{yy}-S_{xy}^2=2\cdot2-1=3>0,\ S_{xx}=2>0$ → 극소 (물리적으로 최소)",
       r"$z=\dfrac{32}{16}=2$,  $S=16+16+16=48$"],
  check=_c)


def _c():
    f = x**2 + x*y + y**2 - 6*y
    assert solve([diff(f, x), diff(f, y)], [x, y]) == {x: -2, y: 4}
    import itertools
    vals = []
    for a in [i/20 for i in range(-60, 61)]:
        for b in [j/20 for j in range(0, 101)]:
            vals.append(a*a + a*b + b*b - 6*b)
    assert abs(max(vals) - 19) < 1e-9 and abs(min(vals) - (-12)) < 1e-9
P(id="4-16", ch=14, sec="14.7", type="14-absext", src="복습 14.7–8 심화1 유형",
  q=r"$f(x,y)=x^2+xy+y^2-6y$의 직사각형 $D=[-3,3]\times[0,5]$에서의 최댓값과 최솟값을 구하라.",
  hint=r"내부 임계점 1개 + 네 변 각각에서 1변수 최대·최소 (변의 끝점인 꼭짓점도 후보!)",
  ans=r"최댓값 $19$ (점 $(3,5)$),  최솟값 $-12$ (점 $(-2,4)$)",
  sol=[r"내부: $f_x=2x+y=0,\ f_y=x+2y-6=0 \Rightarrow (-2,4)$, $f(-2,4)=4-8+16-24=-12$",
       r"$y=0$: $f=x^2$ → $0\sim9$;  $y=5$: $f=x^2+5x-5$ → 최소 $f(-\tfrac52,5)=-\tfrac{45}{4}$, 끝점 $-11,\ 19$",
       r"$x=-3$: $f=y^2-9y+9$ → 최소 $-\tfrac{45}{4}$ ($y=\tfrac92$), 끝점 $9,\ -11$;  $x=3$: $f=y^2-3y+9$ → $\tfrac{27}{4}\sim19$",
       r"후보 중 최댓값 $19$ ($(3,5)$), 최솟값 $-12$ ($(-2,4)$)"],
  check=_c)


def _c():
    lam = symbols('lam')
    sols = solve([y*z - 2*lam*x, x*z - 4*lam*y, x*y - 6*lam*z, x**2 + 2*y**2 + 3*z**2 - 6], [x, y, z, lam], dict=True)
    vals = [simplify((x*y*z).subs(c)) for c in sols]
    assert EQ(max(vals, key=lambda q: float(q)), 2*sqrt(3)/3) and EQ(min(vals, key=lambda q: float(q)), -2*sqrt(3)/3)
P(id="4-17", ch=14, sec="14.8", type="14-lagrange", src="과제 14.8 #12 유형",
  q=r"타원면 $x^2+2y^2+3z^2=6$ 위에서 $f(x,y,z)=xyz$의 최댓값과 최솟값을 구하라.",
  hint=r"$yz=2\lambda x,\ xz=4\lambda y,\ xy=6\lambda z$에 각각 $x,y,z$를 곱하면 $xyz$가 공통으로 나와요.",
  ans=r"최댓값 $\dfrac{2\sqrt3}{3}$,  최솟값 $-\dfrac{2\sqrt3}{3}$",
  sol=[r"$\nabla f=\lambda\nabla g$: $yz=2\lambda x,\ xz=4\lambda y,\ xy=6\lambda z$",
       r"각각 $x,\ y,\ z$를 곱하면 $xyz=2\lambda x^2=4\lambda y^2=6\lambda z^2$ → ($xyz\ne0$일 때) $x^2=2y^2=3z^2$",
       r"제약에 대입: $3x^2=6 \Rightarrow x^2=2,\ y^2=1,\ z^2=\tfrac23$",
       r"$|xyz|=\sqrt2\cdot1\cdot\sqrt{\tfrac23}=\dfrac{2}{\sqrt3}$ → 최댓값 $\dfrac{2\sqrt3}{3}$, 최솟값 $-\dfrac{2\sqrt3}{3}$ (한 좌표가 0인 점에서는 $f=0$)"],
  check=_c)


def _c():
    lam, mu = symbols('lam mu')
    eqs = [3 - lam - 2*mu*x, -1 - lam, -3 + lam - 4*mu*z, x + y - z, x**2 + 2*z**2 - 1]
    sols = solve(eqs, [x, y, z, lam, mu], dict=True)
    vals = sorted([simplify((3*x - y - 3*z).subs(c)) for c in sols], key=lambda q: float(q))
    assert EQ(vals[0], -2*sqrt(6)) and EQ(vals[-1], 2*sqrt(6))
P(id="4-18", ch=14, sec="14.8", type="14-lagrange2", src="강의 14.8 ex5 유형",
  q=r"두 제약조건 $x+y-z=0$, $x^2+2z^2=1$ 아래에서 $f(x,y,z)=3x-y-3z$의 최댓값과 최솟값을 구하라.",
  hint=r"$\nabla f=\lambda\nabla g+\mu\nabla h$: $\langle3,-1,-3\rangle=\lambda\langle1,1,-1\rangle+\mu\langle2x,0,4z\rangle$ — $y$성분에서 $\lambda$가 바로 나와요.",
  ans=r"최댓값 $2\sqrt6$,  최솟값 $-2\sqrt6$",
  sol=[r"$y$성분: $-1=\lambda$",
       r"$x$성분: $3=-1+2\mu x \Rightarrow x=\dfrac{2}{\mu}$;  $z$성분: $-3=1+4\mu z \Rightarrow z=-\dfrac{1}{\mu}$",
       r"$x^2+2z^2=\dfrac{4}{\mu^2}+\dfrac{2}{\mu^2}=1 \Rightarrow \mu=\pm\sqrt6$,  $y=z-x=-\dfrac{3}{\mu}$",
       r"$f=3x-y-3z=\dfrac{6+3+3}{\mu}=\dfrac{12}{\mu}=\pm\dfrac{12}{\sqrt6}=\pm2\sqrt6$"],
  check=_c)


def _c():
    F = 3*x**2 + 2*y**2 + z**2
    k = sqrt(6)/2
    for sg in (1, -1):
        pt = {x: sg*k, y: sg*k, z: sg*k}
        assert EQ(F.subs(pt), 9)
        g = grad(F, [x, y, z]).subs(pt)
        assert EQ(g.cross(Matrix([3, 2, 1])), [0, 0, 0])
        assert EQ(3*pt[x] + 2*pt[y] + pt[z], sg*3*sqrt(6))
P(id="4-19", ch=14, sec="14.6", type="14-levelsurf", src="강의 14.6 ex8 확장",
  q=r"타원면 $3x^2+2y^2+z^2=9$ 위에서 접평면이 평면 $3x+2y+z=1$과 평행한 점들을 구하고, 각 점에서의 접평면의 방정식을 구하라.",
  hint=r"접평면이 평행 ⇔ $\nabla F=\langle6x,4y,2z\rangle\parallel\langle3,2,1\rangle$",
  ans=r"점 $\pm\left(\tfrac{\sqrt6}{2},\tfrac{\sqrt6}{2},\tfrac{\sqrt6}{2}\right)$,  접평면 $3x+2y+z=\pm3\sqrt6$",
  sol=[r"$\langle6x,4y,2z\rangle=k\langle3,2,1\rangle \Rightarrow x=y=z=\dfrac k2$",
       r"타원면에 대입: $3x^2+2x^2+x^2=6x^2=9 \Rightarrow x=\pm\dfrac{\sqrt6}{2}$",
       r"점 $\pm\tfrac{\sqrt6}{2}(1,1,1)$, 접평면 $3(x-x_0)+2(y-y_0)+(z-z_0)=0$",
       r"$3x+2y+z=6x_0=\pm3\sqrt6$"],
  check=_c)


# ───────── Ch.15 ─────────
def _c():
    I1 = integrate(y, (y, sqrt(1 - x**2), x), (x, 1/sqrt(2), 1))
    I2 = integrate(y, (y, 0, x), (x, 1, sqrt(2)))
    I3 = integrate(y, (y, 0, sqrt(4 - x**2)), (x, sqrt(2), 2))
    polar = integrate(r*sin(th) * r, (r, 1, 2), (th, 0, pi/4))
    assert EQ(I1 + I2 + I3, polar) and EQ(polar, 7*(2 - sqrt(2))/6)
P(id="4-20", ch=15, sec="15.3", type="15-polar", src="과제 15.3 #49 유형",
  q=r"다음 합을 하나의 극좌표 이중적분으로 바꾸어 계산하라. $$\int_{1/\sqrt2}^{1}\!\!\int_{\sqrt{1-x^2}}^{x}y\,dy\,dx+\int_{1}^{\sqrt2}\!\!\int_{0}^{x}y\,dy\,dx+\int_{\sqrt2}^{2}\!\!\int_{0}^{\sqrt{4-x^2}}y\,dy\,dx$$",
  hint=r"세 영역을 합치면 직선 $y=x$, $x$축, 원 $r=1$, 원 $r=2$로 둘러싸인 부채꼴 띠예요.",
  ans=r"$\displaystyle\int_0^{\pi/4}\!\!\int_1^2 r^2\sin\theta\,dr\,d\theta=\frac{7(2-\sqrt2)}{6}$",
  sol=[r"영역 합: $1\le r\le2,\ 0\le\theta\le\tfrac\pi4$ ($y=x$ 아래, $x$축 위, 두 원 사이)",
       r"$\displaystyle\int_0^{\pi/4}\!\!\int_1^2 r\sin\theta\cdot r\,dr\,d\theta=\Big[-\cos\theta\Big]_0^{\pi/4}\Big[\tfrac{r^3}{3}\Big]_1^2$",
       r"$=\left(1-\tfrac{\sqrt2}{2}\right)\cdot\dfrac73=\dfrac{7(2-\sqrt2)}{6}$"],
  check=_c)


def _c():
    assert EQ(integrate(r**2 * r, (r, 0, 2*cos(th)), (th, -pi/2, pi/2)), 3*pi/2)
P(id="4-21", ch=15, sec="15.3", type="15-polar", src="강의 15.3 ex2 · ex3 확장",
  q=r"포물면 $z=x^2+y^2$ 아래, $xy$평면 위, 원기둥 $x^2+y^2=2x$ 안에 있는 입체의 부피를 구하라.",
  hint=r"$x^2+y^2=2x$ ⇔ $r=2\cos\theta$, $-\tfrac\pi2\le\theta\le\tfrac\pi2$",
  ans=r"$\dfrac{3\pi}{2}$",
  sol=[r"$V=\displaystyle\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}r^2\cdot r\,dr\,d\theta=\int_{-\pi/2}^{\pi/2}4\cos^4\theta\,d\theta$",
       r"$\displaystyle\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta=\frac{3\pi}{8}$ ($\cos^4\theta=\tfrac38+\tfrac12\cos2\theta+\tfrac18\cos4\theta$)",
       r"$V=4\cdot\dfrac{3\pi}{8}=\dfrac{3\pi}{2}$"],
  check=_c)


def _c():
    val = integrate(sin(x)*cos(x)*sqrt(1 + cos(x)**2), (x, 0, pi/2))
    assert EQ(val, (2*sqrt(2) - 1) / 3)
    assert EQ(integrate(cos(x)*sqrt(1 + cos(x)**2), (y, 0, sin(x))), sin(x)*cos(x)*sqrt(1 + cos(x)**2))
P(id="4-22", ch=15, sec="15.2", type="15-order", src="과제 15.2 #61 심화형",
  q=r"$\displaystyle\int_0^1\!\!\int_{\arcsin y}^{\pi/2}\cos x\,\sqrt{1+\cos^2x}\,dx\,dy$를 계산하라.",
  hint=r"영역: $0\le y\le1,\ \arcsin y\le x\le\tfrac\pi2$ ⇔ $0\le x\le\tfrac\pi2,\ 0\le y\le\sin x$",
  ans=r"$\dfrac{2\sqrt2-1}{3}$",
  sol=[r"순서 변경: $\displaystyle\int_0^{\pi/2}\!\!\int_0^{\sin x}\cos x\sqrt{1+\cos^2x}\,dy\,dx=\int_0^{\pi/2}\sin x\cos x\sqrt{1+\cos^2x}\,dx$",
       r"$u=1+\cos^2x$, $du=-2\sin x\cos x\,dx$:  $\displaystyle\frac12\int_1^2\sqrt u\,du$",
       r"$=\dfrac12\cdot\dfrac23\Big[u^{3/2}\Big]_1^2=\dfrac{2\sqrt2-1}{3}$"],
  check=_c)


def _c():
    val = integrate(exp(y**3), (z, 0, x), (x, 0, y), (y, 0, 1))
    assert EQ(val, (E - 1) / 6)
P(id="4-23", ch=15, sec="15.6", type="15-order3", src="강의 15.6 ex4 · 과제 15.6 #39 유형",
  q=r"적분 순서를 바꾸어 $\displaystyle\int_0^1\!\!\int_z^1\!\!\int_x^1 e^{y^3}\,dy\,dx\,dz$를 계산하라.",
  hint=r"영역은 $0\le z\le x\le y\le1$. $y$를 가장 바깥으로 보내 $dz\,dx\,dy$ 순서로 바꿔요.",
  ans=r"$\dfrac{e-1}{6}$",
  sol=[r"영역 $E=\{0\le z\le x\le y\le1\}$ → $\displaystyle\int_0^1\!\!\int_0^{y}\!\!\int_0^{x}e^{y^3}\,dz\,dx\,dy$",
       r"$\displaystyle\int_0^{y}\!\!\int_0^{x}dz\,dx=\frac{y^2}{2}$ → $\displaystyle\int_0^1\frac{y^2}{2}e^{y^3}\,dy$",
       r"$=\dfrac16\Big[e^{y^3}\Big]_0^1=\dfrac{e-1}{6}$"],
  check=_c)


def _c():
    assert EQ(integrate((2 - r**2 - r) * r, (r, 0, 1), (th, 0, 2*pi)), 5*pi/6)
P(id="4-24", ch=15, sec="15.7", type="15-cyl", src="복습 15.6–8 기초3 · 4 유형",
  q=r"원뿔 $z=\sqrt{x^2+y^2}$ 위, 포물면 $z=2-x^2-y^2$ 아래에 있는 입체의 부피를 구하라.",
  hint=r"원주좌표에서 $r\le z\le2-r^2$. 두 곡면의 교선은 $r=2-r^2$에서 $r=1$.",
  ans=r"$\dfrac{5\pi}{6}$",
  sol=[r"교선: $r=2-r^2 \Rightarrow r=1$ ($r\ge0$)",
       r"$V=\displaystyle\int_0^{2\pi}\!\!\int_0^1\!\!\int_r^{2-r^2}r\,dz\,dr\,d\theta=2\pi\int_0^1(2r-r^3-r^2)\,dr$",
       r"$=2\pi\Big(1-\tfrac14-\tfrac13\Big)=2\pi\cdot\dfrac{5}{12}=\dfrac{5\pi}{6}$"],
  check=_c)


def _c():
    V = integrate(rho**2*sin(ph), (rho, 0, 2*cos(ph)), (ph, 0, pi/4), (th, 0, 2*pi))
    Mz = integrate(rho*cos(ph)*rho**2*sin(ph), (rho, 0, 2*cos(ph)), (ph, 0, pi/4), (th, 0, 2*pi))
    assert EQ(V, pi) and EQ(Mz, 7*pi/6) and EQ(Mz / V, R(7, 6))
P(id="4-25", ch=15, sec="15.8", type="15-sph", src="복습 15.6–8 심화1 · 강의 15.6 ex6 (질량중심) 유형",
  q=r"$E$가 원뿔 $z=\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=2z$ 안의 입체일 때<br>(a) $E$의 부피 (b) $\displaystyle\iiint_E z\,dV$ (c) 밀도가 일정할 때 질량중심을 구하라.",
  hint=r"구 $x^2+y^2+z^2=2z$ ⇔ $\rho=2\cos\phi$, 원뿔 ⇔ $\phi=\tfrac\pi4$. 대칭이라 $\bar x=\bar y=0$.",
  ans=r"(a) $\pi$  (b) $\dfrac{7\pi}{6}$  (c) $\left(0,\ 0,\ \tfrac76\right)$",
  sol=[r"$E: 0\le\rho\le2\cos\phi,\ 0\le\phi\le\tfrac\pi4,\ 0\le\theta\le2\pi$",
       r"(a) $V=2\pi\displaystyle\int_0^{\pi/4}\frac{8\cos^3\phi}{3}\sin\phi\,d\phi=\frac{16\pi}{3}\Big[-\tfrac{\cos^4\phi}{4}\Big]_0^{\pi/4}=\frac{16\pi}{3}\cdot\frac14\cdot\frac34=\pi$",
       r"(b) $\displaystyle2\pi\int_0^{\pi/4}\!\!\int_0^{2\cos\phi}\rho^3\cos\phi\sin\phi\,d\rho\,d\phi=2\pi\int_0^{\pi/4}4\cos^5\phi\sin\phi\,d\phi=8\pi\cdot\frac16\Big(1-\frac18\Big)=\frac{7\pi}{6}$",
       r"(c) $\bar z=\dfrac{7\pi/6}{\pi}=\dfrac76$, 대칭성으로 $\bar x=\bar y=0$ → $\left(0,0,\tfrac76\right)$"],
  check=_c)


# ───────── Ch.16 ─────────
def _c():
    Pf, Qf = -y / (x**2 + y**2), x / (x**2 + y**2)
    assert simplify(diff(Qf, x) - diff(Pf, y)) == 0
    a_ = symbols('a', positive=True)
    xx, yy = a_*cos(t), a_*sin(t)
    loop = integrate(simplify(Pf.subs({x: xx, y: yy})*diff(xx, t) + Qf.subs({x: xx, y: yy})*diff(yy, t)), (t, 0, 2*pi))
    assert EQ(loop, 2*pi)
    xx, yy = 3*cos(t), 2*sin(t)
    ell = integrate(simplify(Pf.subs({x: xx, y: yy})*diff(xx, t) + Qf.subs({x: xx, y: yy})*diff(yy, t)), (t, 0, 2*pi))
    assert EQ(ell, 2*pi)
P(id="4-26", ch=16, sec="16.4", type="16-singular", src="강의 16.4 ex5 유형",
  q=r"$\mathbf F(x,y)=\dfrac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$에 대해 다음 곡선(모두 반시계 방향)을 따른 $\displaystyle\oint\mathbf F\cdot d\mathbf r$를 구하라.<br>(a) $C_1$: 타원 $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$  (b) $C_2$: 원 $(x-3)^2+y^2=1$",
  hint=r"원점에서 $\mathbf F$가 정의되지 않아요. 원점을 둘러싸는지가 핵심 — 둘러싸면 작은 원으로 바꿔 계산해요.",
  ans=r"(a) $2\pi$  (b) $0$",
  sol=[r"원점 밖에서 $Q_x-P_y=\dfrac{y^2-x^2}{(x^2+y^2)^2}-\dfrac{y^2-x^2}{(x^2+y^2)^2}=0$",
       r"(b) $C_2$가 둘러싼 영역에는 원점이 없으므로 그린 정리로 $\displaystyle\oint_{C_2}=\iint 0\,dA=0$",
       r"(a) 원점을 포함 → 타원 안쪽에 작은 원 $C'$: $x=a\cos t,\ y=a\sin t$를 잡으면, 두 곡선 사이 영역에서 그린 정리에 의해 $\displaystyle\oint_{C_1}=\oint_{C'}$",
       r"$\displaystyle\oint_{C'}=\int_0^{2\pi}\frac{a^2\sin^2t+a^2\cos^2t}{a^2}\,dt=2\pi$"],
  check=_c)


def _c():
    xx, yy = cos(t)**3, sin(t)**3
    A = R(1, 2) * integrate(simplify(xx*diff(yy, t) - yy*diff(xx, t)), (t, 0, 2*pi))
    assert EQ(A, 3*pi/8)
P(id="4-27", ch=16, sec="16.4", type="16-greenarea", src="강의 16.4 ex3 (넓이 공식) 확장",
  q=r"아스트로이드 $x=\cos^3t,\ y=\sin^3t$ $(0\le t\le2\pi)$로 둘러싸인 영역의 넓이를 그린 정리를 이용해 구하라.",
  hint=r"$A=\dfrac12\displaystyle\oint_C(x\,dy-y\,dx)$",
  ans=r"$\dfrac{3\pi}{8}$",
  sol=[r"$dx=-3\cos^2t\sin t\,dt,\ \ dy=3\sin^2t\cos t\,dt$",
       r"$x\,dy-y\,dx=3\sin^2t\cos^2t(\cos^2t+\sin^2t)\,dt=\tfrac34\sin^22t\,dt$",
       r"$A=\dfrac12\displaystyle\int_0^{2\pi}\frac34\sin^22t\,dt=\frac38\cdot\pi=\frac{3\pi}{8}$"],
  check=_c)


def _c():
    integrand = (diff(-x*y**2, x) - diff(x**2*y, y)).subs({x: r*cos(th), y: r*sin(th)})
    assert EQ(integrate(integrand * r, (r, 1, 2), (th, 0, pi/2)), -15*pi/8)
P(id="4-28", ch=16, sec="16.4", type="16-green", src="강의 16.4 ex4 유형",
  q=r"$C$가 제1사분면에서 두 원 $x^2+y^2=1$, $x^2+y^2=4$ 사이 영역의 경계(양의 방향)일 때 $\displaystyle\oint_C x^2y\,dx-xy^2\,dy$를 구하라.",
  hint=r"$Q_x-P_y$를 구한 뒤 $1\le r\le2,\ 0\le\theta\le\tfrac\pi2$에서 극좌표 적분.",
  ans=r"$-\dfrac{15\pi}{8}$",
  sol=[r"$P=x^2y,\ Q=-xy^2 \Rightarrow Q_x-P_y=-y^2-x^2=-r^2$",
       r"$\displaystyle\iint_D(-r^2)\,dA=-\int_0^{\pi/2}\!\!\int_1^2 r^3\,dr\,d\theta=-\frac{\pi}{2}\cdot\frac{16-1}{4}=-\frac{15\pi}{8}$"],
  check=_c)


def _c():
    Fv = Matrix([exp(y), x*exp(y) + z, y + 2*z])
    f = x*exp(y) + y*z + z**2
    assert EQ(grad(f, [x, y, z]), Fv)
    rr = Matrix([cos(pi*t), t**2, t**3 + 1])
    st, en = rr.subs(t, 0), rr.subs(t, 1)
    assert EQ(st, [1, 0, 1]) and EQ(en, [-1, 1, 2])
    assert EQ(f.subs({x: en[0], y: en[1], z: en[2]}) - f.subs({x: st[0], y: st[1], z: st[2]}), 4 - E)
P(id="4-29", ch=16, sec="16.3", type="16-ftli", src="과제 16.3 #16 유형",
  q=r"$\mathbf F=\langle e^y,\ xe^y+z,\ y+2z\rangle$이고 $C:\ \mathbf r(t)=\langle\cos\pi t,\ t^2,\ t^3+1\rangle$, $0\le t\le1$일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$를 구하라.",
  hint=r"보존장 판정 ($P_y=Q_x,\ Q_z=R_y,\ R_x=P_z$) → 퍼텐셜 → 끝점 대입",
  ans=r"$4-e$",
  sol=[r"$P_y=e^y=Q_x,\ \ Q_z=1=R_y,\ \ R_x=0=P_z$ → 보존장",
       r"$f=xe^y+g(y,z)$, $f_y=xe^y+g_y=xe^y+z \Rightarrow g=yz+h(z)$, $f_z=y+h'(z)=y+2z \Rightarrow h=z^2$",
       r"$f=xe^y+yz+z^2$,  시작점 $\mathbf r(0)=(1,0,1)$, 끝점 $\mathbf r(1)=(-1,1,2)$",
       r"$f(-1,1,2)-f(1,0,1)=(-e+2+4)-(1+0+1)=4-e$"],
  check=_c)


def _c():
    I1 = integrate((t - t)*1 + (t - 2)*1, (t, 0, 1))
    I2 = integrate((t - t**2)*1 + (t - 2)*2*t, (t, 0, 1))
    assert EQ(I1, R(-3, 2)) and EQ(I2, R(-7, 6))
    green = integrate(diff(x - 2, x) - diff(x - y, y), (y, x**2, x), (x, 0, 1))
    assert EQ(green, R(1, 3)) and EQ(I2 - I1, green)
P(id="4-30", ch=16, sec="16.4", type="16-green", src="강의 16.3 ex2(a) + 16.4 종합",
  q=r"$\mathbf F=\langle x-y,\ x-2\rangle$에 대해<br>(a) $C_1$: 직선 $y=x$  (b) $C_2$: 포물선 $y=x^2$ 를 따라 $(0,0)$에서 $(1,1)$까지의 $\displaystyle\int\mathbf F\cdot d\mathbf r$를 각각 구하라.<br>(c) 두 값의 차이를 그린 정리로 설명하라.",
  hint=r"$C_2$를 따라 갔다가 $C_1$을 거꾸로 돌아오면 두 곡선 사이 영역을 반시계로 한 바퀴 도는 폐곡선이 돼요.",
  ans=r"(a) $-\dfrac32$  (b) $-\dfrac76$  (c) 차이 $\tfrac13=\displaystyle\iint_D(Q_x-P_y)\,dA$ → $\mathbf F$는 보존장이 아님",
  sol=[r"(a) $\mathbf r=\langle t,t\rangle$: $\mathbf F\cdot\mathbf r'=(t-t)+(t-2)=t-2$ → $\displaystyle\int_0^1(t-2)\,dt=-\frac32$",
       r"(b) $\mathbf r=\langle t,t^2\rangle$: $\mathbf F\cdot\mathbf r'=(t-t^2)+(t-2)(2t)=t^2-3t$ → $\dfrac13-\dfrac32=-\dfrac76$",
       r"(c) $C_2-C_1$은 영역 $D:\ x^2\le y\le x$의 경계를 반시계로 도는 폐곡선",
       r"$Q_x-P_y=1-(-1)=2$ → $\displaystyle\iint_D2\,dA=2\Big(\frac12-\frac13\Big)=\frac13=\Big(-\frac76\Big)-\Big(-\frac32\Big)$ ✓",
       r"$Q_x\ne P_y$이므로 보존장이 아니고, 선적분이 경로에 따라 달라진다."],
  check=_c)

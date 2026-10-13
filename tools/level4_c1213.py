"""4단계 · 심화 추가분 — Ch.12·13: 4-31 ~ 4-34"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    P0 = Matrix([1, 0, 1]); v2 = Matrix([1, 2, -1])
    tt = symbols('tt')
    Q = Matrix([tt, 1 + tt, tt])
    sol = solve((Q - P0).dot(v2), tt)
    assert sol == [-1]
    d = Q.subs(tt, -1) - P0
    assert EQ(d, [-2, 0, -2])
    m = Matrix([1, 0, 1])
    # M과 L2: 만나지 않음 + 평행 아님 → 꼬인 위치
    a, b = symbols('a b')
    eqs = [1 + a - (2 + b), 0 - (3 + 2*b), 1 + a - (-b)]
    assert solve(eqs, [a, b]) == []
    n = m.cross(v2)
    assert EQ(n, [-2, 2, 2])
    diff_ = Matrix([2, 3, 0]) - P0
    assert EQ(abs(n.dot(diff_)) / n.norm(), sqrt(3)/3)
P(id="4-31", ch=12, sec="12.5", type="12-line", src="교재 12.5 심화형 (두 직선과 만나는 직선)",
  q=r"점 $P(1,0,1)$을 지나고, 직선 $L_1:\ x=t,\ y=1+t,\ z=t$와 만나며, 방향벡터가 직선 $L_2:\ x=2+s,\ y=3+2s,\ z=-s$의 방향벡터와 수직인 직선 $M$이 있다.<br>(a) $M$의 매개방정식을 구하라.  (b) $M$과 $L_2$가 꼬인 위치임을 보이고 두 직선 사이의 거리를 구하라.",
  hint=r"$M$이 $L_1$과 만나는 점을 $Q(t,\ 1+t,\ t)$로 두면 $M$의 방향은 $\overrightarrow{PQ}$. 이것이 $\mathbf v_2=\langle1,2,-1\rangle$과 수직이라는 조건으로 $t$를 정해요.",
  ans=r"(a) $M:\ x=1+u,\ y=0,\ z=1+u$  (b) 거리 $\dfrac{\sqrt3}{3}$",
  sol=[r"$\overrightarrow{PQ}=\langle t-1,\ 1+t,\ t-1\rangle$, $\overrightarrow{PQ}\cdot\langle1,2,-1\rangle=(t-1)+2(1+t)-(t-1)=2t+2=0\Rightarrow t=-1$",
       r"$Q=(-1,0,-1)$, $\overrightarrow{PQ}=\langle-2,0,-2\rangle\parallel\langle1,0,1\rangle$ → (a) $M:\ x=1+u,\ y=0,\ z=1+u$",
       r"(b) 방향 $\langle1,0,1\rangle$과 $\langle1,2,-1\rangle$은 평행하지 않음. 연립 $1+u=2+s,\ 0=3+2s$ → $s=-\tfrac32,\ u=-\tfrac12$인데 $z$: $1+u=\tfrac12\ne-s=\tfrac32$ → 만나지 않음 → 꼬인 위치",
       r"$\mathbf n=\langle1,0,1\rangle\times\langle1,2,-1\rangle=\langle-2,2,2\rangle$, 두 직선 위의 점 $(1,0,1)$, $(2,3,0)$ 사이 벡터 $\langle1,3,-1\rangle$",
       r"$d=\dfrac{|\mathbf n\cdot\langle1,3,-1\rangle|}{|\mathbf n|}=\dfrac{|-2+6-2|}{2\sqrt3}=\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}$"],
  check=_c)


def _c():
    A, B, C = Matrix([1, 0, 0]), Matrix([0, 2, 0]), Matrix([0, 0, 3])
    half = (B - A).cross(C - A) / 2
    assert EQ(half, [3, R(3, 2), 1]) and EQ(half.norm(), R(7, 2))
    V = abs(A.dot(B.cross(C))) / 6
    assert V == 1
    assert EQ(3*V / half.norm(), R(6, 7)) and EQ(R(6, 7), 6 / sqrt(36 + 9 + 4))
    assert EQ(1**2 + 3**2 + R(3, 2)**2, R(7, 2)**2)
P(id="4-32", ch=12, sec="12.4", type="12-cross", src="교재 12.4 심화형 (외적과 정사영 넓이)",
  q=r"평면 $6x+3y+2z=6$이 $x,y,z$축과 만나는 점을 각각 $A,B,C$라 하자.<br>(a) 삼각형 $ABC$의 넓이를 구하라.  (b) 사면체 $OABC$의 부피를 구하고, 이를 이용해 원점과 평면 사이의 거리를 구하라.  (c) 삼각형 $ABC$를 세 좌표평면에 정사영한 세 삼각형의 넓이를 각각 $S_1,S_2,S_3$이라 할 때 $S_1^2+S_2^2+S_3^2=(\triangle ABC)^2$임을 확인하라.",
  hint=r"$\triangle ABC=\tfrac12|\overrightarrow{AB}\times\overrightarrow{AC}|$. 사면체 부피 $V=\tfrac13\cdot(\text{밑넓이})\cdot(\text{높이})$에서 밑면을 $\triangle ABC$로 보면 높이가 곧 원점–평면 거리예요.",
  ans=r"(a) $\dfrac72$  (b) $V=1$, 거리 $\dfrac67$  (c) $1^2+3^2+\big(\tfrac32\big)^2=\tfrac{49}{4}=\big(\tfrac72\big)^2$",
  sol=[r"$A(1,0,0),\ B(0,2,0),\ C(0,0,3)$, $\overrightarrow{AB}=\langle-1,2,0\rangle,\ \overrightarrow{AC}=\langle-1,0,3\rangle$",
       r"(a) $\overrightarrow{AB}\times\overrightarrow{AC}=\langle6,3,2\rangle$, 크기 $7$ → 넓이 $\dfrac72$",
       r"(b) $V=\tfrac16|\overrightarrow{OA}\cdot(\overrightarrow{OB}\times\overrightarrow{OC})|=\tfrac16\cdot1\cdot2\cdot3=1$. $V=\tfrac13\cdot\tfrac72\cdot d$ → $d=\dfrac67$ (공식 $\tfrac{6}{\sqrt{36+9+4}}=\tfrac67$과 일치)",
       r"(c) $\tfrac12\overrightarrow{AB}\times\overrightarrow{AC}=\langle3,\tfrac32,1\rangle$의 각 성분이 $yz$, $xz$, $xy$평면으로의 정사영 넓이 ($\triangle OBC=3,\ \triangle OCA=\tfrac32,\ \triangle OAB=1$)",
       r"$9+\tfrac94+1=\tfrac{49}{4}=\big(\tfrac72\big)^2$ ✓"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    tt = symbols('tt', real=True)
    rr = Matrix([1 + cos(tt), sin(tt), 2*sin(tt/2)])
    assert simplify(rr[0]**2 + rr[1]**2 + rr[2]**2 - 4) == 0
    assert simplify((rr[0] - 1)**2 + rr[1]**2 - 1) == 0
    assert EQ(rr.subs(tt, pi/2), [1, 1, sqrt(2)])
    d = rr.diff(tt).subs(tt, pi/2)
    assert EQ(d, [-1, 0, sqrt(2)/2])
    gF = Matrix([2, 2, 2*sqrt(2)]); gG = Matrix([0, 2, 0])
    assert EQ(d.dot(gF), 0) and EQ(d.dot(gG), 0)
    assert EQ(gF.cross(gG), [-4*sqrt(2), 0, 4])
P(id="4-33", ch=13, sec="13.2", type="13-curve", src="교재 13.1–13.2 심화형 (비비아니 곡선)",
  q=r"구 $x^2+y^2+z^2=4$와 원기둥 $(x-1)^2+y^2=1$의 교선 $C$에 대해<br>(a) $x=1+\cos t,\ y=\sin t$로 두고 $C$ 전체를 하나의 벡터함수로 매개화하라.  (b) 점 $(1,1,\sqrt2)$에서 $C$의 접선의 매개방정식을 구하라.  (c) (b)의 접선 방향이 두 곡면의 법선벡터 모두와 수직임을 확인하라.",
  hint=r"$z^2=4-x^2-y^2=2-2\cos t=4\sin^2\tfrac t2$. $z=2\sin\tfrac t2$로 두고 $t$를 $0$부터 $4\pi$까지 돌리면 $z$의 부호가 바뀌는 부분까지 한 번에 그려져요.",
  ans=r"(a) $\mathbf r(t)=\langle1+\cos t,\ \sin t,\ 2\sin\tfrac t2\rangle,\ 0\le t\le4\pi$  (b) $x=1-u,\ y=1,\ z=\sqrt2+\tfrac{\sqrt2}{2}u$  (c) 내적이 모두 $0$",
  sol=[r"(a) $x^2+y^2=2+2\cos t$ → $z^2=4-(2+2\cos t)=2-2\cos t=4\sin^2\tfrac t2$ → $z=2\sin\tfrac t2$ ($0\le t\le4\pi$에서 $z\ge0$, $z\le0$ 부분을 모두 지남)",
       r"(b) $(1,1,\sqrt2)$ ↔ $t=\tfrac\pi2$. $\mathbf r'(t)=\langle-\sin t,\ \cos t,\ \cos\tfrac t2\rangle$ → $\mathbf r'(\tfrac\pi2)=\langle-1,0,\tfrac{\sqrt2}{2}\rangle$",
       r"접선: $x=1-u,\ y=1,\ z=\sqrt2+\tfrac{\sqrt2}{2}u$",
       r"(c) 구의 법선 $\nabla(x^2+y^2+z^2)=\langle2,2,2\sqrt2\rangle$: $-2+0+2=0$. 원기둥의 법선 $\langle2(x-1),2y,0\rangle=\langle0,2,0\rangle$: $0$",
       r"따라서 교선의 접선은 $\nabla F\times\nabla G=\langle-4\sqrt2,0,4\rangle\parallel\langle-1,0,\tfrac{\sqrt2}{2}\rangle$ 방향 — 14.6에서 다시 쓰는 성질이에요."],
  check=_c)


def _c():
    tt = symbols('tt', positive=True)
    rr = Matrix([tt, tt**2/4, tt**3/24])
    assert simplify(rr[0]**2 - 4*rr[1]) == 0 and simplify(6*rr[2] - rr[0]*rr[1]) == 0
    sp2 = rr.diff(tt).dot(rr.diff(tt))
    assert simplify(sp2 - (1 + tt**2/8)**2) == 0
    assert EQ(rr.subs(tt, 4), [4, 4, R(8, 3)])
    assert EQ(integrate(1 + tt**2/8, (tt, 0, 4)), R(20, 3))
    T = rr.diff(tt).subs(tt, 4) / (1 + R(16, 8))
    assert EQ(T, [R(1, 3), R(2, 3), R(2, 3)])
P(id="4-34", ch=13, sec="13.3", type="13-arc", src="교재 13.3 심화형 (교선의 길이)",
  q=r"포물기둥 $x^2=4y$와 곡면 $6z=xy$의 교선을 $C$라 하자.<br>(a) $x=t$로 두고 $C$를 매개화하라.  (b) 원점에서 점 $\big(4,4,\tfrac83\big)$까지 $C$의 길이를 구하라.  (c) 점 $\big(4,4,\tfrac83\big)$에서의 단위접선벡터를 구하라.",
  hint=r"$|\mathbf r'(t)|^2=1+\dfrac{t^2}{4}+\dfrac{t^4}{64}$가 완전제곱식이 돼요.",
  ans=r"(a) $\mathbf r(t)=\big\langle t,\ \tfrac{t^2}{4},\ \tfrac{t^3}{24}\big\rangle$  (b) $\dfrac{20}{3}$  (c) $\big\langle\tfrac13,\tfrac23,\tfrac23\big\rangle$",
  sol=[r"(a) $y=\tfrac{t^2}{4}$, $z=\tfrac{xy}{6}=\tfrac{t^3}{24}$",
       r"$\mathbf r'(t)=\big\langle1,\ \tfrac t2,\ \tfrac{t^2}{8}\big\rangle$, $|\mathbf r'(t)|^2=1+\tfrac{t^2}{4}+\tfrac{t^4}{64}=\big(1+\tfrac{t^2}{8}\big)^2$",
       r"(b) 끝점은 $t=4$: $L=\displaystyle\int_0^4\Big(1+\frac{t^2}{8}\Big)dt=4+\frac{64}{24}=\frac{20}{3}$",
       r"(c) $\mathbf r'(4)=\langle1,2,2\rangle$, $|\mathbf r'(4)|=1+2=3$ → $\mathbf T=\big\langle\tfrac13,\tfrac23,\tfrac23\big\rangle$"],
  check=_c)

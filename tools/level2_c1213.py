"""2단계 · 표준 추가분 — Ch.12·13: 2-31 ~ 2-34"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    n1, n2 = Matrix([1, 1, -1]), Matrix([2, -1, 1])
    d = n1.cross(n2)
    assert EQ(d, [0, -3, -3])
    P0 = Matrix([1, 0, -1])
    assert P0.dot(n1) == 2 and P0.dot(n2) == 1
    Q = Matrix([2, 1, 1]); dd = Matrix([0, 1, 1])
    assert EQ((Q - P0).cross(dd), [-1, -1, 1]) and EQ((Q - P0).cross(dd).norm() / dd.norm(), sqrt(6) / 2)
P(id="2-31", ch=12, sec="12.5", type="12-line", src="2022 생명과학대 기말 4번 유형",
  q=r"두 평면 $x+y-z=2$, $2x-y+z=1$의 교선 $L$의 매개방정식을 구하고, 점 $Q(2,1,1)$에서 $L$까지의 거리를 구하라.",
  hint=r"방향벡터 $=\mathbf n_1\times\mathbf n_2$. 교선 위의 한 점은 $y=0$으로 두고 찾아요. 거리 $=\dfrac{|\overrightarrow{P_0Q}\times\mathbf d|}{|\mathbf d|}$",
  ans=r"$L:\ x=1,\ y=t,\ z=-1+t$,  거리 $\dfrac{\sqrt6}{2}$",
  sol=[r"$\mathbf n_1\times\mathbf n_2=\langle1,1,-1\rangle\times\langle2,-1,1\rangle=\langle0,-3,-3\rangle\parallel\langle0,1,1\rangle$",
       r"$y=0$: $x-z=2,\ 2x+z=1 \Rightarrow x=1,\ z=-1$ → $P_0=(1,0,-1)$",
       r"$L:\ x=1,\ y=t,\ z=-1+t$",
       r"$\overrightarrow{P_0Q}=\langle1,1,2\rangle$, $\overrightarrow{P_0Q}\times\langle0,1,1\rangle=\langle-1,-1,1\rangle$",
       r"거리 $=\dfrac{\sqrt3}{\sqrt2}=\dfrac{\sqrt6}{2}$"],
  check=_c)


def _c():
    a, b, c_ = Matrix([1, 2, -1]), Matrix([0, 1, 3]), Matrix([2, -1, 1])
    assert EQ(b.cross(c_), [4, 6, -2]) and a.dot(b.cross(c_)) == 18
P(id="2-32", ch=12, sec="12.4", type="12-triple", src="2022 생명과학대 기말 13(a) 유형",
  q=r"세 모서리가 $\mathbf a=\langle1,2,-1\rangle$, $\mathbf b=\langle0,1,3\rangle$, $\mathbf c=\langle2,-1,1\rangle$인 평행육면체의 부피를 구하라.",
  hint=r"$V=|\mathbf a\cdot(\mathbf b\times\mathbf c)|$ (스칼라 삼중적)",
  ans=r"$18$",
  sol=[r"$\mathbf b\times\mathbf c=\langle1\cdot1-3\cdot(-1),\ 3\cdot2-0\cdot1,\ 0\cdot(-1)-1\cdot2\rangle=\langle4,6,-2\rangle$",
       r"$\mathbf a\cdot(\mathbf b\times\mathbf c)=4+12+2=18$",
       r"$V=18$ (사면체라면 $\tfrac16$배인 $3$)"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    F1, F2 = x**2 + y**2 - 25, y + z - 7
    pt = {x: 3, y: 4, z: 3}
    assert F1.subs(pt) == 0 and F2.subs(pt) == 0
    d = grad(F1, (x, y, z)).subs(pt).cross(grad(F2, (x, y, z)).subs(pt))
    assert EQ(d, [8, -6, 6])
    rr = Matrix([5*cos(t), 5*sin(t), 7 - 5*sin(t)])
    t0 = atan2(4, 3)
    assert EQ(rr.subs(t, t0), [3, 4, 3]) and EQ(rr.diff(t).subs(t, t0), [-4, 3, -3])
P(id="2-33", ch=13, sec="13.2", type="13-curve", src="2022 생명과학대 기말 5번 유형",
  q=r"원기둥 $x^2+y^2=25$와 평면 $y+z=7$의 교선을 $C$라 하자. $C$를 매개화하고, 점 $(3,4,3)$에서 $C$의 접선의 매개방정식을 구하라.",
  hint=r"$x=5\cos t,\ y=5\sin t,\ z=7-y$. 점에 해당하는 $t$는 $\cos t=\tfrac35,\ \sin t=\tfrac45$",
  ans=r"$\mathbf r(t)=\langle5\cos t,\ 5\sin t,\ 7-5\sin t\rangle$,  접선 $x=3+4s,\ y=4-3s,\ z=3+3s$",
  sol=[r"$\mathbf r(t)=\langle5\cos t,\ 5\sin t,\ 7-5\sin t\rangle,\ 0\le t\le2\pi$",
       r"$(3,4,3)$: $\cos t=\tfrac35,\ \sin t=\tfrac45$.  $\mathbf r'(t)=\langle-5\sin t,\ 5\cos t,\ -5\cos t\rangle=\langle-4,\ 3,\ -3\rangle$",
       r"방향벡터 $\langle-4,3,-3\rangle\parallel\langle4,-3,3\rangle$ → 접선 $x=3+4s,\ y=4-3s,\ z=3+3s$",
       r"검산: 두 법선의 외적 $\langle6,8,0\rangle\times\langle0,1,1\rangle=\langle8,-6,6\rangle\parallel\langle4,-3,3\rangle$ ✓"],
  check=_c)


def _c():
    tt = symbols('tt', positive=True)
    rr = Matrix([2*tt, tt**2, log(tt)])
    sp2 = rr.diff(tt).dot(rr.diff(tt))
    assert simplify(sp2 - (2*tt + 1/tt)**2) == 0
    assert EQ(integrate(2*tt + 1/tt, (tt, 1, E)), E**2)
P(id="2-34", ch=13, sec="13.3", type="13-arc", src="과제 13.3 유형 (완전제곱이 되는 속력)",
  q=r"곡선 $\mathbf r(t)=\langle 2t,\ t^2,\ \ln t\rangle$의 $1\le t\le e$ 부분의 길이를 구하라.",
  hint=r"$|\mathbf r'(t)|^2=4+4t^2+\dfrac1{t^2}=\Big(2t+\dfrac1t\Big)^2$",
  ans=r"$e^2$",
  sol=[r"$\mathbf r'(t)=\left\langle2,\ 2t,\ \tfrac1t\right\rangle$, $|\mathbf r'(t)|=\sqrt{4t^2+4+\tfrac1{t^2}}=2t+\tfrac1t$",
       r"$L=\displaystyle\int_1^e\Big(2t+\frac1t\Big)dt=\Big[t^2+\ln t\Big]_1^e=(e^2+1)-1=e^2$"],
  check=_c)

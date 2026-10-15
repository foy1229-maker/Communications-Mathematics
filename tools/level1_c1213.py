"""1단계 · 기본 추가분 — Ch.12·13 (14~16장 풀이에 필요한 계산만): 1-31 ~ 1-34"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    Pp, Q, Rr = Matrix([1, 2, 0]), Matrix([3, 0, 1]), Matrix([0, 1, 2])
    n = (Q - Pp).cross(Rr - Pp)
    assert EQ(n, [-3, -5, -4])
    for pt in (Pp, Q, Rr):
        assert 3*pt[0] + 5*pt[1] + 4*pt[2] == 13
P(id="1-31", ch=12, sec="12.5", type="12-plane", src="강의 12.5 (세 점을 지나는 평면) · 접평면 계산 준비",
  q=r"세 점 $P(1,2,0)$, $Q(3,0,1)$, $R(0,1,2)$를 지나는 평면의 방정식을 구하라.",
  hint=r"평면 위의 두 벡터 $\overrightarrow{PQ}$, $\overrightarrow{PR}$의 외적이 법선벡터예요.",
  ans=r"$3x+5y+4z=13$",
  sol=[r"$\overrightarrow{PQ}=\langle 2,-2,1\rangle$,  $\overrightarrow{PR}=\langle -1,-1,2\rangle$",
       r"$\mathbf n=\overrightarrow{PQ}\times\overrightarrow{PR}=\langle(-2)(2)-(1)(-1),\ (1)(-1)-(2)(2),\ (2)(-1)-(-2)(-1)\rangle=\langle-3,-5,-4\rangle\parallel\langle3,5,4\rangle$",
       r"$3(x-1)+5(y-2)+4(z-0)=0 \Rightarrow 3x+5y+4z=13$",
       r"검산: $Q$ → $9+0+4=13$, $R$ → $0+5+8=13$ ✓"],
  check=_c)


def _c():
    assert EQ(abs(2*2 - (-1) + 2*3 - 1) / 3, R(10, 3))
    assert EQ(abs(R(11, 2) - 1) / 3, R(3, 2))
P(id="1-32", ch=12, sec="12.5", type="12-dist", src="강의 12.5 (점과 평면 사이 거리) 유형",
  q=r"(a) 점 $(2,-1,3)$과 평면 $2x-y+2z=1$ 사이의 거리를 구하라.<br>(b) 평행한 두 평면 $2x-y+2z=1$, $4x-2y+4z=11$ 사이의 거리를 구하라.",
  hint=r"$d=\dfrac{|ax_0+by_0+cz_0-d|}{\sqrt{a^2+b^2+c^2}}$. (b)는 두 번째 식을 2로 나눠 법선을 맞춰요.",
  ans=r"(a) $\dfrac{10}{3}$  (b) $\dfrac32$",
  sol=[r"(a) $d=\dfrac{|2\cdot2-(-1)+2\cdot3-1|}{\sqrt{4+1+4}}=\dfrac{10}{3}$",
       r"(b) 두 번째 평면: $2x-y+2z=\tfrac{11}{2}$. 첫 평면 위의 점 $(0,-1,0)$에서의 거리",
       r"$d=\dfrac{|0+1+0-\tfrac{11}{2}|}{3}=\dfrac{9/2}{3}=\dfrac32$  (공식 $\dfrac{|d_1-d_2|}{|\mathbf n|}=\dfrac{|1-\frac{11}{2}|}{3}$과 같아요)"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    rr = Matrix([2*cos(t), 2*sin(t), 3 - 2*cos(t)])
    assert simplify(rr[0]**2 + rr[1]**2 - 4) == 0 and simplify(rr[0] + rr[2] - 3) == 0
    seg = Matrix([1 + 2*t, 2 - 3*t, 4*t])
    assert EQ(seg.subs(t, 0), [1, 2, 0]) and EQ(seg.subs(t, 1), [3, -1, 4])
P(id="1-33", ch=13, sec="13.1", type="13-curve", src="강의 13.1 (교선의 매개화) · 16.2 선적분 준비",
  q=r"(a) 원기둥 $x^2+y^2=4$와 평면 $x+z=3$의 교선을 매개화하라.<br>(b) 점 $A(1,2,0)$에서 $B(3,-1,4)$로 가는 선분을 $0\le t\le1$에서 매개화하라.",
  hint=r"(a) 원기둥은 $x=2\cos t,\ y=2\sin t$로 두고 평면에서 $z$를 구해요. (b) $\mathbf r(t)=(1-t)A+tB=A+t\,\overrightarrow{AB}$",
  ans=r"(a) $\mathbf r(t)=\langle 2\cos t,\ 2\sin t,\ 3-2\cos t\rangle,\ 0\le t\le2\pi$  (b) $\mathbf r(t)=\langle 1+2t,\ 2-3t,\ 4t\rangle$",
  sol=[r"(a) $x=2\cos t,\ y=2\sin t$이면 $x^2+y^2=4$ 자동 만족, 평면에서 $z=3-x=3-2\cos t$",
       r"$\mathbf r(t)=\langle 2\cos t,\ 2\sin t,\ 3-2\cos t\rangle,\ 0\le t\le 2\pi$",
       r"(b) $\overrightarrow{AB}=\langle 2,-3,4\rangle$ → $\mathbf r(t)=\langle1,2,0\rangle+t\langle2,-3,4\rangle=\langle 1+2t,\ 2-3t,\ 4t\rangle$",
       r"확인: $t=0$이면 $A$, $t=1$이면 $B$ ✓ (선적분에서 그대로 쓰는 매개화예요)"],
  check=_c)


def _c():
    rr = Matrix([exp(t), t*exp(t), t**2 + 1])
    assert EQ(rr.subs(t, 0), [1, 0, 1]) and EQ(rr.diff(t).subs(t, 0), [1, 1, 0])
P(id="1-34", ch=13, sec="13.2", type="13-deriv", src="강의 13.2 (접선) 유형",
  q=r"곡선 $\mathbf r(t)=\langle e^{t},\ te^{t},\ t^2+1\rangle$ 위의 점 $(1,0,1)$에서 접선의 매개방정식을 구하라.",
  hint=r"점에 대응하는 $t$를 찾고, 방향벡터는 $\mathbf r'(t)$예요.",
  ans=r"$x=1+s,\ y=s,\ z=1$",
  sol=[r"$(1,0,1)$은 $t=0$일 때 ($e^0=1,\ 0\cdot e^0=0,\ 0+1=1$)",
       r"$\mathbf r'(t)=\langle e^t,\ (1+t)e^t,\ 2t\rangle \Rightarrow \mathbf r'(0)=\langle1,1,0\rangle$",
       r"접선: $x=1+s,\ y=s,\ z=1$"],
  check=_c)

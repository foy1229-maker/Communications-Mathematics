"""3단계 · 응용 추가분 — Ch.12·13: 3-31 ~ 3-34"""
from bank_lib import *


# ───────── Ch.12 ─────────
def _c():
    a1, a2, a3, b1, b2, b3 = symbols('a1 a2 a3 b1 b2 b3', real=True)
    A = Matrix([a1, a2, a3]); B = Matrix([b1, b2, b3])
    lhs = (A.dot(B) / A.dot(A) * A).cross(A.dot(B) / B.dot(B) * B)
    rhs = A.dot(B)**2 / (A.dot(A) * B.dot(B)) * A.cross(B)
    assert all(simplify(p - q) == 0 for p, q in zip(lhs, rhs))
    n = Matrix([2, -1, 2])
    ab_norm = n.norm() / sin(pi/3)
    dot = ab_norm * cos(pi/3)
    assert EQ(ab_norm, 2*sqrt(3)) and EQ(dot, sqrt(3))
    assert EQ((dot**2 / ab_norm**2) * n.norm(), R(3, 4))
P(id="3-31", ch=12, sec="12.4", type="12-identity", src="2022 생명과학대 기말 3번 유형",
  q=r"두 벡터 $\mathbf a,\mathbf b$ 사이의 각이 $\dfrac\pi3$이고 $\mathbf a\times\mathbf b=\langle2,-1,2\rangle$이다.<br>(a) $\mathbf a\cdot\mathbf b$를 구하라.  (b) $\big|\operatorname{proj}_{\mathbf a}\mathbf b\times\operatorname{proj}_{\mathbf b}\mathbf a\big|$를 구하라.",
  hint=r"$|\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$, $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta$. 두 사영은 각각 $\mathbf a$, $\mathbf b$의 스칼라배예요.",
  ans=r"(a) $\sqrt3$  (b) $\dfrac34$",
  sol=[r"$|\mathbf a\times\mathbf b|=\sqrt{4+1+4}=3=|\mathbf a||\mathbf b|\cdot\tfrac{\sqrt3}{2} \Rightarrow |\mathbf a||\mathbf b|=2\sqrt3$",
       r"(a) $\mathbf a\cdot\mathbf b=2\sqrt3\cdot\tfrac12=\sqrt3$",
       r"(b) $\operatorname{proj}_{\mathbf a}\mathbf b=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\mathbf a,\ \operatorname{proj}_{\mathbf b}\mathbf a=\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|^2}\mathbf b$ → 외적 $=\dfrac{(\mathbf a\cdot\mathbf b)^2}{|\mathbf a|^2|\mathbf b|^2}(\mathbf a\times\mathbf b)$",
       r"크기: $\dfrac{3}{12}\cdot3=\dfrac34$"],
  check=_c)


def _c():
    v1, v2 = Matrix([1, -1, 2]), Matrix([2, 1, -1])
    assert EQ(v1.dot(v2) / (v1.norm()*v2.norm()), R(-1, 6))
    sol = solve([1 + t - (2 + 2*s), -t - (1 + s)], [t, s])
    assert sol == {t: R(-1, 3), s: R(-2, 3)} and 2*sol[t] != -sol[s]
    n = v1.cross(v2)
    assert EQ(n, [-1, 5, 3])
    P1, P2 = Matrix([1, 0, 0]), Matrix([2, 1, 0])
    assert EQ(abs(n.dot(P2 - P1)) / n.norm(), 4/sqrt(35))
P(id="3-32", ch=12, sec="12.5", type="12-dist", src="2022 생명과학대 기말 12번 유형",
  q=r"두 직선 $L_1:\ x=1+t,\ y=-t,\ z=2t$와 $L_2:\ \dfrac{x-2}{2}=y-1=\dfrac{z}{-1}$에 대해<br>(a) 두 방향벡터 사이의 각 $\theta$에 대해 $\cos\theta$를 구하라.  (b) 두 직선이 꼬인 위치임을 보여라.  (c) 두 직선 사이의 거리를 구하라.",
  hint=r"$L_2$를 $x=2+2s,\ y=1+s,\ z=-s$로 매개화. 거리 $=\dfrac{|\mathbf n\cdot\overrightarrow{P_1P_2}|}{|\mathbf n|}$, $\mathbf n=\mathbf v_1\times\mathbf v_2$",
  ans=r"(a) $-\dfrac16$  (b) 평행하지 않고 만나지 않음  (c) $\dfrac{4}{\sqrt{35}}=\dfrac{4\sqrt{35}}{35}$",
  sol=[r"(a) $\mathbf v_1=\langle1,-1,2\rangle,\ \mathbf v_2=\langle2,1,-1\rangle$, $\cos\theta=\dfrac{2-1-2}{\sqrt6\sqrt6}=-\dfrac16$",
       r"(b) 방향벡터가 평행하지 않아요. $L_2:\ x=2+2s,\ y=1+s,\ z=-s$와 연립: $1+t=2+2s,\ -t=1+s$ → $s=-\tfrac23,\ t=-\tfrac13$",
       r"$z$를 비교하면 $2t=-\tfrac23\ne-s=\tfrac23$ → 만나지 않음 → 꼬인 위치",
       r"(c) $\mathbf n=\mathbf v_1\times\mathbf v_2=\langle(-1)(-1)-2\cdot1,\ 2\cdot2-1\cdot(-1),\ 1\cdot1-(-1)\cdot2\rangle=\langle-1,5,3\rangle$",
       r"$P_1=(1,0,0),\ P_2=(2,1,0)$, $\overrightarrow{P_1P_2}=\langle1,1,0\rangle$ → $d=\dfrac{|-1+5|}{\sqrt{35}}=\dfrac{4}{\sqrt{35}}$"],
  check=_c)


# ───────── Ch.13 ─────────
def _c():
    r1 = Matrix([2 + 3*t, 1 - t**2, 3 - 4*t + t**2]); r2 = Matrix([1 + u**2, 2*u**3 - 1, 2*u + 1])
    assert EQ(r1.subs(t, 0), [2, 1, 3]) and EQ(r2.subs(u, 1), [2, 1, 3])
    n = r1.diff(t).subs(t, 0).cross(r2.diff(u).subs(u, 1))
    assert EQ(n, [24, -14, 18]) and 12*2 - 7*1 + 9*3 == 44
P(id="3-33", ch=13, sec="13.2", type="13-tplane", src="복습 13장 심화1 유형",
  q=r"곡면 $S$ 위에 두 곡선 $\mathbf r_1(t)=\langle2+3t,\ 1-t^2,\ 3-4t+t^2\rangle$, $\mathbf r_2(u)=\langle1+u^2,\ 2u^3-1,\ 2u+1\rangle$이 놓여 있고 둘 다 점 $P(2,1,3)$을 지난다. $P$에서 $S$의 접평면의 방정식을 구하라.",
  hint=r"두 곡선의 접벡터가 모두 접평면 안에 있어요 → 법선 $=\mathbf r_1'\times\mathbf r_2'$ (각각 $P$에 대응하는 매개변수에서)",
  ans=r"$12x-7y+9z=44$",
  sol=[r"$P$에 대응: $\mathbf r_1$은 $t=0$, $\mathbf r_2$는 $u=1$",
       r"$\mathbf r_1'(0)=\langle3,0,-4\rangle$,  $\mathbf r_2'(1)=\langle2u,6u^2,2\rangle\big|_{u=1}=\langle2,6,2\rangle$",
       r"$\mathbf n=\langle3,0,-4\rangle\times\langle2,6,2\rangle=\langle24,-14,18\rangle\parallel\langle12,-7,9\rangle$",
       r"$12(x-2)-7(y-1)+9(z-3)=0 \Rightarrow 12x-7y+9z=44$"],
  check=_c)


def _c():
    tt = symbols('tt', real=True)
    rr = Matrix([exp(tt)*cos(tt), exp(tt)*sin(tt), exp(tt)])
    sp2 = simplify(rr.diff(tt).dot(rr.diff(tt)))
    assert simplify(sp2 - 3*exp(2*tt)) == 0
    assert EQ(integrate(sqrt(3)*exp(tt), (tt, 0, tt)) - sqrt(3)*(exp(tt) - 1), 0)
    ss = symbols('ss', positive=True)
    T = log(1 + ss/sqrt(3))
    rs = rr.subs(tt, T)
    assert EQ(simplify(rs.diff(ss).dot(rs.diff(ss))).subs(ss, 2), 1)
P(id="3-34", ch=13, sec="13.3", type="13-arcfn", src="과제 13.3 #17 유형",
  q=r"곡선 $\mathbf r(t)=\langle e^{t}\cos t,\ e^{t}\sin t,\ e^{t}\rangle$을 $t=0$인 점에서 시작하는 호의 길이 $s$로 재매개화하라.",
  hint=r"$|\mathbf r'(t)|=\sqrt3\,e^{t}$, $s(t)=\displaystyle\int_0^t\sqrt3e^{u}du$를 $t$에 대해 풀어요.",
  ans=r"$t=\ln\!\Big(1+\dfrac{s}{\sqrt3}\Big)$,  $\mathbf r(s)=\Big(1+\dfrac{s}{\sqrt3}\Big)\big\langle\cos\ln(1+\tfrac{s}{\sqrt3}),\ \sin\ln(1+\tfrac{s}{\sqrt3}),\ 1\big\rangle$",
  sol=[r"$\mathbf r'(t)=e^t\langle\cos t-\sin t,\ \sin t+\cos t,\ 1\rangle$, $|\mathbf r'(t)|=e^t\sqrt{(\cos t-\sin t)^2+(\sin t+\cos t)^2+1}=\sqrt3e^t$",
       r"$s=\displaystyle\int_0^t\sqrt3e^u\,du=\sqrt3(e^t-1) \Rightarrow e^t=1+\dfrac{s}{\sqrt3},\ t=\ln\Big(1+\dfrac{s}{\sqrt3}\Big)$",
       r"$\mathbf r(t(s))$에 대입: $e^t=1+\tfrac{s}{\sqrt3}$를 그대로 쓰면 위의 답 ($s\ge0$)"],
  check=_c)

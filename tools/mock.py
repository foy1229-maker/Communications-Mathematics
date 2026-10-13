# -*- coding: utf-8 -*-
"""중간고사 예상 모의고사 (mock.html) — 문제 · 정답 · 풀이 원본과 sympy 검산.

예상 유형 10개로 만든 10문항(EXAM), 2025 시험에 나왔지만 예상 목록에 없던 유형 5문항(EXTRA),
2025 중간고사 문항별 비교표(MAP_MID). 텍스트 안의 $...$ / $$...$$ 는 페이지에서 KaTeX로 그려요.
build.py 가 check_all() 로 모든 정답을 다시 계산해 확인한 뒤 assets/mock-problems.js 를 만들어요.
"""

EXAM = [
    {
        "id": "q1", "no": "1", "type": "예상 유형 1 · 극좌표 이중적분 (장미곡선)", "ref": "2025 중간 1번과 같은 계산 방식",
        "stem": "",
        "parts": [
            ("a", r"$D$가 장미곡선 $r=\sin 3\theta$ 의 한 꽃잎 $\left(0\le\theta\le\frac{\pi}{3}\right)$ 으로 둘러싸인 영역일 때, $\displaystyle\iint_D \sqrt{x^2+y^2}\,dA$ 를 구하시오."),
            ("b", r"장미곡선 $r=2\cos 2\theta$ 의 내부이면서 원 $r=1$ 의 외부인 영역의 넓이를 이중적분으로 구하시오."),
        ],
        "answer": [("a", r"$\dfrac{4}{27}$"), ("b", r"$\dfrac{2\pi}{3}+\sqrt3$")],
        "solution": [
            ("a", [
                r"극좌표에서 $\sqrt{x^2+y^2}=r$, $dA=r\,dr\,d\theta$. 꽃잎 하나는 $0\le\theta\le\frac{\pi}{3}$, $0\le r\le\sin3\theta$ 예요.",
                r"$$\begin{aligned}&\iint_D\sqrt{x^2+y^2}\,dA\\&=\int_0^{\pi/3}\!\!\int_0^{\sin3\theta} r^2\,dr\,d\theta\\&=\frac13\int_0^{\pi/3}\sin^3 3\theta\,d\theta\end{aligned}$$",
                r"$u=3\theta$ 로 치환하면 $$\begin{aligned}&\frac19\int_0^{\pi}\sin^3u\,du\\&=\frac19\Big[-\cos u+\frac{\cos^3u}{3}\Big]_0^{\pi}\\&=\frac19\cdot\frac43=\frac{4}{27}\end{aligned}$$",
            ]),
            ("b", [
                r"교점: $2\cos2\theta=1 \Rightarrow \theta=\pm\frac{\pi}{6}$ ($\theta=0$ 방향 꽃잎). 꽃잎 네 개가 합동이라 한 꽃잎에서 원 바깥 부분을 구해 4배 해요.",
                r"$$\begin{aligned}A&=4\int_{-\pi/6}^{\pi/6}\!\!\int_1^{2\cos2\theta} r\,dr\,d\theta\\&=2\int_{-\pi/6}^{\pi/6}\big(4\cos^2 2\theta-1\big)\,d\theta\end{aligned}$$",
                r"$4\cos^22\theta-1=1+2\cos4\theta$ 이므로 $$\begin{aligned}A&=2\Big[\theta+\tfrac12\sin4\theta\Big]_{-\pi/6}^{\pi/6}\\&=2\Big(\frac{\pi}{3}+\frac{\sqrt3}{2}\Big)=\frac{2\pi}{3}+\sqrt3\end{aligned}$$",
            ]),
        ],
    },
    {
        "id": "q2", "no": "2", "type": "예상 유형 2 · 극한과 연속", "ref": "2025 중간 3번",
        "stem": "다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
        "parts": [
            ("a", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y^3}{x^4+y^4}$"),
            ("b", r"$\displaystyle\lim_{(x,y)\to(0,0)}\frac{\sin(xy^2)}{x^2+y^4}$"),
            ("c", r"$g(x,y)=\dfrac{\sin(xy^2)}{x^2+y^4}\ \big((x,y)\ne(0,0)\big)$, $g(0,0)=0$ 일 때, $g$가 연속인 점의 집합을 구하시오."),
        ],
        "answer": [("a", r"$0$"), ("b", r"존재하지 않음 (곡선 $x=ky^2$ 를 따라 $\frac{k}{k^2+1}$)"), ("c", r"원점을 뺀 모든 점 $\{(x,y)\mid (x,y)\ne(0,0)\}$")],
        "solution": [
            ("a", [
                r"$x^4+y^4-2x^2y^2=(x^2-y^2)^2\ge0$ 이므로 $\dfrac{x^2y^2}{x^4+y^4}\le\dfrac12$.",
                r"$$\left|\frac{x^2y^3}{x^4+y^4}\right|=|y|\cdot\frac{x^2y^2}{x^4+y^4}\le\frac{|y|}{2}\to0$$ 조임정리로 극한은 $0$.",
            ]),
            ("b", [
                r"직선 $y=mx$ 를 따라가면 모두 $0$ 이라 판정이 안 돼요. 분모의 $x^2$ 와 $y^4$ 의 차수가 같아지도록 곡선 $x=ky^2$ 를 써요.",
                r"대입하면 $$\begin{aligned}&\frac{\sin(ky^4)}{(k^2+1)\,y^4}\\&=\frac{\sin(ky^4)}{ky^4}\cdot\frac{k}{k^2+1}\\&\longrightarrow\ \frac{k}{k^2+1}\quad(y\to0,\ k\ne0)\end{aligned}$$",
                r"$k=0$ (즉 $x=0$) 이면 $0$, $k=1$ 이면 $\frac12$. 경로마다 값이 다르므로 극한은 존재하지 않아요.",
            ]),
            ("c", [
                r"$(x,y)\ne(0,0)$ 이면 분모 $x^2+y^4>0$ 이고 분자·분모가 연속이므로 $g$는 연속이에요.",
                r"원점에서는 (b)에서 $\lim g$ 가 존재하지 않으므로 불연속. 연속인 점의 집합은 원점을 뺀 평면 전체예요.",
            ]),
        ],
    },
    {
        "id": "q3", "no": "3", "type": "예상 유형 3 · 등위곡면의 접평면과 법선", "ref": "2025 중간 6번 일부",
        "stem": r"곡면 $S:\ x^2+2y^2+z^2+xz=9$ 위의 점 $P(1,-1,2)$ 에 대하여",
        "parts": [
            ("a", r"$P$에서 $S$의 접평면과 법선의 방정식을 구하시오."),
            ("b", r"접평면이 $xy$평면과 평행한 $S$ 위의 점을 모두 구하시오."),
            ("c", r"$S$와 평면 $x+y+z=2$ 의 교선을 $C$라 할 때, $P$에서 $C$의 접선의 매개방정식을 구하시오."),
        ],
        "answer": [
            ("a", r"접평면 $4x-4y+5z=18$, 법선 $\dfrac{x-1}{4}=\dfrac{y+1}{-4}=\dfrac{z-2}{5}$"),
            ("b", r"$(\sqrt3,\,0,\,-2\sqrt3)$, $(-\sqrt3,\,0,\,2\sqrt3)$"),
            ("c", r"$x=1-9t,\ y=-1+t,\ z=2+8t$"),
        ],
        "solution": [
            ("a", [
                r"$F=x^2+2y^2+z^2+xz$ 라 두면 $S$는 등위곡면 $F=9$. $\nabla F=\langle 2x+z,\ 4y,\ 2z+x\rangle$, $\nabla F(1,-1,2)=\langle4,-4,5\rangle$.",
                r"접평면: $4(x-1)-4(y+1)+5(z-2)=0 \Rightarrow 4x-4y+5z=18$.",
                r"법선: $x=1+4t,\ y=-1-4t,\ z=2+5t$, 대칭방정식으로 $\dfrac{x-1}{4}=\dfrac{y+1}{-4}=\dfrac{z-2}{5}$.",
            ]),
            ("b", [
                r"접평면이 $xy$평면과 평행 $\Leftrightarrow$ 법선벡터 $\nabla F$ 가 $\mathbf k$ 와 평행 $\Leftrightarrow$ $F_x=F_y=0$: $2x+z=0,\ 4y=0$.",
                r"$y=0,\ z=-2x$ 를 $S$에 대입: $x^2+4x^2-2x^2=3x^2=9 \Rightarrow x=\pm\sqrt3$.",
                r"점 $(\sqrt3,0,-2\sqrt3)$, $(-\sqrt3,0,2\sqrt3)$. 이때 $F_z=-3x\ne0$ 이라 법선이 실제로 $\mathbf k$ 방향이에요.",
            ]),
            ("c", [
                r"$P$가 평면 위에 있는지 확인: $1-1+2=2$. $C$는 두 곡면 위에 있으므로 접선은 두 법선 $\langle4,-4,5\rangle$, $\langle1,1,1\rangle$ 에 모두 수직이에요.",
                r"방향벡터: $$\langle4,-4,5\rangle\times\langle1,1,1\rangle=\langle -9,\ 1,\ 8\rangle$$",
                r"접선: $x=1-9t,\ y=-1+t,\ z=2+8t$.",
            ]),
        ],
    },
    {
        "id": "q4", "no": "4", "type": "예상 유형 4 · 라그랑주 승수법", "ref": "2025 중간 8번",
        "stem": "",
        "parts": [
            ("a", r"타원 $\dfrac{x^2}{8}+\dfrac{y^2}{2}=1$ 위에서 $f(x,y)=xy$ 의 최댓값과 최솟값을 구하시오."),
            ("b", r"평면 $x+y-z=0$ 과 곡면 $x^2+2z^2=1$ 의 교선 위에서 $f(x,y,z)=3x-y-3z$ 의 최댓값과 최솟값을 구하시오."),
        ],
        "answer": [
            ("a", r"최댓값 $2$ $\big((2,1),(-2,-1)\big)$, 최솟값 $-2$ $\big((2,-1),(-2,1)\big)$"),
            ("b", r"최댓값 $2\sqrt6$ $\big(\big(\tfrac{\sqrt6}{3},-\tfrac{\sqrt6}{2},-\tfrac{\sqrt6}{6}\big)\big)$, 최솟값 $-2\sqrt6$"),
        ],
        "solution": [
            ("a", [
                r"$g=\dfrac{x^2}{8}+\dfrac{y^2}{2}$, $\nabla f=\lambda\nabla g$: $\ y=\dfrac{\lambda x}{4},\quad x=\lambda y$.",
                r"대입하면 $y=\dfrac{\lambda^2}{4}y$. $y=0$ 이면 $x=0$ 인데 타원 위의 점이 아니므로 $\lambda^2=4$.",
                r"$\lambda=2$: $x=2y$, $y^2=1$ → $(2,1),(-2,-1)$ 에서 $f=2$. $\lambda=-2$: $x=-2y$ → $(-2,1),(2,-1)$ 에서 $f=-2$.",
                r"타원은 닫힌 유계 곡선이라 최댓값·최솟값이 존재해요. 최댓값 $2$, 최솟값 $-2$.",
            ]),
            ("b", [
                r"$g=x+y-z=0$, $h=x^2+2z^2=1$, $\nabla f=\lambda\nabla g+\mu\nabla h$: $$\langle3,-1,-3\rangle=\lambda\langle1,1,-1\rangle+\mu\langle2x,0,4z\rangle$$",
                r"$y$성분에서 $\lambda=-1$. 그러면 $3=-1+2\mu x \Rightarrow x=\dfrac{2}{\mu}$, $\ -3=1+4\mu z\Rightarrow z=-\dfrac{1}{\mu}$.",
                r"$h=1$ 에 대입: $\dfrac{4}{\mu^2}+\dfrac{2}{\mu^2}=1 \Rightarrow \mu=\pm\sqrt6$. 또 $y=z-x=-\dfrac{3}{\mu}$.",
                r"$f=3x-y-3z=\dfrac{6+3+3}{\mu}=\dfrac{12}{\mu}=\pm2\sqrt6$. 최댓값 $2\sqrt6$ (점 $\big(\tfrac{\sqrt6}{3},-\tfrac{\sqrt6}{2},-\tfrac{\sqrt6}{6}\big)$), 최솟값 $-2\sqrt6$.",
            ]),
        ],
    },
    {
        "id": "q5", "no": "5", "type": "예상 유형 5 · 이중적분 (순서 바꾸기 · 극좌표 · 심장형)", "ref": "2025 중간 2(b), 7번의 영역",
        "stem": "다음을 계산하시오.",
        "parts": [
            ("a", r"(적분 순서를 바꾸어) $\displaystyle\int_0^4\!\!\int_{\sqrt x}^{2}\frac{1}{y^3+1}\,dy\,dx$"),
            ("b", r"(극좌표로 바꾸어) $$\begin{aligned}&\int_0^1\!\!\int_{\sqrt{1-x^2}}^{\sqrt{4-x^2}} xy\,dy\,dx\\&\quad+\int_1^2\!\!\int_0^{\sqrt{4-x^2}} xy\,dy\,dx\end{aligned}$$"),
            ("c", r"$D=\{(x,y)\mid x^2+y^2\le\sqrt{x^2+y^2}+x\}$ 일 때 $\displaystyle\iint_D x\,dA$"),
            ("d", r"직선 $y=x-4$ 와 포물선 $y^2=2x$ 로 둘러싸인 영역 $D$에서 $\displaystyle\iint_D xy\,dA$"),
        ],
        "answer": [("a", r"$\dfrac23\ln3$"), ("b", r"$\dfrac{15}{8}$"), ("c", r"$\dfrac{5\pi}{4}$"), ("d", r"$90$")],
        "solution": [
            ("a", [
                r"영역: $0\le x\le4,\ \sqrt x\le y\le2$ $\Leftrightarrow$ $0\le y\le2,\ 0\le x\le y^2$.",
                r"$$\begin{aligned}\int_0^2\!\!\int_0^{y^2}\frac{1}{y^3+1}\,dx\,dy&=\int_0^2\frac{y^2}{y^3+1}\,dy\\&=\frac13\ln(y^3+1)\Big|_0^2\\&=\frac13\ln9=\frac23\ln3\end{aligned}$$",
            ]),
            ("b", [
                r"첫 적분은 원 $x^2+y^2=1$ 과 $x^2+y^2=4$ 사이($0\le x\le1$), 둘째는 $1\le x\le2$ 에서 큰 원 안쪽. 합치면 1사분면 고리 $1\le r\le2,\ 0\le\theta\le\frac{\pi}{2}$.",
                r"$$\begin{aligned}&\int_0^{\pi/2}\!\!\int_1^2 (r\cos\theta)(r\sin\theta)\,r\,dr\,d\theta\\&=\int_0^{\pi/2}\sin\theta\cos\theta\,d\theta\cdot\int_1^2 r^3\,dr\\&=\frac12\cdot\frac{15}{4}=\frac{15}{8}\end{aligned}$$",
            ]),
            ("c", [
                r"극좌표로 쓰면 $r^2\le r+r\cos\theta \Leftrightarrow r\le1+\cos\theta$. 심장형 곡선의 내부예요.",
                r"$$\begin{aligned}\iint_D x\,dA&=\int_0^{2\pi}\!\!\int_0^{1+\cos\theta} r^2\cos\theta\,dr\,d\theta\\&=\frac13\int_0^{2\pi}(1+\cos\theta)^3\cos\theta\,d\theta\end{aligned}$$",
                r"전개하면 $\cos\theta+3\cos^2\theta+3\cos^3\theta+\cos^4\theta$. 한 주기 적분은 차례로 $0,\ 3\pi,\ 0,\ \frac{3\pi}{4}$ 이므로 $\frac13\cdot\frac{15\pi}{4}=\frac{5\pi}{4}$.",
            ]),
            ("d", [
                r"교점: $y^2=2(y+4) \Rightarrow y=-2,\ 4$, 즉 $(2,-2),(8,4)$. $x$로 자르면 아래 경계가 바뀌어 두 조각이 되니 $y$ 기준(유형 II)으로 써요: $-2\le y\le4,\ \frac{y^2}{2}\le x\le y+4$.",
                r"$$\begin{aligned}&\int_{-2}^{4}\!\!\int_{y^2/2}^{y+4} xy\,dx\,dy\\&=\frac12\int_{-2}^{4}\Big(y(y+4)^2-\frac{y^5}{4}\Big)dy\\&=\frac12(348-168)=90\end{aligned}$$",
            ]),
        ],
    },
    {
        "id": "q6", "no": "6", "type": "예상 유형 6 · 삼중적분 (직교 · 원주 · 구면 · 순서 바꾸기)", "ref": "2025 중간 4, 9, 10번",
        "stem": "다음을 계산하시오.",
        "parts": [
            ("a", r"$E$가 평면 $z=1+x+y$ 아래, $xy$평면 위에 있고 밑면이 곡선 $y=\sqrt x$, $y=0$, $x=1$ 로 둘러싸인 영역인 입체일 때 $\displaystyle\iiint_E 6xy\,dV$"),
            ("b", r"포물면 $z=x^2+y^2$ 과 평면 $z=4$ 로 둘러싸인 입체 $E$에서 $\displaystyle\iiint_E z\,dV$"),
            ("c", r"다음 적분을 구면좌표로 바꾸어 나타내고 값을 구하시오. $$\int_0^{2\pi}\!\!\int_0^{\sqrt2}\!\!\int_r^{\sqrt{4-r^2}} r\sqrt{r^2+z^2}\,dz\,dr\,d\theta$$"),
            ("d", r"(적분 순서를 바꾸어) $\displaystyle\int_0^1\!\!\int_0^x\!\!\int_x^1 6e^{z^3}\,dz\,dy\,dx$"),
        ],
        "answer": [
            ("a", r"$\dfrac{65}{28}$"), ("b", r"$\dfrac{64\pi}{3}$"),
            ("c", r"$\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^2 \rho^3\sin\phi\,d\rho\,d\phi\,d\theta=4\pi(2-\sqrt2)$"),
            ("d", r"$e-1$"),
        ],
        "solution": [
            ("a", [
                r"$E=\{0\le x\le1,\ 0\le y\le\sqrt x,\ 0\le z\le1+x+y\}$.",
                r"$$\begin{aligned}&\int_0^1\!\!\int_0^{\sqrt x} 6xy(1+x+y)\,dy\,dx\\&=\int_0^1\Big[3xy^2(1+x)+2xy^3\Big]_0^{\sqrt x}dx\\&=\int_0^1\big(3x^2+3x^3+2x^{5/2}\big)dx\end{aligned}$$",
                r"$=1+\frac34+\frac47=\frac{65}{28}$.",
            ]),
            ("b", [
                r"원주좌표: 포물면과 평면은 $r=2$ 에서 만나므로 $0\le\theta\le2\pi,\ 0\le r\le2,\ r^2\le z\le4$.",
                r"$$\begin{aligned}&\int_0^{2\pi}\!\!\int_0^2\!\!\int_{r^2}^4 z\,r\,dz\,dr\,d\theta\\&=2\pi\int_0^2\frac{16-r^4}{2}\,r\,dr\\&=\pi\Big[8r^2-\frac{r^6}{6}\Big]_0^2=\frac{64\pi}{3}\end{aligned}$$",
            ]),
            ("c", [
                r"영역 읽기: $z\ge r$ 는 원뿔 $\phi\le\frac{\pi}{4}$ 의 위, $z\le\sqrt{4-r^2}$ 는 구 $\rho\le2$ 의 안쪽, $r\le\sqrt2$ 는 둘이 만나는 원이에요.",
                r"$r\,dz\,dr\,d\theta=dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$, $\sqrt{r^2+z^2}=\rho$: $$\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^2 \rho^3\sin\phi\,d\rho\,d\phi\,d\theta$$",
                r"$=2\pi\cdot\Big(1-\frac{\sqrt2}{2}\Big)\cdot\frac{2^4}{4}=8\pi\Big(1-\frac{\sqrt2}{2}\Big)=4\pi(2-\sqrt2)$.",
            ]),
            ("d", [
                r"$e^{z^3}$ 은 $z$로 먼저 적분할 수 없어요. 영역: $0\le x\le1,\ 0\le y\le x,\ x\le z\le1$.",
                r"$z$를 바깥으로: $0\le z\le1,\ 0\le x\le z,\ 0\le y\le x$. $$\begin{aligned}&\int_0^1\!\!\int_0^z\!\!\int_0^x 6e^{z^3}\,dy\,dx\,dz\\&=\int_0^1 6e^{z^3}\cdot\frac{z^2}{2}\,dz\\&=\Big[e^{z^3}\Big]_0^1=e-1\end{aligned}$$",
            ]),
        ],
    },
    {
        "id": "q7", "no": "7", "type": "예상 유형 7 · 방향미분계수와 그래디언트", "ref": "2025 중간 6(a)",
        "stem": r"$f(x,y,z)=xy^2+yz+e^{xz}$, $P(0,1,2)$ 일 때",
        "parts": [
            ("a", r"$\nabla f(P)$ 를 구하시오."),
            ("b", r"$P$에서 점 $Q(2,3,3)$ 을 향하는 방향으로의 방향미분계수를 구하시오."),
            ("c", r"곡선 $\mathbf r(t)=\langle \sin t,\ 1+t^2,\ 2e^{t}\rangle$ 을 따라 움직이는 입자가 $t=0$ 에서 $P$를 지난다. 이 순간 $f(\mathbf r(t))$ 의 변화율과, $P$에서 곡선의 접선 방향으로의 방향미분계수를 각각 구하시오."),
        ],
        "answer": [("a", r"$\langle3,\ 2,\ 1\rangle$"), ("b", r"$\dfrac{11}{3}$"), ("c", r"변화율 $5$, 방향미분계수 $\sqrt5$")],
        "solution": [
            ("a", [r"$\nabla f=\langle y^2+ze^{xz},\ 2xy+z,\ y+xe^{xz}\rangle$ 이므로 $\nabla f(0,1,2)=\langle 1+2,\ 0+2,\ 1+0\rangle=\langle3,2,1\rangle$."]),
            ("b", [r"$\overrightarrow{PQ}=\langle2,2,1\rangle$, $|\overrightarrow{PQ}|=3$, $\mathbf u=\frac13\langle2,2,1\rangle$ → $D_{\mathbf u}f(P)=\nabla f(P)\cdot\mathbf u=\frac{6+4+1}{3}=\frac{11}{3}$."]),
            ("c", [
                r"$\mathbf r(0)=\langle0,1,2\rangle=P$, $\mathbf r'(t)=\langle\cos t,\ 2t,\ 2e^t\rangle$ → $\mathbf r'(0)=\langle1,0,2\rangle$.",
                r"연쇄법칙: $\dfrac{d}{dt}f(\mathbf r(t))\Big|_{t=0}=\nabla f(P)\cdot\mathbf r'(0)=3+0+2=5$.",
                r"접선 방향 단위벡터 $\mathbf u=\frac{1}{\sqrt5}\langle1,0,2\rangle$ → $D_{\mathbf u}f(P)=\frac{5}{\sqrt5}=\sqrt5$. (변화율 $5$ = 방향미분계수 $\sqrt5$ × 속력 $|\mathbf r'(0)|=\sqrt5$)",
            ]),
        ],
    },
    {
        "id": "q8", "no": "8", "type": "예상 유형 8 · 선적분의 기본정리", "ref": "2025 기말 1(a), 4번",
        "stem": r"$\mathbf F(x,y,z)=\langle y^2+2xz,\ \ 2xy+e^{z},\ \ x^2+ye^{z}\rangle$ 일 때",
        "parts": [
            ("a", r"$\mathbf F$가 보존장임을 보이고 $\mathbf F=\nabla f$ 인 함수 $f$를 구하시오."),
            ("b", r"$C:\ \mathbf r(t)=\big\langle \cos\pi t,\ \sin\frac{\pi t}{2},\ t\,e^{t^2-1}\big\rangle,\ 0\le t\le1$ 일 때 $\displaystyle\int_C\mathbf F\cdot d\mathbf r$ 를 구하시오."),
            ("c", r"$\mathbf G(x,y)=\langle 2xy+3y,\ x^2+x\rangle$ 는 보존장이 아니다. $C$가 원 $x^2+y^2=1$ 의 위쪽 반원을 $(1,0)$에서 $(-1,0)$까지 가는 곡선일 때, $\mathbf G$를 보존장과 간단한 벡터장의 합으로 나누어 $\displaystyle\int_C\mathbf G\cdot d\mathbf r$ 를 구하시오."),
        ],
        "answer": [("a", r"$f(x,y,z)=xy^2+x^2z+ye^{z}+K$"), ("b", r"$e$"), ("c", r"$-\pi$")],
        "solution": [
            ("a", [
                r"$P=y^2+2xz,\ Q=2xy+e^z,\ R=x^2+ye^z$: $P_y=2y=Q_x$, $\ Q_z=e^z=R_y$, $\ R_x=2x=P_z$. 정의역이 $\mathbb R^3$ 이므로 보존장이에요.",
                r"$f=\int P\,dx=xy^2+x^2z+g(y,z)$. $\ f_y=2xy+g_y=2xy+e^z \Rightarrow g=ye^z+h(z)$.",
                r"$f_z=x^2+ye^z+h'(z)=R \Rightarrow h'(z)=0$. 따라서 $f=xy^2+x^2z+ye^z+K$.",
            ]),
            ("b", [
                r"시작점 $\mathbf r(0)=(1,0,0)$, 끝점 $\mathbf r(1)=(-1,1,1)$. 곡선의 모양과 상관없이 끝점만 필요해요.",
                r"$$\begin{aligned}\int_C\mathbf F\cdot d\mathbf r&=f(-1,1,1)-f(1,0,0)\\&=(-1+1+e)-0=e\end{aligned}$$",
            ]),
            ("c", [
                r"$\mathbf G=\langle2xy,\ x^2\rangle+\langle3y,\ x\rangle=\nabla(x^2y)+\langle3y,\ x\rangle$. ($\mathbf G$ 자체는 $Q_x-P_y=(2x+1)-(2x+3)=-2\ne0$)",
                r"보존장 부분: $x^2y\Big|_{(1,0)}^{(-1,0)}=0-0=0$.",
                r"나머지 $\langle3y,\ x\rangle$: $x=\cos t,\ y=\sin t\ (0\le t\le\pi)$, $d\mathbf r=\langle-\sin t,\ \cos t\rangle\,dt$ $$\begin{aligned}&\int_0^{\pi}\big(-3\sin^2t+\cos^2t\big)\,dt\\&=-\frac{3\pi}{2}+\frac{\pi}{2}=-\pi\end{aligned}$$",
                r"합: $0+(-\pi)=-\pi$.",
            ]),
        ],
    },
    {
        "id": "q9", "no": "9", "type": "예상 유형 9 · 그린 정리", "ref": "2025 기말 1(b), 5번",
        "stem": "",
        "parts": [
            ("a", r"$C$가 $y=x^2$ 과 $y=1$ 로 둘러싸인 영역의 경계(반시계 방향)일 때 $\displaystyle\oint_C y^2\,dx+3xy\,dy$ 를 (i) $C$를 두 곡선으로 나누어 직접 계산하고, (ii) 그린 정리로 계산하시오."),
            ("b", r"$C$가 원 $x^2+y^2=4$ 의 위쪽 반원을 $(2,0)$에서 $(-2,0)$까지 가는 곡선일 때 $$\int_C (x^2-y^3)\,dx+(x^3+e^{y^2})\,dy$$"),
            ("c", r"$C$가 꼭짓점이 $(-1,-1),\ (2,-1),\ (-1,2)$ 인 삼각형(반시계 방향)일 때 $\displaystyle\oint_C\frac{-y\,dx+x\,dy}{x^2+y^2}$"),
        ],
        "answer": [("a", r"$\dfrac45$ (두 방법 모두)"), ("b", r"$12\pi-\dfrac{16}{3}$"), ("c", r"$2\pi$")],
        "solution": [
            ("a", [
                r"(i) $C_1$: 포물선 $x=t,\ y=t^2$, $-1\le t\le1$: $$\begin{aligned}&\int_{-1}^{1}\big(t^4\cdot1+3t\cdot t^2\cdot2t\big)\,dt\\&=\int_{-1}^1 7t^4\,dt=\frac{14}{5}\end{aligned}$$",
                r"$C_2$: 선분 $y=1$, $(1,1)\to(-1,1)$, $dy=0$: $\displaystyle\int_1^{-1}1\,dx=-2$. 합: $\frac{14}{5}-2=\frac45$.",
                r"(ii) $Q_x-P_y=3y-2y=y$: $$\begin{aligned}\iint_D y\,dA&=\int_{-1}^1\!\!\int_{x^2}^1 y\,dy\,dx\\&=\int_{-1}^1\frac{1-x^4}{2}\,dx=\frac45\end{aligned}$$",
            ]),
            ("b", [
                r"반원만으로는 닫힌 곡선이 아니에요. 선분 $L:(-2,0)\to(2,0)$ 을 붙이면 $C\cup L$ 은 위쪽 반원판 $D$의 경계(반시계).",
                r"그린 정리: $Q_x-P_y=3x^2+3y^2$ $$\begin{aligned}\oint_{C\cup L}&=\iint_D 3(x^2+y^2)\,dA\\&=\int_0^{\pi}\!\!\int_0^2 3r^2\cdot r\,dr\,d\theta=12\pi\end{aligned}$$",
                r"$L$ 위에서는 $y=0,\ dy=0$: $\displaystyle\int_L=\int_{-2}^{2}x^2\,dx=\frac{16}{3}$.",
                r"$\displaystyle\int_C=12\pi-\frac{16}{3}$. ($e^{y^2}$ 항을 직접 적분할 필요가 없어져요.)",
            ]),
            ("c", [
                r"$P=\dfrac{-y}{x^2+y^2},\ Q=\dfrac{x}{x^2+y^2}$ 는 원점 밖에서 $Q_x-P_y=0$. 그런데 원점이 삼각형 안에 있어서 삼각형 전체에 그린 정리를 바로 쓸 수 없어요.",
                r"삼각형 안에 작은 원 $C_a:\ x=a\cos t,\ y=a\sin t$ (반시계)를 잡고 사이 영역에 그린 정리: $\displaystyle\oint_C-\oint_{C_a}=\iint 0\,dA=0$.",
                r"$$\begin{aligned}\oint_{C_a}&=\int_0^{2\pi}\frac{a^2\sin^2t+a^2\cos^2t}{a^2}\,dt\\&=\int_0^{2\pi}1\,dt=2\pi\end{aligned}$$ 따라서 $\displaystyle\oint_C=2\pi$.",
            ]),
        ],
    },
    {
        "id": "q10", "no": "10", "type": "예상 유형 10 · 최대 증가 방향과 기울기", "ref": "강의 14.6 예제 6 응용",
        "stem": r"언덕의 높이가 $h(x,y)=4-x^2-2y^2$ 이고 등산객이 점 $P(1,1)$ 에 서 있다.",
        "parts": [
            ("a", r"$P$에서 가장 가파르게 올라가는 방향(단위벡터)과 그 방향의 기울기를 구하시오."),
            ("b", r"$P$에서 높이가 변하지 않는 방향을 모두 구하고, $P$를 지나는 등위곡선의 접선의 방정식을 구하시오."),
            ("c", r"$D_{\mathbf u}h(P)=2$ 를 만족하는 단위벡터 $\mathbf u$를 모두 구하시오."),
        ],
        "answer": [
            ("a", r"방향 $\frac{1}{\sqrt5}\langle-1,-2\rangle$, 기울기 $2\sqrt5$"),
            ("b", r"$\pm\frac{1}{\sqrt5}\langle2,-1\rangle$, 접선 $x+2y=3$"),
            ("c", r"$\langle-1,\ 0\rangle$, $\ \big\langle\frac35,\ -\frac45\big\rangle$"),
        ],
        "solution": [
            ("a", [
                r"$\nabla h=\langle-2x,\ -4y\rangle$, $\nabla h(1,1)=\langle-2,-4\rangle$.",
                r"가장 가파르게 올라가는 방향은 $\mathbf u=\dfrac{\nabla h}{|\nabla h|}=\dfrac{1}{\sqrt5}\langle-1,-2\rangle$, 그 방향의 기울기(최대 변화율)는 $|\nabla h|=\sqrt{20}=2\sqrt5$.",
            ]),
            ("b", [
                r"$D_{\mathbf u}h=\nabla h\cdot\mathbf u=0 \Leftrightarrow \mathbf u\perp\langle-2,-4\rangle$ → $\mathbf u=\pm\dfrac{1}{\sqrt5}\langle2,-1\rangle$.",
                r"이 방향이 등위곡선 $h=1$, 즉 $x^2+2y^2=3$ 의 접선 방향이에요. 접선: $-2(x-1)-4(y-1)=0 \Rightarrow x+2y=3$.",
            ]),
            ("c", [
                r"$\mathbf u=\langle a,b\rangle$, $a^2+b^2=1$, $-2a-4b=2 \Rightarrow a=-1-2b$.",
                r"대입: $(1+2b)^2+b^2=1 \Rightarrow 5b^2+4b=0 \Rightarrow b=0$ 또는 $b=-\frac45$.",
                r"$\mathbf u=\langle-1,0\rangle$ 또는 $\big\langle\frac35,-\frac45\big\rangle$. (최대 기울기 $2\sqrt5\approx4.47$ 보다 작은 값이라 두 방향이 나와요.)",
            ]),
        ],
    },
]

EXTRA = [
    {
        "id": "x1", "no": "추가 1", "type": "14.7 극값과 안장점", "ref": "2025 중간 2(a)",
        "stem": r"$f(x,y)=2x^3+xy^2+5x^2+y^2$ 의 극댓값, 극솟값, 안장점을 모두 구하시오.",
        "parts": [],
        "answer": [("", r"극솟값 $0$ $(0,0)$, 극댓값 $\dfrac{125}{27}$ $\big(-\frac53,0\big)$, 안장점 $(-1,2),\ (-1,-2)$")],
        "solution": [("", [
            r"$f_x=6x^2+y^2+10x=0$, $\ f_y=2xy+2y=2y(x+1)=0$.",
            r"$y=0$: $6x^2+10x=0 \Rightarrow x=0,\ -\frac53$. $\ x=-1$: $6+y^2-10=0 \Rightarrow y=\pm2$. 임계점 $(0,0),\ \big(-\frac53,0\big),\ (-1,\pm2)$.",
            r"$f_{xx}=12x+10,\ f_{yy}=2x+2,\ f_{xy}=2y$, $\ D=f_{xx}f_{yy}-f_{xy}^2$.",
            r"$(0,0)$: $D=20>0,\ f_{xx}=10>0$ → 극솟값 $0$. $\big(-\frac53,0\big)$: $f_{xx}=-10,\ f_{yy}=-\frac43$, $D=\frac{40}{3}>0$ → 극댓값 $\frac{125}{27}$.",
            r"$(-1,\pm2)$: $f_{xx}=-2,\ f_{yy}=0,\ f_{xy}=\pm4$, $D=-16<0$ → 안장점.",
        ])],
    },
    {
        "id": "x2", "no": "추가 2", "type": "14.7 닫힌 영역에서의 최댓값·최솟값", "ref": "2025 중간 7번",
        "stem": r"$f(x,y)=x^2+2y^2-2x$ 의 원판 $D=\{(x,y)\mid x^2+y^2\le4\}$ 위에서의 최댓값과 최솟값을 구하시오.",
        "parts": [],
        "answer": [("", r"최댓값 $9$ $\big((-1,\pm\sqrt3)\big)$, 최솟값 $-1$ $\big((1,0)\big)$")],
        "solution": [("", [
            r"내부 임계점: $f_x=2x-2=0,\ f_y=4y=0$ → $(1,0)$, $f(1,0)=-1$.",
            r"경계 $x^2+y^2=4$: $y^2=4-x^2$ 대입 → $f=x^2+2(4-x^2)-2x=8-x^2-2x$, $\ -2\le x\le2$.",
            r"$\frac{d}{dx}(8-x^2-2x)=-2x-2=0 \Rightarrow x=-1$: $f=9$ (점 $(-1,\pm\sqrt3)$). 끝점 $x=2$: $f=0$, $\ x=-2$: $f=8$.",
            r"비교하면 최댓값 $9$, 최솟값 $-1$. (경계는 라그랑주 승수법으로 풀어도 같아요.)",
        ])],
    },
    {
        "id": "x3", "no": "추가 3", "type": "14.5 연쇄법칙 (2계 편도함수)", "ref": "2025 중간 5번",
        "stem": r"$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=s^2-t^2,\ y=2st$ 일 때",
        "parts": [
            ("a", r"$z_s,\ z_t$ 를 $f_x,\ f_y$ 로 나타내시오."),
            ("b", r"$z_{ss}+z_{tt}=4(s^2+t^2)\,(f_{xx}+f_{yy})$ 임을 보이시오."),
            ("c", r"$f_{xx}(0,2)=3,\ f_{yy}(0,2)=2$ 일 때 $(s,t)=(1,1)$ 에서 $z_{ss}+z_{tt}$ 의 값을 구하시오."),
        ],
        "answer": [("a", r"$z_s=2s\,f_x+2t\,f_y$, $\ z_t=-2t\,f_x+2s\,f_y$"), ("b", "아래 풀이"), ("c", r"$40$")],
        "solution": [
            ("a", [r"$z_s=f_x\cdot x_s+f_y\cdot y_s=2s\,f_x+2t\,f_y$, $\ z_t=f_x\cdot x_t+f_y\cdot y_t=-2t\,f_x+2s\,f_y$."]),
            ("b", [
                r"$f_x,\ f_y$ 도 $s,t$ 의 함수라 연쇄법칙을 한 번 더: $(f_x)_s=2s\,f_{xx}+2t\,f_{xy}$, $\ (f_y)_s=2s\,f_{xy}+2t\,f_{yy}$.",
                r"$z_{ss}=2f_x+2s(2sf_{xx}+2tf_{xy})+2t(2sf_{xy}+2tf_{yy})=2f_x+4s^2f_{xx}+8st\,f_{xy}+4t^2f_{yy}$.",
                r"같은 방법으로 $z_{tt}=-2f_x+4t^2f_{xx}-8st\,f_{xy}+4s^2f_{yy}$.",
                r"더하면 $f_x$, $f_{xy}$ 항이 지워져 $z_{ss}+z_{tt}=4(s^2+t^2)(f_{xx}+f_{yy})$.",
            ]),
            ("c", [r"$(s,t)=(1,1)$ 이면 $(x,y)=(0,2)$. $\ 4\cdot(1+1)\cdot(3+2)=40$."]),
        ],
    },
    {
        "id": "x4", "no": "추가 4", "type": "14.4–14.6 음함수 미분과 선형근사", "ref": "2025 중간 6번",
        "stem": r"방정식 $x^2z+yz^2=2$ 가 점 $(1,1,1)$ 근처에서 $z=z(x,y)$ 를 정한다.",
        "parts": [
            ("a", r"$z_x(1,1),\ z_y(1,1)$ 을 구하시오."),
            ("b", r"점 $(1,1,1)$ 에서 이 곡면의 접평면을 구하시오."),
            ("c", r"선형근사로 $z(1.06,\ 0.97)$ 의 근삿값을 구하시오."),
            ("d", r"$(1,1)$ 에서 $\langle3,4\rangle$ 방향으로의 $z$의 변화율을 구하시오."),
        ],
        "answer": [("a", r"$-\dfrac23,\ -\dfrac13$"), ("b", r"$2x+y+3z=6$"), ("c", r"$0.97$"), ("d", r"$-\dfrac23$")],
        "solution": [
            ("a", [
                r"$F=x^2z+yz^2-2$: $F_x=2xz,\ F_y=z^2,\ F_z=x^2+2yz$ → $(1,1,1)$ 에서 $2,\ 1,\ 3$.",
                r"$z_x=-\dfrac{F_x}{F_z}=-\dfrac23$, $\ z_y=-\dfrac{F_y}{F_z}=-\dfrac13$.",
            ]),
            ("b", [r"$\nabla F(1,1,1)=\langle2,1,3\rangle$ → $2(x-1)+(y-1)+3(z-1)=0 \Rightarrow 2x+y+3z=6$."]),
            ("c", [r"$z\approx1-\frac23(x-1)-\frac13(y-1)$ → $z(1.06,0.97)\approx1-\frac23(0.06)-\frac13(-0.03)=1-0.04+0.01=0.97$."]),
            ("d", [r"$\mathbf u=\big\langle\frac35,\frac45\big\rangle$: $D_{\mathbf u}z=-\frac23\cdot\frac35-\frac13\cdot\frac45=-\frac25-\frac{4}{15}=-\frac23$."]),
        ],
    },
    {
        "id": "x5", "no": "추가 5", "type": "12–13장 직선과 벡터함수", "ref": "2025 시험엔 없지만 우리 범위",
        "stem": "",
        "parts": [
            ("a", r"두 직선 $L_1:\ x=1+t,\ y=t,\ z=-1$ 과 $L_2:\ x=0,\ y=2+s,\ z=1+s$ 가 꼬인 위치에 있음을 보이고, 두 직선 사이의 거리를 구하시오."),
            ("b", r"$\mathbf r(t)=\big\langle t,\ t^2,\ \frac23t^3\big\rangle$ 의 $0\le t\le1$ 부분의 길이와 $t=1$ 에서의 단위접선벡터를 구하시오."),
        ],
        "answer": [("a", r"거리 $\dfrac{\sqrt3}{3}$"), ("b", r"길이 $\dfrac53$, $\ \mathbf T(1)=\frac13\langle1,2,2\rangle$")],
        "solution": [
            ("a", [
                r"방향 $\mathbf v_1=\langle1,1,0\rangle,\ \mathbf v_2=\langle0,1,1\rangle$ 은 평행하지 않아요.",
                r"만나는지: $1+t=0,\ t=2+s,\ -1=1+s$. 앞의 두 식에서 $t=-1,\ s=-3$ 인데 셋째 식은 $s=-2$ → 모순이라 꼬인 위치.",
                r"$\mathbf n=\mathbf v_1\times\mathbf v_2=\langle1,-1,1\rangle$, $P_1=(1,0,-1),\ P_2=(0,2,1)$: $$d=\frac{|\mathbf n\cdot\overrightarrow{P_1P_2}|}{|\mathbf n|}=\frac{|-1-2+2|}{\sqrt3}=\frac{\sqrt3}{3}$$",
            ]),
            ("b", [
                r"$\mathbf r'(t)=\langle1,2t,2t^2\rangle$, $|\mathbf r'(t)|=\sqrt{1+4t^2+4t^4}=1+2t^2$.",
                r"$L=\displaystyle\int_0^1(1+2t^2)\,dt=\frac53$, $\quad\mathbf T(1)=\dfrac{\mathbf r'(1)}{|\mathbf r'(1)|}=\frac13\langle1,2,2\rangle$.",
            ]),
        ],
    },
]

# 2025 중간고사 문항 ↔ 단원 ↔ 예상 목록 ↔ 이 시험지
MAP_MID = [
    ("1", r"두 원 사이 판의 질량중심 (밀도 $\sqrt{x^2+y^2}$)", "15.4 · 15.3", "1 (계산 방식)", "1번 · 질량중심 자체는 범위 밖", "q1"),
    ("2(a)", "극값과 안장점", "14.7", "", "추가 1", "x1"),
    ("2(b)", "적분 세 개의 합 → 극좌표", "15.3", "5", "5(b)", "q5"),
    ("3", "극한 (조임정리, 곡선 경로 $x-1=ky^2$)", "14.2", "2", "2번", "q2"),
    ("4", "원주좌표 삼중적분", "15.7", "6", "6(b)", "q6"),
    ("5", "2계 연쇄법칙", "14.5", "", "추가 3", "x3"),
    ("6", "음함수의 접평면 → 방향 변화율, 선형근사", "14.4–14.6", "3 · 7 일부", "추가 4", "x4"),
    ("7", "심장형 영역에서 최댓값·최솟값", "14.7", "", "추가 2", "x2"),
    ("8", "교선 위 라그랑주 (제약 2개)", "14.8", "4", "4(b)", "q4"),
    ("9", r"삼중적분 순서 바꾸기 ($e^{z^2}$)", "15.6", "6", "6(d)", "q6"),
    ("10", "원주좌표 → 구면좌표 변환", "15.8", "6", "6(c)", "q6"),
]


def check_all():
    """모든 정답을 sympy(일부는 mpmath 수치 적분)로 다시 계산. 실패한 항목 목록을 돌려줘요."""
    import mpmath as mp
    import sympy as sp
    from sympy import pi, sqrt, sin, cos, exp, log, E, Rational as R, integrate, simplify, diff, symbols, Matrix

    x, y, z, t, s, r, th, ph, rho, u, k, m = symbols('x y z t s r theta phi rho u k m', real=True)
    results = []

    def check(name, got, want):
        if isinstance(got, (tuple, list, bool)) or isinstance(want, bool):
            ok = bool(got == want)
        else:
            ok = simplify(sp.nsimplify(got) - want) == 0
        results.append((name, ok, got, want))

    # ── 1. 극좌표 이중적분 (장미곡선)
    I1a = integrate(integrate(r * r, (r, 0, sin(3 * th))), (th, 0, pi / 3))
    check('1a', I1a, R(4, 27))
    A1b = 4 * integrate(integrate(r, (r, 1, 2 * cos(2 * th))), (th, -pi / 6, pi / 6))
    check('1b', A1b, 2 * pi / 3 + sqrt(3))
    # 교점 확인 2cos2θ=1 at θ=π/6
    check('1b-intersection', 2 * cos(2 * pi / 6), 1)

    # ── 2. 극한
    f2a = x**2 * y**3 / (x**4 + y**4)
    # 극좌표로 r→0 이면 0 (상계 |y|/2)
    check('2a-bound', simplify((x**4 + y**4 - 2 * x**2 * y**2) - (x**2 - y**2)**2), 0)
    check('2a-polar', sp.limit(f2a.subs({x: r * cos(th), y: r * sin(th)}).subs(th, pi / 7), r, 0), 0)
    f2b = sin(x * y**2) / (x**2 + y**4)
    path = sp.limit(f2b.subs(x, k * y**2), y, 0)
    check('2b-path', simplify(path - k / (k**2 + 1)), 0)
    check('2b-line', sp.limit(f2b.subs(y, m * x), x, 0), 0)

    # ── 3. 접평면·법선
    F3 = x**2 + 2 * y**2 + z**2 + x * z
    P3 = {x: 1, y: -1, z: 2}
    check('3-onS', F3.subs(P3), 9)
    g3 = Matrix([diff(F3, v) for v in (x, y, z)]).subs(P3)
    check('3a-grad', tuple(g3), (4, -4, 5))
    check('3a-plane-const', 4 * 1 - 4 * (-1) + 5 * 2, 18)
    # (b) 수평 접평면: Fx=Fy=0
    sol3b = sp.solve([diff(F3, x), diff(F3, y), F3 - 9], [x, y, z], dict=True)
    pts3b = sorted([(s_[x], s_[y], s_[z]) for s_ in sol3b], key=lambda p: float(p[0]))
    check('3b', pts3b, [(-sqrt(3), 0, 2 * sqrt(3)), (sqrt(3), 0, -2 * sqrt(3))])
    # (c) 교선 접선 방향 = ∇F × <1,1,1>
    d3c = g3.cross(Matrix([1, 1, 1]))
    check('3c-dir', tuple(d3c), (-9, 1, 8))
    check('3c-onplane', 1 + (-1) + 2, 2)

    # ── 4. 라그랑주
    lam, mu = symbols('lambda mu', real=True)
    sol4a = sp.solve([y - lam * x / 4, x - lam * y, x**2 / 8 + y**2 / 2 - 1], [x, y, lam], dict=True)
    vals4a = sorted(set(sp.nsimplify(s_[x] * s_[y]) for s_ in sol4a))
    check('4a', vals4a, [-2, 2])
    f4 = 3 * x - y - 3 * z
    sol4b = sp.solve([3 - lam - 2 * mu * x, -1 - lam, -3 + lam - 4 * mu * z, x + y - z, x**2 + 2 * z**2 - 1], [x, y, z, lam, mu], dict=True)
    vals4b = sorted(set(simplify(f4.subs(s_)) for s_ in sol4b), key=float)
    check('4b', vals4b, [-2 * sqrt(6), 2 * sqrt(6)])
    pmax = [s_ for s_ in sol4b if simplify(f4.subs(s_) - 2 * sqrt(6)) == 0][0]
    check('4b-point', (simplify(pmax[x]), simplify(pmax[y]), simplify(pmax[z])), (sqrt(6) / 3, -sqrt(6) / 2, -sqrt(6) / 6))

    # ── 5. 이중적분
    I5a = integrate(integrate(1 / (y**3 + 1), (x, 0, y**2)), (y, 0, 2))
    check('5a', I5a, R(2, 3) * log(3))
    I5b_cart = integrate(integrate(x * y, (y, sqrt(1 - x**2), sqrt(4 - x**2))), (x, 0, 1)) + integrate(integrate(x * y, (y, 0, sqrt(4 - x**2))), (x, 1, 2))
    I5b_pol = integrate(integrate(r * cos(th) * r * sin(th) * r, (r, 1, 2)), (th, 0, pi / 2))
    check('5b-cart', I5b_cart, R(15, 8))
    check('5b-polar', I5b_pol, R(15, 8))
    I5c = integrate(integrate(r * cos(th) * r, (r, 0, 1 + cos(th))), (th, 0, 2 * pi))
    check('5c', I5c, 5 * pi / 4)
    # 심장형 영역 확인: r^2 <= r + r cos θ  <=>  r <= 1 + cos θ
    I5d = integrate(integrate(x * y, (x, y**2 / 2, y + 4)), (y, -2, 4))
    check('5d', I5d, 90)
    check('5d-intersections', sp.solve(y**2 - 2 * (y + 4), y), [-2, 4])

    # ── 6. 삼중적분
    I6a = integrate(integrate(integrate(6 * x * y, (z, 0, 1 + x + y)), (y, 0, sqrt(x))), (x, 0, 1))
    check('6a', I6a, R(65, 28))
    I6b = integrate(integrate(integrate(z * r, (z, r**2, 4)), (r, 0, 2)), (th, 0, 2 * pi))
    check('6b', I6b, 64 * pi / 3)
    I6c_cyl = 2 * mp.pi * mp.quad(lambda rr: mp.quad(lambda zz: rr * mp.sqrt(rr**2 + zz**2), [rr, mp.sqrt(4 - rr**2)]), [0, mp.sqrt(2)])
    I6c_sph = integrate(integrate(integrate(rho * rho**2 * sin(ph), (rho, 0, 2)), (ph, 0, pi / 4)), (th, 0, 2 * pi))
    check('6c-sph', I6c_sph, 4 * pi * (2 - sqrt(2)))
    check('6c-cyl-num', abs(float(I6c_cyl) - float(sp.N(4 * pi * (2 - sqrt(2))))) < 1e-9, True)
    # (d) 바꾼 순서: z∈[0,1], x∈[0,z], y∈[0,x]
    I6d = integrate(integrate(integrate(6 * exp(z**3), (y, 0, x)), (x, 0, z)), (z, 0, 1))
    check('6d', I6d, E - 1)

    # ── 7. 방향미분계수
    f7 = x * y**2 + y * z + exp(x * z)
    P7 = {x: 0, y: 1, z: 2}
    g7 = Matrix([diff(f7, v) for v in (x, y, z)]).subs(P7)
    check('7a', tuple(g7), (3, 2, 1))
    v7 = Matrix([2, 2, 1])
    check('7b', (g7.dot(v7) / v7.norm()), R(11, 3))
    rt = Matrix([sin(t), 1 + t**2, 2 * exp(t)])
    check('7c-onP', tuple(rt.subs(t, 0)), (0, 1, 2))
    rate = diff(f7.subs({x: rt[0], y: rt[1], z: rt[2]}), t).subs(t, 0)
    check('7c-rate', rate, 5)
    rp = rt.diff(t).subs(t, 0)
    check('7c-Du', g7.dot(rp) / rp.norm(), sqrt(5))

    # ── 8. 선적분의 기본정리
    P8, Q8, R8 = y**2 + 2 * x * z, 2 * x * y + exp(z), x**2 + y * exp(z)
    check('8a-curl', (simplify(diff(P8, y) - diff(Q8, x)), simplify(diff(Q8, z) - diff(R8, y)), simplify(diff(R8, x) - diff(P8, z))), (0, 0, 0))
    f8 = x * y**2 + x**2 * z + y * exp(z)
    check('8a-pot', tuple(simplify(diff(f8, v) - w) for v, w in ((x, P8), (y, Q8), (z, R8))), (0, 0, 0))
    r8 = (cos(pi * t), sin(pi * t / 2), t * exp(t**2 - 1))
    A8, B8 = [tuple(sp.nsimplify(c.subs(t, tv)) for c in r8) for tv in (0, 1)]
    check('8b-ends', (A8, B8), ((1, 0, 0), (-1, 1, 1)))
    I8b = f8.subs(dict(zip((x, y, z), B8))) - f8.subs(dict(zip((x, y, z), A8)))
    check('8b', I8b, E)
    # 직접 매개화로도 확인 (수치)
    integrand = sum(Fc.subs(dict(zip((x, y, z), r8))) * diff(rc, t) for Fc, rc in zip((P8, Q8, R8), r8))
    fi = sp.lambdify(t, integrand, 'mpmath')
    check('8b-numeric', abs(float(mp.quad(fi, [0, 1])) - float(E)) < 1e-10, True)
    G8 = (2 * x * y + 3 * y, x**2 + x)
    xc, yc = cos(t), sin(t)
    I8c = integrate((G8[0] * diff(xc, t) + G8[1] * diff(yc, t)).subs({x: xc, y: yc}), (t, 0, pi))
    check('8c', I8c, -pi)

    # ── 9. 그린 정리
    Pa, Qa = y**2, 3 * x * y
    green9a = integrate(integrate(diff(Qa, x) - diff(Pa, y), (y, x**2, 1)), (x, -1, 1))
    c1 = integrate((Pa * diff(t, t) + Qa * diff(t**2, t)).subs({x: t, y: t**2}), (t, -1, 1))       # 포물선 (-1,1)→(1,1)
    c2 = integrate((Pa * diff(-t, t) + Qa * 0).subs({x: -t, y: 1}), (t, -1, 1))                   # y=1, (1,1)→(-1,1)
    check('9a-green', green9a, R(4, 5))
    check('9a-direct', c1 + c2, R(4, 5))
    check('9a-pieces', (c1, c2), (R(14, 5), -2))
    Pb, Qb = x**2 - y**3, x**3 + exp(y**2)
    green9b = integrate(integrate((diff(Qb, x) - diff(Pb, y)).subs({x: r * cos(th), y: r * sin(th)}) * r, (r, 0, 2)), (th, 0, pi))
    seg9b = integrate(Pb.subs(y, 0), (x, -2, 2))
    check('9b-green', green9b, 12 * pi)
    check('9b-seg', seg9b, R(16, 3))
    check('9b', green9b - seg9b, 12 * pi - R(16, 3))
    # 직접 계산(수치)으로도 확인: 반원 (2cos t, 2 sin t), t: 0→π
    xb, yb = 2 * cos(t), 2 * sin(t)
    direct9b = mp.quad(sp.lambdify(t, (Pb * diff(xb, t) + Qb * diff(yb, t)).subs({x: xb, y: yb}), 'mpmath'), [0, mp.pi])
    check('9b-numeric', abs(float(direct9b) - float(12 * pi - R(16, 3))) < 1e-10, True)
    Pc, Qc = -y / (x**2 + y**2), x / (x**2 + y**2)
    check('9c-curlfree', simplify(diff(Qc, x) - diff(Pc, y)), 0)
    # 삼각형 세 변을 수치 적분 (반시계: (-1,-1)→(2,-1)→(-1,2)→(-1,-1))
    V = [(-1, -1), (2, -1), (-1, 2), (-1, -1)]
    tot = 0
    for (x0, y0), (x1, y1) in zip(V, V[1:]):
        xs, ys = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        tot += mp.quad(sp.lambdify(t, (Pc * (x1 - x0) + Qc * (y1 - y0)).subs({x: xs, y: ys}), 'mpmath'), [0, 1])
    check('9c', abs(float(tot) - float(2 * pi)) < 1e-10, True)

    # ── 10. 최대 증가 방향
    h = 4 - x**2 - 2 * y**2
    gh = Matrix([diff(h, x), diff(h, y)]).subs({x: 1, y: 1})
    check('10a-grad', tuple(gh), (-2, -4))
    check('10a-rate', gh.norm(), 2 * sqrt(5))
    check('10b-perp', gh.dot(Matrix([2, -1])), 0)
    a_, b_ = symbols('a b', real=True)
    sol10c = sp.solve([gh[0] * a_ + gh[1] * b_ - 2, a_**2 + b_**2 - 1], [a_, b_], dict=True)
    check('10c', sorted([(s_[a_], s_[b_]) for s_ in sol10c], key=lambda p: float(p[0])), [(-1, 0), (R(3, 5), R(-4, 5))])

    # ── 추가 1. 극값·안장점
    fB1 = 2 * x**3 + x * y**2 + 5 * x**2 + y**2
    crit = sp.solve([diff(fB1, x), diff(fB1, y)], [x, y], dict=True)
    cls = []
    for c_ in crit:
        fxx, fyy, fxy = [diff(fB1, *d).subs(c_) for d in ((x, x), (y, y), (x, y))]
        D = fxx * fyy - fxy**2
        kind = 'saddle' if D < 0 else ('min' if fxx > 0 else 'max') if D > 0 else '?'
        cls.append((c_[x], c_[y], kind, fB1.subs(c_)))
    cls.sort(key=lambda q: (float(q[0]), float(q[1])))
    check('B1', cls, [(R(-5, 3), 0, 'max', R(125, 27)), (-1, -2, 'saddle', 3), (-1, 2, 'saddle', 3), (0, 0, 'min', 0)])

    # ── 추가 2. 원판 위 최대·최소
    fB2 = x**2 + 2 * y**2 - 2 * x
    check('B2-crit', sp.solve([diff(fB2, x), diff(fB2, y)], [x, y], dict=True), [{x: 1, y: 0}])
    cb = symbols('c', real=True)
    gB2 = fB2.subs({x: 2 * cb, y: sqrt(4 - 4 * cb**2)})
    cands = [fB2.subs({x: 1, y: 0})] + [simplify(gB2.subs(cb, c0)) for c0 in sp.solve(diff(gB2, cb), cb) + [-1, 1]]
    check('B2', (max(cands), min(cands)), (9, -1))
    check('B2-maxpt', fB2.subs({x: -1, y: sqrt(3)}), 9)

    # ── 추가 3. 2계 연쇄법칙
    X, Y = s**2 - t**2, 2 * s * t
    # f_xx + f_yy 로 정리되는지: 다항식 f = x^3 + x y^2 + 5y^2 등 시험 함수 몇 개로 확인
    for test in (x**3 * y - y**3, sp.exp(x) * sp.sin(y), x**4 + x**2 * y**2):
        zz = test.subs({x: X, y: Y})
        lhs = simplify(diff(zz, s, 2) + diff(zz, t, 2))
        rhs = simplify(4 * (s**2 + t**2) * (diff(test, x, 2) + diff(test, y, 2)).subs({x: X, y: Y}))
        check('B3-identity', simplify(lhs - rhs), 0)
    check('B3c', 4 * (1 + 1) * (3 + 2), 40)
    check('B3-point', (X.subs({s: 1, t: 1}), Y.subs({s: 1, t: 1})), (0, 2))

    # ── 추가 4. 음함수, 선형근사
    FB4 = x**2 * z + y * z**2 - 2
    P4 = {x: 1, y: 1, z: 1}
    zx = (-diff(FB4, x) / diff(FB4, z)).subs(P4)
    zy = (-diff(FB4, y) / diff(FB4, z)).subs(P4)
    check('B4a', (zx, zy), (R(-2, 3), R(-1, 3)))
    check('B4c', 1 + zx * R(6, 100) + zy * R(-3, 100), R(97, 100))
    check('B4d', zx * R(3, 5) + zy * R(4, 5), R(-2, 3))
    exact = [sv for sv in sp.solve(FB4.subs({x: R(106, 100), y: R(97, 100)}), z) if sv > 0][0]
    check('B4c-actual~', abs(float(exact) - 0.97) < 0.002, True)

    # ── 추가 5. 꼬인 직선 거리, 호의 길이
    v1, v2 = Matrix([1, 1, 0]), Matrix([0, 1, 1])
    P1, P2 = Matrix([1, 0, -1]), Matrix([0, 2, 1])
    nB5 = v1.cross(v2)
    check('B5a-n', tuple(nB5), (1, -1, 1))
    check('B5a', abs(nB5.dot(P2 - P1)) / nB5.norm(), sqrt(3) / 3)
    check('B5a-noint', sp.solve([1 + t - 0, t - (2 + s), -1 - (1 + s)], [t, s], dict=True), [])
    rB5 = Matrix([t, t**2, R(2, 3) * t**3])
    speed = simplify(rB5.diff(t).norm())
    check('B5b-speed', sp.expand(speed**2 - (1 + 2 * t**2)**2), 0)  # 제곱끼리 비교 (sympy가 근호를 못 벗김)
    check('B5b', integrate(1 + 2 * t**2, (t, 0, 1)), R(5, 3))
    T1 = rB5.diff(t).subs(t, 1) / rB5.diff(t).subs(t, 1).norm()
    check('B5b-T', tuple(T1), (R(1, 3), R(2, 3), R(2, 3)))

    return results

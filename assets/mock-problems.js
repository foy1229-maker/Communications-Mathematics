/* 자동 생성 파일 — tools/mock.py 를 고친 뒤 tools/build.py 로 다시 만드세요. */
window.CM_MOCK = {
 "exam": [
  {
   "id": "q1",
   "no": "1",
   "type": "예상 유형 1 · 극좌표 이중적분 (장미곡선)",
   "ref": "2025 중간 1번과 같은 계산 방식",
   "stem": "",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$D$가</span> 장미곡선 $r=\\sin 3\\theta$ 의 한 꽃잎 $\\left(0\\le\\theta\\le\\frac{\\pi}{3}\\right)$ 으로 둘러싸인 영역일 때, $\\displaystyle\\iint_D \\sqrt{x^2+y^2}\\,dA$ 를 구하시오."
    ],
    [
     "b",
     "장미곡선 $r=2\\cos 2\\theta$ 의 내부이면서 원 $r=1$ 의 외부인 영역의 넓이를 이중적분으로 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$\\dfrac{4}{27}$"
    ],
    [
     "b",
     "$\\dfrac{2\\pi}{3}+\\sqrt3$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "극좌표에서 <span class=\"nw\">$\\sqrt{x^2+y^2}=r$,</span> <span class=\"nw\">$dA=r\\,dr\\,d\\theta$.</span> 꽃잎 하나는 $0\\le\\theta\\le\\frac{\\pi}{3}\\text{,}$ $0\\le r\\le\\sin3\\theta$ 예요.",
      "$$\\begin{aligned}&amp;\\iint_D\\sqrt{x^2+y^2}\\,dA\\\\&amp;=\\int_0^{\\pi/3}\\!\\!\\int_0^{\\sin3\\theta} r^2\\,dr\\,d\\theta\\\\&amp;=\\frac13\\int_0^{\\pi/3}\\sin^3 3\\theta\\,d\\theta\\end{aligned}$$",
      "$u=3\\theta$ 로 치환하면 $$\\begin{aligned}&amp;\\frac19\\int_0^{\\pi}\\sin^3u\\,du\\\\&amp;=\\frac19\\Big[-\\cos u+\\frac{\\cos^3u}{3}\\Big]_0^{\\pi}\\\\&amp;=\\frac19\\cdot\\frac43=\\frac{4}{27}\\end{aligned}$$"
     ]
    ],
    [
     "b",
     [
      "교점: $2\\cos2\\theta=1 \\Rightarrow \\theta=\\pm\\frac{\\pi}{6}$ ($\\theta=0$ 방향 꽃잎). 꽃잎 네 개가 합동이라 한 꽃잎에서 원 바깥 부분을 구해 4배 해요.",
      "$$\\begin{aligned}A&amp;=4\\int_{-\\pi/6}^{\\pi/6}\\!\\!\\int_1^{2\\cos2\\theta} r\\,dr\\,d\\theta\\\\&amp;=2\\int_{-\\pi/6}^{\\pi/6}\\big(4\\cos^2 2\\theta-1\\big)\\,d\\theta\\end{aligned}$$",
      "$4\\cos^22\\theta-1=1+2\\cos4\\theta$ 이므로 $$\\begin{aligned}A&amp;=2\\Big[\\theta+\\tfrac12\\sin4\\theta\\Big]_{-\\pi/6}^{\\pi/6}\\\\&amp;=2\\Big(\\frac{\\pi}{3}+\\frac{\\sqrt3}{2}\\Big)=\\frac{2\\pi}{3}+\\sqrt3\\end{aligned}$$"
     ]
    ]
   ]
  },
  {
   "id": "q2",
   "no": "2",
   "type": "예상 유형 2 · 극한과 연속",
   "ref": "2025 중간 3번",
   "stem": "다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
   "parts": [
    [
     "a",
     "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^2y^3}{x^4+y^4}$"
    ],
    [
     "b",
     "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{\\sin(xy^2)}{x^2+y^4}$"
    ],
    [
     "c",
     "$g(x,y)=\\dfrac{\\sin(xy^2)}{x^2+y^4}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $g(0,0)=0$ 일 때, <span class=\"nw\">$g$가</span> 연속인 점의 집합을 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$0$"
    ],
    [
     "b",
     "존재하지 않음 (곡선 $x=ky^2$ 를 따라 <span class=\"nw\">$\\frac{k}{k^2+1}$)</span>"
    ],
    [
     "c",
     "원점을 뺀 모든 점 $\\{(x,y)\\mid (x,y)\\ne(0,0)\\}$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$x^4+y^4-2x^2y^2=(x^2-y^2)^2\\ge0$ 이므로 $\\dfrac{x^2y^2}{x^4+y^4}\\le\\dfrac12\\text{.}$",
      "$$\\left|\\frac{x^2y^3}{x^4+y^4}\\right|=|y|\\cdot\\frac{x^2y^2}{x^4+y^4}\\le\\frac{|y|}{2}\\to0$$ 조임정리로 극한은 <span class=\"nw\">$0$.</span>"
     ]
    ],
    [
     "b",
     [
      "직선 $y=mx$ 를 따라가면 모두 $0$ 이라 판정이 안 돼요. 분모의 $x^2$ 와 $y^4$ 의 차수가 같아지도록 곡선 $x=ky^2$ 를 써요.",
      "대입하면 $$\\begin{aligned}&amp;\\frac{\\sin(ky^4)}{(k^2+1)\\,y^4}\\\\&amp;=\\frac{\\sin(ky^4)}{ky^4}\\cdot\\frac{k}{k^2+1}\\\\&amp;\\longrightarrow\\ \\frac{k}{k^2+1}\\quad(y\\to0,\\ k\\ne0)\\end{aligned}$$",
      "$k=0$ (즉 <span class=\"nw\">$x=0$)</span> 이면 <span class=\"nw\">$0$,</span> $k=1$ 이면 <span class=\"nw\">$\\frac12$.</span> 경로마다 값이 다르므로 극한은 존재하지 않아요."
     ]
    ],
    [
     "c",
     [
      "$(x,y)\\ne(0,0)$ 이면 분모 $x^2+y^4>0$ 이고 분자·분모가 연속이므로 <span class=\"nw\">$g$는</span> 연속이에요.",
      "원점에서는 (b)에서 $\\lim g$ 가 존재하지 않으므로 불연속. 연속인 점의 집합은 원점을 뺀 평면 전체예요."
     ]
    ]
   ]
  },
  {
   "id": "q3",
   "no": "3",
   "type": "예상 유형 3 · 등위곡면의 접평면과 법선",
   "ref": "2025 중간 6번 일부",
   "stem": "곡면 $S:\\ x^2+2y^2+z^2+xz=9$ 위의 점 $P(1,-1,2)$ 에 대하여",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$P$에서</span> <span class=\"nw\">$S$의</span> 접평면과 법선의 방정식을 구하시오."
    ],
    [
     "b",
     "접평면이 <span class=\"nw\">$xy$평면과</span> 평행한 $S$ 위의 점을 모두 구하시오."
    ],
    [
     "c",
     "<span class=\"nw\">$S$와</span> 평면 $x+y+z=2$ 의 교선을 <span class=\"nw\">$C$라</span> 할 때, <span class=\"nw\">$P$에서</span> <span class=\"nw\">$C$의</span> 접선의 매개방정식을 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "접평면 <span class=\"nw\">$4x-4y+5z=18$,</span> 법선 $\\dfrac{x-1}{4}=\\dfrac{y+1}{-4}=\\dfrac{z-2}{5}$"
    ],
    [
     "b",
     "$(\\sqrt3,\\,0,\\,-2\\sqrt3)\\text{,}$ $(-\\sqrt3,\\,0,\\,2\\sqrt3)$"
    ],
    [
     "c",
     "$x=1-9t,\\ y=-1+t,\\ z=2+8t$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$F=x^2+2y^2+z^2+xz$ 라 두면 <span class=\"nw\">$S$는</span> 등위곡면 <span class=\"nw\">$F=9$.</span> $\\nabla F=\\langle 2x+z,\\ 4y,\\ 2z+x\\rangle\\text{,}$ $\\nabla F(1,-1,2)=\\langle4,-4,5\\rangle\\text{.}$",
      "접평면: $4(x-1)-4(y+1)+5(z-2)=0 \\Rightarrow 4x-4y+5z=18\\text{.}$",
      "법선: $x=1+4t,\\ y=-1-4t,\\ z=2+5t\\text{,}$ 대칭방정식으로 $\\dfrac{x-1}{4}=\\dfrac{y+1}{-4}=\\dfrac{z-2}{5}\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "접평면이 <span class=\"nw\">$xy$평면과</span> 평행 $\\Leftrightarrow$ 법선벡터 $\\nabla F$ 가 $\\mathbf k$ 와 평행 $\\Leftrightarrow$ <span class=\"nw\">$F_x=F_y=0$:</span> <span class=\"nw\">$2x+z=0,\\ 4y=0$.</span>",
      "$y=0,\\ z=-2x$ 를 <span class=\"nw\">$S$에</span> 대입: $x^2+4x^2-2x^2=3x^2=9 \\Rightarrow x=\\pm\\sqrt3\\text{.}$",
      "점 $(\\sqrt3,0,-2\\sqrt3)\\text{,}$ $(-\\sqrt3,0,2\\sqrt3)\\text{.}$ 이때 $F_z=-3x\\ne0$ 이라 법선이 실제로 $\\mathbf k$ 방향이에요."
     ]
    ],
    [
     "c",
     [
      "<span class=\"nw\">$P$가</span> 평면 위에 있는지 확인: <span class=\"nw\">$1-1+2=2$.</span> <span class=\"nw\">$C$는</span> 두 곡면 위에 있으므로 접선은 두 법선 $\\langle4,-4,5\\rangle\\text{,}$ $\\langle1,1,1\\rangle$ 에 모두 수직이에요.",
      "방향벡터: $$\\langle4,-4,5\\rangle\\times\\langle1,1,1\\rangle=\\langle -9,\\ 1,\\ 8\\rangle$$",
      "접선: $x=1-9t,\\ y=-1+t,\\ z=2+8t\\text{.}$"
     ]
    ]
   ]
  },
  {
   "id": "q4",
   "no": "4",
   "type": "예상 유형 4 · 라그랑주 승수법",
   "ref": "2025 중간 8번",
   "stem": "",
   "parts": [
    [
     "a",
     "타원 $\\dfrac{x^2}{8}+\\dfrac{y^2}{2}=1$ 위에서 $f(x,y)=xy$ 의 최댓값과 최솟값을 구하시오."
    ],
    [
     "b",
     "평면 $x+y-z=0$ 과 곡면 $x^2+2z^2=1$ 의 교선 위에서 $f(x,y,z)=3x-y-3z$ 의 최댓값과 최솟값을 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "최댓값 $2$ $\\big((2,1),(-2,-1)\\big)\\text{,}$ 최솟값 $-2$ $\\big((2,-1),(-2,1)\\big)$"
    ],
    [
     "b",
     "최댓값 $2\\sqrt6$ $\\big(\\big(\\tfrac{\\sqrt6}{3},-\\tfrac{\\sqrt6}{2},-\\tfrac{\\sqrt6}{6}\\big)\\big)\\text{,}$ 최솟값 $-2\\sqrt6$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$g=\\dfrac{x^2}{8}+\\dfrac{y^2}{2}\\text{,}$ $\\nabla f=\\lambda\\nabla g\\text{:}$ $\\ y=\\dfrac{\\lambda x}{4},\\quad x=\\lambda y\\text{.}$",
      "대입하면 $y=\\dfrac{\\lambda^2}{4}y\\text{.}$ $y=0$ 이면 $x=0$ 인데 타원 위의 점이 아니므로 <span class=\"nw\">$\\lambda^2=4$.</span>",
      "<span class=\"nw\">$\\lambda=2$:</span> <span class=\"nw\">$x=2y$,</span> $y^2=1$ → $(2,1),(-2,-1)$ 에서 <span class=\"nw\">$f=2$.</span> <span class=\"nw\">$\\lambda=-2$:</span> $x=-2y$ → $(-2,1),(2,-1)$ 에서 <span class=\"nw\">$f=-2$.</span>",
      "타원은 닫힌 유계 곡선이라 최댓값·최솟값이 존재해요. 최댓값 <span class=\"nw\">$2$,</span> 최솟값 <span class=\"nw\">$-2$.</span>"
     ]
    ],
    [
     "b",
     [
      "<span class=\"nw\">$g=x+y-z=0$,</span> <span class=\"nw\">$h=x^2+2z^2=1$,</span> $\\nabla f=\\lambda\\nabla g+\\mu\\nabla h\\text{:}$ $$\\langle3,-1,-3\\rangle=\\lambda\\langle1,1,-1\\rangle+\\mu\\langle2x,0,4z\\rangle$$",
      "<span class=\"nw\">$y$성분에서</span> <span class=\"nw\">$\\lambda=-1$.</span> 그러면 $3=-1+2\\mu x \\Rightarrow x=\\dfrac{2}{\\mu}\\text{,}$ $\\ -3=1+4\\mu z\\Rightarrow z=-\\dfrac{1}{\\mu}\\text{.}$",
      "$h=1$ 에 대입: $\\dfrac{4}{\\mu^2}+\\dfrac{2}{\\mu^2}=1 \\Rightarrow \\mu=\\pm\\sqrt6\\text{.}$ 또 $y=z-x=-\\dfrac{3}{\\mu}\\text{.}$",
      "$f=3x-y-3z=\\dfrac{6+3+3}{\\mu}=\\dfrac{12}{\\mu}=\\pm2\\sqrt6\\text{.}$ 최댓값 $2\\sqrt6$ (점 $\\big(\\tfrac{\\sqrt6}{3},-\\tfrac{\\sqrt6}{2},-\\tfrac{\\sqrt6}{6}\\big)\\text{),}$ 최솟값 <span class=\"nw\">$-2\\sqrt6$.</span>"
     ]
    ]
   ]
  },
  {
   "id": "q5",
   "no": "5",
   "type": "예상 유형 5 · 이중적분 (순서 바꾸기 · 극좌표 · 심장형)",
   "ref": "2025 중간 2(b), 7번의 영역",
   "stem": "다음을 계산하시오.",
   "parts": [
    [
     "a",
     "(적분 순서를 바꾸어) $\\displaystyle\\int_0^4\\!\\!\\int_{\\sqrt x}^{2}\\frac{1}{y^3+1}\\,dy\\,dx$"
    ],
    [
     "b",
     "(극좌표로 바꾸어) $$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_{\\sqrt{1-x^2}}^{\\sqrt{4-x^2}} xy\\,dy\\,dx\\\\&amp;\\quad+\\int_1^2\\!\\!\\int_0^{\\sqrt{4-x^2}} xy\\,dy\\,dx\\end{aligned}$$"
    ],
    [
     "c",
     "$D=\\{(x,y)\\mid x^2+y^2\\le\\sqrt{x^2+y^2}+x\\}$ 일 때 $\\displaystyle\\iint_D x\\,dA$"
    ],
    [
     "d",
     "직선 $y=x-4$ 와 포물선 $y^2=2x$ 로 둘러싸인 영역 <span class=\"nw\">$D$에서</span> $\\displaystyle\\iint_D xy\\,dA$"
    ]
   ],
   "answer": [
    [
     "a",
     "$\\dfrac23\\ln3$"
    ],
    [
     "b",
     "$\\dfrac{15}{8}$"
    ],
    [
     "c",
     "$\\dfrac{5\\pi}{4}$"
    ],
    [
     "d",
     "$90$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "영역: $0\\le x\\le4,\\ \\sqrt x\\le y\\le2$ $\\Leftrightarrow$ $0\\le y\\le2,\\ 0\\le x\\le y^2\\text{.}$",
      "$$\\begin{aligned}\\int_0^2\\!\\!\\int_0^{y^2}\\frac{1}{y^3+1}\\,dx\\,dy&amp;=\\int_0^2\\frac{y^2}{y^3+1}\\,dy\\\\&amp;=\\frac13\\ln(y^3+1)\\Big|_0^2\\\\&amp;=\\frac13\\ln9=\\frac23\\ln3\\end{aligned}$$"
     ]
    ],
    [
     "b",
     [
      "첫 적분은 원 $x^2+y^2=1$ 과 $x^2+y^2=4$ 사이(<span class=\"nw\">$0\\le x\\le1$),</span> 둘째는 $1\\le x\\le2$ 에서 큰 원 안쪽. 합치면 1사분면 고리 $1\\le r\\le2,\\ 0\\le\\theta\\le\\frac{\\pi}{2}\\text{.}$",
      "$$\\begin{aligned}&amp;\\int_0^{\\pi/2}\\!\\!\\int_1^2 (r\\cos\\theta)(r\\sin\\theta)\\,r\\,dr\\,d\\theta\\\\&amp;=\\int_0^{\\pi/2}\\sin\\theta\\cos\\theta\\,d\\theta\\cdot\\int_1^2 r^3\\,dr\\\\&amp;=\\frac12\\cdot\\frac{15}{4}=\\frac{15}{8}\\end{aligned}$$"
     ]
    ],
    [
     "c",
     [
      "극좌표로 쓰면 $r^2\\le r+r\\cos\\theta \\Leftrightarrow r\\le1+\\cos\\theta\\text{.}$ 심장형 곡선의 내부예요.",
      "$$\\begin{aligned}\\iint_D x\\,dA&amp;=\\int_0^{2\\pi}\\!\\!\\int_0^{1+\\cos\\theta} r^2\\cos\\theta\\,dr\\,d\\theta\\\\&amp;=\\frac13\\int_0^{2\\pi}(1+\\cos\\theta)^3\\cos\\theta\\,d\\theta\\end{aligned}$$",
      "전개하면 $\\cos\\theta+3\\cos^2\\theta+3\\cos^3\\theta+\\cos^4\\theta\\text{.}$ 한 주기 적분은 차례로 $0,\\ 3\\pi,\\ 0,\\ \\frac{3\\pi}{4}$ 이므로 $\\frac13\\cdot\\frac{15\\pi}{4}=\\frac{5\\pi}{4}\\text{.}$"
     ]
    ],
    [
     "d",
     [
      "교점: $y^2=2(y+4) \\Rightarrow y=-2,\\ 4\\text{,}$ 즉 <span class=\"nw\">$(2,-2),(8,4)$.</span> <span class=\"nw\">$x$로</span> 자르면 아래 경계가 바뀌어 두 조각이 되니 $y$ 기준(유형 II)으로 써요: $-2\\le y\\le4,\\ \\frac{y^2}{2}\\le x\\le y+4\\text{.}$",
      "$$\\begin{aligned}&amp;\\int_{-2}^{4}\\!\\!\\int_{y^2/2}^{y+4} xy\\,dx\\,dy\\\\&amp;=\\frac12\\int_{-2}^{4}\\Big(y(y+4)^2-\\frac{y^5}{4}\\Big)dy\\\\&amp;=\\frac12(348-168)=90\\end{aligned}$$"
     ]
    ]
   ]
  },
  {
   "id": "q6",
   "no": "6",
   "type": "예상 유형 6 · 삼중적분 (직교 · 원주 · 구면 · 순서 바꾸기)",
   "ref": "2025 중간 4, 9, 10번",
   "stem": "다음을 계산하시오.",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$E$가</span> 평면 $z=1+x+y$ 아래, <span class=\"nw\">$xy$평면</span> 위에 있고 밑면이 곡선 <span class=\"nw\">$y=\\sqrt x$,</span> <span class=\"nw\">$y=0$,</span> $x=1$ 로 둘러싸인 영역인 입체일 때 $\\displaystyle\\iiint_E 6xy\\,dV$"
    ],
    [
     "b",
     "포물면 $z=x^2+y^2$ 과 평면 $z=4$ 로 둘러싸인 입체 <span class=\"nw\">$E$에서</span> $\\displaystyle\\iiint_E z\\,dV$"
    ],
    [
     "c",
     "다음 적분을 구면좌표로 바꾸어 나타내고 값을 구하시오. $$\\int_0^{2\\pi}\\!\\!\\int_0^{\\sqrt2}\\!\\!\\int_r^{\\sqrt{4-r^2}} r\\sqrt{r^2+z^2}\\,dz\\,dr\\,d\\theta$$"
    ],
    [
     "d",
     "(적분 순서를 바꾸어) $\\displaystyle\\int_0^1\\!\\!\\int_0^x\\!\\!\\int_x^1 6e^{z^3}\\,dz\\,dy\\,dx$"
    ]
   ],
   "answer": [
    [
     "a",
     "$\\dfrac{65}{28}$"
    ],
    [
     "b",
     "$\\dfrac{64\\pi}{3}$"
    ],
    [
     "c",
     "$\\displaystyle\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/4}\\!\\!\\int_0^2 \\rho^3\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta=4\\pi(2-\\sqrt2)$"
    ],
    [
     "d",
     "$e-1$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$E=\\{0\\le x\\le1,\\ 0\\le y\\le\\sqrt x,\\ 0\\le z\\le1+x+y\\}\\text{.}$",
      "$$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^{\\sqrt x} 6xy(1+x+y)\\,dy\\,dx\\\\&amp;=\\int_0^1\\Big[3xy^2(1+x)+2xy^3\\Big]_0^{\\sqrt x}dx\\\\&amp;=\\int_0^1\\big(3x^2+3x^3+2x^{5/2}\\big)dx\\end{aligned}$$",
      "$=1+\\frac34+\\frac47=\\frac{65}{28}\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "원주좌표: 포물면과 평면은 $r=2$ 에서 만나므로 $0\\le\\theta\\le2\\pi,\\ 0\\le r\\le2,\\ r^2\\le z\\le4\\text{.}$",
      "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^2\\!\\!\\int_{r^2}^4 z\\,r\\,dz\\,dr\\,d\\theta\\\\&amp;=2\\pi\\int_0^2\\frac{16-r^4}{2}\\,r\\,dr\\\\&amp;=\\pi\\Big[8r^2-\\frac{r^6}{6}\\Big]_0^2=\\frac{64\\pi}{3}\\end{aligned}$$"
     ]
    ],
    [
     "c",
     [
      "영역 읽기: $z\\ge r$ 는 원뿔 $\\phi\\le\\frac{\\pi}{4}$ 의 위, $z\\le\\sqrt{4-r^2}$ 는 구 $\\rho\\le2$ 의 안쪽, $r\\le\\sqrt2$ 는 둘이 만나는 원이에요.",
      "$r\\,dz\\,dr\\,d\\theta=dV=\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\text{,}$ $\\sqrt{r^2+z^2}=\\rho\\text{:}$ $$\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/4}\\!\\!\\int_0^2 \\rho^3\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$$",
      "$=2\\pi\\cdot\\Big(1-\\frac{\\sqrt2}{2}\\Big)\\cdot\\frac{2^4}{4}=8\\pi\\Big(1-\\frac{\\sqrt2}{2}\\Big)=4\\pi(2-\\sqrt2)\\text{.}$"
     ]
    ],
    [
     "d",
     [
      "$e^{z^3}$ 은 <span class=\"nw\">$z$로</span> 먼저 적분할 수 없어요. 영역: $0\\le x\\le1,\\ 0\\le y\\le x,\\ x\\le z\\le1\\text{.}$",
      "<span class=\"nw\">$z$를</span> 바깥으로: $0\\le z\\le1,\\ 0\\le x\\le z,\\ 0\\le y\\le x\\text{.}$ $$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^z\\!\\!\\int_0^x 6e^{z^3}\\,dy\\,dx\\,dz\\\\&amp;=\\int_0^1 6e^{z^3}\\cdot\\frac{z^2}{2}\\,dz\\\\&amp;=\\Big[e^{z^3}\\Big]_0^1=e-1\\end{aligned}$$"
     ]
    ]
   ]
  },
  {
   "id": "q7",
   "no": "7",
   "type": "예상 유형 7 · 방향미분계수와 그래디언트",
   "ref": "2025 중간 6(a)",
   "stem": "$f(x,y,z)=xy^2+yz+e^{xz}\\text{,}$ $P(0,1,2)$ 일 때",
   "parts": [
    [
     "a",
     "$\\nabla f(P)$ 를 구하시오."
    ],
    [
     "b",
     "<span class=\"nw\">$P$에서</span> 점 $Q(2,3,3)$ 을 향하는 방향으로의 방향미분계수를 구하시오."
    ],
    [
     "c",
     "곡선 $\\mathbf r(t)=\\langle \\sin t,\\ 1+t^2,\\ 2e^{t}\\rangle$ 을 따라 움직이는 입자가 $t=0$ 에서 <span class=\"nw\">$P$를</span> 지난다. 이 순간 $f(\\mathbf r(t))$ 의 변화율과, <span class=\"nw\">$P$에서</span> 곡선의 접선 방향으로의 방향미분계수를 각각 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$\\langle3,\\ 2,\\ 1\\rangle$"
    ],
    [
     "b",
     "$\\dfrac{11}{3}$"
    ],
    [
     "c",
     "변화율 <span class=\"nw\">$5$,</span> 방향미분계수 $\\sqrt5$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$\\nabla f=\\langle y^2+ze^{xz},\\ 2xy+z,\\ y+xe^{xz}\\rangle$ 이므로 $\\nabla f(0,1,2)=\\langle 1+2,\\ 0+2,\\ 1+0\\rangle=\\langle3,2,1\\rangle\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "$\\overrightarrow{PQ}=\\langle2,2,1\\rangle\\text{,}$ $|\\overrightarrow{PQ}|=3\\text{,}$ $\\mathbf u=\\frac13\\langle2,2,1\\rangle$ → $D_{\\mathbf u}f(P)=\\nabla f(P)\\cdot\\mathbf u=\\frac{6+4+1}{3}=\\frac{11}{3}\\text{.}$"
     ]
    ],
    [
     "c",
     [
      "$\\mathbf r(0)=\\langle0,1,2\\rangle=P\\text{,}$ $\\mathbf r'(t)=\\langle\\cos t,\\ 2t,\\ 2e^t\\rangle$ → $\\mathbf r'(0)=\\langle1,0,2\\rangle\\text{.}$",
      "연쇄법칙: $\\dfrac{d}{dt}f(\\mathbf r(t))\\Big|_{t=0}=\\nabla f(P)\\cdot\\mathbf r'(0)=3+0+2=5\\text{.}$",
      "접선 방향 단위벡터 $\\mathbf u=\\frac{1}{\\sqrt5}\\langle1,0,2\\rangle$ → $D_{\\mathbf u}f(P)=\\frac{5}{\\sqrt5}=\\sqrt5\\text{.}$ (변화율 $5$ = 방향미분계수 $\\sqrt5$ × 속력 $|\\mathbf r'(0)|=\\sqrt5\\text{)}$"
     ]
    ]
   ]
  },
  {
   "id": "q8",
   "no": "8",
   "type": "예상 유형 8 · 선적분의 기본정리",
   "ref": "2025 기말 1(a), 4번",
   "stem": "$\\mathbf F(x,y,z)=\\langle y^2+2xz,\\ \\ 2xy+e^{z},\\ \\ x^2+ye^{z}\\rangle$ 일 때",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$\\mathbf F$가</span> 보존장임을 보이고 $\\mathbf F=\\nabla f$ 인 함수 <span class=\"nw\">$f$를</span> 구하시오."
    ],
    [
     "b",
     "$C:\\ \\mathbf r(t)=\\big\\langle \\cos\\pi t,\\ \\sin\\frac{\\pi t}{2},\\ t\\,e^{t^2-1}\\big\\rangle,\\ 0\\le t\\le1$ 일 때 $\\displaystyle\\int_C\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
    ],
    [
     "c",
     "$\\mathbf G(x,y)=\\langle 2xy+3y,\\ x^2+x\\rangle$ 는 보존장이 아니다. <span class=\"nw\">$C$가</span> 원 $x^2+y^2=1$ 의 위쪽 반원을 <span class=\"nw\">$(1,0)$에서</span> <span class=\"nw\">$(-1,0)$까지</span> 가는 곡선일 때, <span class=\"nw\">$\\mathbf G$를</span> 보존장과 간단한 벡터장의 합으로 나누어 $\\displaystyle\\int_C\\mathbf G\\cdot d\\mathbf r$ 를 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$f(x,y,z)=xy^2+x^2z+ye^{z}+K$"
    ],
    [
     "b",
     "$e$"
    ],
    [
     "c",
     "$-\\pi$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$P=y^2+2xz,\\ Q=2xy+e^z,\\ R=x^2+ye^z\\text{:}$ <span class=\"nw\">$P_y=2y=Q_x$,</span> <span class=\"nw\">$\\ Q_z=e^z=R_y$,</span> <span class=\"nw\">$\\ R_x=2x=P_z$.</span> 정의역이 $\\mathbb R^3$ 이므로 보존장이에요.",
      "$f=\\int P\\,dx=xy^2+x^2z+g(y,z)\\text{.}$ $\\ f_y=2xy+g_y=2xy+e^z \\Rightarrow g=ye^z+h(z)\\text{.}$",
      "$f_z=x^2+ye^z+h'(z)=R \\Rightarrow h'(z)=0\\text{.}$ 따라서 <span class=\"nw\">$f=xy^2+x^2z+ye^z+K$.</span>"
     ]
    ],
    [
     "b",
     [
      "시작점 $\\mathbf r(0)=(1,0,0)\\text{,}$ 끝점 $\\mathbf r(1)=(-1,1,1)\\text{.}$ 곡선의 모양과 상관없이 끝점만 필요해요.",
      "$$\\begin{aligned}\\int_C\\mathbf F\\cdot d\\mathbf r&amp;=f(-1,1,1)-f(1,0,0)\\\\&amp;=(-1+1+e)-0=e\\end{aligned}$$"
     ]
    ],
    [
     "c",
     [
      "$\\mathbf G=\\langle2xy,\\ x^2\\rangle+\\langle3y,\\ x\\rangle=\\nabla(x^2y)+\\langle3y,\\ x\\rangle\\text{.}$ ($\\mathbf G$ 자체는 $Q_x-P_y=(2x+1)-(2x+3)=-2\\ne0\\text{)}$",
      "보존장 부분: $x^2y\\Big|_{(1,0)}^{(-1,0)}=0-0=0\\text{.}$",
      "나머지 $\\langle3y,\\ x\\rangle\\text{:}$ $x=\\cos t,\\ y=\\sin t\\ (0\\le t\\le\\pi)\\text{,}$ $d\\mathbf r=\\langle-\\sin t,\\ \\cos t\\rangle\\,dt$ $$\\begin{aligned}&amp;\\int_0^{\\pi}\\big(-3\\sin^2t+\\cos^2t\\big)\\,dt\\\\&amp;=-\\frac{3\\pi}{2}+\\frac{\\pi}{2}=-\\pi\\end{aligned}$$",
      "합: <span class=\"nw\">$0+(-\\pi)=-\\pi$.</span>"
     ]
    ]
   ]
  },
  {
   "id": "q9",
   "no": "9",
   "type": "예상 유형 9 · 그린 정리",
   "ref": "2025 기말 1(b), 5번",
   "stem": "",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$C$가</span> $y=x^2$ 과 $y=1$ 로 둘러싸인 영역의 경계(반시계 방향)일 때 $\\displaystyle\\oint_C y^2\\,dx+3xy\\,dy$ 를 (i) <span class=\"nw\">$C$를</span> 두 곡선으로 나누어 직접 계산하고, (ii) 그린 정리로 계산하시오."
    ],
    [
     "b",
     "<span class=\"nw\">$C$가</span> 원 $x^2+y^2=4$ 의 위쪽 반원을 <span class=\"nw\">$(2,0)$에서</span> <span class=\"nw\">$(-2,0)$까지</span> 가는 곡선일 때 $$\\int_C (x^2-y^3)\\,dx+(x^3+e^{y^2})\\,dy$$"
    ],
    [
     "c",
     "<span class=\"nw\">$C$가</span> 꼭짓점이 $(-1,-1),\\ (2,-1),\\ (-1,2)$ 인 삼각형(반시계 방향)일 때 $\\displaystyle\\oint_C\\frac{-y\\,dx+x\\,dy}{x^2+y^2}$"
    ]
   ],
   "answer": [
    [
     "a",
     "$\\dfrac45$ (두 방법 모두)"
    ],
    [
     "b",
     "$12\\pi-\\dfrac{16}{3}$"
    ],
    [
     "c",
     "$2\\pi$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "(i) <span class=\"nw\">$C_1$:</span> 포물선 <span class=\"nw\">$x=t,\\ y=t^2$,</span> <span class=\"nw\">$-1\\le t\\le1$:</span> $$\\begin{aligned}&amp;\\int_{-1}^{1}\\big(t^4\\cdot1+3t\\cdot t^2\\cdot2t\\big)\\,dt\\\\&amp;=\\int_{-1}^1 7t^4\\,dt=\\frac{14}{5}\\end{aligned}$$",
      "<span class=\"nw\">$C_2$:</span> 선분 <span class=\"nw\">$y=1$,</span> <span class=\"nw\">$(1,1)\\to(-1,1)$,</span> <span class=\"nw\">$dy=0$:</span> $\\displaystyle\\int_1^{-1}1\\,dx=-2\\text{.}$ 합: $\\frac{14}{5}-2=\\frac45\\text{.}$",
      "(ii) <span class=\"nw\">$Q_x-P_y=3y-2y=y$:</span> $$\\begin{aligned}\\iint_D y\\,dA&amp;=\\int_{-1}^1\\!\\!\\int_{x^2}^1 y\\,dy\\,dx\\\\&amp;=\\int_{-1}^1\\frac{1-x^4}{2}\\,dx=\\frac45\\end{aligned}$$"
     ]
    ],
    [
     "b",
     [
      "반원만으로는 닫힌 곡선이 아니에요. 선분 $L:(-2,0)\\to(2,0)$ 을 붙이면 $C\\cup L$ 은 위쪽 반원판 <span class=\"nw\">$D$의</span> 경계(반시계).",
      "그린 정리: $Q_x-P_y=3x^2+3y^2$ $$\\begin{aligned}\\oint_{C\\cup L}&amp;=\\iint_D 3(x^2+y^2)\\,dA\\\\&amp;=\\int_0^{\\pi}\\!\\!\\int_0^2 3r^2\\cdot r\\,dr\\,d\\theta=12\\pi\\end{aligned}$$",
      "$L$ 위에서는 <span class=\"nw\">$y=0,\\ dy=0$:</span> $\\displaystyle\\int_L=\\int_{-2}^{2}x^2\\,dx=\\frac{16}{3}\\text{.}$",
      "$\\displaystyle\\int_C=12\\pi-\\frac{16}{3}\\text{.}$ ($e^{y^2}$ 항을 직접 적분할 필요가 없어져요.)"
     ]
    ],
    [
     "c",
     [
      "$P=\\dfrac{-y}{x^2+y^2},\\ Q=\\dfrac{x}{x^2+y^2}$ 는 원점 밖에서 <span class=\"nw\">$Q_x-P_y=0$.</span> 그런데 원점이 삼각형 안에 있어서 삼각형 전체에 그린 정리를 바로 쓸 수 없어요.",
      "삼각형 안에 작은 원 $C_a:\\ x=a\\cos t,\\ y=a\\sin t$ (반시계)를 잡고 사이 영역에 그린 정리: $\\displaystyle\\oint_C-\\oint_{C_a}=\\iint 0\\,dA=0\\text{.}$",
      "$$\\begin{aligned}\\oint_{C_a}&amp;=\\int_0^{2\\pi}\\frac{a^2\\sin^2t+a^2\\cos^2t}{a^2}\\,dt\\\\&amp;=\\int_0^{2\\pi}1\\,dt=2\\pi\\end{aligned}$$ 따라서 $\\displaystyle\\oint_C=2\\pi\\text{.}$"
     ]
    ]
   ]
  },
  {
   "id": "q10",
   "no": "10",
   "type": "예상 유형 10 · 최대 증가 방향과 기울기",
   "ref": "강의 14.6 예제 6 응용",
   "stem": "언덕의 높이가 $h(x,y)=4-x^2-2y^2$ 이고 등산객이 점 $P(1,1)$ 에 서 있다.",
   "parts": [
    [
     "a",
     "<span class=\"nw\">$P$에서</span> 가장 가파르게 올라가는 방향(단위벡터)과 그 방향의 기울기를 구하시오."
    ],
    [
     "b",
     "<span class=\"nw\">$P$에서</span> 높이가 변하지 않는 방향을 모두 구하고, <span class=\"nw\">$P$를</span> 지나는 등위곡선의 접선의 방정식을 구하시오."
    ],
    [
     "c",
     "$D_{\\mathbf u}h(P)=2$ 를 만족하는 단위벡터 <span class=\"nw\">$\\mathbf u$를</span> 모두 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "방향 $\\frac{1}{\\sqrt5}\\langle-1,-2\\rangle\\text{,}$ 기울기 $2\\sqrt5$"
    ],
    [
     "b",
     "$\\pm\\frac{1}{\\sqrt5}\\langle2,-1\\rangle\\text{,}$ 접선 $x+2y=3$"
    ],
    [
     "c",
     "$\\langle-1,\\ 0\\rangle\\text{,}$ $\\ \\big\\langle\\frac35,\\ -\\frac45\\big\\rangle$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$\\nabla h=\\langle-2x,\\ -4y\\rangle\\text{,}$ $\\nabla h(1,1)=\\langle-2,-4\\rangle\\text{.}$",
      "가장 가파르게 올라가는 방향은 $\\mathbf u=\\dfrac{\\nabla h}{|\\nabla h|}=\\dfrac{1}{\\sqrt5}\\langle-1,-2\\rangle\\text{,}$ 그 방향의 기울기(최대 변화율)는 $|\\nabla h|=\\sqrt{20}=2\\sqrt5\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "$D_{\\mathbf u}h=\\nabla h\\cdot\\mathbf u=0 \\Leftrightarrow \\mathbf u\\perp\\langle-2,-4\\rangle$ → $\\mathbf u=\\pm\\dfrac{1}{\\sqrt5}\\langle2,-1\\rangle\\text{.}$",
      "이 방향이 등위곡선 <span class=\"nw\">$h=1$,</span> 즉 $x^2+2y^2=3$ 의 접선 방향이에요. 접선: $-2(x-1)-4(y-1)=0 \\Rightarrow x+2y=3\\text{.}$"
     ]
    ],
    [
     "c",
     [
      "$\\mathbf u=\\langle a,b\\rangle\\text{,}$ <span class=\"nw\">$a^2+b^2=1$,</span> $-2a-4b=2 \\Rightarrow a=-1-2b\\text{.}$",
      "대입: $(1+2b)^2+b^2=1 \\Rightarrow 5b^2+4b=0 \\Rightarrow b=0$ 또는 <span class=\"nw\">$b=-\\frac45$.</span>",
      "$\\mathbf u=\\langle-1,0\\rangle$ 또는 $\\big\\langle\\frac35,-\\frac45\\big\\rangle\\text{.}$ (최대 기울기 $2\\sqrt5\\approx4.47$ 보다 작은 값이라 두 방향이 나와요.)"
     ]
    ]
   ]
  }
 ],
 "extra": [
  {
   "id": "x1",
   "no": "추가 1",
   "type": "14.7 극값과 안장점",
   "ref": "2025 중간 2(a)",
   "stem": "$f(x,y)=2x^3+xy^2+5x^2+y^2$ 의 극댓값, 극솟값, 안장점을 모두 구하시오.",
   "parts": [],
   "answer": [
    [
     "",
     "극솟값 $0$ <span class=\"nw\">$(0,0)$,</span> 극댓값 $\\dfrac{125}{27}$ $\\big(-\\frac53,0\\big)\\text{,}$ 안장점 $(-1,2),\\ (-1,-2)$"
    ]
   ],
   "solution": [
    [
     "",
     [
      "<span class=\"nw\">$f_x=6x^2+y^2+10x=0$,</span> $\\ f_y=2xy+2y=2y(x+1)=0\\text{.}$",
      "<span class=\"nw\">$y=0$:</span> $6x^2+10x=0 \\Rightarrow x=0,\\ -\\frac53\\text{.}$ <span class=\"nw\">$\\ x=-1$:</span> $6+y^2-10=0 \\Rightarrow y=\\pm2\\text{.}$ 임계점 $(0,0),\\ \\big(-\\frac53,0\\big),\\ (-1,\\pm2)\\text{.}$",
      "$f_{xx}=12x+10,\\ f_{yy}=2x+2,\\ f_{xy}=2y\\text{,}$ $\\ D=f_{xx}f_{yy}-f_{xy}^2\\text{.}$",
      "<span class=\"nw\">$(0,0)$:</span> $D=20>0,\\ f_{xx}=10>0$ → 극솟값 <span class=\"nw\">$0$.</span> $\\big(-\\frac53,0\\big)\\text{:}$ $f_{xx}=-10,\\ f_{yy}=-\\frac43\\text{,}$ $D=\\frac{40}{3}>0$ → 극댓값 <span class=\"nw\">$\\frac{125}{27}$.</span>",
      "<span class=\"nw\">$(-1,\\pm2)$:</span> $f_{xx}=-2,\\ f_{yy}=0,\\ f_{xy}=\\pm4\\text{,}$ $D=-16\\lt 0$ → 안장점."
     ]
    ]
   ]
  },
  {
   "id": "x2",
   "no": "추가 2",
   "type": "14.7 닫힌 영역에서의 최댓값·최솟값",
   "ref": "2025 중간 7번",
   "stem": "$f(x,y)=x^2+2y^2-2x$ 의 원판 $D=\\{(x,y)\\mid x^2+y^2\\le4\\}$ 위에서의 최댓값과 최솟값을 구하시오.",
   "parts": [],
   "answer": [
    [
     "",
     "최댓값 $9$ $\\big((-1,\\pm\\sqrt3)\\big)\\text{,}$ 최솟값 $-1$ $\\big((1,0)\\big)$"
    ]
   ],
   "solution": [
    [
     "",
     [
      "내부 임계점: $f_x=2x-2=0,\\ f_y=4y=0$ → <span class=\"nw\">$(1,0)$,</span> <span class=\"nw\">$f(1,0)=-1$.</span>",
      "경계 <span class=\"nw\">$x^2+y^2=4$:</span> $y^2=4-x^2$ 대입 → $f=x^2+2(4-x^2)-2x=8-x^2-2x\\text{,}$ <span class=\"nw\">$\\ -2\\le x\\le2$.</span>",
      "$\\frac{d}{dx}(8-x^2-2x)=-2x-2=0 \\Rightarrow x=-1\\text{:}$ $f=9$ (점 <span class=\"nw\">$(-1,\\pm\\sqrt3)$).</span> 끝점 <span class=\"nw\">$x=2$:</span> <span class=\"nw\">$f=0$,</span> <span class=\"nw\">$\\ x=-2$:</span> <span class=\"nw\">$f=8$.</span>",
      "비교하면 최댓값 <span class=\"nw\">$9$,</span> 최솟값 <span class=\"nw\">$-1$.</span> (경계는 라그랑주 승수법으로 풀어도 같아요.)"
     ]
    ]
   ]
  },
  {
   "id": "x3",
   "no": "추가 3",
   "type": "14.5 연쇄법칙 (2계 편도함수)",
   "ref": "2025 중간 5번",
   "stem": "$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=s^2-t^2,\\ y=2st$ 일 때",
   "parts": [
    [
     "a",
     "$z_s,\\ z_t$ 를 $f_x,\\ f_y$ 로 나타내시오."
    ],
    [
     "b",
     "$z_{ss}+z_{tt}=4(s^2+t^2)\\,(f_{xx}+f_{yy})$ 임을 보이시오."
    ],
    [
     "c",
     "$f_{xx}(0,2)=3,\\ f_{yy}(0,2)=2$ 일 때 $(s,t)=(1,1)$ 에서 $z_{ss}+z_{tt}$ 의 값을 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$z_s=2s\\,f_x+2t\\,f_y\\text{,}$ $\\ z_t=-2t\\,f_x+2s\\,f_y$"
    ],
    [
     "b",
     "아래 풀이"
    ],
    [
     "c",
     "$40$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "$z_s=f_x\\cdot x_s+f_y\\cdot y_s=2s\\,f_x+2t\\,f_y\\text{,}$ $\\ z_t=f_x\\cdot x_t+f_y\\cdot y_t=-2t\\,f_x+2s\\,f_y\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "$f_x,\\ f_y$ 도 $s,t$ 의 함수라 연쇄법칙을 한 번 더: $(f_x)_s=2s\\,f_{xx}+2t\\,f_{xy}\\text{,}$ $\\ (f_y)_s=2s\\,f_{xy}+2t\\,f_{yy}\\text{.}$",
      "$z_{ss}=2f_x+2s(2sf_{xx}+2tf_{xy})+2t(2sf_{xy}+2tf_{yy})=2f_x+4s^2f_{xx}+8st\\,f_{xy}+4t^2f_{yy}\\text{.}$",
      "같은 방법으로 $z_{tt}=-2f_x+4t^2f_{xx}-8st\\,f_{xy}+4s^2f_{yy}\\text{.}$",
      "더하면 <span class=\"nw\">$f_x$,</span> $f_{xy}$ 항이 지워져 $z_{ss}+z_{tt}=4(s^2+t^2)(f_{xx}+f_{yy})\\text{.}$"
     ]
    ],
    [
     "c",
     [
      "$(s,t)=(1,1)$ 이면 <span class=\"nw\">$(x,y)=(0,2)$.</span> $\\ 4\\cdot(1+1)\\cdot(3+2)=40\\text{.}$"
     ]
    ]
   ]
  },
  {
   "id": "x4",
   "no": "추가 4",
   "type": "14.4–14.6 음함수 미분과 선형근사",
   "ref": "2025 중간 6번",
   "stem": "방정식 $x^2z+yz^2=2$ 가 점 $(1,1,1)$ 근처에서 $z=z(x,y)$ 를 정한다.",
   "parts": [
    [
     "a",
     "$z_x(1,1),\\ z_y(1,1)$ 을 구하시오."
    ],
    [
     "b",
     "점 $(1,1,1)$ 에서 이 곡면의 접평면을 구하시오."
    ],
    [
     "c",
     "선형근사로 $z(1.06,\\ 0.97)$ 의 근삿값을 구하시오."
    ],
    [
     "d",
     "$(1,1)$ 에서 $\\langle3,4\\rangle$ 방향으로의 <span class=\"nw\">$z$의</span> 변화율을 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "$-\\dfrac23,\\ -\\dfrac13$"
    ],
    [
     "b",
     "$2x+y+3z=6$"
    ],
    [
     "c",
     "$0.97$"
    ],
    [
     "d",
     "$-\\dfrac23$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "<span class=\"nw\">$F=x^2z+yz^2-2$:</span> $F_x=2xz,\\ F_y=z^2,\\ F_z=x^2+2yz$ → $(1,1,1)$ 에서 <span class=\"nw\">$2,\\ 1,\\ 3$.</span>",
      "$z_x=-\\dfrac{F_x}{F_z}=-\\dfrac23\\text{,}$ $\\ z_y=-\\dfrac{F_y}{F_z}=-\\dfrac13\\text{.}$"
     ]
    ],
    [
     "b",
     [
      "$\\nabla F(1,1,1)=\\langle2,1,3\\rangle$ → $2(x-1)+(y-1)+3(z-1)=0 \\Rightarrow 2x+y+3z=6\\text{.}$"
     ]
    ],
    [
     "c",
     [
      "$z\\approx1-\\frac23(x-1)-\\frac13(y-1)$ → $z(1.06,0.97)\\approx1-\\frac23(0.06)-\\frac13(-0.03)=1-0.04+0.01=0.97\\text{.}$"
     ]
    ],
    [
     "d",
     [
      "$\\mathbf u=\\big\\langle\\frac35,\\frac45\\big\\rangle\\text{:}$ $D_{\\mathbf u}z=-\\frac23\\cdot\\frac35-\\frac13\\cdot\\frac45=-\\frac25-\\frac{4}{15}=-\\frac23\\text{.}$"
     ]
    ]
   ]
  },
  {
   "id": "x5",
   "no": "추가 5",
   "type": "12–13장 직선과 벡터함수",
   "ref": "2025 시험엔 없지만 우리 범위",
   "stem": "",
   "parts": [
    [
     "a",
     "두 직선 $L_1:\\ x=1+t,\\ y=t,\\ z=-1$ 과 $L_2:\\ x=0,\\ y=2+s,\\ z=1+s$ 가 꼬인 위치에 있음을 보이고, 두 직선 사이의 거리를 구하시오."
    ],
    [
     "b",
     "$\\mathbf r(t)=\\big\\langle t,\\ t^2,\\ \\frac23t^3\\big\\rangle$ 의 $0\\le t\\le1$ 부분의 길이와 $t=1$ 에서의 단위접선벡터를 구하시오."
    ]
   ],
   "answer": [
    [
     "a",
     "거리 $\\dfrac{\\sqrt3}{3}$"
    ],
    [
     "b",
     "길이 <span class=\"nw\">$\\dfrac53$,</span> $\\ \\mathbf T(1)=\\frac13\\langle1,2,2\\rangle$"
    ]
   ],
   "solution": [
    [
     "a",
     [
      "방향 $\\mathbf v_1=\\langle1,1,0\\rangle,\\ \\mathbf v_2=\\langle0,1,1\\rangle$ 은 평행하지 않아요.",
      "만나는지: $1+t=0,\\ t=2+s,\\ -1=1+s\\text{.}$ 앞의 두 식에서 $t=-1,\\ s=-3$ 인데 셋째 식은 $s=-2$ → 모순이라 꼬인 위치.",
      "$\\mathbf n=\\mathbf v_1\\times\\mathbf v_2=\\langle1,-1,1\\rangle\\text{,}$ $P_1=(1,0,-1),\\ P_2=(0,2,1)\\text{:}$ $$d=\\frac{|\\mathbf n\\cdot\\overrightarrow{P_1P_2}|}{|\\mathbf n|}=\\frac{|-1-2+2|}{\\sqrt3}=\\frac{\\sqrt3}{3}$$"
     ]
    ],
    [
     "b",
     [
      "$\\mathbf r'(t)=\\langle1,2t,2t^2\\rangle\\text{,}$ $|\\mathbf r'(t)|=\\sqrt{1+4t^2+4t^4}=1+2t^2\\text{.}$",
      "$L=\\displaystyle\\int_0^1(1+2t^2)\\,dt=\\frac53\\text{,}$ $\\quad\\mathbf T(1)=\\dfrac{\\mathbf r'(1)}{|\\mathbf r'(1)|}=\\frac13\\langle1,2,2\\rangle\\text{.}$"
     ]
    ]
   ]
  }
 ],
 "map": [
  {
   "no": "1",
   "what": "두 원 사이 판의 질량중심 (밀도 <span class=\"nw\">$\\sqrt{x^2+y^2}$)</span>",
   "sec": "15.4 · 15.3",
   "mine": "1 (계산 방식)",
   "here": "1번 · 질량중심 자체는 범위 밖",
   "href": "q1"
  },
  {
   "no": "2(a)",
   "what": "극값과 안장점",
   "sec": "14.7",
   "mine": "",
   "here": "추가 1",
   "href": "x1"
  },
  {
   "no": "2(b)",
   "what": "적분 세 개의 합 → 극좌표",
   "sec": "15.3",
   "mine": "5",
   "here": "5(b)",
   "href": "q5"
  },
  {
   "no": "3",
   "what": "극한 (조임정리, 곡선 경로 <span class=\"nw\">$x-1=ky^2$)</span>",
   "sec": "14.2",
   "mine": "2",
   "here": "2번",
   "href": "q2"
  },
  {
   "no": "4",
   "what": "원주좌표 삼중적분",
   "sec": "15.7",
   "mine": "6",
   "here": "6(b)",
   "href": "q6"
  },
  {
   "no": "5",
   "what": "2계 연쇄법칙",
   "sec": "14.5",
   "mine": "",
   "here": "추가 3",
   "href": "x3"
  },
  {
   "no": "6",
   "what": "음함수의 접평면 → 방향 변화율, 선형근사",
   "sec": "14.4–14.6",
   "mine": "3 · 7 일부",
   "here": "추가 4",
   "href": "x4"
  },
  {
   "no": "7",
   "what": "심장형 영역에서 최댓값·최솟값",
   "sec": "14.7",
   "mine": "",
   "here": "추가 2",
   "href": "x2"
  },
  {
   "no": "8",
   "what": "교선 위 라그랑주 (제약 2개)",
   "sec": "14.8",
   "mine": "4",
   "here": "4(b)",
   "href": "q4"
  },
  {
   "no": "9",
   "what": "삼중적분 순서 바꾸기 (<span class=\"nw\">$e^{z^2}$)</span>",
   "sec": "15.6",
   "mine": "6",
   "here": "6(d)",
   "href": "q6"
  },
  {
   "no": "10",
   "what": "원주좌표 → 구면좌표 변환",
   "sec": "15.8",
   "mine": "6",
   "here": "6(c)",
   "href": "q6"
  }
 ]
};

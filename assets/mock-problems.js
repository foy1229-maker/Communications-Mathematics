/* 자동 생성 파일 — tools/mock.py · tools/mock_sets.py 를 고친 뒤 tools/build.py 로 다시 만드세요. */
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
 ],
 "sets": [
  {
   "id": "s1",
   "no": 1,
   "title": "실전 모의고사 1회",
   "focus": "예상 유형 10선 · 표준",
   "lead": "예상 유형 10개(극좌표 이중적분, 극한과 연속, 접평면·법선, 라그랑주, 이중적분, 삼중적분, 방향도함수, 선적분의 기본정리, 그린 정리, 최대 증가 방향)를 한 문항씩 표준 난이도로 묶었어요. 처음 푸는 회차로 추천해요.",
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "극좌표 이중적분",
     "ref": "2025 중간 1번 · 2(b) 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "극좌표로 바꾸어 계산하시오. $\\displaystyle\\int_0^1\\!\\!\\int_{y}^{\\sqrt{2-y^2}}\\sqrt{x^2+y^2}\\,dx\\,dy$"
      ],
      [
       "b",
       "원 $x^2+y^2=2y$ 의 내부이면서 원 $x^2+y^2=1$ 의 외부인 영역을 $D$ 라 할 때 $\\displaystyle\\iint_D y\\,dA$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\sqrt2\\,\\pi}{6}$"
      ],
      [
       "b",
       "$\\dfrac{2\\pi}{3}+\\dfrac{\\sqrt3}{4}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역: $0\\le y\\le1,\\ y\\le x\\le\\sqrt{2-y^2}$ → 직선 $y=x$ 아래, <span class=\"nw\">$x$축</span> 위, 원 $x^2+y^2=2$ 안의 부채꼴 → $0\\le\\theta\\le\\frac\\pi4,\\ 0\\le r\\le\\sqrt2$",
        "$$\\int_0^{\\pi/4}\\!\\!\\int_0^{\\sqrt2}r\\cdot r\\,dr\\,d\\theta=\\frac\\pi4\\cdot\\frac{2\\sqrt2}{3}=\\frac{\\sqrt2\\,\\pi}{6}$$"
       ]
      ],
      [
       "b",
       [
        "$x^2+y^2=2y \\iff r=2\\sin\\theta\\text{.}$ 교점 $2\\sin\\theta=1 \\Rightarrow \\theta=\\frac\\pi6,\\ \\frac{5\\pi}6$ → $D:\\ \\frac\\pi6\\le\\theta\\le\\frac{5\\pi}6,\\ 1\\le r\\le2\\sin\\theta$",
        "$$\\begin{aligned}\\iint_Dy\\,dA&amp;=\\int_{\\pi/6}^{5\\pi/6}\\!\\!\\int_1^{2\\sin\\theta}r^2\\sin\\theta\\,dr\\,d\\theta\\\\&amp;=\\frac13\\int_{\\pi/6}^{5\\pi/6}\\big(8\\sin^4\\theta-\\sin\\theta\\big)\\,d\\theta\\end{aligned}$$",
        "$\\displaystyle\\int_{\\pi/6}^{5\\pi/6}\\sin^4\\theta\\,d\\theta=\\Big[\\tfrac{3\\theta}8-\\tfrac{\\sin2\\theta}4+\\tfrac{\\sin4\\theta}{32}\\Big]_{\\pi/6}^{5\\pi/6}=\\frac\\pi4+\\frac{7\\sqrt3}{32}\\text{,}$ $\\displaystyle\\int_{\\pi/6}^{5\\pi/6}\\sin\\theta\\,d\\theta=\\sqrt3$",
        "$\\dfrac13\\Big(2\\pi+\\dfrac{7\\sqrt3}{4}-\\sqrt3\\Big)=\\dfrac{2\\pi}3+\\dfrac{\\sqrt3}4$"
       ]
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "극한과 연속",
     "ref": "2025 중간 3번 · 2022 중간 블럭2 2번 유형",
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^2y^2}{(x^2+y^2)^{3/2}}$ 를 구하시오."
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{xy^2}{x^2+4y^4}$ 가 존재하지 않음을 보이시오."
      ],
      [
       "c",
       "$g(x,y)=\\dfrac{x^3-y^3}{x^2+y^2}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $g(0,0)=0$ 일 때 $g$ 가 원점에서 연속임을 보이고 $g_x(0,0),\\ g_y(0,0)$ 을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$0$"
      ],
      [
       "b",
       "곡선 $x=ky^2$ 을 따라 $\\dfrac{k}{k^2+4}$ → 존재하지 않음"
      ],
      [
       "c",
       "연속, $g_x(0,0)=1,\\ g_y(0,0)=-1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "극좌표: $\\dfrac{r^4\\cos^2\\theta\\sin^2\\theta}{r^3}=r\\cos^2\\theta\\sin^2\\theta\\text{,}$ $0\\le|\\cdot|\\le r\\to0$ → 극한 $0$"
       ]
      ],
      [
       "b",
       [
        "직선 $y=mx$ 로는 $\\dfrac{m^2x^3}{x^2+4m^4x^4}\\to0$ 이라 판정이 안 돼요. 분모 차수를 맞추는 곡선 <span class=\"nw\">$x=ky^2$:</span>",
        "$\\dfrac{ky^4}{k^2y^4+4y^4}=\\dfrac{k}{k^2+4}$ → $k=0$ 이면 <span class=\"nw\">$0$,</span> $k=2$ 이면 $\\frac14$ → 존재하지 않음"
       ]
      ],
      [
       "c",
       [
        "$|x^3-y^3|\\le|x|^3+|y|^3\\le\\sqrt{x^2+y^2}\\,(x^2+y^2)$ → $|g(x,y)|\\le\\sqrt{x^2+y^2}\\to0=g(0,0)$ → 연속",
        "$g_x(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{g(h,0)-0}{h}=\\lim\\frac{h^3/h^2}{h}=1\\text{,}$&emsp;$g_y(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{-h^3/h^2}{h}=-1$"
       ]
      ]
     ],
     "types": [
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ],
      [
       "14-dne",
       "극한이 존재하지 않음"
      ],
      [
       "14-defpartial",
       "연속성 판정·정의로 구하는 편도함수"
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "접평면과 법선",
     "ref": "2022 중간 블럭1 7번 · 강의 14.6 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "곡면 $x^2y+y^2z+z^2x=3$ 위의 점 $(1,1,1)$ 에서 접평면과 법선의 방정식을 구하시오."
      ],
      [
       "b",
       "타원면 $x^2+4y^2+z^2=9$ 위에서 접평면이 평면 $2x+4y+z=1$ 과 평행한 점을 모두 구하고, 각 점에서의 접평면을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "접평면 <span class=\"nw\">$x+y+z=3$,</span> 법선 $x-1=y-1=z-1$"
      ],
      [
       "b",
       "<span class=\"nw\">$(2,1,1)$:</span> <span class=\"nw\">$2x+4y+z=9$,</span>&emsp;<span class=\"nw\">$(-2,-1,-1)$:</span> $2x+4y+z=-9$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$F=x^2y+y^2z+z^2x$,</span> $\\nabla F=\\langle2xy+z^2,\\ x^2+2yz,\\ y^2+2zx\\rangle$ → $\\nabla F(1,1,1)=\\langle3,3,3\\rangle$",
        "접평면 $3(x-1)+3(y-1)+3(z-1)=0 \\Rightarrow x+y+z=3\\text{,}$ 법선 $x=1+t,\\ y=1+t,\\ z=1+t$"
       ]
      ],
      [
       "b",
       [
        "$\\nabla G=\\langle2x,8y,2z\\rangle=c\\langle2,4,1\\rangle$ → $x=c,\\ y=\\frac c2,\\ z=\\frac c2$",
        "대입: $c^2+c^2+\\frac{c^2}{4}=\\frac94c^2=9 \\Rightarrow c=\\pm2$ → 점 <span class=\"nw\">$(2,1,1)$,</span> $(-2,-1,-1)$",
        "접평면 $2(x-2)+4(y-1)+(z-1)=0 \\Rightarrow 2x+4y+z=9\\text{,}$ 반대 점에서는 $2x+4y+z=-9$"
       ]
      ]
     ],
     "types": [
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "라그랑주 승수법",
     "ref": "2025 중간 8번 유형",
     "stem": "라그랑주 승수법을 이용하여 다음을 구하시오.",
     "parts": [
      [
       "a",
       "구 $x^2+y^2+z^2=9$ 위에서 $f(x,y,z)=x+2y+2z$ 의 최댓값과 최솟값"
      ],
      [
       "b",
       "원기둥 $x^2+y^2=2$ 와 평면 $x+z=1$ 의 교선 위에서 $f(x,y,z)=x+y+z$ 의 최댓값과 최솟값"
      ]
     ],
     "answer": [
      [
       "a",
       "최댓값 $9$ (점 <span class=\"nw\">$(1,2,2)$),</span> 최솟값 $-9$ (점 <span class=\"nw\">$(-1,-2,-2)$)</span>"
      ],
      [
       "b",
       "최댓값 $1+\\sqrt2$ (점 <span class=\"nw\">$(0,\\sqrt2,1)$),</span> 최솟값 $1-\\sqrt2$ (점 <span class=\"nw\">$(0,-\\sqrt2,1)$)</span>"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\langle1,2,2\\rangle=\\lambda\\langle2x,2y,2z\\rangle$ → $x=\\frac1{2\\lambda},\\ y=z=\\frac1\\lambda$",
        "대입: $\\frac{1}{4\\lambda^2}+\\frac{2}{\\lambda^2}=\\frac{9}{4\\lambda^2}=9 \\Rightarrow \\lambda=\\pm\\frac12$ → $(1,2,2)$ 에서 <span class=\"nw\">$9$,</span> $(-1,-2,-2)$ 에서 $-9$"
       ]
      ],
      [
       "b",
       [
        "$g=x^2+y^2=2,\\ h=x+z=1\\text{:}$ $\\langle1,1,1\\rangle=\\lambda\\langle2x,2y,0\\rangle+\\mu\\langle1,0,1\\rangle$",
        "<span class=\"nw\">$z$성분:</span> $\\mu=1$ → <span class=\"nw\">$x$성분:</span> <span class=\"nw\">$2\\lambda x=0$,</span> <span class=\"nw\">$y$성분:</span> $2\\lambda y=1$ 이므로 $\\lambda\\ne0$ → $x=0$",
        "$y=\\pm\\sqrt2,\\ z=1-x=1$ → $f=1\\pm\\sqrt2$ → 최댓값 <span class=\"nw\">$1+\\sqrt2$,</span> 최솟값 $1-\\sqrt2$"
       ]
      ]
     ],
     "types": [
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "14-lagrange2",
       "제약조건 2개 라그랑주"
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "이중적분 (순서 바꾸기 · 부피)",
     "ref": "2024 중간 2(a) 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "적분 순서를 바꾸어 계산하시오. $\\displaystyle\\int_0^1\\!\\!\\int_{\\sqrt y}^{1}\\sqrt{x^3+1}\\,dx\\,dy$"
      ],
      [
       "b",
       "포물기둥 $y=x^2$ 과 평면 <span class=\"nw\">$y=1,\\ z=0$,</span> 곡면 $z=x^2+y^2$ 으로 둘러싸인 입체의 부피를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{2}{9}\\big(2\\sqrt2-1\\big)$"
      ],
      [
       "b",
       "$\\dfrac{88}{105}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역: $0\\le y\\le1,\\ \\sqrt y\\le x\\le1$ ⟺ $0\\le x\\le1,\\ 0\\le y\\le x^2$",
        "$$\\int_0^1\\!\\!\\int_0^{x^2}\\sqrt{x^3+1}\\,dy\\,dx=\\int_0^1x^2\\sqrt{x^3+1}\\,dx=\\Big[\\tfrac29(x^3+1)^{3/2}\\Big]_0^1=\\tfrac29(2\\sqrt2-1)$$"
       ]
      ],
      [
       "b",
       [
        "밑면 $D=\\{-1\\le x\\le1,\\ x^2\\le y\\le1\\}\\text{,}$ 높이 $x^2+y^2$",
        "$$\\begin{aligned}V&amp;=\\int_{-1}^1\\!\\!\\int_{x^2}^1(x^2+y^2)\\,dy\\,dx\\\\&amp;=\\int_{-1}^1\\Big(x^2-x^4+\\frac{1-x^6}{3}\\Big)dx\\\\&amp;=2\\Big(\\frac13-\\frac15+\\frac13-\\frac1{21}\\Big)=\\frac{88}{105}\\end{aligned}$$"
       ]
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-general",
       "일반 영역(Type I/II)·부피"
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "삼중적분 (원주 · 구면좌표)",
     "ref": "2025 중간 4번 · 10번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "$E$ 가 원기둥 $x^2+y^2=4$ 의 내부에서 평면 $z=0$ 위, 평면 $z=4-y$ 아래에 있는 입체일 때 $\\displaystyle\\iiint_E\\sqrt{x^2+y^2}\\,dV$ 를 구하시오."
      ],
      [
       "b",
       "$E$ 가 원뿔 $z=\\sqrt{x^2+y^2}$ 위, 구 $x^2+y^2+z^2=4$ 안에 있는 입체일 때 $\\displaystyle\\iiint_E z\\,dV$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{64\\pi}{3}$"
      ],
      [
       "b",
       "$2\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "원주좌표: $0\\le\\theta\\le2\\pi,\\ 0\\le r\\le2,\\ 0\\le z\\le4-r\\sin\\theta$ (<span class=\"nw\">$4-y\\ge2>0$)</span>",
        "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^2(4-r\\sin\\theta)\\,r\\cdot r\\,dr\\,d\\theta\\\\&amp;=4\\cdot2\\pi\\cdot\\frac83-\\int_0^{2\\pi}\\sin\\theta\\,d\\theta\\cdot4=\\frac{64\\pi}{3}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "구면좌표: 원뿔 $z=r$ ⟺ $\\phi=\\frac\\pi4$ → $0\\le\\phi\\le\\frac\\pi4,\\ 0\\le\\rho\\le2$",
        "$$\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/4}\\!\\!\\int_0^2\\rho\\cos\\phi\\cdot\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta=2\\pi\\cdot\\frac{\\sin^2(\\pi/4)}{2}\\cdot4=2\\pi$$"
       ]
      ]
     ],
     "types": [
      [
       "15-cyl",
       "원주좌표"
      ],
      [
       "15-sph",
       "구면좌표 삼중적분"
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "방향도함수와 그래디언트",
     "ref": "2022 중간 블럭1 5번 · 강의 14.6 유형",
     "stem": "<span class=\"nw\">$f(x,y,z)=xy^2+yz^3$,</span> <span class=\"nw\">$P(2,-1,1)$,</span> $Q(4,0,-1)$ 에 대하여",
     "parts": [
      [
       "a",
       "$\\nabla f(P)$ 를 구하시오."
      ],
      [
       "b",
       "$P$ 에서 $Q$ 를 향하는 방향의 방향도함수를 구하시오."
      ],
      [
       "c",
       "$P$ 에서 $f$ 가 가장 빨리 감소하는 방향과 그때의 변화율을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\langle1,-3,-3\\rangle$"
      ],
      [
       "b",
       "$\\dfrac53$"
      ],
      [
       "c",
       "방향 $\\dfrac{1}{\\sqrt{19}}\\langle-1,3,3\\rangle\\text{,}$ 변화율 $-\\sqrt{19}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=y^2,\\ f_y=2xy+z^3,\\ f_z=3yz^2$ → $(1,\\ -4+1,\\ -3)=\\langle1,-3,-3\\rangle$"
       ]
      ],
      [
       "b",
       [
        "$\\overrightarrow{PQ}=\\langle2,1,-2\\rangle\\text{,}$ $|\\overrightarrow{PQ}|=3$ → $D_{\\mathbf u}f=\\dfrac{2-3+6}{3}=\\dfrac53$"
       ]
      ],
      [
       "c",
       [
        "가장 빨리 감소하는 방향은 $-\\nabla f$ 방향, 변화율은 $-|\\nabla f|=-\\sqrt{1+9+9}=-\\sqrt{19}$"
       ]
      ]
     ],
     "types": [
      [
       "14-dir",
       "방향도함수"
      ],
      [
       "14-maxrate",
       "최대 변화율과 방향"
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "선적분의 기본정리",
     "ref": "2024 기말 2(b) 유형",
     "stem": "$\\mathbf F(x,y,z)=\\big\\langle y^2+2xz,\\ 2xy+z,\\ x^2+y\\big\\rangle\\text{,}$ $C:\\ \\mathbf r(t)=\\big\\langle t^2,\\ \\sin\\tfrac{\\pi t}{2},\\ e^{t-1}\\big\\rangle\\ (0\\le t\\le1)$ 에 대하여",
     "parts": [
      [
       "a",
       "$\\mathbf F$ 가 보존장임을 보이고 $\\mathbf F=\\nabla f$ 인 $f$ 를 구하시오."
      ],
      [
       "b",
       "$\\displaystyle\\int_C\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ],
      [
       "c",
       "$\\mathbf G=\\mathbf F+\\langle0,0,x\\rangle$ 일 때 $\\displaystyle\\int_C\\mathbf G\\cdot d\\mathbf r$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$f=xy^2+x^2z+yz$"
      ],
      [
       "b",
       "$3$"
      ],
      [
       "c",
       "$4-\\dfrac2e$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$P_y=2y=Q_x,\\ P_z=2x=R_x,\\ Q_z=1=R_y$ → 보존장",
        "$f=\\int(y^2+2xz)\\,dx=xy^2+x^2z+g(y,z)\\text{,}$ $f_y=2xy+g_y=2xy+z \\Rightarrow g=yz+h(z)\\text{,}$ $f_z=x^2+y \\Rightarrow h$ 상수 → $f=xy^2+x^2z+yz$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r(0)=(0,0,e^{-1})\\text{,}$ $\\mathbf r(1)=(1,1,1)$ → $f(1,1,1)-f(0,0,e^{-1})=3-0=3$"
       ]
      ],
      [
       "c",
       [
        "$\\displaystyle\\int_C\\mathbf G\\cdot d\\mathbf r=3+\\int_Cx\\,dz=3+\\int_0^1t^2e^{t-1}\\,dt$",
        "$\\displaystyle\\int_0^1t^2e^{t}\\,dt=\\Big[(t^2-2t+2)e^t\\Big]_0^1=e-2$ → $e^{-1}(e-2)=1-\\frac2e$ → 답 $4-\\dfrac2e$"
       ]
      ]
     ],
     "types": [
      [
       "16-conserv",
       "보존장 판정·퍼텐셜"
      ],
      [
       "16-ftli",
       "선적분의 기본정리"
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "그린 정리",
     "ref": "2024 기말 1번 유형",
     "stem": "그린 정리를 이용하여 다음을 구하시오.",
     "parts": [
      [
       "a",
       "$C$ 가 원 $x^2+y^2=4$ (반시계 방향)일 때 $\\displaystyle\\oint_C(x^2-y^3)\\,dx+(x^3+y^2)\\,dy$"
      ],
      [
       "b",
       "$C$ 가 꼭짓점 $(0,0),\\ (1,0),\\ (1,2)$ 인 삼각형의 경계(반시계 방향)일 때 $\\displaystyle\\oint_C(y+e^x)\\,dx+(2x+\\cos y)\\,dy$"
      ],
      [
       "c",
       "타원 $\\dfrac{x^2}{9}+\\dfrac{y^2}{4}=1$ 로 둘러싸인 영역의 넓이"
      ]
     ],
     "answer": [
      [
       "a",
       "$24\\pi$"
      ],
      [
       "b",
       "$1$"
      ],
      [
       "c",
       "$6\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$Q_x-P_y=3x^2+3y^2$ → $\\displaystyle\\iint_D3r^2\\,dA=\\int_0^{2\\pi}\\!\\!\\int_0^23r^3\\,dr\\,d\\theta=2\\pi\\cdot12=24\\pi$"
       ]
      ],
      [
       "b",
       [
        "$Q_x-P_y=2-1=1$ → 값 = 삼각형의 넓이 $=\\tfrac12\\cdot1\\cdot2=1$"
       ]
      ],
      [
       "c",
       [
        "$A=\\dfrac12\\displaystyle\\oint_Cx\\,dy-y\\,dx\\text{,}$ $x=3\\cos t,\\ y=2\\sin t\\text{:}$ $x\\,dy-y\\,dx=(6\\cos^2t+6\\sin^2t)\\,dt=6\\,dt$",
        "$A=\\dfrac12\\displaystyle\\int_0^{2\\pi}6\\,dt=6\\pi$"
       ]
      ]
     ],
     "types": [
      [
       "16-green",
       "그린 정리"
      ],
      [
       "16-greenarea",
       "그린 정리로 넓이"
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "최대 증가 방향",
     "ref": "강의 14.6 예제 응용 · 2022 중간 블럭2 3(a)",
     "stem": "평면 위 점 $(x,y)$ 의 온도가 $T(x,y)=\\dfrac{100}{1+x^2+2y^2}$ 이다.",
     "parts": [
      [
       "a",
       "점 $(1,1)$ 에서 온도가 가장 빨리 증가하는 방향과 최대 증가율을 구하시오."
      ],
      [
       "b",
       "점 $(1,1)$ 에서 온도가 순간적으로 변하지 않는 방향을 모두 구하시오."
      ],
      [
       "c",
       "점 $(1,1)$ 에서 출발해 매 순간 온도가 가장 빨리 증가하는 방향으로 움직이는 입자의 경로를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "방향 $\\dfrac{1}{\\sqrt5}\\langle-1,-2\\rangle\\text{,}$ 최대 증가율 $\\dfrac{25\\sqrt5}{2}$"
      ],
      [
       "b",
       "$\\pm\\dfrac{1}{\\sqrt5}\\langle2,-1\\rangle$"
      ],
      [
       "c",
       "$y=x^2$ (원점 쪽으로)"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\nabla T=\\dfrac{-100\\langle2x,4y\\rangle}{(1+x^2+2y^2)^2}$ → $\\nabla T(1,1)=\\dfrac{-100\\langle2,4\\rangle}{16}=\\big\\langle-\\tfrac{25}{2},-25\\big\\rangle$",
        "방향 $\\langle-1,-2\\rangle/\\sqrt5\\text{,}$ 최대 증가율 $|\\nabla T|=\\tfrac{25}{2}\\sqrt{1+4}=\\tfrac{25\\sqrt5}{2}$"
       ]
      ],
      [
       "b",
       [
        "$D_{\\mathbf u}T=0 \\iff \\mathbf u\\perp\\nabla T$ → $\\mathbf u=\\pm\\frac{1}{\\sqrt5}\\langle2,-1\\rangle$ (등온선의 접선 방향)"
       ]
      ],
      [
       "c",
       [
        "경로의 기울기 $\\dfrac{dy}{dx}=\\dfrac{T_y}{T_x}=\\dfrac{4y}{2x}=\\dfrac{2y}{x}$ → $\\ln|y|=2\\ln|x|+C$ → $y=cx^2$",
        "$(1,1)$ 을 지나므로 <span class=\"nw\">$y=x^2$.</span> $\\nabla T$ 가 원점을 향하므로 입자는 이 포물선을 따라 원점(최고 온도)으로 가요."
       ]
      ]
     ],
     "types": [
      [
       "14-maxrate",
       "최대 변화율과 방향"
      ],
      [
       "14-dir",
       "방향도함수"
      ]
     ]
    }
   ]
  },
  {
   "id": "s2",
   "no": 2,
   "title": "실전 모의고사 2회",
   "focus": "2025 중간 스타일",
   "lead": "2025학년도 중간고사의 문항 구성을 그대로 따라가요 — 질량중심, 극값 + 극좌표 변환, 극한, 원주좌표, 2계 연쇄법칙, 음함수와 선형근사, 심장형 영역의 최대·최소, 제약 2개 라그랑주. 마지막 두 문항은 우리 범위인 선적분의 기본정리와 그린 정리예요.",
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "판의 질량중심 (극좌표)",
     "ref": "2025 중간 1번 유형",
     "stem": "원 $x^2+y^2=2x$ 의 내부이면서 원 $x^2+y^2=2$ 의 외부인 영역을 차지하는 판의 밀도가 $\\rho(x,y)=\\sqrt{x^2+y^2}$ 일 때,",
     "parts": [
      [
       "a",
       "판의 질량을 구하시오."
      ],
      [
       "b",
       "판의 질량중심을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\sqrt2\\,(20-3\\pi)}{9}$"
      ],
      [
       "b",
       "$\\Big(\\dfrac{84}{100-15\\pi},\\ 0\\Big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x^2+y^2=2x \\iff r=2\\cos\\theta\\text{,}$ 교점 $2\\cos\\theta=\\sqrt2 \\Rightarrow \\theta=\\pm\\frac\\pi4$ → $D:\\ |\\theta|\\le\\frac\\pi4,\\ \\sqrt2\\le r\\le2\\cos\\theta$",
        "$$\\begin{aligned}m&amp;=\\int_{-\\pi/4}^{\\pi/4}\\!\\!\\int_{\\sqrt2}^{2\\cos\\theta}r^2\\,dr\\,d\\theta=\\int_{-\\pi/4}^{\\pi/4}\\frac{8\\cos^3\\theta-2\\sqrt2}{3}\\,d\\theta\\end{aligned}$$",
        "$\\displaystyle\\int_{-\\pi/4}^{\\pi/4}\\cos^3\\theta\\,d\\theta=\\Big[\\sin\\theta-\\tfrac{\\sin^3\\theta}{3}\\Big]_{-\\pi/4}^{\\pi/4}=\\frac{5\\sqrt2}{6}$ → $m=\\dfrac{20\\sqrt2}{9}-\\dfrac{\\sqrt2\\pi}{3}=\\dfrac{\\sqrt2(20-3\\pi)}{9}$"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$x$축</span> 대칭 → $\\bar y=0$",
        "$$\\begin{aligned}M_y&amp;=\\int_{-\\pi/4}^{\\pi/4}\\!\\!\\int_{\\sqrt2}^{2\\cos\\theta}r^3\\cos\\theta\\,dr\\,d\\theta\\\\&amp;=\\int_{-\\pi/4}^{\\pi/4}\\cos\\theta\\cdot\\frac{16\\cos^4\\theta-4}{4}\\,d\\theta=4\\cdot\\frac{43\\sqrt2}{60}-\\sqrt2=\\frac{28\\sqrt2}{15}\\end{aligned}$$",
        "($\\int_{-\\pi/4}^{\\pi/4}\\cos^5\\theta\\,d\\theta=\\big[\\sin\\theta-\\tfrac23\\sin^3\\theta+\\tfrac15\\sin^5\\theta\\big]_{-\\pi/4}^{\\pi/4}=\\tfrac{43\\sqrt2}{60}\\text{)}$",
        "$\\bar x=\\dfrac{28\\sqrt2/15}{\\sqrt2(20-3\\pi)/9}=\\dfrac{84}{5(20-3\\pi)}=\\dfrac{84}{100-15\\pi}\\approx1.59$"
       ]
      ]
     ],
     "types": [
      [
       "15-mass",
       "질량·질량중심"
      ],
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "극값과 안장점 · 극좌표로 바꾸기",
     "ref": "2025 중간 2번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "$f(x,y)=2x^3+xy^2+5x^2+y^2$ 의 극댓값, 극솟값, 안장점을 구하시오."
      ],
      [
       "b",
       "다음 합을 극좌표의 이중적분 하나로 나타내고, $f(x,y)=x$ 일 때 값을 구하시오. $$\\int_{1/2}^{1}\\!\\!\\int_{\\sqrt{1-x^2}}^{\\sqrt3\\,x}f\\,dy\\,dx+\\int_1^2\\!\\!\\int_0^{\\sqrt{4-x^2}}f\\,dy\\,dx$$"
      ]
     ],
     "answer": [
      [
       "a",
       "극솟값 <span class=\"nw\">$f(0,0)=0$,</span> 극댓값 $f\\big(-\\tfrac53,0\\big)=\\tfrac{125}{27}\\text{,}$ 안장점 $(-1,\\pm2)$"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^{\\pi/3}\\!\\!\\int_1^2f(r\\cos\\theta,r\\sin\\theta)\\,r\\,dr\\,d\\theta\\text{,}$ 값 $\\dfrac{7\\sqrt3}{6}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=6x^2+y^2+10x=0,\\ f_y=2y(x+1)=0$",
        "<span class=\"nw\">$y=0$:</span> $6x^2+10x=0 \\Rightarrow x=0,\\ -\\tfrac53\\text{;}$&emsp;<span class=\"nw\">$x=-1$:</span> $y^2=4 \\Rightarrow y=\\pm2$",
        "$f_{xx}=12x+10,\\ f_{yy}=2x+2,\\ f_{xy}=2y$",
        "<span class=\"nw\">$(0,0)$:</span> $D=20>0,\\ f_{xx}>0$ → 극소 <span class=\"nw\">$0$;</span>&emsp;$\\big(-\\tfrac53,0\\big)\\text{:}$ $f_{xx}=-10,\\ f_{yy}=-\\tfrac43\\text{,}$ $D=\\tfrac{40}3>0$ → 극대 <span class=\"nw\">$\\tfrac{125}{27}$;</span>&emsp;<span class=\"nw\">$(-1,\\pm2)$:</span> $D=0-16\\lt 0$ → 안장점"
       ]
      ],
      [
       "b",
       [
        "첫 조각: 원 $r=1$ 바깥, 직선 $y=\\sqrt3x$ (<span class=\"nw\">$\\theta=\\frac\\pi3$)</span> 아래. 둘째 조각: 원 $r=2$ 안, $x\\ge1$ → 합치면 $1\\le r\\le2,\\ 0\\le\\theta\\le\\frac\\pi3$",
        "$$\\int_0^{\\pi/3}\\!\\!\\int_1^2 r\\cos\\theta\\cdot r\\,dr\\,d\\theta=\\frac73\\cdot\\frac{\\sqrt3}{2}=\\frac{7\\sqrt3}{6}$$"
       ]
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "극한",
     "ref": "2025 중간 3번 유형",
     "stem": "다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^4\\sin y}{(x^2+y^2)^2}$"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,1)}\\frac{\\sin(xy^2)\\cos x-\\cos(xy^2)\\sin x}{x^2+(y-1)^2}$"
      ],
      [
       "c",
       "$\\displaystyle\\lim_{(x,y)\\to(0,1)}\\frac{\\sin(xy^2)\\cos x-\\cos(xy^2)\\sin x}{\\sqrt{x^2+(y-1)^2}}$"
      ]
     ],
     "answer": [
      [
       "a",
       "$0$"
      ],
      [
       "b",
       "존재하지 않음 (직선 $x=k(y-1)$ 을 따라 <span class=\"nw\">$\\tfrac{2k}{k^2+1}$)</span>"
      ],
      [
       "c",
       "$0$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x^4\\le(x^2+y^2)^2$ → $\\Big|\\dfrac{x^4\\sin y}{(x^2+y^2)^2}\\Big|\\le|\\sin y|\\to0$ → 극한 $0$"
       ]
      ],
      [
       "b",
       [
        "분자 $=\\sin(xy^2-x)=\\sin\\big(x(y-1)(y+1)\\big)\\text{.}$ $v=y-1$ 로 두면 $(x,v)\\to(0,0)$",
        "직선 <span class=\"nw\">$x=kv$:</span> $\\dfrac{\\sin\\big(kv^2(v+2)\\big)}{(k^2+1)v^2}\\to\\dfrac{2k}{k^2+1}$ → $k=0$ 이면 <span class=\"nw\">$0$,</span> $k=1$ 이면 $1$ → 존재하지 않음"
       ]
      ],
      [
       "c",
       [
        "$|\\sin w|\\le|w|$ → $|\\text{분자}|\\le|x||v||v+2|\\le\\dfrac{x^2+v^2}{2}\\,|v+2|$",
        "$\\Big|\\dfrac{\\text{분자}}{\\sqrt{x^2+v^2}}\\Big|\\le\\dfrac{\\sqrt{x^2+v^2}}{2}|v+2|\\to0$ → 극한 $0$"
       ]
      ]
     ],
     "types": [
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ],
      [
       "14-dne",
       "극한이 존재하지 않음"
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "원주좌표 삼중적분",
     "ref": "2025 중간 4번 유형",
     "stem": "$E$ 가 포물면 $z=x^2+y^2$ 과 평면 $z=4$ 로 둘러싸인 입체 중 $x\\ge0$ 인 부분일 때,",
     "parts": [
      [
       "a",
       "$\\displaystyle\\iiint_Ex\\,dV$ 를 구하시오."
      ],
      [
       "b",
       "$\\displaystyle\\iiint_Ez\\,dV$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{128}{15}$"
      ],
      [
       "b",
       "$\\dfrac{32\\pi}{3}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "원주좌표: $-\\frac\\pi2\\le\\theta\\le\\frac\\pi2,\\ 0\\le r\\le2,\\ r^2\\le z\\le4$",
        "$$\\begin{aligned}\\iiint_Ex\\,dV&amp;=\\int_{-\\pi/2}^{\\pi/2}\\!\\!\\int_0^2(4-r^2)\\,r\\cos\\theta\\cdot r\\,dr\\,d\\theta\\\\&amp;=2\\int_0^2(4r^2-r^4)\\,dr=2\\Big(\\frac{32}{3}-\\frac{32}{5}\\Big)=\\frac{128}{15}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$$\\begin{aligned}\\iiint_Ez\\,dV&amp;=\\int_{-\\pi/2}^{\\pi/2}\\!\\!\\int_0^2\\frac{16-r^4}{2}\\,r\\,dr\\,d\\theta\\\\&amp;=\\pi\\cdot\\frac12\\Big(32-\\frac{64}{6}\\Big)=\\frac{32\\pi}{3}\\end{aligned}$$"
       ]
      ]
     ],
     "types": [
      [
       "15-cyl",
       "원주좌표"
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "2계 연쇄법칙",
     "ref": "2025 중간 5번 유형",
     "stem": "$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=s+t,\\ y=st$ 이다. $f_x(3,2)=1,\\ f_y(3,2)=-2,\\ f_{xx}(3,2)=3,\\ f_{xy}(3,2)=1,\\ f_{yy}(3,2)=-1$ 일 때 $(s,t)=(1,2)$ 에서",
     "parts": [
      [
       "a",
       "$\\dfrac{\\partial^2z}{\\partial s\\,\\partial t}$ 를 구하시오."
      ],
      [
       "b",
       "$\\dfrac{\\partial^2z}{\\partial s^2}$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$2$"
      ],
      [
       "b",
       "$3$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$(s,t)=(1,2)$ ↔ <span class=\"nw\">$(x,y)=(3,2)$.</span> $z_s=f_x\\cdot1+f_y\\cdot t$",
        "$t$ 로 미분 (<span class=\"nw\">$x_t=1,\\ y_t=s$):</span> $z_{st}=(f_{xx}+f_{xy}s)+f_y+t\\,(f_{yx}+f_{yy}s)$",
        "$=(3+1)+(-2)+2(1-1)=2$"
       ]
      ],
      [
       "b",
       [
        "$s$ 로 미분 (<span class=\"nw\">$x_s=1,\\ y_s=t$):</span> $z_{ss}=(f_{xx}+f_{xy}t)+t\\,(f_{yx}+f_{yy}t)$",
        "$=(3+2)+2(1-2)=3$"
       ]
      ]
     ],
     "types": [
      [
       "14-chain2",
       "2계 연쇄법칙"
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "음함수 · 접평면 · 선형근사",
     "ref": "2025 중간 6번 유형",
     "stem": "미분가능한 함수 $F(x,y,z)$ 에 대해 $F_z\\ne0$ 이고, $z=z(x,y)$ 는 $F\\big(x,y,z(x,y)\\big)=0$ 으로 정해진다. 곡면 $F(x,y,z)=0$ 의 점 $(2,1,3)$ 에서의 접평면이 $3x-y+2z=11$ 일 때,",
     "parts": [
      [
       "a",
       "점 $(2,1)$ 에서 $z$ 의 $\\mathbf v=\\langle3,4\\rangle$ 방향으로의 변화율을 구하시오."
      ],
      [
       "b",
       "선형근사로 $z(2.1,\\ 0.8)$ 의 근삿값을 구하시오."
      ],
      [
       "c",
       "점 $(2,1)$ 에서 $z$ 의 최대 변화율을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$-\\dfrac12$"
      ],
      [
       "b",
       "$2.75$"
      ],
      [
       "c",
       "$\\dfrac{\\sqrt{10}}{2}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "접평면의 법선 $\\langle3,-1,2\\rangle\\parallel\\nabla F$ → $z_x=-\\dfrac{F_x}{F_z}=-\\dfrac32,\\ z_y=-\\dfrac{F_y}{F_z}=\\dfrac12$",
        "$\\mathbf u=\\big\\langle\\tfrac35,\\tfrac45\\big\\rangle\\text{:}$ $D_{\\mathbf u}z=-\\tfrac32\\cdot\\tfrac35+\\tfrac12\\cdot\\tfrac45=-\\tfrac{9}{10}+\\tfrac{4}{10}=-\\tfrac12$"
       ]
      ],
      [
       "b",
       [
        "$z(2.1,0.8)\\approx3-\\tfrac32(0.1)+\\tfrac12(-0.2)=3-0.15-0.1=2.75$ (접평면 $z=\\tfrac{11-3x+y}{2}$ 에 대입한 값과 같아요)"
       ]
      ],
      [
       "c",
       [
        "$|\\nabla z(2,1)|=\\sqrt{\\tfrac94+\\tfrac14}=\\dfrac{\\sqrt{10}}{2}$"
       ]
      ]
     ],
     "types": [
      [
       "14-implicit",
       "음함수 편미분"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ],
      [
       "14-dir",
       "방향도함수"
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "닫힌 영역의 최댓값·최솟값",
     "ref": "2025 중간 7번 유형",
     "stem": "$f(x,y)=x^2+y^2+y$ 의 영역 $D=\\big\\{(x,y)\\ \\big|\\ x^2+y^2\\le\\sqrt{x^2+y^2}-y\\big\\}$ 위에서의 최댓값과 최솟값을 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "최댓값 $2$ (점 <span class=\"nw\">$(0,-2)$),</span> 최솟값 $-\\dfrac14$ (점 $\\big(0,-\\tfrac12\\big)\\text{)}$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "극좌표: $r^2\\le r-r\\sin\\theta \\iff r\\le1-\\sin\\theta$ (아래로 향한 심장형)",
        "내부 임계점: $f_x=2x=0,\\ f_y=2y+1=0$ → $\\big(0,-\\tfrac12\\big)$ ($\\theta=-\\frac\\pi2$ 방향, $r=\\tfrac12\\le2$ 이므로 $D$ 안), $f=-\\tfrac14$",
        "경계 <span class=\"nw\">$r=1-\\sin\\theta$:</span> $\\sin\\theta=1-r$ 이므로 $f=r^2+r\\sin\\theta=r^2+r(1-r)=r$ (<span class=\"nw\">$0\\le r\\le2$)</span>",
        "경계에서 $f$ 의 최댓값 $2$ (<span class=\"nw\">$r=2$,</span> 즉 <span class=\"nw\">$\\theta=-\\frac\\pi2$,</span> 점 <span class=\"nw\">$(0,-2)$),</span> 최솟값 $0$",
        "후보 비교: 최댓값 $2$ (점 <span class=\"nw\">$(0,-2)$),</span> 최솟값 $-\\tfrac14$ (점 <span class=\"nw\">$(0,-\\tfrac12)$)</span>"
       ]
      ]
     ],
     "types": [
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "라그랑주 승수법 (제약 2개)",
     "ref": "2025 중간 8번 유형",
     "stem": "라그랑주 승수법을 이용하여 곡면 $x^2+y^2+z^4=2$ 와 평면 $y=x$ 의 교선 위에서 $f(x,y,z)=x^2+y^2+z^2$ 의 최댓값과 최솟값을 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "최댓값 $\\dfrac94$ ($x=y=\\pm\\sqrt{\\tfrac78},\\ z=\\pm\\tfrac1{\\sqrt2}\\text{),}$ 최솟값 $\\sqrt2$ (점 <span class=\"nw\">$(0,0,\\pm\\sqrt[4]2)$)</span>"
      ]
     ],
     "solution": [
      [
       "",
       [
        "$\\nabla f=\\lambda\\nabla g+\\mu\\nabla h\\text{,}$ $g=x^2+y^2+z^4,\\ h=x-y\\text{:}$ $2x=2\\lambda x+\\mu,\\ 2y=2\\lambda y-\\mu,\\ 2z=4\\lambda z^3$",
        "$x=y$ 이므로 처음 두 식을 더하고 빼면 $\\mu=0,\\ x(1-\\lambda)=0$",
        "① <span class=\"nw\">$x=0$:</span> $z^4=2$ → <span class=\"nw\">$f=z^2=\\sqrt2$.</span>&emsp;② <span class=\"nw\">$z=0$:</span> $2x^2=2$ → $f=2$",
        "③ <span class=\"nw\">$\\lambda=1,\\ z\\ne0$:</span> $z^2=\\dfrac{1}{2\\lambda}=\\dfrac12$ → $2x^2=2-\\tfrac14=\\tfrac74$ → $f=\\tfrac74+\\tfrac12=\\tfrac94$",
        "후보 $\\sqrt2\\approx1.41,\\ 2,\\ \\tfrac94$ → 최댓값 <span class=\"nw\">$\\tfrac94$,</span> 최솟값 $\\sqrt2$ (교선은 닫힌 곡선이라 둘 다 존재)"
       ]
      ]
     ],
     "types": [
      [
       "14-lagrange2",
       "제약조건 2개 라그랑주"
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "선적분의 기본정리",
     "ref": "2024 기말 2·3번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "$\\mathbf F(x,y,z)=\\big\\langle2x\\cos y-z,\\ -x^2\\sin y,\\ -x+3z^2\\big\\rangle$ 이고 $C:\\ \\mathbf r(t)=\\big\\langle1+t^3,\\ \\tfrac\\pi2\\sin\\tfrac{\\pi t}{2},\\ t^2\\big\\rangle\\ (0\\le t\\le1)$ 일 때 $\\displaystyle\\int_C\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ],
      [
       "b",
       "연속함수 $f$ 가 $\\displaystyle\\int_0^1f(u)\\,du=2$ 를 만족한다. $C$ 가 $(0,0,0)$ 에서 $(2,0,1)$ 까지 가는 임의의 매끄러운 곡선일 때 $\\displaystyle\\int_Cf(x+y-z)\\,(dx+dy-dz)$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$-2$"
      ],
      [
       "b",
       "$2$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$P_y=-2x\\sin y=Q_x,\\ P_z=-1=R_x,\\ Q_z=0=R_y$ → 보존장",
        "$f=x^2\\cos y-xz+z^3$ (<span class=\"nw\">$f_x=2x\\cos y-z$,</span> <span class=\"nw\">$f_y=-x^2\\sin y$,</span> <span class=\"nw\">$f_z=-x+3z^2$)</span>",
        "$\\mathbf r(0)=(1,0,0)\\text{,}$ $\\mathbf r(1)=\\big(2,\\tfrac\\pi2,1\\big)$ → $f\\big(2,\\tfrac\\pi2,1\\big)-f(1,0,0)=(0-2+1)-1=-2$"
       ]
      ],
      [
       "b",
       [
        "$g(x,y,z)=\\displaystyle\\int_0^{x+y-z}f(u)\\,du$ 로 두면 $\\nabla g=f(x+y-z)\\langle1,1,-1\\rangle$",
        "값 $=g(2,0,1)-g(0,0,0)=\\displaystyle\\int_0^{1}f(u)\\,du=2$"
       ]
      ]
     ],
     "types": [
      [
       "16-ftli",
       "선적분의 기본정리"
      ],
      [
       "16-conserv",
       "보존장 판정·퍼텐셜"
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "그린 정리",
     "ref": "2024 기말 1번 · 2022 기말 블럭2 4번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "$C$ 가 원 $x^2+y^2=9$ (반시계 방향)일 때 $\\displaystyle\\oint_C\\big(3y-e^{\\sin x}\\big)\\,dx+\\big(7x+\\sqrt{y^4+1}\\big)\\,dy$ 를 구하시오."
      ],
      [
       "b",
       "$C$ 가 원 $x^2+y^2=4$ 의 위쪽 반원을 $(2,0)$ 에서 $(-2,0)$ 까지 가는 곡선일 때 그린 정리를 이용하여 $\\displaystyle\\int_C(x^2+y)\\,dx+(3x+y^3)\\,dy$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$36\\pi$"
      ],
      [
       "b",
       "$4\\pi-\\dfrac{16}{3}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$Q_x-P_y=7-3=4$ → $\\displaystyle\\oint_C=\\iint_D4\\,dA=4\\cdot9\\pi=36\\pi$ (직접 계산하기 힘든 항들이 모두 사라져요)"
       ]
      ],
      [
       "b",
       [
        "선분 <span class=\"nw\">$L$:</span> $(-2,0)\\to(2,0)$ 을 붙이면 $C+L$ 은 위쪽 반원판 $D$ 의 양의 방향 경계, $Q_x-P_y=3-1=2$",
        "$\\displaystyle\\oint_{C+L}=\\iint_D2\\,dA=2\\cdot2\\pi=4\\pi$",
        "<span class=\"nw\">$L$:</span> $y=0,\\ dy=0$ → $\\displaystyle\\int_L=\\int_{-2}^2x^2\\,dx=\\frac{16}{3}$ → $\\displaystyle\\int_C=4\\pi-\\frac{16}{3}$"
       ]
      ]
     ],
     "types": [
      [
       "16-green",
       "그린 정리"
      ]
     ]
    }
   ]
  },
  {
   "id": "s3",
   "no": 3,
   "title": "실전 모의고사 3회",
   "focus": "2024 중간 스타일",
   "lead": "2024학년도 중간고사 구성을 따라가요 — 임계점 + 음함수, 순서 바꾸기 + 삼중적분, 테일러로 보는 극한, 사면체·직육면체 라그랑주, 동차 꼴 연쇄법칙과 선형근사, 겹치는 원판, 2계 방향도함수, 원주→구면좌표. 9번은 2024 기말의 특이점 벡터장 유형이에요.",
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "임계점 분류 · 음함수 편미분",
     "ref": "2024 중간 1번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "$f(x,y)=x^4-4xy+2y^2$ 의 임계점을 모두 구하고 분류하시오."
      ],
      [
       "b",
       "$x^2+2y^2+3z^2+xyz=7$ 일 때 점 $(1,1,1)$ 에서 $\\dfrac{\\partial z}{\\partial x},\\ \\dfrac{\\partial z}{\\partial y}$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$(0,0)$ 안장점, $(1,1)$ 과 $(-1,-1)$ 에서 극솟값 $-1$"
      ],
      [
       "b",
       "$z_x=-\\dfrac37,\\ z_y=-\\dfrac57$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=4x^3-4y=0,\\ f_y=-4x+4y=0$ → $y=x,\\ x^3=x$ → $(0,0),\\ (1,1),\\ (-1,-1)$",
        "$f_{xx}=12x^2,\\ f_{yy}=4,\\ f_{xy}=-4$",
        "<span class=\"nw\">$(0,0)$:</span> $D=0-16\\lt 0$ → 안장점;&emsp;<span class=\"nw\">$(\\pm1,\\pm1)$:</span> $D=48-16=32>0,\\ f_{xx}=12>0$ → 극솟값 $1-4+2=-1$"
       ]
      ],
      [
       "b",
       [
        "$F=x^2+2y^2+3z^2+xyz\\text{:}$ $F_x=2x+yz=3,\\ F_y=4y+xz=5,\\ F_z=6z+xy=7$",
        "$z_x=-\\dfrac{F_x}{F_z}=-\\dfrac37\\text{,}$&emsp;$z_y=-\\dfrac{F_y}{F_z}=-\\dfrac57$"
       ]
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "14-implicit",
       "음함수 편미분"
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "이중적분 순서 바꾸기 · 삼중적분",
     "ref": "2024 중간 2번 유형",
     "stem": "다음 적분을 계산하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^1\\!\\!\\int_{y^2}^{1}y\\sin(x^2)\\,dx\\,dy$"
      ],
      [
       "b",
       "$\\displaystyle\\iiint_Ey\\,dV\\text{,}$ $E$ 는 곡면 <span class=\"nw\">$y=\\sqrt x$,</span> <span class=\"nw\">$y=x$,</span> <span class=\"nw\">$z=0$,</span> $z=x+y$ 로 둘러싸인 입체"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{1-\\cos1}{4}$"
      ],
      [
       "b",
       "$\\dfrac{11}{120}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\sin(x^2)$ 은 $x$ 로 적분할 수 없으므로 순서를 바꿔요: $0\\le y\\le1,\\ y^2\\le x\\le1$ ⟺ $0\\le x\\le1,\\ 0\\le y\\le\\sqrt x$",
        "$$\\int_0^1\\!\\!\\int_0^{\\sqrt x}y\\sin(x^2)\\,dy\\,dx=\\int_0^1\\frac x2\\sin(x^2)\\,dx=\\Big[-\\frac14\\cos(x^2)\\Big]_0^1=\\frac{1-\\cos1}{4}$$"
       ]
      ],
      [
       "b",
       [
        "$0\\le x\\le1$ 에서 $x\\le\\sqrt x$ → $E=\\{0\\le x\\le1,\\ x\\le y\\le\\sqrt x,\\ 0\\le z\\le x+y\\}$",
        "$$\\begin{aligned}\\iiint_Ey\\,dV&amp;=\\int_0^1\\!\\!\\int_x^{\\sqrt x}y(x+y)\\,dy\\,dx=\\int_0^1\\Big[\\frac{xy^2}{2}+\\frac{y^3}{3}\\Big]_x^{\\sqrt x}dx\\\\&amp;=\\int_0^1\\Big(\\frac{x^2}{2}+\\frac{x^{3/2}}{3}-\\frac{5x^3}{6}\\Big)dx=\\frac16+\\frac2{15}-\\frac5{24}=\\frac{11}{120}\\end{aligned}$$"
       ]
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-triple",
       "직교좌표 삼중적분·부피"
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "극한",
     "ref": "2024 중간 3번 유형",
     "stem": "다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{y-y\\cos x}{x^2+y^2}$"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x\\sin2y-2y\\sin x}{x^4+y^4}$"
      ]
     ],
     "answer": [
      [
       "a",
       "$0$"
      ],
      [
       "b",
       "존재하지 않음 ($y=0$ 을 따라 <span class=\"nw\">$0$,</span> $y=x$ 를 따라 <span class=\"nw\">$-\\tfrac12$)</span>"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$0\\le1-\\cos x\\le\\dfrac{x^2}{2}$ → $\\Big|\\dfrac{y(1-\\cos x)}{x^2+y^2}\\Big|\\le\\dfrac{|y|}{2}\\cdot\\dfrac{x^2}{x^2+y^2}\\le\\dfrac{|y|}{2}\\to0$ → 극한 $0$"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$y=0$:</span> 분자 $=0$ → $0$",
        "<span class=\"nw\">$y=x$:</span> $\\sin u=u-\\frac{u^3}{6}+\\cdots$ 로 분자 $=x\\big(2x-\\tfrac{8x^3}{6}\\big)-2x\\big(x-\\tfrac{x^3}{6}\\big)+\\cdots=-x^4+\\cdots$",
        "$\\dfrac{-x^4+\\cdots}{2x^4}\\to-\\dfrac12$ → 경로마다 다르므로 존재하지 않음"
       ]
      ]
     ],
     "types": [
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ],
      [
       "14-dne",
       "극한이 존재하지 않음"
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "라그랑주 승수법 (최적화)",
     "ref": "2024 중간 4번 유형",
     "stem": "라그랑주 승수법을 이용하여, 타원면 $\\dfrac{x^2}{4}+\\dfrac{y^2}{9}+z^2=1$ 에 내접하고 각 면이 좌표평면과 평행한 직육면체의 부피의 최댓값과 그때의 세 모서리 길이를 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "최대 부피 $\\dfrac{16\\sqrt3}{3}\\text{,}$ 모서리 $\\dfrac{4}{\\sqrt3},\\ 2\\sqrt3,\\ \\dfrac{2}{\\sqrt3}$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "제1팔분공간의 꼭짓점을 $(x,y,z)$ 라 하면 <span class=\"nw\">$V=8xyz$,</span> 제약 $g=\\frac{x^2}{4}+\\frac{y^2}{9}+z^2=1$",
        "$8yz=\\lambda\\frac x2,\\ 8xz=\\lambda\\frac{2y}{9},\\ 8xy=2\\lambda z$ → 각각 $x,y,z$ 를 곱하면 $8xyz=\\lambda\\frac{x^2}2=\\lambda\\frac{2y^2}{9}=2\\lambda z^2$",
        "$\\Rightarrow \\frac{x^2}{4}=\\frac{y^2}{9}=z^2\\text{,}$ 합이 $1$ 이므로 각각 $\\frac13$ → $x=\\frac{2}{\\sqrt3},\\ y=\\sqrt3,\\ z=\\frac1{\\sqrt3}$",
        "$V=8\\cdot\\frac{2}{\\sqrt3}\\cdot\\sqrt3\\cdot\\frac{1}{\\sqrt3}=\\frac{16}{\\sqrt3}=\\frac{16\\sqrt3}{3}\\text{,}$ 모서리 $2x,2y,2z$"
       ]
      ]
     ],
     "types": [
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "14-optim",
       "최적화 응용"
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "연쇄법칙 · 선형근사",
     "ref": "2024 중간 5번 유형",
     "stem": "$F$ 는 미분가능한 한 변수 함수이고 $g(x,y)=x^4F\\!\\left(\\dfrac{y}{x^2}\\right)$ (<span class=\"nw\">$x>0$)</span> 이다.",
     "parts": [
      [
       "a",
       "$x\\,g_x+2y\\,g_y-4g$ 를 구하시오."
      ],
      [
       "b",
       "$F(1)=3,\\ F'(1)=-1$ 일 때, $g$ 의 점 $(1,1)$ 에서의 선형근사를 이용해 $g(1.1,\\ 0.9)$ 의 근삿값을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$0$"
      ],
      [
       "b",
       "$4.5$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$w=\\dfrac{y}{x^2}$:</span> $g_x=4x^3F(w)+x^4F'(w)\\cdot\\Big(-\\dfrac{2y}{x^3}\\Big)=4x^3F-2xyF'\\text{,}$&emsp;$g_y=x^4F'(w)\\cdot\\dfrac{1}{x^2}=x^2F'$",
        "$x\\,g_x+2y\\,g_y=4x^4F-2x^2yF'+2x^2yF'=4x^4F=4g$ → 답 $0$ ($g(tx,t^2y)=t^4g$ 꼴이라 생기는 성질)"
       ]
      ],
      [
       "b",
       [
        "$(1,1)$ 에서 <span class=\"nw\">$w=1$:</span> <span class=\"nw\">$g=3$,</span> $g_x=4\\cdot3-2\\cdot(-1)=14\\text{,}$ $g_y=-1$",
        "$g(1.1,0.9)\\approx3+14(0.1)+(-1)(-0.1)=3+1.4+0.1=4.5$"
       ]
      ]
     ],
     "types": [
      [
       "14-chain",
       "연쇄법칙"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "극좌표 이중적분 (겹치는 원판)",
     "ref": "2024 중간 6번 유형",
     "stem": "$D_1,\\ D_2$ 가 각각 원판 $x^2+y^2\\le3$ 과 $x^2+y^2\\le2\\sqrt3\\,y$ 일 때 $\\displaystyle\\iint_{D_1\\cup D_2}(x^2+y^2)\\,dA$ 를 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "$12\\pi+\\dfrac{63\\sqrt3}{8}$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "$\\displaystyle\\iint_{D_1\\cup D_2}=\\iint_{D_1}+\\iint_{D_2}-\\iint_{D_1\\cap D_2}\\text{.}$ <span class=\"nw\">$D_2$:</span> $r\\le2\\sqrt3\\sin\\theta\\text{,}$ 두 원은 <span class=\"nw\">$\\sin\\theta=\\frac12$,</span> 즉 $\\theta=\\frac\\pi6,\\frac{5\\pi}6$ 에서 만나요",
        "$\\displaystyle\\iint_{D_1}r^2\\,dA=2\\pi\\cdot\\frac94=\\frac{9\\pi}2\\text{,}$&emsp;$\\displaystyle\\iint_{D_2}=\\int_0^\\pi\\frac{(2\\sqrt3\\sin\\theta)^4}{4}d\\theta=36\\cdot\\frac{3\\pi}8=\\frac{27\\pi}{2}$",
        "$$\\begin{aligned}\\iint_{D_1\\cap D_2}&amp;=\\int_{\\pi/6}^{5\\pi/6}\\frac94\\,d\\theta+2\\int_0^{\\pi/6}36\\sin^4\\theta\\,d\\theta\\\\&amp;=\\frac{3\\pi}{2}+72\\Big(\\frac\\pi{16}-\\frac{7\\sqrt3}{64}\\Big)=6\\pi-\\frac{63\\sqrt3}{8}\\end{aligned}$$",
        "답: $\\dfrac{9\\pi}2+\\dfrac{27\\pi}2-6\\pi+\\dfrac{63\\sqrt3}8=12\\pi+\\dfrac{63\\sqrt3}{8}$"
       ]
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "2계 방향도함수",
     "ref": "2024 중간 7번 유형",
     "stem": "<span class=\"nw\">$f(x,y)=x^3+xy^2$,</span> $\\mathbf u=\\Big\\langle\\dfrac1{\\sqrt2},\\dfrac1{\\sqrt2}\\Big\\rangle$ 이고 $D_{\\mathbf u}^2f=D_{\\mathbf u}(D_{\\mathbf u}f)$ 이다.",
     "parts": [
      [
       "a",
       "$D_{\\mathbf u}f(1,2)$ 와 $D_{\\mathbf u}^2f(1,2)$ 를 구하시오."
      ],
      [
       "b",
       "$h(x,y)=\\ln f(x,y)$ 일 때 $D_{\\mathbf u}^2h(1,2)$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$D_{\\mathbf u}f=\\dfrac{11\\sqrt2}{2},\\ D_{\\mathbf u}^2f=8$"
      ],
      [
       "b",
       "$-\\dfrac{41}{50}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=3x^2+y^2=7,\\ f_y=2xy=4$ → $D_{\\mathbf u}f=\\dfrac{7+4}{\\sqrt2}=\\dfrac{11\\sqrt2}{2}$",
        "$f_{xx}=6x=6,\\ f_{xy}=2y=4,\\ f_{yy}=2x=2$ → $D_{\\mathbf u}^2f=f_{xx}u_1^2+2f_{xy}u_1u_2+f_{yy}u_2^2=\\dfrac{6+8+2}{2}=8$"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$h=\\ln f$:</span> $D_{\\mathbf u}h=\\dfrac{D_{\\mathbf u}f}{f}\\text{,}$ $D_{\\mathbf u}^2h=\\dfrac{D_{\\mathbf u}^2f}{f}-\\dfrac{(D_{\\mathbf u}f)^2}{f^2}$ (1변수 $\\ln$ 의 2계 도함수와 같은 꼴)",
        "<span class=\"nw\">$f(1,2)=5$:</span> $D_{\\mathbf u}^2h=\\dfrac85-\\dfrac{121/2}{25}=\\dfrac{80-121}{50}=-\\dfrac{41}{50}$"
       ]
      ]
     ],
     "types": [
      [
       "14-dir",
       "방향도함수"
      ],
      [
       "14-chain2",
       "2계 연쇄법칙"
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "원주좌표 → 구면좌표 변환",
     "ref": "2024 중간 8번 유형",
     "stem": "다음 적분 $I$ 에 대하여 $$I=\\int_0^{2\\pi}\\!\\!\\int_0^{1/\\sqrt3}\\!\\!\\int_r^{\\sqrt3\\,r}zr\\,dz\\,dr\\,d\\theta+\\int_0^{2\\pi}\\!\\!\\int_{1/\\sqrt3}^{1}\\!\\!\\int_r^{1}zr\\,dz\\,dr\\,d\\theta$$",
     "parts": [
      [
       "a",
       "적분 영역 $E$ 를 설명하고 $I$ 를 구면좌표 적분 하나로 나타내시오."
      ],
      [
       "b",
       "$I$ 의 값을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "두 원뿔 $z=r$ 과 $z=\\sqrt3\\,r$ 사이, 평면 $z=1$ 아래: $\\displaystyle\\int_0^{2\\pi}\\!\\!\\int_{\\pi/6}^{\\pi/4}\\!\\!\\int_0^{\\sec\\phi}\\rho^3\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$"
      ],
      [
       "b",
       "$\\dfrac{\\pi}{6}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$r\\le z\\le\\sqrt3\\,r$:</span> 원뿔 $z=r$ (<span class=\"nw\">$\\phi=\\frac\\pi4$)</span> 안쪽이고 원뿔 $z=\\sqrt3r$ (<span class=\"nw\">$\\phi=\\frac\\pi6$)</span> 바깥쪽. 둘째 적분은 $z\\le1$ 로 잘린 부분 → $E=\\{r\\le z\\le\\sqrt3r,\\ z\\le1\\}$",
        "구면좌표: $\\frac\\pi6\\le\\phi\\le\\frac\\pi4\\text{,}$ $z=\\rho\\cos\\phi\\le1 \\iff \\rho\\le\\sec\\phi\\text{,}$ 피적분 $z\\cdot\\rho^2\\sin\\phi=\\rho^3\\cos\\phi\\sin\\phi$"
       ]
      ],
      [
       "b",
       [
        "$$\\begin{aligned}I&amp;=2\\pi\\int_{\\pi/6}^{\\pi/4}\\frac{\\sec^4\\phi}{4}\\cos\\phi\\sin\\phi\\,d\\phi=\\frac\\pi2\\int_{\\pi/6}^{\\pi/4}\\frac{\\sin\\phi}{\\cos^3\\phi}d\\phi\\\\&amp;=\\frac\\pi2\\Big[\\frac{1}{2\\cos^2\\phi}\\Big]_{\\pi/6}^{\\pi/4}=\\frac\\pi2\\Big(1-\\frac23\\Big)=\\frac\\pi6\\end{aligned}$$"
       ]
      ]
     ],
     "types": [
      [
       "15-sphconv",
       "구면좌표로 바꾸어 쓰기"
      ],
      [
       "15-cyl",
       "원주좌표"
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "특이점이 있는 벡터장의 선적분",
     "ref": "2024 기말 4번 유형",
     "stem": "$\\mathbf F(x,y)=\\dfrac{3x-y}{x^2+y^2}\\,\\mathbf i+\\dfrac{x+3y}{x^2+y^2}\\,\\mathbf j$ 에 대하여",
     "parts": [
      [
       "a",
       "$C:\\ \\mathbf r(t)=(t^2-4)\\,\\mathbf i+t\\,\\mathbf j\\ (-2\\le t\\le2)$ 일 때 $\\displaystyle\\int_C\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ],
      [
       "b",
       "타원 $\\dfrac{x^2}{4}+\\dfrac{y^2}{9}=1$ 을 반시계 방향으로 한 바퀴 돌 때 $\\displaystyle\\oint\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$-\\pi$"
      ],
      [
       "b",
       "$2\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf F=\\dfrac32\\nabla\\ln(x^2+y^2)+\\dfrac{-y\\,\\mathbf i+x\\,\\mathbf j}{x^2+y^2}$ — 앞부분은 기울기장, 뒷부분의 선적분은 원점에 대한 각 $\\theta$ 의 변화량",
        "시작 <span class=\"nw\">$(0,-2)$,</span> 끝 <span class=\"nw\">$(0,2)$:</span> $x^2+y^2$ 가 둘 다 $4$ → 첫 부분 $0$",
        "$C$ 는 $(0,-2)\\to(-4,0)\\to(0,2)$ 로 원점의 왼쪽을 돌아가요: $\\theta$ 가 $\\frac{3\\pi}2\\to\\pi\\to\\frac\\pi2$ (시계 방향) → $\\Delta\\theta=-\\pi$",
        "답 $0+(-\\pi)=-\\pi$"
       ]
      ],
      [
       "b",
       [
        "닫힌 곡선이라 기울기장 부분은 <span class=\"nw\">$0$,</span> 원점을 반시계로 한 바퀴 감으므로 각의 변화 $2\\pi$ → $2\\pi$"
       ]
      ]
     ],
     "types": [
      [
       "16-singular",
       "특이점이 있는 벡터장"
      ],
      [
       "16-ftli",
       "선적분의 기본정리"
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "구면좌표 삼중적분",
     "ref": "2024 중간 10번 유형",
     "stem": "$E$ 가 곡면 $(x^2+y^2+z^2)^{3/2}=z^2$ 으로 둘러싸인 입체 중 $z\\ge0$ 인 부분일 때,",
     "parts": [
      [
       "a",
       "$E$ 의 부피를 구하시오."
      ],
      [
       "b",
       "$\\displaystyle\\iiint_Ez\\,dV$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{2\\pi}{21}$"
      ],
      [
       "b",
       "$\\dfrac{\\pi}{20}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\rho^3=\\rho^2\\cos^2\\phi$ → 곡면 <span class=\"nw\">$\\rho=\\cos^2\\phi$,</span> $E=\\{0\\le\\theta\\le2\\pi,\\ 0\\le\\phi\\le\\frac\\pi2,\\ 0\\le\\rho\\le\\cos^2\\phi\\}$",
        "$V=2\\pi\\displaystyle\\int_0^{\\pi/2}\\frac{\\cos^6\\phi}{3}\\sin\\phi\\,d\\phi=\\frac{2\\pi}{3}\\cdot\\frac17=\\frac{2\\pi}{21}$"
       ]
      ],
      [
       "b",
       [
        "$\\displaystyle\\iiint_Ez\\,dV=2\\pi\\int_0^{\\pi/2}\\!\\!\\int_0^{\\cos^2\\phi}\\rho^3\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi=\\frac\\pi2\\int_0^{\\pi/2}\\cos^9\\phi\\sin\\phi\\,d\\phi=\\frac{\\pi}{20}$"
       ]
      ]
     ],
     "types": [
      [
       "15-sph",
       "구면좌표 삼중적분"
      ]
     ]
    }
   ]
  },
  {
   "id": "s4",
   "no": 4,
   "title": "실전 모의고사 4회",
   "focus": "2022 중간 스타일 + 16장",
   "lead": "2022학년도 중간고사(블럭 1·2)의 단골 유형을 모았어요 — 2·3변수 극한, 적분 영역 그리고 순서 바꾸기, 합성함수 연쇄법칙과 선형화, 극값, 정보로 그래디언트 복원, 원판 위 최대·최소, 접평면 조건, 판의 질량중심. 마지막 두 문항은 16장(적분으로 정의된 함수, 열린 곡선의 그린 정리)이에요.",
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "극한 (2변수 · 3변수)",
     "ref": "2022 중간 블럭1·2 1번 유형",
     "stem": "다음 극한이 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{2x^3-xy}{x^2+y^2}$"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^2y}{x^2+y^2}\\cos\\Big(\\frac{1}{x^2+y^2}\\Big)$"
      ],
      [
       "c",
       "$\\displaystyle\\lim_{(x,y,z)\\to(0,0,0)}\\frac{x^2yz}{x^2+y^2+z^2}$"
      ]
     ],
     "answer": [
      [
       "a",
       "존재하지 않음 ($y=mx$ 를 따라 <span class=\"nw\">$-\\tfrac{m}{1+m^2}$)</span>"
      ],
      [
       "b",
       "$0$"
      ],
      [
       "c",
       "$0$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\dfrac{2x^3}{x^2+y^2}$ 부분은 $|\\cdot|\\le2|x|\\to0$ 이지만 $\\dfrac{-xy}{x^2+y^2}$ 은 방향마다 달라요",
        "<span class=\"nw\">$y=mx$:</span> $\\dfrac{2x^3-mx^2}{(1+m^2)x^2}\\to-\\dfrac{m}{1+m^2}$ → $m=0$ 이면 <span class=\"nw\">$0$,</span> $m=1$ 이면 $-\\frac12$ → 존재하지 않음"
       ]
      ],
      [
       "b",
       [
        "$\\dfrac{x^2}{x^2+y^2}\\le1,\\ |\\cos(\\cdot)|\\le1$ → $|\\cdot|\\le|y|\\to0$ → 극한 $0$"
       ]
      ],
      [
       "c",
       [
        "$\\rho^2=x^2+y^2+z^2$ 라 하면 $|x^2yz|\\le\\rho^2\\cdot\\rho\\cdot\\rho=\\rho^4$ → $|\\cdot|\\le\\rho^2\\to0$ → 극한 $0$"
       ]
      ]
     ],
     "types": [
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ],
      [
       "14-dne",
       "극한이 존재하지 않음"
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "적분 순서 바꾸기",
     "ref": "2022 중간 블럭1 2번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "적분 영역을 그리고 계산하시오. $$\\int_0^1\\!\\!\\int_{x/3}^{x}e^{y^2}\\,dy\\,dx+\\int_1^3\\!\\!\\int_{x/3}^{1}e^{y^2}\\,dy\\,dx$$"
      ],
      [
       "b",
       "적분 영역을 그리고 순서를 바꾼 반복적분 하나로 나타내시오. (계산하지 않음) $$\\int_{-1}^{0}\\!\\!\\int_0^{x+1}f(x,y)\\,dy\\,dx+\\int_0^1\\!\\!\\int_0^{1-x^2}f(x,y)\\,dy\\,dx$$"
      ]
     ],
     "answer": [
      [
       "a",
       "$e-1$"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^1\\!\\!\\int_{y-1}^{\\sqrt{1-y}}f(x,y)\\,dx\\,dy$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "두 영역을 합치면 직선 <span class=\"nw\">$y=x$,</span> <span class=\"nw\">$y=\\frac x3$,</span> $y=1$ 로 둘러싸인 삼각형 → $0\\le y\\le1,\\ y\\le x\\le3y$",
        "$$\\int_0^1\\!\\!\\int_y^{3y}e^{y^2}\\,dx\\,dy=\\int_0^12ye^{y^2}\\,dy=e-1$$"
       ]
      ],
      [
       "b",
       [
        "영역: $x\\in[-1,0]$ 에서 $0\\le y\\le x+1$ (직선), $x\\in[0,1]$ 에서 $0\\le y\\le1-x^2$ (포물선)",
        "$y$ 를 고정하면 왼쪽 경계 <span class=\"nw\">$x=y-1$,</span> 오른쪽 경계 $x=\\sqrt{1-y}$ (<span class=\"nw\">$0\\le y\\le1$)</span> → $\\displaystyle\\int_0^1\\!\\!\\int_{y-1}^{\\sqrt{1-y}}f\\,dx\\,dy$"
       ]
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "연쇄법칙 · 선형화",
     "ref": "2022 중간 블럭1 3번 유형",
     "stem": "$f(x,y)=g\\big(2x-y,\\ x^2+y^2,\\ xy\\big)\\text{,}$ $g(r,s,t)=r^2s-t^2$ 일 때",
     "parts": [
      [
       "a",
       "연쇄법칙으로 $f_x(1,1),\\ f_y(1,1)$ 을 구하시오."
      ],
      [
       "b",
       "$f$ 의 점 $(1,1)$ 에서의 선형화를 구하시오."
      ],
      [
       "c",
       "(b)를 이용해 $f(1.02,\\ 0.97)$ 의 근삿값을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$f_x=8,\\ f_y=-4$"
      ],
      [
       "b",
       "$L(x,y)=1+8(x-1)-4(y-1)$"
      ],
      [
       "c",
       "$1.28$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$(x,y)=(1,1)$ ↔ <span class=\"nw\">$(r,s,t)=(1,2,1)$.</span> $g_r=2rs=4,\\ g_s=r^2=1,\\ g_t=-2t=-2$",
        "$f_x=g_r\\cdot2+g_s\\cdot2x+g_t\\cdot y=8+2-2=8$",
        "$f_y=g_r\\cdot(-1)+g_s\\cdot2y+g_t\\cdot x=-4+2-2=-4$"
       ]
      ],
      [
       "b",
       [
        "$f(1,1)=g(1,2,1)=2-1=1$ → $L(x,y)=1+8(x-1)-4(y-1)$"
       ]
      ],
      [
       "c",
       [
        "$f(1.02,0.97)\\approx1+8(0.02)-4(-0.03)=1+0.16+0.12=1.28$"
       ]
      ]
     ],
     "types": [
      [
       "14-chain",
       "연쇄법칙"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "극값과 안장점",
     "ref": "2022 중간 블럭1 4번 유형",
     "stem": "$f(x,y)=x^3+3xy^2-3x^2-3y^2+4$ 의 극댓값, 극솟값, 안장점을 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "극댓값 <span class=\"nw\">$f(0,0)=4$,</span> 극솟값 <span class=\"nw\">$f(2,0)=0$,</span> 안장점 $(1,\\pm1)$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "$f_x=3x^2+3y^2-6x=0,\\ f_y=6xy-6y=6y(x-1)=0$",
        "<span class=\"nw\">$y=0$:</span> $3x^2-6x=0 \\Rightarrow x=0,2\\text{;}$&emsp;<span class=\"nw\">$x=1$:</span> $3+3y^2-6=0 \\Rightarrow y=\\pm1$",
        "$f_{xx}=6x-6,\\ f_{yy}=6x-6,\\ f_{xy}=6y$",
        "<span class=\"nw\">$(0,0)$:</span> $D=36>0,\\ f_{xx}=-6\\lt 0$ → 극댓값 <span class=\"nw\">$4$;</span>&emsp;<span class=\"nw\">$(2,0)$:</span> $D=36>0,\\ f_{xx}=6>0$ → 극솟값 <span class=\"nw\">$0$;</span>&emsp;<span class=\"nw\">$(1,\\pm1)$:</span> $D=0-36\\lt 0$ → 안장점"
       ]
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "주어진 정보로 그래디언트 구하기",
     "ref": "2022 중간 블럭1 5번 유형",
     "stem": "미분가능한 함수 $f,g$ 가 점 $P$ 에서 다음을 만족한다.<br>① $f$ 는 $P$ 에서 $\\langle2,1,-2\\rangle$ 방향으로 최대 변화율 $3$ 을 가진다.<br>② 곡면 $g(x,y,z)=1$ 의 $P$ 에서의 접평면이 평면 $x-2y+2z=0$ 과 평행하다.<br>③ $\\mathbf u=\\tfrac13\\langle2,-1,2\\rangle$ 에 대해 $D_{\\mathbf u}g(P)=-8$ 이다.&emsp;④ $f(P)=2,\\ g(P)=1$",
     "parts": [
      [
       "a",
       "$\\nabla f(P)$ 를 구하시오."
      ],
      [
       "b",
       "$\\nabla g(P)$ 를 구하시오."
      ],
      [
       "c",
       "$h=f\\,g^2$ 일 때 $P$ 에서 $\\langle1,2,2\\rangle$ 방향으로의 $h$ 의 변화율을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\langle2,1,-2\\rangle$"
      ],
      [
       "b",
       "$\\langle-3,6,-6\\rangle$"
      ],
      [
       "c",
       "$-4$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "최대 변화율의 방향 = $\\nabla f$ 방향, 크기 = $|\\nabla f|=3$ → $\\nabla f(P)=3\\cdot\\dfrac{\\langle2,1,-2\\rangle}{3}=\\langle2,1,-2\\rangle$"
       ]
      ],
      [
       "b",
       [
        "접평면의 법선이 $\\nabla g$ → $\\nabla g(P)=k\\langle1,-2,2\\rangle$",
        "$D_{\\mathbf u}g=k\\cdot\\dfrac{2+2+4}{3}=\\dfrac{8k}{3}=-8 \\Rightarrow k=-3$ → $\\nabla g(P)=\\langle-3,6,-6\\rangle$"
       ]
      ],
      [
       "c",
       [
        "$\\nabla h=g^2\\nabla f+2fg\\nabla g=\\langle2,1,-2\\rangle+4\\langle-3,6,-6\\rangle=\\langle-10,25,-26\\rangle$",
        "단위벡터 $\\tfrac13\\langle1,2,2\\rangle\\text{:}$ $D h=\\dfrac{-10+50-52}{3}=-4$"
       ]
      ]
     ],
     "types": [
      [
       "14-dir",
       "방향도함수"
      ],
      [
       "14-maxrate",
       "최대 변화율과 방향"
      ],
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "닫힌 영역의 최대·최소 (라그랑주)",
     "ref": "2022 중간 블럭2 5(b) · 블럭1 6번 유형",
     "stem": "$f(x,y)=2x^3+y^4$ 의 닫힌 원판 $D=\\{(x,y)\\mid x^2+y^2\\le1\\}$ 위에서의 최댓값과 최솟값을 구하시오. (경계에서는 라그랑주 승수법을 쓰시오.)",
     "parts": [],
     "answer": [
      [
       "",
       "최댓값 $2$ (점 <span class=\"nw\">$(1,0)$),</span> 최솟값 $-2$ (점 <span class=\"nw\">$(-1,0)$)</span>"
      ]
     ],
     "solution": [
      [
       "",
       [
        "내부: $f_x=6x^2=0,\\ f_y=4y^3=0$ → <span class=\"nw\">$(0,0)$,</span> $f=0$",
        "경계 <span class=\"nw\">$x^2+y^2=1$:</span> $6x^2=2\\lambda x,\\ 4y^3=2\\lambda y$ → ($x=0$ 또는 <span class=\"nw\">$\\lambda=3x$)</span> 그리고 ($y=0$ 또는 <span class=\"nw\">$\\lambda=2y^2$)</span>",
        "<span class=\"nw\">$x=0$:</span> <span class=\"nw\">$(0,\\pm1)$,</span> <span class=\"nw\">$f=1$.</span>&emsp;<span class=\"nw\">$y=0$:</span> <span class=\"nw\">$(\\pm1,0)$,</span> <span class=\"nw\">$f=\\pm2$.</span>&emsp;둘 다 아니면 $3x=2y^2=2(1-x^2)$ → $2x^2+3x-2=0$ → $x=\\frac12,\\ y^2=\\frac34\\text{,}$ $f=\\frac14+\\frac9{16}=\\frac{13}{16}$",
        "후보 $0,\\ 1,\\ \\pm2,\\ \\frac{13}{16}$ 비교 → 최댓값 $2$ (<span class=\"nw\">$(1,0)$),</span> 최솟값 $-2$ (<span class=\"nw\">$(-1,0)$)</span>"
       ]
      ]
     ],
     "types": [
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ],
      [
       "14-lagrange",
       "라그랑주 승수"
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "접평면 조건 (타원면 · 포물면)",
     "ref": "2022 중간 블럭1 7번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "평면 $x+y+mz=3$ 이 타원면 $x^2+\\dfrac{y^2}{4}+\\dfrac{z^2}{2}=1$ 에 접할 때 양수 $m$ 을 구하시오."
      ],
      [
       "b",
       "(a)의 $m$ 에 대해 평면 $x+y+mz=3$ 이 포물면 $z=x^2+y^2+k$ 에도 접할 때 실수 $k$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$m=\\sqrt2$"
      ],
      [
       "b",
       "$k=\\dfrac{3\\sqrt2}{2}+\\dfrac14$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "접점 $(a,b,c)$ 에서의 접평면: $ax+\\dfrac b4y+\\dfrac c2z=1\\text{.}$ 이것이 $\\dfrac x3+\\dfrac y3+\\dfrac m3z=1$ 과 같아야 하므로 $a=\\tfrac13,\\ b=\\tfrac43,\\ c=\\tfrac{2m}{3}$",
        "타원면 위: $\\tfrac19+\\tfrac{16}{9}\\cdot\\tfrac14+\\tfrac{4m^2}{9}\\cdot\\tfrac12=1 \\Rightarrow \\tfrac{5}{9}+\\tfrac{2m^2}{9}=1 \\Rightarrow m^2=2$ → $m=\\sqrt2$"
       ]
      ],
      [
       "b",
       [
        "평면: $z=\\dfrac{3-x-y}{\\sqrt2}\\text{.}$ 포물면의 $(a,b)$ 에서 접평면 기울기 $2a=2b=-\\dfrac1{\\sqrt2}$ → $a=b=-\\dfrac{\\sqrt2}{4}$",
        "접점의 높이 $a^2+b^2+k=\\tfrac14+k$ 가 평면 위의 값 $\\dfrac{3-a-b}{\\sqrt2}=\\dfrac{3}{\\sqrt2}+\\dfrac12$ 와 같아야 함",
        "$k=\\dfrac{3}{\\sqrt2}+\\dfrac14=\\dfrac{3\\sqrt2}{2}+\\dfrac14$"
       ]
      ]
     ],
     "types": [
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "판의 질량 · 질량중심",
     "ref": "2022 중간 블럭1 8번 유형",
     "stem": "판이 영역 $D=\\{(x,y)\\mid x^2+y^2\\le2y,\\ x^2+y^2\\ge1,\\ x\\ge0\\}$ 을 차지하고 밀도가 $\\rho(x,y)=x$ 일 때",
     "parts": [
      [
       "a",
       "판의 질량을 구하시오."
      ],
      [
       "b",
       "질량중심의 $y$ 좌표를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{11}{24}$"
      ],
      [
       "b",
       "$\\bar y=\\dfrac{27}{22}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$r=2\\sin\\theta$ 와 $r=1$ 의 교점 <span class=\"nw\">$\\theta=\\frac\\pi6$,</span> $x\\ge0$ → $D:\\ \\frac\\pi6\\le\\theta\\le\\frac\\pi2,\\ 1\\le r\\le2\\sin\\theta$",
        "$$\\begin{aligned}m&amp;=\\int_{\\pi/6}^{\\pi/2}\\!\\!\\int_1^{2\\sin\\theta}r^2\\cos\\theta\\,dr\\,d\\theta=\\int_{\\pi/6}^{\\pi/2}\\frac{8\\sin^3\\theta-1}{3}\\cos\\theta\\,d\\theta\\\\&amp;=\\frac13\\Big[2\\sin^4\\theta-\\sin\\theta\\Big]_{\\pi/6}^{\\pi/2}=\\frac13\\Big(1-\\big(\\tfrac18-\\tfrac12\\big)\\Big)=\\frac{11}{24}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$$\\begin{aligned}M_x&amp;=\\iint_Dy\\,\\rho\\,dA=\\int_{\\pi/6}^{\\pi/2}\\!\\!\\int_1^{2\\sin\\theta}r^3\\sin\\theta\\cos\\theta\\,dr\\,d\\theta\\\\&amp;=\\frac14\\Big[\\frac{16\\sin^6\\theta}{6}-\\frac{\\sin^2\\theta}{2}\\Big]_{\\pi/6}^{\\pi/2}=\\frac14\\Big(\\frac{13}{6}+\\frac1{12}\\Big)=\\frac{9}{16}\\end{aligned}$$",
        "$\\bar y=\\dfrac{9/16}{11/24}=\\dfrac{27}{22}$"
       ]
      ]
     ],
     "types": [
      [
       "15-mass",
       "질량·질량중심"
      ],
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "선적분의 기본정리 (적분으로 정의된 함수)",
     "ref": "2024 기말 3번 유형",
     "stem": "연속함수 $f$ 가 $\\displaystyle\\int_0^1f(u)\\,du=2,\\ \\int_0^1uf(u)\\,du=\\frac12$ 를 만족하고 $g(x,y,z)=\\displaystyle\\int_0^{xy-z}f(u)\\,du$ 이다.",
     "parts": [
      [
       "a",
       "$C$ 가 $(1,1,1)$ 에서 $(1,1,0)$ 까지 가는 임의의 매끄러운 곡선일 때 $\\displaystyle\\int_Cf(xy-z)\\,(y\\,dx+x\\,dy-dz)$ 를 구하시오."
      ],
      [
       "b",
       "$C$ 가 $(0,0,0)$ 에서 $(1,0,-1)$ 까지의 선분일 때 $\\displaystyle\\int_Cg(x,y,z)\\,ds$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$2$"
      ],
      [
       "b",
       "$\\dfrac{3\\sqrt2}{2}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\nabla g=f(xy-z)\\,\\langle y,\\ x,\\ -1\\rangle$ → 피적분 벡터장이 $\\nabla g$",
        "값 $=g(1,1,0)-g(1,1,1)=\\displaystyle\\int_0^1f\\,du-\\int_0^0f\\,du=2$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r(t)=\\langle t,0,-t\\rangle\\text{:}$ <span class=\"nw\">$xy-z=t$,</span> $ds=\\sqrt2\\,dt$ → $\\displaystyle\\int_Cg\\,ds=\\sqrt2\\int_0^1G(t)\\,dt\\text{,}$ $G(t)=\\int_0^tf$",
        "부분적분: $\\displaystyle\\int_0^1G(t)\\,dt=\\big[tG(t)\\big]_0^1-\\int_0^1tf(t)\\,dt=2-\\frac12=\\frac32$ → $\\dfrac{3\\sqrt2}{2}$"
       ]
      ]
     ],
     "types": [
      [
       "16-ftli",
       "선적분의 기본정리"
      ],
      [
       "16-scalar",
       "스칼라 선적분 ∫f ds"
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "그린 정리 (열린 곡선 닫기)",
     "ref": "2022 기말 블럭2 4번 유형",
     "stem": "$\\mathbf F(x,y)=\\big\\langle e^x+xy,\\ x^2+3x+\\sin y\\big\\rangle$ 이고 $C$ 는 원 $x^2+y^2=2x$ 의 위쪽 반원을 $(2,0)$ 에서 $(0,0)$ 까지 가는 곡선이다. 그린 정리를 이용하여 $\\displaystyle\\int_C\\mathbf F\\cdot d\\mathbf r$ 를 구하시오.",
     "parts": [],
     "answer": [
      [
       "",
       "$2\\pi+1-e^2$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "선분 <span class=\"nw\">$L$:</span> $(0,0)\\to(2,0)$ 을 붙이면 $C+L$ 은 위쪽 반원판 $D$ ($(x-1)^2+y^2\\le1,\\ y\\ge0\\text{)}$ 의 양의 방향 경계",
        "$Q_x-P_y=(2x+3)-x=x+3$ → $\\displaystyle\\iint_D(x+3)\\,dA=\\bar x\\cdot A+3A=1\\cdot\\frac\\pi2+\\frac{3\\pi}{2}=2\\pi$ (반원판의 <span class=\"nw\">$\\bar x=1$)</span>",
        "<span class=\"nw\">$L$:</span> $y=0,\\ dy=0$ → $\\displaystyle\\int_L\\mathbf F\\cdot d\\mathbf r=\\int_0^2e^x\\,dx=e^2-1$",
        "$\\displaystyle\\int_C=2\\pi-(e^2-1)=2\\pi+1-e^2$"
       ]
      ]
     ],
     "types": [
      [
       "16-green",
       "그린 정리"
      ]
     ]
    }
   ]
  },
  {
   "id": "s5",
   "no": 5,
   "title": "실전 모의고사 5회",
   "focus": "종합 심화 · 12–16장 전 범위",
   "lead": "마지막 점검용 심화 회차예요. 12–13장(교선·거리·곡선 길이)부터 정의로 구하는 편도함수, 극좌표 2계 연쇄법칙, 교선의 접선과 곡면 사이 각, 절댓값 함정이 있는 부피, 경계가 바뀌는 삼중적분 순서, 구면좌표 무게중심, 선적분, 특이점이 있는 그린 정리까지 전 범위를 다뤄요.",
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "직선·평면과 곡선의 길이 (12–13장)",
     "ref": "복습 12–13장 · 과제 12.5, 13.3 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "두 평면 $x+y+z=2$ 와 $x-y+2z=1$ 의 교선의 매개방정식을 구하시오."
      ],
      [
       "b",
       "점 $P(1,2,3)$ 과 (a)의 직선 사이의 거리를 구하시오."
      ],
      [
       "c",
       "곡선 $\\mathbf r(t)=\\big\\langle e^t,\\ e^{-t},\\ \\sqrt2\\,t\\big\\rangle$ 의 $0\\le t\\le1$ 부분의 길이를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$x=\\tfrac32+3t,\\ y=\\tfrac12-t,\\ z=-2t$"
      ],
      [
       "b",
       "$\\dfrac{2\\sqrt{70}}{7}$"
      ],
      [
       "c",
       "$e-\\dfrac1e$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "방향: $\\langle1,1,1\\rangle\\times\\langle1,-1,2\\rangle=\\langle3,-1,-2\\rangle$",
        "한 점: $z=0$ 이면 $x+y=2,\\ x-y=1$ → $\\big(\\tfrac32,\\tfrac12,0\\big)$ → $x=\\tfrac32+3t,\\ y=\\tfrac12-t,\\ z=-2t$"
       ]
      ],
      [
       "b",
       [
        "$Q=\\big(\\tfrac32,\\tfrac12,0\\big)\\text{,}$ $\\overrightarrow{QP}=\\big\\langle-\\tfrac12,\\tfrac32,3\\big\\rangle\\text{,}$ $\\overrightarrow{QP}\\times\\langle3,-1,-2\\rangle=\\langle0,8,-4\\rangle$",
        "$d=\\dfrac{|\\overrightarrow{QP}\\times\\mathbf d|}{|\\mathbf d|}=\\dfrac{\\sqrt{80}}{\\sqrt{14}}=\\dfrac{4\\sqrt5}{\\sqrt{14}}=\\dfrac{2\\sqrt{70}}{7}$"
       ]
      ],
      [
       "c",
       [
        "$|\\mathbf r'(t)|^2=e^{2t}+e^{-2t}+2=(e^t+e^{-t})^2$",
        "$L=\\displaystyle\\int_0^1(e^t+e^{-t})\\,dt=e-e^{-1}$"
       ]
      ]
     ],
     "types": [
      [
       "12-line",
       "직선의 방정식·두 직선의 위치"
      ],
      [
       "12-dist",
       "거리 공식"
      ],
      [
       "13-arc",
       "호의 길이"
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "연속성 · 정의로 구하는 편도함수",
     "ref": "2022 중간 블럭2 2번 유형",
     "stem": "$f(x,y)=\\begin{cases}\\dfrac{2x^3-y^5}{2x^2+x^2y^2+y^4} &amp; (x,y)\\ne(0,0)\\\\[2mm] 0 &amp; (x,y)=(0,0)\\end{cases}$ 에 대하여",
     "parts": [
      [
       "a",
       "$f$ 가 원점에서 연속임을 보이시오."
      ],
      [
       "b",
       "$f_x(0,0)$ 과 $f_{xx}(0,0)$ 을 구하시오."
      ],
      [
       "c",
       "$y\\ne0$ 일 때 $f_x(0,y)$ 를 구하고, $f_{xy}(0,0)$ 이 존재하지 않음을 보이시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$|f|\\le|x|+|y|\\to0$"
      ],
      [
       "b",
       "$f_x(0,0)=1,\\ f_{xx}(0,0)=0$"
      ],
      [
       "c",
       "$f_x(0,y)=0\\ (y\\ne0)$ → $\\dfrac{f_x(0,k)-f_x(0,0)}{k}=-\\dfrac1k$ 발산"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\Big|\\dfrac{2x^3}{2x^2+x^2y^2+y^4}\\Big|\\le\\dfrac{2|x|^3}{2x^2}=|x|\\text{,}$&emsp;$\\Big|\\dfrac{y^5}{2x^2+x^2y^2+y^4}\\Big|\\le\\dfrac{|y|^5}{y^4}=|y|$",
        "$|f(x,y)|\\le|x|+|y|\\to0=f(0,0)$ → 연속"
       ]
      ],
      [
       "b",
       [
        "$f(x,0)=\\dfrac{2x^3}{2x^2}=x$ (<span class=\"nw\">$x\\ne0$),</span> $f(0,0)=0$ → 모든 $x$ 에서 $f(x,0)=x$",
        "따라서 $f_x(x,0)=1$ (모든 <span class=\"nw\">$x$)</span> → <span class=\"nw\">$f_x(0,0)=1$,</span> $f_{xx}(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{1-1}{h}=0$"
       ]
      ],
      [
       "c",
       [
        "<span class=\"nw\">$y\\ne0$:</span> <span class=\"nw\">$f(0,y)=-y$,</span> $\\dfrac{f(h,y)-f(0,y)}{h}=\\dfrac{2h^2+2hy+hy^3}{2h^2+h^2y^2+y^4}\\to0$ → $f_x(0,y)=0$",
        "$f_{xy}(0,0)=\\displaystyle\\lim_{k\\to0}\\frac{f_x(0,k)-f_x(0,0)}{k}=\\lim_{k\\to0}\\frac{0-1}{k}$ → 발산, 존재하지 않음"
       ]
      ]
     ],
     "types": [
      [
       "14-defpartial",
       "연속성 판정·정의로 구하는 편도함수"
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "극좌표 연쇄법칙 (2계)",
     "ref": "강의 14.5 · 2025 중간 5번 응용",
     "stem": "$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=r\\cos\\theta,\\ y=r\\sin\\theta$ 이다.",
     "parts": [
      [
       "a",
       "$\\Big(\\dfrac{\\partial z}{\\partial r}\\Big)^2+\\dfrac{1}{r^2}\\Big(\\dfrac{\\partial z}{\\partial\\theta}\\Big)^2=\\big(f_x\\big)^2+\\big(f_y\\big)^2$ 임을 보이시오."
      ],
      [
       "b",
       "점 $(\\sqrt3,1)$ 에서 $f_x=2,\\ f_y=-1,\\ f_{xx}=1,\\ f_{xy}=0,\\ f_{yy}=3$ 일 때 $(r,\\theta)=\\big(2,\\tfrac\\pi6\\big)$ 에서 $z_{rr}$ 와 $z_{r\\theta}$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "아래 풀이"
      ],
      [
       "b",
       "$z_{rr}=\\dfrac32,\\ z_{r\\theta}=\\dfrac{\\sqrt3}{2}-1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$z_r=f_x\\cos\\theta+f_y\\sin\\theta\\text{,}$ $z_\\theta=-r\\sin\\theta f_x+r\\cos\\theta f_y$ → $\\dfrac{z_\\theta}{r}=-f_x\\sin\\theta+f_y\\cos\\theta$",
        "제곱해 더하면 교차항이 지워지고 $(\\cos^2\\theta+\\sin^2\\theta)(f_x^2+f_y^2)=f_x^2+f_y^2$"
       ]
      ],
      [
       "b",
       [
        "$(r,\\theta)=(2,\\frac\\pi6)$ ↔ <span class=\"nw\">$(x,y)=(\\sqrt3,1)$,</span> $\\cos\\theta=\\frac{\\sqrt3}2,\\ \\sin\\theta=\\frac12\\text{,}$ $x_\\theta=-r\\sin\\theta=-1,\\ y_\\theta=r\\cos\\theta=\\sqrt3$",
        "$z_{rr}=f_{xx}\\cos^2\\theta+2f_{xy}\\sin\\theta\\cos\\theta+f_{yy}\\sin^2\\theta=\\tfrac34+0+\\tfrac34=\\tfrac32$",
        "$z_{r\\theta}=\\dfrac{\\partial}{\\partial\\theta}(f_x\\cos\\theta+f_y\\sin\\theta)=-f_x\\sin\\theta+f_y\\cos\\theta+\\cos\\theta\\,(f_{xx}x_\\theta+f_{xy}y_\\theta)+\\sin\\theta\\,(f_{yx}x_\\theta+f_{yy}y_\\theta)$",
        "$=-1-\\tfrac{\\sqrt3}{2}+\\tfrac{\\sqrt3}{2}(-1)+\\tfrac12(3\\sqrt3)=\\tfrac{\\sqrt3}{2}-1$"
       ]
      ]
     ],
     "types": [
      [
       "14-chain2",
       "2계 연쇄법칙"
      ],
      [
       "14-chain",
       "연쇄법칙"
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "교선의 접선 · 두 곡면 사이의 각",
     "ref": "강의 14.6 · 2022 중간 블럭1 7번 응용",
     "stem": "구 $S_1:\\ x^2+y^2+z^2=9$ 와 곡면 $S_2:\\ z=x^2-y^2-1$ 이 점 $P(2,1,2)$ 에서 만난다.",
     "parts": [
      [
       "a",
       "$P$ 에서 두 곡면의 교선의 접선의 매개방정식을 구하시오."
      ],
      [
       "b",
       "$P$ 에서 두 곡면이 이루는 각 $\\theta$ (법선끼리의 예각)에 대해 $\\cos\\theta$ 를 구하시오."
      ],
      [
       "c",
       "$P$ 에서 $S_2$ 의 법선이 $xy$ 평면과 만나는 점을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$x=2+3t,\\ y=1+10t,\\ z=2-8t$"
      ],
      [
       "b",
       "$\\dfrac{4\\sqrt{21}}{63}$"
      ],
      [
       "c",
       "$(10,-3,0)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\nabla F_1=\\langle2x,2y,2z\\rangle=\\langle4,2,4\\rangle\\text{,}$ $S_2$ 를 $F_2=x^2-y^2-z=1$ 로 보면 $\\nabla F_2=\\langle2x,-2y,-1\\rangle=\\langle4,-2,-1\\rangle$",
        "접선 방향 $\\nabla F_1\\times\\nabla F_2=\\langle6,20,-16\\rangle\\parallel\\langle3,10,-8\\rangle$ → $x=2+3t,\\ y=1+10t,\\ z=2-8t$"
       ]
      ],
      [
       "b",
       [
        "$\\cos\\theta=\\dfrac{|\\langle4,2,4\\rangle\\cdot\\langle4,-2,-1\\rangle|}{6\\cdot\\sqrt{21}}=\\dfrac{8}{6\\sqrt{21}}=\\dfrac{4}{3\\sqrt{21}}=\\dfrac{4\\sqrt{21}}{63}$"
       ]
      ],
      [
       "c",
       [
        "법선: $(2+4t,\\ 1-2t,\\ 2-t)\\text{,}$ $z=0$ 이면 $t=2$ → $(10,-3,0)$"
       ]
      ]
     ],
     "types": [
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ],
      [
       "13-tplane",
       "두 곡선으로 접평면"
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "닫힌 원판에서 최대·최소 (라그랑주)",
     "ref": "2022 중간 블럭2 5번 유형",
     "stem": "$f(x,y)=x^2+2y^2-x$ 의 닫힌 원판 $x^2+y^2\\le1$ 위에서의 최댓값과 최솟값을 구하시오. (경계는 라그랑주 승수법)",
     "parts": [],
     "answer": [
      [
       "",
       "최댓값 $\\dfrac94$ (점 $\\big(-\\tfrac12,\\pm\\tfrac{\\sqrt3}{2}\\big)\\text{),}$ 최솟값 $-\\dfrac14$ (점 $\\big(\\tfrac12,0\\big)\\text{)}$"
      ]
     ],
     "solution": [
      [
       "",
       [
        "내부: $f_x=2x-1=0,\\ f_y=4y=0$ → $\\big(\\tfrac12,0\\big)\\text{,}$ $f=-\\tfrac14$",
        "경계: $2x-1=2\\lambda x,\\ 4y=2\\lambda y$ → $y=0$ 또는 $\\lambda=2$",
        "<span class=\"nw\">$y=0$:</span> $(\\pm1,0)$ 에서 $f(1,0)=0,\\ f(-1,0)=2\\text{.}$&emsp;<span class=\"nw\">$\\lambda=2$:</span> $2x-1=4x \\Rightarrow x=-\\tfrac12,\\ y^2=\\tfrac34$ → $f=\\tfrac14+\\tfrac32+\\tfrac12=\\tfrac94$",
        "후보 비교 → 최댓값 <span class=\"nw\">$\\tfrac94$,</span> 최솟값 $-\\tfrac14$"
       ]
      ]
     ],
     "types": [
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ],
      [
       "14-lagrange",
       "라그랑주 승수"
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "극좌표로 부피 (구와 원기둥)",
     "ref": "2022 중간 블럭1 9번 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "원기둥 $x^2+y^2=2x$ 의 내부에서 $xy$ 평면 위, 구 $x^2+y^2+z^2=4$ 아래에 있는 입체의 부피를 구하시오."
      ],
      [
       "b",
       "구 $x^2+y^2+z^2=4$ 와 원기둥 $x^2+y^2=2x$ 의 공통 내부의 부피를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{8\\pi}{3}-\\dfrac{32}{9}$"
      ],
      [
       "b",
       "$\\dfrac{16\\pi}{3}-\\dfrac{64}{9}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "밑면 $r\\le2\\cos\\theta\\ (-\\frac\\pi2\\le\\theta\\le\\frac\\pi2)\\text{,}$ 높이 $\\sqrt{4-r^2}$",
        "$$\\begin{aligned}V&amp;=\\int_{-\\pi/2}^{\\pi/2}\\!\\!\\int_0^{2\\cos\\theta}\\sqrt{4-r^2}\\,r\\,dr\\,d\\theta=\\int_{-\\pi/2}^{\\pi/2}\\frac{8-(4\\sin^2\\theta)^{3/2}}{3}\\,d\\theta\\\\&amp;=\\frac{8\\pi}{3}-\\frac83\\int_{-\\pi/2}^{\\pi/2}|\\sin\\theta|^3d\\theta=\\frac{8\\pi}{3}-\\frac83\\cdot\\frac43=\\frac{8\\pi}3-\\frac{32}9\\end{aligned}$$",
        "주의: $(\\sin^2\\theta)^{3/2}=|\\sin\\theta|^3$ — 절댓값을 빼먹으면 $0$ 이 되어 틀려요"
       ]
      ],
      [
       "b",
       [
        "위아래 대칭이므로 (a)의 2배: $\\dfrac{16\\pi}{3}-\\dfrac{64}{9}$"
       ]
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "삼중적분 순서 바꾸기",
     "ref": "2022 중간 블럭2 8(a) 유형",
     "stem": "$I=\\displaystyle\\int_0^1\\!\\!\\int_0^{1-x^2}\\!\\!\\int_0^{1-x}f(x,y,z)\\,dy\\,dz\\,dx$ 에 대하여",
     "parts": [
      [
       "a",
       "$I$ 를 $dx\\,dz\\,dy$ 순서로 다시 쓰시오."
      ],
      [
       "b",
       "$f=1$ 일 때 $I$ (적분 영역의 부피)를 구하시오."
      ],
      [
       "c",
       "$f=y$ 일 때 $I$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\displaystyle\\int_0^1\\!\\!\\int_0^{2y-y^2}\\!\\!\\int_0^{1-y}f\\,dx\\,dz\\,dy+\\int_0^1\\!\\!\\int_{2y-y^2}^{1}\\!\\!\\int_0^{\\sqrt{1-z}}f\\,dx\\,dz\\,dy$"
      ],
      [
       "b",
       "$\\dfrac{5}{12}$"
      ],
      [
       "c",
       "$\\dfrac{3}{20}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역: $0\\le x\\le1,\\ 0\\le z\\le1-x^2,\\ 0\\le y\\le1-x$ → $(y,z)$ 를 고정하면 $x$ 는 $x\\le1-y$ 와 $x\\le\\sqrt{1-z}$ 를 모두 만족",
        "$1-y\\le\\sqrt{1-z} \\iff z\\le1-(1-y)^2=2y-y^2$ → 그 아래에서는 <span class=\"nw\">$x\\le1-y$,</span> 위에서는 $x\\le\\sqrt{1-z}$ (경계가 바뀌는 곡선으로 나눠요)"
       ]
      ],
      [
       "b",
       [
        "$V=\\displaystyle\\int_0^1(1-x)(1-x^2)\\,dx=\\int_0^1(1-x-x^2+x^3)\\,dx=1-\\frac12-\\frac13+\\frac14=\\frac5{12}$"
       ]
      ],
      [
       "c",
       [
        "$\\displaystyle\\int_0^1\\!\\!\\int_0^{1-x^2}\\frac{(1-x)^2}{2}\\,dz\\,dx=\\frac12\\int_0^1(1-x)^3(1+x)\\,dx\\overset{w=1-x}{=}\\frac12\\int_0^1w^3(2-w)\\,dw=\\frac12\\Big(\\frac12-\\frac15\\Big)=\\frac{3}{20}$"
       ]
      ]
     ],
     "types": [
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ],
      [
       "15-triple",
       "직교좌표 삼중적분·부피"
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "구면좌표 (무게중심)",
     "ref": "2022 중간 블럭2 10번 유형",
     "stem": "$E$ 가 두 구 <span class=\"nw\">$x^2+y^2+z^2=1$,</span> $x^2+y^2+z^2=4$ 사이에 있고 원뿔 $z=\\sqrt{\\dfrac{x^2+y^2}{3}}$ 위쪽에 있는 밀도가 일정한 입체일 때",
     "parts": [
      [
       "a",
       "$E$ 의 부피를 구하시오."
      ],
      [
       "b",
       "$E$ 의 질량중심을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{7\\pi}{3}$"
      ],
      [
       "b",
       "$\\Big(0,\\ 0,\\ \\dfrac{135}{112}\\Big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "원뿔: $\\tan\\phi=\\dfrac{r}{z}=\\sqrt3$ → <span class=\"nw\">$\\phi=\\frac\\pi3$.</span> $E=\\{1\\le\\rho\\le2,\\ 0\\le\\phi\\le\\frac\\pi3\\}$",
        "$V=2\\pi\\cdot\\big(1-\\cos\\tfrac\\pi3\\big)\\cdot\\dfrac{8-1}{3}=2\\pi\\cdot\\dfrac12\\cdot\\dfrac73=\\dfrac{7\\pi}{3}$"
       ]
      ],
      [
       "b",
       [
        "대칭 → $\\bar x=\\bar y=0$",
        "$\\displaystyle\\iiint z\\,dV=2\\pi\\int_0^{\\pi/3}\\cos\\phi\\sin\\phi\\,d\\phi\\int_1^2\\rho^3d\\rho=2\\pi\\cdot\\frac38\\cdot\\frac{15}{4}=\\frac{45\\pi}{16}$",
        "$\\bar z=\\dfrac{45\\pi/16}{7\\pi/3}=\\dfrac{135}{112}$"
       ]
      ]
     ],
     "types": [
      [
       "15-sph",
       "구면좌표 삼중적분"
      ],
      [
       "15-mass",
       "질량·질량중심"
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "스칼라·벡터 선적분",
     "ref": "2022 기말 블럭2 2번 · 2024 기말 2(a) 유형",
     "stem": "",
     "parts": [
      [
       "a",
       "곡선 $\\mathbf r(t)=\\Big\\langle t,\\ \\dfrac{2\\sqrt2}{3}t^{3/2},\\ \\dfrac{t^2}{2}\\Big\\rangle\\ (0\\le t\\le1)$ 모양의 철사의 밀도가 $\\delta(x,y,z)=1+x$ 일 때 철사의 질량을 구하시오."
      ],
      [
       "b",
       "$\\mathbf F(x,y,z)=\\langle z,\\ x,\\ y\\rangle$ 가 나선 $\\mathbf r(t)=\\langle\\cos t,\\ \\sin t,\\ t\\rangle\\ (0\\le t\\le2\\pi)$ 을 따라 입자를 옮길 때 한 일을 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac73$"
      ],
      [
       "b",
       "$3\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'=\\langle1,\\ \\sqrt2\\,t^{1/2},\\ t\\rangle\\text{,}$ $|\\mathbf r'|^2=1+2t+t^2=(1+t)^2$ → $ds=(1+t)\\,dt$",
        "$m=\\displaystyle\\int_0^1(1+t)(1+t)\\,dt=\\Big[\\frac{(1+t)^3}{3}\\Big]_0^1=\\frac{8-1}{3}=\\frac73$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf F(\\mathbf r(t))\\cdot\\mathbf r'(t)=\\langle t,\\cos t,\\sin t\\rangle\\cdot\\langle-\\sin t,\\cos t,1\\rangle=-t\\sin t+\\cos^2t+\\sin t$",
        "$\\displaystyle\\int_0^{2\\pi}(-t\\sin t)\\,dt=\\Big[t\\cos t-\\sin t\\Big]_0^{2\\pi}=2\\pi\\text{,}$ $\\displaystyle\\int_0^{2\\pi}\\cos^2t\\,dt=\\pi\\text{,}$ $\\displaystyle\\int_0^{2\\pi}\\sin t\\,dt=0$ → $W=3\\pi$"
       ]
      ]
     ],
     "types": [
      [
       "16-scalar",
       "스칼라 선적분 ∫f ds"
      ],
      [
       "16-vector",
       "벡터 선적분·일"
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "그린 정리와 특이점",
     "ref": "2022 기말 블럭1 3번 · 2024 기말 4번 응용",
     "stem": "$\\mathbf F(x,y)=\\Big\\langle\\dfrac{-y}{x^2+y^2}+y,\\ \\dfrac{x}{x^2+y^2}+2x\\Big\\rangle$ 에 대하여 (모두 반시계 방향)",
     "parts": [
      [
       "a",
       "원 $(x-2)^2+y^2=9$ 를 따라 $\\displaystyle\\oint\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ],
      [
       "b",
       "원 $(x-5)^2+y^2=4$ 를 따라 $\\displaystyle\\oint\\mathbf F\\cdot d\\mathbf r$ 를 구하시오."
      ]
     ],
     "answer": [
      [
       "a",
       "$11\\pi$"
      ],
      [
       "b",
       "$4\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf F=\\mathbf F_1+\\mathbf F_2\\text{,}$ $\\mathbf F_1=\\dfrac{\\langle-y,x\\rangle}{x^2+y^2}$ (원점에서만 정의되지 않음, <span class=\"nw\">$Q_x=P_y$),</span> $\\mathbf F_2=\\langle y,2x\\rangle$ (<span class=\"nw\">$Q_x-P_y=1$)</span>",
        "원 $(x-2)^2+y^2=9$ 는 원점을 감싸요 (<span class=\"nw\">$2\\lt 3$).</span> <span class=\"nw\">$\\mathbf F_1$:</span> 원점을 감싸는 곡선을 따라 항상 $2\\pi$ (작은 원과 사이 영역에 그린 정리)",
        "<span class=\"nw\">$\\mathbf F_2$:</span> 그린 정리로 넓이 $9\\pi$ → 합 $2\\pi+9\\pi=11\\pi$"
       ]
      ],
      [
       "b",
       [
        "원 $(x-5)^2+y^2=4$ 는 원점을 감싸지 않음 → $\\mathbf F_1$ 부분은 그린 정리로 $0$",
        "$\\mathbf F_2$ 부분은 넓이 $4\\pi$ → $4\\pi$"
       ]
      ]
     ],
     "types": [
      [
       "16-singular",
       "특이점이 있는 벡터장"
      ],
      [
       "16-green",
       "그린 정리"
      ]
     ]
    }
   ]
  }
 ]
};

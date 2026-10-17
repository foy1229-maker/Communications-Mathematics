/* 자동 생성 파일 — tools/mock_sets.py 를 고친 뒤 tools/build.py 로 다시 만드세요. */
window.CM_MOCK = {
 "topics": [
  [
   1,
   "극좌표 꽃잎(장미곡선) 이중적분"
  ],
  [
   2,
   "라그랑주 승수법"
  ],
  [
   3,
   "다변수 극한의 존재성"
  ],
  [
   4,
   "미분가능성의 정의"
  ],
  [
   5,
   "원주좌표 삼중적분"
  ],
  [
   6,
   "구면좌표 삼중적분"
  ],
  [
   7,
   "u·v 변수변환 (야코비안)"
  ],
  [
   8,
   "적분 순서 바꾸기 (이중·삼중)"
  ],
  [
   9,
   "그린 정리 · 곡선 나누어 직접 계산"
  ],
  [
   10,
   "편도함수와 그래디언트"
  ],
  [
   11,
   "곡선의 길이"
  ],
  [
   12,
   "연쇄법칙"
  ],
  [
   13,
   "스칼라 사영·벡터 사영 (comp·proj)"
  ],
  [
   14,
   "접평면과 그래디언트"
  ],
  [
   15,
   "2계 도함수 판정법 (극값·안장점)"
  ]
 ],
 "sets": [
  {
   "id": "a",
   "no": 1,
   "label": "A",
   "title": "모의고사 A세트",
   "focus": "15개 주제 · 10문항 · 각 10점",
   "lead": "15개 주제를 10문항에 모두 담은 첫 번째 세트예요. 곡선의 길이와 사영으로 가볍게 시작해서 장미곡선 적분, 극한과 미분가능성의 정의, 그린 정리(두 방법), 원주·구면좌표, 극값과 닫힌 영역, 극좌표 연쇄법칙, u·v 변수변환, 라그랑주와 접평면, 적분 순서 바꾸기까지 단원 순서를 섞어 배치했어요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
   "mins": 81,
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "곡선의 길이 · 사영(comp·proj)",
     "ref": "13.3 · 12.3 · 13.2",
     "mins": 6,
     "topics": [
      [
       11,
       "곡선의 길이"
      ],
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ]
     ],
     "types": [
      [
       "13-arc",
       "호의 길이"
      ],
      [
       "12-proj",
       "정사영과 일"
      ],
      [
       "13-motion",
       "속도·속력·가속도"
      ]
     ],
     "stem": "곡선 $\\mathbf r(t)=\\langle 2t,\\ t^2,\\ \\ln t\\rangle\\ (t>0)$ 에 대하여",
     "parts": [
      [
       "a",
       "$1\\le t\\le e$ 부분의 길이를 구하시오. [4점]"
      ],
      [
       "b",
       "$t=1$ 에서의 속도 $\\mathbf v=\\mathbf r'(1)\\text{,}$ 가속도 $\\mathbf a=\\mathbf r''(1)$ 에 대하여 $\\operatorname{comp}_{\\mathbf v}\\mathbf a$ 와 $\\operatorname{proj}_{\\mathbf v}\\mathbf a$ 를 구하시오. [4점]"
      ],
      [
       "c",
       "$\\mathbf a$ 를 $\\mathbf v$ 에 평행한 벡터와 $\\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$e^2$"
      ],
      [
       "b",
       "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=1\\text{,}$&emsp;$\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\big\\langle\\frac23,\\ \\frac23,\\ \\frac13\\big\\rangle$"
      ],
      [
       "c",
       "$\\mathbf a=\\big\\langle\\frac23,\\frac23,\\frac13\\big\\rangle+\\big\\langle-\\frac23,\\frac43,-\\frac43\\big\\rangle\\text{,}$ 수직인 벡터의 크기 $2$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'(t)=\\big\\langle 2,\\ 2t,\\ \\frac1t\\big\\rangle\\text{,}$ $\\ |\\mathbf r'(t)|^2=4t^2+4+\\dfrac1{t^2}=\\Big(2t+\\dfrac1t\\Big)^2$ → $|\\mathbf r'(t)|=2t+\\dfrac1t$ (완전제곱이 되는지 먼저 보기)",
        "$$\\begin{aligned}L&amp;=\\int_1^e\\Big(2t+\\frac1t\\Big)dt=\\Big[t^2+\\ln t\\Big]_1^e\\\\&amp;=(e^2+1)-1=e^2\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r''(t)=\\big\\langle0,\\ 2,\\ -\\frac1{t^2}\\big\\rangle$ → $\\mathbf v=\\langle2,2,1\\rangle\\text{,}$ $\\mathbf a=\\langle0,2,-1\\rangle\\text{,}$ <span class=\"nw\">$|\\mathbf v|=3$,</span> $\\mathbf a\\cdot\\mathbf v=0+4-1=3$",
        "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=\\dfrac{\\mathbf a\\cdot\\mathbf v}{|\\mathbf v|}=\\dfrac33=1$",
        "$\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\dfrac{\\mathbf a\\cdot\\mathbf v}{|\\mathbf v|^2}\\,\\mathbf v=\\dfrac39\\langle2,2,1\\rangle=\\big\\langle\\frac23,\\frac23,\\frac13\\big\\rangle$"
       ]
      ],
      [
       "c",
       [
        "수직 성분: $\\mathbf a-\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\big\\langle-\\frac23,\\ \\frac43,\\ -\\frac43\\big\\rangle$ (확인: $\\mathbf v$ 와 내적하면 <span class=\"nw\">$\\frac{-4+8-4}{3}=0$)</span>",
        "크기 $\\dfrac{\\sqrt{4+16+16}}{3}=2\\text{.}$ 가속도를 접선 방향 $1$ 과 법선 방향 $2$ 로 나눈 셈이에요. ($a_N=\\frac{|\\mathbf v\\times\\mathbf a|}{|\\mathbf v|}=\\frac{|\\langle-4,2,4\\rangle|}{3}=2$ 와 같아요.)"
       ]
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "극좌표 이중적분 (장미곡선)",
     "ref": "15.3",
     "mins": 7,
     "topics": [
      [
       1,
       "극좌표 꽃잎(장미곡선) 이중적분"
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ],
     "stem": "$D$ 는 장미곡선 $r=2\\sin2\\theta$ 의 제1사분면에 있는 꽃잎 $\\big(0\\le\\theta\\le\\frac\\pi2\\big)$ 으로 둘러싸인 영역이다.",
     "parts": [
      [
       "a",
       "$D$ 의 넓이를 이중적분으로 구하시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_D x\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\pi}{2}$"
      ],
      [
       "b",
       "$\\dfrac{128}{105}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$D:\\ 0\\le\\theta\\le\\frac\\pi2,\\ 0\\le r\\le2\\sin2\\theta\\text{,}$ $\\ dA=r\\,dr\\,d\\theta$",
        "$$\\begin{aligned}A&amp;=\\int_0^{\\pi/2}\\!\\!\\int_0^{2\\sin2\\theta}r\\,dr\\,d\\theta\\\\&amp;=\\int_0^{\\pi/2}2\\sin^22\\theta\\,d\\theta\\\\&amp;=\\int_0^{\\pi/2}(1-\\cos4\\theta)\\,d\\theta=\\frac\\pi2\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$x=r\\cos\\theta$:</span> $$\\begin{aligned}\\iint_Dx\\,dA&amp;=\\int_0^{\\pi/2}\\!\\!\\int_0^{2\\sin2\\theta}r^2\\cos\\theta\\,dr\\,d\\theta\\\\&amp;=\\frac83\\int_0^{\\pi/2}\\sin^32\\theta\\,\\cos\\theta\\,d\\theta\\end{aligned}$$",
        "$\\sin2\\theta=2\\sin\\theta\\cos\\theta$ 이므로 $\\sin^32\\theta\\cos\\theta=8\\sin^3\\theta\\cos^4\\theta=8(1-\\cos^2\\theta)\\cos^4\\theta\\,\\sin\\theta$",
        "$u=\\cos\\theta$ 로 치환: $$\\begin{aligned}\\frac{64}{3}\\int_0^1(u^4-u^6)\\,du&amp;=\\frac{64}{3}\\Big(\\frac15-\\frac17\\Big)\\\\&amp;=\\frac{64}{3}\\cdot\\frac{2}{35}=\\frac{128}{105}\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "극한의 존재성 · 미분가능성의 정의",
     "ref": "14.2 · 14.4",
     "mins": 9,
     "topics": [
      [
       3,
       "다변수 극한의 존재성"
      ],
      [
       4,
       "미분가능성의 정의"
      ]
     ],
     "types": [
      [
       "14-dne",
       "극한이 존재하지 않음"
      ],
      [
       "14-differentiable",
       "미분가능성의 정의 (ε₁·ε₂)"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{xy^2}{x^2+y^4}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "b",
       "$f(x,y)=\\dfrac{xy^2}{x^2+y^2}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $\\ f(0,0)=0$ 일 때, $f$ 가 원점에서 연속임을 보이고 $f_x(0,0),\\ f_y(0,0)$ 을 구하시오. [3점]"
      ],
      [
       "c",
       "(b)의 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 $\\Delta z=f_x(a,b)\\Delta x+f_y(a,b)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $(\\Delta x,\\Delta y)\\to(0,0)$ 일 때 $\\varepsilon_1,\\varepsilon_2\\to0$ 인 $\\varepsilon_1,\\varepsilon_2$ 가 존재한다는 뜻이다.)"
      ]
     ],
     "answer": [
      [
       "a",
       "존재하지 않음 (<span class=\"nw\">$x$축을</span> 따라 <span class=\"nw\">$0$,</span> 곡선 $x=y^2$ 을 따라 <span class=\"nw\">$\\frac12$)</span>"
      ],
      [
       "b",
       "연속, $\\ f_x(0,0)=0,\\ f_y(0,0)=0$"
      ],
      [
       "c",
       "미분가능하지 않음 ($\\Delta y=\\Delta x$ 로 두면 $\\varepsilon_1+\\varepsilon_2=\\frac12\\text{)}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$x$축</span> $(y=0)$ 을 따라 <span class=\"nw\">$0$.</span> 직선 $y=mx$ 를 따라가도 $\\dfrac{m^2x^3}{x^2+m^4x^4}=\\dfrac{m^2x}{1+m^4x^2}\\to0$ 이라 직선만으로는 판정이 안 돼요.",
        "분모의 두 항 차수를 맞추는 곡선 $x=y^2$ 을 따라가면 $\\dfrac{y^4}{y^4+y^4}=\\dfrac12\\to\\dfrac12$",
        "경로에 따라 값이 다르므로 극한은 존재하지 않아요."
       ]
      ],
      [
       "b",
       [
        "$\\dfrac{y^2}{x^2+y^2}\\le1$ 이므로 $|f(x,y)|\\le|x|\\to0=f(0,0)$ → 조임정리로 연속",
        "$f(h,0)=0,\\ f(0,h)=0$ 이므로 $f_x(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{f(h,0)-f(0,0)}{h}=0\\text{,}$ 같은 방법으로 $f_y(0,0)=0$"
       ]
      ],
      [
       "c",
       [
        "미분가능하다고 가정하면 (b)에 의해 $\\Delta z=f(\\Delta x,\\Delta y)-f(0,0)=\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $\\varepsilon_1,\\varepsilon_2\\to0$ 이어야 해요.",
        "$\\Delta y=\\Delta x\\ (\\ne0)$ 로 두면 좌변은 $f(\\Delta x,\\Delta x)=\\dfrac{(\\Delta x)^3}{2(\\Delta x)^2}=\\dfrac{\\Delta x}{2}\\text{,}$ 우변은 $(\\varepsilon_1+\\varepsilon_2)\\Delta x$ → $\\varepsilon_1+\\varepsilon_2=\\dfrac12$",
        "그런데 $\\Delta x\\to0$ 이면 $(\\Delta x,\\Delta y)\\to(0,0)$ 이므로 $\\varepsilon_1+\\varepsilon_2\\to0$ 이어야 해요. 모순이므로 $f$ 는 원점에서 <b>미분가능하지 않아요</b>. (연속이고 편도함수도 있지만 미분가능하지 않은 예)"
       ]
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "그린 정리 · 곡선 나누어 직접 계산",
     "ref": "16.2 · 16.4",
     "mins": 9,
     "topics": [
      [
       9,
       "그린 정리 · 곡선 나누어 직접 계산"
      ]
     ],
     "types": [
      [
       "16-vector",
       "벡터 선적분·일"
      ],
      [
       "16-green",
       "그린 정리"
      ],
      [
       "16-greenarea",
       "그린 정리로 넓이"
      ]
     ],
     "stem": "$C$ 는 곡선 $y=x^2$ 과 직선 $y=x$ 로 둘러싸인 영역 $D$ 의 경계이고, 양의 방향(반시계 방향)이다. $\\displaystyle I=\\oint_C xy\\,dx+x^2\\,dy$ 에 대하여",
     "parts": [
      [
       "a",
       "$C$ 를 두 곡선으로 나누어 $I$ 를 직접 계산하시오. [4점]"
      ],
      [
       "b",
       "그린 정리를 이용해 $I$ 를 계산하고 (a)와 같은지 확인하시오. [4점]"
      ],
      [
       "c",
       "그린 정리를 이용하여 $D$ 의 넓이를 선적분으로 구하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{1}{12}$"
      ],
      [
       "b",
       "$\\dfrac{1}{12}$"
      ],
      [
       "c",
       "$\\dfrac16$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "양의 방향: $C_1$ 은 $y=x^2$ 을 따라 <span class=\"nw\">$(0,0)\\to(1,1)$,</span> $C_2$ 는 $y=x$ 를 따라 $(1,1)\\to(0,0)$",
        "$C_1:\\ x=t,\\ y=t^2\\ (0\\le t\\le1)\\text{,}$ $dx=dt,\\ dy=2t\\,dt$ → $\\displaystyle\\int_{C_1}=\\int_0^1\\big(t^3+t^2\\cdot2t\\big)\\,dt=\\int_0^13t^3\\,dt=\\frac34$",
        "$C_2:\\ x=t,\\ y=t\\ (t:1\\to0)$ → $\\displaystyle\\int_{C_2}=\\int_1^0\\big(t^2+t^2\\big)\\,dt=-\\frac23$",
        "$I=\\dfrac34-\\dfrac23=\\dfrac1{12}$"
       ]
      ],
      [
       "b",
       [
        "$P=xy,\\ Q=x^2$ → <span class=\"nw\">$Q_x-P_y=2x-x=x$,</span> $\\ D:\\ 0\\le x\\le1,\\ x^2\\le y\\le x$",
        "$$\\begin{aligned}I&amp;=\\iint_Dx\\,dA=\\int_0^1 x\\,(x-x^2)\\,dx\\\\&amp;=\\frac13-\\frac14=\\frac1{12}\\end{aligned}$$ — (a)와 같아요."
       ]
      ],
      [
       "c",
       [
        "$P=0,\\ Q=x$ 이면 $Q_x-P_y=1$ 이므로 넓이 $A=\\displaystyle\\oint_C x\\,dy$",
        "$\\displaystyle\\int_{C_1}x\\,dy=\\int_0^1t\\cdot2t\\,dt=\\frac23\\text{,}$ $\\ \\displaystyle\\int_{C_2}x\\,dy=\\int_1^0t\\,dt=-\\frac12$ → $A=\\dfrac23-\\dfrac12=\\dfrac16$",
        "(확인: $\\displaystyle\\int_0^1(x-x^2)\\,dx=\\frac16\\text{)}$"
       ]
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "원주좌표 · 구면좌표 삼중적분",
     "ref": "15.7 · 15.8",
     "mins": 9,
     "topics": [
      [
       5,
       "원주좌표 삼중적분"
      ],
      [
       6,
       "구면좌표 삼중적분"
      ]
     ],
     "types": [
      [
       "15-cyl",
       "원주좌표"
      ],
      [
       "15-sphconv",
       "구면좌표로 바꾸어 쓰기"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$E$ 가 포물면 $z=4-x^2-y^2$ 과 $xy$ 평면으로 둘러싸인 입체일 때, 원주좌표를 이용하여 $\\displaystyle\\iiint_E(x^2+y^2)\\,dV$ 를 구하시오. [5점]"
      ],
      [
       "b",
       "다음 적분을 구면좌표의 적분으로 바꾸어 쓰고, 그 값을 구하시오. [5점] $$\\int_0^{2\\pi}\\!\\!\\int_0^{\\sqrt3}\\!\\!\\int_{r/\\sqrt3}^{\\sqrt{4-r^2}}z\\,r\\,dz\\,dr\\,d\\theta$$"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{32\\pi}{3}$"
      ],
      [
       "b",
       "$\\int_0^{2\\pi}\\!\\int_0^{\\pi/3}\\!\\int_0^2\\rho^3\\cos\\phi\\,\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\text{,}$ 값 $3\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "원주좌표: $E:\\ 0\\le\\theta\\le2\\pi,\\ 0\\le r\\le2,\\ 0\\le z\\le4-r^2\\text{,}$ <span class=\"nw\">$\\ x^2+y^2=r^2$,</span> $\\ dV=r\\,dz\\,dr\\,d\\theta$",
        "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^2\\!\\!\\int_0^{4-r^2}r^3\\,dz\\,dr\\,d\\theta\\\\&amp;=2\\pi\\int_0^2(4r^3-r^5)\\,dr\\\\&amp;=2\\pi\\Big(16-\\frac{64}{6}\\Big)=\\frac{32\\pi}{3}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "아래 경계 $z=\\dfrac{r}{\\sqrt3}$ 은 원뿔: $\\tan\\phi=\\dfrac rz=\\sqrt3$ → <span class=\"nw\">$\\phi=\\dfrac\\pi3$.</span> 위 경계 $z=\\sqrt{4-r^2}$ 은 구 $\\rho=2$ (두 곡면은 $r=\\sqrt3$ 에서 만나요).",
        "$E:\\ 0\\le\\theta\\le2\\pi,\\ 0\\le\\phi\\le\\frac\\pi3,\\ 0\\le\\rho\\le2\\text{,}$ <span class=\"nw\">$\\ z=\\rho\\cos\\phi$,</span> $\\ r\\,dz\\,dr\\,d\\theta=dV=\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$",
        "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/3}\\!\\!\\int_0^2\\rho^3\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\\\&amp;=2\\pi\\cdot\\Big[\\frac{\\sin^2\\phi}{2}\\Big]_0^{\\pi/3}\\cdot\\frac{2^4}{4}\\\\&amp;=2\\pi\\cdot\\frac38\\cdot4=3\\pi\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "2계 도함수 판정법 · 닫힌 영역의 최대·최소",
     "ref": "14.7",
     "mins": 9,
     "topics": [
      [
       15,
       "2계 도함수 판정법 (극값·안장점)"
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ]
     ],
     "stem": "$f(x,y)=x^3-6xy+3y^2$ 에 대하여",
     "parts": [
      [
       "a",
       "$f$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"
      ],
      [
       "b",
       "정사각형 영역 $R=\\{(x,y)\\mid0\\le x\\le3,\\ 0\\le y\\le3\\}$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "<span class=\"nw\">$(0,0)$:</span> 안장점,&emsp;<span class=\"nw\">$(2,2)$:</span> 극솟값 $-4$"
      ],
      [
       "b",
       "최댓값 $27$ (점 <span class=\"nw\">$(3,0),\\ (0,3)$),</span> 최솟값 $-4$ (점 <span class=\"nw\">$(2,2)$)</span>"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=3x^2-6y=0,\\ \\ f_y=-6x+6y=0$ → <span class=\"nw\">$y=x$,</span> $\\ 3x^2-6x=0$ → $x=0,\\ 2$ → 임계점 $(0,0),\\ (2,2)$",
        "$f_{xx}=6x,\\ f_{yy}=6,\\ f_{xy}=-6\\text{,}$ $\\ D=f_{xx}f_{yy}-f_{xy}^2=36x-36$",
        "<span class=\"nw\">$(0,0)$:</span> $D=-36\\lt 0$ → 안장점.&emsp;<span class=\"nw\">$(2,2)$:</span> $D=36>0,\\ f_{xx}=12>0$ → 극솟값 $f(2,2)=8-24+12=-4$"
       ]
      ],
      [
       "b",
       [
        "내부 임계점은 $(2,2)$ 하나 (값 <span class=\"nw\">$-4$).</span> 경계는 네 변으로 나누어 1변수 문제로 봐요.",
        "<span class=\"nw\">$y=0$:</span> <span class=\"nw\">$f=x^3\\in[0,27]$.</span>&emsp;<span class=\"nw\">$x=0$:</span> <span class=\"nw\">$f=3y^2\\in[0,27]$.</span>&emsp;<span class=\"nw\">$x=3$:</span> $f=3y^2-18y+27=3(y-3)^2\\in[0,27]$",
        "<span class=\"nw\">$y=3$:</span> <span class=\"nw\">$f=x^3-18x+27$,</span> $\\ f'=3x^2-18=0 \\Rightarrow x=\\sqrt6$ → $f(\\sqrt6,3)=27-12\\sqrt6\\ (\\approx-2.4)\\text{,}$ 끝점에서는 $27,\\ 0$",
        "후보 비교: $27-12\\sqrt6>-4 \\iff 12\\sqrt6\\lt 31 \\iff 864\\lt 961$ → 최댓값 $27$ (점 <span class=\"nw\">$(3,0),\\ (0,3)$),</span> 최솟값 $-4$ (점 <span class=\"nw\">$(2,2)$)</span>"
       ]
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "연쇄법칙 · 그래디언트",
     "ref": "14.5 · 14.6",
     "mins": 8,
     "topics": [
      [
       12,
       "연쇄법칙"
      ],
      [
       10,
       "편도함수와 그래디언트"
      ]
     ],
     "types": [
      [
       "14-chain",
       "연쇄법칙"
      ],
      [
       "14-maxrate",
       "최대 변화율과 방향"
      ]
     ],
     "stem": "$z=f(x,y)$ 는 미분가능하고 $x=r\\cos\\theta,\\ y=r\\sin\\theta$ 이다.",
     "parts": [
      [
       "a",
       "$\\dfrac{\\partial z}{\\partial r},\\ \\dfrac{\\partial z}{\\partial\\theta}$ 를 $f_x,\\ f_y$ 로 나타내시오. [3점]"
      ],
      [
       "b",
       "$\\big(f_x\\big)^2+\\big(f_y\\big)^2=\\Big(\\dfrac{\\partial z}{\\partial r}\\Big)^2+\\dfrac{1}{r^2}\\Big(\\dfrac{\\partial z}{\\partial\\theta}\\Big)^2$ 임을 보이시오. [4점]"
      ],
      [
       "c",
       "$(r,\\theta)=\\big(2,\\frac\\pi2\\big)$ 에서 $\\dfrac{\\partial z}{\\partial r}=3,\\ \\dfrac{\\partial z}{\\partial\\theta}=-4$ 일 때, 점 $(0,2)$ 에서 $\\nabla f$ 와 $f$ 의 최대 변화율을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$z_r=f_x\\cos\\theta+f_y\\sin\\theta\\text{,}$&emsp;$z_\\theta=-f_x\\,r\\sin\\theta+f_y\\,r\\cos\\theta$"
      ],
      [
       "b",
       "아래 풀이"
      ],
      [
       "c",
       "$\\nabla f(0,2)=\\langle2,\\ 3\\rangle\\text{,}$ 최대 변화율 $\\sqrt{13}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$z_r=f_x\\dfrac{\\partial x}{\\partial r}+f_y\\dfrac{\\partial y}{\\partial r}=f_x\\cos\\theta+f_y\\sin\\theta$",
        "$z_\\theta=f_x\\dfrac{\\partial x}{\\partial\\theta}+f_y\\dfrac{\\partial y}{\\partial\\theta}=-f_x\\,r\\sin\\theta+f_y\\,r\\cos\\theta$"
       ]
      ],
      [
       "b",
       [
        "$z_r^2=f_x^2\\cos^2\\theta+2f_xf_y\\sin\\theta\\cos\\theta+f_y^2\\sin^2\\theta$",
        "$\\dfrac{1}{r^2}z_\\theta^2=f_x^2\\sin^2\\theta-2f_xf_y\\sin\\theta\\cos\\theta+f_y^2\\cos^2\\theta$",
        "더하면 교차항이 지워지고 $\\sin^2\\theta+\\cos^2\\theta=1$ 이므로 $z_r^2+\\dfrac{1}{r^2}z_\\theta^2=f_x^2+f_y^2$"
       ]
      ],
      [
       "c",
       [
        "$(r,\\theta)=\\big(2,\\frac\\pi2\\big)$ 이면 <span class=\"nw\">$(x,y)=(0,2)$,</span> $\\ \\cos\\theta=0,\\ \\sin\\theta=1$",
        "<span class=\"nw\">$z_r=f_y=3$,</span> $\\ z_\\theta=-2f_x=-4 \\Rightarrow f_x=2$ → $\\nabla f(0,2)=\\langle2,3\\rangle$",
        "최대 변화율 $|\\nabla f(0,2)|=\\sqrt{4+9}=\\sqrt{13}$ (방향 $\\frac1{\\sqrt{13}}\\langle2,3\\rangle\\text{).}$ (b)로 확인: $3^2+\\frac14(-4)^2=13$"
       ]
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "변수변환 (야코비안)",
     "ref": "15.9",
     "mins": 8,
     "topics": [
      [
       7,
       "u·v 변수변환 (야코비안)"
      ]
     ],
     "types": [
      [
       "15-change",
       "변수변환·야코비안"
      ]
     ],
     "stem": "$R$ 은 네 직선 $x-y=0,\\ x-y=2,\\ x+y=0,\\ x+y=3$ 으로 둘러싸인 영역이다. 변환 $u=x+y,\\ v=x-y$ 를 이용하여",
     "parts": [
      [
       "a",
       "야코비안 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_R(x+y)\\,e^{x^2-y^2}\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial(x,y)}{\\partial(u,v)}=-\\dfrac12$ (절댓값 <span class=\"nw\">$\\frac12$),</span> $\\ S=\\{(u,v)\\mid0\\le u\\le3,\\ 0\\le v\\le2\\}$"
      ],
      [
       "b",
       "$\\dfrac{e^6-7}{4}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x=\\dfrac{u+v}{2},\\ y=\\dfrac{u-v}{2}$ → $$\\frac{\\partial(x,y)}{\\partial(u,v)}=\\begin{vmatrix}\\frac12&amp;\\frac12\\\\[2pt]\\frac12&amp;-\\frac12\\end{vmatrix}=-\\frac14-\\frac14=-\\frac12$$",
        "네 직선이 $v=0,\\ v=2,\\ u=0,\\ u=3$ 이 되므로 $S:\\ 0\\le u\\le3,\\ 0\\le v\\le2$ (직사각형)"
       ]
      ],
      [
       "b",
       [
        "$x^2-y^2=(x+y)(x-y)=uv\\text{,}$ $\\ dA=\\Big|\\dfrac{\\partial(x,y)}{\\partial(u,v)}\\Big|\\,du\\,dv=\\dfrac12\\,du\\,dv$",
        "$$\\begin{aligned}&amp;\\iint_R(x+y)e^{x^2-y^2}\\,dA\\\\&amp;=\\frac12\\int_0^3\\!\\!\\int_0^2 u\\,e^{uv}\\,dv\\,du\\end{aligned}$$ $v$ 로 먼저 적분하면 $u\\,e^{uv}$ 가 바로 적분돼요.",
        "$$\\begin{aligned}&amp;\\frac12\\int_0^3\\Big[e^{uv}\\Big]_{v=0}^{v=2}du\\\\&amp;=\\frac12\\int_0^3\\big(e^{2u}-1\\big)\\,du\\\\&amp;=\\frac12\\Big(\\frac{e^6-1}{2}-3\\Big)=\\frac{e^6-7}{4}\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "라그랑주 승수법 · 접평면과 그래디언트",
     "ref": "14.8 · 14.6",
     "mins": 9,
     "topics": [
      [
       2,
       "라그랑주 승수법"
      ],
      [
       14,
       "접평면과 그래디언트"
      ]
     ],
     "types": [
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ]
     ],
     "stem": "타원면 $E:\\ x^2+2y^2+3z^2=66$ 과 함수 $f(x,y,z)=x+y+z$ 에 대하여",
     "parts": [
      [
       "a",
       "라그랑주 승수법으로 $E$ 위에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]"
      ],
      [
       "b",
       "$f$ 가 최댓값을 갖는 점에서 $E$ 의 접평면의 방정식을 구하시오. [3점]"
      ],
      [
       "c",
       "(b)의 접평면이 $f$ 의 등위면 $f(x,y,z)=k$ ($k$ 는 (a)의 최댓값)와 같은 평면인 이유를 그래디언트를 이용해 설명하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "최댓값 $11$ (점 <span class=\"nw\">$(6,3,2)$),</span> 최솟값 $-11$ (점 <span class=\"nw\">$(-6,-3,-2)$)</span>"
      ],
      [
       "b",
       "$x+y+z=11$"
      ],
      [
       "c",
       "최대점에서 $\\nabla f=\\lambda\\nabla g$ — 두 평면의 법선벡터가 평행하고 같은 점을 지나요."
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$g=x^2+2y^2+3z^2$,</span> $\\ \\nabla f=\\lambda\\nabla g\\text{:}$ $1=2\\lambda x,\\ 1=4\\lambda y,\\ 1=6\\lambda z$ (<span class=\"nw\">$\\lambda\\ne0$)</span> → $x=\\dfrac1{2\\lambda},\\ y=\\dfrac1{4\\lambda},\\ z=\\dfrac1{6\\lambda}$",
        "제약식에 대입: $\\dfrac{1}{\\lambda^2}\\Big(\\dfrac14+\\dfrac28+\\dfrac3{36}\\Big)=\\dfrac{11}{24\\lambda^2}=66 \\Rightarrow \\lambda^2=\\dfrac1{144},\\ \\lambda=\\pm\\dfrac1{12}$",
        "<span class=\"nw\">$\\lambda=\\frac1{12}$:</span> 점 <span class=\"nw\">$(6,3,2)$,</span> <span class=\"nw\">$f=11$.</span>&emsp;$\\lambda=-\\frac1{12}\\text{:}$ 점 <span class=\"nw\">$(-6,-3,-2)$,</span> $f=-11$ → 최댓값 <span class=\"nw\">$11$,</span> 최솟값 $-11$"
       ]
      ],
      [
       "b",
       [
        "$\\nabla g=\\langle2x,\\ 4y,\\ 6z\\rangle$ → $\\nabla g(6,3,2)=\\langle12,\\ 12,\\ 12\\rangle\\parallel\\langle1,1,1\\rangle$",
        "$(x-6)+(y-3)+(z-2)=0 \\Rightarrow x+y+z=11$"
       ]
      ],
      [
       "c",
       [
        "최대점에서 $\\nabla f=\\lambda\\nabla g$ 이므로 등위면 $f=11$ 의 법선 $\\nabla f=\\langle1,1,1\\rangle$ 과 $E$ 의 법선 $\\nabla g$ 가 평행해요.",
        "두 평면 모두 점 $(6,3,2)$ 를 지나고 법선이 평행하므로 같은 평면이에요. (평면 $x+y+z=k$ 를 밀어 가다 $E$ 에 마지막으로 접하는 순간의 $k$ 가 최댓값)"
       ]
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "적분 순서 바꾸기 (이중·삼중)",
     "ref": "15.2 · 15.6",
     "mins": 7,
     "topics": [
      [
       8,
       "적분 순서 바꾸기 (이중·삼중)"
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ]
     ],
     "stem": "적분 순서를 바꾸어 다음 값을 구하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^1\\!\\!\\int_{\\sqrt y}^1 e^{x^3}\\,dx\\,dy$ [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^1\\!\\!\\int_x^1\\!\\!\\int_0^x 6\\cos(y^3)\\,dz\\,dy\\,dx$ [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{e-1}{3}$"
      ],
      [
       "b",
       "$\\sin1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역: $0\\le y\\le1,\\ \\sqrt y\\le x\\le1$ → $0\\le x\\le1,\\ 0\\le y\\le x^2$",
        "$$\\begin{aligned}\\int_0^1\\!\\!\\int_0^{x^2}e^{x^3}\\,dy\\,dx&amp;=\\int_0^1x^2e^{x^3}\\,dx\\\\&amp;=\\Big[\\frac{e^{x^3}}{3}\\Big]_0^1=\\frac{e-1}{3}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\cos(y^3)$ 은 $y$ 로 바로 적분할 수 없으니 $y$ 를 가장 바깥으로 보내요.",
        "영역: $0\\le x\\le1,\\ x\\le y\\le1,\\ 0\\le z\\le x$ → $0\\le y\\le1,\\ 0\\le x\\le y,\\ 0\\le z\\le x$",
        "$$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^y\\!\\!\\int_0^x6\\cos(y^3)\\,dz\\,dx\\,dy\\\\&amp;=\\int_0^16\\cos(y^3)\\cdot\\frac{y^2}{2}\\,dy\\\\&amp;=\\Big[\\sin(y^3)\\Big]_0^1=\\sin1\\end{aligned}$$"
       ]
      ]
     ]
    }
   ]
  },
  {
   "id": "b",
   "no": 2,
   "label": "B",
   "title": "모의고사 B세트",
   "focus": "15개 주제 · 10문항 · 각 10점",
   "lead": "같은 15개 주제를 다른 조합으로 묶은 두 번째 세트예요. 교수님이 예고한 일변수 증분식 유도로 시작해서 그래디언트와 접평면, 평행사변형 변수변환, 장미곡선과 원의 공통부분, 합성함수·음함수 연쇄법칙, 삼각형 위 그린 정리(두 방법), 곡선의 길이와 사영, 극값 판정과 라그랑주, 이중·삼중 적분 순서, 원주·구면좌표를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
   "mins": 81,
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "미분가능성의 정의 · 극한의 존재성",
     "ref": "14.4 · 14.2",
     "mins": 9,
     "topics": [
      [
       4,
       "미분가능성의 정의"
      ],
      [
       3,
       "다변수 극한의 존재성"
      ]
     ],
     "types": [
      [
       "14-differentiable",
       "미분가능성의 정의 (ε₁·ε₂)"
      ],
      [
       "14-dne",
       "극한이 존재하지 않음"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "일변수함수 $y=g(x)$ 가 $x=a$ 에서 미분가능할 때, 미분의 정의로부터 $$\\Delta y=g'(a)\\,\\Delta x+\\varepsilon\\,\\Delta x$$ 이고 $\\Delta x\\to0$ 일 때 $\\varepsilon\\to0$ 인 $\\varepsilon$ 이 존재함을 보이시오. 단, $\\Delta y=g(a+\\Delta x)-g(a)$ 이다. [3점]"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^2y}{x^4+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "c",
       "$f(x,y)=\\dfrac{x^2y^2}{x^2+y^2}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $\\ f(0,0)=0$ 일 때, $f_x(0,0),\\ f_y(0,0)$ 을 구하고 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 $\\Delta z=f_x(a,b)\\Delta x+f_y(a,b)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $(\\Delta x,\\Delta y)\\to(0,0)$ 일 때 $\\varepsilon_1,\\varepsilon_2\\to0$ 인 $\\varepsilon_1,\\varepsilon_2$ 가 존재한다는 뜻이다.)"
      ]
     ],
     "answer": [
      [
       "a",
       "아래 풀이"
      ],
      [
       "b",
       "존재하지 않음 (<span class=\"nw\">$x$축을</span> 따라 <span class=\"nw\">$0$,</span> 곡선 $y=x^2$ 을 따라 <span class=\"nw\">$\\frac12$)</span>"
      ],
      [
       "c",
       "$f_x(0,0)=f_y(0,0)=0\\text{,}$ 미분가능 $\\Big(\\varepsilon_1=\\dfrac{\\Delta x\\,(\\Delta y)^2}{(\\Delta x)^2+(\\Delta y)^2},\\ \\varepsilon_2=0\\Big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\Delta x\\ne0$ 일 때 $\\varepsilon=\\dfrac{\\Delta y}{\\Delta x}-g'(a)$ 로 정의해요.",
        "미분의 정의 $g'(a)=\\displaystyle\\lim_{\\Delta x\\to0}\\frac{\\Delta y}{\\Delta x}$ 에서 $\\displaystyle\\lim_{\\Delta x\\to0}\\varepsilon=g'(a)-g'(a)=0$",
        "정의한 식의 양변에 $\\Delta x$ 를 곱하면 $\\Delta y=g'(a)\\Delta x+\\varepsilon\\Delta x\\text{.}$ $\\ \\Delta x=0$ 일 때는 $\\varepsilon=0$ 으로 정하면 양변이 모두 $0$ 이라 그대로 성립해요."
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$x$축</span> $(y=0)$ 을 따라 <span class=\"nw\">$0$.</span> 직선 $y=mx$ 를 따라가도 $\\dfrac{mx^3}{x^4+m^2x^2}=\\dfrac{mx}{x^2+m^2}\\to0$ 이라 직선만으로는 판정이 안 돼요.",
        "곡선 $y=x^2$ 을 따라가면 $\\dfrac{x^4}{x^4+x^4}=\\dfrac12$ → 경로마다 값이 다르므로 극한은 존재하지 않아요."
       ]
      ],
      [
       "c",
       [
        "$f(h,0)=f(0,h)=0$ 이므로 $f_x(0,0)=f_y(0,0)=0$",
        "$$\\begin{aligned}\\Delta z&amp;=f(\\Delta x,\\Delta y)-f(0,0)\\\\&amp;=\\frac{(\\Delta x)^2(\\Delta y)^2}{(\\Delta x)^2+(\\Delta y)^2}\\\\&amp;=\\underbrace{\\frac{\\Delta x\\,(\\Delta y)^2}{(\\Delta x)^2+(\\Delta y)^2}}_{\\varepsilon_1}\\,\\Delta x+\\underbrace{0}_{\\varepsilon_2}\\cdot\\Delta y\\end{aligned}$$",
        "$\\dfrac{(\\Delta y)^2}{(\\Delta x)^2+(\\Delta y)^2}\\le1$ 이므로 $|\\varepsilon_1|\\le|\\Delta x|\\to0$ (조임정리), $\\ \\varepsilon_2=0$ → 정의를 만족하므로 원점에서 <b>미분가능</b>해요."
       ]
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "그래디언트 · 방향도함수 · 접평면",
     "ref": "14.6 · 14.3",
     "mins": 8,
     "topics": [
      [
       10,
       "편도함수와 그래디언트"
      ],
      [
       14,
       "접평면과 그래디언트"
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
     ],
     "stem": "$f(x,y,z)=x\\,e^{y}+yz^2$ 과 점 $P(2,0,1)$ 에 대하여",
     "parts": [
      [
       "a",
       "$f_x,\\ f_y,\\ f_z$ 와 $\\nabla f(P)$ 를 구하시오. [2점]"
      ],
      [
       "b",
       "$P$ 에서 점 $Q(4,1,3)$ 을 향하는 방향으로의 방향도함수를 구하시오. [3점]"
      ],
      [
       "c",
       "$P$ 에서 $f$ 가 가장 빠르게 증가하는 방향(단위벡터)과 그 방향의 변화율을 구하시오. [2점]"
      ],
      [
       "d",
       "등위곡면 $f(x,y,z)=2$ 위의 점 $P$ 에서 접평면과 법선의 방정식을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$f_x=e^y,\\ f_y=xe^y+z^2,\\ f_z=2yz\\text{,}$ $\\ \\nabla f(P)=\\langle1,3,0\\rangle$"
      ],
      [
       "b",
       "$\\dfrac53$"
      ],
      [
       "c",
       "$\\dfrac{1}{\\sqrt{10}}\\langle1,3,0\\rangle\\text{,}$ 변화율 $\\sqrt{10}$"
      ],
      [
       "d",
       "접평면 <span class=\"nw\">$x+3y=2$,</span> 법선 $x=2+t,\\ y=3t,\\ z=1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=e^y,\\ \\ f_y=xe^y+z^2,\\ \\ f_z=2yz$ → $\\nabla f(2,0,1)=\\langle1,\\ 2+1,\\ 0\\rangle=\\langle1,3,0\\rangle$"
       ]
      ],
      [
       "b",
       [
        "$\\overrightarrow{PQ}=\\langle2,1,2\\rangle\\text{,}$ $|\\overrightarrow{PQ}|=3\\text{,}$ $\\ \\mathbf u=\\frac13\\langle2,1,2\\rangle$ (반드시 단위벡터로)",
        "$D_{\\mathbf u}f(P)=\\nabla f(P)\\cdot\\mathbf u=\\dfrac{2+3+0}{3}=\\dfrac53$"
       ]
      ],
      [
       "c",
       [
        "가장 빠르게 증가하는 방향은 $\\nabla f(P)$ 방향: $\\mathbf u=\\dfrac{1}{\\sqrt{10}}\\langle1,3,0\\rangle\\text{,}$ 그 변화율은 $|\\nabla f(P)|=\\sqrt{10}$"
       ]
      ],
      [
       "d",
       [
        "$f(P)=2e^0+0=2$ 이므로 $P$ 는 등위곡면 $f=2$ 위의 점이고 법선벡터는 $\\nabla f(P)=\\langle1,3,0\\rangle$",
        "접평면: $1(x-2)+3(y-0)+0(z-1)=0 \\Rightarrow x+3y=2$",
        "법선: $x=2+t,\\ y=3t,\\ z=1$"
       ]
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "변수변환 (야코비안)",
     "ref": "15.9",
     "mins": 8,
     "topics": [
      [
       7,
       "u·v 변수변환 (야코비안)"
      ]
     ],
     "types": [
      [
       "15-change",
       "변수변환·야코비안"
      ]
     ],
     "stem": "$R$ 은 네 직선 $x-2y=0,\\ x-2y=4,\\ 3x-y=1,\\ 3x-y=8$ 로 둘러싸인 평행사변형이다. 변환 $u=x-2y,\\ v=3x-y$ 를 이용하여",
     "parts": [
      [
       "a",
       "야코비안 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_R\\frac{x-2y}{3x-y}\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac15\\text{,}$ $\\ S=\\{(u,v)\\mid0\\le u\\le4,\\ 1\\le v\\le8\\}$"
      ],
      [
       "b",
       "$\\dfrac{8\\ln8}{5}=\\dfrac{24\\ln2}{5}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$$\\frac{\\partial(u,v)}{\\partial(x,y)}=\\begin{vmatrix}1&amp;-2\\\\3&amp;-1\\end{vmatrix}=-1+6=5$$ 이므로 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac{1}{5}$ (역변환 $x,y$ 를 따로 구하지 않아도 돼요)",
        "네 직선이 $u=0,\\ u=4,\\ v=1,\\ v=8$ 로 바뀌어 $S:\\ 0\\le u\\le4,\\ 1\\le v\\le8$ (직사각형)"
       ]
      ],
      [
       "b",
       [
        "$dA=\\dfrac15\\,du\\,dv$ → $$\\begin{aligned}\\iint_R\\frac{x-2y}{3x-y}\\,dA&amp;=\\frac15\\int_1^8\\!\\!\\int_0^4\\frac uv\\,du\\,dv\\\\&amp;=\\frac15\\cdot\\Big[\\frac{u^2}{2}\\Big]_0^4\\cdot\\Big[\\ln v\\Big]_1^8\\end{aligned}$$",
        "$=\\dfrac15\\cdot8\\cdot\\ln8=\\dfrac{8\\ln8}{5}=\\dfrac{24\\ln2}{5}$"
       ]
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "극좌표 이중적분 (장미곡선)",
     "ref": "15.3",
     "mins": 8,
     "topics": [
      [
       1,
       "극좌표 꽃잎(장미곡선) 이중적분"
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ],
     "stem": "장미곡선 $r=2\\cos2\\theta$ 에 대하여",
     "parts": [
      [
       "a",
       "장미곡선이 둘러싸는 영역 전체(꽃잎 4장)의 넓이를 구하시오. [4점]"
      ],
      [
       "b",
       "장미곡선의 내부이면서 원 $r=1$ 의 내부인 영역의 넓이를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$2\\pi$"
      ],
      [
       "b",
       "$\\dfrac{4\\pi}{3}-\\sqrt3$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "꽃잎 한 장: $-\\frac\\pi4\\le\\theta\\le\\frac\\pi4,\\ 0\\le r\\le2\\cos2\\theta\\text{.}$ 꽃잎 4장이 합동이고 한 장은 <span class=\"nw\">$x$축</span> 대칭이라 $0\\le\\theta\\le\\frac\\pi4$ 부분의 8배예요.",
        "넓이 <span class=\"nw\">$A$:</span> $$\\begin{aligned}&amp;8\\int_0^{\\pi/4}\\!\\!\\int_0^{2\\cos2\\theta}r\\,dr\\,d\\theta\\\\&amp;=8\\int_0^{\\pi/4}2\\cos^22\\theta\\,d\\theta\\\\&amp;=8\\int_0^{\\pi/4}(1+\\cos4\\theta)\\,d\\theta=8\\cdot\\frac\\pi4=2\\pi\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "교점: $2\\cos2\\theta=1 \\Rightarrow \\theta=\\pm\\frac\\pi6$ (오른쪽 꽃잎). 꽃잎 안에서 $|\\theta|\\le\\frac\\pi6$ 이면 원이 안쪽(<span class=\"nw\">$r\\le1$),</span> $\\frac\\pi6\\le|\\theta|\\le\\frac\\pi4$ 이면 장미곡선이 안쪽(<span class=\"nw\">$r\\le2\\cos2\\theta$)</span>",
        "꽃잎 한 장에서: $$\\begin{aligned}&amp;\\int_{-\\pi/6}^{\\pi/6}\\!\\!\\int_0^1r\\,dr\\,d\\theta\\\\&amp;\\quad+2\\int_{\\pi/6}^{\\pi/4}\\!\\!\\int_0^{2\\cos2\\theta}r\\,dr\\,d\\theta\\\\&amp;=\\frac\\pi6+2\\int_{\\pi/6}^{\\pi/4}(1+\\cos4\\theta)\\,d\\theta\\\\&amp;=\\frac\\pi6+2\\Big(\\frac\\pi{12}-\\frac{\\sqrt3}{8}\\Big)=\\frac\\pi3-\\frac{\\sqrt3}{4}\\end{aligned}$$",
        "꽃잎 4장이 합동이므로 $4\\Big(\\dfrac\\pi3-\\dfrac{\\sqrt3}4\\Big)=\\dfrac{4\\pi}3-\\sqrt3$"
       ]
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "연쇄법칙 (합성함수 · 음함수)",
     "ref": "14.5 · 14.4",
     "mins": 7,
     "topics": [
      [
       12,
       "연쇄법칙"
      ]
     ],
     "types": [
      [
       "14-chain",
       "연쇄법칙"
      ],
      [
       "14-implicit",
       "음함수 편미분"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$f$ 는 미분가능하고 $f_x(2,3)=-1,\\ f_y(2,3)=4$ 이다. $w=f(s^2t,\\ s+t)$ 일 때 $(s,t)=(1,2)$ 에서 $\\dfrac{\\partial w}{\\partial s},\\ \\dfrac{\\partial w}{\\partial t}$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "방정식 $xz+y\\,e^{z}=2$ 가 점 $(1,2,0)$ 근처에서 $z=z(x,y)$ 를 정한다. 양변을 $x,\\ y$ 에 대해 연쇄법칙으로 미분하여 $z_x(1,2),\\ z_y(1,2)$ 를 구하시오. [4점]"
      ],
      [
       "c",
       "(b)의 결과와 선형근사를 이용하여 $z(1.03,\\ 1.94)$ 의 근삿값을 구하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial w}{\\partial s}=0,\\ \\ \\dfrac{\\partial w}{\\partial t}=3$"
      ],
      [
       "b",
       "$z_x(1,2)=0,\\ \\ z_y(1,2)=-\\dfrac13$"
      ],
      [
       "c",
       "$0.02$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$x=s^2t,\\ y=s+t$:</span> $(s,t)=(1,2)$ 이면 <span class=\"nw\">$(x,y)=(2,3)$,</span> $\\ x_s=2st=4,\\ x_t=s^2=1,\\ y_s=y_t=1$",
        "$w_s=f_x\\,x_s+f_y\\,y_s=(-1)(4)+4(1)=0\\text{,}$&emsp;$w_t=f_x\\,x_t+f_y\\,y_t=(-1)(1)+4(1)=3$"
       ]
      ],
      [
       "b",
       [
        "$x$ 로 미분 ($z$ 는 $x,y$ 의 함수): $z+x\\,z_x+y\\,e^{z}z_x=0 \\Rightarrow z_x=-\\dfrac{z}{x+ye^z}$",
        "$y$ 로 미분: $x\\,z_y+e^z+y\\,e^zz_y=0 \\Rightarrow z_y=-\\dfrac{e^z}{x+ye^z}$",
        "$(1,2,0)$ 에서 $x+ye^z=3$ → $z_x=0,\\ z_y=-\\dfrac13$ (공식 $z_x=-F_x/F_z,\\ z_y=-F_y/F_z$ 와 같아요)"
       ]
      ],
      [
       "c",
       [
        "$z\\approx z(1,2)+z_x(1,2)(x-1)+z_y(1,2)(y-2)=0+0\\cdot0.03-\\dfrac13(-0.06)=0.02$"
       ]
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "그린 정리 · 곡선 나누어 직접 계산",
     "ref": "16.2 · 16.4",
     "mins": 9,
     "topics": [
      [
       9,
       "그린 정리 · 곡선 나누어 직접 계산"
      ]
     ],
     "types": [
      [
       "16-vector",
       "벡터 선적분·일"
      ],
      [
       "16-green",
       "그린 정리"
      ]
     ],
     "stem": "$C$ 는 세 점 $(0,0),\\ (2,0),\\ (2,1)$ 을 꼭짓점으로 하는 삼각형의 경계이고, 양의 방향이다. $\\displaystyle I=\\oint_C x^2y\\,dx+xy\\,dy$ 에 대하여",
     "parts": [
      [
       "a",
       "$C$ 를 세 선분으로 나누어 $I$ 를 직접 계산하시오. [5점]"
      ],
      [
       "b",
       "그린 정리를 이용해 $I$ 를 계산하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$-\\dfrac53$"
      ],
      [
       "b",
       "$-\\dfrac53$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "양의 방향(반시계): <span class=\"nw\">$C_1:(0,0)\\to(2,0)$,</span> $\\ C_2:(2,0)\\to(2,1)\\text{,}$ $\\ C_3:(2,1)\\to(0,0)$",
        "<span class=\"nw\">$C_1$:</span> $y=0,\\ dy=0$ → <span class=\"nw\">$0$.</span>&emsp;<span class=\"nw\">$C_2$:</span> $x=2,\\ dx=0$ → $\\displaystyle\\int_0^1 2y\\,dy=1$",
        "<span class=\"nw\">$C_3$:</span> 직선 $y=\\frac x2$ 위를 <span class=\"nw\">$x:2\\to0$,</span> $\\ dy=\\frac12dx$ → $$\\int_2^0\\Big(\\frac{x^3}{2}+\\frac{x^2}{4}\\Big)dx=-\\Big(2+\\frac23\\Big)=-\\frac83$$",
        "$I=0+1-\\dfrac83=-\\dfrac53$"
       ]
      ],
      [
       "b",
       [
        "$P=x^2y,\\ Q=xy$ → <span class=\"nw\">$Q_x-P_y=y-x^2$,</span> $\\ D:\\ 0\\le x\\le2,\\ 0\\le y\\le\\frac x2$",
        "$$\\begin{aligned}I&amp;=\\int_0^2\\!\\!\\int_0^{x/2}(y-x^2)\\,dy\\,dx\\\\&amp;=\\int_0^2\\Big(\\frac{x^2}{8}-\\frac{x^3}{2}\\Big)dx=\\frac13-2=-\\frac53\\end{aligned}$$ — (a)와 같아요."
       ]
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "곡선의 길이 · 사영(comp·proj)",
     "ref": "13.3 · 12.3 · 13.2",
     "mins": 7,
     "topics": [
      [
       11,
       "곡선의 길이"
      ],
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ]
     ],
     "types": [
      [
       "13-arc",
       "호의 길이"
      ],
      [
       "12-proj",
       "정사영과 일"
      ],
      [
       "13-motion",
       "속도·속력·가속도"
      ]
     ],
     "stem": "곡선 $\\mathbf r(t)=\\langle e^t\\cos t,\\ e^t\\sin t,\\ e^t\\rangle$ 에 대하여",
     "parts": [
      [
       "a",
       "$0\\le t\\le\\ln3$ 부분의 길이를 구하시오. [4점]"
      ],
      [
       "b",
       "모든 $t$ 에서 $\\operatorname{comp}_{\\mathbf r'(t)}\\mathbf k$ 가 일정함을 보이고 그 값을 구하시오. (즉, 접선과 <span class=\"nw\">$z$축</span> 사이의 각이 일정하다.) [3점]"
      ],
      [
       "c",
       "$\\mathbf r''(0)$ 을 $\\operatorname{proj}_{\\mathbf r'(0)}\\mathbf r''(0)$ 과 $\\mathbf r'(0)$ 에 수직인 벡터의 합으로 나타내시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$2\\sqrt3$"
      ],
      [
       "b",
       "$\\dfrac{1}{\\sqrt3}$"
      ],
      [
       "c",
       "$\\langle0,2,1\\rangle=\\langle1,1,1\\rangle+\\langle-1,1,0\\rangle$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'(t)=e^t\\langle\\cos t-\\sin t,\\ \\sin t+\\cos t,\\ 1\\rangle$",
        "$|\\mathbf r'(t)|^2=e^{2t}\\big[(\\cos t-\\sin t)^2+(\\sin t+\\cos t)^2+1\\big]=e^{2t}(2+1)$ → $|\\mathbf r'(t)|=\\sqrt3\\,e^t$",
        "$L=\\displaystyle\\int_0^{\\ln3}\\sqrt3\\,e^t\\,dt=\\sqrt3\\,(3-1)=2\\sqrt3$"
       ]
      ],
      [
       "b",
       [
        "$\\operatorname{comp}_{\\mathbf r'}\\mathbf k=\\dfrac{\\mathbf k\\cdot\\mathbf r'}{|\\mathbf r'|}=\\dfrac{e^t}{\\sqrt3\\,e^t}=\\dfrac1{\\sqrt3}$ — $t$ 와 무관한 상수",
        "$\\mathbf k$ 가 단위벡터라 이 값이 곧 접선과 <span class=\"nw\">$z$축</span> 사잇각의 코사인이에요: $\\cos\\alpha=\\frac1{\\sqrt3}$"
       ]
      ],
      [
       "c",
       [
        "$\\mathbf r''(t)=e^t\\langle-2\\sin t,\\ 2\\cos t,\\ 1\\rangle$ → $\\mathbf r''(0)=\\langle0,2,1\\rangle\\text{,}$ $\\ \\mathbf r'(0)=\\langle1,1,1\\rangle$",
        "$\\operatorname{proj}_{\\mathbf r'(0)}\\mathbf r''(0)=\\dfrac{0+2+1}{3}\\langle1,1,1\\rangle=\\langle1,1,1\\rangle\\text{,}$ 수직 성분 $\\langle0,2,1\\rangle-\\langle1,1,1\\rangle=\\langle-1,1,0\\rangle$",
        "(확인: $\\langle-1,1,0\\rangle\\cdot\\langle1,1,1\\rangle=0\\text{)}$ → $\\mathbf r''(0)=\\langle1,1,1\\rangle+\\langle-1,1,0\\rangle$"
       ]
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "2계 도함수 판정법 · 라그랑주 승수법",
     "ref": "14.7 · 14.8",
     "mins": 9,
     "topics": [
      [
       15,
       "2계 도함수 판정법 (극값·안장점)"
      ],
      [
       2,
       "라그랑주 승수법"
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "14-lagrange",
       "라그랑주 승수"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$f(x,y)=x^2y-x^2-2y^2$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"
      ],
      [
       "b",
       "라그랑주 승수법으로 원 $x^2+y^2=2$ 위에서 $h(x,y)=x^2+xy+y^2$ 의 최댓값과 최솟값을 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "<span class=\"nw\">$(0,0)$:</span> 극댓값 <span class=\"nw\">$0$,</span>&emsp;<span class=\"nw\">$(2,1),\\ (-2,1)$:</span> 안장점"
      ],
      [
       "b",
       "최댓값 $3$ (점 <span class=\"nw\">$(1,1),\\ (-1,-1)$),</span> 최솟값 $1$ (점 <span class=\"nw\">$(1,-1),\\ (-1,1)$)</span>"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=2xy-2x=2x(y-1)=0,\\ \\ f_y=x^2-4y=0$",
        "$x=0$ 이면 $y=0$ → <span class=\"nw\">$(0,0)$.</span>&emsp;$y=1$ 이면 $x^2=4$ → $(\\pm2,1)$",
        "$f_{xx}=2y-2,\\ f_{yy}=-4,\\ f_{xy}=2x\\text{,}$ $\\ D=-4(2y-2)-4x^2$",
        "<span class=\"nw\">$(0,0)$:</span> $D=8>0,\\ f_{xx}=-2\\lt 0$ → 극댓값 <span class=\"nw\">$f(0,0)=0$.</span>&emsp;<span class=\"nw\">$(\\pm2,1)$:</span> $D=0-16=-16\\lt 0$ → 안장점"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$g=x^2+y^2$,</span> $\\ \\nabla h=\\lambda\\nabla g\\text{:}$ $2x+y=2\\lambda x,\\ \\ x+2y=2\\lambda y$",
        "두 식을 빼면 $(x-y)(1-2\\lambda)=0\\text{,}$ 더하면 $(x+y)(3-2\\lambda)=0\\text{.}$ $x=y=0$ 은 원 위에 없으므로 $\\lambda=\\frac32$ 이고 <span class=\"nw\">$x=y$,</span> 또는 $\\lambda=\\frac12$ 이고 $x=-y$",
        "<span class=\"nw\">$x=y$:</span> $2x^2=2$ → <span class=\"nw\">$(1,1),\\ (-1,-1)$,</span> <span class=\"nw\">$\\ h=3$.</span>&emsp;<span class=\"nw\">$x=-y$:</span> <span class=\"nw\">$(1,-1),\\ (-1,1)$,</span> $\\ h=1$",
        "최댓값 <span class=\"nw\">$3$,</span> 최솟값 $1$"
       ]
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "적분 순서 바꾸기 (이중·삼중)",
     "ref": "15.2 · 15.6",
     "mins": 7,
     "topics": [
      [
       8,
       "적분 순서 바꾸기 (이중·삼중)"
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ]
     ],
     "stem": "적분 순서를 바꾸어 다음 값을 구하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^2\\!\\!\\int_{y/2}^1 e^{x^2}\\,dx\\,dy$ [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^1\\!\\!\\int_z^1\\!\\!\\int_y^1 6\\sin(x^3)\\,dx\\,dy\\,dz$ [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$e-1$"
      ],
      [
       "b",
       "$1-\\cos1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역: $0\\le y\\le2,\\ \\frac y2\\le x\\le1$ → $0\\le x\\le1,\\ 0\\le y\\le2x$",
        "$$\\begin{aligned}\\int_0^1\\!\\!\\int_0^{2x}e^{x^2}\\,dy\\,dx&amp;=\\int_0^12x\\,e^{x^2}\\,dx\\\\&amp;=\\Big[e^{x^2}\\Big]_0^1=e-1\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\sin(x^3)$ 은 $x$ 로 바로 적분할 수 없으니 $x$ 를 가장 바깥으로 보내요.",
        "영역: $0\\le z\\le1,\\ z\\le y\\le1,\\ y\\le x\\le1\\text{,}$ 즉 $0\\le z\\le y\\le x\\le1$ → $0\\le x\\le1,\\ 0\\le y\\le x,\\ 0\\le z\\le y$",
        "$$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^x\\!\\!\\int_0^y6\\sin(x^3)\\,dz\\,dy\\,dx\\\\&amp;=\\int_0^16\\sin(x^3)\\cdot\\frac{x^2}{2}\\,dx\\\\&amp;=\\Big[-\\cos(x^3)\\Big]_0^1=1-\\cos1\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "원주좌표 · 구면좌표 삼중적분",
     "ref": "15.7 · 15.8",
     "mins": 9,
     "topics": [
      [
       5,
       "원주좌표 삼중적분"
      ],
      [
       6,
       "구면좌표 삼중적분"
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
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "원기둥 $x^2+y^2=2x$ 의 내부에 있고 원뿔 $z=\\sqrt{x^2+y^2}$ 의 아래, $xy$ 평면의 위에 있는 입체의 부피를 원주좌표로 구하시오. [5점]"
      ],
      [
       "b",
       "두 구면 $x^2+y^2+z^2=1,\\ x^2+y^2+z^2=4$ 사이에 있고 원뿔 $z=\\sqrt3\\,\\sqrt{x^2+y^2}$ 의 위쪽에 있는 입체를 $E$ 라 할 때, 구면좌표로 $\\displaystyle\\iiint_E z\\,dV$ 를 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{32}{9}$"
      ],
      [
       "b",
       "$\\dfrac{15\\pi}{16}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x^2+y^2=2x \\iff r=2\\cos\\theta\\ \\big(-\\frac\\pi2\\le\\theta\\le\\frac\\pi2\\big)\\text{,}$ 높이 $0\\le z\\le r$",
        "$$\\begin{aligned}V&amp;=\\int_{-\\pi/2}^{\\pi/2}\\!\\!\\int_0^{2\\cos\\theta}\\!\\!\\int_0^r r\\,dz\\,dr\\,d\\theta\\\\&amp;=\\int_{-\\pi/2}^{\\pi/2}\\frac{8\\cos^3\\theta}{3}\\,d\\theta=\\frac83\\cdot\\frac43=\\frac{32}{9}\\end{aligned}$$",
        "$\\displaystyle\\int_{-\\pi/2}^{\\pi/2}\\cos^3\\theta\\,d\\theta=\\Big[\\sin\\theta-\\frac{\\sin^3\\theta}{3}\\Big]_{-\\pi/2}^{\\pi/2}=\\frac43$"
       ]
      ],
      [
       "b",
       [
        "원뿔 <span class=\"nw\">$z=\\sqrt3\\,r$:</span> $\\tan\\phi=\\dfrac rz=\\dfrac1{\\sqrt3}$ → <span class=\"nw\">$\\phi=\\dfrac\\pi6$.</span> 원뿔의 위쪽이므로 $0\\le\\phi\\le\\frac\\pi6\\text{,}$ $\\ 1\\le\\rho\\le2$",
        "$$\\begin{aligned}&amp;\\iiint_Ez\\,dV\\\\&amp;=\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/6}\\!\\!\\int_1^2\\rho^3\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\\\&amp;=2\\pi\\cdot\\Big[\\frac{\\sin^2\\phi}{2}\\Big]_0^{\\pi/6}\\cdot\\Big[\\frac{\\rho^4}{4}\\Big]_1^2\\\\&amp;=2\\pi\\cdot\\frac18\\cdot\\frac{15}{4}=\\frac{15\\pi}{16}\\end{aligned}$$"
       ]
      ]
     ]
    }
   ]
  },
  {
   "id": "c",
   "no": 3,
   "label": "C",
   "title": "모의고사 C세트",
   "focus": "15개 주제 · 10문항 · 각 10점",
   "lead": "같은 15개 주제를 또 다른 조합으로 묶은 세 번째 세트예요. 곡선 위에서의 변화율(연쇄법칙)과 곡선의 길이로 시작해서 평행사변형 변수변환, 직선·곡선 경로로 보는 극한과 정의로 구하는 편도함수, 세 잎 장미곡선, 두 포물면 사이와 구·원뿔 삼중적분, 평면까지의 거리(라그랑주와 사영), 포물선 영역의 그린 정리, 다항함수의 ε₁·ε₂ 와 선형근사, 삼각형 영역의 최대·최소, 적분 순서 바꾸기를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
   "mins": 81,
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "곡선의 길이 · 연쇄법칙",
     "ref": "13.3 · 14.5 · 14.6",
     "mins": 7,
     "topics": [
      [
       11,
       "곡선의 길이"
      ],
      [
       12,
       "연쇄법칙"
      ]
     ],
     "types": [
      [
       "13-arc",
       "호의 길이"
      ],
      [
       "14-chain",
       "연쇄법칙"
      ],
      [
       "14-dir",
       "방향도함수"
      ]
     ],
     "stem": "곡선 $\\mathbf r(t)=\\langle e^t,\\ e^{-t},\\ \\sqrt2\\,t\\rangle$ 와 함수 $f(x,y,z)=x^2y+yz+z^2$ 에 대하여",
     "parts": [
      [
       "a",
       "$0\\le t\\le1$ 부분의 길이를 구하시오. [4점]"
      ],
      [
       "b",
       "점이 곡선을 따라 움직일 때 $t=0$ 에서 $\\dfrac{d}{dt}f(\\mathbf r(t))$ 를 연쇄법칙으로 구하시오. [3점]"
      ],
      [
       "c",
       "$\\mathbf r(0)$ 에서 곡선의 단위접선벡터 $\\mathbf T(0)$ 방향으로의 $f$ 의 방향도함수를 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$e-\\dfrac1e$"
      ],
      [
       "b",
       "$1+\\sqrt2$"
      ],
      [
       "c",
       "$\\dfrac{1+\\sqrt2}{2}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'(t)=\\langle e^t,\\ -e^{-t},\\ \\sqrt2\\rangle\\text{,}$ $\\ |\\mathbf r'(t)|^2=e^{2t}+e^{-2t}+2=\\big(e^t+e^{-t}\\big)^2$ → $|\\mathbf r'(t)|=e^t+e^{-t}$ (완전제곱이 되는지 먼저 보기)",
        "$$\\begin{aligned}L&amp;=\\int_0^1\\big(e^t+e^{-t}\\big)\\,dt=\\Big[e^t-e^{-t}\\Big]_0^1\\\\&amp;=e-\\frac1e\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r(0)=(1,1,0)\\text{,}$ $\\ \\mathbf r'(0)=\\langle1,\\ -1,\\ \\sqrt2\\rangle$",
        "$\\nabla f=\\langle 2xy,\\ x^2+z,\\ y+2z\\rangle$ → $\\nabla f(1,1,0)=\\langle2,\\ 1,\\ 1\\rangle$",
        "$\\dfrac{d}{dt}f(\\mathbf r(t))\\Big|_{t=0}=\\nabla f(1,1,0)\\cdot\\mathbf r'(0)=2-1+\\sqrt2=1+\\sqrt2$ (확인: $f(\\mathbf r(t))=e^t+\\sqrt2\\,te^{-t}+2t^2$ 을 미분해도 같아요)"
       ]
      ],
      [
       "c",
       [
        "$|\\mathbf r'(0)|=e^0+e^0=2$ → $\\mathbf T(0)=\\dfrac{\\mathbf r'(0)}{|\\mathbf r'(0)|}=\\dfrac12\\langle1,\\ -1,\\ \\sqrt2\\rangle$",
        "$D_{\\mathbf T}f=\\nabla f(1,1,0)\\cdot\\mathbf T(0)=\\dfrac{1+\\sqrt2}{2}$ — (b)의 변화율을 속력 $2$ 로 나눈 값이에요."
       ]
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "변수변환 (야코비안)",
     "ref": "15.9",
     "mins": 8,
     "topics": [
      [
       7,
       "u·v 변수변환 (야코비안)"
      ]
     ],
     "types": [
      [
       "15-change",
       "변수변환·야코비안"
      ]
     ],
     "stem": "$R$ 은 네 직선 $x+y=1,\\ x+y=4,\\ y-2x=0,\\ y-2x=3$ 으로 둘러싸인 평행사변형이다. 변환 $u=x+y,\\ v=y-2x$ 를 이용하여",
     "parts": [
      [
       "a",
       "야코비안 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_R(y-2x)\\,e^{x+y}\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac13\\text{,}$ $\\ S=\\{(u,v)\\mid1\\le u\\le4,\\ 0\\le v\\le3\\}$"
      ],
      [
       "b",
       "$\\dfrac32\\big(e^4-e\\big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$$\\frac{\\partial(u,v)}{\\partial(x,y)}=\\begin{vmatrix}1&amp;1\\\\-2&amp;1\\end{vmatrix}=1+2=3$$ 이므로 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac13$ (역변환 $x=\\frac{u-v}{3},\\ y=\\frac{2u+v}{3}$ 으로 직접 계산해도 같아요)",
        "네 직선이 $u=1,\\ u=4,\\ v=0,\\ v=3$ 이 되어 $S:\\ 1\\le u\\le4,\\ 0\\le v\\le3$ (직사각형)"
       ]
      ],
      [
       "b",
       [
        "피적분함수 $(y-2x)e^{x+y}=v\\,e^u\\text{,}$ $\\ dA=\\Big|\\dfrac{\\partial(x,y)}{\\partial(u,v)}\\Big|\\,du\\,dv=\\dfrac13\\,du\\,dv$",
        "$$\\begin{aligned}&amp;\\iint_R(y-2x)e^{x+y}\\,dA\\\\&amp;=\\frac13\\int_1^4\\!\\!\\int_0^3v\\,e^u\\,dv\\,du\\\\&amp;=\\frac13\\cdot\\frac92\\cdot\\big(e^4-e\\big)=\\frac32\\big(e^4-e\\big)\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "극한의 존재성 · 연속 · 편도함수",
     "ref": "14.2 · 14.3",
     "mins": 8,
     "topics": [
      [
       3,
       "다변수 극한의 존재성"
      ],
      [
       10,
       "편도함수와 그래디언트"
      ]
     ],
     "types": [
      [
       "14-dne",
       "극한이 존재하지 않음"
      ],
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ],
      [
       "14-defpartial",
       "연속성 판정·정의로 구하는 편도함수"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{xy}{x^2+xy+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{2xy^3}{x^2+y^6}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "c",
       "$g(x,y)=\\dfrac{x^3+y^3}{x^2+y^2}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $\\ g(0,0)=0$ 일 때, $g$ 가 원점에서 연속임을 보이고 편도함수의 정의를 이용해 $g_x(0,0),\\ g_y(0,0)$ 을 구하시오. [4점]"
      ]
     ],
     "answer": [
      [
       "a",
       "존재하지 않음 (직선 $y=mx$ 를 따라 <span class=\"nw\">$\\dfrac{m}{1+m+m^2}$:</span> <span class=\"nw\">$x$축에서</span> <span class=\"nw\">$0$,</span> $y=x$ 에서 <span class=\"nw\">$\\frac13$)</span>"
      ],
      [
       "b",
       "존재하지 않음 (직선을 따라서는 모두 <span class=\"nw\">$0$,</span> 곡선 $x=y^3$ 을 따라 <span class=\"nw\">$1$)</span>"
      ],
      [
       "c",
       "연속, $\\ g_x(0,0)=1,\\ g_y(0,0)=1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "직선 $y=mx\\ (x\\ne0)$ 를 따라가면 $$\\frac{mx^2}{x^2+mx^2+m^2x^2}=\\frac{m}{1+m+m^2}$$ 으로 기울기 $m$ 에 따라 값이 달라요.",
        "<span class=\"nw\">$x$축(</span><span class=\"nw\">$m=0$)에서는</span> <span class=\"nw\">$0$,</span> 직선 <span class=\"nw\">$y=x$(</span><span class=\"nw\">$m=1$)에서는</span> $\\frac13$ → 극한은 존재하지 않아요."
       ]
      ],
      [
       "b",
       [
        "직선 <span class=\"nw\">$y=mx$:</span> $\\dfrac{2m^3x^4}{x^2+m^6x^6}=\\dfrac{2m^3x^2}{1+m^6x^4}\\to0\\text{,}$ <span class=\"nw\">$\\ y$축</span> 위에서도 $0$ → 직선만으로는 판정이 안 돼요.",
        "분모의 $x^2$ 과 $y^6$ 의 차수를 맞추는 곡선 $x=y^3$ 을 따라가면 $\\dfrac{2y^6}{y^6+y^6}=1\\to1$",
        "경로에 따라 값($0$ 과 <span class=\"nw\">$1$)이</span> 다르므로 극한은 존재하지 않아요. (일반적으로 곡선 $x=ky^3$ 을 따라 <span class=\"nw\">$\\frac{2k}{k^2+1}$)</span>"
       ]
      ],
      [
       "c",
       [
        "극좌표 $x=r\\cos\\theta,\\ y=r\\sin\\theta\\text{:}$ $\\ |g|=r\\,|\\cos^3\\theta+\\sin^3\\theta|\\le2r\\to0=g(0,0)$ → 원점에서 연속",
        "$g(h,0)=\\dfrac{h^3}{h^2}=h$ → $g_x(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{g(h,0)-g(0,0)}{h}=\\lim_{h\\to0}\\frac hh=1$",
        "같은 방법으로 $g(0,h)=h$ 이므로 $g_y(0,0)=1$"
       ]
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "극좌표 이중적분 (장미곡선)",
     "ref": "15.3",
     "mins": 8,
     "topics": [
      [
       1,
       "극좌표 꽃잎(장미곡선) 이중적분"
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ],
     "stem": "장미곡선 $r=2\\cos3\\theta$ (꽃잎 3장)에 대하여, 꽃잎 한 장 $\\big(-\\frac\\pi6\\le\\theta\\le\\frac\\pi6\\big)$ 으로 둘러싸인 영역을 $D$ 라 하자.",
     "parts": [
      [
       "a",
       "$D$ 의 넓이를 이중적분으로 구하시오. [3점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_D(x^2+y^2)\\,dA$ 를 구하시오. [3점]"
      ],
      [
       "c",
       "장미곡선의 내부이면서 원 $r=1$ 의 외부인 영역(꽃잎 3장 전체)의 넓이를 구하시오. [4점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac\\pi3$"
      ],
      [
       "b",
       "$\\dfrac\\pi2$"
      ],
      [
       "c",
       "$\\dfrac\\pi3+\\dfrac{\\sqrt3}{2}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$D:\\ -\\frac\\pi6\\le\\theta\\le\\frac\\pi6,\\ 0\\le r\\le2\\cos3\\theta\\text{,}$ $\\ dA=r\\,dr\\,d\\theta$",
        "$$\\begin{aligned}A&amp;=\\int_{-\\pi/6}^{\\pi/6}\\!\\!\\int_0^{2\\cos3\\theta}r\\,dr\\,d\\theta\\\\&amp;=\\int_{-\\pi/6}^{\\pi/6}2\\cos^23\\theta\\,d\\theta\\\\&amp;=\\int_{-\\pi/6}^{\\pi/6}(1+\\cos6\\theta)\\,d\\theta=\\frac\\pi3\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$x^2+y^2=r^2$:</span> $$\\begin{aligned}\\iint_D(x^2+y^2)\\,dA&amp;=\\int_{-\\pi/6}^{\\pi/6}\\!\\!\\int_0^{2\\cos3\\theta}r^3\\,dr\\,d\\theta\\\\&amp;=4\\int_{-\\pi/6}^{\\pi/6}\\cos^43\\theta\\,d\\theta\\end{aligned}$$",
        "$u=3\\theta$ 로 치환하고 $\\cos^4u=\\dfrac38+\\dfrac12\\cos2u+\\dfrac18\\cos4u\\text{:}$ $$\\frac43\\int_{-\\pi/2}^{\\pi/2}\\cos^4u\\,du=\\frac43\\cdot\\frac{3\\pi}{8}=\\frac\\pi2$$"
       ]
      ],
      [
       "c",
       [
        "교점: $2\\cos3\\theta=1 \\Rightarrow 3\\theta=\\pm\\frac\\pi3 \\Rightarrow \\theta=\\pm\\frac\\pi9\\text{.}$ 꽃잎 $D$ 에서 $|\\theta|\\le\\frac\\pi9$ 일 때 장미곡선이 원 바깥에 있어요.",
        "$$\\begin{aligned}&amp;\\frac12\\int_{-\\pi/9}^{\\pi/9}\\big(4\\cos^23\\theta-1\\big)\\,d\\theta\\\\&amp;=\\frac12\\int_{-\\pi/9}^{\\pi/9}(1+2\\cos6\\theta)\\,d\\theta\\\\&amp;=\\frac12\\Big(\\frac{2\\pi}{9}+\\frac23\\sin\\frac{2\\pi}{3}\\Big)=\\frac\\pi9+\\frac{\\sqrt3}{6}\\end{aligned}$$",
        "꽃잎 3장이 합동이므로 $3\\Big(\\dfrac\\pi9+\\dfrac{\\sqrt3}6\\Big)=\\dfrac\\pi3+\\dfrac{\\sqrt3}2$"
       ]
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "원주좌표 · 구면좌표 삼중적분",
     "ref": "15.7 · 15.8",
     "mins": 9,
     "topics": [
      [
       5,
       "원주좌표 삼중적분"
      ],
      [
       6,
       "구면좌표 삼중적분"
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
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "두 포물면 $z=x^2+y^2$ 과 $z=8-x^2-y^2$ 으로 둘러싸인 입체를 $E$ 라 할 때, 원주좌표를 이용하여 $\\displaystyle\\iiint_Ez\\,dV$ 를 구하시오. [5점]"
      ],
      [
       "b",
       "구 $x^2+y^2+z^2=2z$ 의 내부이고 원뿔 $z=\\sqrt{x^2+y^2}$ 의 위쪽에 있는 입체의 부피를 구면좌표로 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$64\\pi$"
      ],
      [
       "b",
       "$\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "두 곡면은 <span class=\"nw\">$r^2=8-r^2$,</span> 즉 $r=2$ 에서 만나요. $E:\\ 0\\le\\theta\\le2\\pi,\\ 0\\le r\\le2,\\ r^2\\le z\\le8-r^2\\text{,}$ $\\ dV=r\\,dz\\,dr\\,d\\theta$",
        "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^2\\!\\!\\int_{r^2}^{8-r^2}z\\,r\\,dz\\,dr\\,d\\theta\\\\&amp;=2\\pi\\int_0^2\\frac{(8-r^2)^2-r^4}{2}\\,r\\,dr\\\\&amp;=\\pi\\int_0^2(64-16r^2)\\,r\\,dr\\\\&amp;=\\pi\\Big[32r^2-4r^4\\Big]_0^2=64\\pi\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "구: $\\rho^2=2\\rho\\cos\\phi \\Rightarrow \\rho=2\\cos\\phi\\text{.}$&emsp;원뿔 <span class=\"nw\">$z=r$:</span> $\\tan\\phi=1 \\Rightarrow \\phi=\\frac\\pi4\\text{,}$ 그 위쪽이므로 $0\\le\\phi\\le\\frac\\pi4$",
        "$$\\begin{aligned}V&amp;=\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/4}\\!\\!\\int_0^{2\\cos\\phi}\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\\\&amp;=2\\pi\\int_0^{\\pi/4}\\frac{8\\cos^3\\phi}{3}\\sin\\phi\\,d\\phi\\\\&amp;=\\frac{16\\pi}{3}\\Big[-\\frac{\\cos^4\\phi}{4}\\Big]_0^{\\pi/4}\\\\&amp;=\\frac{16\\pi}{3}\\cdot\\frac14\\Big(1-\\frac14\\Big)=\\pi\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "사영 · 라그랑주 승수법",
     "ref": "12.3 · 12.5 · 14.8",
     "mins": 8,
     "topics": [
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ],
      [
       2,
       "라그랑주 승수법"
      ]
     ],
     "types": [
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "12-proj",
       "정사영과 일"
      ],
      [
       "12-dist",
       "거리 공식"
      ]
     ],
     "stem": "평면 $\\Pi:\\ 2x-y+2z=16$ 과 점 $Q(1,\\ 2,\\ -1)$ 에 대하여",
     "parts": [
      [
       "a",
       "라그랑주 승수법으로 $\\Pi$ 위에서 $Q$ 에 가장 가까운 점과 그 거리를 구하시오. [5점]"
      ],
      [
       "b",
       "$\\Pi$ 위의 점 $P_0(8,0,0)$ 과 법선벡터 $\\mathbf n=\\langle2,-1,2\\rangle$ 에 대하여 $\\operatorname{comp}_{\\mathbf n}\\overrightarrow{P_0Q}$ 와 $\\operatorname{proj}_{\\mathbf n}\\overrightarrow{P_0Q}$ 를 구하고, 이것으로 (a)의 결과를 확인하시오. [3점]"
      ],
      [
       "c",
       "평면 $\\Pi$ 에 대하여 $Q$ 와 대칭인 점을 구하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "가장 가까운 점 <span class=\"nw\">$(5,\\ 0,\\ 3)$,</span> 거리 $6$"
      ],
      [
       "b",
       "$\\operatorname{comp}_{\\mathbf n}\\overrightarrow{P_0Q}=-6\\text{,}$ $\\ \\operatorname{proj}_{\\mathbf n}\\overrightarrow{P_0Q}=\\langle-4,\\ 2,\\ -4\\rangle$"
      ],
      [
       "c",
       "$(9,\\ -2,\\ 7)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "거리의 제곱 $f=(x-1)^2+(y-2)^2+(z+1)^2$ 을 제약 $g=2x-y+2z=16$ 아래에서 최소화해요. $\\nabla f=\\lambda\\nabla g\\text{:}$",
        "$2(x-1)=2\\lambda,\\ \\ 2(y-2)=-\\lambda,\\ \\ 2(z+1)=2\\lambda$ → $x=1+\\lambda,\\ y=2-\\frac\\lambda2,\\ z=-1+\\lambda$",
        "제약식에 대입: $2(1+\\lambda)-\\big(2-\\frac\\lambda2\\big)+2(-1+\\lambda)=16 \\Rightarrow \\frac92\\lambda=18,\\ \\lambda=4$ → 점 <span class=\"nw\">$(5,0,3)$,</span> 거리 $\\sqrt{16+4+16}=6$ (평면 위에서 멀어질수록 $f$ 가 커지므로 이 점에서 최소)"
       ]
      ],
      [
       "b",
       [
        "$\\overrightarrow{P_0Q}=\\langle-7,\\ 2,\\ -1\\rangle\\text{,}$ <span class=\"nw\">$\\ |\\mathbf n|=3$,</span> $\\ \\mathbf n\\cdot\\overrightarrow{P_0Q}=-14-2-2=-18$",
        "$\\operatorname{comp}_{\\mathbf n}\\overrightarrow{P_0Q}=\\dfrac{-18}{3}=-6$ → $Q$ 와 평면 사이의 거리는 $|-6|=6$",
        "$\\operatorname{proj}_{\\mathbf n}\\overrightarrow{P_0Q}=\\dfrac{-18}{9}\\langle2,-1,2\\rangle=\\langle-4,\\ 2,\\ -4\\rangle$ 는 평면에서 $Q$ 로 가는 수직 벡터예요. 가장 가까운 점은 $Q-\\langle-4,2,-4\\rangle=(5,0,3)$ → (a)와 같아요."
       ]
      ],
      [
       "c",
       [
        "$Q$ 에서 평면까지 수직으로 $\\langle4,-2,4\\rangle$ 만큼 가면 $(5,0,3)$ 이므로, 한 번 더 가면 대칭점: $Q+2\\langle4,-2,4\\rangle=(9,\\ -2,\\ 7)$",
        "(확인: 중점 $(5,0,3)$ 이 평면 위에 있고 $\\langle8,-4,8\\rangle\\parallel\\mathbf n\\text{)}$"
       ]
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "그린 정리 · 곡선 나누어 직접 계산",
     "ref": "16.2 · 16.4",
     "mins": 9,
     "topics": [
      [
       9,
       "그린 정리 · 곡선 나누어 직접 계산"
      ]
     ],
     "types": [
      [
       "16-green",
       "그린 정리"
      ],
      [
       "16-vector",
       "벡터 선적분·일"
      ],
      [
       "16-conserv",
       "보존장 판정·퍼텐셜"
      ]
     ],
     "stem": "$D$ 는 포물선 $y=1-x^2$ 과 <span class=\"nw\">$x$축으로</span> 둘러싸인 영역이고, $C$ 는 $D$ 의 경계로 양의 방향(반시계 방향)이다. $\\displaystyle I=\\oint_C(x^2-y^2)\\,dx+xy\\,dy$ 에 대하여",
     "parts": [
      [
       "a",
       "$C$ 를 선분과 포물선으로 나누어 $I$ 를 직접 계산하시오. [4점]"
      ],
      [
       "b",
       "그린 정리를 이용해 $I$ 를 계산하고 (a)와 같은지 확인하시오. [4점]"
      ],
      [
       "c",
       "같은 $C$ 에서 $\\displaystyle\\oint_C(2xy+e^x)\\,dx+(x^2+\\cos y)\\,dy=0$ 인 이유를 그린 정리로 설명하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac85$"
      ],
      [
       "b",
       "$\\dfrac85$"
      ],
      [
       "c",
       "$Q_x-P_y=2x-2x=0$ 이므로 $\\displaystyle\\oint_C=\\iint_D0\\,dA=0$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "양의 방향: $C_1$ 은 <span class=\"nw\">$x$축</span> 위 선분 <span class=\"nw\">$(-1,0)\\to(1,0)$,</span> $C_2$ 는 포물선을 따라 $(1,0)\\to(-1,0)$",
        "$C_1:\\ y=0,\\ dy=0$ → $\\displaystyle\\int_{C_1}=\\int_{-1}^1x^2\\,dx=\\frac23$",
        "$C_2:\\ x=t,\\ y=1-t^2\\ (t:1\\to-1)\\text{,}$ <span class=\"nw\">$\\ dy=-2t\\,dt$:</span> $$\\begin{aligned}\\int_{C_2}&amp;=\\int_1^{-1}\\Big[t^2-(1-t^2)^2-2t^2(1-t^2)\\Big]dt\\\\&amp;=-\\int_{-1}^1\\big(t^4+t^2-1\\big)\\,dt\\\\&amp;=-\\Big(\\frac25+\\frac23-2\\Big)=\\frac{14}{15}\\end{aligned}$$",
        "$I=\\dfrac23+\\dfrac{14}{15}=\\dfrac{24}{15}=\\dfrac85$"
       ]
      ],
      [
       "b",
       [
        "$P=x^2-y^2,\\ Q=xy$ → <span class=\"nw\">$Q_x-P_y=y-(-2y)=3y$,</span> $\\ D:\\ -1\\le x\\le1,\\ 0\\le y\\le1-x^2$",
        "$$\\begin{aligned}I&amp;=\\iint_D3y\\,dA=\\int_{-1}^1\\frac32(1-x^2)^2\\,dx\\\\&amp;=\\frac32\\cdot\\frac{16}{15}=\\frac85\\end{aligned}$$ — (a)와 같아요."
       ]
      ],
      [
       "c",
       [
        "$P=2xy+e^x,\\ Q=x^2+\\cos y$ 이면 $Q_x-P_y=2x-2x=0$",
        "그린 정리로 $\\displaystyle\\oint_C=\\iint_D0\\,dA=0\\text{.}$ ($\\mathbf F=\\nabla\\big(x^2y+e^x+\\sin y\\big)$ 인 보존장이라 닫힌 곡선을 한 바퀴 돌면 $0$ 이에요.)"
       ]
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "미분가능성의 정의 · 접평면",
     "ref": "14.4",
     "mins": 8,
     "topics": [
      [
       4,
       "미분가능성의 정의"
      ],
      [
       14,
       "접평면과 그래디언트"
      ]
     ],
     "types": [
      [
       "14-differentiable",
       "미분가능성의 정의 (ε₁·ε₂)"
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ],
     "stem": "$f(x,y)=xy^2$ 과 점 $(2,1)$ 에 대하여",
     "parts": [
      [
       "a",
       "$\\Delta z=f(2+\\Delta x,\\ 1+\\Delta y)-f(2,1)$ 을 전개하여 $\\Delta z=f_x(2,1)\\Delta x+f_y(2,1)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 를 만족하는 $\\varepsilon_1,\\ \\varepsilon_2$ 를 찾고, 정의를 이용해 $f$ 가 $(2,1)$ 에서 미분가능함을 보이시오. [4점]<br>(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 $\\Delta z=f_x(a,b)\\Delta x+f_y(a,b)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $(\\Delta x,\\Delta y)\\to(0,0)$ 일 때 $\\varepsilon_1,\\varepsilon_2\\to0$ 인 $\\varepsilon_1,\\varepsilon_2$ 가 존재한다는 뜻이다.)"
      ],
      [
       "b",
       "곡면 $z=f(x,y)$ 위의 점 $(2,\\ 1,\\ 2)$ 에서의 접평면의 방정식을 구하시오. [3점]"
      ],
      [
       "c",
       "선형근사를 이용하여 $f(2.02,\\ 0.97)$ 의 근삿값을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\varepsilon_1=2\\Delta y+(\\Delta y)^2,\\ \\ \\varepsilon_2=2\\Delta y$ (둘 다 <span class=\"nw\">$\\to0$)</span> → 미분가능"
      ],
      [
       "b",
       "$z=x+4y-4$"
      ],
      [
       "c",
       "$1.9$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=y^2,\\ f_y=2xy$ → $f_x(2,1)=1,\\ f_y(2,1)=4$",
        "$$\\begin{aligned}\\Delta z&amp;=(2+\\Delta x)(1+\\Delta y)^2-2\\\\&amp;=\\Delta x+4\\Delta y+2(\\Delta y)^2\\\\&amp;\\quad+2\\Delta x\\Delta y+\\Delta x(\\Delta y)^2\\end{aligned}$$",
        "$$\\begin{aligned}\\Delta z&amp;=1\\cdot\\Delta x+4\\Delta y\\\\&amp;\\quad+\\underbrace{\\big(2\\Delta y+(\\Delta y)^2\\big)}_{\\varepsilon_1}\\Delta x+\\underbrace{2\\Delta y}_{\\varepsilon_2}\\Delta y\\end{aligned}$$",
        "$(\\Delta x,\\Delta y)\\to(0,0)$ 이면 $\\varepsilon_1\\to0,\\ \\varepsilon_2\\to0$ 이므로 정의에 의해 $(2,1)$ 에서 **미분가능**해요. ($\\varepsilon_1,\\varepsilon_2$ 를 고르는 방법은 하나가 아니에요.)"
       ]
      ],
      [
       "b",
       [
        "$z=f(2,1)+f_x(2,1)(x-2)+f_y(2,1)(y-1)=2+(x-2)+4(y-1)$",
        "정리하면 $z=x+4y-4$"
       ]
      ],
      [
       "c",
       [
        "$L(x,y)=x+4y-4$ → $f(2.02,\\ 0.97)\\approx2.02+3.88-4=1.9$",
        "(실제 값 $2.02\\times0.9409=1.900618$ — 오차 $\\Delta z-dz=\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 가 아주 작아요)"
       ]
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "2계 도함수 판정법 · 닫힌 영역의 최대·최소",
     "ref": "14.7",
     "mins": 9,
     "topics": [
      [
       15,
       "2계 도함수 판정법 (극값·안장점)"
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ]
     ],
     "stem": "$f(x,y)=xy(3-x-y)$ 에 대하여",
     "parts": [
      [
       "a",
       "$f$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"
      ],
      [
       "b",
       "세 점 $(0,0),\\ (4,0),\\ (0,4)$ 를 꼭짓점으로 하는 닫힌 삼각형 영역 $T$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$(0,0),\\ (3,0),\\ (0,3)\\text{:}$ 안장점,&emsp;<span class=\"nw\">$(1,1)$:</span> 극댓값 $1$"
      ],
      [
       "b",
       "최댓값 $1$ (점 <span class=\"nw\">$(1,1)$),</span> 최솟값 $-4$ (점 <span class=\"nw\">$(2,2)$)</span>"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$f=3xy-x^2y-xy^2$:</span> $\\ f_x=y(3-2x-y)=0,\\ \\ f_y=x(3-x-2y)=0$",
        "$x=0$ 이면 $f_x=y(3-y)=0$ → <span class=\"nw\">$(0,0),\\ (0,3)$.</span>&emsp;$y=0$ 이면 $f_y=x(3-x)=0$ → <span class=\"nw\">$(3,0)$.</span>&emsp;$x,y\\ne0$ 이면 $2x+y=3,\\ x+2y=3$ → $(1,1)$",
        "$f_{xx}=-2y,\\ f_{yy}=-2x,\\ f_{xy}=3-2x-2y\\text{,}$ $\\ D=4xy-(3-2x-2y)^2$",
        "<span class=\"nw\">$(0,0),(3,0),(0,3)$:</span> $D=-9\\lt 0$ → 안장점.&emsp;<span class=\"nw\">$(1,1)$:</span> $D=4-1=3>0,\\ f_{xx}=-2\\lt 0$ → 극댓값 $f(1,1)=1$"
       ]
      ],
      [
       "b",
       [
        "내부 임계점은 $(1,1)$ 하나 (값 <span class=\"nw\">$1$).</span> 나머지 임계점은 경계(두 변) 위에 있어요.",
        "두 변 <span class=\"nw\">$x=0$,</span> $y=0$ 위에서는 $f=0$",
        "빗변 $x+y=4\\ (0\\le x\\le4)\\text{:}$ $f=xy(3-4)=-x(4-x)$ → $x=2$ 에서 최소 <span class=\"nw\">$f(2,2)=-4$,</span> 양 끝에서 $0$",
        "후보 $1,\\ 0,\\ -4$ 를 비교하면 최댓값 $1$ (점 <span class=\"nw\">$(1,1)$),</span> 최솟값 $-4$ (점 <span class=\"nw\">$(2,2)$)</span>"
       ]
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "적분 순서 바꾸기 (이중·삼중)",
     "ref": "15.2 · 15.6",
     "mins": 7,
     "topics": [
      [
       8,
       "적분 순서 바꾸기 (이중·삼중)"
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ]
     ],
     "stem": "적분 순서를 바꾸어 다음 값을 구하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^{\\sqrt\\pi}\\!\\!\\int_y^{\\sqrt\\pi}\\sin(x^2)\\,dx\\,dy$ [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^1\\!\\!\\int_x^1\\!\\!\\int_y^1 9\\sqrt{1+z^3}\\,dz\\,dy\\,dx$ [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$1$"
      ],
      [
       "b",
       "$2\\sqrt2-1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\sin(x^2)$ 은 $x$ 로 바로 적분할 수 없으니 $x$ 를 바깥으로 보내요. 영역: $0\\le y\\le\\sqrt\\pi,\\ y\\le x\\le\\sqrt\\pi$ → $0\\le x\\le\\sqrt\\pi,\\ 0\\le y\\le x$",
        "$$\\begin{aligned}\\int_0^{\\sqrt\\pi}\\!\\!\\int_0^x\\sin(x^2)\\,dy\\,dx&amp;=\\int_0^{\\sqrt\\pi}x\\sin(x^2)\\,dx\\\\&amp;=\\Big[-\\frac{\\cos(x^2)}{2}\\Big]_0^{\\sqrt\\pi}=\\frac{1+1}{2}=1\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\sqrt{1+z^3}$ 은 $z$ 로 바로 적분할 수 없으니 $z$ 를 가장 바깥으로 보내요.",
        "영역: $0\\le x\\le1,\\ x\\le y\\le1,\\ y\\le z\\le1\\text{,}$ 즉 $0\\le x\\le y\\le z\\le1$ → $0\\le z\\le1,\\ 0\\le y\\le z,\\ 0\\le x\\le y$",
        "$$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^z\\!\\!\\int_0^y9\\sqrt{1+z^3}\\,dx\\,dy\\,dz\\\\&amp;=\\int_0^19\\sqrt{1+z^3}\\cdot\\frac{z^2}{2}\\,dz\\\\&amp;=\\Big[(1+z^3)^{3/2}\\Big]_0^1=2\\sqrt2-1\\end{aligned}$$"
       ]
      ]
     ]
    }
   ]
  },
  {
   "id": "d",
   "no": 4,
   "label": "D",
   "title": "모의고사 D세트",
   "focus": "15개 주제 · 10문항 · 각 10점",
   "lead": "15개 주제를 네 번째 조합으로 묶은 세트예요. 언덕 높이 함수의 그래디언트·방향도함수·접평면으로 시작해서 적분 순서 바꾸기, 곡선의 길이와 접선 방향 가속도(사영), 경로로 보는 극한과 미분가능성의 정의(미분가능하지 않은 예), 사분원판 그린 정리, 사다리꼴 변수변환, 2계 연쇄법칙, 네 잎 장미곡선, 원판 위 최대·최소(판정법과 라그랑주), 원주·구면좌표를 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
   "mins": 81,
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "그래디언트 · 방향도함수 · 접평면",
     "ref": "14.6 · 14.4",
     "mins": 8,
     "topics": [
      [
       10,
       "편도함수와 그래디언트"
      ],
      [
       14,
       "접평면과 그래디언트"
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
      ],
      [
       "14-tangent",
       "접평면·선형근사"
      ]
     ],
     "stem": "어떤 언덕의 높이가 $h(x,y)=12-x^2-y^2+xy-4x$ 이고, 등산객이 점 $P(1,2)$ 에 서 있다.",
     "parts": [
      [
       "a",
       "$\\nabla h(P)$ 를 구하고, $P$ 에서 가장 가파르게 올라가는 방향(단위벡터)과 그 방향의 기울기(변화율)를 구하시오. [3점]"
      ],
      [
       "b",
       "$P$ 에서 높이가 변하지 않는 방향(단위벡터)을 모두 구하시오. [2점]"
      ],
      [
       "c",
       "$D_{\\mathbf u}h(P)=3$ 을 만족하는 단위벡터 $\\mathbf u$ 를 모두 구하시오. [2점]"
      ],
      [
       "d",
       "곡면 $z=h(x,y)$ 위의 점 $(1,\\ 2,\\ 5)$ 에서의 접평면과 법선의 방정식을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\nabla h(P)=\\langle-4,\\ -3\\rangle\\text{,}$ 방향 $\\big\\langle-\\frac45,\\ -\\frac35\\big\\rangle\\text{,}$ 기울기 $5$"
      ],
      [
       "b",
       "$\\pm\\big\\langle\\frac35,\\ -\\frac45\\big\\rangle$"
      ],
      [
       "c",
       "$\\langle0,\\ -1\\rangle\\text{,}$ $\\ \\big\\langle-\\frac{24}{25},\\ \\frac{7}{25}\\big\\rangle$"
      ],
      [
       "d",
       "접평면 <span class=\"nw\">$4x+3y+z=15$,</span> 법선 $x=1+4t,\\ y=2+3t,\\ z=5+t$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$h_x=-2x+y-4,\\ \\ h_y=-2y+x$ → $\\nabla h(1,2)=\\langle-2+2-4,\\ -4+1\\rangle=\\langle-4,\\ -3\\rangle$",
        "가장 가파르게 올라가는 방향은 $\\nabla h$ 방향: $\\mathbf u=\\dfrac15\\langle-4,-3\\rangle=\\big\\langle-\\frac45,-\\frac35\\big\\rangle\\text{,}$ 그 기울기는 $|\\nabla h(P)|=5$"
       ]
      ],
      [
       "b",
       [
        "$D_{\\mathbf u}h=\\nabla h\\cdot\\mathbf u=0 \\iff \\mathbf u\\perp\\langle-4,-3\\rangle$ → $\\mathbf u=\\pm\\dfrac15\\langle3,-4\\rangle$ (등위곡선의 접선 방향)"
       ]
      ],
      [
       "c",
       [
        "$\\mathbf u=\\langle a,b\\rangle,\\ a^2+b^2=1\\text{,}$ $\\ -4a-3b=3 \\Rightarrow b=-1-\\frac43a$",
        "대입: $a^2+\\big(1+\\frac43a\\big)^2=1 \\Rightarrow \\frac{25}{9}a^2+\\frac83a=0 \\Rightarrow a=0$ 또는 $a=-\\frac{24}{25}$",
        "$\\mathbf u=\\langle0,\\ -1\\rangle$ 또는 $\\big\\langle-\\frac{24}{25},\\ \\frac7{25}\\big\\rangle$ (최대 기울기 $5$ 보다 작은 값이라 방향이 두 개 나와요)"
       ]
      ],
      [
       "d",
       [
        "$z=h(x,y)$ 의 접평면: $z=5+h_x(P)(x-1)+h_y(P)(y-2)=5-4(x-1)-3(y-2)$ → $4x+3y+z=15$",
        "법선벡터 $\\langle h_x,\\ h_y,\\ -1\\rangle=\\langle-4,-3,-1\\rangle\\parallel\\langle4,3,1\\rangle$ → 법선 $x=1+4t,\\ y=2+3t,\\ z=5+t$"
       ]
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "적분 순서 바꾸기 (이중·삼중)",
     "ref": "15.2 · 15.6",
     "mins": 7,
     "topics": [
      [
       8,
       "적분 순서 바꾸기 (이중·삼중)"
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ]
     ],
     "stem": "적분 순서를 바꾸어 다음 값을 구하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^1\\!\\!\\int_{2y}^2e^{-x^2}\\,dx\\,dy$ [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^\\pi\\!\\!\\int_0^2\\!\\!\\int_x^\\pi\\frac{\\sin z}{z}\\,dz\\,dy\\,dx$ [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{1-e^{-4}}{4}$"
      ],
      [
       "b",
       "$4$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$e^{-x^2}$ 은 $x$ 로 바로 적분할 수 없어요. 영역: $0\\le y\\le1,\\ 2y\\le x\\le2$ → $0\\le x\\le2,\\ 0\\le y\\le\\frac x2$",
        "$$\\begin{aligned}\\int_0^2\\!\\!\\int_0^{x/2}e^{-x^2}\\,dy\\,dx&amp;=\\int_0^2\\frac x2e^{-x^2}\\,dx\\\\&amp;=\\Big[-\\frac{e^{-x^2}}{4}\\Big]_0^2=\\frac{1-e^{-4}}{4}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\dfrac{\\sin z}{z}$ 는 $z$ 로 바로 적분할 수 없으니 $z$ 를 가장 바깥으로 보내요.",
        "영역: $0\\le x\\le\\pi,\\ 0\\le y\\le2,\\ x\\le z\\le\\pi$ → $0\\le z\\le\\pi,\\ 0\\le x\\le z,\\ 0\\le y\\le2$",
        "$$\\begin{aligned}&amp;\\int_0^\\pi\\!\\!\\int_0^z\\!\\!\\int_0^2\\frac{\\sin z}{z}\\,dy\\,dx\\,dz\\\\&amp;=\\int_0^\\pi\\frac{\\sin z}{z}\\cdot2z\\,dz=2\\int_0^\\pi\\sin z\\,dz=4\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "곡선의 길이 · 사영(comp·proj)",
     "ref": "13.3 · 12.3 · 13.2",
     "mins": 7,
     "topics": [
      [
       11,
       "곡선의 길이"
      ],
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ]
     ],
     "types": [
      [
       "13-arc",
       "호의 길이"
      ],
      [
       "12-proj",
       "정사영과 일"
      ],
      [
       "13-motion",
       "속도·속력·가속도"
      ]
     ],
     "stem": "곡선 $\\mathbf r(t)=\\big\\langle 2t,\\ t^2,\\ \\tfrac13t^3\\big\\rangle$ 에 대하여",
     "parts": [
      [
       "a",
       "$0\\le t\\le3$ 부분의 길이를 구하시오. [3점]"
      ],
      [
       "b",
       "$t=2$ 에서의 속도 $\\mathbf v=\\mathbf r'(2)\\text{,}$ 가속도 $\\mathbf a=\\mathbf r''(2)$ 에 대하여 $\\operatorname{comp}_{\\mathbf v}\\mathbf a$ 와 $\\operatorname{proj}_{\\mathbf v}\\mathbf a$ 를 구하시오. [4점]"
      ],
      [
       "c",
       "$\\mathbf a$ 를 $\\mathbf v$ 에 평행한 벡터와 $\\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$15$"
      ],
      [
       "b",
       "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=4\\text{,}$ $\\ \\operatorname{proj}_{\\mathbf v}\\mathbf a=\\big\\langle\\frac43,\\ \\frac83,\\ \\frac83\\big\\rangle$"
      ],
      [
       "c",
       "$\\mathbf a=\\big\\langle\\frac43,\\frac83,\\frac83\\big\\rangle+\\big\\langle-\\frac43,-\\frac23,\\frac43\\big\\rangle\\text{,}$ 수직인 벡터의 크기 $2$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'(t)=\\langle2,\\ 2t,\\ t^2\\rangle\\text{,}$ $\\ |\\mathbf r'(t)|^2=4+4t^2+t^4=(t^2+2)^2$ → $|\\mathbf r'(t)|=t^2+2$ (완전제곱)",
        "$L=\\displaystyle\\int_0^3(t^2+2)\\,dt=9+6=15$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r''(t)=\\langle0,\\ 2,\\ 2t\\rangle$ → $\\mathbf v=\\langle2,4,4\\rangle\\text{,}$ $\\ \\mathbf a=\\langle0,2,4\\rangle\\text{,}$ <span class=\"nw\">$\\ |\\mathbf v|=6$,</span> $\\ \\mathbf a\\cdot\\mathbf v=0+8+16=24$",
        "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=\\dfrac{24}{6}=4$ (속력 $t^2+2$ 의 변화율 $2t$ 의 $t=2$ 값과 같아요)",
        "$\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\dfrac{24}{36}\\langle2,4,4\\rangle=\\big\\langle\\frac43,\\frac83,\\frac83\\big\\rangle$"
       ]
      ],
      [
       "c",
       [
        "수직 성분: $\\mathbf a-\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\big\\langle-\\frac43,\\ -\\frac23,\\ \\frac43\\big\\rangle$ (확인: $\\mathbf v$ 와 내적하면 $\\frac{-8-8+16}{3}=0\\text{)}$",
        "크기 $\\dfrac{\\sqrt{16+4+16}}{3}=2$ ($\\frac{|\\mathbf v\\times\\mathbf a|}{|\\mathbf v|}=\\frac{|\\langle8,-8,4\\rangle|}{6}=2$ 와 같아요)"
       ]
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "극한의 존재성 · 미분가능성의 정의",
     "ref": "14.2 · 14.4",
     "mins": 9,
     "topics": [
      [
       3,
       "다변수 극한의 존재성"
      ],
      [
       4,
       "미분가능성의 정의"
      ]
     ],
     "types": [
      [
       "14-dne",
       "극한이 존재하지 않음"
      ],
      [
       "14-differentiable",
       "미분가능성의 정의 (ε₁·ε₂)"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{x^3y}{x^6+y^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "b",
       "$f(x,y)=\\dfrac{x^3}{x^2+y^2}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $\\ f(0,0)=0$ 일 때, $f$ 가 원점에서 연속임을 보이고 $f_x(0,0),\\ f_y(0,0)$ 을 구하시오. [3점]"
      ],
      [
       "c",
       "(b)의 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 $\\Delta z=f_x(a,b)\\Delta x+f_y(a,b)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $(\\Delta x,\\Delta y)\\to(0,0)$ 일 때 $\\varepsilon_1,\\varepsilon_2\\to0$ 인 $\\varepsilon_1,\\varepsilon_2$ 가 존재한다는 뜻이다.)"
      ]
     ],
     "answer": [
      [
       "a",
       "존재하지 않음 (직선을 따라서는 <span class=\"nw\">$0$,</span> 곡선 $y=x^3$ 을 따라 <span class=\"nw\">$\\frac12$)</span>"
      ],
      [
       "b",
       "연속, $\\ f_x(0,0)=1,\\ f_y(0,0)=0$"
      ],
      [
       "c",
       "미분가능하지 않음 ($\\Delta y=\\Delta x$ 로 두면 $\\varepsilon_1+\\varepsilon_2=-\\frac12\\text{)}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "직선 <span class=\"nw\">$y=mx$:</span> $\\dfrac{mx^4}{x^6+m^2x^2}=\\dfrac{mx^2}{x^4+m^2}\\to0\\text{,}$ <span class=\"nw\">$\\ y$축(</span><span class=\"nw\">$x=0$)</span> 위에서도 $0$ → 직선만으로는 판정이 안 돼요.",
        "분모의 $x^6$ 과 $y^2$ 의 차수를 맞추는 곡선 $y=x^3$ 을 따라가면 $\\dfrac{x^6}{x^6+x^6}=\\dfrac12$",
        "경로에 따라 값이 다르므로 극한은 존재하지 않아요. (일반적으로 곡선 $y=kx^3$ 을 따라 <span class=\"nw\">$\\frac{k}{1+k^2}$)</span>"
       ]
      ],
      [
       "b",
       [
        "$\\dfrac{x^2}{x^2+y^2}\\le1$ 이므로 $|f(x,y)|\\le|x|\\to0=f(0,0)$ → 조임정리로 연속",
        "$f(h,0)=\\dfrac{h^3}{h^2}=h$ → $f_x(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{h-0}{h}=1$",
        "$f(0,h)=0$ → $f_y(0,0)=\\displaystyle\\lim_{h\\to0}\\frac{0-0}{h}=0$"
       ]
      ],
      [
       "c",
       [
        "미분가능하다고 가정하면 $\\Delta z=f(\\Delta x,\\Delta y)-f(0,0)=1\\cdot\\Delta x+0\\cdot\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $\\varepsilon_1,\\varepsilon_2\\to0$ 이어야 해요.",
        "$\\Delta y=\\Delta x\\ (\\ne0)$ 로 두면 좌변은 $f(\\Delta x,\\Delta x)=\\dfrac{(\\Delta x)^3}{2(\\Delta x)^2}=\\dfrac{\\Delta x}{2}$ → $\\dfrac{\\Delta x}2=\\Delta x+(\\varepsilon_1+\\varepsilon_2)\\Delta x$ → $\\varepsilon_1+\\varepsilon_2=-\\dfrac12$",
        "그런데 $\\Delta x\\to0$ 이면 $(\\Delta x,\\Delta y)\\to(0,0)$ 이므로 $\\varepsilon_1+\\varepsilon_2\\to0$ 이어야 해서 모순 → 원점에서 **미분가능하지 않아요**. (연속이고 편도함수도 있지만 미분가능하지 않은 예)"
       ]
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "그린 정리 · 곡선 나누어 직접 계산",
     "ref": "16.2 · 16.4",
     "mins": 9,
     "topics": [
      [
       9,
       "그린 정리 · 곡선 나누어 직접 계산"
      ]
     ],
     "types": [
      [
       "16-green",
       "그린 정리"
      ],
      [
       "16-vector",
       "벡터 선적분·일"
      ]
     ],
     "stem": "$D$ 는 원 $x^2+y^2=4$ 의 제1사분면 부분(사분원판)이고, $C$ 는 $D$ 의 경계로 양의 방향이다. $\\displaystyle I=\\oint_C(x+y^2)\\,dx+3xy\\,dy$ 에 대하여",
     "parts": [
      [
       "a",
       "$C$ 를 두 선분과 원호로 나누어 $I$ 를 직접 계산하시오. [5점]"
      ],
      [
       "b",
       "그린 정리를 이용해 $I$ 를 계산하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac83$"
      ],
      [
       "b",
       "$\\dfrac83$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "양의 방향: <span class=\"nw\">$C_1:(0,0)\\to(2,0)$,</span> <span class=\"nw\">$\\ C_2$:</span> 원호 <span class=\"nw\">$(2,0)\\to(0,2)$,</span> $\\ C_3:(0,2)\\to(0,0)$",
        "$C_1:\\ y=0,\\ dy=0$ → $\\displaystyle\\int_0^2x\\,dx=2\\text{.}$&emsp;$\\ C_3:\\ x=0,\\ dx=0$ 이고 $Q=3xy=0$ → $0$",
        "$C_2:\\ x=2\\cos t,\\ y=2\\sin t\\ \\big(0\\le t\\le\\frac\\pi2\\big)\\text{:}$ $$\\begin{aligned}&amp;\\int_0^{\\pi/2}\\Big[(2\\cos t+4\\sin^2t)(-2\\sin t)\\\\&amp;\\qquad+12\\cos t\\sin t\\cdot2\\cos t\\Big]dt\\\\&amp;=\\int_0^{\\pi/2}\\big(-4\\sin t\\cos t-8\\sin^3t\\\\&amp;\\qquad+24\\cos^2t\\sin t\\big)\\,dt\\\\&amp;=-2-\\frac{16}{3}+8=\\frac23\\end{aligned}$$",
        "$I=2+\\dfrac23+0=\\dfrac83$"
       ]
      ],
      [
       "b",
       [
        "$P=x+y^2,\\ Q=3xy$ → $Q_x-P_y=3y-2y=y$",
        "$$\\begin{aligned}I&amp;=\\iint_Dy\\,dA=\\int_0^{\\pi/2}\\!\\!\\int_0^2r\\sin\\theta\\cdot r\\,dr\\,d\\theta\\\\&amp;=\\frac83\\Big[-\\cos\\theta\\Big]_0^{\\pi/2}=\\frac83\\end{aligned}$$ — (a)와 같아요."
       ]
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "변수변환 (야코비안)",
     "ref": "15.9",
     "mins": 8,
     "topics": [
      [
       7,
       "u·v 변수변환 (야코비안)"
      ]
     ],
     "types": [
      [
       "15-change",
       "변수변환·야코비안"
      ]
     ],
     "stem": "$R$ 은 네 점 $(2,0),\\ (4,0),\\ (0,4),\\ (0,2)$ 를 꼭짓점으로 하는 사다리꼴이다. 변환 $u=y-x,\\ v=y+x$ 를 이용하여",
     "parts": [
      [
       "a",
       "야코비안 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}$ 를 구하고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 부등식으로 나타내시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_R\\cos\\Big(\\frac{y-x}{y+x}\\Big)\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial(x,y)}{\\partial(u,v)}=-\\dfrac12$ (절댓값 <span class=\"nw\">$\\frac12$),</span> $\\ S=\\{(u,v)\\mid2\\le v\\le4,\\ -v\\le u\\le v\\}$"
      ],
      [
       "b",
       "$6\\sin1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x=\\dfrac{v-u}{2},\\ y=\\dfrac{u+v}{2}$ → $$\\frac{\\partial(x,y)}{\\partial(u,v)}=\\begin{vmatrix}-\\frac12&amp;\\frac12\\\\[2pt]\\frac12&amp;\\frac12\\end{vmatrix}=-\\frac14-\\frac14=-\\frac12$$",
        "경계: $x+y=2,\\ x+y=4$ → <span class=\"nw\">$v=2,\\ v=4$.</span>&emsp;$\\ y=0$ → <span class=\"nw\">$u=-v$,</span>&emsp;$\\ x=0$ → $u=v$",
        "$S:\\ 2\\le v\\le4,\\ -v\\le u\\le v$ (사다리꼴 — $u$ 의 범위가 $v$ 에 따라 달라져요)"
       ]
      ],
      [
       "b",
       [
        "$dA=\\dfrac12\\,du\\,dv\\text{,}$ 피적분함수 $\\cos\\dfrac uv$ 는 $u$ 로 먼저 적분하면 쉬워요.",
        "$$\\begin{aligned}&amp;\\frac12\\int_2^4\\!\\!\\int_{-v}^{v}\\cos\\frac uv\\,du\\,dv\\\\&amp;=\\frac12\\int_2^4\\Big[v\\sin\\frac uv\\Big]_{u=-v}^{u=v}dv\\\\&amp;=\\frac12\\int_2^42v\\sin1\\,dv=\\sin1\\cdot\\Big[\\frac{v^2}{2}\\Big]_2^4=6\\sin1\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "2계 연쇄법칙",
     "ref": "14.5",
     "mins": 7,
     "topics": [
      [
       12,
       "연쇄법칙"
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
     ],
     "stem": "$z=f(x,y)$ 의 2계 편도함수가 연속이고 $x=2s+t,\\ y=s-2t$ 이다.",
     "parts": [
      [
       "a",
       "$z_s,\\ z_t$ 를 $f_x,\\ f_y$ 로 나타내시오. [3점]"
      ],
      [
       "b",
       "$z_{ss}+z_{tt}=5\\big(f_{xx}+f_{yy}\\big)$ 임을 보이시오. [4점]"
      ],
      [
       "c",
       "$z_{st}$ 를 $f_{xx},\\ f_{xy},\\ f_{yy}$ 로 나타내고, $f_{xx}(3,-1)=4,\\ f_{xy}(3,-1)=-1,\\ f_{yy}(3,-1)=2$ 일 때 $(s,t)=(1,1)$ 에서 $z_{st}$ 와 $z_{ss}+z_{tt}$ 의 값을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$z_s=2f_x+f_y,\\ \\ z_t=f_x-2f_y$"
      ],
      [
       "b",
       "아래 풀이"
      ],
      [
       "c",
       "$z_{st}=2f_{xx}-3f_{xy}-2f_{yy}\\text{;}$&emsp;$(s,t)=(1,1)$ 에서 $z_{st}=7,\\ \\ z_{ss}+z_{tt}=30$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x_s=2,\\ x_t=1,\\ y_s=1,\\ y_t=-2$ (모두 상수)",
        "$z_s=f_x\\,x_s+f_y\\,y_s=2f_x+f_y\\text{,}$&emsp;$\\ z_t=f_x\\,x_t+f_y\\,y_t=f_x-2f_y$"
       ]
      ],
      [
       "b",
       [
        "$f_x,\\ f_y$ 도 $s,t$ 의 함수라 연쇄법칙을 한 번 더: $(f_x)_s=2f_{xx}+f_{xy}\\text{,}$ $\\ (f_y)_s=2f_{xy}+f_{yy}\\text{,}$ $\\ (f_x)_t=f_{xx}-2f_{xy}\\text{,}$ $\\ (f_y)_t=f_{xy}-2f_{yy}$",
        "$z_{ss}=2(2f_{xx}+f_{xy})+(2f_{xy}+f_{yy})=4f_{xx}+4f_{xy}+f_{yy}$",
        "$z_{tt}=(f_{xx}-2f_{xy})-2(f_{xy}-2f_{yy})=f_{xx}-4f_{xy}+4f_{yy}$",
        "더하면 $f_{xy}$ 항이 지워져 $z_{ss}+z_{tt}=5f_{xx}+5f_{yy}=5\\big(f_{xx}+f_{yy}\\big)$"
       ]
      ],
      [
       "c",
       [
        "$z_{st}=(z_s)_t=2(f_x)_t+(f_y)_t=2(f_{xx}-2f_{xy})+(f_{xy}-2f_{yy})=2f_{xx}-3f_{xy}-2f_{yy}$",
        "$(s,t)=(1,1)$ 이면 $(x,y)=(3,-1)$ → <span class=\"nw\">$z_{st}=8+3-4=7$,</span> $\\ z_{ss}+z_{tt}=5(4+2)=30$"
       ]
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "극좌표 이중적분 (장미곡선)",
     "ref": "15.3",
     "mins": 8,
     "topics": [
      [
       1,
       "극좌표 꽃잎(장미곡선) 이중적분"
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ],
     "stem": "장미곡선 $r=3\\sin2\\theta$ (꽃잎 4장)에 대하여, 제1사분면의 꽃잎 $\\big(0\\le\\theta\\le\\frac\\pi2\\big)$ 으로 둘러싸인 영역을 $D$ 라 하자.",
     "parts": [
      [
       "a",
       "장미곡선 전체(꽃잎 4장)로 둘러싸인 영역의 넓이를 구하시오. [3점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_D\\sqrt{x^2+y^2}\\,dA$ 를 구하시오. [3점]"
      ],
      [
       "c",
       "$\\displaystyle\\iint_D xy\\,dA$ 를 구하시오. [4점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{9\\pi}{2}$"
      ],
      [
       "b",
       "$6$"
      ],
      [
       "c",
       "$\\dfrac{27}{5}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\theta$ 가 $0$ 에서 $2\\pi$ 까지 변하는 동안 꽃잎 4장을 한 번씩 그려요 ($r\\lt 0$ 인 구간은 반대쪽 사분면의 꽃잎).",
        "$$\\begin{aligned}A&amp;=\\frac12\\int_0^{2\\pi}9\\sin^22\\theta\\,d\\theta\\\\&amp;=\\frac94\\int_0^{2\\pi}(1-\\cos4\\theta)\\,d\\theta=\\frac{9\\pi}{2}\\end{aligned}$$ (꽃잎 한 장 $\\frac{9\\pi}8$ 의 4배)"
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$\\sqrt{x^2+y^2}=r$:</span> $$\\begin{aligned}\\iint_Dr\\,dA&amp;=\\int_0^{\\pi/2}\\!\\!\\int_0^{3\\sin2\\theta}r^2\\,dr\\,d\\theta\\\\&amp;=9\\int_0^{\\pi/2}\\sin^32\\theta\\,d\\theta\\end{aligned}$$",
        "<span class=\"nw\">$u=2\\theta$:</span> $\\ \\dfrac92\\displaystyle\\int_0^{\\pi}\\sin^3u\\,du=\\frac92\\Big[-\\cos u+\\frac{\\cos^3u}{3}\\Big]_0^{\\pi}=\\frac92\\cdot\\frac43=6$"
       ]
      ],
      [
       "c",
       [
        "$xy=r^2\\cos\\theta\\sin\\theta=\\dfrac{r^2}{2}\\sin2\\theta\\text{:}$ $$\\begin{aligned}\\iint_Dxy\\,dA&amp;=\\int_0^{\\pi/2}\\!\\!\\int_0^{3\\sin2\\theta}\\frac{\\sin2\\theta}{2}\\,r^3\\,dr\\,d\\theta\\\\&amp;=\\frac{81}{8}\\int_0^{\\pi/2}\\sin^52\\theta\\,d\\theta\\end{aligned}$$",
        "$u=2\\theta$ 로 바꾸고 $\\sin^5u=(1-\\cos^2u)^2\\sin u\\text{,}$ <span class=\"nw\">$\\ w=\\cos u$:</span> $$\\frac{81}{16}\\int_{-1}^{1}(1-w^2)^2\\,dw=\\frac{81}{16}\\cdot\\frac{16}{15}=\\frac{27}{5}$$"
       ]
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "2계 도함수 판정법 · 라그랑주 승수법",
     "ref": "14.7 · 14.8",
     "mins": 9,
     "topics": [
      [
       15,
       "2계 도함수 판정법 (극값·안장점)"
      ],
      [
       2,
       "라그랑주 승수법"
      ]
     ],
     "types": [
      [
       "14-crit",
       "임계점·2계 판정법"
      ],
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "14-absext",
       "닫힌 영역의 최댓값·최솟값"
      ]
     ],
     "stem": "$f(x,y)=xy-x-y$ 의 닫힌 원판 $R=\\{(x,y)\\mid x^2+y^2\\le4\\}$ 에서의 최댓값과 최솟값을 구하려고 한다.",
     "parts": [
      [
       "a",
       "$f$ 의 임계점을 구하고 2계 도함수 판정법으로 판정하시오. [3점]"
      ],
      [
       "b",
       "라그랑주 승수법으로 경계 $x^2+y^2=4$ 위에서 $f$ 의 최댓값과 최솟값의 후보를 구하시오. [4점]"
      ],
      [
       "c",
       "$R$ 에서 $f$ 의 최댓값과 최솟값을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "<span class=\"nw\">$(1,1)$:</span> 안장점 ($f_{xx}f_{yy}-f_{xy}^2=-1\\lt 0\\text{)}$"
      ],
      [
       "b",
       "$x=y$ 에서 $2\\mp2\\sqrt2$ (점 <span class=\"nw\">$\\pm(\\sqrt2,\\sqrt2)$),</span>&emsp;$x+y=1$ 인 두 점에서 $-\\frac52$"
      ],
      [
       "c",
       "최댓값 $2+2\\sqrt2$ (점 <span class=\"nw\">$(-\\sqrt2,-\\sqrt2)$),</span> 최솟값 $-\\dfrac52$ (점 $\\big(\\frac{1\\pm\\sqrt7}{2},\\ \\frac{1\\mp\\sqrt7}{2}\\big)\\text{)}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$f_x=y-1=0,\\ f_y=x-1=0$ → 임계점 $(1,1)$ ($R$ 의 내부: <span class=\"nw\">$1+1\\lt 4$)</span>",
        "$f_{xx}=0,\\ f_{yy}=0,\\ f_{xy}=1$ → $f_{xx}f_{yy}-f_{xy}^2=0-1=-1\\lt 0$ → 안장점 (<span class=\"nw\">$f(1,1)=-1$).</span> 내부에는 극값이 없어요."
       ]
      ],
      [
       "b",
       [
        "<span class=\"nw\">$g=x^2+y^2=4$,</span> $\\ \\nabla f=\\lambda\\nabla g\\text{:}$ $\\ y-1=2\\lambda x,\\ \\ x-1=2\\lambda y$",
        "두 식을 빼면 $y-x=2\\lambda(x-y) \\Rightarrow (x-y)(1+2\\lambda)=0$ → $x=y$ 또는 $\\lambda=-\\frac12$",
        "<span class=\"nw\">$x=y$:</span> $2x^2=4,\\ x=\\pm\\sqrt2$ → $f(\\sqrt2,\\sqrt2)=2-2\\sqrt2\\text{,}$ $\\ f(-\\sqrt2,-\\sqrt2)=2+2\\sqrt2$",
        "<span class=\"nw\">$\\lambda=-\\frac12$:</span> <span class=\"nw\">$y-1=-x$,</span> 즉 <span class=\"nw\">$x+y=1$.</span> 이때 $xy=\\dfrac{(x+y)^2-(x^2+y^2)}{2}=\\dfrac{1-4}{2}=-\\dfrac32$ → $f=xy-(x+y)=-\\dfrac52$ (점 $x=\\frac{1\\pm\\sqrt7}{2},\\ y=1-x\\text{)}$"
       ]
      ],
      [
       "c",
       [
        "닫힌 유계 영역이라 최댓값·최솟값이 존재하고, 내부 임계점은 안장점뿐이라 후보는 경계의 값들이에요.",
        "$2\\sqrt2\\lt 3$ 이므로 $2-2\\sqrt2>-1>-\\frac52$ → 최댓값 $2+2\\sqrt2$ (점 <span class=\"nw\">$(-\\sqrt2,-\\sqrt2)$),</span> 최솟값 $-\\dfrac52$"
       ]
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "원주좌표 · 구면좌표 삼중적분",
     "ref": "15.7 · 15.8",
     "mins": 9,
     "topics": [
      [
       5,
       "원주좌표 삼중적분"
      ],
      [
       6,
       "구면좌표 삼중적분"
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
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "원기둥 $x^2+y^2=4$ 의 안쪽, 평면 $z=0$ 의 위쪽, 평면 $z=x+3$ 의 아래쪽에 있는 입체를 $E$ 라 할 때, 원주좌표를 이용하여 $E$ 의 부피와 $\\displaystyle\\iiint_Ex\\,dV$ 를 구하시오. [5점]"
      ],
      [
       "b",
       "반구 $H=\\{(x,y,z)\\mid x^2+y^2+z^2\\le4,\\ z\\ge0\\}$ 에서 구면좌표를 이용하여 $\\displaystyle\\iiint_H(x^2+y^2)\\,dV$ 를 구하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "부피 <span class=\"nw\">$12\\pi$,</span> $\\ \\displaystyle\\iiint_Ex\\,dV=4\\pi$"
      ],
      [
       "b",
       "$\\dfrac{128\\pi}{15}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$r\\le2$ 에서 $x+3=r\\cos\\theta+3\\ge1>0$ 이므로 $E:\\ 0\\le\\theta\\le2\\pi,\\ 0\\le r\\le2,\\ 0\\le z\\le r\\cos\\theta+3$",
        "$$\\begin{aligned}V&amp;=\\int_0^{2\\pi}\\!\\!\\int_0^2(r\\cos\\theta+3)\\,r\\,dr\\,d\\theta\\\\&amp;=0+3\\cdot2\\pi\\cdot\\frac{2^2}{2}=12\\pi\\end{aligned}$$ ($\\cos\\theta$ 항은 한 바퀴 적분하면 <span class=\"nw\">$0$)</span>",
        "$$\\begin{aligned}\\iiint_Ex\\,dV&amp;=\\int_0^{2\\pi}\\!\\!\\int_0^2r\\cos\\theta\\,(r\\cos\\theta+3)\\,r\\,dr\\,d\\theta\\\\&amp;=\\int_0^{2\\pi}\\cos^2\\theta\\,d\\theta\\cdot\\int_0^2r^3\\,dr=\\pi\\cdot4=4\\pi\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$x^2+y^2=\\rho^2\\sin^2\\phi\\text{,}$ $\\ H:\\ 0\\le\\theta\\le2\\pi,\\ 0\\le\\phi\\le\\frac\\pi2,\\ 0\\le\\rho\\le2$",
        "$$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^{\\pi/2}\\!\\!\\int_0^2\\rho^4\\sin^3\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\\\&amp;=2\\pi\\cdot\\int_0^{\\pi/2}\\sin^3\\phi\\,d\\phi\\cdot\\frac{2^5}{5}\\\\&amp;=2\\pi\\cdot\\frac23\\cdot\\frac{32}{5}=\\frac{128\\pi}{15}\\end{aligned}$$"
       ]
      ]
     ]
    }
   ]
  },
  {
   "id": "e",
   "no": 5,
   "label": "E",
   "title": "모의고사 E세트",
   "focus": "15개 주제 · 10문항 · 각 10점",
   "lead": "다섯 번째 세트예요. 등위곡면의 접평면과 원점까지의 거리(사영)로 시작해서 적분 순서 바꾸기, 직교좌표 적분을 원주·구면좌표로 바꾸기, 교수님이 예고한 일변수 증분식을 구체적인 함수로 써 보는 미분가능성 문항과 극좌표로 보는 극한, 네 잎 장미곡선과 원, 음함수 연쇄법칙과 그래디언트, 비선형 변수변환(u = xy, v = y/x), 평면곡선의 길이와 사영, 반타원 그린 정리, 라그랑주 승수법과 극값 판정을 다뤄요. 75–90분 안에 평균 70점 정도를 목표로 난이도를 맞췄어요.",
   "mins": 81,
   "problems": [
    {
     "id": "q1",
     "no": "1",
     "type": "접평면 · 사영(comp·proj)",
     "ref": "14.6 · 12.3 · 12.5",
     "mins": 7,
     "topics": [
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ],
      [
       14,
       "접평면과 그래디언트"
      ]
     ],
     "types": [
      [
       "14-levelsurf",
       "등위곡면의 접평면·법선"
      ],
      [
       "12-proj",
       "정사영과 일"
      ],
      [
       "12-dist",
       "거리 공식"
      ]
     ],
     "stem": "곡면 $S:\\ xyz=6$ 위의 점 $P(1,\\ 2,\\ 3)$ 에 대하여",
     "parts": [
      [
       "a",
       "$P$ 에서 $S$ 의 접평면과 법선의 방정식을 구하시오. [4점]"
      ],
      [
       "b",
       "$\\operatorname{comp}$ 를 이용하여 원점에서 (a)의 접평면까지의 거리를 구하시오. [3점]"
      ],
      [
       "c",
       "$\\operatorname{proj}$ 를 이용하여 (a)의 접평면 위에서 원점에 가장 가까운 점을 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "접평면 <span class=\"nw\">$6x+3y+2z=18$,</span> 법선 $x=1+6t,\\ y=2+3t,\\ z=3+2t$"
      ],
      [
       "b",
       "$\\dfrac{18}{7}$"
      ],
      [
       "c",
       "$\\Big(\\dfrac{108}{49},\\ \\dfrac{54}{49},\\ \\dfrac{36}{49}\\Big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$F=xyz$ 라 두면 $S$ 는 등위곡면 <span class=\"nw\">$F=6$,</span> $\\ \\nabla F=\\langle yz,\\ xz,\\ xy\\rangle$ → $\\nabla F(1,2,3)=\\langle6,\\ 3,\\ 2\\rangle$",
        "접평면: $6(x-1)+3(y-2)+2(z-3)=0 \\Rightarrow 6x+3y+2z=18$",
        "법선: $x=1+6t,\\ y=2+3t,\\ z=3+2t$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf n=\\langle6,3,2\\rangle\\text{,}$ $\\ |\\mathbf n|=\\sqrt{36+9+4}=7\\text{.}$ 원점 $O$ 에서 평면 위의 점 $P$ 로 가는 벡터 $\\overrightarrow{OP}=\\langle1,2,3\\rangle$",
        "$\\operatorname{comp}_{\\mathbf n}\\overrightarrow{OP}=\\dfrac{6+6+6}{7}=\\dfrac{18}{7}$ → 원점과 접평면 사이의 거리는 $\\dfrac{18}7$"
       ]
      ],
      [
       "c",
       [
        "$\\operatorname{proj}_{\\mathbf n}\\overrightarrow{OP}=\\dfrac{18}{49}\\langle6,3,2\\rangle$ 은 원점에서 평면에 내린 수선 벡터예요.",
        "가장 가까운 점 $\\Big(\\dfrac{108}{49},\\ \\dfrac{54}{49},\\ \\dfrac{36}{49}\\Big)$ (확인: $\\frac{648+162+72}{49}=\\frac{882}{49}=18$ 이라 평면 위)"
       ]
      ]
     ]
    },
    {
     "id": "q2",
     "no": "2",
     "type": "적분 순서 바꾸기 (이중·삼중)",
     "ref": "15.2 · 15.6",
     "mins": 7,
     "topics": [
      [
       8,
       "적분 순서 바꾸기 (이중·삼중)"
      ]
     ],
     "types": [
      [
       "15-order",
       "적분 순서 바꾸기"
      ],
      [
       "15-order3",
       "삼중적분 순서 바꾸기"
      ]
     ],
     "stem": "적분 순서를 바꾸어 다음 값을 구하시오.",
     "parts": [
      [
       "a",
       "$\\displaystyle\\int_0^1\\!\\!\\int_x^1\\frac{2}{1+y^4}\\,dy\\,dx$ [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^1\\!\\!\\int_y^1\\!\\!\\int_x^1 6\\ln(1+z^3)\\,dz\\,dx\\,dy$ [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac\\pi4$"
      ],
      [
       "b",
       "$2\\ln2-1$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\dfrac{1}{1+y^4}$ 은 $y$ 로 적분하기가 매우 번거로워요. 영역: $0\\le x\\le1,\\ x\\le y\\le1$ → $0\\le y\\le1,\\ 0\\le x\\le y$",
        "$$\\begin{aligned}\\int_0^1\\!\\!\\int_0^y\\frac{2}{1+y^4}\\,dx\\,dy&amp;=\\int_0^1\\frac{2y}{1+y^4}\\,dy\\\\&amp;=\\Big[\\arctan(y^2)\\Big]_0^1=\\frac\\pi4\\end{aligned}$$ ($w=y^2$ 로 치환)"
       ]
      ],
      [
       "b",
       [
        "$\\ln(1+z^3)$ 을 $z$ 로 먼저 적분하기 어려우니 $z$ 를 가장 바깥으로 보내요.",
        "영역: $0\\le y\\le1,\\ y\\le x\\le1,\\ x\\le z\\le1\\text{,}$ 즉 $0\\le y\\le x\\le z\\le1$ → $0\\le z\\le1,\\ 0\\le x\\le z,\\ 0\\le y\\le x$",
        "$$\\begin{aligned}&amp;\\int_0^1\\!\\!\\int_0^z\\!\\!\\int_0^x6\\ln(1+z^3)\\,dy\\,dx\\,dz\\\\&amp;=\\int_0^13z^2\\ln(1+z^3)\\,dz\\quad(w=1+z^3)\\\\&amp;=\\int_1^2\\ln w\\,dw=\\Big[w\\ln w-w\\Big]_1^2\\\\&amp;=2\\ln2-1\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q3",
     "no": "3",
     "type": "원주좌표 · 구면좌표 삼중적분",
     "ref": "15.7 · 15.8",
     "mins": 9,
     "topics": [
      [
       5,
       "원주좌표 삼중적분"
      ],
      [
       6,
       "구면좌표 삼중적분"
      ]
     ],
     "types": [
      [
       "15-cyl",
       "원주좌표"
      ],
      [
       "15-sphconv",
       "구면좌표로 바꾸어 쓰기"
      ],
      [
       "15-sph",
       "구면좌표 삼중적분"
      ]
     ],
     "stem": "다음 적분을 지시한 좌표계의 적분으로 바꾸어 쓰고, 그 값을 구하시오.",
     "parts": [
      [
       "a",
       "원주좌표로 바꾸어 계산하시오. [5점] $$\\int_{-1}^{1}\\!\\!\\int_{-\\sqrt{1-x^2}}^{\\sqrt{1-x^2}}\\!\\!\\int_{x^2+y^2}^{1}\\sqrt{x^2+y^2}\\,dz\\,dy\\,dx$$"
      ],
      [
       "b",
       "구면좌표로 바꾸어 계산하시오. [5점] $$\\int_0^2\\!\\!\\int_0^{\\sqrt{4-x^2}}\\!\\!\\int_0^{\\sqrt{4-x^2-y^2}}z\\sqrt{x^2+y^2+z^2}\\,dz\\,dy\\,dx$$"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\displaystyle\\int_0^{2\\pi}\\!\\!\\int_0^1\\!\\!\\int_{r^2}^1r^2\\,dz\\,dr\\,d\\theta=\\frac{4\\pi}{15}$"
      ],
      [
       "b",
       "$\\displaystyle\\int_0^{\\pi/2}\\!\\!\\int_0^{\\pi/2}\\!\\!\\int_0^2\\rho^4\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta=\\frac{8\\pi}{5}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "영역 읽기: $(x,y)$ 는 단위원판 <span class=\"nw\">$x^2+y^2\\le1$,</span> $z$ 는 포물면 $z=r^2$ 부터 평면 $z=1$ 까지 → $0\\le\\theta\\le2\\pi,\\ 0\\le r\\le1,\\ r^2\\le z\\le1$",
        "<span class=\"nw\">$\\sqrt{x^2+y^2}=r$,</span> $\\ dV=r\\,dz\\,dr\\,d\\theta\\text{:}$ $$\\begin{aligned}&amp;\\int_0^{2\\pi}\\!\\!\\int_0^1\\!\\!\\int_{r^2}^1r^2\\,dz\\,dr\\,d\\theta\\\\&amp;=2\\pi\\int_0^1(r^2-r^4)\\,dr\\\\&amp;=2\\pi\\Big(\\frac13-\\frac15\\Big)=\\frac{4\\pi}{15}\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "영역 읽기: $x\\ge0,\\ y\\ge0,\\ z\\ge0$ 이고 $x^2+y^2+z^2\\le4$ → 구의 제1팔분공간 부분: $0\\le\\theta\\le\\frac\\pi2,\\ 0\\le\\phi\\le\\frac\\pi2,\\ 0\\le\\rho\\le2$",
        "$z\\sqrt{x^2+y^2+z^2}=\\rho\\cos\\phi\\cdot\\rho\\text{,}$ $\\ dV=\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\text{:}$ $$\\begin{aligned}&amp;\\int_0^{\\pi/2}\\!\\!\\int_0^{\\pi/2}\\!\\!\\int_0^2\\rho^4\\cos\\phi\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta\\\\&amp;=\\frac\\pi2\\cdot\\Big[\\frac{\\sin^2\\phi}{2}\\Big]_0^{\\pi/2}\\cdot\\frac{2^5}{5}\\\\&amp;=\\frac\\pi2\\cdot\\frac12\\cdot\\frac{32}5=\\frac{8\\pi}{5}\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q4",
     "no": "4",
     "type": "미분가능성의 정의 · 극한의 존재성",
     "ref": "14.4 · 14.2",
     "mins": 9,
     "topics": [
      [
       4,
       "미분가능성의 정의"
      ],
      [
       3,
       "다변수 극한의 존재성"
      ]
     ],
     "types": [
      [
       "14-differentiable",
       "미분가능성의 정의 (ε₁·ε₂)"
      ],
      [
       "14-limit",
       "극한 계산·존재 보이기"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "$g(x)=x^3$ 이고 $\\Delta y=g(1+\\Delta x)-g(1)$ 일 때, $\\Delta y=g'(1)\\,\\Delta x+\\varepsilon\\,\\Delta x$ 를 만족하는 $\\varepsilon$ 을 $\\Delta x$ 로 나타내고, $\\Delta x\\to0$ 이면 $\\varepsilon\\to0$ 임을 보이시오. [3점]"
      ],
      [
       "b",
       "$\\displaystyle\\lim_{(x,y)\\to(0,0)}\\frac{1-\\cos(x^2+y^2)}{(x^2+y^2)^2}$ 가 존재하면 구하고, 존재하지 않으면 그 이유를 보이시오. [3점]"
      ],
      [
       "c",
       "$f(x,y)=\\dfrac{xy^2}{\\sqrt{x^2+y^2}}\\ \\big((x,y)\\ne(0,0)\\big)\\text{,}$ $\\ f(0,0)=0$ 일 때, $f_x(0,0),\\ f_y(0,0)$ 을 구하고 $f$ 가 원점에서 미분가능한지 정의를 이용해 판정하시오. [4점]<br>(미분가능성의 정의: $f$ 가 $(a,b)$ 에서 미분가능하다는 것은 $\\Delta z=f_x(a,b)\\Delta x+f_y(a,b)\\Delta y+\\varepsilon_1\\Delta x+\\varepsilon_2\\Delta y$ 이고 $(\\Delta x,\\Delta y)\\to(0,0)$ 일 때 $\\varepsilon_1,\\varepsilon_2\\to0$ 인 $\\varepsilon_1,\\varepsilon_2$ 가 존재한다는 뜻이다.)"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\varepsilon=3\\Delta x+(\\Delta x)^2\\to0$"
      ],
      [
       "b",
       "$\\dfrac12$"
      ],
      [
       "c",
       "$f_x(0,0)=f_y(0,0)=0\\text{,}$ 미분가능 $\\Big(\\varepsilon_1=\\dfrac{(\\Delta y)^2}{\\sqrt{(\\Delta x)^2+(\\Delta y)^2}},\\ \\varepsilon_2=0\\Big)$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "<span class=\"nw\">$g'(1)=3$,</span> $\\ \\Delta y=(1+\\Delta x)^3-1=3\\Delta x+3(\\Delta x)^2+(\\Delta x)^3$",
        "$\\Delta y=3\\Delta x+\\big(3\\Delta x+(\\Delta x)^2\\big)\\Delta x$ 이므로 $\\varepsilon=3\\Delta x+(\\Delta x)^2$",
        "$\\Delta x\\to0$ 이면 <span class=\"nw\">$\\varepsilon\\to0$.</span> (일반적으로 $\\varepsilon=\\frac{\\Delta y}{\\Delta x}-g'(a)$ 로 두면 미분의 정의에서 $\\varepsilon\\to0$ — 교수님이 설명한 유도와 같은 꼴이에요)"
       ]
      ],
      [
       "b",
       [
        "$x^2+y^2=w$ 로 두면 $(x,y)\\to(0,0)$ 일 때 $w\\to0^+$ 이고, 식은 $w$ 만의 함수 $\\dfrac{1-\\cos w}{w^2}$ 가 돼요 (다가가는 방향과 무관).",
        "$\\displaystyle\\lim_{w\\to0^+}\\frac{1-\\cos w}{w^2}=\\lim_{w\\to0^+}\\frac{\\sin w}{2w}=\\frac12$ (로피탈) → 극한은 존재하고 값은 $\\dfrac12$"
       ]
      ],
      [
       "c",
       [
        "$f(h,0)=0,\\ f(0,h)=0$ 이므로 $f_x(0,0)=f_y(0,0)=0$",
        "$$\\begin{aligned}\\Delta z&amp;=f(\\Delta x,\\Delta y)-f(0,0)\\\\&amp;=\\underbrace{\\frac{(\\Delta y)^2}{\\sqrt{(\\Delta x)^2+(\\Delta y)^2}}}_{\\varepsilon_1}\\,\\Delta x+\\underbrace{0}_{\\varepsilon_2}\\cdot\\Delta y\\end{aligned}$$",
        "$\\dfrac{|\\Delta y|}{\\sqrt{(\\Delta x)^2+(\\Delta y)^2}}\\le1$ 이므로 $|\\varepsilon_1|\\le|\\Delta y|\\to0$ (조임정리), $\\ \\varepsilon_2=0$ → 정의를 만족하므로 원점에서 **미분가능**해요."
       ]
      ]
     ]
    },
    {
     "id": "q5",
     "no": "5",
     "type": "극좌표 이중적분 (장미곡선)",
     "ref": "15.3",
     "mins": 8,
     "topics": [
      [
       1,
       "극좌표 꽃잎(장미곡선) 이중적분"
      ]
     ],
     "types": [
      [
       "15-polar",
       "극좌표 이중적분·넓이"
      ]
     ],
     "stem": "장미곡선 $r=4\\sin2\\theta$ (꽃잎 4장)에 대하여",
     "parts": [
      [
       "a",
       "장미곡선 전체로 둘러싸인 영역의 넓이를 구하시오. [3점]"
      ],
      [
       "b",
       "제1사분면의 꽃잎 $D\\ \\big(0\\le\\theta\\le\\frac\\pi2\\big)$ 에서 $\\displaystyle\\iint_D(x^2+y^2)\\,dA$ 를 구하시오. [3점]"
      ],
      [
       "c",
       "장미곡선의 내부이면서 원 $r=2\\sqrt2$ 의 외부인 영역(꽃잎 4장 전체)의 넓이를 구하시오. [4점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$8\\pi$"
      ],
      [
       "b",
       "$12\\pi$"
      ],
      [
       "c",
       "$8$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$$\\begin{aligned}A&amp;=\\frac12\\int_0^{2\\pi}16\\sin^22\\theta\\,d\\theta\\\\&amp;=4\\int_0^{2\\pi}(1-\\cos4\\theta)\\,d\\theta=8\\pi\\end{aligned}$$ ($0\\le\\theta\\le2\\pi$ 동안 꽃잎 4장을 한 번씩 그려요. 꽃잎 한 장은 <span class=\"nw\">$2\\pi$)</span>"
       ]
      ],
      [
       "b",
       [
        "$$\\begin{aligned}\\iint_Dr^2\\,dA&amp;=\\int_0^{\\pi/2}\\!\\!\\int_0^{4\\sin2\\theta}r^3\\,dr\\,d\\theta\\\\&amp;=64\\int_0^{\\pi/2}\\sin^42\\theta\\,d\\theta\\end{aligned}$$",
        "$u=2\\theta$ 로 치환하고 $\\sin^4u=\\dfrac38-\\dfrac12\\cos2u+\\dfrac18\\cos4u\\text{:}$ $\\ 32\\displaystyle\\int_0^{\\pi}\\sin^4u\\,du=32\\cdot\\frac{3\\pi}{8}=12\\pi$"
       ]
      ],
      [
       "c",
       [
        "교점: $4\\sin2\\theta=2\\sqrt2 \\Rightarrow \\sin2\\theta=\\frac{\\sqrt2}2 \\Rightarrow \\theta=\\frac\\pi8,\\ \\frac{3\\pi}8$ (제1사분면 꽃잎)",
        "$$\\begin{aligned}&amp;\\frac12\\int_{\\pi/8}^{3\\pi/8}\\big(16\\sin^22\\theta-8\\big)\\,d\\theta\\\\&amp;=\\int_{\\pi/8}^{3\\pi/8}(-4\\cos4\\theta)\\,d\\theta\\\\&amp;=-\\Big[\\sin4\\theta\\Big]_{\\pi/8}^{3\\pi/8}=-(-1-1)=2\\end{aligned}$$",
        "꽃잎 4장이 합동이므로 $4\\times2=8$ (답에 $\\pi$ 가 없어요)"
       ]
      ]
     ]
    },
    {
     "id": "q6",
     "no": "6",
     "type": "연쇄법칙 (음함수) · 그래디언트",
     "ref": "14.5 · 14.6",
     "mins": 8,
     "topics": [
      [
       12,
       "연쇄법칙"
      ],
      [
       10,
       "편도함수와 그래디언트"
      ]
     ],
     "types": [
      [
       "14-implicit",
       "음함수 편미분"
      ],
      [
       "14-maxrate",
       "최대 변화율과 방향"
      ],
      [
       "14-dir",
       "방향도함수"
      ]
     ],
     "stem": "방정식 $e^{xz}+yz=3$ 이 점 $(0,\\ 2,\\ 1)$ 근처에서 $z=z(x,y)$ 를 정한다.",
     "parts": [
      [
       "a",
       "양변을 $x,\\ y$ 에 대해 연쇄법칙으로 미분하여 $z_x(0,2),\\ z_y(0,2)$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "$(0,2)$ 에서 $\\nabla z$ 를 구하고, $z$ 가 가장 빠르게 증가하는 방향(단위벡터)과 그 변화율을 구하시오. [3점]"
      ],
      [
       "c",
       "$(0,2)$ 에서 벡터 $\\langle3,\\ -4\\rangle$ 방향으로의 $z$ 의 방향도함수를 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$z_x(0,2)=-\\dfrac12,\\ \\ z_y(0,2)=-\\dfrac12$"
      ],
      [
       "b",
       "$\\nabla z(0,2)=\\big\\langle-\\frac12,\\ -\\frac12\\big\\rangle\\text{,}$ 방향 $\\dfrac{1}{\\sqrt2}\\langle-1,\\ -1\\rangle\\text{,}$ 변화율 $\\dfrac{\\sqrt2}{2}$"
      ],
      [
       "c",
       "$\\dfrac1{10}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$x$ 로 미분 ($z$ 는 $x,y$ 의 함수): $e^{xz}(z+x\\,z_x)+y\\,z_x=0$ → $(0,2,1)$ 에서 $1\\cdot(1+0)+2z_x=0 \\Rightarrow z_x=-\\dfrac12$",
        "$y$ 로 미분: $e^{xz}\\,x\\,z_y+z+y\\,z_y=0$ → $(0,2,1)$ 에서 $0+1+2z_y=0 \\Rightarrow z_y=-\\dfrac12$",
        "(공식 $z_x=-\\dfrac{F_x}{F_z},\\ z_y=-\\dfrac{F_y}{F_z}\\text{,}$ $F=e^{xz}+yz-3$ 으로 구해도 같아요: $F_x=1,\\ F_y=1,\\ F_z=2\\text{)}$"
       ]
      ],
      [
       "b",
       [
        "$\\nabla z(0,2)=\\langle z_x,\\ z_y\\rangle=\\big\\langle-\\frac12,-\\frac12\\big\\rangle$",
        "가장 빠르게 증가하는 방향 $\\dfrac{\\nabla z}{|\\nabla z|}=\\dfrac1{\\sqrt2}\\langle-1,-1\\rangle\\text{,}$ 변화율 $|\\nabla z|=\\sqrt{\\frac14+\\frac14}=\\dfrac{\\sqrt2}2$"
       ]
      ],
      [
       "c",
       [
        "단위벡터 $\\mathbf u=\\dfrac15\\langle3,-4\\rangle$",
        "$D_{\\mathbf u}z=\\nabla z\\cdot\\mathbf u=\\dfrac{-3+4}{10}=\\dfrac1{10}$"
       ]
      ]
     ]
    },
    {
     "id": "q7",
     "no": "7",
     "type": "변수변환 (야코비안)",
     "ref": "15.9",
     "mins": 9,
     "topics": [
      [
       7,
       "u·v 변수변환 (야코비안)"
      ]
     ],
     "types": [
      [
       "15-change",
       "변수변환·야코비안"
      ]
     ],
     "stem": "$R$ 은 제1사분면에서 곡선 $xy=1,\\ xy=4$ 와 직선 $y=x,\\ y=4x$ 로 둘러싸인 영역이다. 변환 $u=xy,\\ v=\\dfrac yx$ 를 이용하여",
     "parts": [
      [
       "a",
       "$\\dfrac{\\partial(u,v)}{\\partial(x,y)}$ 를 구하여 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}$ 를 $u,v$ 로 나타내고, $R$ 에 대응하는 $uv$ 평면의 영역 $S$ 를 구하시오. [4점]"
      ],
      [
       "b",
       "$\\displaystyle\\iint_Ry^2\\,dA$ 를 구하시오. [6점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac{1}{2v}\\text{,}$ $\\ S=\\{(u,v)\\mid1\\le u\\le4,\\ 1\\le v\\le4\\}$"
      ],
      [
       "b",
       "$\\dfrac{45}{4}$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$$\\frac{\\partial(u,v)}{\\partial(x,y)}=\\begin{vmatrix}y&amp;x\\\\[2pt]-\\frac{y}{x^2}&amp;\\frac1x\\end{vmatrix}=\\frac yx+\\frac yx=\\frac{2y}{x}=2v$$",
        "따라서 $\\dfrac{\\partial(x,y)}{\\partial(u,v)}=\\dfrac{1}{2v}$ (제1사분면이라 <span class=\"nw\">$v>0$).</span> (역변환 $x=\\sqrt{u/v},\\ y=\\sqrt{uv}$ 로 직접 계산해도 같아요)",
        "$xy=1,\\ xy=4$ → <span class=\"nw\">$u=1,\\ u=4$;</span>&emsp;$\\ y=x,\\ y=4x$ → $v=1,\\ v=4$ → $S:\\ 1\\le u\\le4,\\ 1\\le v\\le4$"
       ]
      ],
      [
       "b",
       [
        "$uv=xy\\cdot\\dfrac yx=y^2$ 이므로 피적분함수는 <span class=\"nw\">$uv$,</span> $\\ dA=\\dfrac{1}{2v}\\,du\\,dv$",
        "$$\\begin{aligned}\\iint_Ry^2\\,dA&amp;=\\int_1^4\\!\\!\\int_1^4uv\\cdot\\frac1{2v}\\,du\\,dv\\\\&amp;=\\frac12\\int_1^4\\!\\!\\int_1^4u\\,du\\,dv=\\frac12\\cdot\\frac{15}{2}\\cdot3=\\frac{45}{4}\\end{aligned}$$"
       ]
      ]
     ]
    },
    {
     "id": "q8",
     "no": "8",
     "type": "곡선의 길이 · 사영(comp·proj)",
     "ref": "13.3 · 12.3",
     "mins": 6,
     "topics": [
      [
       11,
       "곡선의 길이"
      ],
      [
       13,
       "스칼라 사영·벡터 사영 (comp·proj)"
      ]
     ],
     "types": [
      [
       "13-arc",
       "호의 길이"
      ],
      [
       "12-proj",
       "정사영과 일"
      ]
     ],
     "stem": "평면곡선 $\\mathbf r(t)=\\langle 3t^2,\\ 2t^3\\rangle$ 에 대하여",
     "parts": [
      [
       "a",
       "$0\\le t\\le\\sqrt3$ 부분의 길이를 구하시오. [3점]"
      ],
      [
       "b",
       "$t=1$ 에서의 $\\mathbf v=\\mathbf r'(1),\\ \\mathbf a=\\mathbf r''(1)$ 에 대하여 $\\operatorname{comp}_{\\mathbf v}\\mathbf a$ 와 $\\operatorname{proj}_{\\mathbf v}\\mathbf a$ 를 구하시오. [4점]"
      ],
      [
       "c",
       "$\\mathbf a$ 를 $\\mathbf v$ 에 평행한 벡터와 $\\mathbf v$ 에 수직인 벡터의 합으로 나타내고, 수직인 벡터의 크기를 구하시오. [3점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$14$"
      ],
      [
       "b",
       "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=9\\sqrt2\\text{,}$ $\\ \\operatorname{proj}_{\\mathbf v}\\mathbf a=\\langle9,\\ 9\\rangle$"
      ],
      [
       "c",
       "$\\mathbf a=\\langle9,9\\rangle+\\langle-3,3\\rangle\\text{,}$ 수직인 벡터의 크기 $3\\sqrt2$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\mathbf r'(t)=\\langle6t,\\ 6t^2\\rangle\\text{,}$ $\\ |\\mathbf r'(t)|=6t\\sqrt{1+t^2}\\ (t\\ge0)$",
        "$w=1+t^2$ 로 치환: $$\\begin{aligned}L&amp;=\\int_0^{\\sqrt3}6t\\sqrt{1+t^2}\\,dt=\\int_1^43\\sqrt w\\,dw\\\\&amp;=\\Big[2w^{3/2}\\Big]_1^4=16-2=14\\end{aligned}$$"
       ]
      ],
      [
       "b",
       [
        "$\\mathbf r''(t)=\\langle6,\\ 12t\\rangle$ → $\\mathbf v=\\langle6,6\\rangle\\text{,}$ $\\ \\mathbf a=\\langle6,12\\rangle\\text{,}$ $\\ |\\mathbf v|=6\\sqrt2\\text{,}$ $\\ \\mathbf a\\cdot\\mathbf v=36+72=108$",
        "$\\operatorname{comp}_{\\mathbf v}\\mathbf a=\\dfrac{108}{6\\sqrt2}=9\\sqrt2\\text{,}$ $\\quad\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\dfrac{108}{72}\\langle6,6\\rangle=\\langle9,\\ 9\\rangle$"
       ]
      ],
      [
       "c",
       [
        "수직 성분: $\\mathbf a-\\operatorname{proj}_{\\mathbf v}\\mathbf a=\\langle-3,\\ 3\\rangle$ (확인: $\\langle-3,3\\rangle\\cdot\\langle6,6\\rangle=0\\text{)}$",
        "크기 $\\sqrt{9+9}=3\\sqrt2$"
       ]
      ]
     ]
    },
    {
     "id": "q9",
     "no": "9",
     "type": "그린 정리 · 곡선 나누어 직접 계산",
     "ref": "16.2 · 16.4",
     "mins": 9,
     "topics": [
      [
       9,
       "그린 정리 · 곡선 나누어 직접 계산"
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
      ],
      [
       "16-vector",
       "벡터 선적분·일"
      ]
     ],
     "stem": "$D$ 는 위쪽 반타원 영역 $\\dfrac{x^2}{9}+\\dfrac{y^2}{4}\\le1,\\ y\\ge0$ 이고, $C$ 는 $D$ 의 경계로 양의 방향이다. $\\displaystyle I=\\oint_C(x^2-y)\\,dx+(x+y^2)\\,dy$ 에 대하여",
     "parts": [
      [
       "a",
       "$C$ 를 선분과 반타원 호로 나누어 $I$ 를 직접 계산하시오. [4점]"
      ],
      [
       "b",
       "그린 정리를 이용해 $I$ 를 계산하시오. [4점]"
      ],
      [
       "c",
       "$\\displaystyle A=\\frac12\\oint_Cx\\,dy-y\\,dx$ 를 계산하여 $D$ 의 넓이를 구하시오. [2점]"
      ]
     ],
     "answer": [
      [
       "a",
       "$6\\pi$"
      ],
      [
       "b",
       "$6\\pi$"
      ],
      [
       "c",
       "$3\\pi$"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "양의 방향: $C_1$ 은 <span class=\"nw\">$x$축</span> 위 선분 <span class=\"nw\">$(-3,0)\\to(3,0)$,</span> $C_2$ 는 호 $x=3\\cos t,\\ y=2\\sin t\\ (0\\le t\\le\\pi)$",
        "$C_1:\\ y=0,\\ dy=0$ → $\\displaystyle\\int_{-3}^3x^2\\,dx=18$",
        "<span class=\"nw\">$C_2$:</span> $dx=-3\\sin t\\,dt,\\ dy=2\\cos t\\,dt$ $$\\begin{aligned}&amp;\\int_0^\\pi\\Big[(9\\cos^2t-2\\sin t)(-3\\sin t)\\\\&amp;\\qquad+(3\\cos t+4\\sin^2t)(2\\cos t)\\Big]dt\\\\&amp;=\\int_0^\\pi\\big(-27\\cos^2t\\sin t+6\\sin^2t\\\\&amp;\\qquad+6\\cos^2t+8\\sin^2t\\cos t\\big)\\,dt\\\\&amp;=-18+3\\pi+3\\pi+0=6\\pi-18\\end{aligned}$$",
        "$I=18+(6\\pi-18)=6\\pi$"
       ]
      ],
      [
       "b",
       [
        "$P=x^2-y,\\ Q=x+y^2$ → $Q_x-P_y=1-(-1)=2$",
        "$I=\\displaystyle\\iint_D2\\,dA=2\\times(\\text{반타원의 넓이})=2\\cdot\\frac{\\pi\\cdot3\\cdot2}{2}=6\\pi$ — (a)와 같아요."
       ]
      ],
      [
       "c",
       [
        "$C_1$ 에서는 $y=0,\\ dy=0$ 이라 <span class=\"nw\">$0$.</span>&emsp;<span class=\"nw\">$C_2$:</span> $x\\,dy-y\\,dx=(3\\cos t)(2\\cos t)\\,dt-(2\\sin t)(-3\\sin t)\\,dt=6\\,dt$",
        "$A=\\dfrac12\\displaystyle\\int_0^\\pi6\\,dt=3\\pi$ (반타원 넓이 $\\frac12\\pi ab$ 와 같아요)"
       ]
      ]
     ]
    },
    {
     "id": "q10",
     "no": "10",
     "type": "라그랑주 승수법 · 2계 도함수 판정법",
     "ref": "14.8 · 14.7",
     "mins": 9,
     "topics": [
      [
       2,
       "라그랑주 승수법"
      ],
      [
       15,
       "2계 도함수 판정법 (극값·안장점)"
      ]
     ],
     "types": [
      [
       "14-lagrange",
       "라그랑주 승수"
      ],
      [
       "14-crit",
       "임계점·2계 판정법"
      ]
     ],
     "stem": "다음 물음에 답하시오.",
     "parts": [
      [
       "a",
       "라그랑주 승수법으로 평면 $x+2y+3z=18$ 의 제1팔분공간 부분(<span class=\"nw\">$x,y,z>0$)에서</span> $f(x,y,z)=xyz$ 의 최댓값을 구하시오. [5점]"
      ],
      [
       "b",
       "$g(x,y)=x^3-12x+y^3-3y$ 의 임계점을 모두 구하고, 2계 도함수 판정법으로 극댓값·극솟값·안장점을 판정하시오. [5점]"
      ]
     ],
     "answer": [
      [
       "a",
       "최댓값 $36$ (점 <span class=\"nw\">$(6,\\ 3,\\ 2)$)</span>"
      ],
      [
       "b",
       "<span class=\"nw\">$(2,1)$:</span> 극솟값 <span class=\"nw\">$-18$,</span>&emsp;<span class=\"nw\">$(-2,-1)$:</span> 극댓값 <span class=\"nw\">$18$,</span>&emsp;<span class=\"nw\">$(2,-1),\\ (-2,1)$:</span> 안장점"
      ]
     ],
     "solution": [
      [
       "a",
       [
        "$\\nabla f=\\lambda\\nabla h\\text{,}$ <span class=\"nw\">$\\ h=x+2y+3z$:</span> $\\ yz=\\lambda,\\ \\ xz=2\\lambda,\\ \\ xy=3\\lambda$",
        "$x,y,z>0$ 이므로 첫 두 식을 나누면 $\\dfrac xy=2 \\Rightarrow x=2y\\text{,}$ 첫·셋째 식을 나누면 $\\dfrac xz=3 \\Rightarrow x=3z$",
        "제약식에 대입: $x+x+x=18 \\Rightarrow x=6,\\ y=3,\\ z=2$ → $f=36$",
        "좌표 중 하나가 $0$ 에 가까워지면 $f\\to0$ 이므로 이 값이 최댓값이에요."
       ]
      ],
      [
       "b",
       [
        "$g_x=3x^2-12=0 \\Rightarrow x=\\pm2\\text{,}$ $\\ g_y=3y^2-3=0 \\Rightarrow y=\\pm1$ → 임계점 4개 $(\\pm2,\\ \\pm1)$",
        "$g_{xx}=6x,\\ g_{yy}=6y,\\ g_{xy}=0$ → $D=36xy$",
        "<span class=\"nw\">$(2,1)$:</span> $D=72>0,\\ g_{xx}=12>0$ → 극솟값 <span class=\"nw\">$g=8-24+1-3=-18$.</span>&emsp;<span class=\"nw\">$(-2,-1)$:</span> $D=72>0,\\ g_{xx}=-12\\lt 0$ → 극댓값 $g=-8+24-1+3=18$",
        "<span class=\"nw\">$(2,-1),\\ (-2,1)$:</span> $D=-72\\lt 0$ → 안장점"
       ]
      ]
     ]
    }
   ]
  }
 ]
};

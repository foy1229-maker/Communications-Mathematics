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
  }
 ]
};

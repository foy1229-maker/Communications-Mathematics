"""문제 원본 파일 하나(또는 몇 개)만 빠르게 검산하는 개발용 스크립트.

사용법 (저장소 루트에서):
    python3 tools/devcheck.py level1_c14 level1_c15
모듈 안의 문제마다 check() 를 실행하고, $ 짝·id 중복·필수 항목을 확인해요.
전체 빌드(assets/problems.js 생성)는 tools/build.py 로 해요.
"""
import importlib
import os
import re
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bank_lib  # noqa: E402
from bank_lib import PROBLEMS  # noqa: E402


def dollars_ok(text):
    return text.replace("$$", "").count("$") % 2 == 0


def main(mods):
    bad = 0
    seen = {}
    for name in mods:
        start = len(PROBLEMS)
        importlib.import_module(name)
        items = PROBLEMS[start:]
        t0 = time.time()
        for p in items:
            pid = p["id"]
            if pid in seen:
                print(f"DUP  {pid} ({seen[pid]} / {name})")
                bad += 1
            seen[pid] = name
            for f in ("q", "hint", "ans"):
                if not dollars_ok(p[f]):
                    print(f"$    {pid} {f}")
                    bad += 1
            for i, line in enumerate(p["sol"]):
                if not dollars_ok(line):
                    print(f"$    {pid} sol[{i}]")
                    bad += 1
            try:
                p["check"]()
            except Exception:  # noqa: BLE001
                bad += 1
                print(f"FAIL {pid}")
                traceback.print_exc(limit=2)
        print(f"{name}: {len(items)}문제 검산 ({time.time() - t0:.1f}s)")
    if bad:
        raise SystemExit(f"문제 {bad}건")
    print("모두 통과")


if __name__ == "__main__":
    main(sys.argv[1:])

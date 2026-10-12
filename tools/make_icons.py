"""파비콘 만들기: 세로로 긴 엠블럼(164x220)을 정사각형 캔버스 가운데에 비율 그대로 놓아요.

브라우저 탭은 아이콘을 정사각형으로 늘려 그리기 때문에, 원본을 그대로 쓰면 엠블럼이 옆으로 퍼져 보여요.

    pip install pillow
    python3 tools/make_icons.py
"""
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"


def fit(emblem, box_w, box_h):
    """비율을 지키며 box 안에 들어가게 줄이기"""
    scale = min(box_w / emblem.width, box_h / emblem.height)
    size = (max(1, round(emblem.width * scale)), max(1, round(emblem.height * scale)))
    return emblem.resize(size, Image.LANCZOS)


def tab_icon(emblem, n):
    """탭 아이콘: 투명 배경, 세로를 꽉 채우고 좌우는 여백"""
    art = fit(emblem, n, n)
    if n <= 32:
        art = art.filter(ImageFilter.UnsharpMask(radius=0.6, percent=60, threshold=1))
    canvas = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    canvas.alpha_composite(art, ((n - art.width) // 2, (n - art.height) // 2))
    return canvas


def touch_icon(emblem, n=180):
    """홈 화면 아이콘(iOS): 투명 부분이 검게 칠해지므로 사이트 배경색 위에 올림"""
    canvas = Image.new("RGBA", (n, n), (11, 26, 32, 255))
    glow = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    # 위쪽이 살짝 밝은 판 (사이트 카드 면과 같은 느낌)
    for y in range(n):
        t = y / (n - 1)
        r, g, b = (round(18 + (11 - 18) * t), round(48 + (26 - 48) * t), round(58 + (32 - 58) * t))
        for x in range(n):
            glow.putpixel((x, y), (r, g, b, 255))
    canvas.alpha_composite(glow)
    art = fit(emblem, round(n * 0.62), round(n * 0.78))
    canvas.alpha_composite(art, ((n - art.width) // 2, (n - art.height) // 2))
    return canvas.convert("RGB")


def main():
    emblem = Image.open(IMG / "ku-emblem.webp").convert("RGBA")
    for n in (16, 32):
        tab_icon(emblem, n).save(IMG / f"favicon-{n}.png", optimize=True)
    touch_icon(emblem).save(IMG / "apple-touch-icon.png", optimize=True)
    print("favicon-16.png, favicon-32.png, apple-touch-icon.png")


if __name__ == "__main__":
    main()

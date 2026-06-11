"""
ブログカバー画像生成スクリプト
サイズ: 1536x1024px (既存カバーと同じ)
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

W, H = 1536, 1024
FONT_BOLD = r"C:\Windows\Fonts\BIZ-UDGothicB.ttc"
FONT_REG  = r"C:\Windows\Fonts\BIZ-UDGothicR.ttc"

# ---------- 記事データ ----------
articles = [
    {
        "slug": "chatgpt-prompt-writing-guide",
        "title": "ChatGPTプロンプトの\n書き方入門",
        "subtitle": "初心者が最初に覚える5つのコツ",
        "tags": "#ChatGPT  #AI活用  #初心者",
        "color1": (30, 120, 220),
        "color2": (10, 60, 150),
        "accent": (80, 200, 255),
        "icon": "✍️",
    },
    {
        "slug": "ai-three-tools-comparison-2026",
        "title": "ChatGPT・Claude・Gemini\n徹底比較",
        "subtitle": "用途別・あなたに合うAIはどれ？",
        "tags": "#比較  #ChatGPT  #Claude  #Gemini",
        "color1": (100, 30, 180),
        "color2": (40, 10, 100),
        "accent": (220, 130, 255),
        "icon": "⚖️",
    },
    {
        "slug": "free-ai-tools-side-job",
        "title": "無料AIツールだけで\n副業を始める方法",
        "subtitle": "初期費用ゼロでスタート",
        "tags": "#副業  #AI活用  #初心者",
        "color1": (20, 150, 100),
        "color2": (10, 80, 50),
        "accent": (80, 230, 160),
        "icon": "💰",
    },
    {
        "slug": "ai-work-efficiency-tips",
        "title": "仕事でAIを使うと\n何が変わる？",
        "subtitle": "実際に試してわかった10の効果",
        "tags": "#仕事効率化  #AI活用  #ChatGPT",
        "color1": (200, 90, 20),
        "color2": (130, 40, 10),
        "accent": (255, 180, 80),
        "icon": "🚀",
    },
    {
        "slug": "kdp-ai-publishing-guide",
        "title": "AIでKindle本を\n作る手順を全公開",
        "subtitle": "KDP副業の始め方ガイド",
        "tags": "#KDP  #副業  #AI活用",
        "color1": (20, 60, 140),
        "color2": (10, 30, 80),
        "accent": (120, 180, 255),
        "icon": "📚",
    },
    {
        "slug": "ai-habit-tips",
        "title": "AIを毎日使い続ける\n習慣化のコツ",
        "subtitle": "3ステップで定着させる方法",
        "tags": "#習慣化  #AI活用  #仕事効率化",
        "color1": (20, 150, 150),
        "color2": (10, 80, 90),
        "accent": (80, 240, 220),
        "icon": "🔄",
    },
    {
        "slug": "gemini-beginner-guide",
        "title": "Geminiの使い方と\n活用例まとめ",
        "subtitle": "GoogleアカウントだけでOK・初心者向け",
        "tags": "#Gemini  #AI活用  #初心者",
        "color1": (30, 100, 200),
        "color2": (180, 40, 20),
        "accent": (255, 220, 80),
        "icon": "🔷",
    },
    {
        "slug": "ai-blog-writing-workflow",
        "title": "AIとブログを組み合わせる\n私のワークフロー",
        "subtitle": "記事作成を時短する具体的な手順",
        "tags": "#AI活用  #副業  #仕事効率化",
        "color1": (180, 60, 20),
        "color2": (100, 30, 10),
        "accent": (255, 160, 60),
        "icon": "📝",
    },
    {
        "slug": "ai-side-job-2026-trends",
        "title": "2026年注目の\nAI副業5選",
        "subtitle": "今始めると有利な理由",
        "tags": "#副業  #AI活用  #トレンド",
        "color1": (80, 20, 140),
        "color2": (30, 10, 80),
        "accent": (200, 120, 255),
        "icon": "📈",
    },
    {
        "slug": "claude-ai-guide",
        "title": "Claudeとは？\nChatGPTとの違いを解説",
        "subtitle": "実際に使い比べてわかったこと",
        "tags": "#Claude  #AI活用  #比較",
        "color1": (160, 60, 30),
        "color2": (90, 20, 10),
        "accent": (255, 150, 100),
        "icon": "🤖",
    },
]

# ---------- 描画ヘルパー ----------

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_gradient(draw, w, h, c1, c2):
    """左上→右下のグラデーション背景"""
    for y in range(h):
        t = y / h
        for x in range(w):
            s = x / w
            col = lerp_color(lerp_color(c1, c2, t), lerp_color(c2, c1, s), 0.4)
            draw.point((x, y), fill=col)


def draw_circles(draw, w, h, accent):
    """装飾的な半透明サークル"""
    circles = [
        (w * 0.85, h * 0.15, 260),
        (w * 0.10, h * 0.80, 180),
        (w * 0.75, h * 0.75, 120),
    ]
    for cx, cy, r in circles:
        a = 40
        bbox = [cx - r, cy - r, cx + r, cy + r]
        overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse(bbox, fill=(*accent, a))
        # PNGオーバーレイは後でマージ
        draw._image.paste(overlay, mask=overlay)


def wrap_text(text, font, max_width, draw):
    """簡易折り返し（\n 手動指定を優先）"""
    lines = []
    for para in text.split("\n"):
        words = list(para)
        line = ""
        for ch in words:
            test = line + ch
            w = draw.textlength(test, font=font)
            if w > max_width:
                lines.append(line)
                line = ch
            else:
                line = test
        lines.append(line)
    return lines


def make_cover(article):
    slug     = article["slug"]
    title    = article["title"]
    subtitle = article["subtitle"]
    tags     = article["tags"]
    c1       = article["color1"]
    c2       = article["color2"]
    accent   = article["accent"]
    icon     = article["icon"]

    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)

    # ---- 背景グラデーション ----
    draw_gradient(draw, W, H, c1, c2)

    # ---- 半透明サークル ----
    # RGBA合成でオーバーレイ
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for cx, cy, r, alpha in [
        (W * 0.88, H * 0.12, 300, 35),
        (W * 0.08, H * 0.85, 200, 30),
        (W * 0.72, H * 0.78, 140, 25),
        (W * 0.45, H * 0.05, 100, 20),
    ]:
        od.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*accent, alpha))
    base_rgba = img.convert("RGBA")
    combined  = Image.alpha_composite(base_rgba, overlay)
    img = combined.convert("RGB")
    draw = ImageDraw.Draw(img)

    # ---- 左帯（アクセントライン）----
    draw.rectangle([0, 0, 12, H], fill=accent)

    # ---- アイコン文字 ----
    try:
        icon_font = ImageFont.truetype(r"C:\Windows\Fonts\seguiemj.ttf", 160)
        draw.text((W - 280, H // 2 - 120), icon, font=icon_font,
                  fill=(*accent, 60) if False else accent,
                  embedded_color=True)
    except Exception:
        pass  # 絵文字フォントなければスキップ

    # ---- タイトル ----
    title_font = ImageFont.truetype(FONT_BOLD, 100)
    lines = title.split("\n")
    line_h = 115
    total_h = line_h * len(lines)
    y_start = (H - total_h) // 2 - 60

    # 影
    for i, line in enumerate(lines):
        y = y_start + i * line_h
        draw.text((82, y + 4), line, font=title_font, fill=(0, 0, 0, 100))

    # 本文
    for i, line in enumerate(lines):
        y = y_start + i * line_h
        draw.text((80, y), line, font=title_font, fill=(255, 255, 255))

    # ---- サブタイトル ----
    sub_font = ImageFont.truetype(FONT_REG, 52)
    sub_y = y_start + len(lines) * line_h + 30
    draw.text((82, sub_y + 3), subtitle, font=sub_font, fill=(0, 0, 0, 80))
    draw.text((80, sub_y), subtitle, font=sub_font,
              fill=tuple(min(255, v + 180) for v in accent))

    # ---- 区切り線 ----
    line_y = sub_y + 80
    draw.rectangle([80, line_y, 600, line_y + 4],
                   fill=tuple(min(255, v + 120) for v in accent))

    # ---- タグ ----
    tag_font = ImageFont.truetype(FONT_REG, 38)
    draw.text((80, line_y + 20), tags, font=tag_font,
              fill=tuple(min(255, int(v * 0.9 + 100)) for v in accent))

    # ---- ブログ名 ----
    blog_font = ImageFont.truetype(FONT_BOLD, 36)
    blog_text = "毎日AI"
    bw = draw.textlength(blog_text, font=blog_font)
    draw.text((W - bw - 40, H - 60), blog_text, font=blog_font,
              fill=(255, 255, 255, 180))

    # ---- 保存 ----
    out_dir = rf"C:\Users\user\myblog\content\posts\{slug}"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cover.png")
    img.save(out_path, "PNG")
    print(f"OK: {slug}")


# ---------- 実行 ----------
for a in articles:
    make_cover(a)

print("\nDone! 10 covers generated.")

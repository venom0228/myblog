import os
import re

BASE_DIR = r"C:\Users\user\myblog\content\posts"
YOUTUBE_CHANNEL = "https://www.youtube.com/@16bit_chill"

# 削除対象のYouTube CTAセクション（全10記事から消す）
YT_SECTION_PATTERN = re.compile(
    r"\n---\n\n## 動画でも解説しています\n.*?チャンネル登録しておくと、新しい動画を見逃しません！\n",
    re.DOTALL
)

# BGMチャンネルの誘導（作業・集中系の記事に追加）
BGM_SECTION = """
---

## 作業中のBGMにどうぞ

副業作業や勉強中に集中したいとき、Sunoで制作した**AI作業用BGM**をYouTubeで公開しています。
ループ再生しながら作業すると、集中力が続きますよ。

▶ **[作業用BGMチャンネル「16bit_chill」はこちら]({url})**
""".format(url=YOUTUBE_CHANNEL)

# 新規10記事（全部からYouTube CTAを削除）
NEW_ARTICLES = [
    "elevenlabs-voice-side-job",
    "runway-ai-video-guide",
    "chatgpt-o3-review",
    "ai-agent-guide",
    "x-twitter-ai-strategy",
    "amazon-affiliate-ai-guide",
    "ideogram-ai-image",
    "ai-automation-workflow",
    "voice-input-productivity",
    "ai-side-job-summer2026",
]

# BGM誘導を追加する記事（作業・集中・副業効率化系）
BGM_ARTICLES = [
    "voice-input-productivity",      # 音声入力×AIで作業時間を半分に
    "ai-automation-workflow",         # AI自動化ワークフローで副業収入UP
    "ai-side-job-summer2026",         # 2026年夏に稼げるAI副業まとめ（Suno副業として言及）
    "suno-bgm-youtube",               # 既存記事：Suno BGM → 直接関連
    "ai-work-efficiency-tips",        # 既存記事：仕事効率化
    "ai-habits-for-productivity",     # 既存記事：生産性・習慣化
]


def remove_yt_section(content):
    """YouTube CTAセクションを削除"""
    return YT_SECTION_PATTERN.sub("", content)


def has_bgm_section(content):
    """すでにBGMセクションが入っているか確認"""
    return "作業中のBGMにどうぞ" in content or "16bit_chill" in content


def process_article(slug, remove_yt=False, add_bgm=False):
    path = os.path.join(BASE_DIR, slug, "index.md")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    if remove_yt:
        new_content = remove_yt_section(content)
        if new_content != content:
            content = new_content
            changed = True
            print(f"  [YT削除] {slug}")

    if add_bgm and not has_bgm_section(content):
        content = content.rstrip() + "\n" + BGM_SECTION
        changed = True
        print(f"  [BGM追加] {slug}")

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(f"  [変更なし] {slug}")


if __name__ == "__main__":
    print("=== YouTube CTAを削除（新規10記事）===")
    for slug in NEW_ARTICLES:
        process_article(slug, remove_yt=True, add_bgm=False)

    print("\n=== BGMチャンネル誘導を追加（関連記事のみ）===")
    for slug in BGM_ARTICLES:
        process_article(slug, remove_yt=False, add_bgm=True)

    print("\nDONE!")

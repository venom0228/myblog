import os
import re

BASE_DIR = r"C:\Users\user\myblog\content\posts"

# 修正対象の記事スラッグ（create_articles3 と create_articles4 で作った20記事）
SLUGS = [
    # create_articles3
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
    # create_articles4
    "luma-ai-video-guide",
    "ai-proofreading-guide",
    "chatgpt-custom-instructions",
    "ai-podcast-script",
    "fiverr-ai-side-job",
    "ai-thumbnail-design",
    "kling-ai-video",
    "ai-newsletter-guide",
    "chatgpt-memory-guide",
    "ai-side-job-mistakes",
]

def fix_toml_tags(content):
    """
    tags = [
      - "tag1"
      - "tag2"
    ]
    を
    tags = [
      "tag1",
      "tag2",
    ]
    に修正する
    """
    def replace_tags(m):
        block = m.group(0)
        # タグを抽出
        tags = re.findall(r'- "([^"]+)"', block)
        if not tags:
            return block
        tag_lines = "\n".join([f'  "{t}",' for t in tags])
        return f"tags = [\n{tag_lines}\n]"

    return re.sub(
        r'tags = \[\n(?:\s+- "[^"]+"\n)+\]',
        replace_tags,
        content
    )

fixed_count = 0
for slug in SLUGS:
    path = os.path.join(BASE_DIR, slug, "index.md")
    if not os.path.exists(path):
        print(f"NOT FOUND: {slug}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = fix_toml_tags(content)

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"FIXED: {slug}")
        fixed_count += 1
    else:
        print(f"NO CHANGE: {slug}")

print(f"\nDONE: {fixed_count} files fixed")

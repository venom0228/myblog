import os
import re

BASE_DIR = r"C:\Users\user\myblog\content\posts"

SLUGS = [
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

# [cover]\n  image = "cover.png"\n  alt = "..."\n を image = "cover.png" に置換
COVER_PATTERN = re.compile(
    r'\[cover\]\n\s+image = "cover\.png"\n\s+alt = "[^"]*"\n',
    re.MULTILINE
)

fixed = 0
for slug in SLUGS:
    path = os.path.join(BASE_DIR, slug, "index.md")
    if not os.path.exists(path):
        print(f"NOT FOUND: {slug}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = COVER_PATTERN.sub('image = "cover.png"\n', content)

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"FIXED: {slug}")
        fixed += 1
    else:
        print(f"NO CHANGE: {slug}")

print(f"\nDONE: {fixed} files fixed")

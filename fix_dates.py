"""
全27記事の日付を整理するスクリプト
- 4/30スタート、基本1日1記事
- 自然なギャップ（約週1回1日空き）
"""
import re

BASE = r"C:\Users\user\myblog\content\posts"

# slug: 新しい日付
schedule = [
    ("first-post",                    "2026-04-30T10:00:00+09:00"),
    ("ai-tools-i-use",                "2026-05-01T10:00:00+09:00"),
    ("chatgpt-start-guide",           "2026-05-02T10:00:00+09:00"),
    # 5/3 空き
    ("chatgpt-prompt-writing-guide",  "2026-05-04T10:00:00+09:00"),
    ("chatgpt-vs-claude",             "2026-05-05T10:00:00+09:00"),
    ("chatgpt-english-study",         "2026-05-06T10:00:00+09:00"),
    ("gemini-image-guide",            "2026-05-07T10:00:00+09:00"),
    # 5/8 空き
    ("gemini-beginner-guide",         "2026-05-09T10:00:00+09:00"),
    ("ai-three-tools-comparison-2026","2026-05-10T10:00:00+09:00"),
    ("copilot-guide",                 "2026-05-11T10:00:00+09:00"),
    # 5/12 空き
    ("perplexity-ai-guide",           "2026-05-13T10:00:00+09:00"),
    ("ai-side-job-beginners",         "2026-05-14T10:00:00+09:00"),
    ("free-ai-tools-side-job",        "2026-05-15T10:00:00+09:00"),
    ("crowdworks-first-job",          "2026-05-16T10:00:00+09:00"),
    # 5/17 空き
    ("promptbase-how-to-sell",        "2026-05-18T10:00:00+09:00"),
    ("kdp-publish-experience",        "2026-05-19T10:00:00+09:00"),
    ("kdp-ai-publishing-guide",       "2026-05-20T10:00:00+09:00"),
    ("ai-income-report",              "2026-05-21T10:00:00+09:00"),
    # 5/22 空き
    ("ai-work-efficiency-tips",       "2026-05-23T10:00:00+09:00"),
    ("notion-ai-guide",               "2026-05-24T10:00:00+09:00"),
    ("canva-eyecatch-guide",          "2026-05-25T10:00:00+09:00"),
    ("ai-blog-writing-workflow",      "2026-05-26T10:00:00+09:00"),
    # 5/27 空き
    ("ai-habit-tips",                 "2026-05-28T10:00:00+09:00"),
    ("ai-habits-for-productivity",    "2026-05-29T10:00:00+09:00"),
    ("suno-bgm-youtube",              "2026-05-30T10:00:00+09:00"),
    # 5/31 空き
    ("claude-ai-guide",               "2026-06-01T10:00:00+09:00"),
    ("ai-side-job-2026-trends",       "2026-06-02T10:00:00+09:00"),
]

for slug, new_date in schedule:
    path = rf"{BASE}\{slug}\index.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    updated = re.sub(
        r"date = '[^']+?'",
        f"date = '{new_date}'",
        content
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"{new_date[:10]}  {slug}")

print("\nDone!")

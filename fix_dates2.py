import re
import os

BASE = r"C:\Users\user\myblog\content\posts"

# 37記事を2026-04-02〜2026-05-14に配置
# 自然な空き日を含む
schedule = [
    # 4/2〜4/6 (5記事、4/7は空き)
    ("first-post",                    "2026-04-02T10:00:00+09:00"),
    ("ai-tools-i-use",                "2026-04-03T10:00:00+09:00"),
    ("chatgpt-start-guide",           "2026-04-04T10:00:00+09:00"),
    ("chatgpt-prompt-writing-guide",  "2026-04-05T10:00:00+09:00"),
    ("ai-blog-writing-workflow",      "2026-04-06T10:00:00+09:00"),
    # 4/8〜4/12 (5記事、4/13は空き)
    ("ai-side-job-beginners",         "2026-04-08T10:00:00+09:00"),
    ("claude-ai-guide",               "2026-04-09T10:00:00+09:00"),
    ("ai-side-job-2026-trends",       "2026-04-10T10:00:00+09:00"),
    ("ai-habit-tips",                 "2026-04-11T10:00:00+09:00"),
    ("ai-habits-for-productivity",    "2026-04-12T10:00:00+09:00"),
    # 4/14〜4/19 (6記事、4/20は空き)
    ("ai-income-report",              "2026-04-14T10:00:00+09:00"),
    ("ai-three-tools-comparison-2026","2026-04-15T10:00:00+09:00"),
    ("ai-work-efficiency-tips",       "2026-04-16T10:00:00+09:00"),
    ("canva-eyecatch-guide",          "2026-04-17T10:00:00+09:00"),
    ("chatgpt-english-study",         "2026-04-18T10:00:00+09:00"),
    ("chatgpt-vs-claude",             "2026-04-19T10:00:00+09:00"),
    # 4/21〜4/25 (5記事、4/26は空き)
    ("copilot-guide",                 "2026-04-21T10:00:00+09:00"),
    ("crowdworks-first-job",          "2026-04-22T10:00:00+09:00"),
    ("free-ai-tools-side-job",        "2026-04-23T10:00:00+09:00"),
    ("gemini-beginner-guide",         "2026-04-24T10:00:00+09:00"),
    ("gemini-image-guide",            "2026-04-25T10:00:00+09:00"),
    # 4/27〜4/30 (4記事)
    ("kdp-ai-publishing-guide",       "2026-04-27T10:00:00+09:00"),
    ("kdp-publish-experience",        "2026-04-28T10:00:00+09:00"),
    ("notion-ai-guide",               "2026-04-29T10:00:00+09:00"),
    ("perplexity-ai-guide",           "2026-04-30T10:00:00+09:00"),
    # 5/1〜5/4 (4記事、5/5は空き)
    ("promptbase-how-to-sell",        "2026-05-01T10:00:00+09:00"),
    ("suno-bgm-youtube",              "2026-05-02T10:00:00+09:00"),
    ("grok-ai-guide",                 "2026-05-03T10:00:00+09:00"),
    ("chatgpt-voice-mode",            "2026-05-04T10:00:00+09:00"),
    # 5/6〜5/10 (5記事、5/11は空き)
    ("midjourney-beginner-guide",     "2026-05-06T10:00:00+09:00"),
    ("ai-side-job-tax",               "2026-05-07T10:00:00+09:00"),
    ("claude-projects-guide",         "2026-05-08T10:00:00+09:00"),
    ("ai-prompt-management",          "2026-05-09T10:00:00+09:00"),
    ("ai-resume-writing",             "2026-05-10T10:00:00+09:00"),
    # 5/12〜5/14 (3記事)
    ("ai-reading-summary",            "2026-05-12T10:00:00+09:00"),
    ("stable-diffusion-guide",        "2026-05-13T10:00:00+09:00"),
    ("ai-sns-writing",                "2026-05-14T10:00:00+09:00"),
]

updated = 0
for slug, new_date in schedule:
    path = os.path.join(BASE, slug, "index.md")
    if not os.path.exists(path):
        print(f"NOT FOUND: {slug}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"date = '[^']*'",
        f"date = '{new_date}'",
        content,
        count=1
    )

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"OK: {slug} → {new_date[:10]}")
        updated += 1
    else:
        print(f"SKIP: {slug}")

print(f"\n完了: {updated}件更新")

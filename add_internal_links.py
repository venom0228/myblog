import os

BASE = r"C:\Users\user\myblog\content\posts"

# 全記事のタイトルマップ
titles = {
    "first-post":                   "AIツールを使い始めて半年で変わったこと",
    "ai-tools-i-use":               "私が毎日使っているAIツール3選【40代在宅ワーカーの本音レビュー】",
    "chatgpt-start-guide":          "ChatGPTの始め方【登録から使い方まで5分で解説】",
    "chatgpt-prompt-writing-guide": "ChatGPTプロンプトの書き方入門【初心者が最初に覚える5つのコツ】",
    "ai-blog-writing-workflow":     "AIとブログを組み合わせる方法【記事作成を時短する私のワークフロー】",
    "ai-side-job-beginners":        "AIを使った副業、初心者におすすめの3つの始め方",
    "claude-ai-guide":              "Claudeとは？ChatGPTと何が違うのか使い比べてわかったこと",
    "ai-side-job-2026-trends":      "2026年に注目のAI副業5選【今始めると有利な理由】",
    "ai-habit-tips":                "AIを毎日使い続けるための習慣化のコツ【3ステップで定着させる方法】",
    "ai-habits-for-productivity":   "AIツールを使いこなすために続けている3つの習慣",
    "ai-income-report":             "AI副業の収支を公開。始めて2ヶ月でどのくらい稼げたか",
    "ai-three-tools-comparison-2026":"ChatGPT・Claude・Gemini どれを使えばいい？2026年版・用途別比較",
    "ai-work-efficiency-tips":      "仕事でAIを使うと何が変わる？実際に試してわかった10の効果",
    "canva-eyecatch-guide":         "Canvaで無料！ブログのアイキャッチ画像を10分で作る方法",
    "chatgpt-english-study":        "ChatGPTで英語学習が変わった。毎日続けられる3つの練習法",
    "chatgpt-vs-claude":            "ChatGPTとClaudeを使い比べてみた【40代が語る正直な感想】",
    "copilot-guide":                "Microsoft CopilotはChatGPTの代わりになる？実際に使い比べた感想",
    "crowdworks-first-job":         "クラウドワークスで最初の仕事を取るまでにやったこと",
    "free-ai-tools-side-job":       "無料AIツールだけで副業を始める方法【初期費用ゼロでスタート】",
    "gemini-beginner-guide":        "Geminiの使い方と活用例【GoogleアカウントだけでOK・初心者向け】",
    "gemini-image-guide":           "Geminiの画像生成が無料で使える！使い方と活用例を解説",
    "kdp-ai-publishing-guide":      "AIでKindle本を作る手順を全部公開【KDP副業の始め方】",
    "kdp-publish-experience":       "AIで写真集を作ってKDPで出版してみた話【完全レポート】",
    "notion-ai-guide":              "NotionAIを使い始めたら、メモの質が上がった話",
    "perplexity-ai-guide":          "Perplexity AIを使ったら調べ物の速さが変わった【ChatGPTとの違いも解説】",
    "promptbase-how-to-sell":       "PromptBaseでプロンプトを売る方法【初心者向け完全ガイド】",
    "suno-bgm-youtube":             "SunoでYouTube作業用BGMを作ってみた。スーファミ風ローファイが思いのほかよかった",
}

# 各記事の関連記事マッピング（スラッグ: [関連スラッグのリスト]）
related = {
    "first-post": [
        "ai-tools-i-use",
        "chatgpt-start-guide",
        "ai-blog-writing-workflow",
    ],
    "ai-tools-i-use": [
        "chatgpt-start-guide",
        "claude-ai-guide",
        "ai-three-tools-comparison-2026",
    ],
    "chatgpt-start-guide": [
        "chatgpt-prompt-writing-guide",
        "claude-ai-guide",
        "ai-tools-i-use",
    ],
    "chatgpt-prompt-writing-guide": [
        "chatgpt-start-guide",
        "ai-blog-writing-workflow",
        "chatgpt-english-study",
    ],
    "ai-blog-writing-workflow": [
        "chatgpt-prompt-writing-guide",
        "canva-eyecatch-guide",
        "ai-habit-tips",
    ],
    "ai-side-job-beginners": [
        "ai-side-job-2026-trends",
        "free-ai-tools-side-job",
        "promptbase-how-to-sell",
    ],
    "claude-ai-guide": [
        "chatgpt-vs-claude",
        "ai-three-tools-comparison-2026",
        "chatgpt-start-guide",
    ],
    "ai-side-job-2026-trends": [
        "ai-side-job-beginners",
        "free-ai-tools-side-job",
        "kdp-ai-publishing-guide",
    ],
    "ai-habit-tips": [
        "ai-habits-for-productivity",
        "ai-work-efficiency-tips",
        "ai-tools-i-use",
    ],
    "ai-habits-for-productivity": [
        "ai-habit-tips",
        "ai-work-efficiency-tips",
        "notion-ai-guide",
    ],
    "ai-income-report": [
        "ai-side-job-beginners",
        "ai-blog-writing-workflow",
        "kdp-publish-experience",
    ],
    "ai-three-tools-comparison-2026": [
        "chatgpt-vs-claude",
        "claude-ai-guide",
        "gemini-beginner-guide",
    ],
    "ai-work-efficiency-tips": [
        "ai-habits-for-productivity",
        "notion-ai-guide",
        "ai-tools-i-use",
    ],
    "canva-eyecatch-guide": [
        "gemini-image-guide",
        "ai-blog-writing-workflow",
        "suno-bgm-youtube",
    ],
    "chatgpt-english-study": [
        "chatgpt-start-guide",
        "chatgpt-prompt-writing-guide",
        "ai-habits-for-productivity",
    ],
    "chatgpt-vs-claude": [
        "claude-ai-guide",
        "ai-three-tools-comparison-2026",
        "gemini-beginner-guide",
    ],
    "copilot-guide": [
        "ai-three-tools-comparison-2026",
        "chatgpt-vs-claude",
        "ai-work-efficiency-tips",
    ],
    "crowdworks-first-job": [
        "ai-side-job-beginners",
        "free-ai-tools-side-job",
        "ai-income-report",
    ],
    "free-ai-tools-side-job": [
        "ai-side-job-beginners",
        "ai-side-job-2026-trends",
        "crowdworks-first-job",
    ],
    "gemini-beginner-guide": [
        "gemini-image-guide",
        "ai-three-tools-comparison-2026",
        "chatgpt-vs-claude",
    ],
    "gemini-image-guide": [
        "gemini-beginner-guide",
        "canva-eyecatch-guide",
        "ai-blog-writing-workflow",
    ],
    "kdp-ai-publishing-guide": [
        "kdp-publish-experience",
        "ai-side-job-2026-trends",
        "free-ai-tools-side-job",
    ],
    "kdp-publish-experience": [
        "kdp-ai-publishing-guide",
        "ai-income-report",
        "ai-side-job-beginners",
    ],
    "notion-ai-guide": [
        "ai-work-efficiency-tips",
        "ai-habits-for-productivity",
        "copilot-guide",
    ],
    "perplexity-ai-guide": [
        "ai-three-tools-comparison-2026",
        "chatgpt-start-guide",
        "gemini-beginner-guide",
    ],
    "promptbase-how-to-sell": [
        "ai-side-job-beginners",
        "free-ai-tools-side-job",
        "ai-side-job-2026-trends",
    ],
    "suno-bgm-youtube": [
        "canva-eyecatch-guide",
        "gemini-image-guide",
        "ai-blog-writing-workflow",
    ],
}

def make_related_section(slug_list):
    lines = ["\n---\n", "\n## 関連記事\n\n"]
    for s in slug_list:
        title = titles[s]
        lines.append(f"- [{title}](/posts/{s}/)\n")
    return "".join(lines)

updated = 0
skipped = 0

for slug, links in related.items():
    path = os.path.join(BASE, slug, "index.md")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        skipped += 1
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # すでに関連記事セクションがある場合はスキップ
    if "## 関連記事" in content:
        print(f"SKIP (already has links): {slug}")
        skipped += 1
        continue

    section = make_related_section(links)
    new_content = content.rstrip() + "\n" + section

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"OK: {slug}")
    updated += 1

print(f"\n完了: {updated}件更新, {skipped}件スキップ")

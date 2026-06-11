import os

BASE = r"C:\Users\user\myblog\content\posts"

fixed = 0
clean = 0

for slug in os.listdir(BASE):
    path = os.path.join(BASE, slug, "index.md")
    if not os.path.exists(path):
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # フロントマターの終わり（2つ目の +++）を探す
    parts = content.split("+++", 2)
    if len(parts) < 3:
        print(f"SKIP (no front matter): {slug}")
        continue

    front = parts[1]       # フロントマター本文
    body = parts[2]        # 記事本文

    # 記事本文の先頭に image = "cover.png" があれば削除
    # 改行 + image行 の形で現れる
    cleaned_body = body
    for pattern in ['image = "cover.png"\n\n', "image = 'cover.png'\n\n",
                    'image = "cover.png"\n', "image = 'cover.png'\n"]:
        if cleaned_body.startswith("\n" + pattern):
            cleaned_body = "\n" + cleaned_body[len("\n" + pattern):]
            break
        if cleaned_body.startswith(pattern):
            cleaned_body = cleaned_body[len(pattern):]
            break

    if cleaned_body != body:
        new_content = "+++" + front + "+++" + cleaned_body
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"FIXED: {slug}")
        fixed += 1
    else:
        clean += 1

print(f"\n完了: {fixed}件修正, {clean}件問題なし")

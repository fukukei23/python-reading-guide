# 20. ファイル入出力（open, read, write）

## ざっくり言うと
プログラムからファイルを読み込んだり、書き込んだりする方法です。設定ファイルの読み込みや、ログの保存などで使います。

## コード例

### 例1：注文ログの保存と読み込み
```python
# ファイルに書き込む（w = write）
with open("order_log.txt", "w", encoding="utf-8") as f:
    f.write("2024-01-15,田中,りんご,150\n")
    f.write("2024-01-15,佐藤,みかん,120\n")
    f.write("2024-01-16,鈴木,牛乳,200\n")

# ファイルから読み込む（r = read）
with open("order_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        date, name, item, price = parts
        print(f"{name}さんが{item}を¥{price}で購入")
```

### 例2：JSON設定ファイルの読み書き
```python
import json

# 設定を保存する
config = {
    "bot_name": "お買い物アシスタント",
    "language": "ja",
    "max_retry": 3
}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# 設定を読み込む
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)
    print(f"ボット名: {loaded_config['bot_name']}")
```

## 読み方ガイド
```python
with open("file.txt", "w", encoding="utf-8") as f:
#         ↑ファイル名   ↑モード    ↑文字コード     ↑変数名
#   モード: "r" = 読み込み, "w" = 書き込み, "a" = 追記

    f.write("テキスト")     # ファイルに1行書き込む
    content = f.read()      # ファイル全体を文字列として読み込む
    lines = f.readlines()   # 1行ずつリストとして読み込む
```
- `"r"` = 読み込みモード（デフォルト）
- `"w"` = 書き込みモード（ファイルがあれば上書き）
- `"a"` = 追記モード（既存の内容の後ろに追加）
- `encoding="utf-8"` = 日本語を扱うときのおまじない

## よくあるパターン

**パターン1：CSVファイルの読み込み**
```python
import csv

with open("products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: ¥{row['price']}")
```

**パターン2：ログファイルへの追記**
```python
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
```

**パターン3：Pathlibを使ったモダンな書き方**
```python
from pathlib import Path

config_path = Path("config.json")
if config_path.exists():
    content = config_path.read_text(encoding="utf-8")
```

## 確認問題

**問1** 以下のコードで、ファイルに何が書き込まれるか説明してください。
```python
with open("memo.txt", "w", encoding="utf-8") as f:
    f.write(" groceries:\n")
    f.write("  - 牛乳\n")
    f.write("  - パン\n")
```

**問2** `"w"` モードと `"a"` モードの違いを説明してください。

**問3** 以下のコードを実行したとき、何が表示されるか答えてください。（例1の書き込みを実行した前提で）
```python
with open("order_log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"{len(lines)}行")
    print(lines[0].strip())
```

---
→ 前: [19. 文字列操作（string operations）](19_string_operations.md)
→ 次: [セクション2: 実践的な読み方](../02_practice/21_reading_patterns.md)

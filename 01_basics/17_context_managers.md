# 17. コンテキストマネージャ（with文）

## ざっくり言うと
「使い始め」と「使い終わり」を自動で管理する仕組みです。電気をつけて部屋に入り、出るときに消すのを自動でやってくれるスイッチのようなものです。

## コード例

### 例1：ファイルの読み書き
```python
with open("orders.csv", "w") as f:
    f.write("商品,金額\n")
    f.write("りんご,150\n")
    f.write("みかん,120\n")
# ここで自動的にファイルが閉じられる

with open("orders.csv", "r") as f:
    content = f.read()
    print(content)
```

### 例2：データベースの接続管理
```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products")
    for row in cursor.fetchall():
        print(f"{row[0]}: ¥{row[1]}")
# ここで自動的にデータベース接続が閉じられる
```

## 読み方ガイド
```python
with open("orders.csv", "w") as f:    # ファイルを開いて、fという名前で使う
    f.write("商品,金額\n")            # ファイルに書き込む
# ↑インデントが戻った時点で自動的に閉じる
```
- `with` = 「このブロックの間だけリソースを使う」という宣言
- `as f` = 開いたファイルを `f` という名前で使う
- インデントを抜けると自動的に後処理（ファイルを閉じる等）が実行される

## よくあるパターン

**パターン1：設定ファイルの読み込み**
```python
import json

with open("config.json", "r") as f:
    config = json.load(f)
    api_key = config["api_key"]
    timeout = config.get("timeout", 30)
```

**パターン2：Lockを使った排他制御（非同期）**
```python
import asyncio

lock = asyncio.Lock()

async def update_inventory(item_id, quantity):
    async with lock:                               # 同時に1つだけ実行できる
        current = await get_stock(item_id)
        await set_stock(item_id, current - quantity)
```

**パターン3：独自のコンテキストマネージャ**
```python
class DatabaseTransaction:
    def __enter__(self):
        self.conn = sqlite3.connect("shop.db")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()       # エラーがなければ保存
        else:
            self.conn.rollback()     # エラーなら元に戻す
        self.conn.close()
```

## 確認問題

**問1** 以下のコードで、インデントを抜けた後はどうなるか説明してください。
```python
with open("log.txt", "w") as f:
    f.write("アクセスログ: 12:00")
```

**問2** `with` 文を使わずにファイルを開いた場合、何を自分でやる必要があるか説明してください。

**問3** 例3の `DatabaseTransaction` で、エラーが起きたときはどうなるか説明してください。

---
→ 前: [16. デコレータ（decorator）](16_decorators.md)
→ 次: [18. 演算子（operators）](18_operators.md)

# 14. 非同期（async/await）

## ざっくり言うと
「待っている間に別の作業をする」仕組みです。レストランで料理を注文したあと、料理が来るまでスマホを見るのと同じです。AIの応答を待つ間に別の処理を進められます。

## コード例

### 例1：LINEボットで複数のAIに同時に問い合わせ
```python
import asyncio

async def ask_ai(bot_name, question):
    print(f"{bot_name}に質問中...")
    await asyncio.sleep(2)             # AIの応答を2秒待つ（疑似的な待ち時間）
    return f"{bot_name}: {question}の回答です"

async def main():
    results = await asyncio.gather(     # 3つのAIに同時に質問する
        ask_ai("ChatGPT", "天気"),
        ask_ai("Claude", "天気"),
        ask_ai("Gemini", "天気"),
    )
    for result in results:
        print(result)

asyncio.run(main())
```

### 例2：複数のAPIからデータを取得
```python
async def fetch_product(product_id):
    print(f"商品{product_id}を取得中...")
    await asyncio.sleep(1)
    return {"id": product_id, "name": f"商品{product_id}"}

async def fetch_all_products():
    products = await asyncio.gather(
        fetch_product("A001"),
        fetch_product("A002"),
        fetch_product("A003"),
    )
    return products
```

## 読み方ガイド
```python
async def ask_ai(bot_name, question):   # async = この関数は非同期（待ち時間あり）
    print(f"{bot_name}に質問中...")
    await asyncio.sleep(2)              # await = ここで結果を待つ（待ってる間に別の作業へ）
    return f"{bot_name}の回答"
```
- `async def` = 「この関数は待ち時間があるよ」という宣言
- `await` = 「ここで結果を待つよ」という合図。待っている間に別の処理が進む
- `asyncio.gather()` = 複数の非同期処理を同時に実行する
- `asyncio.run()` = 非同期プログラムを起動する

## よくあるパターン

**パターン1：外部APIの呼び出し（httpxを使う例）**
```python
async def send_line_message(user_id, text):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=message_data)
    return response.status_code
```

**パターン2：データベースへの非同期アクセス**
```python
async def get_user(user_id):
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT * FROM users WHERE id = $1", user_id
        )
    return row
```

## 確認問題

**問1** 以下のコードで `await asyncio.sleep(3)` は何を意味しているか説明してください。
```python
async def check_inventory(item_id):
    await asyncio.sleep(3)
    return {"item_id": item_id, "stock": 10}
```

**問2** `asyncio.gather()` を使うメリットは何か、例1をもとに説明してください。

**問3** 以下のコードの `async` と `await` それぞれの役割を説明してください。
```python
async def notify(user_id, message):
    await send_push_notification(user_id, message)
    print("通知完了")
```

---
→ 前: [13. エラー処理（try/except）](13_try_except.md)
→ 次: [15. 型ヒント（type hint）](15_type_hints.md)

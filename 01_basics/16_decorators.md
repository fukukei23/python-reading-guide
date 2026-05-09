# 16. デコレータ（decorator） — @マーク

## ざっくり言うと
関数に「追加機能」をつける仕組みです。スマホのケースをつけるようなもので、元の関数を変えずに機能を追加できます。

## コード例

### 例1：実行時間を計測するデコレータ
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.2f}秒")
        return result
    return wrapper

@timer
def process_orders(orders):
    total = sum(order["price"] for order in orders)
    return total

process_orders([{"price": 500}, {"price": 300}])
```

### 例2：ログインチェックのデコレータ
```python
def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("ログインが必要です")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_order_history(user):
    print(f"{user['name']}さんの注文履歴を表示")

view_order_history({"name": "田中", "is_logged_in": True})
view_order_history({"name": "佐藤", "is_logged_in": False})
```

## 読み方ガイド
```python
@timer                              # この関数にtimer機能を追加する
def process_orders(orders):         # 元の関数
    ...

# ↑は実質的に以下と同じ:
# process_orders = timer(process_orders)
```
- `@timer` = 「この関数にtimerという追加機能をつけて」という宣言
- `@` の下にある関数が対象
- デコレータ自体は「関数を受け取って関数を返す関数」です

## よくあるパターン

**パターン1：Flaskのルーティング（Webフレームワーク）**
```python
@app.route("/api/products")
def get_products():
    return {"products": [...]}
```

**パターン2：FastAPIのエンドポイント**
```python
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"id": user_id, "name": "田中"}
```

**パターン3：標準ライブラリの便利デコレータ**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation(n):
    return sum(range(n))
```

## 確認問題

**問1** 例2のコードで、`view_order_history({"name": "佐藤", "is_logged_in": False})` を実行したとき、何が表示されるか答えてください。

**問2** `@timer` がついている関数を実行すると、通常の実行に加えて何が起きるか説明してください。

**問3** 以下のコードの `@app.route("/api/orders")` は何を意味しているか説明してください。
```python
@app.route("/api/orders")
def list_orders():
    return {"orders": []}
```

---
→ 前: [15. 型ヒント（type hint）](15_type_hints.md)
→ 次: [17. コンテキストマネージャ（with文）](17_context_managers.md)

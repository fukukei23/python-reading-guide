# 15. 型ヒント（type hint）

## ざっくり言うと
変数や関数に「このデータは文字です」「この関数は数値を返します」という注釈をつける仕組みです。名前にふりがなをつけるようなもので、コードを読みやすくします。

## コード例

### 例1：ECサイトの関数に型ヒントをつける
```python
def calculate_total(price: int, quantity: int) -> int:
    """合計金額を計算する"""
    return price * quantity

def format_price(amount: int) -> str:
    """金額を表示用にフォーマットする"""
    return f"¥{amount:,}"

total = calculate_total(1500, 3)
print(format_price(total))
```

### 例2：LINEボットのメッセージ処理
```python
from typing import Optional

def find_user(user_id: str) -> Optional[dict]:
    """ユーザーを検索する。見つからなければNoneを返す"""
    users = {"U001": {"name": "田中"}, "U002": {"name": "佐藤"}}
    return users.get(user_id)

def send_reply(reply_token: str, messages: list[str]) -> bool:
    """LINEに返信を送る"""
    print(f"送信: {messages}")
    return True
```

## 読み方ガイド
```python
def calculate_total(price: int, quantity: int) -> int:
#                        ↑int型     ↑int型      ↑戻り値はint型
```
- `price: int` = 「priceという変数は整数（int）です」という注釈
- `-> int` = 「この関数は整数（int）を返します」という注釈
- `Optional[dict]` = 「dictかNoneのどちらか」という意味
- `list[str]` = 「文字列のリスト」という意味

## よくあるパターン

**パターン1：辞書の型を定義する**
```python
from typing import TypedDict

class Product(TypedDict):
    id: str
    name: str
    price: int
    in_stock: bool
```

**パターン2：Union型（複数の型のどれか）**
```python
from typing import Union

def process_input(data: Union[str, int]) -> str:
    if isinstance(data, int):
        return str(data)
    return data
```

**パターン3：モダンな書き方（Python 3.10以降）**
```python
def find_user(user_id: str) -> dict | None:   # Optionalの代わり
def process(data: str | int) -> str:           # Unionの代わり
```

## 確認問題

**問1** 以下の関数の型ヒントを読んで、この関数は何を受け取り何を返すか説明してください。
```python
def get_product_name(product_id: str) -> str:
    products = {"A001": "りんご", "A002": "みかん"}
    return products[product_id]
```

**問2** `Optional[dict]` はどういう意味か、自分の言葉で説明してください。

**問3** 以下のコードの `-> bool` は何を表しているか答えてください。
```python
def is_in_stock(product_id: str) -> bool:
    stock = {"A001": 5, "A002": 0}
    return stock.get(product_id, 0) > 0
```

---
→ 前: [14. 非同期（async/await）](14_async_await.md)
→ 次: [16. デコレータ（decorator）](16_decorators.md)

# 2. 関数（function）

## ざっくり言くと
関数は「ひとまとまりの作業をレシピにする」仕組みです。レシピの名前を呼ぶだけで、中身の作業が実行されます。

## コード例

### 例1：基本的な関数
```python
def say_hello():
    print("こんにちは！")

say_hello()
```

### 例2：計算をまとめる
```python
def calc_tax_price(price):
    tax = price * 0.10
    return price + tax

total = calc_tax_price(1000)
```

### 例3：実務例（予約チェック）
```python
# reserve-optimizer 風
def check_capacity(current_count, max_capacity):
    if current_count >= max_capacity:
        return "満席です"
    return "予約可能です"

result = check_capacity(48, 50)
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `def say_hello():` | say_hello という名前のレシピを定義する |
| `print("こんにちは！")` | （インデントされた行は）レシピの中身 |
| `say_hello()` | say_hello のレシピを実行する |
| `return price + tax` | 計算結果を「呼び出し元」に返す |

- `def` = define（定義する）の略
- 関数名のあとに `()` を付けて呼び出す
- `return` で結果を返す（return がなければ何も返さない）

## よくあるパターン

**パターン1：画面に表示するだけ**
```python
def show_banner():
    print("=" * 30)
    print("  NexusCore Shop")
    print("=" * 30)
```

**パターン2：条件によって違う結果を返す**
```python
# atelier-kyo-manager 風
def get_shipping_fee(area):
    if area == "関東":
        return 500
    return 1000
```

**パターン3：何かを変換して返す**
```python
def format_price(amount):
    return str(amount) + "円"
```

## 確認問題

**問1** 以下のコードを実行すると、何が表示されますか？
```python
def greet():
    print("おはよう！")
    print("今日もよろしく！")

greet()
```

**問2** 以下の `result` には何が入りますか？
```python
def double(n):
    return n * 2

result = double(5)
```

**問3** 以下の関数は `check(3)` として呼び出したとき、何を返しますか？
```python
def check(count):
    if count > 5:
        return "多い"
    return "少ない"
```

---
→ 次: [03. 引数と戻り値（parameter/return）](03_parameters.md)

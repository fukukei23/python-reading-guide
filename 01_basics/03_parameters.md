# 3. 引数と戻り値（parameter / return）

## ざっくり言うと
引数（ひきすう）は「関数に渡す材料」、戻り値は「関数から戻ってくる結果」です。レシピに材料を渡して、完成品を受け取るイメージ。

## コード例

### 例1：引数1つ、戻り値あり
```python
def add_tax(price):
    return int(price * 1.10)

total = add_tax(500)
```

### 例2：引数2つ
```python
def make_message(name, time):
    return name + "さん、" + time + "の予約を受け付けました"

msg = make_message("佐藤", "14:00")
```

### 例3：実務例（在庫チェック）
```python
# NexusCore 風
def check_stock(item_name, quantity, limit):
    if quantity > limit:
        return item_name + "は発注が必要です"
    return item_name + "は在庫十分です"

result = check_stock("Tシャツ", 5, 10)
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `def add_tax(price):` | price という材料を受け取る関数 |
| `return int(price * 1.10)` | price × 1.10 を整数にして返す |
| `total = add_tax(500)` | 500 を材料として渡し、結果を total に受け取る |
| `msg = make_message("佐藤", "14:00")` | 2つの材料（名前と時間）を渡す |

- 関数名の `()` の中に書くのが引数
- 呼び出し側の `()` の中に材料を書く
- `return` の右側にあるものが戻り値

## よくあるパターン

**パターン1：デフォルト値（材料を省略できる）**
```python
def connect_database(host="localhost"):
    return host + "に接続しました"

msg1 = connect_database()              # "localhostに接続しました"
msg2 = connect_database("192.168.1.1") # "192.168.1.1に接続しました"
```

**パターン2：戻り値をそのまま使う**
```python
# atelier-kyo-manager 風
if check_availability("2025-04-01"):
    print("この日は空いています")
```

**パターン3：複数の情報を返す**
```python
def get_user_info(user_id):
    name = "山田"
    age = 28
    return name, age

user_name, user_age = get_user_info(1)
```

## 確認問題

**問1** 以下のコードで `result` には何が入りますか？
```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
```

**問2** 以下の関数を `greet("鈴木")` で呼び出すと、何が返りますか？
```python
def greet(name):
    greeting = name + "さん、いらっしゃい！"
    return greeting
```

**問3** 以下の2つの呼び出しで、それぞれ何が返りますか？
```python
def shipping_cost(region, weight):
    if region == "海外":
        return weight * 500
    return weight * 100

a = shipping_cost("国内", 3)
b = shipping_cost("海外", 3)
```

---
→ 次: [04. 条件分岐（if/else）](04_conditionals.md)

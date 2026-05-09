# 8. 文字列と数値（string / number）

## ざっくり言うと
文字列は「文字のまとまり」、数値は「計算できる数字」です。見た目は似ていても、コンピュータにとっては別のものです。

## コード例

### 例1：文字列の操作
```python
name = "NexusCore"
print(name.lower())         # 小文字にする
print(len(name))            # 文字数を数える
print(name + " Shop")       # つなげる
```

### 例2：数値の計算
```python
price = 1500
count = 3
total = price * count       # 掛け算
discount = total * 0.1      # 1割引
final = total - discount
```

### 例3：実務例（メッセージ組み立て）
```python
# atelier-kyo-manager 風
customer_name = "田中様"
reserve_date = "4月15日"
message = f"{customer_name}、{reserve_date}のご予約を確認しました。"
print(message)
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `"NexusCore"` | `" "` で囲むと文字列になる |
| `name.lower()` | name を小文字に変換する |
| `len(name)` | name の文字数を返す |
| `price * count` | 数値同士の掛け算 |
| `f"{customer_name}、..."` | f文字列。`{ }` の中に変数を埋め込める |

- 文字列 = `" "` で囲む。計算はできない
- 数値 = 囲まない。計算できる
- `f"..."` の中に `{変数名}` を書くと、値が埋め込まれる

## よくあるパターン

**パターン1：型の変換**
```python
age_text = "25"
age_number = int(age_text)       # 文字列 → 数値
age_text2 = str(age_number)      # 数値 → 文字列
```

**パターン2：文字列の一部を取り出す**
```python
# NexusCore 風
product_code = "ITEM-SHOE-001"
category = product_code[5:9]     # "SHOE"
```

**パターン3：文字列の分割と結合**
```python
# reserve-optimizer 風
date_str = "2025-04-15"
parts = date_str.split("-")      # ["2025", "04", "15"]
year = parts[0]
formatted = "/".join(parts)      # "2025/04/15"
```

## 確認問題

**問1** 以下のコードは何を表示しますか？
```python
text = "Hello Python"
print(len(text))
print(text.upper())
```

**問2** 以下のコードで `result` に入る値は何ですか？
```python
price = 2000
tax = 200
result = f"税込み価格: {price + tax}円"
```

**問3** 以下のコードは何を表示しますか？
```python
date = "2025-12-25"
parts = date.split("-")
print(parts[1])
```

---
→ 次: [09. 真偽値とNone（boolean/null）](09_boolean_none.md)

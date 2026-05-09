# 1. 変数（variable）

## ざっくり言うと
変数は「データを入れる箱」です。箱に名前を付けて、あとでその名前で中身を取り出せます。

## コード例

### 例1：基本的な代入
```python
shop_name = "NexusCore"
visitor_count = 150
```

### 例2：計算結果を入れる
```python
price = 1980
tax_rate = 0.10
total = price * (1 + tax_rate)
```

### 例3：実務例（LINEbot設定）
```python
# atelier-kyo-manager より
channel_secret = "your_channel_secret"
channel_access_token = "your_access_token"
bot_reply_message = "ご予約を受け付けました！"
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `shop_name = "NexusCore"` | shop_name という箱に "NexusCore" という文字を入れる |
| `visitor_count = 150` | visitor_count という箱に 150 という数字を入れる |
| `total = price * (1 + tax_rate)` | price × (1 + tax_rate) を計算して、total という箱に入れる |

- `=` は「等しい」ではなく「右辺を左の箱に入れる」と読む
- 箱の名前（変数名）は英語で付けるのがルール
- 文字は `"` で囲む、数字は囲まない

## よくあるパターン

**パターン1：上書き**
```python
status = "受注中"
status = "発送済み"   # 箱の中身が新しい値に変わる
```

**パターン2：自己更新**
```python
score = 0
score = score + 10    # 今のscoreに10足して、もう一度scoreに入れる
```

**パターン3：複数の変数で設定を管理**
```python
# reserve-optimizer より
max_capacity = 50
booking_deadline = "2025-03-31"
is_open = True
```

## 確認問題

**問1** 以下のコードは何をしていますか？
```python
user_name = "田中さん"
greeting = "こんにちは、" + user_name
```

**問2** 以下のコードの後、`total` はいくつになりますか？
```python
a = 100
b = 200
total = a + b
```

**問3** 以下のコードで、最後に `x` に入っている値は何ですか？
```python
x = 10
x = x + 5
x = x * 2
```

---
→ 次: [02. 関数（function）](02_functions.md)

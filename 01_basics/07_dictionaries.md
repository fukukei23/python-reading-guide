# 7. 辞書（dictionary / object）

## ざっくり言うと
辞書は「名前（キー）で値を引き出せる箱」です。名簿で「田中」のページを開いて電話番号を見つけるようなもの。

## コード例

### 例1：基本的な辞書
```python
user = {
    "name": "山田",
    "age": 25,
    "city": "東京"
}

print(user["name"])
```

### 例2：値の更新と追加
```python
product = {"name": "Tシャツ", "price": 1980}
product["price"] = 1480          # 更新
product["color"] = "青"          # 追加
```

### 例3：実務例（LINEbotメッセージ）
```python
# atelier-kyo-manager 風
message = {
    "type": "text",
    "text": "ご予約が確定しました"
}

reply = {
    "replyToken": "abc123xyz",
    "messages": [message]
}
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `"name": "山田"` | キー "name" に値 "山田" を紐付ける |
| `user["name"]` | user の "name" に対応する値を取り出す |
| `product["price"] = 1480` | "price" の値を 1480 に書き換える |
| `"messages": [message]` | 値にはリストも入れられる |

- `{ }`（中カッコ）で囲む
- `キー: 値` のペアをカンマで並べる
- リストは番号で取り出すが、辞書は「キー（名前）」で取り出す

## よくあるパターン

**パターン1：キーがあるか確認**
```python
# reserve-optimizer 風
config = {"max_users": 50, "timeout": 30}

if "timeout" in config:
    print("タイムアウト設定: " + str(config["timeout"]) + "秒")
```

**パターン2：辞書のリスト（よくある形）**
```python
users = [
    {"name": "田中", "role": "admin"},
    {"name": "佐藤", "role": "member"},
    {"name": "鈴木", "role": "member"}
]

for user in users:
    print(user["name"] + " - " + user["role"])
```

**パターン3：get で安全に取り出す**
```python
settings = {"theme": "dark"}

# キーがなくてもエラーにならない
font = settings.get("font", "メイリオ")
```
- `.get(キー, デフォルト値)` = キーがなければデフォルト値を返す

## 確認問題

**問1** 以下のコードで `x` に入る値は何ですか？
```python
item = {"id": "A001", "name": "コーヒー", "price": 350}
x = item["price"]
```

**問2** 以下のコードの後、`player` の中身はどうなりますか？
```python
player = {"name": "太郎", "score": 100}
player["score"] = 200
player["level"] = 5
```

**問3** 以下のコードは何を表示しますか？
```python
book = {"title": "Python入門", "page": 250}
print(book.get("author", "不明"))
```

---
→ 次: [08. 文字列と数値（string/number）](08_strings_numbers.md)

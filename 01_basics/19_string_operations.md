# 19. 文字列操作（f-string, split, join等）

## ざっくり言うと
文字を組み立てたり、分割したりする方法です。LINEbotのメッセージ作成や、CSVデータの解析などでよく使います。

## コード例

### 例1：注文確認メールの文章作成
```python
order_id = "A001"
customer_name = "田中"
items = ["りんご x2", "みかん x3"]
total = 890

message = f"""
{customer_name}様、ご注文ありがとうございます。

注文番号: {order_id}
商品: {', '.join(items)}
合計: ¥{total:,}

お届け予定: 3日以内
"""
print(message)
```

### 例2：CSVデータの解析
```python
csv_line = "田中,25,東京都,エンジニア"
fields = csv_line.split(",")

name = fields[0]
age = int(fields[1])
location = fields[2]
job = fields[3]

profile = f"{name}さん（{age}歳）-{ location }在住 - {job}"
print(profile)

# 文字列の便利なメソッド
text = "  Hello World  "
print(text.strip())         # 前後の空白を削除: "Hello World"
print(text.lower())         # 小文字に変換: "  hello world  "
print(text.replace("World", "Python"))  # 置換: "  Hello Python  "
```

## 読み方ガイド
```python
f"合計: ¥{total:,}"              # f-string: 変数を文字列に埋め込む
                                  # {total:,} = カンマ区切りで表示（1,000）

", ".join(items)                  # リストの要素を「, 」でつなぐ

csv_line.split(",")               # 文字列を「,」で分割してリストにする

text.strip()                      # 前後の余分な空白を削る
text.replace("A", "B")           # 「A」を「B」に置き換える
```

## よくあるパターン

**パターン1：ゼロ埋め（番号のフォーマット）**
```python
order_num = 42
formatted = f"ORD-{order_num:04d}"   # "ORD-0042"
```

**パターン2：小数点の桁数指定**
```python
rate = 0.12345
print(f"変換率: {rate:.2%}")          # "変換率: 12.35%"
print(f"値: {rate:.3f}")             # "値: 0.123"
```

**パターン3：文字列の検索と判定**
```python
email = "tanaka@example.com"
if "@" in email and email.endswith(".com"):
    print("有効なメールアドレスです")

filename = "report.pdf"
if filename.endswith(".pdf"):
    print("PDFファイルです")
```

## 確認問題

**問1** 以下のコードを実行したとき、何が表示されるか答えてください。
```python
users = ["田中", "佐藤", "鈴木"]
result = "、".join(users)
print(result)
```

**問2** 以下のコードで `formatted` には何が入るか答えてください。
```python
price = 1980
tax = 1.1
total = int(price * tax)
formatted = f"税込: ¥{total:,}"
```

**問3** 以下のコードを実行したとき、何が表示されるか答えてください。
```python
text = "banana,apple,cherry"
fruits = text.split(",")
print(fruits[1])
```

---
→ 前: [18. 演算子（operators）](18_operators.md)
→ 次: [20. ファイル入出力（file I/O）](20_file_io.md)

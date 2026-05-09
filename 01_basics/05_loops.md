# 5. 繰り返し（for / while）

## ざっくり言うと
同じ作業を何度も繰り返す仕組みです。買い物リストの品目を1つずつ確認するようなもの。

## コード例

### 例1：forでリストを1つずつ処理
```python
fruits = ["りんご", "みかん", "バナナ"]

for fruit in fruits:
    print(fruit)
```

### 例2：rangeで回数を指定
```python
for i in range(3):
    print(str(i + 1) + "回目の処理")
```

### 例3：実務例（商品リストの処理）
```python
# NexusCore 風
order_items = ["Tシャツ", "ジーンズ", "スニーカー"]

for item in order_items:
    print("発送準備: " + item)
print("全商品の発送準備完了")
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `for fruit in fruits:` | fruits の中身を1つずつ fruit に入れて繰り返す |
| `print(fruit)` | （繰り返しの中で）fruit を表示する |
| `for i in range(3):` | i を 0, 1, 2 と変えながら3回繰り返す |
| `range(3)` | 0から始まって3つ分の数字（0, 1, 2）を作る |

- `for 変数 in リスト:` の形が基本
- インデントされた部分が繰り返される
- リストの中身が尽きたら繰り返し終了

## よくあるパターン

**パターン1：while（条件が満たされている間繰り返す）**
```python
count = 0
while count < 3:
    print("リトライ中...")
    count = count + 1
```

**パターン2：番号付きで処理**
```python
# atelier-kyo-manager 風
reservations = ["10:00 田中", "11:00 佐藤", "14:00 鈴木"]

for i, res in enumerate(reservations):
    print(str(i + 1) + "件目: " + res)
```
- `enumerate` で番号付きにできる

**パターン3：条件で飛ばす**
```python
# reserve-optimizer 風
scores = [85, 30, 92, 45, 78]

for score in scores:
    if score < 50:
        continue        # 50未満は飛ばす
    print(str(score) + "点: 合格")
```
- `continue` = この回の繰り返しをスキップ
- `break` = 繰り返しを途中で終了

## 確認問題

**問1** 以下のコードは何を表示しますか？
```python
names = ["犬", "猫", "鳥"]
for name in names:
    print("これは" + name + "です")
```

**問2** 以下のコードは何を表示しますか？
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**問3** 以下のwhileループは何回 "hello" を表示しますか？
```python
n = 0
while n < 4:
    print("hello")
    n = n + 1
```

---
→ 次: [06. リスト（list/array）](06_lists.md)

# 4. 条件分岐（if / else）

## ざっくり言うと
「もし〇〇ならA、そうでなければB」という判断の仕組みです。交差点で右折するか左折するか決めるようなもの。

## コード例

### 例1：基本的なif/else
```python
age = 20

if age >= 18:
    print("大人料金です")
else:
    print("子供料金です")
```

### 例2：elif（そうでなくもし）
```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"
```

### 例3：実務例（予約システム）
```python
# reserve-optimizer 風
def get_booking_status(reserved, capacity):
    if reserved >= capacity:
        return "満席"
    elif reserved >= capacity - 3:
        return "残りわずか"
    else:
        return "空席あり"
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `if age >= 18:` | もし age が 18以上なら |
| `print("大人料金です")` | （条件に合うとき）これを実行 |
| `else:` | そうでなければ |
| `elif score >= 70:` | そうでなくもし、score が 70以上なら |

- `if` → `elif` → `else` の順で書く
- 条件の最後に `:`（コロン）を付ける
- 条件に合ったブロックはインデント（字下げ）する
- 上から順にチェックして、最初に合ったものだけ実行

## よくあるパターン

**パターン1：等しいかどうかの判定**
```python
# atelier-kyo-manager 風
status = "paid"

if status == "paid":
    print("支払い済みです")
elif status == "pending":
    print("支払い待ちです")
```
- `==` は「等しい」の意味（`=` は代入なので違う）

**パターン2：否定（〜ではない）**
```python
is_sold_out = False

if not is_sold_out:
    print("まだ買えます")
```

**パターン3：複数の条件を組み合わせる**
```python
# NexusCore 風
if member == True and points >= 100:
    print("会員専用クーポンが使えます")
```
- `and` = 両方とも条件を満たす
- `or` = どちらか一方でも条件を満たす

## 確認問題

**問1** 以下のコードで `result` には何が入りますか？
```python
temperature = 35

if temperature >= 30:
    result = "猛暑日"
elif temperature >= 25:
    result = "真夏日"
else:
    result = "普通の日"
```

**問2** 以下のコードは何を表示しますか？
```python
stock = 0

if stock > 0:
    print("在庫あり")
else:
    print("在庫切れ")
```

**問3** 以下のコードで `message` に入る値は何ですか？
```python
role = "admin"
is_active = True

if role == "admin" and is_active == True:
    message = "管理者メニューを表示"
else:
    message = "権限がありません"
```

---
→ 次: [05. 繰り返し（for/while）](05_loops.md)

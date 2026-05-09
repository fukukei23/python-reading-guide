# 9. 真偽値とNone（boolean / null）

## ざっくり言うと
真偽値（boolean）は「はい / いいえ」の2つだけの値です。Noneは「何も入っていない」ことを表す特別な値です。

## コード例

### 例1：True / False
```python
is_member = True
is_sold_out = False

if is_member:
    print("会員割引が適用されます")
```

### 例2：比較結果は真偽値
```python
age = 20
result = age >= 18       # True
result2 = age == 15      # False
```

### 例3：実務例（初期値としてのNone）
```python
# NexusCore 風
def find_user(user_id):
    if user_id == 1:
        return "田中"
    return None

user = find_user(99)

if user is None:
    print("ユーザーが見つかりません")
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `is_member = True` | is_member は「はい（True）」 |
| `is_sold_out = False` | is_sold_out は「いいえ（False）」 |
| `age >= 18` | age が18以上か？ → True か False になる |
| `return None` | 「何もない」ことを返す |
| `if user is None:` | user が「何もない」状態かチェック |

- `True` = はい（条件を満たす）
- `False` = いいえ（条件を満たさない）
- `None` = データが空っぽ（値が存在しない）
- 大文字小文字に注意：`True` `False` `None`（最初だけ大文字）

## よくあるパターン

**パターン1：not で反転**
```python
# atelier-kyo-manager 風
is_closed = False

if not is_closed:
    print("営業中です")
```

**パターン2：and / or で組み合わせ**
```python
has_coupon = True
is_member = False

if has_coupon or is_member:
    print("割引が使えます")
```

**パターン3：初期値チェック**
```python
# reserve-optimizer 風
selected_plan = None

if selected_plan is None:
    print("プランを選択してください")
else:
    print("選択済み: " + selected_plan)
```

## 確認問題

**問1** 以下のコードで `result` には何が入りますか？
```python
x = 10
result = x > 5
```

**問2** 以下のコードは何を表示しますか？
```python
has_ticket = True
at_venue = False

if has_ticket and at_venue:
    print("入場できます")
else:
    print("入場できません")
```

**問3** 以下のコードは何を表示しますか？
```python
data = None

if data is None:
    data = "デフォルト値"

print(data)
```

---
→ 次: [10. インポート（import）](10_imports.md)

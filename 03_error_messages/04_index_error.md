# 4. IndexError: 範囲外

## ざっくり言うと
リストで**存在しない番号**を指定したときのエラーです。
「その番号には何も入っていません」という意味です。

## エラー例

### 例1: リストの範囲を超えた
```python
>>> fruits = ["りんご", "みかん", "バナナ"]
>>> print(fruits[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

### 例2: 空のリストにアクセス
```python
>>> items = []
>>> print(items[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

### 例3: ループの中で起きる
```python
>>> nums = [10, 20, 30]
>>> for i in range(4):
...     print(nums[i])
...
10
20
30
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
```

## トレースバックの読み方

```
IndexError: list index out of range
                   ↑
    「リストの範囲外です」という意味
```

**ポイント**:
- リストの番号は **0 から始まる**
- 長さ3のリスト: `0, 1, 2` まで使える（`3` はダメ）
- `range(4)` は `0, 1, 2, 3` を生成する（4回）

**確認の仕方**:
```python
fruits = ["りんご", "みかん", "バナナ"]
# 長さ: 3
# 使える番号: 0, 1, 2
# fruits[3] はエラー！（4番目は存在しない）
```

## 対処法

1. **`len()`** で長さを確認する
2. **`for item in list`** を使う（番号を使わない）
3. `range(len(list))` で正しい範囲を指定する
4. リストが**空でないか**確認する

## 確認問題

**問1**: 長さ5のリストで使えるインデックスは？
```python
data = [10, 20, 30, 40, 50]
```

**問2**: 次のコードのエラーを直してください。
```python
nums = [1, 2, 3]
for i in range(4):
    print(nums[i])
```

**問3**: `fruits[3]` がエラーにならないのは、リストに何個以上の要素があるとき？

---
→ 前: [03_key_error.md](03_key_error.md)
→ 次: [05_value_error.md](05_value_error.md)

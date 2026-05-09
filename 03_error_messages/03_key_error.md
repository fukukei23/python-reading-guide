# 3. KeyError: キーが見つからない

## ざっくり言うと
辞書（dict）で**存在しないキー**を指定したときのエラーです。
「そのキー、この辞書にはありません」という意味です。

## エラー例

### 例1: 存在しないキーを指定
```python
>>> user = {"name": "たろう", "age": 25}
>>> print(user["email"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'email'
```

### 例2: キーのスペルミス
```python
>>> config = {"host": "localhost", "port": 8080}
>>> print(config["Post"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Post'
```

### 例3: ネストした辞書で間違えた
```python
>>> data = {"user": {"name": "花子"}}
>>> print(data["user"]["age"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```

## トレースバックの読み方

```
KeyError: 'email'
         ↑
    見つからなかったキー
```

**ポイント**:
- エラーの最後の行に**見つからなかったキー**が表示される
- 大文字・小文字も区別される（`"Post"` ≠ `"port"`）
- ネストの場合は**どの段階で失敗したか**を確認する

## 対処法

1. **`.get()`** を使う（キーがなくてもエラーにならない）
   ```python
   user.get("email", "未設定")  # → "未設定"
   ```
2. **`in`** で存在確認する
   ```python
   if "email" in user:
       print(user["email"])
   ```
3. 辞書の中身を `print(dict.keys())` で確認する

## 確認問題

**問1**: 次のエラーを `.get()` を使って直してください。
```python
data = {"name": "たろう"}
print(data["age"])
```

**問2**: 次のコードはエラーになるか？
```python
d = {"a": 1, "b": 2}
print(d.get("c"))
```

**問3**: KeyError を防ぐ方法を2つ挙げてください。

---
→ 前: [02_type_error.md](02_type_error.md)
→ 次: [04_index_error.md](04_index_error.md)

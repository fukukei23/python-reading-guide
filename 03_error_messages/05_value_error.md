# 5. ValueError: 値が不正

## ざっくり言うと
Pythonが「その値は受け付けられません」と言っているエラーです。
型は合っているけれど、**内容が変**なときに起きます。

## エラー例

### 例1: 数値に変換できない文字列
```python
>>> int("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```

### 例2: リストから削除しようとしたが見つからない
```python
>>> fruits = ["りんご", "みかん"]
>>> fruits.remove("バナナ")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

### 例3: unpackの数が合わない
```python
>>> a, b = [1, 2, 3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

## トレースバックの読み方

```
ValueError: invalid literal for int() with base 10: 'hello'
            ↑                                    ↑
      「無効な値」                         問題の値
```

**ポイント**:
- `int() with base 10` = 「10進数の整数に変換しようとした」
- `invalid literal` = 「この文字列は変換できない」
- `'hello'` という文字列が整数にできない理由が分かる

## 対処法

1. **変換前に確認**する
   ```python
   s = "hello"
   if s.isdigit():
       n = int(s)
   ```
2. **try / except** で囲む
   ```python
   try:
       n = int(user_input)
   except ValueError:
       print("数値を入力してください")
   ```
3. **存在確認**してから `remove` する
   ```python
   if "バナナ" in fruits:
       fruits.remove("バナナ")
   ```

## 確認問題

**問1**: 次のコードは ValueError になるか？
```python
int("42")
```

**問2**: ユーザー入力を安全に整数に変換するコードを書いてください。

**問3**: `ValueError: too many values to unpack (expected 2)` はどういう意味？

---
→ 前: [04_index_error.md](04_index_error.md)
→ 次: [06_attribute_error.md](06_attribute_error.md)

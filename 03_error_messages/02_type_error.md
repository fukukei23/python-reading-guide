# 2. TypeError: 型が合わない

## ざっくり言うと
Pythonが「その組み合わせ、できません」と言っているエラーです。
**文字列と数値**など、種類（型）が違うものを組み合わせようとしたときに起きます。

## エラー例

### 例1: 文字列 + 数値
```python
>>> age = 25
>>> print("年齢は" + age + "歳です")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

### 例2: 関数の引数が足りない
```python
>>> def add(a, b):
...     return a + b
...
>>> add(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'b'
```

### 例3: リストに辞書のメソッドを使った
```python
>>> items = [1, 2, 3]
>>> items.keys()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'keys'
```

## トレースバックの読み方

```
TypeError: can only concatenate str (not "int") to str
         ↑                        ↑
    エラーの種類           詳しい理由
```

**ポイント**:
- `str` = 文字列、`int` = 整数、`float` = 小数
- 「str に int をつなげることはできない」と読む
- `not "int"` の部分が「原因の型」

## 対処法

1. **型を変換**する: `str(25)` や `int("3")`
2. **f-string** を使う: `f"年齢は{age}歳です"`
3. 関数を呼ぶときの**引数の数**を確認する
4. その型に**あるメソッド**を使っているか確認する

## 確認問題

**問1**: 次のエラーを直してください。
```python
x = "10"
y = 5
print(x + y)
```

**問2**: 次のエラーメッセージは何を意味する？
```
TypeError: add() takes 2 positional arguments but 3 were given
```

**問3**: 次のコードをエラーなく動くように直してください。
```python
result = "答えは" + 42
```

---
→ 前: [01_name_error.md](01_name_error.md)
→ 次: [03_key_error.md](03_key_error.md)

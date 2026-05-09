# 1. NameError: 名前が見つからない

## ざっくり言うと
Pythonが「その名前、知りません」と言っているエラーです。
変数や関数を**定義する前に使った**ときによく起きます。

## エラー例

### 例1: 未定義の変数を使った
```python
>>> print(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
```

### 例2: 関数名のスペルミス
```python
>>> pritn("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pritn' is not defined. Did you mean: 'print'?
```

### 例3: スコープの外の変数
```python
>>> def test():
...     x = 10
...
>>> print(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

## トレースバックの読み方

```
Traceback (most recent call last):        ← エラーの履歴（新しい順）
  File "<stdin>", line 1, in <module>     ← 場所：1行目
NameError: name 'name' is not defined     ← エラーの種類と理由
```

**読む順序**:
1. **最後の行**をまず読む — エラーの種類と理由が書いてある
2. **File ... の行**を見る — どこで起きたか分かる
3. `Did you mean` があれば**修正候補**を確認する

## 対処法

1. **変数を定義したか**確認する
2. **スペルミス**がないか確認する
3. **スコープ**（使える範囲）を確認する
4. `import` を忘れていないか確認する

## 確認問題

**問1**: 次のコードのエラーを直してください。
```python
score = 80
print(scroe)
```

**問2**: 次のコードで NameError が起きる行はどこ？
```python
def greet():
    message = "こんにちは"
    return message

print(greet())
print(message)
```

**問3**: `Did you mean: 'print'?` というメッセージが出ました。何が起きた？

---
→ 前: ../02_python_syntax/10_exceptions_custom.md
→ 次: [02_type_error.md](02_type_error.md)

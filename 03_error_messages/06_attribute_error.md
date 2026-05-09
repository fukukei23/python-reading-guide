# 6. AttributeError: 属性がない

## ざっくり言うと
Pythonが「そのオブジェクトには、その機能（属性）がありません」と言っているエラーです。
**メソッド名のスペルミス**や**違う型**に対してメソッドを呼んだときに起きます。

## エラー例

### 例1: リストに文字列のメソッドを使った
```python
>>> items = [1, 2, 3]
>>> items.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
```

### 例2: メソッド名のスペルミス
```python
>>> name = "たろう"
>>> name.uppr()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'uppr'. Did you mean: 'upper'?
```

### 例3: Noneに対してメソッドを呼んだ
```python
>>> result = None
>>> result.split()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'split'
```

## トレースバックの読み方

```
AttributeError: 'list' object has no attribute 'upper'
                 ↑                        ↑
            オブジェクトの型          使おうとした属性
```

**ポイント**:
- `'list' object` = リスト型のオブジェクト
- `has no attribute 'upper'` = `upper` という機能を持っていない
- `Did you mean` がある場合は**修正候補**を確認

## 対処法

1. その型に**どんなメソッドがあるか**確認する
   ```python
   dir(name)  # 使えるメソッド一覧を表示
   ```
2. **スペルミス**を確認する
3. **変数の型**が想定通りか確認する
   ```python
   print(type(result))  # 型を確認
   ```
4. `None` になっていないか確認する

## 確認問題

**問1**: 次のエラーの原因は？
```python
x = 100
x.append(5)
```

**問2**: `AttributeError: 'NoneType' object has no attribute 'split'` が出た。何を確認すべきか？

**問3**: 次のコードのエラーを直してください。
```python
name = "hello"
print(name.uppr())
```

---
→ 前: [05_value_error.md](05_value_error.md)
→ 次: [07_import_error.md](07_import_error.md)

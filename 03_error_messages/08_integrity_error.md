# 8. IntegrityError: データベース制約違反

## ざっくり言うと
データベースが「このデータはルール違反です」と言っているエラーです。
**同じIDを2回登録**したり、**必須の項目が空**だったりすると起きます。

## エラー例

### 例1: 主キーの重複
```python
>>> import sqlite3
>>> conn = sqlite3.connect("test.db")
>>> cursor = conn.cursor()
>>> cursor.execute("INSERT INTO users (id, name) VALUES (1, 'たろう')")
<sqlite3.Cursor object>
>>> cursor.execute("INSERT INTO users (id, name) VALUES (1, '花子')")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
sqlite3.IntegrityError: UNIQUE constraint failed: users.id
```

### 例2: NOT NULL 項目が空
```python
>>> cursor.execute("INSERT INTO users (id, name) VALUES (2, NULL)")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
sqlite3.IntegrityError: NOT NULL constraint failed: users.name
```

### 例3: 外部キー制約違反
```python
>>> cursor.execute("INSERT INTO orders (user_id) VALUES (999)")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
sqlite3.IntegrityError: FOREIGN KEY constraint failed
```

## トレースバックの読み方

```
sqlite3.IntegrityError: UNIQUE constraint failed: users.id
                          ↑                      ↑
                    制約の種類             違反した項目
```

**制約の種類**:
- `UNIQUE` = 同じ値を2回登録しようとした
- `NOT NULL` = 空の値を入れようとした
- `FOREIGN KEY` = 参照先のデータが存在しない
- `CHECK` = チェック条件を満たさない

## 対処法

1. **データが既存か確認**してから挿入する
   ```python
   cursor.execute("SELECT * FROM users WHERE id = 1")
   if cursor.fetchone() is None:
       cursor.execute("INSERT INTO users ...")
   ```
2. `INSERT OR IGNORE` や `INSERT OR REPLACE` を使う
3. **必須項目**が空でないか確認する
4. `try / except` で対処する

## 確認問題

**問1**: `UNIQUE constraint failed` は何が起きたことを意味する？

**問2**: 同じIDのデータが既にあるかどうかを確認する方法は？

**問3**: `NOT NULL constraint failed: users.email` というエラーが出た。何をすべきか？

---
→ 前: [07_import_error.md](07_import_error.md)
→ 次: [09_timeout_error.md](09_timeout_error.md)

# 7. ImportError / ModuleNotFoundError: インポート失敗

## ざっくり言うと
Pythonが「そのモジュール（機能のまとまり）が見つかりません」と言っているエラーです。
**インストールしていない**ライブラリや**名前を間違えた**モジュールを指定したときに起きます。

## エラー例

### 例1: インストールしていないライブラリ
```python
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```

### 例2: モジュール名のスペルミス
```python
>>> import datatime
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'datatime'
```

### 例3: 存在しない関数のインポート
```python
>>> from datetime import dat
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'dat' from 'datetime'
```

## トレースバックの読み方

```
ModuleNotFoundError: No module named 'pandas'
                                       ↑
                                見つからなかったモジュール名
```

**ポイント**:
- `ModuleNotFoundError` = モジュール全体が見つからない
- `ImportError` = モジュールはあるが中の関数/クラスが見つからない
- スペルミスの場合、正しい名前は `pip list` で確認できる

## 対処法

1. **インストールする**
   ```bash
   pip install pandas
   ```
2. **モジュール名のスペル**を確認する
   - `datetime` （正）≠ `datatime` （誤）
   - `numpy` （正）≠ `numppy` （誤）
3. **仮想環境**が有効か確認する
   ```bash
   pip list  # インストール済みか確認
   ```
4. `from ... import ...` の**関数名**を確認する

## 確認問題

**問1**: `ModuleNotFoundError: No module named 'reqeusts'` が出た。何を確認すべきか？

**問2**: 次のエラーを直すためのコマンドは？
```python
import flask
# ModuleNotFoundError: No module named 'flask'
```

**問3**: `ImportError` と `ModuleNotFoundError` の違いは？

---
→ 前: [06_attribute_error.md](06_attribute_error.md)
→ 次: [08_integrity_error.md](08_integrity_error.md)

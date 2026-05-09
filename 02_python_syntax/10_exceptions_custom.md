# 10. 例外の種類 — よく見る例外まとめ

## ざっくり言うと
プログラムが実行中に「困ったことが起きた」と報告するのが**例外**です。
Pythonには色々な種類の例外があり、それぞれ「何が起きたか」を知らせてくれます。

## コード例

### 例1: try / except の基本
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません")
```

### 例2: 複数の例外をまとめる
```python
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("数値に変換できません")
except ZeroDivisionError:
    print("0で割ろうとしました")
```

### 例3: 自分で例外を作る
```python
class TooSmallError(Exception):
    pass

age = 15
if age < 18:
    raise TooSmallError("18歳未満は登録できません")
```

## 読み方ガイド

よく見る例外の一覧:

| 例外名 | 意味 | 例 |
|---|---|---|
| `ValueError` | 値がおかしい | `int("abc")` |
| `TypeError` | 型が違う | `"2" + 3` |
| `NameError` | 名前が見つからない | `print(x)` (x未定義) |
| `IndexError` | 範囲外 | `list[10]` (長さ3) |
| `KeyError` | キーがない | `dict["x"]` |
| `ZeroDivisionError` | 0で割った | `1 / 0` |
| `FileNotFoundError` | ファイルがない | `open("x.txt")` |

## よくあるパターン

- `try / except` で囲んでエラーを防ぐ
- `except Exception as e:` で全般的な例外を受け取る
- `raise` で自分から例外を出す
- `finally` で必ず実行する処理を書く

## 確認問題

**問1**: 次のコードはどの例外が起きる？
```python
data = [1, 2, 3]
print(data[5])
```

**問2**: `try / except` を使って、`int("hello")` のエラーを防いでください。

**問3**: `raise` の役割は何？

---
→ 前: [09_slicing.md](09_slicing.md)
→ 次: [../03_error_messages/01_name_error.md](../03_error_messages/01_name_error.md)

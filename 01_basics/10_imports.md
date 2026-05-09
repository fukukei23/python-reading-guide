# 10. インポート（import）

## ざっくり言うと
インポートは「他人が作った便利な道具箱を読み込む」仕組みです。ゼロから作らなくても、用意された道具を使えます。

## コード例

### 例1：標準ライブラリの読み込み
```python
import datetime

today = datetime.date.today()
print(today)
```

### 例2：from で特定の道具だけ読み込む
```python
from pathlib import Path

config_path = Path("config/settings.json")
print(config_path.exists())
```

### 例3：実務例（LINEbot SDKの読み込み）
```python
# atelier-kyo-manager 風
from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi("channel_access_token")
message = TextSendMessage(text="ご予約ありがとうございます")
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `import datetime` | datetime という道具箱を丸ごと読み込む |
| `datetime.date.today()` | datetime 箱の中の date.today() という道具を使う |
| `from pathlib import Path` | pathlib 箱から Path という道具だけ取り出す |
| `from linebot.models import TextSendMessage` | linebot の models から TextSendMessage を取り出す |

- `import X` = Xというモジュール（道具箱）を読み込む
- `from X import Y` = XからYという道具だけ取り出す
- `as` で別名を付けることもできる：`import numpy as np`

## よくあるパターン

**パターン1：as で短い名前に**
```python
import datetime as dt

today = dt.date.today()
```

**パターン2：環境変数の読み込み**
```python
# NexusCore 風
import os

database_url = os.environ.get("DATABASE_URL")
secret_key = os.environ.get("SECRET_KEY")
```

**パターン3：複数の道具を読み込む**
```python
# reserve-optimizer 風
from typing import List, Dict, Optional

def search_reservations(
    date: str,
    names: List[str],
    options: Optional[Dict] = None
):
    pass
```
- `typing` は型を明示するためのモジュール
- `List`, `Dict`, `Optional` などがよく使われる

## 確認問題

**問1** 以下のコードで `random.randint(1, 6)` は何をする道具だと思われますか？
```python
import random

dice = random.randint(1, 6)
print(dice)
```

**問2** 以下の2つの書き方の違いを説明してください。
```python
# 書き方A
import os
path = os.path.join("data", "file.txt")

# 書き方B
from os.path import join
path = join("data", "file.txt")
```

**問3** 以下のコードは何を表示しますか？
```python
import math
result = math.ceil(3.2)
print(result)
```

---
→ これで「Python読解力」基礎編は終了です。おつかれさまでした！

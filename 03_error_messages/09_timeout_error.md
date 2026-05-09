# 9. TimeoutError: 時間切れ

## ざっくり言うと
プログラムが「待ち時間を過ぎました」と言っているエラーです。
通信や処理の**待機時間が制限を超えた**ときに起きます。

## エラー例

### 例1: ネットワーク通信のタイムアウト
```python
>>> import urllib.request
>>> urllib.request.urlopen("http://very-slow-site.com", timeout=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
TimeoutError: timed out
```

### 例2: requestsライブラリのタイムアウト
```python
>>> import requests
>>> requests.get("http://slow-api.com", timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
requests.exceptions.ReadTimeout:
  HTTPConnectionPool(host='slow-api.com', port=80):
  Read timed out. (read timeout=0.001)
```

### 例3: 非同期処理のタイムアウト
```python
>>> import asyncio
>>> async def slow_task():
...     await asyncio.sleep(10)
...
>>> asyncio.wait_for(slow_task(), timeout=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
asyncio.TimeoutError
```

## トレースバックの読み方

```
TimeoutError: timed out
              ↑
         「時間切れ」という意味
```

```
requests.exceptions.ReadTimeout:
  Read timed out. (read timeout=0.001)
                    ↑
              設定したタイムアウト時間
```

**ポイント**:
- タイムアウト時間は**秒単位**で設定する
- ネットワークの状況によって発生したりしなかったりする
- `...` の部分には詳細な呼び出し履歴が入る

## 対処法

1. **タイムアウト時間を長くする**
   ```python
   requests.get(url, timeout=30)  # 30秒にする
   ```
2. **try / except** でリトライする
   ```python
   import time
   for attempt in range(3):
       try:
           response = requests.get(url, timeout=5)
           break
       except TimeoutError:
           print(f"リトライ {attempt + 1}回目")
           time.sleep(2)
   ```
3. 通信先が**生きているか**確認する

## 確認問題

**問1**: `timeout=5` は何秒待つか？

**問2**: タイムアウトが起きたときにリトライする方法を説明してください。

**問3**: TimeoutError がよく起きる状況を2つ挙げてください。

---
→ 前: [08_integrity_error.md](08_integrity_error.md)
→ 次: [10_connection_error.md](10_connection_error.md)

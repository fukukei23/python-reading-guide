# 04-02 リトライ付きスクレイピングを読む

> 出典: **atelier-kyo-manager**（物販管理システム）
> 内容: Webページを自動取得する処理。失敗したら自動で再試行する仕組み

---

## コード全体

```python
async def scrape_with_retry(self, url: str, max_retries: int = 3) -> dict:
    for attempt in range(max_retries):
        try:
            result = await self.browser.fetch(url)
            if result.is_valid():
                return result.to_dict()
        except TimeoutError:
            wait_time = 2 ** attempt + random.uniform(0, 1)
            logger.warning(f"Retry {attempt+1}/{max_retries} after {wait_time:.1f}s")
            await asyncio.sleep(wait_time)
    raise ScrapingError(f"Failed after {max_retries} attempts: {url}")
```

---

## 1行ずつ読む

### `async def scrape_with_retry(self, url: str, max_retries: int = 3) -> dict:`

| 項目 | 説明 |
|------|------|
| `async` | 「非同期」という意味。待っている間に別の処理を進められる |
| `def` | 関数の定義 |
| `url: str` | 取得したいWebページのURL（文字列） |
| `max_retries: int = 3` | 最大試行回数。省略すると3回 |
| `-> dict` | 辞書（データのまとまり）を返す |

**使っている概念**: 非同期関数、デフォルト引数（02_python_syntax）

**一言で**: 「URLを受け取り、失敗しても何度か再挑戦する非同期関数」

---

### `for attempt in range(max_retries):`

| 項目 | 説明 |
|------|------|
| `for ... in ...` | 繰り返し処理（01_basics 参照） |
| `attempt` | 何回目の試行か（0, 1, 2...） |
| `range(max_retries)` | 0から max_retries-1 までの数列 |

**一言で**: 「最大回数まで繰り返すループの開始」

---

### `try:`

| 項目 | 説明 |
|------|------|
| `try` | 「この中のコードでエラーが起きるか試す」 |
| エラーが起きたら `except` に飛ぶ | 安全ネットの仕組み |

**使っている概念**: try/except（01_basics）

**一言で**: 「エラーが起きるかもしれない処理を始める」

---

### `result = await self.browser.fetch(url)`

| 項目 | 説明 |
|------|------|
| `await` | 非同期処理の完了を待つキーワード |
| `self.browser.fetch(url)` | ブラウザでURLにアクセスしてページを取得 |
| `result` | 取得した結果を保存 |

**一言で**: 「Webページを取得する。取得できるまで待つ」

---

### `if result.is_valid():` / `return result.to_dict()`

| 項目 | 説明 |
|------|------|
| `result.is_valid()` | 取得結果が「正しいか」をチェック |
| `return` | 関数をここで終了し、値を返す |
| `result.to_dict()` | 結果を辞書形式に変換して返す |

**一言で**: 「取得したデータが正常なら、辞書にして返して終了」

---

### `except TimeoutError:`

| 項目 | 説明 |
|------|------|
| `except` | tryの中でエラーが起きたときの処理 |
| `TimeoutError` | 「時間切れ」エラー。サーバーの応答が遅すぎた |

**使っている概念**: 例外処理（01_basics）

**一言で**: 「時間切れエラーが起きた場合の処理」

---

### `wait_time = 2 ** attempt + random.uniform(0, 1)`

| 項目 | 説明 |
|------|------|
| `2 ** attempt` | 2の累乗。0回目=1秒、1回目=2秒、2回目=4秒... |
| `random.uniform(0, 1)` | 0〜1のランダムな小数 |
| 合計 | 「指数バックオフ」。だんだん待ち時間を長くする |

**使っている概念**: 演算子、乱数（01_basics）

**一言で**: 「再試行までの待ち時間を計算。後になるほど長く待つ」

---

### `logger.warning(f"Retry {attempt+1}/{max_retries} after {wait_time:.1f}s")`

| 項目 | 説明 |
|------|------|
| `logger.warning(...)` | 警告ログを記録する |
| `f"..."` | f文字列。変数を文字列に埋め込む |
| `{wait_time:.1f}` | 小数を小数点1桁で表示 |

**使っている概念**: f文字列、ログ出力（02_python_syntax）

**一言で**: 「ログに『何回目の再試行か、何秒待つか』を記録」

---

### `await asyncio.sleep(wait_time)`

**一言で**: 「計算した時間だけ待機する」

---

### `raise ScrapingError(f"Failed after {max_retries} attempts: {url}")`

| 項目 | 説明 |
|------|------|
| `raise` | エラーを発生させる |
| `ScrapingError` | スクレイピング専用のエラー型 |

**一言で**: 「全回数試してもダメだったら、エラーを投げて終了」

---

## 処理の流れ（まとめ）

```
URLを受け取る
  → Webページの取得を試みる（最大3回）
    → 成功したら結果を返す
    → タイムアウトしたら少し待って再試行
      （待ち時間は2倍ずつ増える）
  → 全部失敗したらエラーを投げる
```

---

## 使われている「指数バックオフ」

このコードで一番重要なアイデアは **指数バックオフ** です。

| 試行回数 | 待ち時間の計算 | およその待ち時間 |
|----------|---------------|----------------|
| 1回目 | 2^0 + ランダム | 約1秒 |
| 2回目 | 2^1 + ランダム | 約2秒 |
| 3回目 | 2^2 + ランダム | 約4秒 |

「焦らず少しずつ間隔を空ける」のがポイントです。

---

## 練習問題

> このコードを3文で説明してください。

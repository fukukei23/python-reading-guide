# 04-04 LINE Botの状態管理を読む

> 出典: **reserve-optimizer**（予約管理LINE Bot）
> 内容: LINEでユーザーとやり取りする Bot の「状態遷移」
> 言語: JavaScript（Python以外の言語も、構造は同じです）

---

## コード全体

```javascript
function handleLineEvent(event) {
  var userId = event.source.userId;
  var state = getUserState(userId);

  switch (state) {
    case 'IDLE':
      return handleIdle(event);
    case 'AWAITING_DATE':
      return handleDateInput(event);
    case 'AWAITING_PAYMENT':
      return handlePaymentConfirmation(event);
    default:
      return sendFallbackWithContact(event.replyToken, '予期しない状態です');
  }
}
```

---

## 1行ずつ読む

### `function handleLineEvent(event) {`

| 項目 | 説明 |
|------|------|
| `function` | 関数の定義（Pythonの `def` と同じ） |
| `handleLineEvent` | 関数名。「LINEイベントを処理する」 |
| `event` | LINEから送られてきたメッセージなどの情報 |
| `{` | ブロックの開始（Pythonの `:` と同じ） |

**Pythonとの違い**: JavaScriptは `{ }` でブロックを作る

**一言で**: 「LINEからのメッセージを処理する関数」

---

### `var userId = event.source.userId;`

| 項目 | 説明 |
|------|------|
| `var` | 変数の宣言（Pythonにはない） |
| `userId` | メッセージを送ったユーザーのID |
| `event.source.userId` | ドットでつないでデータにアクセス |

**Pythonとの違い**: Pythonは `user_id = event.source.userId` のように `var` が不要

**使っている概念**: 変数、代入、オブジェクトのプロパティアクセス（01_basics）

**一言で**: 「誰からのメッセージか（ユーザーID）を取得」

---

### `var state = getUserState(userId);`

| 項目 | 説明 |
|------|------|
| `getUserState(userId)` | このユーザーが今「どの状態」にいるかを調べる |
| `state` | 状態を保存 |

**一言で**: 「このユーザーが今、会話のどの段階にいるかを確認」

---

### `switch (state) {`

| 項目 | 説明 |
|------|------|
| `switch` | `state` の値によって処理を分ける（Pythonにはない構文） |
| Python相当 | `if state == 'IDLE':` / `elif state == 'AWAITING_DATE':` の連続 |

**Pythonでの書き方**: `if` / `elif` を使う（機能は同じ）

**一言で**: 「状態の値に応じて、処理を振り分ける」

---

### `case 'IDLE': return handleIdle(event);`

| 項目 | 説明 |
|------|------|
| `case 'IDLE'` | 状態が「IDLE（待機中）」のとき |
| `handleIdle` | 待機中のメッセージを処理する関数 |
| `return` | 結果を返して終了 |

**一言で**: 「ユーザーがまだ何も始めていない状態 → 最初の応対をする」

---

### `case 'AWAITING_DATE': return handleDateInput(event);`

| 項目 | 説明 |
|------|------|
| `'AWAITING_DATE'` | 状態が「日付入力待ち」 |
| `handleDateInput` | 日付として解釈して次へ進める |

**一言で**: 「Botが日付を聞いている状態 → 日付として処理」

---

### `case 'AWAITING_PAYMENT': return handlePaymentConfirmation(event);`

| 項目 | 説明 |
|------|------|
| `'AWAITING_PAYMENT'` | 状態が「支払い確認待ち」 |
| `handlePaymentConfirmation` | 支払い確認として処理 |

**一言で**: 「Botが支払い確認を待っている状態 → 確認として処理」

---

### `default: return sendFallbackWithContact(...);`

| 項目 | 説明 |
|------|------|
| `default` | どの `case` にも当てはまらない場合 |
| `sendFallbackWithContact` | 「お問い合わせ」案内を返す |
| `'予期しない状態です'` | エラーメッセージ |

**一言で**: 「想定外の状態になったら、問い合わせを案内する」

---

## 状態遷移の図

このBotは「状態機械（ステートマシン）」という考え方を使っています。

```
ユーザーがメッセージを送る
        │
        ▼
    [IDLE]（待機中）
        │ 「予約したい」と送る
        ▼
  [AWAITING_DATE]（日付待ち）
        │ 「明日」と送る
        ▼
  [AWAITING_PAYMENT]（支払い待ち）
        │ 「はい」と送る
        ▼
    予約確定 → [IDLE] に戻る
```

**ポイント**: 同じ「はい」というメッセージでも、状態によって意味が変わる

---

## Python で書くとどうなる？

```python
def handle_line_event(event):
    user_id = event.source.user_id
    state = get_user_state(user_id)

    if state == 'IDLE':
        return handle_idle(event)
    elif state == 'AWAITING_DATE':
        return handle_date_input(event)
    elif state == 'AWAITING_PAYMENT':
        return handle_payment_confirmation(event)
    else:
        return send_fallback_with_contact(event.reply_token, '予期しない状態です')
```

構造はほぼ同じです。違いは:

| 項目 | JavaScript | Python |
|------|-----------|--------|
| 関数定義 | `function` | `def` |
| 変数宣言 | `var` | 不要 |
| 条件分岐 | `switch` / `case` | `if` / `elif` |
| ブロック | `{ }` | インデント |

---

## 練習問題

> このコードを3文で説明してください。

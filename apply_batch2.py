#!/usr/bin/env python3
"""Apply 3 improvements to all 30 interactive HTML lessons:
  - 1.2: Common mistakes warning card
  - 3.3: Font size adjustment controls
  - 4.1: Cheat sheet / summary print section
"""

import os, re

BASICS = [f'{i:02d}_{n}' for i, n in enumerate([
    'variables','functions','parameters','conditionals','loops','lists',
    'dictionaries','strings_numbers','boolean_none','imports',
    'classes','methods','try_except','async_await','type_hints',
    'decorators','context_managers','operators','string_operations','file_io'
], 1)]

SYNTAX = [f'{i:02d}_{n}' for i, n in enumerate([
    'indentation','fstring','list_comprehension','with_statement',
    'args_kwargs','init_self','lambda','generators','slicing','exceptions_custom'
], 1)]

# === 1.2: Common mistakes data per lesson ===
MISTAKES = {
    '01_variables': [
        {'title': '= の意味を間違える', 'desc': '= は「等しい」ではなく「右辺を左の箱に入れる」という意味。等しいか調べるには == を使います。'},
        {'title': '数字に "" を付ける', 'desc': '文字は "田中" のように囲みますが、数字の 1980 は囲みません。囲むと文字列になって計算できなくなります。'},
    ],
    '02_functions': [
        {'title': 'def の後ろに : を忘れる', 'desc': 'def say_hello(): のように、関数定義の行の最後にコロン（:）が必要です。'},
        {'title': 'インデントを忘れる', 'desc': '関数の中身は必ず字下げ（インデント）します。通常はスペース4つです。'},
    ],
    '03_parameters': [
        {'title': '引数の数を間違える', 'desc': 'def add(a, b) と定義したら、add(1, 2) のように引数を2つ渡す必要があります。'},
        {'title': '仮引数と実引数を混同する', 'desc': 'def add(a, b) の a, b は仮引数（箱の名前）。add(1, 2) の 1, 2 は実引数（入れる値）。'},
    ],
    '04_conditionals': [
        {'title': 'elif を elif と書かず else if と書く', 'desc': 'Pythonでは else if ではなく elif と書きます。'},
        {'title': '条件に = を使う', 'desc': '等しいか調べるには == を使います。= は代入（箱に入れる）です。'},
    ],
    '05_loops': [
        {'title': 'range の範囲を間違える', 'desc': 'range(5) は 0, 1, 2, 3, 4 です。5 は含まれません。'},
        {'title': '無限ループを作ってしまう', 'desc': 'while True: の中に break や条件変更がないと、永遠に繰り返されます。'},
    ],
    '06_lists': [
        {'title': 'インデックスを 1 から始める', 'desc': 'リストのインデックスは 0 から始まります。最初の要素は list[0] です。'},
        {'title': '範囲外のインデックスを指定する', 'desc': '3要素のリストで list[3] にアクセスするとエラーになります。最後は list[2] です。'},
    ],
    '07_dictionaries': [
        {'title': '存在しないキーにアクセスする', 'desc': 'd["age"] でキーが存在しないとエラー。.get("age", 0) なら安全に取得できます。'},
        {'title': 'キーと値を逆に書く', 'desc': 'd = {"名前": "田中"} のように「キー: 値」の順です。値→キーではありません。'},
    ],
    '08_strings_numbers': [
        {'title': '文字列 + 数字 を計算する', 'desc': '"年齢: " + 25 はエラー。str(25) で数字を文字列に変換してから繋ぎます。'},
        {'title': 'input() の戻り値を数字として扱う', 'desc': 'input() は常に文字列を返します。計算するには int() や float() で変換します。'},
    ],
    '09_boolean_none': [
        {'title': 'None と False を同じだと思う', 'desc': 'None は「値がない」。False は「偽」。両方とも if で「偽」として扱われますが、意味が違います。'},
        {'title': '== None ではなく is None を使う', 'desc': 'None との比較は is None が推奨されます。== None でも動きますが、習慣的に is を使います。'},
    ],
    '10_imports': [
        {'title': 'モジュール名を間違える', 'desc': 'import randam のようにスペルミスするとエラー。正しくは import random です。'},
        {'title': 'from ... import * を使いすぎる', 'desc': '便利ですが、どの関数がどのモジュールから来たか分からなくなります。必要なものだけ import しましょう。'},
    ],
    '11_classes': [
        {'title': 'self を忘れる', 'desc': 'メソッドの第一引数には必ず self が必要です。self.name = name のようにインスタンス変数にアクセスします。'},
        {'title': 'クラス名に小文字を使う', 'desc': 'クラス名は MyClass のように大文字始まり（CamelCase）がルールです。'},
    ],
    '12_methods': [
        {'title': 'メソッド呼び出しで . を忘れる', 'desc': 'len(list) は関数ですが、list.append(1) はメソッド。メソッドは「オブジェクト.メソッド()」です。'},
        {'title': '文字列メソッドが元を変えないと勘違いする', 'desc': '"hello".upper() は "HELLO" を返しますが、元の文字列は変わりません。結果を代入する必要があります。'},
    ],
    '13_try_except': [
        {'title': 'except を裸で書く', 'desc': 'except: だけだと全エラーを捕捉してしまい、バグの原因を見つけにくくなります。except ValueError: のように具体的に。'},
        {'title': '例外を無視して pass だけ書く', 'desc': 'except: pass はエラーを隠してしまいます。最低でもログ出力やユーザーへの通知をしましょう。'},
    ],
    '14_async_await': [
        {'title': 'await を async 関数の外で使う', 'desc': 'await は async def の中でしか使えません。普通の関数の中では使えません。'},
        {'title': '非同期関数を直接呼び出す', 'desc': 'async def func() を func() で呼んでも実行されません。await func() または asyncio.run() が必要です。'},
    ],
    '15_type_hints': [
        {'title': '型ヒントを実行時チェックだと思う', 'desc': '型ヒントは「注釈」であり、実行時にエラーになりません。mypy等のツールでチェックします。'},
        {'title': '複雑な型を書きすぎる', 'desc': '最初は str, int, List[int] 程度で十分です。Union, Optional 等は必要になってから使いましょう。'},
    ],
    '16_decorators': [
        {'title': '@ を付け忘れる', 'desc': 'デコレータは @my_decorator のように関数定義の直前に @ 付きで書きます。'},
        {'title': 'デコレータが元の関数を変えると思っている', 'desc': 'デコレータは関数を「包む」ものであり、元の関数自体を書き換えるわけではありません。'},
    ],
    '17_context_managers': [
        {'title': 'with ブロックの外でリソースを使う', 'desc': 'with open(...) as f: の中でのみファイルにアクセスできます。外ではファイルは閉じています。'},
        {'title': '__exit__ の戻り値を間違える', 'desc': '__exit__ で True を返すと例外が握りつぶされます。基本は None（または False）を返します。'},
    ],
    '18_operators': [
        {'title': 'and と or の優先順位を間違える', 'desc': 'and の方が or より優先度が高いです。a or b and c は a or (b and c) と解釈されます。'},
        {'title': 'is と == を混同する', 'desc': '== は値の比較。is は同一オブジェクトかの比較。None のチェックには is を使います。'},
    ],
    '19_string_operations': [
        {'title': '文字列は変更できると思う', 'desc': 'Pythonの文字列は変更不可（イミュータブル）です。s[0] = "a" はエラー。新しい文字列を作る必要があります。'},
        {'title': 'フォーマット方法を混在させる', 'desc': 'f文字列、.format()、%記法が混在すると読みにくい。プロジェクト内では統一しましょう。'},
    ],
    '20_file_io': [
        {'title': 'ファイルを閉じ忘れる', 'desc': 'open() したら close() が必要。with open() を使えば自動で閉じます。'},
        {'title': 'エンコーディングを指定しない', 'desc': 'open("file.txt", encoding="utf-8") のように encoding を指定しないと、環境によって文字化けします。'},
    ],
    '01_indentation': [
        {'title': 'タブとスペースを混ぜる', 'desc': 'Pythonではタブとスペースを混在させるとエラー。スペース4つに統一しましょう。'},
        {'title': 'インデントの幅を揃えない', 'desc': '同じブロック内の行は同じインデント幅でなければなりません。'},
    ],
    '02_fstring': [
        {'title': 'f を付け忘れる', 'desc': '"Hello {name}" だけでは変数展開されません。f"Hello {name}" のように先頭に f が必要です。'},
        {'title': '波括弧を表示したい時にエラーになる', 'desc': '{{ と }} で波括弧自体を表示できます。f"{{x}}" → "{x}"。'},
    ],
    '03_list_comprehension': [
        {'title': '複雑な内包表記を書きすぎる', 'desc': 'if や for が3つ以上続く内包表記は読みにくい。普通の for ループに分けましょう。'},
        {'title': '内包表記で副作用を使う', 'desc': '[print(x) for x in list] は動きますが、None のリストができます。内包表記は値を作るために使いましょう。'},
    ],
    '04_with_statement': [
        {'title': 'with を使わずにリソースを開く', 'desc': 'f = open(...) だけだとエラー時に閉じられない可能性があります。with open() を使いましょう。'},
        {'title': '複数リソースを別々に with で開く', 'desc': 'with open("a") as fa, open("b") as fb: のように1行で書けます。'},
    ],
    '05_args_kwargs': [
        {'title': '*args を普通の引数の前に置く', 'desc': 'def func(*args, name): はエラー。*args は通常の引数の後に置きます。'},
        {'title': '**kwargs のキーに文字列以外を使う', 'desc': '**kwargs のキーは常に文字列です。func(**{1: "a"}) はエラーになります。'},
    ],
    '06_init_self': [
        {'title': 'self に別の名前を付ける', 'desc': '技術的には可能ですが、Pythonの慣習として第一引数は必ず self にします。'},
        {'title': '__init__ の中で self. を付け忘れる', 'desc': 'self.name = name ではなく name = name と書くと、引数を上書きするだけでインスタンス変数に保存されません。'},
    ],
    '07_lambda': [
        {'title': 'lambda に複数行を書く', 'desc': 'lambda は1行の式だけです。複数行の処理は def で通常関数を定義しましょう。'},
        {'title': 'lambda に名前を付ける', 'desc': 'f = lambda x: x+1 は動きますが、def f(x): return x+1 の方がPythonicです。lambda は名前なしで使うのが基本。'},
    ],
    '08_generators': [
        {'title': 'return の代わりに yield を忘れる', 'desc': 'ジェネレータ関数には return ではなく yield が必要です。yield で値を返しつつ中断できます。'},
        {'title': 'ジェネレータを2回使い回す', 'desc': 'ジェネレータは1回しか消費できません。再度使うには list(gen) でリストにするか、新しく作り直します。'},
    ],
    '09_slicing': [
        {'title': 'スライスの終了インデックスを含むと思う', 'desc': 'list[1:4] は list[1], list[2], list[3] です。list[4] は含まれません。'},
        {'title': '負のインデックスの意味を間違える', 'desc': 'list[-1] は最後の要素。list[-3:-1] は後ろから3つ目〜後ろから2つ目（最後は含まない）。'},
    ],
    '10_exceptions_custom': [
        {'title': 'Exception を直接継承する', 'desc': 'カスタム例外は ValueError や RuntimeError など、より具体的な例外を継承するのが推奨されます。'},
        {'title': 'raise で文字列を投げる', 'desc': 'raise "エラー" はエラー。raise ValueError("エラー") のように例外クラスのインスタンスを投げます。'},
    ],
}

# === 4.1: Cheat sheet summaries per lesson ===
CHEAT_SHEETS = {
    '01_variables': {'concept': '変数', 'points': ['x = 10 — 右辺を左の箱に入れる', '数字はそのまま、文字は "" で囲む', '変数名は英語で意味が分かるように', '後から値を上書きできる（だから「変数」）']},
    '02_functions': {'concept': '関数', 'points': ['def name(): で定義', 'return で結果を返す', '呼び出し: name()', 'インデントで中身を示す']},
    '03_parameters': {'concept': '引数', 'points': ['def add(a, b): — a, b は仮引数', 'add(1, 2) — 1, 2 は実引数', 'デフォルト値: def f(x=10):', '*args で可変長引数']},
    '04_conditionals': {'concept': '条件分岐', 'points': ['if / elif / else で分岐', '条件は ==, !=, <, >, <=, >=', 'and / or / not で組み合わせ', 'インデントでブロックを示す']},
    '05_loops': {'concept': '繰り返し', 'points': ['for i in range(n): — n回繰り返し', 'while 条件: — 条件が真の間繰り返し', 'break で途中脱出', 'continue で次の周へスキップ']},
    '06_lists': {'concept': 'リスト', 'points': ['[1, 2, 3] — 角括弧で作成', 'list[0] — インデックスは0始まり', 'list.append(x) — 末尾に追加', 'len(list) — 要素数を取得']},
    '07_dictionaries': {'concept': '辞書', 'points': ['{"key": "value"} — 波括弧で作成', 'd["key"] — キーで値にアクセス', 'd.get("key", default) — 安全な取得', 'd["new"] = val — 新規追加']},
    '08_strings_numbers': {'concept': '文字列と数値', 'points': ['str(123) — 数字→文字列', 'int("123") — 文字列→数字', 'f"値は{x}" — f文字列で埋め込み', '+ */ で演算（型を揃える）']},
    '09_boolean_none': {'concept': '真偽値とNone', 'points': ['True / False — ブール値', 'None — 「値がない」ことを表す', 'x is None — None判定', '0, "", [], {} は False として扱われる']},
    '10_imports': {'concept': 'インポート', 'points': ['import module — モジュール全体', 'from module import func — 関数だけ', 'import module as m — 別名', '__name__ == "__main__" — 直接実行時のみ']},
    '11_classes': {'concept': 'クラス', 'points': ['class MyClass: — 大文字始まり', '__init__(self) — 初期化メソッド', 'self.x — インスタンス変数', 'obj = MyClass() — インスタンス化']},
    '12_methods': {'concept': 'メソッド', 'points': ['obj.method() — ドットで呼び出し', 'self で自分自身にアクセス', '文字列はイミュータブル（メソッドは新規作成）', 'list.sort() は in-place（元を変更）']},
    '13_try_except': {'concept': '例外処理', 'points': ['try: ... except Error: ...', '具体的なエラー型を指定する', 'finally: — 必ず実行', 'raise ValueError("msg") — 意図的にエラー']},
    '14_async_await': {'concept': '非同期', 'points': ['async def func(): — 非同期関数', 'await func() — 結果を待つ', 'asyncio.run(main()) — 実行', 'await は async def の中だけで使える']},
    '15_type_hints': {'concept': '型ヒント', 'points': ['def f(x: int) -> str:', 'List[int], Dict[str, int]', 'Optional[str] = None も可能', '実行時チェックではない（注釈のみ）']},
    '16_decorators': {'concept': 'デコレータ', 'points': ['@decorator — 関数を「包む」', 'def wrapper(*args, **kwargs):', 'functools.wraps(f) — メタデータ維持', '元の関数を変更せず機能を追加']},
    '17_context_managers': {'concept': 'コンテキストマネージャ', 'points': ['with open("f") as f: — 自動close', '__enter__ / __exit__ を定義', 'contextlib.contextmanager で簡易作成', 'リソースの安全な確保・解放']},
    '18_operators': {'concept': '演算子', 'points': ['+ - * / // % ** — 算術', '== != < > <= >= — 比較', 'and or not — 論理', 'is / is not — 同一性比較']},
    '19_string_operations': {'concept': '文字列操作', 'points': ['s.upper() / s.lower() — 大小文字変換', 's.split(",") — 分割', '", ".join(list) — 結合', 's.strip() — 前後空白削除', 's[start:end] — スライス']},
    '20_file_io': {'concept': 'ファイル入出力', 'points': ['with open("f", "r") as f: — 読み込み', 'with open("f", "w") as f: — 書き込み', 'encoding="utf-8" を必ず指定', 'f.read() / f.readline() / f.readlines()']},
    '01_indentation': {'concept': 'インデント', 'points': ['スペース4つが標準', 'タブとスペースを混ぜない', 'インデント = ブロック（{ } の代わり）', 'インデントが揃っていないとエラー']},
    '02_fstring': {'concept': 'f文字列', 'points': ['f"Hello {name}" — 変数展開', 'f"{x:.2f}" — フォーマット指定', 'f"{expr}" — 式も書ける', '{{ }} で波括弧自体を表示']},
    '03_list_comprehension': {'concept': 'リスト内包表記', 'points': ['[x*2 for x in list]', '[x for x in list if x > 0]', '読みにくくなったら for ループに分ける', 'dict/set 内包表記もある']},
    '04_with_statement': {'concept': 'with文', 'points': ['with open("f") as f: — 自動close', '__enter__ / __exit__ を定義すれば自作可能', '複数: with A() as a, B() as b:', 'contextlib.contextmanager で簡単作成']},
    '05_args_kwargs': {'concept': '*args/**kwargs', 'points': ['*args — 可変長位置引数（タプル）', '**kwargs — 可変長キーワード引数（辞書）', 'def f(a, b, *args, **kwargs)', '引数の順序: 通常→*args→**kwargs']},
    '06_init_self': {'concept': '__init__とself', 'points': ['__init__ — インスタンス初期化メソッド', 'self — インスタンス自身を指す', 'self.name = name — インスタンス変数', '__init__ に return は不要']},
    '07_lambda': {'concept': 'ラムダ', 'points': ['lambda x: x + 1 — 無名関数', '1行の式だけ（複数行不可）', 'sorted(list, key=lambda x: x[1])', '名前を付けない使い方が基本']},
    '08_generators': {'concept': 'ジェネレータ', 'points': ['yield で値を返しつつ中断', 'next(gen) で次の値を取得', '1回しか消費できない', 'メモリ効率が良い（大量データ向き）']},
    '09_slicing': {'concept': 'スライス', 'points': ['list[start:stop] — start〜stop-1', 'list[:3] — 先頭から3つ', 'list[::2] — 1つ飛ばし', 'list[::-1] — 逆順', '文字列にも使える']},
    '10_exceptions_custom': {'concept': 'カスタム例外', 'points': ['class MyError(Exception):', 'raise MyError("message")', '具体的な基底クラスを継承', '__str__ でエラーメッセージをカスタマイズ']},
}

# === CSS to inject ===
NEW_CSS = '''
/* === 1.2: Common mistakes card === */
.mistakes-card {
  background: rgba(251,191,36,0.08);
  border: 1px solid rgba(251,191,36,0.3);
  border-left: 4px solid var(--warning);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 24px;
}
.mistakes-label {
  font-size: 12px; font-weight: 700; color: var(--warning);
  margin-bottom: 10px; letter-spacing: 0.06em;
}
.mistake-item {
  font-size: 14px; line-height: 1.7; margin-bottom: 8px;
  padding-left: 16px; position: relative;
}
.mistake-item:last-child { margin-bottom: 0; }
.mistake-item::before {
  content: '\\26A0'; position: absolute; left: 0; top: 0;
  color: var(--warning); font-size: 12px;
}
.mistake-title { font-weight: 600; color: var(--warning); }
.mistake-desc { color: var(--fg-dim); }

/* === 3.3: Font size controls === */
.font-controls {
  display: flex; gap: 4px; align-items: center;
}
.font-btn {
  width: 28px; height: 28px; border: 1px solid var(--border);
  border-radius: 4px; background: rgba(255,255,255,0.06);
  color: var(--fg-dim); font-size: 14px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all var(--transition);
}
.font-btn:hover { background: rgba(255,255,255,0.12); color: var(--fg); }
.font-btn.active { background: var(--accent-dim); color: var(--accent); border-color: var(--accent); }
body.font-sm .concept-card p, body.font-sm .key-point p, body.font-sm .quiz-title,
body.font-sm .mistake-item, body.font-sm .cheat-item { font-size: 13px; }
body.font-sm .code-line .line-content { font-size: 12px; }
body.font-lg .concept-card p, body.font-lg .key-point p, body.font-lg .quiz-title,
body.font-lg .mistake-item, body.font-lg .cheat-item { font-size: 17px; }
body.font-lg .code-line .line-content { font-size: 16px; }

/* === 4.1: Cheat sheet section === */
.cheat-section {
  background: var(--bg-raised); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px 24px;
  margin-bottom: 24px;
}
.cheat-header {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 12px;
}
.cheat-label { font-size: 12px; font-weight: 700; color: var(--success); letter-spacing: 0.06em; }
.cheat-print-btn {
  font-size: 12px; padding: 4px 12px; border-radius: 4px;
  border: 1px solid var(--border); background: rgba(255,255,255,0.06);
  color: var(--fg-dim); cursor: pointer; transition: all var(--transition);
}
.cheat-print-btn:hover { background: rgba(255,255,255,0.12); color: var(--fg); }
.cheat-concept { font-size: 15px; font-weight: 600; color: var(--fg-bright); margin-bottom: 8px; }
.cheat-list { list-style: none; padding: 0; }
.cheat-item {
  font-size: 14px; line-height: 1.8; padding: 4px 0 4px 20px;
  position: relative; color: var(--fg);
}
.cheat-item::before {
  content: '\\2713'; position: absolute; left: 0; color: var(--success);
  font-size: 12px;
}
@media print {
  body > *:not(.container) { display: none !important; }
  .container > *:not(.cheat-section) { display: none !important; }
  .cheat-section { border: 2px solid #333; background: #fff; color: #222; }
  .cheat-print-btn { display: none; }
  .cheat-item { color: #222; }
  .cheat-item::before { color: #16a34a; }
}
body.light .mistakes-card { background: rgba(251,191,36,0.06); }
body.light .cheat-section { background: #f8f9fa; }
'''

# === JS to inject ===
NEW_JS = '''
// === 3.3: Font size toggle ===
(function() {
  var saved = localStorage.getItem('prg-font-size') || 'md';
  if (saved !== 'md') document.body.classList.add('font-' + saved);
  document.addEventListener('click', function(e) {
    if (!e.target.classList.contains('font-btn')) return;
    var size = e.target.getAttribute('data-size');
    document.body.classList.remove('font-sm', 'font-lg');
    if (size !== 'md') document.body.classList.add('font-' + size);
    localStorage.setItem('prg-font-size', size);
    var btns = document.querySelectorAll('.font-btn');
    for (var i = 0; i < btns.length; i++) btns[i].classList.toggle('active', btns[i].getAttribute('data-size') === size);
  });
  // Set initial active
  var btns = document.querySelectorAll('.font-btn');
  for (var i = 0; i < btns.length; i++) btns[i].classList.toggle('active', btns[i].getAttribute('data-size') === saved);
})();

// === 4.1: Print cheat sheet ===
document.addEventListener('click', function(e) {
  if (!e.target.classList.contains('cheat-print-btn')) return;
  window.print();
});
'''


def get_lesson_key(filename):
    """Extract lesson key from filename like '01_variables.html'"""
    return filename.replace('.html', '')


def build_mistakes_html(key):
    """Build the common mistakes card HTML for a lesson."""
    mistakes = MISTAKES.get(key, [])
    if not mistakes:
        return ''
    items = []
    for m in mistakes:
        items.append(f'<div class="mistake-item"><span class="mistake-title">{m["title"]}</span> — <span class="mistake-desc">{m["desc"]}</span></div>')
    return (
        '<div class="mistakes-card">\n'
        '  <div class="mistakes-label">COMMON MISTAKES — よくある間違い</div>\n'
        + '\n'.join(items) + '\n'
        '</div>'
    )


def build_cheat_html(key):
    """Build the cheat sheet section HTML for a lesson."""
    cs = CHEAT_SHEETS.get(key, None)
    if not cs:
        return ''
    items = []
    for p in cs['points']:
        items.append(f'<li class="cheat-item">{p}</li>')
    return (
        '<div class="cheat-section">\n'
        '  <div class="cheat-header">\n'
        '    <div class="cheat-label">CHEAT SHEET — まとめ</div>\n'
        '    <button class="cheat-print-btn" type="button">PDFとして印刷</button>\n'
        '  </div>\n'
        f'  <div class="cheat-concept">{cs["concept"]}</div>\n'
        '  <ul class="cheat-list">\n'
        + '\n'.join(items) + '\n'
        '  </ul>\n'
        '</div>'
    )


def build_font_controls():
    """Build font size control buttons HTML."""
    return (
        '<div class="font-controls">'
        '<button class="font-btn" type="button" data-size="sm" aria-label="小さい文字">A</button>'
        '<button class="font-btn active" type="button" data-size="md" aria-label="標準文字">A</button>'
        '<button class="font-btn" type="button" data-size="lg" aria-label="大きい文字">A</button>'
        '</div>'
    )


def process_file(filepath):
    """Apply all 3 improvements to a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    key = get_lesson_key(filename)
    changed = False

    # === 1.2: Common mistakes card ===
    if 'mistakes-card' not in content:
        mistakes_html = build_mistakes_html(key)
        if mistakes_html:
            # Insert after concept-card + usage-badge, before code stepper section
            match = re.search(r'(<div class="usage-badge">.*?</div>)\s*(<section\s+style)', content, re.DOTALL)
            if match:
                content = content[:match.start(2)] + mistakes_html + '\n\n' + content[match.start(2):]
                changed = True

    # === 4.1: Cheat sheet section ===
    if 'cheat-section' not in content:
        cheat_html = build_cheat_html(key)
        if cheat_html:
            # Insert before nav-footer
            match = re.search(r'(<div class="nav-footer">)', content)
            if match:
                content = content[:match.start(1)] + cheat_html + '\n\n' + content[match.start(1):]
                changed = True

    # === 3.3: Font size controls ===
    if 'font-controls' not in content:
        font_html = build_font_controls()
        # Insert inside header-controls, after theme-toggle button
        match = re.search(r'(<button class="theme-toggle"[^>]*></button>)', content)
        if match:
            content = content[:match.end(1)] + ' ' + font_html + content[match.end(1):]
            changed = True

    # === Inject CSS ===
    if '/* === 1.2: Common mistakes card === */' not in content:
        content = content.replace('</style>', NEW_CSS + '\n</style>')
        changed = True

    # === Inject JS ===
    if '// === 3.3: Font size toggle ===' not in content:
        content = content.replace('</script>', NEW_JS + '\n</script>')
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    dirs = [
        '01_basics/interactive',
        '02_python_syntax/interactive'
    ]
    total = 0
    updated = 0
    for d in dirs:
        full = os.path.join('.', d)
        if not os.path.isdir(full):
            continue
        for f in sorted(os.listdir(full)):
            if not f.endswith('.html'):
                continue
            total += 1
            path = os.path.join(full, f)
            if process_file(path):
                updated += 1
                print(f'  Updated: {path}')
            else:
                print(f'  Skipped: {path}')
    print(f'\nDone: {updated}/{total} files updated')


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()

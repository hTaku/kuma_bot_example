# kuma_bot_example
クマ出現Bot

# 使用言語／ライブラリ
言語：Python
ライブラリ：requests/bs4/selenium/chromedriver

pip install bs4
pip install selenium
pip install chromedriver-binary==chromeのバージョン

# 動作概要
丸森町の安心安全メール掲載サイトからクマ出没の投稿をスクレーピングし、Line Notifyに投稿する。

# 動作方法
1. LINE NotifyとLINEで友だちになる

2. LINE Notifyからアクセストークンを取得する。
https://notify-bot.line.me/ja/

3. 取得したLINE Notifyのアクセストークンをsettings。pyのACCESS_TOKENに記載する。

4. 以下のコマンドで実行する。
python kuma_bot.py
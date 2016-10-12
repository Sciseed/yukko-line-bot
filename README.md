# yukko-line-bot
PythonとLINE Messaging APIを用いたChatbotの実装サンプルです。  
ユーザーとLINE上で雑談することができます。  
おしゃべり機能にはdocomo雑談対話APIを、Q&A機能にdocomo知識Q&AAPIを使用しています。
#環境構成
Python 3.4.0  
LINEからメッセージを送信するとLINE Messaging APIがHeroku上のDjangoサーバーを叩き、yukko-line-botがLINE Messaging APIにレスポンスを返し、LINEに表示されます。
##License
*LICENSE
[MIT](https://github.com/Sciseed/yukko-line-bot/blob/master/LICENSE.txt)
#必要なもの
・docomo APIアカウント  
・LINE Businessアカウント
#導入手順
###yukko-line-botをローカルにクローン  
`git clone git@github.com:Sciseed/yukko-line-bot.git`  
`cd yukko-line-bot`  
###ローカルでyukko-line-botを起動して動作を確認
####仮想環境構築
`source virenv/bin/activate`  
virenv/はvirtualenvが入っているディレクトリです。自身の環境に合わせて参照してください  
`python manage.py runserver`  
ローカルサーバーにGETリクエストを送ってみる  
`curl -X GET http://127.0.0.1:8000/callback`  
{"Successfully": "Connected!"}  
と返されたら成功  
###herokuにデプロイ  
herokuアプリの詳しい作成手順(https://gist.github.com/konitter/5370904)
`heroku create`  
`git push heroku master`  
###デプロイされたかチェックする。  
ブラウザで  
https://xxxxxxx.herokuapp.com/callback  
にアクセス（'xxxxxxx'はアプリ名）  
{"Successfully": "Connected!"}と表示されれば正しく動いています。  
###認証情報を設定  
bot/views.pyの
docomo API KeyとLINEのAuthorizatinoを自分のものに書き換えます。  
###callback URLを設定  
LINE developerからwebhook URLに  
`https://xxxxxxx.herokuapp.com/callback`  
を設定する。  
#Qiita
LINE Messaging APIとPythonを使ってChatbotを作ってみた  
http://qiita.com/Kosuke-Szk/items/eea6457616b6180c82d3
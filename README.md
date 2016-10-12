# yukko-line-bot
LINE Messaging APIを用いたChatbotです。
おしゃべり機能にはdocomo雑談対話APIを、Q&A機能にdocomo知識Q&AAPIを使用しています。
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
`python manage.py runserver`  
ローカルサーバーにGETリクエストを送ってみる  
`curl -X GET http://127.0.0.1:8000/callback`  
{"Successfully": "Connected!"}  
と返されたら成功  
###herokuにデプロイ  
`heroku create`  
`git push heroku master`  
###デプロイされたかチェックする。  
ブラウザで  
https://xxxxxxx.herokuapp.com/callback  
にアクセス（'xxxxxxx'はアプリ名）  
{"Successfully": "Connected!"}と表示されれば正しく動いています。  
###認証情報を設定  
docomo API KeyとLINEのAuthorizatinoを自分のものに書き換えます。  
###callback URLを設定  
LINE developerからwebhook URLに  
`https://xxxxxxx.herokuapp.com/callback`  
を設定する。  
#Qiita
http://qiita.com/Kosuke-Szk/items/eea6457616b6180c82d3
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
###作業スペースを作成  
`mkdir workspace`  
`cd workspace`  
###yukko-line-botをローカルにクローン  
`git clone git@github.com:Sciseed/yukko-line-bot.git`  
`cd yukko-line-bot`  
###herokuにデプロイ  
`heroku create`  
`git push heroku master`  
###デプロイされたかチェックする。  
ブラウザで  
https://xxxxxxx.herokuapp.com/callback  
にアクセス（'xxxxxxx'はアプリ名）  
{"": ""}と表示されれば正しく動いています。  
###認証情報を設定  
docomo API KeyとLINEのAuthorizatinoを自分のものに書き換えます。  
###callback URLを設定  
LINE developerからwebhook URLに  
`https://xxxxxxx.herokuapp.com/callback`  
を設定する。  
#Qiita
http://qiita.com/Kosuke-Szk/items/eea6457616b6180c82d3
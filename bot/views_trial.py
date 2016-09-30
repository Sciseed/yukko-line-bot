#Messaging API版エンドポイント
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

def post_text(reply_token, text):
  #Messaging API版ヘッダー
    header = {
        'Content-Type: application/json',
        'Authorization: Bearer {CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU=}',
    }
    output = mecab_test.make_output(content)
    payload_text = ''.join(output)
    payload = {
          'replyToken':reply_token,
          'message':[
              {
                'type': 'text',
                'text': payload_text
              }
          ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=headers, data=json.dumps(payload))

#Messaging API版
def dispose(events):
  for event in events:
    reply_token = event['replyToken']
    event_type = event['type']
    user_id = event['source']['userId']
    response_to_talk(reply_token, event)

#Messaging API
def response_to_talk(reply_token, event):
  text = event['message']['text']
  post_text(reply_token, text)

      #Messaging API版
      dispose(json.loads(request.body.decode('utf-8'))['events'])
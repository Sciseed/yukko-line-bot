from django.http.response import HttpResponse
from django.shortcuts import render
import os
import json
import random
import doco.client
import requests
from django.http import JsonResponse
from django.views.generic import View
import urllib
import editdistance
from bot import mecab_test

ENDPOINT = 'https://trialbot-api.line.me/v1/events'
DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'
EVENT_REGISTER = '138311609100106403'
EVENT_TALK = '138311609000106303'
DOCOMO_ENDPOINT = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
MIZU_ENDPOINT = 'http://myconcierlb-708356017.us-west-2.elb.amazonaws.com:9000/api/ask'

def post_text(send_to, content):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': "1480426345",
        'X-Line-ChannelSecret': '37df4c7d811276edf33c741471f9f906',
        'X-Line-Trusted-User-With-ACL': 'ufbb1954b3357ab82f558b1e695096212'
    }
    #雑談
    # docomo_client = doco.client.Client(apikey=DOCOMO_API_KEY)
    # docomo_res = docomo_client.send(utt=content,apiname='Dialogue')
    # options = {
    #   'APIKEY': '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33',
    #   'q': content
    # }
    # docomo_res_q = json.loads(requests.get(DOCOMO_ENDPOINT, params=options).text)
    #q = {'q': content}
    #mizu_res = json.loads(requests.get(MIZU_ENDPOINT, params=q).text) #qに対するaが返される
    # 編集距離を算出
    # print('line44')
    # q_user_li = janome_morpheme(q['q'])
    # print('after line44')
    # for res in mizu_res[0]['q']:
    #   res_li = janome_morpheme(res)
    #   distance_li = editdistance.eval(q_user_li, res_li)

    # print('line 51')
    # print(distance_li)

    # if mizu_res != []:
    #       output = mizu_res[0]['a'][0]
    # elif 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
    #     output = docomo_res['utt']
    # else:
    #     output = docomo_res_q['message']['textForDisplay']
    # output = make_output(content)
    # if 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
    #     output = docomo_res['utt']
    # else:
    #     output = docomo_res_q['message']['textForDisplay']
    print(content)
    output = mecab_test.make_output(content)
    payload = {
        'toChannel': 1383378250,
        'eventType': '138311608800106203',
        'to': send_to,
        'content': {
           "contentType":1,
           "toType":1,
           "text": output
        }
    }
    print('request')
    print(payload['content']['text'])
    req = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))
    # print (json.dumps(payload))
    # print (json.dumps(headers))

    #print(req.__dict__)

def post_question(send_to, question):
    options = {
    'APIKEY': '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33',
    'q': question
    }
    docomo_res = json.loads(requests.get(DOCOMO_ENDPOINT, params=options).text)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': "1480426345",
        'X-Line-ChannelSecret': '37df4c7d811276edf33c741471f9f906',
        'X-Line-Trusted-User-With-ACL': 'ufbb1954b3357ab82f558b1e695096212'
    }
    payload = {
    'toChannel': 1383378250,
    'eventType': '138311608800106203',
    'to': send_to,
    'content': {
       "contentType":1,
       "toType":1,
       "text":docomo_res['message']['textForDisplay'],
       }
    }
    print('post_question')
    req = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))
    print (json.dumps(payload))
    print (json.dumps(headers))
    print('request')
    print(req.__dict__)

def post_sticker(send_to):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': "1480426345",
        'X-Line-ChannelSecret': '37df4c7d811276edf33c741471f9f906',
        'X-Line-Trusted-User-With-ACL': 'ufbb1954b3357ab82f558b1e695096212'
    }
    payload = {
        'toChannel': 1383378250,
        'eventType': '138311608800106203',
        'to': send_to,
        'content': {
           "contentType":8,
           "toType":1,
           "contentMetadata":{
             "STKID":"1",
             "STKPKGID":"1",
             "STKVER":"100"
           }
        }
    }
    req = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))
    print (json.dumps(payload))
    print (json.dumps(headers))
    print('request')
    print(req.__dict__)

def post_image(send_to):
    print("this is image requests")
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': "1480426345",
        'X-Line-ChannelSecret': '37df4c7d811276edf33c741471f9f906',
        'X-Line-Trusted-User-With-ACL': 'ufbb1954b3357ab82f558b1e695096212'
    }
    payload = {
         "to":send_to,
         "toChannel":1383378250,
         "eventType":"138311608800106203",
         "content":{
           "contentType":2,
           "toType":1,
           "originalContentUrl":"http://koebu.com/images/topic/8/8d/8d52/8d527791877c8b394fabaca0b16bbf74eb044aae.png",
           "previewImageUrl":"http://koebu.com/images/topic/8/8d/8d52/8d527791877c8b394fabaca0b16bbf74eb044aae.png"
  }
}

    req = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))

def response_to_register(send_to):
  user_name = get_user_name(send_to[0])
  text = '{0}さん、はじめまして！'.format(user_name.encode('utf-8'))
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Line-ChannelID': "1480426345",
    'X-Line-ChannelSecret': '37df4c7d811276edf33c741471f9f906',
    'X-Line-Trusted-User-With-ACL': 'ufbb1954b3357ab82f558b1e695096212'
  }
  payload = {
      'toChannel': 1383378250,
      'eventType': '138311608800106203',
      'to': send_to,
      'content': {
         "contentType":1,
         "toType":1,
         "text":text,
      }
  }
  requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))


def dispose(results):
  for result in results:
    event_type = result['eventType']
    if event_type == EVENT_REGISTER:
      send_to = [result['content']['params'][0]]
      operation_type = result['content']['onType']
      if int(operation_type) == 4:
        response_to_register(send_to)
    elif event_type == EVENT_TALK:
      send_to = [result['content']['from']]
      response_to_talk(send_to, result)

def response_to_talk(send_to, result):
    content_type = result['content']['contentType']
    text = result['content']['text']
    print(content_type)
    if content_type == 1:
       print("this is text request")
       if('みお' in result['content']['text']):
              post_image(send_to)
       else:
              post_text(send_to, text)
    elif content_type == 8:
       print("this is sticker request")
       post_sticker(send_to)
    else:
       print("this require me to send image")
       post_image(send_to)

def janome_morpheme(sentence):
  t = Tokenizer()
  tokens = t.tokenize(sentence)
  li = [token.surface for token in tokens]
  return li

def post_test(request):
  return render(request, 'post_test.html')

class HelloView(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        return JsonResponse({'suzuki':'kosuke'})

    def post(self, request, *args, **kwargs):
      dispose(json.loads(request.body.decode("utf-8"))['result'])
      return JsonResponse({'kosuke': 'suzuki'})
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
from bot import create_answer

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'
EVENT_REGISTER = '138311609100106403'
EVENT_TALK = '138311609000106303'
DOCOMO_ENDPOINT = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
MIZU_ENDPOINT = 'http://myconcierlb-708356017.us-west-2.elb.amazonaws.com:9000/api/ask'

def post_text(reply_token, text):
    print("enter post text")
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer rrlbmMP4gH0kCdQFinWHscLBKEwKWNVITHjEBjnC+x3BMBa3QC2P+s5QjvK4LDJ/sF+IYKpGL/cu9GZAisaJSdvU7fVkapN7ynV/dg3b/z8E5IrfTWIa0ovmrlUA4L4NLpXmcRzgeoIWcWHJ0ZrEFwdB04t89/1O/w1cDnyilFU="

    }
    output = create_answer.make_output(text)
    payload_text = ''.join(output)
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": payload_text
                }
            ]
    }

    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def post_carousel(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer rrlbmMP4gH0kCdQFinWHscLBKEwKWNVITHjEBjnC+x3BMBa3QC2P+s5QjvK4LDJ/sF+IYKpGL/cu9GZAisaJSdvU7fVkapN7ynV/dg3b/z8E5IrfTWIa0ovmrlUA4L4NLpXmcRzgeoIWcWHJ0ZrEFwdB04t89/1O/w1cDnyilFU="

    }
    payload = {
          "replyToken":reply_token,
          "messages":[
              {
                "type": "template",
                "altText": "おすすめレストラン",
                "template": {
                    "type": "carousel",
                    "columns": [

                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg",
                          "title": "ジャンク・バーガー",
                          "text": "誰が何と言おうとジャンクフードの王様は、今も昔も変わらずハンバーガー。",
                          "actions": [

                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/pizza_240.jpeg",
                          "title": "pizza cap",
                          "text": "本場ナポリの味を早く、安く。都内に17店舗展開するピザ専門店です。",
                          "actions": [
                          
                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/bread_240.jpeg",
                          "title": "本格パン工房 たけよし",
                          "text": "パンにとって一番大事だと思うものはなんですか？たけよしは、表面の焼き上がりこそが命であると考えています。",
                          "actions": [
                          
                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/harumaki_240.jpeg",
                          "title": "ヴェトナムTokyo",
                          "text": "東池袋にあるしたベトナム料理の老舗。40年以上人々に愛され続けてきたベトナム料理をご提供します。",
                          "actions": [
                          
                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
           
                    ]
                }
              }
            ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def post_confirm(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer rrlbmMP4gH0kCdQFinWHscLBKEwKWNVITHjEBjnC+x3BMBa3QC2P+s5QjvK4LDJ/sF+IYKpGL/cu9GZAisaJSdvU7fVkapN7ynV/dg3b/z8E5IrfTWIa0ovmrlUA4L4NLpXmcRzgeoIWcWHJ0ZrEFwdB04t89/1O/w1cDnyilFU="
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
            {
              "type": "template",
              "altText": "this is a confirm template",
              "template": {
                  "type": "confirm",
                  "text": "男性ですか？女性ですか？",
                  "actions": [
                      {
                        "type": "message",
                        "label": "Man",
                        "text": "男性"
                      },
                      {
                        "type": "message",
                        "label": "Woman",
                        "text": "女性"
                      }
                  ]
              }
            }
          ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))


def post_imagemap(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
            {
              "type": "imagemap",
              "baseUrl": "http://blogimg.goo.ne.jp/user_image/03/1f/d4a55e24e0cd7993539025c25fe426b8.jpg",
              "altText": "this is an imagemap",
              "baseSize": {
                  "height": 1040,
                  "width": 1040
              },
              "actions": [
                  {
                      "type": "uri",
                      "linkUri": "https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%90",
                      "area": {
                          "x": 0,
                          "y": 0,
                          "width": 520,
                          "height": 1040
                      }
                  },
                  {
                      "type": "message",
                      "text": "焼きそばだよ！！！！！",
                      "area": {
                          "x": 520,
                          "y": 0,
                          "width": 520,
                          "height": 1040
                      }
                  }
              ]
            }
          ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def dispose(events):
  print('This is dispose request')
  for event in events:
    reply_token = event['replyToken']
    event_type = event['type']
    user_id = event['source']['userId']
    response_to_talk(reply_token, event)

def response_to_talk(reply_token, event):
  print("enter response to talk")
  text = event['message']['text']
  if ('レストラン' in text or 'ランチ' in text or 'ディナー' in text or '食べ物' in text) and ('おすすめ' in text or '教えて' in text):
    post_carousel(reply_token)
  else:
    post_text(reply_token, text)

class ViewSet(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
      return JsonResponse({'Successfully': 'Connected!'})

    def post(self, request, *args, **kwargs):
      dispose(json.loads(request.body.decode("utf-8"))['events'])
      return JsonResponse({'': ''})
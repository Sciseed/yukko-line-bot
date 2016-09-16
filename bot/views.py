from django.http.response import HttpResponse
from django.shortcuts import render
#from . import forms
import os
import json
import random
import base64
import hashlib
import binascii
import logging
import doco.client

import requests
from django.http import JsonResponse
from django.views.generic import View

ENDPOINT = 'https://trialbot-api.line.me/v1/events'
DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'

logger = logging.getLogger('command')

def post_text(send_to, content):
    user = {'t': 20}
    docomo_client = doco.client.Client(apikey=DOCOMO_API_KEY, user=user)
    docomo_res = docomo_client.send(utt=content,apiname='Dialogue')
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
           "text":docomo_res['utt'],
        }
    }
    print('request')
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

def dispose(results):
  print("this is dispose request")
  for result in results:
    event_type = result['eventType']
    send_to = [result['content']['from']]
    text = result['content']['text']
    content_type = result['content']['contentType']
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


def post_test(request):
  return render(request, 'post_test.html')

class HelloView(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        return JsonResponse({'suzuki':'kosuke'})

    def post(self, request, *args, **kwargs):
      print('done post method')
      dispose(json.loads(request.body.decode("utf-8"))['result'])
      return JsonResponse({'kosuke': 'suzuki'})
#coding: utf-8

import sys
import json
import requests
import editdistance
import doco.client
import pandas
import codecs
import csv

DOCOMO_ENDPOINT = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
MIZU_ENDPOINT = 'http://myconcierlb-708356017.us-west-2.elb.amazonaws.com:9000/api/ask'
DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'


def make_output(content):
  #ユーザーの入力をqに格納
  q = {'q': content}
  docomo_client = doco.client.Client(apikey=DOCOMO_API_KEY)
  #入力をdocomo apiに投げる
  docomo_res = docomo_client.send(utt=content,apiname='Dialogue')
  #入力をdocomo api Q&Aに投げる
  options = {
  'APIKEY': '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33',
  'q': content
  }
  docomo_res_q = json.loads(requests.get(DOCOMO_ENDPOINT, params=options).text)
  mizu_res = []
  #outputの選択
  if mizu_res != [] and mizu_res[0]['a'] != []:
        output = mizu_res[0]['a']
  elif 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
      output = [docomo_res['utt']]
  else:
      output = [docomo_res_q['message']['textForDisplay']]
  return output
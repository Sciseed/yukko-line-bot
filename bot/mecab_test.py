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
  #入力をMIZU APIに投げる→回答リストを取得
  try:
    print(requests.get(MIZU_ENDPOINT, params=q).text)
    mizu_res = json.loads(requests.get(MIZU_ENDPOINT, params=q).text)
  except:
    print('mizu_res : value error')

  #outputの選択
  if mizu_res != [] and mizu_res[0]['a'] != []:
        output = mizu_res[0]['a']
  elif 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
      output = [docomo_res['utt']]
  else:
      output = [docomo_res_q['message']['textForDisplay']]

  return output

# def mecab_morpheme(sentence):
#   m = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
#   wakati = m.parse(sentence)
#   li = wakati.split(' ')
#   return li

# def janome_morpheme(sentence):
#   t = Tokenizer()
#   tokens = t.tokenize(sentence)
#   li = [token.surface for token in tokens]
#   return li

# def input_csv_to_automaton(csv_file):
#   with codecs.open(csv_file, "r", "Shift-JIS", "ignore") as file:
#     df = pandas.read_table(file, delimiter=",")
#     for script in df['script']:
#       flag = automaton.make_flag(script)
#       print(flag)

# def input_automaton_to_csv(csv_file):
#   with codecs.open(csv_file, "r", "Shift-JIS", "ignore") as file:
#     df = pandas.read_table(file, delimiter=",")
#     for script in df['script']:
#       flag = automaton.make_flag(script)

# def print_csv(csv_file):
#   with codecs.open(csv_file, "r", "Shift-JIS", "ignore") as file:
#     df = pandas.read_table(file, delimiter=",")
#     print(df['script'])

def output_csv(csv_file):
  with codecs.open(csv_file, "r", "utf-8", "ignore") as file:
    df = pandas.read_table(file, delimiter=",")
    g = open('result_recent_message.csv', 'w')
    writer = csv.writer(g)
    for script in df.iloc[:,1]:
      flag = cross_layer.make_flag(script)
      writer.writerow(flag)
    g.close()

if __name__ == '__main__':
  output_csv('recent_message_list.csv')

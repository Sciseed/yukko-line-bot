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
MIZU_ENDPOINT = 'http://ec2-52-40-78-63.us-west-2.compute.amazonaws.com:8001/api/ask'
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
    mizu_res = json.loads(requests.get(MIZU_ENDPOINT, params=q).text)
  #   #質問を形態素解析して単語ごとにリスト化
  #   #q_user_li = janome_morpheme(q['q'])
  #   answerType_q = automaton.make_flag(q['q'])
  #   distance_li = []
  #   sentaku_list = []
  #   aaa_list = []
  #   kotae_list = []
  #   for k in mizu_res:
  #     for res in k['q']:
  #       print(res)
  #       answerType_res = automaton.make_flag(res)
  #       if answerType_res == answerType_q:
  #         sentaku_list.append(res)
  #         aaa_list.append(1)
  #       else:
  #         aaa_list.append(0)
  #       #回答の要素を形態素解析
  #       # res_li = janome_morpheme(res)
  #       # print(res_li)
  #       # distance = editdistance.eval(q_user_li, res_li)
  #       # distance_li.append(distance)
  #     #編集距離最短のindexを取得
  #     # print(distance_li)
  #     # n = distance_li.index(min(distance_li))
  #     # min_dis_ans = mizu_res[0]['a'][n]
  #   j = 0
  #   for kkk in aaa_list:
  #     if kkk == 1:
  #       kotae_list.append(mizu_res[j]['a'])
  #       j += 1
  #     else:
  #       j += 1
  #       continue

  #   print(kotae_list)
  except:
    print('mizu_res : value error')

  #outputの選択
  if mizu_res != []:
        output = mizu_res[0]['a']
  elif 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
      output = docomo_res['utt']
  else:
      output = docomo_res_q['message']['textForDisplay']

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

# def output_csv(csv_file):
#   with codecs.open(csv_file, "r", "utf-8", "ignore") as file:
#     df = pandas.read_table(file, delimiter=",")
#     g = open('result_recent_message.csv', 'w')
#     writer = csv.writer(g)
#     for script in df.iloc[:,1]:
#       flag = cross_layer.make_flag(script)
#       writer.writerow(flag)
#     g.close()


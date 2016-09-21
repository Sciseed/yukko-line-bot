import sys
from janome.tokenizer import Tokenizer
import json
import requests
import editdistance
import doco.client

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
  #入力をMIZU APIに投げる→回答リストを取得
  mizu_res = json.loads(requests.get(MIZU_ENDPOINT, params=q).text)
  #質問を形態素解析して単語ごとにリスト化
  q_user_li = janome_morpheme(q['q'])
  print(q_user_li)
  for res in mizu_res[0]['q']:
    #回答の要素を形態素解析
    res_li = janome_morpheme(res)
    print(res_li)
    distance = editdistance.eval(q_user_li, res_li)
    distance_li = []
    distance_li.append(distance)
  #編集距離最短のindexを取得
  return distance_li
  # n = distance_li.index(min(distance_li))
  # min_dis_ans = mizu_res[0]['q'][n]

  # #outputの選択
  # if mizu_res != []:
  #       output = min_dis_ans
  # elif 'わかりませんでした' in docomo_res_q['message']['textForDisplay']:
  #     output = docomo_res['utt']
  # else:
  #     output = docomo_res_q['message']['textForDisplay']

  # return output

def janome_morpheme(sentence):
  t = Tokenizer()
  tokens = t.tokenize(sentence)
  li = [token.surface for token in tokens]
  return li

if __name__ == "__main__":
  content = "インターンって何ですか？"
  output = make_output(content)
  print(output)
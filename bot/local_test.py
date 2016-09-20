import doco.client
import urllib.parse
import requests
import json


DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'
DOCOMO_ENDPOINT = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'


#questionをURLエンコード
urllib.parse.urlencode({'q': "富士山の高さは"})

# docomo_client = doco.client.Client(apikey=DOCOMO_API_KEY)
# docomo_res = docomo_client.send(q='',apiname='Dialogue')
options = {
'APIKEY': '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33',
'q': '%E4%BA%BA%E9%A1%9E%E5%88%9D%E3%81%AE%E5%AE%87%E5%AE%99%E9%A3%9B%E8%A1%8C%E5%A3%AB%E3%81%AF'
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
    'to': {},
    'content': {
       #"contentType":1,
       "toType":1,
       "text": docomo_res['message']['textForDisplay'],
    }
}
print(payload['content']['text'])
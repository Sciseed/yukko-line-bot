import MeCab
from collections import defaultdict

def analyze(txt):
  m = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
  return m.parse(txt)

def dicnize(txt):
    buf = txt.split("\n")
    dics = list(filter(lambda x: x, map(lambda x: texts2dic(x.split()), buf)))
    return dics


def texts2dic(txt_list):
    if len(txt_list) < 4:
        return None

    morph_dic = {}
    morph_dic["surface"] = txt_list[0]
    morph_dic["pronunce"] = txt_list[1]
    morph_dic["base"] = txt_list[2]
    poses = txt_list[3].split("-")
    morph_dic["pos"] = poses[0]
    if len(poses) > 1:
        morph_dic["pos1"] = poses[1]
    if len(poses) > 2:
      morph_dic["pos2"] = poses[2]
    else:
      morph_dic["pos2"] = ""
    return morph_dic

def ngram(sentence, n):
  m = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
  results = []
  words = m.parse(sentence).split()
  if len(words) >= n:
    for i in range(len(words)-n+1):
      results.append(words[i:i+n])
  return results

def check_register(sentence, middle_output):
  if '大学' in sentence:
    if '学部' in sentence:
      middle_output = 'Register'
    elif '修士' in sentence:
      middle_output = 'Register'
    elif '専攻' in sentence:
      middle_output = 'Register'
    elif '4年' in sentence:
      middle_output = 'Register'
    elif '3年' in sentence:
      middle_output = 'Register'
    elif '2年' in sentence:
      middle_output = 'Register'
    elif '1年' in sentence:
      middle_output = 'Register'
    elif '回' in sentence:
      middle_output = 'Register'
    elif '研究科' in sentence:
      middle_output = 'Register'
  return middle_output

def check_campaign(word, middle_output):
  if word in campaign_list:
    middle_output = 'キャンペーン'
  return middle_output

def check_event(word, middle_output):
  if word in event_list:
    middle_output = 'イベント'
  return middle_output

def get_name(word_pos2):
  if word_pos2 == '名前':
    return True
  else:
    return False

shukatsu_list = ['就活', '就職活動']
kigyo_list = ['企業', '会社', '本社', 'ベンチャー', '大手', '中小']
internship_list = ['インターン', 'インターンシップ']
shigoto_list = ['仕事', '業務', '職種']
gyokai_list = ['業界', '業種']
advice_list = ['アドバイス']
how_list = ['どう', 'やり方', 'やりかた', '仕方', 'アドバイス']
prepare_list = ['準備', '用意']
myself_list = ['自分', 'じぶん', '私', 'わたし', '僕', 'ぼく']
campaign_list = ['キャンペーン', '商品券']
event_list = ['イベント']
honorific_list = ['さん', '様', 'くん', '君']
s1_list = ['軸']
s2_list = ['内定辞退', '辞退']
s3_list = ['試験', 'SPI', 'Webテスト', 'webテスト', 'WEBテスト', 'ウェブテスト', 'SPI']
s4_list = ['自己分析']
s5_list = ['内定']
s6_list = ['面接', 'グループ面接', '面談', '個人面接', '1次面接', '2次面接', '最終面接']
s7_list = ['ES', 'エントリーシート']
s8_list = ['リクルーター','リクルータ']
s9_list = ['分析']
s10_list = ['モチベーション']
s11_list = ['スケジュール']
s12_list = ['自己PR']
s13_list = ['選考']
s14_list = ['逆質問', '質問']
s15_list = ['企業研究', '業界研究']
s16_list = ['合う', '活かす']
s17_list = ['専攻']
s18_list = ['興味']
s19_list = ['GD', 'グループディスカッション']
s20_list = ['絞る', '選ぶ']
l1_list = ['何', 'なに']
l2_list = ['いつ']
l3_list = ['どこで']
l4_list = ['なぜ']
l5_list = ['どう', '方法', '仕方', 'やり方', 'アドバイス', '対策', 'コツ']
l6_list = ['教える', 'おしえる', '悩む','悩み']

#bigram
bs1_list = [['やり', 'たい']]

bl2_list = [['何','時']]
bl6_list = [['わかる', 'ない']]

no_meaning_list = ['ありがとう', 'はい', '了解', 'りょうかい', 'よろしく', 'よろしくお願いします', 'わかる', 'お願い', 'なるほど', 'こんにちは', 'こんばんは', 'すみません', 'すいません', 'かしこまる', 'はじめまして', '大丈夫', 'おはよう', 'こんにちわ', '理解']

def make_flag(sentence):
  status_list = []
  name_list = []
  first_output = 'xxx'
  middle_output = 'xxx'
  last_output = 'xxx'
  morph = analyze(sentence)
  morph_dics = dicnize(morph)
  #first層での分類
  for x in morph_dics:
    key = x['base']
    if key in shukatsu_list:
      status_list.extend(['s1','s4', 's5', 's10', 's11'])
      first_output = '就活'
    if key in kigyo_list:
      status_list.extend(['s1', 's2','s4', 's5', 's6', 's9', 's14','s15', 's18', 's20', 'bs1'])
      first_output = '企業'
    if key in internship_list:
      status_list.extend(['s7', 's19'])
      first_output = 'インターン'
    if key in shigoto_list:
      status_list.extend(['s1','s4', 's10', 's18', 'bs1'])
      first_output = '仕事'
    if key in gyokai_list:
      status_list.extend(['s1', 's9'])
      first_output = '業界'
    if key in prepare_list:
      status_list.extend(['s3', 's6', 's14'])
      first_output = '準備'
    if key in myself_list:
      status_list.extend(['s16', 's18', 'bs1'])
      first_output = '自分'
    else: continue
  # print(status_list)
  morph_dics = dicnize(morph)
  #first層を踏まえたmiddle層の分類
  for y in morph_dics:
    key = y['base']
    if 's1' in status_list:
      if key in s1_list:
        middle_output = "軸"
    if 's2' in status_list:
      if key in s2_list:
        middle_output = "内定辞退"
    if 's3' in status_list:
      if key in s3_list:
        middle_output = "試験"
    if 's4' in status_list:
      if key in s4_list:
        middle_output = "自己分析"
    if 's5' in status_list:
      if key in s5_list:
        middle_output = "内定"
    if 's6' in status_list:
      if key in s6_list:
        middle_output = "面接"
    if 's7' in status_list:
      if key in s7_list:
        middle_output = "ES"
    if 's8' in status_list:
      if key in s8_list:
        middle_output = "リクルーター"
    if 's9' in status_list:
      if key in s9_list:
        middle_output = "分析"
    if 's10' in status_list:
      if key in s10_list:
        middle_output = "モチベーション"
    if 's11' in status_list:
      if key in s11_list:
        middle_output = "就活の進め方"
    if 's12' in status_list:
      if key in s12_list:
        middle_output = "自己PR"
    if 's13' in status_list:
      if key in s13_list:
        middle_output = "選考"
    if 's14' in status_list:
      if key in s14_list:
        middle_output = "逆質問"
    if 's15' in status_list:
      if key in s15_list:
        middle_output = "企業研究"
    if 's16' in status_list:
      if key in s16_list:
        middle_output = "自己分析"
    if 's18' in status_list:
      if key in s18_list:
        middle_output = "自己分析"
    if 's19' in s19_list:
      if key in s19_list:
        middle_output = "GD"
    if 's20' in status_list:
      if key in s20_list:
        middle_output = "企業研究"
    #middle層で選抜可能なものは以下に記載
    elif key in s1_list:
      middle_output = "軸"
    elif key in s2_list:
      middle_output = "内定辞退"
    elif key in s3_list:
      middle_output = "試験"
    elif key in s4_list:
      middle_output = "自己分析"
    elif key in s6_list:
      middle_output = "面接"
    elif key in s7_list:
      middle_output = "ES"
    elif key in s8_list:
      middle_output = "リクルーター"
    elif key in s15_list:
      middle_output = "企業研究"
    elif key in s19_list:
      middle_output = "GD"
    else: continue

  #bigramの判定
  bigram = ngram(sentence, 2)
  for by in bigram:
    if 'bs1' in status_list:
      if by in bs1_list:
        middle_output = "自己分析"
    else: continue
  morph_dics = dicnize(morph)
  #last層の分類
  for z in morph_dics:
    key = z['base']
    if key in l1_list:
      last_output = 'WHAT'
    if key in l2_list:
      last_output = 'WHEN'
    if key in l3_list:
      last_output = 'WHERE'
    if key in l4_list:
      last_output = 'WHY'
    if key in l5_list:
      last_output = 'HOW'
    if last_output == 'xxx':
      if key in l6_list:
        last_output = 'TEACH'
    else: continue

  bigram = ngram(sentence, 2)
  for bz in bigram:
    if bz in bl2_list:
      last_output = 'WHEN'
    if bz in bl6_list:
      last_output = 'TEACH'
    else: continue

  name =''
  name_list = []
  name_length_list = []
  callname = ''
  max_index = 0
  morph_dics = dicnize(morph)
  n = 0
  i = 0
  for word in morph_dics:
    before_word = morph_dics[n-1]
    n += 1
    middle_output = check_campaign(word['surface'], middle_output)
    # middle_output = check_event(word['surface'], middle_output)
    if word['pos2'] == '人名':
      if not word['surface'] in honorific_list:
        if i==0:
          callname = word['surface']
          i += 1
        if before_word['pos2'] == '人名':
          fullname = before_word['surface'] + word['surface']
          name_list.append(fullname)
    else:
      if not name:
        name = ''
      if not callname:
        callname = ''
  for l in name_list:
    name_length_list.append(len(l))
  # print(name_length_list)
  if name_length_list != []:
    max_index = name_length_list.index(max(name_length_list))
  else:
    max_index = -1
  if max_index != -1:
    name = name_list[max_index]
  else:
    name = callname

  # if name != '':
  #   nishida = sentence.replace(name, '◯◯')
  # else:
  #   nishida = ''

  if (first_output=='xxx')and(middle_output=='xxx')and(last_output=='xxx'):
    morph_dics = dicnize(morph)
    for x in morph_dics:
      key = x['base']
      if middle_output == 'xxx':
        if key in no_meaning_list:
          middle_output = 'No Meaning'
        else:
          continue

  if (middle_output=='xxx' or middle_output=='No Meaning'):
    morph_dics = dicnize(morph)
    for y in morph_dics:
      key = y['base']
      middle_output = check_register(sentence, middle_output)
  # if callname:
  #   print('こんにちは！%sさん' % callname)
  status_list = []
  return [first_output, middle_output, last_output, name, callname, sentence]

def rank_message_candidates(query, candidates):
  query_output = make_flag(query)
  weights = []
  for candidate in candidates:
    candidate_output = make_flag(candidate['q'][0])
    weights.append(dispose(query_output, candidate_output))
  output_index = weights.index(max(weights))
  candidates = candidates[output_index]
  print(candidates)
  return candidates


  #   candidate_output = make_flag(candidate[0]['q'])
  #   weights.append(dispose(query_output, candidate_output))
  # output_index = weights.index(max(weights))
  # candidates = candidates[output_index]

def dispose(question_output, stock_output):
  q_first = question_output[0]
  q_middle = question_output[1]
  q_last = question_output[2]
  s_first = stock_output[0]
  s_middle = stock_output[1]
  s_last = stock_output[2]
  weight = 0
  if q_first == s_first:
    weight += 1
  if q_middle == s_middle:
    weight += 2
  if q_last == s_middle:
    weight += 1
  return weight #sentenceごとに重みを付与
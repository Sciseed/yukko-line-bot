import MeCab
import sys

def main():
  sentence = input()
  flag = make_flag(sentence)
  print(flag)

def analyze(txt):
  m = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
  return m.parse(txt)

def dicnize(txt):
    buf = txt.split("\n")
    dics = filter(lambda x: x, map(lambda x: texts2dic(x.split()), buf))
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
    return morph_dic

def make_flag(sentence):
    morph = analyze(sentence)
    morph_dics = dicnize(morph)
    state = 'init'
    answertype = 'None'
    answertype_list = ['自己分析', '面接', '企業の探し方','企業研究', '試験', '就活', 'リクルーター', '内定辞退', '就活の時期と主にやること', '職種軸', '業種軸', '質問', '企業の強み']


    s1_list = ['自己分析', '仕事', 'キャリアプラン']
    s2_list = ['面接', '個人面接', 'グループ面接','グループ面談','一次面接', '二次面接']
    s3_list = ['企業研究', '業界研究']
    s4_list = ['試験', 'webテスト', 'ウェブテスト', '試験対策', '筆記試験', 'SPI', 'Webテスト']
    s5_list = ['就活']
    s6_list = ['リクルーター']
    s7_list = ['内定', '内定辞退']
    s8_list = ['就活', '就職活動']
    s9_list = []
    s10_list = ['軸']
    s11_list = ['逆質問']
    s12_list = ['企業']

    s1_1_list = ['方法', '仕方', 'やり方']
    s2_1_list = ['心構え', '対策', 'コツ', 'アドバイス', '注意点', '気をつけること','よく聞かれること']
    s3_1_list = ['企業', '業界', '探索', '探し方']
    s3_1_another_list = ['企業','業界', '探索', '探し方']
    s4_1_list = ['対策', '勉強']
    s5_1_list = ['タイムライン', 'スケジュール']
    s6_1_list = ['どの']
    s7_1_list = ['辞退', '断る']
    s8_1_list = ['進め方', 'スケジュール', 'タイムライン']
    s9_1_list = ['企業', '業界', '職種']
    s10_1_list = ['仕事', '自己分析']
    s11_1_list = ['面接', '最後', '逆質問']
    s12_1_list = ['情報', '強み']
    weights = [0] * len(answertype_list)
    for x in morph_dics:
      key = x['surface']
      #初期層
      if state == 'init':
        if key in s1_list:
          weights[answertype_list.index('自己分析')] += 1
          state = 's11'
        elif key in s2_list:
          weights[answertype_list.index('面接')] += 1
          state = 's21'
        elif key in s3_list:
          weights[answertype_list.index('企業の探し方')] += 1
          state = 's31'
        # elif (key=='いつ'):
        #   weights[answertype_list.index('自己分析')] += 0.2
        #   state = 's111'
        elif key in s4_list:
          weights[answertype_list.index('試験')] += 1
          state = 's41'
        elif key in s5_list:
          weights[answertype_list.index('就活')] += 1
          state = 's51'
        elif key in s6_list:
          weights[answertype_list.index('リクルーター')] += 1
          state = 's61'
        elif key in s7_list:
          weights[answertype_list.index('内定辞退')] += 1
          state = 's71'
        elif key in s8_list:
          weights[answertype_list.index('就活の時期と主にやること')] += 1
          state = 's81'
        elif key in s9_list:
          weights[answertype_list.index('職種軸')] += 1
          state = 's91'
        # elif key == '軸':
        #   weights[answertype_list.index('業種軸')] += 1
        #   state = 's101'
        elif key in s11_list:
          weights[answertype_list.index('質問')] += 1
          state = 's111'
        elif key in s12_list:
          weights[answertype_list.index('企業の強み')] += 1
          state = 's121'
        else:
          continue

      #第２層
      elif state == 's11':
        if key in s3_1_list:
          weights[answertype_list.index('企業研究')] += 1
        elif key in s1_1_list:
          weights[answertype_list.index('自己分析')] += 1
        else:
          continue
      elif state == 's21':
        if key in s2_1_list:
          weights[answertype_list.index('面接')] += 1
        else:
          continue
      elif state == 's31':
        if key in s1_1_list:
          weights[answertype_list.index('自己分析')] += 1
        elif key in s3_1_another_list:
          weights[answertype_list.index('企業の探し方')] += 1
        else:
          continue
      elif state == 's41':
        if key in s4_1_list:
          weights[answertype_list.index('試験')] += 1
        else:
          continue
      elif state == 's51':
        if key in s5_1_list:
          weights[answertype_list.index('就活')] += 1
        elif key in s8_1_list:
          weights[answertype_list.index('就活の時期と主にやること')] += 1
        else:
          continue
      elif state == 's61':
        if key in s6_1_list:
          weights[answertype_list.index('リクルーター')] += 1
        else:
          continue
      elif state == 's71':
        if key in s7_1_list:
          weights[answertype_list.index('内定辞退')] += 1
        else:
          continue
      elif state == 's81':
        if key in s8_1_list:
          weights[answertype_list.index('就活の時期と主にやること')] += 1
        else:
          continue
      elif state == 's91':
        if key in s9_1_list:
          weights[answertype_list.index('職種軸')] += 1
        elif key in s10_1_list:
          weights[answertype_list.index('業種軸')] += 1
        else:
          continue
      elif state == 's111':
        if key in s11_1_list:
          weights[answertype_list.index('質問')] += 1
        else:
          continue
      elif state == 's121':
        if key in s12_1_list:
          weights[answertype_list.index('企業の強み')] += 1
        else:
          continue
      # elif state == 's111':
      #   if key in s111_list:
      #     weights[answertype_list.index('自己分析')] += 0.3
      #     state = 's112'
      #   else:
      #     continue
      # elif state == 's112':
      #   if key in s1111_list:
      #     weights[answertype_list.index('自己分析')] += 0.6
      #   else:
      #     continue
    answertype = answertype_list[weights.index(max(weights))]
    if any(weights):
      answertype_num = weights.index(max(weights))
    else:
      answertype_num = 'X'
    # print(weights)
    return answertype_num


if __name__=='__main__':
    main()
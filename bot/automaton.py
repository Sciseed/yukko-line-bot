import MeCab
import sys

# def main():
#     sentence = "自己分析をするのですか？"
#     answertype = make_flag(sentence)
#     print(answertype)

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
    for x in morph_dics:
      #print(x)
      # print(x["surface"])
      if state == 'init':
        if x['surface'] == '自己分析':
          answertype = 'Self-analysis'
        elif x['surface'] == '面接':
          answertype = 'Interview'
        elif x['surface'] == '企業研究':
          answertype = 'Coporate-research'
        elif x['surface'] == '試験':
          answertype = 'Test'
        elif x['surface'] == '就活':
          answertype = 'Job-hunting'
        elif x['surface'] == 'リクルーター':
          answertype = 'recruiter'
        elif x['surface'] == '内定辞退':
          answertype = 'Bow-out'
        elif x['surface'] == '職種軸':
          answertype = 'Occup-type'
        elif x['surface'] == '質問':
          answertype = 'Question'
        elif x['surface'] == '強み':
          answertype = 'Strongth'
        else:
          continue
    print(answertype)
    return answertype

def mecab_reader(mecabfile):
    sentences = []
    sentence = []
    for line in mecabfile:
        if line == "EOS\n":
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            dic = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1]
            }
            sentence.append(dic)
    return sentences

def tabbed_str_to_dict(tabbed_str: str) -> dict:
    """
    例えば「次第に   シダイニ    次第に   副詞-一般   」のようなタブ区切りで形態素を表す文字列をDict型に変換する.
    :param tabbed_str タブ区切りで形態素を表す文字列
    :return Dict型で表された形態素
    """
    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def morphemes_to_sentence(morphemes: list) -> list:
    """
    Dict型で表された形態素のリストを句点毎にグルーピングし、リスト化する.
    :param morphemes Dict型で表された形態素のリスト
    :return 文章のリスト
    """
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences

if __name__=='__main__':
    main()
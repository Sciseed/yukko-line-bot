import sys
import MeCab

def mecab_morpheme(sentence):
  m = MeCab.Tagger("-Owakati")
  a = m.parse("sentence")
  li = a.split(' ')
  return li
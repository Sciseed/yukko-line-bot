import sys
from janome.tokenizer import Tokenizer

def janome_morpheme(sentence):
  t = Tokenizer()
  tokens = t.tokenize(sentence)
  li = [token.surface for token in tokens]
  return li
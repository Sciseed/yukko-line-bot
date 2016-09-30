import codecs
import re
from collections import Counter
import pandas
import automaton
import MeCab

# fsen = codec.open('talkscript.csv', 'r', 'latin_1')
with codecs.open('talkscript.csv', "r", "Shift-JIS", "ignore") as file:
    df = pandas.read_table(file, delimiter=",")

def checkstopwords(word, stopwords):
  return True if word in stopwords else False

if __name__ == '__main__':
  # outputfile = 'talkscript_csv.txt'
  # outputfile1 = 'stop_list.txt'
  # g = open(outputfile, 'w')
  # g1 = open(outputfile1, 'w')
  # words = []
  m = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
  # for line in df['script']:
  #   word_arr = m.parse(line).split(' ')
  #   for word in word_arr:
  #     words.append(word)
  # counter = Counter(words)
  # for word , count in counter.most_common():
  #   g.write("%s %s\n" % (word, count))
  #   g1.write("%s \n" % word)
  # g.close()
  features = []
  stopwords = []
  fstop = codecs.open('stop_list.txt', 'r')
  fout = codecs.open('words.txt', 'w')
  stopwords = [line for line in fstop]
  for line in df['script']:
    string = m.parse(line).split(' ')
    for word in string:
      if not checkstopwords(word, stopwords):
        features.append(word)
    line = ' '.join(features) + '\n'
    fout.writelines(line)
    features = []
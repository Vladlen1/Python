__author__ = 'vladbirukov'
import re
import sys
#name = raw_input('Write name text file:')
name = sys.argv[2]
with open(name) as tex_file:
    tex_file=tex_file.read()

def col_sence(text):
    sentence = 0
    for i in tex_file:
        if i == '.' or i == '?' or i == '!':
                sentence += 1
    return sentence
col_senc = col_sence(tex_file)

def col_word_in_sence(text):
    result = []
    replace = re.sub('[?!]','.',text)
    for word in replace.split('.'):
        result.append(len(word.split()))
    return result
col_words = col_word_in_sence(tex_file)


def average_repeat(col_word, scence):
    sum_word = sum(col_word)
    average_number_world = float(sum_word)/float(scence)
    return average_number_world
print 'The average number of words in the sentence',average_repeat(col_words, col_senc)


def media_repeat(word_list, scence):
    if scence % 2 == 0:
        word_list.sort()
        media_number = (float(word_list[1] + word_list[-1]))/2
    else:
        word_list.sort()
        media_number = word_list[(scence)/2]
    return media_number
print 'The median number of words in a sentence',media_repeat(col_words, col_senc)


def repeat_world(text):
  word_dictionary = {}
  replace = re.sub('[?!,.()""]',' ',text)
  for word in replace.split():
      if word == '':
          continue
      else:
        word_dictionary[word.lower()] = word_dictionary.get(word.lower(), 0) + 1
  return word_dictionary
print 'How many times each word is repeated in this text',repeat_world(tex_file)


def repeat_word_in_my_mind(top, lench, text):
    key = []
    gram = []
    dict = {}
    replace = re.sub('[?!,.()""-]',' ',text)
    for word in replace.split():
        if word == '':
            continue
        else:
           key.append(word.lower())
    for word in key:
        for i in range(len(word)+1-lench):
            gram.append(word[i:(i+lench)])
    for word in gram:
        dict[word] = dict.get(word, 0) + 1
    result = sorted(dict.items(), key=lambda (k, v): v, reverse=True)
    print 'Top-K the most frequently recurring letters N-gram',result[0:top]
top = int(raw_input('Write top mumber:'))
lench = int(raw_input('Write len:'))
repeat_word_in_my_mind(top,lench, tex_file)
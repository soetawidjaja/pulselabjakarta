#!/usr/bin/python
import os, sys, re

stopwords = {'sw':1}
del stopwords['sw']

def load_stopwords(fd_stopwords):
   for line in open(fd_stopwords):
      stopwords[line.lower().replace('\n','')] = 1

def remove_url(line):
   res = []
   for word in line.split():
      if not 'http' in word:
         res.append(word)
   return ' '.join(res)

def preprocessing(txt):

   '''to remove mention IDs'''
   tmp = []
   for word in line.split():
      if not word[0]=='@':
         tmp.append(word)
   txt = ' '.join(tmp)

   txt = re.sub('[.!?]', ' ', txt)
   txt = re.sub('[^A-Za-z0-9 ]+', ' ', txt)
   #text = re.sub('[^A-Za-z0-9 ]+', '', text)
   txt = re.sub('[ ]+', ' ', txt)
   
   res = []
   for word in txt.split():
      if not word.isdigit()==True:
         res.append(word)
   return ' '.join(res)

def remove_stop_words(line):
   res = []
   for word in line.split():
      if not stopwords.has_key(word):
         res.append(word)

   return ' '.join(res)

if __name__ == '__main__':
   if len(sys.argv) <> 3:
      sys.stderr.write('[usage] %s (tweet text) (stop word file)\n'%(sys.argv[0]))
      #sys.stderr.write('[usage] %s (tweet text)\n'%(sys.argv[0]))
      exit()
   
   PARAM_text = sys.argv[1]
   PARAM_stopwords = sys.argv[2]

   load_stopwords(PARAM_stopwords)

   for line in open(PARAM_text):
      line = line.lower()
      tmp = remove_url(line)
      tmp = preprocessing(tmp)
      tmp = remove_stop_words(tmp)
      if not tmp=='':
         print tmp

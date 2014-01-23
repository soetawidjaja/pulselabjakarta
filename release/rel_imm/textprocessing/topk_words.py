#!/usr/bin/python

import os, sys

freq = {'a':1}
del freq['a']

dic_except = {'no':1}
del dic_except['no']

def load_except_words(fd_except):
   for line in open(fd_except):
      word = line.replace('\n','')
      dic_except[word] = 1

def count(fd_text):
   for line in open(fd_text):
      line = line.lower()
      es = line.split()
      for i in range(0, len(es)):
         key = '%s'%(es[i])
         if not dic_except.has_key(key):
            if freq.has_key(key):
               freq[key] = freq[key] + 1
            else:
               freq[key] = 1

if __name__ == '__main__':
   
   if len(sys.argv) <> 3:
      sys.stderr.write('[usage] %s (input text) (except file)'%(sys.argv[1]))
      sys.stderr.write('\t (except file) to have a list of words not to be considered (e.g. taxonomy)\n')
      sys.stderr.write('\t Given \'no\' for (except file), no need to make a file\n')
      exit()

   PARAM_text = sys.argv[1]
   PARAM_except = sys.argv[2]

   if not PARAM_except == 'no':
      load_except_words(PARAM_except)

   count(PARAM_text)

   for x in sorted(freq.items(), key=lambda x: x[1], reverse=True):
      print x[0], x[1]

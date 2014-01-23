#!/usr/bin/python

import os, sys

freq = {'a-b':1}
del freq['a-b']

def count(fd_text):
   for line in open(fd_text):
      line = line.lower()
      es = line.split()
      for i in range(0, len(es)):
         for j in range(i+1, len(es)):
            key = '%s-%s'%(es[i], es[j])
            if freq.has_key(key):
               freq[key] = freq[key] + 1
            else:
               rev_key = '%s-%s'%(es[j], es[i])
               if freq.has_key(rev_key):
                  freq[rev_key] = freq[rev_key] + 1
               else:
                  freq[rev_key] = 1

if __name__ == '__main__':
   
   if len(sys.argv) <> 2:
      sys.stderr.write('[usage] %s (normalized text - line per tweet)\n'%(sys.argv[0]))
      exit()

   PARAM_text = sys.argv[1]
   count(PARAM_text)

   for x in sorted(freq.items(), key=lambda x: x[1], reverse=True):
      print x[0].split('-')[0], x[0].split('-')[1], x[1]

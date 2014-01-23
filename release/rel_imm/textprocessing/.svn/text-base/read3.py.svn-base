#!/usr/bin/python
import os, sys
import json

'''
File: read3.py
Last updated on Dec 16, 2013
By Jonggun
'''

def extract(tweet, field):
   output = 'NONE'
   try:
      res = tweet[field[0]]
      for x in range(1,len(field)):
         #res = res[field[x]]
         if field[x].isdigit()==False:
            res = res[field[x]]
         else:
            res = res[int(field[x])]
      output = json.dumps(res)
   except:
      pass
   return output

def process(infile, split, fields):
   data = []
   with open(infile) as f:
      for line in f:
         data.append(json.loads(line))

   res = []
   s = '|'
   if split=='space':
      s = ' '
   for tweet in data:
      res = []
      for field in fields:
         res.append(extract(tweet, field.split('.')))
      print s.join(res)

if __name__ == '__main__':

   if len(sys.argv) < 4 or (sys.argv[2]!='bar' and sys.argv[2]!='space'):
      sys.stderr.write('[usage] %s (input) (bar or space) (field 1) ... (field N)\n'%(sys.argv[0]))
      sys.stderr.write('\t (example) %s bar input.json twitter.user.name twitter.text\n'%(sys.argv[0]))
      exit(0)

   PARAM_infile = sys.argv[1]
   PARAM_split = sys.argv[2]
   PARAM_fields = sys.argv[3:]

   process(PARAM_infile, PARAM_split, PARAM_fields)

#!/usr/bin/python
import os, sys
import json

'''
File: extract.py
Last updated on Dec 18, 2013
By Jonggun
'''

def extract(tweet, field, value):
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

   output = output.lower()
   value = value.lower()
   if output==value or output=='\"%s\"'%(value):
      return True
   return False

def process(infile, fields):
   data = []
   with open(infile) as f:
      for line in f:
         data.append(json.loads(line))

   res = []
   for tweet in data:
      check = True

      for i in range(0,len(fields)/2):
         field = fields[2*i]
         value = fields[2*i+1]
         check = check & extract(tweet, field.split('.'), value)
         #print field, value, check

      if check==True:
         print json.dumps(tweet)

if __name__ == '__main__':
   if len(sys.argv) < 4:
      sys.stderr.write('[usage] %s (input) (field 1) (field 1 value) ... (field N) (field N value)\n'%(sys.argv[0]))
      sys.stderr.write('\t (example) %s input.json twitter.user.screen_id jonggun\n'%(sys.argv[0]))
      exit(0)

   PARAM_infile = sys.argv[1]
   PARAM_fields = sys.argv[2:]

   process(PARAM_infile, PARAM_fields)

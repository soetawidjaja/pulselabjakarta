#!/usr/bin/python
#!/usr/bin/python
import os, sys, csv

'''
File name: read2.py
Written by Jong Gun Lee
Last updated on Nov 12, 2013
Description:
   - To extract some fields given by field index or field name 
   - Input: CSV file with head line at the first line
'''


if len(sys.argv) < 3:
   sys.stderr.write('[usage] %s (input.csv) (params...)\n'%(sys.argv[0]))
   sys.stderr.write('\t number as a param: field index starting from 0\n')
   sys.stderr.write('\t string as a param: field full or partial name\n')
   exit()

PARAM_INFILE = sys.argv[1]
PARAMS = sys.argv[2:]

is_first_line = True
ith_index = []
with open(PARAM_INFILE, 'rb') as csvfile:
   tweetreader = csv.reader(csvfile, delimiter=',')
   for row in tweetreader:
      if is_first_line == True:
         for param in PARAMS:
            if param.isdigit() == True:
               ith_index.append(int(param))
            else:
               for i in range(0, len(row)):
                  if param in row[i]:
                     ith_index.append(i)
         for i in ith_index:
            print '{%s:%s}'%(i,row[i])
         print 
         ## sort ith_index if needed
         is_first_line = False

      else: # NOT (if is_first_line == True)
         res = ''
         for i in ith_index:
            try:
               res = '%s|%s'%(res, row[i])
            except:
               continue
         print '%s|'%(res)
         '''
         for i in ith_index:
            res = '%s|%s'%(res,row[i])
            print '%s|'%(res)
         '''



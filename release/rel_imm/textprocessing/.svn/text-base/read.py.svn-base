#!/usr/bin/python
import os, sys, csv

if len(sys.argv) <> 3:
    sys.stderr.write('[usage] %s (input.csv) (ith column)\n'%(sys.argv[0]))
    exit()

PARAM_INFILE = sys.argv[1]
PARAM_ITH = int(sys.argv[2])

with open(PARAM_INFILE, 'rb') as csvfile:
   tweetreader = csv.reader(csvfile, delimiter=',')
   for row in tweetreader:
      try:
         print row[PARAM_ITH]#print ', '.join(row)
      except:
         continue



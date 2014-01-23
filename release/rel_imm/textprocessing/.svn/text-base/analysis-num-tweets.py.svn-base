#!/usr/bin/python
import os, sys
'''
input: 177th field (tweet date)
'''
if len(sys.argv) <> 2:
    sys.stderr.write('[usage] %s (input-233th)\n'%(sys.argv[0]))
    exit()

months = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun',\
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

for line in open(sys.argv[1]):
    es = line.split()
    try:
        print '%d %d'%(months.index(es[2].lower()), int(es[1]))
    except:
        continue

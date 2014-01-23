import os,sys

for line in open('info.txt'):
    if int(line.split()[1]) > 500:
        print '\'%s\','%(line.split()[0])

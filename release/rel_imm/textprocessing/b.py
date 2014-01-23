import os,sys

dic = {'key':0}
del dic['key']

index = 0
for line in open('info'):
    es = line.split(',')
    for e in es:
        key = e.replace('\"','').lower()
        dic[key] = index
        #print key, index
        index = index + 1

for line in open('info.txt'):
    es = line.split()
    try:
        print dic[es[0].lower()], line,
    except:
        continue

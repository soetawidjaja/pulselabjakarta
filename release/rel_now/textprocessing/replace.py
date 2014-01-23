import os, sys

dic = {'name':0}
del dic['name']
last = 0

for line in open('raw'):
	#print line,
	es = line.split(',')
	if not dic.has_key(es[0]):
		last = last + 1
		dic[es[0]] = last
	try:
		print dic[es[0]], es[1], es[2],
	except:
		continue


for k in dic.keys():
	print k, dic[k]


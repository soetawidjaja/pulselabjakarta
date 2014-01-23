#!/usr/bin/python

import os, sys
import json

immunization = ['imunisasi', 'imun', 'vaksinasi', 'vaksin', 'mengimunisasi', 'diimunisasi', 'diimun',\
                  'divaksin', 'divaksinasi', 'mengimun', 'memvaksinasi', 'memvaksin']
new_vaccine = ['5 in 1', '5in1', 'peluncuran', 'meluncurkan', 'luncurkan', 'canangkan', 'mencanangkan',\
                  'pencanangan','pengenalan', 'mengenalkan', 'kenalkan', 'introduksi', 'launching']
disease = ['difteri', 'dipteri', 'diphteria', 'pertusis', 'perthusis', 'batuk 100 hari', 'batuk 100hari',\
               'batuk100hari', 'batuk 100 hr', 'batuk 100hr', 'batuk100hr', 'batuk rejan', 'campak',\
               'sarampah', 'sarampa', 'polio', 'rubella', 'rubela', 'cacar jerman']
outbreak = ['wabah', 'kejadian luar biasa', 'KLB', 'kasus', 'tertular', 'menular', 'ditularkan', 'terserang',\
               'menyerang', 'terinfeksi', 'infeksi', 'terjangkit', 'berjangkit', 'penyebaran', 'persebaran',\
               'menyebar', 'pencegahan', 'mencegah', 'dicegah']
symptom = ['kipi', 'reaksi', 'efek samping', 'efek simpang', 'panas', 'demam', 'sakit', 'lumpuh', 'kelumpuhan',\
               'bengkak', 'kejang', 'kejang-kejang', 'kejang2', 'autis', 'meninggal', 'mati', 'keracunan',\
               'keluhan', 'nangis', 'menangis', 'muntah', 'muntah-muntah', 'muntah2', 'nyeri', 'luka', 'abses',\
               'syok', 'shock', 'alergi', 'sesak napas', 'sesak nafas']
halal_haram = ['halal', 'thayib', 'thayyib', 'haram', 'dihalalkan', 'menghalalkan', 'mengharamkan', 'diharamkan',\
                  'fatwa', 'dalil', 'mui', 'ulama', 'quran', 'qur\'an', 'alquran', 'alqur\'an', 'hadits', 'hadith', 'babi']
injection = ['suntik', 'suntikan']
pentavalent = ['pentavelen', 'pentabio', 'DTP+HepB+HiB', 'DPT+HepB+HiB', 'vaksin baru']
filters = [immunization, new_vaccine, disease, outbreak, symptom, halal_haram, injection, pentavalent]

def check(txt):
   res = [0, 0, 0, 0, 0, 0, 0, 0]

   for i in range(0,len(filters)):
      for w in filters[i]:
         if w in txt:
            res[i] = 1
            #print i, w
            break
   return res

def check_muslim(txt):
   for w in ['muslim', 'agama', 'islam']:
      if w in txt:
         break
      else:
         return False
   for w in ['dibolehkan', 'dilarang', 'melarang', 'membolehkan']:
      if w in txt:
            return True
   return False

def determine(res):
   output = [0, 0, 0, 0] #NV, OB, SE, HH
   if res[0]==1: 
      if res[1]==1: #immunization + new_vaccine -> NV  
         output[0] = 1 
      #
      if res[2]==1: #immunization + disease -> OB
         output[1] = 1
      #
      if res[4]==1: #immunization + symptom -> SE
         output[2] = 1
      #
      if res[5]==1 or res[8]==1: #immunization + halal_haram/muslim -> HH 
         output[3] = 1
         
   # disease + symptom + injection -> SE
   if output[2]==0 and (res[2]==1 and res[4]==1 and res[6]==1):
      output[2] = 1

   # disease + outbreak -> OB
   if output[1]==0 and (res[2]==1 and res[3]==1):
      output[1] = 1

   # pentavelent -> NV
   if output[0]==0 and res[7]==1:
      output[0] = 1

   return output

def write_file(fd_name, tweet, txt):
   #print '%s\t%s'%(fd_name, txt)
   fd = open(fd_name, 'a')
   fd.write('%s\n'%(json.dumps(tweet)))
   fd.close()

def result(output, tweet, txt):
   if output[0]==1:
      write_file('nv.json', tweet, txt)

   if output[1]==1:
      write_file('ob.json', tweet, txt)

   if output[2]==1:
      write_file('se.json', tweet, txt)

   if output[3]==1:
      write_file('hh.json', tweet, txt)

def process(a_json):
   data = []
   with open(a_json) as f:
      for line in f:
         data.append(json.loads(line))
   
   for tweet in data:
      try:
         txt = tweet['interaction']['content'].lower()
         #print txt
         #txt = 'imunisasi suntik kipi pentavelen halal'
         res = check(txt)
         if res[0] == True:
            if check_muslim(txt) == True:
               res.append(1)
            else:
               res.append(0)
         output = determine(res)
         result(output, tweet, txt)
      except:
         continue
      
if __name__ == '__main__':
   cnt = 0
   for f in open('input'):
      in_file = '/Users/jonggunlee/Desktop/s3.imm.2013/%s'%(f.strip())
      cnt = cnt + 1
      sys.stderr.write('Processing... %d\r'%(cnt))
      process(in_file)
      

#!/usr/bin/python
import os, sys
import datetime, time
import csv

months = ['',\
'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

commodities = ['',\
'minyak goreng kemasan',\
'minyak goreng curah',\
'daging sapi',\
'daging ayam broiler',\
'daging ayam kampung',\
'telur ayam ras',\
'telur ayam kampung',\
'tepung terigu',\
'kedelai impor',\
'kedelai lokal',\
'beras medium',\
'gula pasir',\
'susu kental manis',\
'mie instant',\
'cabai merah keriting',\
'cabai merah biasa',\
'bawang merah',\
'ikan teri asin',\
'kacang hijau',\
'kacang tanah',\
'ketela pohon']

with open('nowcasting_official_data_sep10-agu13.csv') as csvfile:
    pricedata = csv.reader(csvfile, delimiter=',')
    for line in pricedata:
        dd_MM_yy = line[0].split('-')
        yyyy = 2000 + int(dd_MM_yy[2])
        mm = months.index(dd_MM_yy[1])
        dd = int(dd_MM_yy[0])
        d = datetime.date(yyyy,mm,dd)
        commodity = commodities.index(line[1])
        price = line[2].replace(',','')

        print commodity, yyyy, mm, dd, int(time.mktime(d.timetuple())), price


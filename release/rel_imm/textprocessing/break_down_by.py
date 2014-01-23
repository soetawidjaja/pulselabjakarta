#!/usr/bin/python
import os, sys

output_files = []

def load_keywords(fd_keywords):
   for line in open(fd_keywords):
      line = line.replace('\n','')
      output_files.append('-'.join(line.split(',')))

def classify_tweets(fd_tweets):
   fd = []
   for i in range(0,len(output_files)):
      fd.append(open(output_files[i],'a'))

   for tweet in open(fd_tweets):
      tweet = tweet.lower()
      for i in range(0,len(output_files)):
         for keyword in output_files[i].split('-'):
            if keyword in tweet:
               fd[i].write(tweet)
               fd[i].flush()
               break

   for x in fd:
      x.close()

if __name__ == '__main__':
   if len(sys.argv) <> 3:
      sys.stderr.write('[usage] %s (CSV file) (keyword file)\n'%(sys.argv[0]))
      sys.stderr.write('\t (CSV file): tweet file\n')
      sys.stderr.write('\t (keyword file): a keyword(s) each line\n')
      exit()

   PARAM_tweets = sys.argv[1]
   PARAM_keywords = sys.argv[2]
   
   load_keywords(PARAM_keywords)
   classify_tweets(PARAM_tweets)

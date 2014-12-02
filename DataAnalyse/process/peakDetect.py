#!/usr/bin/env python
# Filename: peakDetect.py

__author__ = 'Echo ZHAN'

import sqlite3
import math	
import split
import frqcnt
import config
from operator import itemgetter
import outputGen

#this class is to implemented the algorithm of peak time detecting
#to initiate this class, you need to give three time strings in the shape of "0000-00-00 00:00:00.000"
#the function update is to help update the value of the mean  and the mean deviation of tweet quantity in each time window
#the function  find_peak_windows is to find the peak time windows
class peakWnd(object):
	
	def __init__(self, starttime, endtime, tminterval, event):
		self.pwindows = []
		self.keyw = []
		self.start = starttime
		self.end = endtime
		self.interval = tminterval
		self.termdic = {}
		self.event = event
		
	def __update(self, oldmean, oldmeandev, updatevalue, alph):
		diff = abs(oldmean - updatevalue)
		newmeandev = (alph * diff) + ((1 - alph) * oldmeandev)
		newmean = (alph * updatevalue) + ((1 - alph) * oldmean)
		return newmean, newmeandev

	def find_peak_windows(self):
		twcount, timIntv = frqcnt.twCount(self.start, self.end, self.interval,self.event)
		#initiate the mean and the mean deviation of tweet quantity
		#tao and alph is two important constant parameters when implementing this algorithm
		mean = twcount[0]
		temean = (twcount[0]+twcount[1]+twcount[2]+twcount[3]+twcount[4])/5
		meandev = (abs(twcount[0]-temean)+abs(twcount[1]-temean)+abs(twcount[2]-temean)+abs(twcount[3]-temean)+abs(twcount[4]-temean))/5
		tao = config.tao
		alph = config.alph
		
		i = 2
		length = len(twcount)
		while i < length:
			if twcount[i] > twcount[i-1] and abs(twcount[i]-mean) > (tao * meandev):
				#when find a significant increase, start a peak time window
				start = i - 1
				while i < length and twcount[i] > twcount[i-1]:
					#if the quantity of tweets keeps increasing
					mean, meandev = self.__update(mean, meandev, twcount[i], alph)
					i += 1
					end = i
				while i < length and twcount[i] > twcount[start]:
					if twcount[i] > twcount[i-1] and abs(twcount[i]-mean) > (tao * meandev):
						#when find another significant increase, you need to start a new peak time window 
						 i -= 1
						 end = i
						 break
					else:
						#otherwise, go on unless finding the tweet quantity is lower than the start point
						mean, meandev = self.__update(mean, meandev, twcount[i], alph)
						end = i
						i += 1
				self.pwindows.append((timIntv[start], timIntv[end], start, end))
			else:
				mean, meandev = self.__update(mean, meandev, twcount[i], alph)
			
			i += 1
			
		#this part is to output the results
		
	import config
	
	def termfrqs(self, peakSt, peakEd, opt):
		#this function calculate the term frequency of a word
		conn = sqlite3.connect(config.databasePath)
		cursor = conn.cursor()

		#get all the tweets in a time period
		front = peakSt
		back = peakEd
		targetf = 'datetime(\''+front+'\')'
		targetb = 'datetime(\''+back+'\')'
		target = 'select text_content from DataAnalyse_twitter where event=\''+self.event+'\' AND datetime(pub_date)>'+targetf+' AND datetime(pub_date)<'+targetb
		cursor.execute(target)
		value =  cursor.fetchall()
		
		cursor.close()
		conn.close()
		
		#for every tweet, first spilt the words, then calsulate the term frequency
		dit = {}
		for eveTw in value:
			s = split.splitwd(eveTw[0], 1)
			for eveword in s:
				dit[eveword.lower()] = dit.get(eveword.lower(), 0) + 1
				#dit[eveword] = dit.get(eveword, 0) + 1
		
		#two kinds of output, dictionary or a sorted list 
		if opt == 1:
			return dit
		else:
			return sorted(dit.items(), key=itemgetter(1), reverse=True)

	def keywgen_idf(self):	
		#this function calculate the keywords of a peak time window
		
		#this part calculate the document frequency of each word
		timeSt = frqcnt.Timestamp(frqcnt.dateEnd(self.start), frqcnt.dateEnd(self.end), frqcnt.dateEnd(self.interval))
		timeSl = timeSt.tmSlGen()
		length = len(timeSl)
		i = 0
		self.termdic = {}
		while i < (length-1):
			front = timeSl[i]
			i += 1
			back = timeSl[i]
			wnterm = self.termfrqs(front, back, 1).keys()
			for word in wnterm:
				self.termdic[word] = self.termdic.get(word, 0) + 1
		
		#for the first 200 words with the highest term frequency, calculate their TF-IDF
		#rank the words according to their TF-IDF, output the first 20 words as keywords		
		key = {}	
		for evewnd in self.pwindows:
			key.clear()
			tf = self.termfrqs(evewnd[0], evewnd[1], 0)
			i = 0
			while i<200:
				try:
					idf = math.log((length/(self.termdic[(tf[i][0])]+1)),2)
					tfidf = tf[i][1] * idf
					key[(tf[i][0])] = tfidf
					i += 1
				except:
					break
			self.keyw.append(sorted(key.items(), key=itemgetter(1), reverse=True)[:20])
			outputGen.TWOuput(self, self.keyw, self.event)
		return self.keyw
		

# End of peakDetect.py
#!/usr/bin/env python
# Filename: outputGen.py

__author__ = 'Echo ZHAN'

import os
import json

def TWOuput(wnd, tuples, event):
	destin = os.path.abspath('.')
	destin = os.path.join(destin, 'output')
	#os.mkdir(destin)
	destin = os.path.join(destin, 'keywords_'+event+'.json')
	df = open(destin, 'w')
	length = len(tuples)
	
	i = 0
	wndInfo = {}
	while i < length:
		wndInfo['No.'] = str(i+1)
		wndInfo['start'] = wnd.pwindows[i][0]
		wndInfo['end'] = wnd.pwindows[i][1]
		wndInfo['startNum'] = str(wnd.pwindows[i][2])
		wndInfo['endNum'] = str(wnd.pwindows[i][3])
		j = 1
		for tup in tuples[i]:
			wndInfo['keyword'+str(j)] = tup[0]
			j += 1
		
		target = json.dumps(wndInfo)	
		df.write(target+'\n')
		wndInfo.clear()
		i += 1
		
	df.close()
	
def WndOutput(TwCount, TmSlot, event):
	destin = os.path.abspath('.')
	destin = os.path.join(destin, 'output')
	#os.mkdir(destin)
	destin = os.path.join(destin, 'TwQuantity_'+event+'.json')
	df = open(destin, 'w')
	length = len(TwCount)
	
	i = 0
	wndInfo = {}
	while i < length:
		wndInfo['time'] = TmSlot[i]
		wndInfo['Quantity'] = TwCount[i]
		
		target = json.dumps(wndInfo)	
		df.write(target+'\n')
		wndInfo.clear()
		i += 1
		
	df.close()

# End of outputGen.py
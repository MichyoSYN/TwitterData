#!/usr/bin/env python
# Filename: split.py

__author__ = "Echo ZHAN"

def splitwd(line, opt):
	#opt to decide extract the words or the urls
	lenth = len(line)
	front = 0
	
	#if the character is not an alphabet or number or _, then I treat it as a dividing line between two words
	alph = line[front]
	while not(((alph>='a')and(alph<='z')) or ((alph>='A')and(alph<='Z')) or ((alph>='0')and(alph<='9')) or (alph=='_')):
		front = front + 1
		alph = line[front]	
	back = front
	
	s = set([])
	url = set([])
	while back < lenth:
		beta = line[back]
		try:
			while (((beta>='a')and(beta<='z')) or ((beta>='A')and(beta<='Z')) or ((beta>='0')and(beta<='9')) or (beta=='_')):
				back = back + 1
				beta = line[back]
		except IndexError:
			s.add(line[front:])
			break
		# to detect the url
		#to add the words to the word set, add url to the url set
		if beta == ':':
			if (((back - front)==4) and (line[front]=='h') and (line[front:back] == 'http')):
				try:
					while beta != ' ':
						back += 1
						beta = line[back]
				except IndexError:
					url.add(line[front:])
					break
			url.add(line[front:back])
		else:
			s.add(line[front:back])
		try:
			front = back + 1
			alph = line[front]
			# to find the start of the next word
			while not(((alph>='a')and(alph<='z')) or ((alph>='A')and(alph<='Z')) or ((alph>='0')and(alph<='9')) or (alph=='_')):
				front = front + 1
				alph = line[front]	
		except IndexError:
			break
		back = front
	# if opt==1, then return the word set
	# otherwise, return the url set
	if opt == 1:
		return s
	else:
		return url
	
# End of split.py
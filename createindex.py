#-*-coding:utf-8-*-
#!/usr/bin/python

import mydate
import sys
import os
import pprint
import pickle
import pdb
import re

def getmydoc(thepath,onedir):
	ans=[]
	for line in open(thepath+'/'+onedir):
		line=line.strip()
		line=re.sub(r'\W',' ',line)
		mydate.totword+=1
		b=list(line.split(' '))
		#print b
		while ("" in b):
			b.remove("")
		ans.extend(b)
	return ans

def createindex(thepath):
	#global mydate.mydir

	mydate.mydir=os.listdir(thepath)
	for i in mydate.mydir:
		if(os.path.isdir(thepath+'/'+i)==True):
			mydate.mydir.remove(i)
	#print mydate.mydir
	#mydate.mydir=['a.txt','b.txt','c.txt']
	mydate.wordcnt=0#dict中的个数
	mydate.doccnt=0#文档个数
	mydate.listcnt=0#index个数
	#print id(wordcnt)
	for onedoc in mydate.mydir:
		mydate.mylist=getmydoc(thepath,onedoc)
		onedocword=0#每个词在这个文本中的位置
		mydate.docworddict={}
		for myword in mydate.mylist:
			if(myword not in mydate.mywordsdict):
				mydate.mywords.append([0]*3)
				mydate.mywords[mydate.wordcnt][0]=myword
				mydate.mywords[mydate.wordcnt][2]=0######################################DF
				mydate.mywordsdict[myword]=mydate.wordcnt
				mydate.wordcnt+=1
				#print myword,mywordsdict[myword]
			if(myword not in mydate.docworddict):
				mydate.docworddict[myword]=mydate.listcnt
				mydate.listcnt+=1
				mydate.myindex.append([0]*3)
				mydate.mywords[mydate.mywordsdict[myword]][2]+=1
			
			ins=mydate.docworddict[myword]
			mydate.myindex[ins][0]=mydate.doccnt
			mydate.myindex[ins][1]=mydate.mywordsdict[myword]
			mydate.myindex[ins][2]+=1
			mydate.myindex[ins].append(onedocword)
			onedocword+=1
		
		mydate.doccnt+=1
	mydate.myindex.sort(key=lambda x:(x[1],x[0])) #sort
	beg=0
	fin=0
	for i in range(len(mydate.mywords)):
		#pdb.set_trace()
		mydate.mywordsdictindex[i]=beg
		mydate.mywords[i][1]=beg
		while fin <len(mydate.myindex) and mydate.myindex[fin][1]==i:#python不支持逻辑短路
			fin+=1
		mydate.antimywordsdict[i]=fin
		beg=fin
	#pdb.set_trace()
	mydate.avgdoclen=(mydate.wordcnt+0.0)/mydate.doccnt#评价文档长度
	out=open("myindex.dat","wb")
	pickle.dump(mydate.myindex,out)
	out=open("mywords.dat","wb")
	pickle.dump(mydate.mywords,out)

	out=open("mydir.dat","wb")
	pickle.dump(mydate.mydir,out)
	out=open("mywordsdictindex.dat","wb")
	pickle.dump(mydate.mywordsdictindex,out)
	out=open("antimywordsdict.dat","wb")
	pickle.dump(mydate.antimywordsdict,out)
	out=open("mywordsdict.dat","wb")
	pickle.dump(mydate.mywordsdict,out)
	l=[mydate.wordcnt,mydate.doccnt,mydate.listcnt,mydate.totword,mydate.avgdoclen]
	out=open("basic.dat","wb")
	pickle.dump(l,out)
	'''
	for i in range(len(mydate.mywords)):
		mydate.mywordsdictindex[i]=mydate.mywords[i][1]
		if(i==len(mydate.mywords)-1):
			mydate.antimywordsdict[i]=len(mydate.myindex)
		else:
			mydate.antimywordsdict[i]=mydate.mywords[i+1][1]
			'''
#print id(mywords)
#pdb.set_trace()
'''
pprint.pprint (mydate.mywords)
pprint.pprint (mydate.myindex)
pprint.pprint (mydate.mywordsdict)
pprint.pprint (mydate.mywordsdictindex)
pprint.pprint (mydate.antimywordsdict)
'''

	

	
	

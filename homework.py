#-*-coding:utf-8-*-
#!/usr/bin/python

'''
数据结构
建立索引
mydir   文档列表
mydoc  每一个文档
mywords 字典
myindex 0 文档下标 1 单词下标 2 次数 3...
三个字典
mywordsdictindex  单词编号 起始位置
antimywordsdict   单词编号 结束位置
mywordsdict       单词->单词编号
#mypos是每个的单词起始的index下标，myfindindex是每个单词的标号，
'''
import hwf
import sys
import os
import pprint
import pickle
'''
thepath='C:/downtext'
mydir=os.listdir(thepath)
for i in mydir:
	if(os.path.isdir(thepath+'/'+i)==True):
		mydir.remove(i)
print mydir
'''
def createindex(thepath):
	mydir=['a.txt','b.txt','c.txt']
	mywords=[]
	myindex=[]
	wordcnt=0#dict中的个数
	doccnt=0#文档个数
	listcnt=0#index个数
	mywordsdict={}
	for onedoc in mydir:
		mylist=hwf.getmydoc(thepath,onedoc)
		onedocword=0#每个词在这个文本中的位置
		docworddict={}
		for myword in mylist:
			if(myword not in mywordsdict):
				mywords.append([0]*2)
				mywords[wordcnt][0]=myword
				mywordsdict[myword]=wordcnt
				wordcnt+=1
				#print myword,mywordsdict[myword]
			if(myword not in docworddict):
				docworddict[myword]=listcnt
				listcnt+=1
				myindex.append([0]*3)
			ins=docworddict[myword]
			myindex[ins][0]=doccnt
			myindex[ins][1]=mywordsdict[myword]
			myindex[ins][2]+=1
			myindex[ins].append(onedocword)
			onedocword+=1
		doccnt+=1
	myindex.sort(key=lambda x:x[1]) #sort
	beg=0
	fin=0
	mywordsdictindex={}
	antimywordsdict={}
	for i in range(len(mywords)):
		mywordsdictindex[mywords[i][0]]=beg
		mywords[i][1]=beg	
		while fin <len(myindex) and myindex[fin][1]==i:#python不支持逻辑短路
			fin+=1
		beg=fin
	for i in range(len(mywords)):
		mywordsdictindex[i]=mywords[i][1]
		if(i==len(mywords)-1):
			antimywordsdict[i]=len(myindex)
		else:
			antimywordsdict[i]=mywords[i+1][1]
	'''
	pprint.pprint (mywords)
	pprint.pprint (myindex)
	pprint.pprint (mywordsdict)
	pprint.pprint (mywordsdictindex)
	pprint.pprint (antimywordsdict)

	out=open("myindex.dat","wb")
	pickle.dump(myindex,out)
	out=open("mywords.dat","wb")
	pickle.dump(mywords,out)

	单个文本搜索
	'''

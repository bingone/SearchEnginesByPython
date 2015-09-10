#-*-coding:utf-8-*-
#!/usr/bin/python
#得到一个文本的列表
import sys
import os
import pprint
import pickle
import pdb
import mydate
import VSM
import init
def findword(loc,flag):#loc当前查询的单词在查询中的下标
	
	if(loc==len(mydate.mypos)):
		#if(mydate.mydoc==74):
			#pdb.set_trace()
		#pdb.set_trace()
		mydate.direct=1#############################
		if(flag==1):
			mydate.mydocs.append(mydate.mydoc)
			i=mydate.mypos[loc-1]+1
			#print mydate.mydocs
			if(i<mydate.antimywordsdict[mydate.myfindindex[loc-1]]):
				mydate.mydoc=mydate.myindex[i][0]
				mydate.mypos[loc-1]=i
			else:
				return -1
		return 1
	x=1
	if(loc==0):
		x=0
	i=mydate.mypos[loc]
	while i<mydate.antimywordsdict[mydate.myfindindex[loc]]:
		#if(mydate.mydoc==74):
			#pdb.set_trace()
		i=mydate.mypos[loc]#没有重新取值，i没有跟着mypos变化 信息滞后
		if(flag==-1):
			return -1
		if(loc==0 and mydate.direct==1):
			mydate.direct=0
		
		T=0
		while i<mydate.antimywordsdict[mydate.myfindindex[loc]] and mydate.myindex[i][0]<=mydate.mydoc:
			if(mydate.myindex[i][0]==mydate.mydoc):
				T=1
				break
			i+=1
		
		if(T==0):
			if(i==mydate.antimywordsdict[mydate.myfindindex[loc]]):#这个不应该是i+1，可以到最后一个
				return -1
			mydate.mydoc=mydate.myindex[i][0]
		mydate.mypos[loc]=i#############################
		if( T==1 and flag==1 and loc==0 and x==1):
			mydate.mydocs.append(mydate.mydoc)#############################
			i+=1
			#print mydate.mydate.mydocs
			if(i<mydate.antimywordsdict[mydate.myfindindex[loc]]):
				mydate.mydoc=mydate.myindex[i][0]
				mydate.mypos[loc]=i
			else:
				return -1
		#pdb.set_trace()
		if(flag==1 and T==1):
			pass
		else:
			T=0
		if(mydate.direct==1):
			return T
		flag=findword(loc+1,T)
		x=1
	return 0

def getwords():
	init.usu_init()
	mydate.searchword=raw_input("find words\n")
	mydate.searchword=mydate.searchword.split(' ')
	flag=True
	for i in range(len(mydate.searchword)):
		if(mydate.searchword[i] not in mydate.mywordsdict):
			flag=False
			break
		mydate.myfindindex.append(mydate.mywordsdict[mydate.searchword[i]])#mydate.mypos是每个的单词起始的index下标，myfindindex是每个单词的标号，三个字典
		mydate.mypos.append(mydate.mywordsdictindex[mydate.myfindindex[i]])
		
	if(flag==False):
		print 'wrong'
		return
	mydate.mydoc=mydate.myindex[mydate.mywordsdictindex[mydate.myfindindex[0]]][0]
	mydate.direct=0

	import pdb
	#pdb.set_trace()
	mydate.mydoc=mydate.myindex[mydate.mypos[0]][0]
	flag=findword(0,0)
	VSM.VSM()
	#print mydate.mydir
	#print mydate.mydocs   mydate.mydocs 查询到的文档号 返回这个数据
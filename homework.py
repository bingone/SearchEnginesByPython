#-*-coding:utf-8-*-
#!/usr/bin/python

'''
���ݽṹ
��������
mydir   �ĵ��б�
mydoc  ÿһ���ĵ�
mywords �ֵ�
myindex 0 �ĵ��±� 1 �����±� 2 ���� 3...
�����ֵ�
mywordsdictindex  ���ʱ�� ��ʼλ��
antimywordsdict   ���ʱ�� ����λ��
mywordsdict       ����->���ʱ��
#mypos��ÿ���ĵ�����ʼ��index�±꣬myfindindex��ÿ�����ʵı�ţ�
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
	wordcnt=0#dict�еĸ���
	doccnt=0#�ĵ�����
	listcnt=0#index����
	mywordsdict={}
	for onedoc in mydir:
		mylist=hwf.getmydoc(thepath,onedoc)
		onedocword=0#ÿ����������ı��е�λ��
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
		while fin <len(myindex) and myindex[fin][1]==i:#python��֧���߼���·
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

	�����ı�����
	'''

#-*-coding:utf-8-*-
#!/usr/bin/python
'''
avgdoclen=wordcnt/doccnt 平均文档长度

'''
import mydate
import math
import pdb
def VSM():
	maxnum=0
	#print mydate.myfindindex
	for i in mydate.myfindindex:
		if(i in mydate.queryTF):
			mydate.queryTF[i]+=1
		else:
			mydate.queryTF[i]=1
		if(maxnum<mydate.queryTF[i]):
			maxnum=mydate.queryTF[i]
	for k in mydate.queryTF:
		#mydate.queryTF[k]=(mydate.queryTF[k]+0.0)/maxnum
		#pdb.set_trace()
		mydate.docIDF[k]=math.log((mydate.doccnt+1.0)/mydate.mywords[k][2],math.e)*(mydate.queryTF[k]+0.0)/mydate.avgdoclen#/maxnum
	a={}
	for i in mydate.mydocs:
		tmp=0
		for k in mydate.queryTF:
			j=mydate.mywords[k][1]
			#pdb.set_trace()
			while(j<mydate.antimywordsdict[k] and mydate.myindex[j][0]<i):
				j+=1
			tmp+=(math.log(math.log(mydate.myindex[j][2],math.e)+1,math.e)+1)*mydate.docIDF[k]
		a[i]=tmp
	mydate.ansSort=sorted(a.items(), key=lambda a:a[1],reverse=True)
	'''
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
'''
计算query中的TF
'''
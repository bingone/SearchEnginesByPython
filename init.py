#-*-coding:utf-8-*-
#!/usr/bin/python
import mydate
import pickle


def basic_init():
	out=open("myindex.dat","rb")
	mydate.myindex=pickle.load(out)
	out=open("mywords.dat","rb")
	mydate.mywords=pickle.load(out)
	out=open("mydir.dat","rb")
	mydate.mydir=pickle.load(out)
	out=open("mywordsdictindex.dat","rb")
	mydate.mywordsdictindex=pickle.load(out)
	out=open("antimywordsdict.dat","rb")
	mydate.antimywordsdict=pickle.load(out)
	out=open("mywordsdict.dat","rb")
	mydate.mywordsdict=pickle.load(out)
	out=open("basic.dat","rb")
	mydate.wordcnt,mydate.doccnt,mydate.listcnt,mydate.totword,mydate.avgdoclen=pickle.load(out)
def usu_init():
	mydate.mypos=[]
	mydate.mydocs=[]
	mydate.myfindindex=[]
	mydate.mydoc=0
	mydate.direct=0
	mydate.queryTF={}
	mydate.docTF={}
	mydate.docIDF={}
	mydate.ansSort=[]
	mydate.searchword=[]

def init():
	mydate.queryTF={}
	mydate.docTF={}
	mydate.docIDF={}
	mydate.ansSort=[]

	mydate.mydir=[]
	mydate.mywords=[]
	mydate.myindex=[]

	mydate.mywordsdictindex={}
	mydate.antimywordsdict={}
	mydate.mywordsdict={}

	mydate.wordcnt=0#dict�еĸ���
	mydate.doccnt=0#�ĵ�����
	mydate.listcnt=0#index����
	mydate.totword=0#�ܴ���
	mydate.avgdoclen=0#ƽ���ĵ�����

	mydate.mypos=[]#ÿ���ʲ�ѯ��ǰλ��
	mydate.mydocs=[]#��ѯ���
	mydate.mydoc=0#��ѯ�ĵ�������
	mydate.direct=0#��ѯ����

	mydate.searchword=[]#��ѯ��
	mydate.myfindindex=[]#��ѯ�ʵ�mywords�±�
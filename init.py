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

	mydate.wordcnt=0#dict中的个数
	mydate.doccnt=0#文档个数
	mydate.listcnt=0#index个数
	mydate.totword=0#总词数
	mydate.avgdoclen=0#平均文档长度

	mydate.mypos=[]#每个词查询当前位置
	mydate.mydocs=[]#查询结果
	mydate.mydoc=0#查询文档迭代器
	mydate.direct=0#查询方向

	mydate.searchword=[]#查询词
	mydate.myfindindex=[]#查询词的mywords下标
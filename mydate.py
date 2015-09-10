#-*-coding:utf-8-*-
#!/usr/bin/python

'''
数据结构
建立索引
mydir   文档列表
onedoc  每一个文档
mydoc   当前查询的文档

mywords 建立索引的字典 0 是单词 1是起始下标 2是DF 
myindex 0 文档下标 1 单词下标 2 次数 3...
wordcntdict中的个数 doccnt文档个数


三个字典
mywordsdictindex  单词编号 起始位置
antimywordsdict   单词编号 结束位置
mywordsdict       单词->单词编号

查询
mypos是每个的单词起始的index下标
myfindindex是每个单词的标号，
mydocs 查询到的文档号

queryTF 查询的TF
docTF   文档的TF
docIDF  文档的IDF
ansSort 最终排序

'''
queryTF={}
docTF={}
docIDF={}
ansSort=[]

mydir=[]
mywords=[]
myindex=[]

mywordsdictindex={}
antimywordsdict={}
mywordsdict={}

wordcnt=0#dict中的个数
doccnt=0#文档个数
listcnt=0#index个数
totword=0#总词数
avgdoclen=0#平均文档长度

mypos=[]#每个词查询当前位置
mydocs=[]#查询结果
mydoc=0#查询文档迭代器
direct=0#查询方向

searchword=[]#查询词
myfindindex=[]#查询词的mywords下标
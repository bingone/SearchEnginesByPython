# SearchEnginesByPython
##1.基本情况
实现功能主要是构建索引、查询处理、引入VSM计算IDF并排序给出结果。

由于时间关系没有引入网络爬虫直接从网上下数据，使用的是文本信息。

##2.程序文件说明

使用cmd.bat会更快

work.py      程序入口，主文件

init.py          初始化一些参数

hwf.py  查询处理

VSM.py  VSM模型计算

createindex.py 创建索引

##3.生成数据文件说明
basic.dat    基本参数

mydir.dat    文本目录

myindex.dat  索引

mywords.dat  单词表

mywordsdict.dat 单词->单词编号

mywordsdictindex.dat 单词编号->起始位置

-------------------------
I write this project in 2014.11 and upload in 2015.9

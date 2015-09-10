#-*-coding:utf-8-*-
#!/usr/bin/python
import hwf
import mydate
import createindex
import VSM
import init
import sys
import os
import pprint
import pickle
import pdb

#pdb.set_trace()
#init.init()

tmpdir=os.listdir(".")
if("basic.dat" not in tmpdir or 1):
	init.init()
	createindex.createindex('../testtxt')#创建索引

else:
	init.basic_init()
while(True):
	hwf.getwords()#查询单词
	cnt=0
	for k ,v in mydate.ansSort:
		cnt+=1
		print mydate.mydir[k],v
	print "result count=",cnt
	

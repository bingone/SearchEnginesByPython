#-*-coding:utf-8-*-
#!/usr/bin/python

'''
���ݽṹ
��������
mydir   �ĵ��б�
onedoc  ÿһ���ĵ�
mydoc   ��ǰ��ѯ���ĵ�

mywords �����������ֵ� 0 �ǵ��� 1����ʼ�±� 2��DF 
myindex 0 �ĵ��±� 1 �����±� 2 ���� 3...
wordcntdict�еĸ��� doccnt�ĵ�����


�����ֵ�
mywordsdictindex  ���ʱ�� ��ʼλ��
antimywordsdict   ���ʱ�� ����λ��
mywordsdict       ����->���ʱ��

��ѯ
mypos��ÿ���ĵ�����ʼ��index�±�
myfindindex��ÿ�����ʵı�ţ�
mydocs ��ѯ�����ĵ���

queryTF ��ѯ��TF
docTF   �ĵ���TF
docIDF  �ĵ���IDF
ansSort ��������

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

wordcnt=0#dict�еĸ���
doccnt=0#�ĵ�����
listcnt=0#index����
totword=0#�ܴ���
avgdoclen=0#ƽ���ĵ�����

mypos=[]#ÿ���ʲ�ѯ��ǰλ��
mydocs=[]#��ѯ���
mydoc=0#��ѯ�ĵ�������
direct=0#��ѯ����

searchword=[]#��ѯ��
myfindindex=[]#��ѯ�ʵ�mywords�±�
#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'
# д�룺 alllinkfile  notsinglelinkfile  alllinkstrfile  : ���߷�����tweet @ ��������ͼ
# ͨ��tweet֮���@��ϵ���õ���Ҫ����Ϣ

# attempt to open file for reading
hyperlinkcount=0#��������
authorset=set()#��״̬�����߼��ϣ�setȥ���ظ�����
atauthorset=set()#״̬�б�@�����߼��ϣ�setȥ���ظ�����
authornotsingleset=set()#���ǹ���������߼���
name2number={}#�������ֵ�tweet�ŵ�ӳ��


# ��ȡ�������֣�authornamefilereader
# ��ȡtweet���ݣ�contentfilereader
# ��ȡtweet id(936467521)��tweetidfilereader
# ��ȡ����nick name��authornicknamefilereader
# ��ȡtweet �������ڣ�pubdatefilereader
# ��ȡÿ��tweet����б�ǩ tweetsentimentfilereader

try:
    #authornameÿ��tweet�������б����ظ���
    authornamefilereader=open('Z:\\TweetAnalysisSeries\\test','r')
    contentfilereader=open('Z:\\TweetAnalysisSeries\\test','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachLine in authornamefilereader:
        eachLine=eachLine.strip('\n').split('\t')
        # authorset ���߼���ȥ�����ظ������ߣ�
        # name2number ����-��� �ֵ�
        if eachLine[1] not in authorset:
            authorset.add(eachLine[1])
            name2number[eachLine[1]]=i
            i=i+1
    authornamefilereader.close()
#print authorset

    
# ����content ��ѯcontent�е�@��Ϣ��Ȼ�����@���������Ϣ���õ�@������
for contentsline in contentfilereader:
    temp=contentsline.strip('\n').split('\t')
    content=temp[4]
    author=temp[1]
    if len(content)!=0:
        startpos=content.find('@')
        while startpos!=-1:
            endpos=content.find(' ',startpos)
            # name �� @�������������
            if endpos!=-1:
                name=content[startpos+1:endpos]
                
                content=content[endpos:len(content)]
                #print contentline
            else:
                name=content[startpos+1:len(content)]

            # author����contentÿ��tweet�ķ����ˣ�name��content�а���������
            if name in authorset:
                atauthorset.add(name)
                atauthorset.add(author)
            if endpos==-1:
                break
            else:
                startpos=content.find('@')

print atauthorset
authornamefilereader.close()
contentfilereader.close()


tweetsreader=open('Z:\\TweetAnalysisSeries\\test','r')
tweetidwriter=open('Z:\\TweetAnalysisSeries\\tweetid','w')
authorwriter=open('Z:\\TweetAnalysisSeries\\author','w')
publishtimewriter=open('Z:\\TweetAnalysisSeries\\publishtime','w')
contentwriter=open('Z:\\TweetAnalysisSeries\\content','w')
for lines in tweetsreader:
    line=lines.strip('\n').split('\t')
    tweetid=line[0]
    authorcontent=line[1]
    publishtime=line[3]
    content=line[4]
    if authorcontent in atauthorset:
        tweetidwriter.write(tweetid+"\n")
        authorwriter.write(authorcontent+"\n")
        publishtimewriter.write(publishtime+"\n")
        contentwriter.write(content+"\n")
tweetidwriter.flush(),tweetidwriter.close()
authorwriter.flush(),authorwriter.close()
publishtimewriter.flush(),publishtimewriter.close()
contentwriter.flush(),contentwriter.close()

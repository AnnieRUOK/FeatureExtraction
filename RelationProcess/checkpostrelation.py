#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'

#   ͨ��content��author.name��author.nickname�����ļ��õ�tweet֮���relation



#   ���������б�Ԫ��д�뵽�ļ���
def listwrite2file(tweetrelationfilewriter,authorname2tweetNos):
    for content in authorname2tweetNos:
        tweetrelationfilewriter.write(str(content))
        tweetrelationfilewriter.write(str(" "))
                     


# attempt to open file for reading

#��״̬�����߼��ϣ�setȥ���ظ�����
authorset=set()
authornicknameset=set()
#nickname��authorname��ӳ��
nickname2authorname={}
#�������ֵ�tweet�ŵ�ӳ��
authorname2tweetNo={}

try:
    #authornameÿ��tweet�������б����ظ���
    authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
#    authornicknamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ʵ������Ԥ����\\Obama\\author.nickname','r')
except IOError,e:
    print ("***  file open error:",e)
else:
    # �������������ļ��������ߵ����ִ��뵽���߼����У�ȥ���ظ����ߣ���ͬʱ����¼ÿ�����߷�����tweet״̬��
    tweetNo=1
    for authorname in authornamefilereader:
        authorname=authorname.strip('\n')
#        nickname=authornicknamefilereader.readline()
#        nickname=nickname.strip('\n')
#        if len(nickname)!=0:
#            authornicknameset.add(nickname)
#            nickname2authorname[nickname]=authorname
        #   �����ǰ���߲����������߼��У���ô�ͽ�������ӵ����߼������ҳ�ʼ�����ߵ�tweetNo��ӳ��
        #   ����˵������֮ǰ�Ѿ���ӹ���ֱ�ӽ����߷�����tweetNo��ӵ�֮ǰ��ӵ�tweetNo����
        if authorname not in authorset:
            authorset.add(authorname)
            authorname2tweetNo[authorname]=[tweetNo]
        else:
            authorname2tweetNo[authorname].append(tweetNo)
        tweetNo=tweetNo+1
    authornamefilereader.close()
#    authornicknamefilereader.close()

#   �õ��Ľṹ�壺
#   authorset authornicknameset ���߼���
#   nickname2authorname  nickname��authorname��ӳ��
#   authorname2tweetNo  �������ֵ�tweet�ŵ�ӳ��

#   ����ÿһ��tweet content����ѯcontent�е�@���ţ�����@������s
#   Ȼ��ͨ���ֵ伯authorname2tweetNo ��ѯ�����߷���tweets����¼���ļ���
try:
    contentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\content','r')
    tweetrelationfilewriter = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','w')
except IoError,e:
    print ("*** contentfilereader file open error:",e)
else:
    tweetNo=1
    for content in contentfilereader:
        content = content.strip('\n')
        tweetNo=tweetNo+1
        if len(content)!=0:
             startpos=content.find('@')
             while startpos!=-1:
                endpos=content.find(' ',startpos)
                if endpos!=-1:
                     atauthorname=content[startpos+1:endpos]
                     content=content[endpos:len(content)]
                else:
                     atauthorname=content[startpos+1:len(content)]
#                atauthorname = atauthorname.strip(":")

                # �������߷�����tweetNo������ļ���
                if atauthorname in authorset:
                    listwrite2file(tweetrelationfilewriter,authorname2tweetNo[atauthorname])
                elif atauthorname in authornicknameset:
                    listwrite2file(tweetrelationfilewriter,authorname2tweetNo[authornicknameset[atauthorname]])
                if endpos==-1:
                     break
                else:
                    startpos=content.find('@')
        tweetrelationfilewriter.write('\n')
    contentfilereader.close();

tweetrelationfilewriter.flush()
tweetrelationfilewriter.close()
                    

                


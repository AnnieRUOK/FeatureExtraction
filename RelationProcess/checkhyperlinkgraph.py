#!/usr/bin/env python
# -*- coding: cp936 -*-
from __future__ import division  
'readTextFile.py -- read and display text file'
# д�룺 alllinkfile  notsinglelinkfile  alllinkstrfile  : ���߷�����tweet @ ��������ͼ
# ͨ��tweet֮���@��ϵ���õ���Ҫ����Ϣ

# attempt to open file for reading
hyperlinkcount=0#��������
authorset=set()#��״̬�����߼��ϣ�setȥ���ظ�����
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
    authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
    contentfilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\content','r')
    #tweetidfilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweet.id','r')
    #authornicknamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.nickname','r')
    pubdatefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\pub.date.GMT','r')
    tweetsentimentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\sentiment','r')
    
    alllinkfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\alllink.net','w')
    notsinglelinkfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\notsinglelink.net','w')
    alllinkstrfile=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\alllinkstr','w')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachLine in authornamefilereader:
        eachLine=eachLine.strip('\n')
        # authorset ���߼���ȥ�����ظ������ߣ�
        # name2number ����-��� �ֵ�
        if eachLine not in authorset:
            authorset.add(eachLine)
            name2number[eachLine]=i
            i=i+1
    authornamefilereader.close()
#print authorset
authornamefilereader=open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\author.name','r')
alllinkfile.write("*Vertices"+' '+str(len(authorset))+'\n')

# �����ߵı�ź����ߵ���������� alllinkfile
i=1
for author,number in name2number.items():
    alllinkfile.write(' '+str(number)+' '+author+'\n')
    i=i+1

alllinkfile.write("*Arcs"+'\n')
notsinglelinkfile.write("*Arcs"+'\n')
# ����content ��ѯcontent�е�@��Ϣ��Ȼ�����@���������Ϣ���õ�@������
for contentline in contentfilereader:
    author=authornamefilereader.readline()
    author=author.strip('\n')
    if len(contentline)!=0:
        startpos=contentline.find('@')
        while startpos!=-1:
            endpos=contentline.find(' ',startpos)
            # name �� @�������������
            if endpos!=-1:
                name=contentline[startpos+1:endpos]
                
                contentline=contentline[endpos:len(contentline)]
                #print contentline
            else:
                name=contentline[startpos+1:len(contentline)]

            # author����contentÿ��tweet�ķ����ˣ�name��content�а���������
            # authornotsingleset �洢���ڹ����ߵ�@ ���ߣ����ǹ������ߵ�
            # alllinkstrfile �洢����֮���@ direct��ϵ����author @ ��name
            # alllinkfile 
            if name in authorset:
                authornotsingleset.add(author)
                authornotsingleset.add(name)
                alllinkstrfile.write(' '+author+' ')
                alllinkstrfile.write(name+'\n')
                alllinkfile.write(' '+str(name2number[author])+' ')
                alllinkfile.write(str(name2number[name])+'\n')

                notsinglelinkfile.write(' '+str(name2number[author])+' ')
                notsinglelinkfile.write(str(name2number[name])+'\n')
                hyperlinkcount=hyperlinkcount+1
            if endpos==-1:
                break
            else:
                startpos=contentline.find('@')


# ��ϵͼָ��ļ���
print '����������'
print hyperlinkcount
print 'ratio : '
setsize=len(authorset)
fulllink=setsize*(setsize-1)/2;
ratio=hyperlinkcount/fulllink
print ratio
alllinkfile.flush()
alllinkfile.close()
alllinkstrfile.flush()
alllinkstrfile.close()
print '��author����:'
print len(authorset)
print '�Ƕ���������'
print len(authornotsingleset)

#print authornotsingleset



#���ֻ�зǶ������ͼ�Ķ���

notsinglelinkfile.write("*Vertices"+' '+str(len(authornotsingleset))+'\n')
for nonsingleauthor in authornotsingleset:
    notsinglelinkfile.write(' '+str(name2number[nonsingleauthor])+' '+nonsingleauthor+'\n')

notsinglelinkfile.flush()
notsinglelinkfile.close()
    

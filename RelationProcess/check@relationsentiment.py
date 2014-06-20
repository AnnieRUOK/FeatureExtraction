#!/usr/bin/env python
# -*- coding: cp936 -*-

from __future__ import division  
'readTextFile.py -- read and display text file'
import string
# ͨ������relation��ϵ�ļ���sentiment��б���ļ����õ�direct��mutial @��ϵ�����һ���Աȶ�

maxTweetNo=90000000
        

# tweetNo��ÿ��tweet����б�ǵ�ӳ��
tweetNo2sentiment={}
Num_positive=0
Num_neturl=0
Num_negative=0
try:
    sentimentfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\sentiment','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    i=1
    for eachline in sentimentfilereader:
        eachline = eachline.strip('\n')
        tweetNo2sentiment[i]=eachline
        if eachline == "positive":
            Num_positive = Num_positive +1
        elif eachline == "neutral":
            Num_neturl = Num_neturl +1
        elif eachline == "negative":
            Num_negative = Num_negative +1
        i=i+1
    sentimentfilereader.close()

# ��tweets֮���@��ϵ������
tweetNo2tweetNos={}
try:
    relationreader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    tweetNo = 0
    for eachline in relationreader:
        tweetNo = tweetNo+1
        eachline = eachline.strip('\n')
        tweetNo2tweetNos[tweetNo] = eachline
    relationreader.close()

# direct@ ���һ������
Num_directat=0 #@�ߣ�����tweet���һ�µ�����
Num_directatPositive=0#@�ߣ�����tweet���һ�£�����Ϊ��������� 
Num_directatNegative=0#@�ߣ�����tweet���һ�£�����Ϊ��������� 
Num_directatNetural=0#@�ߣ�����tweet���һ�£�����Ϊ��������� 
TotalNum_directat=0#�ܵ�@����
Num_mutialat=0#����@�ߣ�����tweet���һ�µ�����
TotalNum_mutialat=0#����@���ܱ���

TotalNum_directatNonNetural=0#@�����������ǲ���������
Num_directatPositive=0 #@�ߣ�����tweet���һ�£�����Ϊ���࣬���ǲ���������
Num_directatNegative=0 #@�ߣ�����tweet���һ�£�����Ϊ���࣬���ǲ���������


number_all_parentssentiment=0 #��ǰtweet������������ߣ�tweet��С��������к�
number_parents=0
number_all_childrensentiment=0 #��ǰtweet������������ߣ�tweet�Ŵ���������к�
number_children=0
number_one_parensentiment=0 #��ǰtweet������������ߣ�tweet��С��������������������
number_one_parent=0
number_one_child=0
number_one_childsentiment=0 #��ǰtweet������������ߣ�tweet�Ŵ���������������������
try:
    relationfilereader = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\tweetrelation','r')
except IOError,e:
    print ("*** authorname file open error:",e)
else:
    tweetNo = 0
    for eachline in relationfilereader:
        tweetNo=tweetNo+1
        eachline = eachline.strip('\n')
        if eachline =='':
            continue
        minparentNo=-1
        maxchildNo=maxTweetNo
        numbers = eachline.split(' ')
        for number in numbers:
            if number =='':
                continue
            # ���Ǳ��ֵ����������Ĳ�ͬ����£����һ�µĸ���
            
            if string.atoi(number) < tweetNo:
                #parent
                if string.atoi(number) > minparentNo:
                    minparentNo=string.atoi(number)
                number_parents= number_parents+1
                if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                    number_all_parentssentiment=number_all_parentssentiment+1
            if string.atoi(number) > tweetNo: #child
                if string.atoi(number) < maxchildNo:
                    maxchildNo=string.atoi(number)
                number_children = number_children+1
                if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                    number_all_childrensentiment=number_all_childrensentiment+1
            
            

            TotalNum_directat=TotalNum_directat+1
            if tweetNo2sentiment[tweetNo] != "neutral" and  tweetNo2sentiment[string.atoi(number)]!="neutral":
                TotalNum_directatNonNetural = TotalNum_directatNonNetural+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[string.atoi(number)]:
                Num_directat=Num_directat+1
                if tweetNo2sentiment[tweetNo]=="positive":
                    Num_directatPositive = Num_directatPositive+1
                elif tweetNo2sentiment[tweetNo]=="neutral":
                    Num_directatNetural = Num_directatNetural+1
                elif tweetNo2sentiment[tweetNo]=="negative":
                    Num_directatNegative = Num_directatNegative+1
            # �ж� number����tweet�Ƿ�@��tweetNo����tweet
            if str(tweetNo) in tweetNo2tweetNos[string.atoi(number)].split(' '):
                TotalNum_mutialat=TotalNum_mutialat+1
                if tweetNo2sentiment[string.atoi(number)] == tweetNo2sentiment[tweetNo]:
                    
                    Num_mutialat=Num_mutialat+1
        #  minparentNo , maxchildNo
        if minparentNo != -1:
            number_one_parent = number_one_parent+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[minparentNo]:
                number_one_parensentiment=number_one_parensentiment+1
        if maxchildNo != maxTweetNo:
            number_one_child = number_one_child+1
            if tweetNo2sentiment[tweetNo] == tweetNo2sentiment[maxchildNo]:
                number_one_childsentiment=number_one_childsentiment+1
            
    relationfilereader.close()
#statisticfilewriter = open('F:\\_Galaxysvn\\TweetSentimentAnalysisSeries\\ExperimentData\\PythonWorkSpaceInPreprocess\\tacobell\\beforepreprocess\\output\\directat','w')
print "Num_directatPositive:",Num_directatPositive,"Num_directatNetural:",Num_directatNetural,"Num_directatNegative:",Num_directatNegative
print "Num_directat:",Num_directat,"TotalNum_directatNonNetural",TotalNum_directatNonNetural,"TotalNum_directat:",TotalNum_directat
print "��Num_directatPositive+Num_directatNegative��/TotalNum_directatNonNetural",(Num_directatPositive+Num_directatNegative)/TotalNum_directatNonNetural,"Num_directat/TotalNum_directat:",Num_directat/TotalNum_directat
print Num_mutialat,TotalNum_mutialat,Num_mutialat/TotalNum_mutialat
print "Num_positive:",Num_positive,"Num_neturl:",Num_neturl,"Num_negative:",Num_negative,"Random direct: ",pow(Num_positive/3232,2)+pow(Num_neturl/3232,2)+pow(Num_negative/3232,2)
print "random direct without netural:",pow(Num_positive/(Num_positive+Num_negative),2)+pow(Num_negative/(Num_positive+Num_negative),2)

print "number_all_parentssentiment/number_parents:",number_all_parentssentiment/number_parents
print "number_all_childrensentiment/number_children",number_all_childrensentiment/number_children
print "number_one_parensentiment/number_one_parent",number_one_parensentiment/number_one_parent
print "number_one_childsentiment/number_one_child",number_one_childsentiment/number_one_child
#statisticfilewriter.flush()
#statisticfilewriter.close()

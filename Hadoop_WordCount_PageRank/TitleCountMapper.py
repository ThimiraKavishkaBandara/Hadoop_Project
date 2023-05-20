#!/usr/bin/env python3
import re
import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
with open(stopWordsPath) as f:
    # TODO
        stopWords = f.read()
        stopWords = stopWords.split()
        # print(stopWords)



#TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read()
    regex = ' |\t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|\_|\*|\/|\s|\|'
    # print(regex)
    # print(delimiters)



test = []
for line in sys.stdin:
    titles = re.split(regex,line)                         
    for title in titles:
        title = title.lower().strip()                     #continue cleaning (lower case) and flatten list
        if not title in stopWords:                        #only append words that are not in the stopwords list
                test.append(title)

test = [j for j in test if j]                             #remove any empty items from list ('')
#srt_list = sorted(test)


  
    # TODO
for word in test: #srt_list:
     print('%s\t%s' % (word,1))
    # print('%s\t%s' % (  ,  )) pass this output to reducer



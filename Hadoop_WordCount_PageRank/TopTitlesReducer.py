#!/usr/bin/env python3
import sys



# input comes from STDIN
tlist = []
for line in sys.stdin:
    # TODO
    line = line.strip()
    wordCount= line.split('\t')
    tlist.append(wordCount)
top5 = tlist[0:10]
top5.reverse()
for item in top5:
    print('%s\t%s' % (item[0],item[1]))


# print(res)
    #print(res) 
    # print('%s\t%s' % (  ,  )) print as final output
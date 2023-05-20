#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
word = None
count = 0



# input comes from STDIN
# res = {}
# for line in sys.stdin:
#     # TODO
#     line = line.strip()
# DICTIONARY METHOD  
    # word, count = line.split('\t')
    # if word in res:
    #     res[word] = res.get(word, int(count)) + 1 
    # else:
    #     res[word]= int(count)




res = {}
for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t', 1)
    if word in res:
        res[word] = res.get(word,int(count))+ 1
    else:
        res[word] = int(count)
    
sorted_res = dict(sorted(res.items(), key = lambda x: (-x[1],x[0])))
#print(sorted_res)
        

    # TODO

# TODO
# print('%s\t%s' % (  ,  )) print as final output

for w, c in sorted_res.items():
    print('%s\t%s' % (w,c))

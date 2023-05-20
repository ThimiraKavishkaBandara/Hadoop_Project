#!/usr/bin/env python3
import sys
from operator import itemgetter


# TODO

alist = []
for line in sys.stdin:
       line = line.strip()
       word, count = line.split('\t')

#TODO
       print('%s\t%s' % (word , count)) 
       

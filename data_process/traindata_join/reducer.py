#!/usr/bin/env python
from operator import itemgetter
#split by ','
import sys

def reducer():
    lastuid = ""
    for line in sys.stdin:
        if line.strip() == "":
            continue
        fields = line.split("\t", 1)
        uid = fields[0].strip().split()[0]
        uid_flag = fields[0].strip().split()[1][-1]
        if uid != lastuid and uid_flag == "1":
            data2 = fields[1].strip()
        elif uid == lastuid and uid_flag == "2":
            data1 = '\t'.join(fields[1].strip().split('\t')[:-1])
            label = fields[1].strip().split('\t')[-1]
            if label == "-1":
                label = '0'
            if data2:
                print '\t'.join(("uid " + lastuid, data1, data2, "label " + label))
        lastuid = uid

if __name__ == '__main__':
    reducer()
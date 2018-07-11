#!/usr/bin/env python
from operator import itemgetter

import sys

def reducer():
    lastuid = ""

    for line in sys.stdin:
        if line.strip() == "":
            continue
        fields = line.split("\t", 1)
        uid = fields[0].strip().split()[0].strip()
        uid_flag = fields[0].strip().split()[1][-1]
        if uid != lastuid and uid_flag == "1":
            data2 = fields[1].strip()
        elif uid == lastuid and uid_flag == "2":
            data1 = fields[1].strip()
            if data2:
                print '\t'.join((lastuid, data1, data2))
        elif uid_flag == "2":
            pass
        lastuid = uid

if __name__ == '__main__':
    reducer()
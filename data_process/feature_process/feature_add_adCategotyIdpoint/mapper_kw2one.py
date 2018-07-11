#!/usr/bin/env python
from operator import itemgetter
import os
import sys

def mapper():
    for line in sys.stdin:
        if line.strip() == '':
            continue
        fields = line.split('\t')
        aid = fields[1].split()[-1].strip()
        adCategoryId = fields[2].split()[-3].strip()
        #label = fields[-1].split()[-1].strip()
        #if label == '-1':
        #    label = '0'
        newline = []
        kw_point = 0
        for i in range(len(fields)):
            if "kw1" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    kwId_adCId = "adCategoryId kw1 " + field_i_split[j] + " " + adCategoryId
                    kw_point += float(dict_kw.get(kwId_adCId, 0))
            elif "kw2" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    kwId_adCId = "adCategoryId kw2 " + field_i_split[j] + " " + adCategoryId
                    kw_point += float(dict_kw.get(kwId_adCId, 0))
            elif "kw3" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    kwId_adCId = "adCategoryId kw3 " + field_i_split[j] + " " + adCategoryId
                    kw_point += float(dict_kw.get(kwId_adCId, 0))
            else:
                newline.append(fields[i].strip())
        #print "\t".join(newline[:-1]) + "\t" + "kw_point " + str(kw_point) + "\t" + "label " + label
        print "\t".join(newline) + "\t" + "kw_point " + str(kw_point)
if __name__ == '__main__':
    mapper()

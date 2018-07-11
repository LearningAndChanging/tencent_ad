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
        #   label = '0'
        newline = []
        appIdAction_point = 0
        for i in range(len(fields)):
            if "appIdAction" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    appIdActionId_adCId = "adCategoryId appIdAction " + field_i_split[j] + " " + adCategoryId
                    appIdAction_point += float(dict_appIdAction.get(appIdActionId_adCId, 0))
            else:
                newline.append(fields[i].strip())
        #print "\t".join(newline[:-1]) + "\t" + "appIdAction_point " + str(appIdAction_point) + "\t" + "label " + label
        print "\t".join(newline) + "\t" + "appIdAction_point " + str(appIdAction_point)
if __name__ == '__main__':
    mapper()

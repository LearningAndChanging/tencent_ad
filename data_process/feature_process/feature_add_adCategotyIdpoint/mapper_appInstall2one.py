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
        appIdInstall_point = 0
        for i in range(len(fields)):
            if "appIdInstall" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    appIdInstallId_adCId = "adCategoryId appIdInstall " + field_i_split[j] + " " + adCategoryId
                    appIdInstall_point += float(dict_appIdInstall.get(appIdInstallId_adCId, 0))
            else:
                newline.append(fields[i].strip())
        #print "\t".join(newline[:-1]) + "\t" + "appIdInstall_point " + str(appIdInstall_point) + "\t" + "label " + label
        print "\t".join(newline) + "\t" + "appIdInstall_point " + str(appIdInstall_point)
if __name__ == '__main__':
    mapper()

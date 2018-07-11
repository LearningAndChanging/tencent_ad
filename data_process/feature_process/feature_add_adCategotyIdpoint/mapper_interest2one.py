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
        interest_point = 0
        for i in range(len(fields)):
            if "interest1" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    interestId_adCId = "adCategoryId interest1 " + field_i_split[j] + " " + adCategoryId
                    interest_point += float(dict_interest.get(interestId_adCId, 0))
            elif "interest2" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    interestId_adCId = "adCategoryId interest2 " + field_i_split[j] + " " + adCategoryId
                    interest_point += float(dict_interest.get(interestId_adCId, 0))
            elif "interest3" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    interestId_adCId = "adCategoryId interest3 " + field_i_split[j] + " " + adCategoryId
                    interest_point += float(dict_interest.get(interestId_adCId, 0))
            elif "interest4" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    interestId_adCId = "adCategoryId interest4 " + field_i_split[j] + " " + adCategoryId
                    interest_point += float(dict_interest.get(interestId_adCId, 0))
            elif "interest5" in fields[i]:
                field_i_split = fields[i].split()
                for j in range(1, len(field_i_split)):
                    interestId_adCId = "adCategoryId interest5 " + field_i_split[j] + " " + adCategoryId
                    interest_point += float(dict_interest.get(interestId_adCId, 0))
            else:
                newline.append(fields[i].strip())
        #print "\t".join(newline[:-1]) + "\t" + "interest_point " + str(interest_point) + "\t" + "label " + label
        print "\t".join(newline) + "\t" + "interest_point " + str(interest_point)
if __name__ == '__main__':
    mapper()

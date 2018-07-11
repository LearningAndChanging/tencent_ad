#!/usr/bin/env python
from operator import itemgetter
import os
import sys

def mapper():
    for line in sys.stdin:
        if line.strip() == '':
            continue
        if line.strip("\n"):
            fields = line.split('\t')
            aid = fields[1].split()[-1].strip()
            adCategoryId = fields[2].split()[-3].strip()
            #label = fields[-1].split()[-1].strip()
            #if label == '-1':
            #    label = '0'
            newline = []
            topic_point = 0
            for i in range(len(fields)):
                if "topic1" in fields[i]:
                    field_i_split = fields[i].split()
                    for j in range(1, len(field_i_split)):
                        topicId_adCId = "adCategoryId topic1 " + field_i_split[j] + " " + adCategoryId
                        topic_point += float(dict_topic.get(topicId_adCId, 0))
                elif "topic2" in fields[i]:
                    field_i_split = fields[i].split()
                    for j in range(1, len(field_i_split)):
                        topicId_adCId = "adCategoryId topic2 " + field_i_split[j] + " " + adCategoryId
                        topic_point += float(dict_topic.get(topicId_adCId, 0))
                elif "topic3" in fields[i]:
                    field_i_split = fields[i].split()
                    for j in range(1, len(field_i_split)):
                        topicId_adCId = "adCategoryId topic3 " + field_i_split[j] + " " + adCategoryId
                        topic_point += float(dict_topic.get(topicId_adCId, 0))
                else:
                    newline.append(fields[i].strip())
            #print "\t".join(newline[:-1]) + "\t" + "topic_point " + str(topic_point) + "\t" + "label " + label
            print "\t".join(newline[:]) + "\t" + "topic_point " + str(topic_point)
if __name__ == '__main__':
    mapper()

#!/usr/bin/env python
from operator import itemgetter
import os
import sys


def mapper():
    adFeature_list = ["aid", "advertiserId", "campaignId", "creativeId"]
    for line in sys.stdin:
        if line.strip() == '':
            continue
        fields = line.split('\t')
        aid = fields[1].split()[-1].strip()
        advertiserId = fields[2].split()[1].strip()
        campaignId = fields[2].split()[2].strip()
        creativeId = fields[2].split()[3].strip()
        label = fields[-1].split()[-1].strip()
        if label == '-1':
            label = '0'
        for i in range(1,len(fields)):
            for feature in adFeature_list:
                if feature == "aid":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest1 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest2 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest3 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest4 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest5 " + field_i_split[j] + " " + aid + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw1 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw2 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw3 " + field_i_split[j] + " " + aid + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic1 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic2 " + field_i_split[j] + " " + aid + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic3 " + field_i_split[j] + " " + aid + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdInstall " + field_i_split[j] + " " + aid + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdAction " + field_i_split[j] + " " + aid + " " + label, label))
                elif feature == "advertiserId":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest1 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest2 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest3 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest4 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest5 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw1 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw2 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw3 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic1 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic2 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic3 " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdInstall " + field_i_split[j] + " " + advertiserId + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdAction " + field_i_split[j] + " " + advertiserId + " " + label, label))
                elif feature == "campaignId":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest1 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest2 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest3 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest4 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest5 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw1 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw2 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw3 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic1 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic2 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic3 " + field_i_split[j] + " " + campaignId + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdInstall " + field_i_split[j] + " " + campaignId + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdAction " + field_i_split[j] + " " + campaignId + " " + label, label))
                elif feature == "creativeId":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest1 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest2 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest3 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest4 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " interest5 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw1 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw2 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw3 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic1 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic2 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic3 " + field_i_split[j] + " " + creativeId + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdInstall " + field_i_split[j] + " " + creativeId + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdAction " + field_i_split[j] + " " + creativeId + " " + label, label))
                
if __name__ == '__main__':
    mapper()

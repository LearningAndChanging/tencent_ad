#!/usr/bin/env python
from operator import itemgetter
import os
import sys


def mapper():
    adFeature_list = ["creativeSize", "adCategoryId", "productId", "productType"]
    for line in sys.stdin:
        if line.strip() == '':
            continue
        fields = line.split('\t')
        creativeSize = fields[2].split()[4].strip()
        adCategoryId = fields[2].split()[5].strip()
        productId = fields[2].split()[6].strip()
        productType = fields[2].split()[7].strip()
        label = fields[-1].split()[-1].strip()
        if label == '-1':
            label = '0'
        for i in range(1, len(fields)):
            for feature in adFeature_list:
                if feature == "creativeSize":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest1 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest2 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest3 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest4 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest5 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw1 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw2 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " kw3 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic1 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic2 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " topic3 " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdInstall " + field_i_split[j] + " " + creativeSize + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdAction " + field_i_split[j] + " " + creativeSize + " " + label, label))
                elif feature == "adCategoryId":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest1 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest2 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest3 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest4 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest5 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw1 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw2 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw3 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic1 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic2 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic3 " + field_i_split[j] + " " + adCategoryId + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdInstall " + field_i_split[
                                j] + " " + adCategoryId + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join((feature + " appIdAction " + field_i_split[
                                j] + " " + adCategoryId + " " + label, label))
                elif feature == "productId":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest1 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest2 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest3 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest4 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest5 " + field_i_split[j] + " " + productId + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw1 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw2 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw3 " + field_i_split[j] + " " + productId + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic1 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic2 " + field_i_split[j] + " " + productId + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic3 " + field_i_split[j] + " " + productId + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdInstall " + field_i_split[j] + " " + productId + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdAction " + field_i_split[j] + " " + productId + " " + label, label))
                elif feature == "productType":
                    if "interest1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest1 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "interest2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest2 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "interest3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest3 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "interest4" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest4 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "interest5" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " interest5 " + field_i_split[j] + " " + productType + " " + label, label))
                    if "kw1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw1 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "kw2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw2 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "kw3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " kw3 " + field_i_split[j] + " " + productType + " " + label, label))
                    if "topic1" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic1 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "topic2" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic2 " + field_i_split[j] + " " + productType + " " + label, label))
                    elif "topic3" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " topic3 " + field_i_split[j] + " " + productType + " " + label, label))
                    if "appIdInstall" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdInstall " + field_i_split[j] + " " + productType + " " + label, label))
                    if "appIdAction" in fields[i]:
                        field_i_split = fields[i].split()
                        for j in range(1, len(field_i_split)):
                            print '\t'.join(
                                (feature + " appIdAction " + field_i_split[j] + " " + productType + " " + label, label))


if __name__ == '__main__':
    mapper()

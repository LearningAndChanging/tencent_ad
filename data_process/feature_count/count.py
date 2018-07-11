#!/usr/bin/env python
from operator import itemgetter
import sys
import os
import math

def mapper():
    array_list = ['uid',
 'aid',
 'advertiserId',
 'campaignId',
 'creativeId',
 'creativeSize',
 'adCategoryId',
 'productId',
 'productType',
 'age',
 'gender_0',
 'gender_1',
 'gender_2',
 'marriageStatus_0',
 'marriageStatus_10',
 'marriageStatus_10_12_13',
 'marriageStatus_10_13',
 'marriageStatus_10_13_15',
 'marriageStatus_10_13_2',
 'marriageStatus_10_13_5',
 'marriageStatus_10_13_6',
 'marriageStatus_10_13_9',
 'marriageStatus_10_15',
 'marriageStatus_11',
 'marriageStatus_12_13',
 'marriageStatus_12_13_9',
 'marriageStatus_13',
 'marriageStatus_13_15',
 'marriageStatus_13_2',
 'marriageStatus_13_2_9',
 'marriageStatus_13_5',
 'marriageStatus_13_5_9',
 'marriageStatus_13_6',
 'marriageStatus_13_6_9',
 'marriageStatus_13_9',
 'marriageStatus_14',
 'marriageStatus_15',
 'marriageStatus_3',
 'marriageStatus_8',
 'education_0',
 'education_1',
 'education_2',
 'education_3',
 'education_4',
 'education_5',
 'education_6',
 'education_7',
 'consumptionAbility',
 'LBS',
 'appIdInstall_point',
 'appIdAction_point',
 'ct_0',
 'ct_1',
 'ct_1_2',
 'ct_1_2_3',
 'ct_1_2_3_4',
 'ct_1_2_4',
 'ct_1_3',
 'ct_1_3_4',
 'ct_1_4',
 'ct_2',
 'ct_2_3',
 'ct_2_3_4',
 'ct_2_4',
 'ct_3',
 'ct_3_4',
 'ct_4',
 'os_0',
 'os_1',
 'os_1_2',
 'os_2',
 'carrier_0',
 'carrier_1',
 'carrier_2',
 'carrier_3',
 'house',
 'interest_point',
 'topic_point',
 'kw_point',
 'label']


    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    for line in sys.stdin:
        if "single_feature_data" in filename:
            line = line.strip().strip("\n")
            if line and "id" not in line:
                words_raw = line.split('\t')
                if len(words_raw) == 80:
                    for i in range(2, len(words_raw)):
                        if i in [49, 50, 76, 77, 78]:
                            words_raw[i] = int(math.sqrt(float(words_raw[i]))*10)
                        if i in [j for j in range(10, 47)] + [j for j in range(51, 75)]:
                            if words_raw[i] != '0':
                                print '%s\t%s' % (array_list[i] + ' ' + str(words_raw[i]) + ' ' + words_raw[79], words_raw[79])
                        else:
                            print '%s\t%s' % (array_list[i] + ' ' + str(words_raw[i]) + ' ' + words_raw[79], words_raw[79])

if __name__ == "__main__":
    mapper()




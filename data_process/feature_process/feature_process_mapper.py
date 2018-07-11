#!/usr/bin/env python
from operator import itemgetter
import os
import sys
import math

def mapper():
    aid_datalist = ['177', '2050', '1716', '336', '671', '529', '927', '1714', '977', '450', '1749', '404', '302', '1202', '838',
     '1842', '875', '846', '1962', '1171', '1781', '1622', '1254', '231', '191', '113', '1057', '145', '1284', '86',
     '686', '1291', '853', '765', '2031', '1507', '2054', '1599', '1338', '1672', '1350', '1415', '420', '1021', '1931',
     '1925', '432', '1044', '117', '1930', '1950', '1621', '206', '2196', '121', '1508', '2068', '894', '1317', '1871',
     '471', '436', '174', '681', '1957', '1468', '1242', '1023', '1991', '1998', '1966', '903', '2154', '951', '1407',
     '1215', '1429', '1017', '647', '205', '2048', '1107', '966', '2216', '1904', '1277', '562', '272', '561', '164',
     '1375', '519', '1819', '1335', '960', '1847', '1503', '792', '2205', '1351', '1728', '1496', '369', '725', '727',
     '699', '313', '2197', '1027', '2047', '1119', '1449', '886', '1580', '975', '74', '136', '311', '1140', '1910',
     '7', '1827', '1483', '613', '1746', '1790', '1230', '692', '1596', '1671', '212', '543', '939', '932', '1379',
     '411', '2112', '18', '1970', '1894', '2201', '1841', '6', '516', '2066', '624', '1605', '1377', '914', '12',
     '2169', '1182', '70', '98', '1201', '286', '2118', '173', '1512', '748', '1566', '2044', '1085', '454', '916',
     '688', '660', '1635', '1918', '1530', '389', '1940', '2013']
    advertiserId_datalist = ['8203', '19441', '5552', '370', '45705', '10122', '79', '5758', '21359', '821', '18621', '452', '27367', '60',
     '8864', '25420', '17597', '8350', '11487', '25485', '388', '6841', '1082', '29704', '83042', '327', '915', '3993',
     '702', '7565', '133292', '2676', '7300', '11437', '18630', '58643', '41806', '990', '13915', '20943', '243',
     '14315', '9106', '7926', '728', '8494', '15174', '285', '22802', '47823', '5459', '10055', '9571', '2775', '21017',
     '44008', '2509', '7229', '66025', '11459', '8668', '43189', '23805', '3387', '75748', '9619', '6946', '24704',
     '1025', '149', '71505', '101662', '14818', '11195', '16770', '6937', '49772', '104071', '158679']
    campaignId_datalist = ['76104', '178687', '158101', '4833', '352827', '163352', '219802', '25739', '199508', '361928', '888', '745599',
     '47118', '131853', '95990', '128701', '310473', '262085', '135565', '51385', '244601', '159012', '50138', '134068',
     '154634', '159118', '696695', '40405', '60929', '280832', '358536', '31020', '63752', '12724', '110094', '353610',
     '464828', '692763', '243160', '36763', '18237', '33813', '18552', '407774', '233191', '51315', '23303', '445098',
     '10460', '115759', '73450', '38391', '15634', '734054', '80', '378648', '668182', '174407', '404', '994', '12711',
     '42104', '26003', '59293', '295567', '475236', '172796', '86429', '741453', '7527', '538818', '37818', '68476',
     '12128', '167166', '100565', '241577', '67127', '358059', '169332', '645468', '52258', '141893', '2295', '331396',
     '286844', '17378', '42625', '170445', '170485', '7686', '295940', '531344', '132657', '18296', '13953', '49189',
     '27030', '76011', '13044', '50305', '98158', '61383', '163957', '204378', '40877', '296367', '48236', '84178',
     '1123', '90700', '163120', '155063', '74452', '188857', '308103', '57846', '766460', '20048', '286065', '18683',
     '19215', '209098', '111645', '420987', '38402', '42614', '5616', '3372', '104406', '186348', '487541', '134120',
     '76252', '473537', '643438', '662422', '30399']
    creativeId_datalist = ['1500666', '245165', '1080850', '119845', '660519', '220558', '492484', '1608684', '1080962', '565415', '585909',
     '1353465', '1628574', '1083112', '1640724', '1211265', '832650', '1073411', '608495', '717054', '1606251',
     '838455', '1383456', '991964', '58465', '1202263', '1340722', '981822', '1758880', '416399', '1464074', '1434096',
     '154811', '1271219', '425385', '745048', '794412', '792238', '1147463', '942499', '1554384', '1334609', '1451219',
     '1249596', '1401261', '1765755', '1081485', '38299', '619519', '683342', '1016027', '1462184', '440096', '767513',
     '1494257', '1367823', '1661158', '43862', '480095', '1589088', '731893', '621766', '1512679', '1638352', '1513931',
     '1610899', '883304', '192305', '1441131', '1260597', '1116089', '210057', '1772271', '993205', '962151', '1360276',
     '641118', '1614385', '910853', '1040130', '240336', '476885', '666210', '1321733', '414738', '1205997', '864509',
     '1108416', '808799', '474978', '249293', '577602', '1562482', '1769240', '1655556', '1394962', '1230210',
     '1564743', '1149439', '1203413', '884105', '1673644', '1229175', '1485462', '1473655', '731679', '979528',
     '700445', '1266652', '20199', '798752', '1724522', '333622', '72027', '913588', '108752', '1187573', '27461',
     '1305307', '326633', '221432', '1236432', '418462', '546986', '287080', '1636465', '46884', '455396', '181137',
     '332490', '1083491', '1391569', '104188', '1806760', '469197', '220179', '750122', '857791', '797661', '638911',
     '477814', '904288', '1702986', '1106145', '1075635', '1735807', '1755470', '1146648', '141973', '1612095', '43877',
     '818363', '5977', '130171', '1172593', '131847', '1012717', '267290', '1246897', '202309', '520004', '869346',
     '644672', '1442655', '838056', '1753448', '1160702', '145496', '1690612', '1099732', '1354071', '530889',
     '1427984']
    creativeSize_datalist = ['59', '53', '35', '22', '42', '100', '91', '95', '93', '20', '105', '109', '77', '79', '60']
    adCategoryId_datalist = ['282', '1', '27', '67', '10', '21', '218', '25', '34', '43', '4', '59', '51', '13', '108', '70', '94', '74', '8',
     '24', '265', '125', '30', '204', '142', '48', '179', '102', '192', '81', '149', '137', '121', '40', '22', '100',
     '77', '140', '89', '9']
    productId_datalist = ['0', '113', '3733', '1455', '439', '12193', '16791', '3194', '25730', '15454', '19256', '4669', '5615', '27855',
     '13727', '38', '11636', '4666', '5336', '1313', '6131', '4772', '7992', '28986', '14314', '3826', '3794', '24947',
     '542', '70', '17614', '9760', '3791']
    productType_datalist = ['6', '9', '4', '11']
    age_datalist = [str(x) for x in range(6)]
    consumptionAbility_datalist = ['0', '1', '2']
    LBS_datalist = ['null','258', '309', '424', '471', '66', '802', '978']
    house_datalist = ['0', '1']
    gender_edu_datalist = ['gender_0',
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
                           'education_7']
    ct_carrier_datalist = ['ct_0',
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
                           'carrier_3']
    appIdInstall_point_title = ['appInstall_point0',
                                'appInstall_point1',
                                'appInstall_point2',
                                'appInstall_point3',
                                'appInstall_point4',
                                'appInstall_point5',
                                'appInstall_point6']
    appIdAction_point_title = ['appIdAction_point0',
                               'appIdAction_point1',
                               'appIdAction_point2',
                               'appIdAction_point3',
                               'appIdAction_point4',
                               'appIdAction_point5']
    interest_point_title = ['interest_point0',
                            'interest_point1',
                            'interest_point2',
                            'interest_point3',
                            'interest_point4',
                            'interest_point5',
                            'interest_point6']
    topic_point_title = ['topic_point0',
                         'topic_point1',
                         'topic_point2',
                         'topic_point3',
                         'topic_point4',
                         'topic_point5',
                         'topic_point6']
    kw_point_title = ['kw_point0',
                      'kw_point1',
                      'kw_point2',
                      'kw_point3',
                      'kw_point4',
                      'kw_point5']
    
    for line in sys.stdin:
        aid_list = ['0'] * len(aid_datalist)
        advertiserId_list = ['0']*len(advertiserId_datalist)
        campaignId_list = ['0']*len(campaignId_datalist)
        creativeId_list = ['0']*len(creativeId_datalist)
        creativeSize_list = ['0']*len(creativeSize_datalist)
        adCategoryId_list = ['0'] * len(adCategoryId_datalist)
        productId_list = ['0']*len(productId_datalist)
        productType_list = ['0']*len(productType_datalist)
        age_list = ['0']*len(age_datalist)
        consumptionAbility_list = ['0']*len(consumptionAbility_datalist)
        LBS_list = ['0']*(len(LBS_datalist))
        house_list = ['0']*len(house_datalist)
        appIdInstall_point_list = ['0']*7
        appIdAction_point_list = ['0']*6
        interest_point_list = ['0']*7
        topic_point_list = ['0']*7
        kw_point_list = ['0']*6
        if line.strip() and "id" not in line:
            if line.strip("\n"):
                fields = line.split('\t')
                #if len(fields) == 80:
                if len(fields) == 79:
                    if fields[1] in aid_datalist:
                        aid_list[aid_datalist.index(fields[1])] = '1'
                    if fields[2] in advertiserId_datalist:
                        advertiserId_list[advertiserId_datalist.index(fields[2])] = '1'
                    if fields[3] in campaignId_datalist:
                        campaignId_list[campaignId_datalist.index(fields[3])] = '1'
                    if fields[4] in creativeId_datalist:
                        creativeId_list[creativeId_datalist.index(fields[4])] = '1'
                    if fields[5] in creativeSize_datalist:
                        creativeSize_list[creativeSize_datalist.index(fields[5])] = '1'
                    if fields[6] in adCategoryId_datalist:
                        adCategoryId_list[adCategoryId_datalist.index(fields[6])] = '1'
                    if fields[7] in productId_datalist:
                        productId_list[productId_datalist.index(fields[7])] = '1'
                    if fields[8] in productType_datalist:
                        productType_list[productType_datalist.index(fields[8])] = '1'
                    if fields[9] in age_datalist:
                        age_list[age_datalist.index(fields[9])] = '1'
                    if fields[47] in consumptionAbility_datalist:
                        consumptionAbility_list[consumptionAbility_datalist.index(fields[47])] = '1'
                    if fields[48] in LBS_datalist:
                        LBS_list[LBS_datalist.index(fields[48])] = '1'
                    else:
                        LBS_list[0] = '1'
                    if fields[75] in house_datalist:
                        house_list[house_datalist.index(fields[75])] = '1'
                    appIdInstall_point_ = int(math.sqrt(float(fields[49])) * 10)
                    appIdAction_point_ = int(math.sqrt(float(fields[50])) * 10)
                    interest_point_ = int(math.sqrt(float(fields[76])) * 10)
                    topic_point_ = int(math.sqrt(float(fields[77])) * 10)
                    kw_point_ = int(math.sqrt(float(fields[78])) * 10)
                    if appIdInstall_point_ == 0:
                        appIdInstall_point_list[0] = '1'
                    elif appIdInstall_point_ > 0 and appIdInstall_point_ <= 10:
                        appIdInstall_point_list[1] = '1'
                    elif appIdInstall_point_ > 10 and appIdInstall_point_ <= 16:
                        appIdInstall_point_list[2] = '1'
                    elif appIdInstall_point_ > 16 and appIdInstall_point_ <= 24:
                        appIdInstall_point_list[3] = '1'
                    elif appIdInstall_point_ > 24 and appIdInstall_point_ <= 42:
                        appIdInstall_point_list[4] = '1'
                    elif appIdInstall_point_ > 42 and appIdInstall_point_ <= 66:
                        appIdInstall_point_list[5] = '1'
                    elif appIdInstall_point_ > 66:
                        appIdInstall_point_list[6] = '1'
                    if appIdAction_point_ == 0:
                        appIdAction_point_list[0] = '1'
                    elif appIdAction_point_ > 0 and appIdAction_point_ <= 6:
                        appIdAction_point_list[1] = '1'
                    elif appIdAction_point_ > 6 and appIdAction_point_ <= 9:
                        appIdAction_point_list[2] = '1'
                    elif appIdAction_point_ > 9 and appIdAction_point_ <= 15:
                        appIdAction_point_list[3] = '1'
                    elif appIdAction_point_ > 15 and appIdAction_point_ <= 22:
                        appIdAction_point_list[4] = '1'
                    elif appIdAction_point_ > 22:
                        appIdAction_point_list[5] = '1'
                    if interest_point_ == 0:
                        interest_point_list[0] = '1'
                    elif interest_point_ > 0 and interest_point_ <= 8:
                        interest_point_list[1] = '1'
                    elif interest_point_ > 8 and interest_point_ <= 18:
                        interest_point_list[2] = '1'
                    elif interest_point_ > 18 and interest_point_ <= 22:
                        interest_point_list[3] = '1'
                    elif interest_point_ > 22 and interest_point_ <= 25:
                        interest_point_list[4] = '1'
                    elif interest_point_ > 25 and interest_point_ <= 34:
                        interest_point_list[5] = '1'
                    elif interest_point_ > 34:
                        interest_point_list[6] = '1'
                    if topic_point_ == 0:
                        topic_point_list[0] = '1'
                    elif topic_point_ > 0 and topic_point_ <= 8:
                        topic_point_list[1] = '1'
                    elif topic_point_ > 8 and topic_point_ <= 11:
                        topic_point_list[2] = '1'
                    elif topic_point_ > 11 and topic_point_ <= 13:
                        topic_point_list[3] = '1'
                    elif topic_point_ > 13 and topic_point_ <= 14:
                        topic_point_list[4] = '1'
                    elif topic_point_ > 14 and topic_point_ <= 15:
                        topic_point_list[5] = '1'
                    elif topic_point_ > 15:
                        topic_point_list[6] = '1'
                    if kw_point_ == 0:
                        kw_point_list[0] = '1'
                    elif kw_point_ > 0 and kw_point_ <= 9:
                        kw_point_list[1] = '1'
                    elif kw_point_ > 9 and kw_point_ <= 13:
                        kw_point_list[2] = '1'
                    elif kw_point_ > 13 and kw_point_ <= 14:
                        kw_point_list[3] = '1'
                    elif kw_point_ > 14 and kw_point_ <= 15:
                        kw_point_list[4] = '1'
                    elif kw_point_ > 15:
                        kw_point_list[5] = '1'
                    aid_list_str = '\t'.join(aid_list)
                    advertiserId_list_str = '\t'.join(advertiserId_list)
                    campaignId_list_str = '\t'.join(campaignId_list)
                    creativeId_list_str = '\t'.join(creativeId_list)
                    creativeSize_list_str = '\t'.join(creativeSize_list)
                    adCategoryId_list_str = '\t'.join(adCategoryId_list)
                    productId_list_str = '\t'.join(productId_list)
                    productType_list_str = '\t'.join(productType_list)
                    age_list_str = '\t'.join(age_list)
                    consumptionAbility_list_str = '\t'.join(consumptionAbility_list)
                    LBS_list_str = '\t'.join(LBS_list)
                    house_list_str = '\t'.join(house_list)
                    appIdInstall_point_list_str = '\t'.join(appIdInstall_point_list)
                    appIdAction_point_list_str = '\t'.join(appIdAction_point_list)
                    interest_point_list_str = '\t'.join(interest_point_list)
                    topic_point_list_str = '\t'.join(topic_point_list)
                    kw_point_list_str = '\t'.join(kw_point_list)
                    #print '\t'.join(
                    #    (fields[0], aid_list_str, advertiserId_list_str, campaignId_list_str, creativeId_list_str,
                    #     creativeSize_list_str, adCategoryId_list_str, productId_list_str, productType_list_str,
                    #     age_list_str, '\t'.join(fields[10:47]), consumptionAbility_list_str, LBS_list_str,
                    #     '\t'.join(fields[51:75]), house_list_str, appIdInstall_point_list_str,
                    #     appIdAction_point_list_str, interest_point_list_str, topic_point_list_str, kw_point_list_str,
                    #     fields[79].strip('\n')))
                    print '\t'.join(
                        (fields[0], aid_list_str, advertiserId_list_str, campaignId_list_str, creativeId_list_str,
                         creativeSize_list_str, adCategoryId_list_str, productId_list_str, productType_list_str,
                         age_list_str, '\t'.join(fields[10:47]), consumptionAbility_list_str, LBS_list_str,
                         '\t'.join(fields[51:75]), house_list_str, appIdInstall_point_list_str,
                         appIdAction_point_list_str, interest_point_list_str, topic_point_list_str, kw_point_list_str))

if __name__ == '__main__':
    mapper()

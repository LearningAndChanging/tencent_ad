#!/usr/bin/env python
from operator import itemgetter
import os
import sys


def mapper():
    adFeature={
     '1017': '11487 741453 1614385 22 21 0 4',
     '1021': '388 243160 1249596 22 27 113 9',
     '1023': '8494 12711 192305 42 24 4666 11',
     '1027': '915 31020 1266652 22 51 0 4',
     '1044': '18630 33813 38299 35 4 0 4',
     '1057': '388 134068 1340722 35 27 113 9',
     '1085': '8203 134120 644672 77 218 0 6',
     '1107': '5552 68476 476885 35 27 113 9',
     '1119': '3993 63752 798752 59 10 19256 11',
     '113': '79 25739 1202263 59 10 1455 11',
     '1140': '43189 98158 1305307 22 43 28986 9',
     '117': '702 18552 619519 53 24 5615 11',
     '1171': '370 262085 717054 35 27 113 9',
     '1182': '8494 42614 818363 22 24 4666 11',
     '12': '388 420987 1612095 35 67 113 9',
     '1201': '5552 68476 1172593 35 27 113 9',
     '1202': '8203 47118 1083112 95 218 0 6',
     '121': '243 10460 1494257 22 27 113 9',
     '1215': '5459 172796 1360276 59 142 0 6',
     '1230': '9619 40877 46884 53 40 0 4',
     '1242': '702 15634 883304 35 34 5615 11',
     '1254': '8350 244601 1383456 35 59 0 4',
     '1277': '2775 12128 1205997 35 21 0 4',
     '1284': '6841 159118 1758880 42 10 3733 11',
     '1291': '1082 40405 1434096 53 13 0 6',
     '1317': '702 15634 480095 35 24 5615 11',
     '1335': '9106 645468 1769240 79 21 0 4',
     '1338': '702 12724 1147463 105 10 4669 11',
     '1350': '7565 353610 1554384 109 94 0 4',
     '1351': '7229 17378 1203413 35 24 6131 11',
     '136': '452 50305 1187573 35 10 7992 11',
     '1375': '370 67127 249293 35 27 113 9',
     '1377': '388 209098 1146648 35 27 113 9',
     '1379': '8864 90700 469197 22 27 113 9',
     '1407': '702 12724 962151 105 10 4669 11',
     '1415': '133292 464828 1334609 22 74 0 4',
     '1429': '10055 86429 641118 22 21 0 6',
     '1449': '285 13953 1724522 42 30 0 6',
     '145': '18621 154634 981822 35 21 0 4',
     '1468': '915 994 1610899 60 51 0 4',
     '1483': '1082 40405 418462 53 13 0 6',
     '1496': '702 52258 1673644 59 10 4669 11',
     '1503': '79 2295 1230210 59 10 38 11',
     '1507': '327 358536 745048 35 67 113 9',
     '1508': '452 115759 1367823 35 10 12193 11',
     '1512': '702 20048 1246897 42 34 5615 11',
     '1530': '11437 18237 1099732 100 21 0 4',
     '1566': '6946 296367 520004 59 24 3794 11',
     '1580': '8203 27030 72027 59 142 0 6',
     '1596': '24704 48236 181137 35 27 113 9',
     '1599': '3993 63752 792238 59 10 19256 11',
     '1605': '11195 19215 1755470 53 140 0 4',
     '1621': '990 51315 1462184 35 27 13727 9',
     '1622': '17597 51385 838455 35 27 0 6',
     '1635': '2775 3372 145496 22 59 0 4',
     '164': '370 241577 474978 35 67 113 9',
     '1671': '702 15634 332490 35 34 5615 11',
     '1672': '327 110094 942499 35 67 113 9',
     '1714': '79 25739 1608684 59 10 1455 11',
     '1716': '5552 158101 1080850 35 27 113 9',
     '1728': '8203 42625 884105 59 218 0 6',
     '173': '6937 186348 267290 35 89 3791 9',
     '174': '11487 668182 1512679 22 21 0 4',
     '1746': '75748 204378 287080 22 121 0 4',
     '1749': '21359 361928 585909 100 21 0 4',
     '177': '8203 76104 1500666 59 282 0 6',
     '1781': '25420 135565 1606251 53 4 0 4',
     '1790': '8494 12711 1636465 42 24 4666 11',
     '18': '8203 74452 857791 95 218 0 6',
     '1819': '10055 169332 1562482 53 192 0 6',
     '1827': '17597 51385 1236432 35 27 0 6',
     '1841': '8668 57846 904288 42 10 17614 11',
     '1842': '27367 95990 1211265 35 25 16791 9',
     '1847': '2509 141893 1394962 35 81 1313 9',
     '1871': '9106 734054 1589088 79 21 0 4',
     '1894': '17597 51385 638911 35 27 0 6',
     '1904': '8203 37818 414738 109 142 0 6',
     '191': '25485 50138 58465 35 51 15454 11',
     '1910': '23805 61383 326633 42 149 14314 11',
     '1918': '158679 643438 1690612 60 4 0 4',
     '1925': '79 25739 1765755 59 10 1455 11',
     '1930': '58643 407774 683342 35 67 113 9',
     '1931': '7300 36763 1401261 79 21 0 4',
     '1940': '5552 30399 530889 35 27 113 9',
     '1950': '41806 233191 1016027 35 13 27855 9',
     '1957': '388 404 1513931 22 27 113 9',
     '1962': '8203 76104 608495 95 282 0 6',
     '1966': '5552 158101 1116089 35 27 113 9',
     '1970': '71505 188857 797661 35 67 0 4',
     '1991': '702 42104 1441131 53 10 4669 11',
     '1998': '15174 26003 1260597 35 125 0 6',
     '2013': '6937 186348 1427984 35 89 3791 9',
     '2031': '83042 280832 425385 22 70 0 4',
     '2044': '49772 487541 869346 35 9 0 9',
     '2047': '11459 18296 20199 91 94 0 4',
     '2048': '8203 37818 240336 59 142 0 6',
     '205': '9571 538818 1040130 35 48 5336 9',
     '2050': '19441 178687 245165 53 1 0 6',
     '2054': '915 31020 794412 22 51 0 4',
     '206': '13915 23303 440096 91 108 0 4',
     '2066': '14818 286065 1075635 109 27 113 9',
     '2068': '14315 73450 1661158 42 265 0 4',
     '2112': '149 155063 750122 53 10 70 11',
     '2118': '11195 19215 1012717 53 140 0 4',
     '212': '8203 47118 1083491 77 218 0 6',
     '2154': '22802 295567 1772271 91 204 0 4',
     '2169': '16770 38402 43877 35 89 9760 9',
     '2196': '20943 445098 767513 53 4 0 4',
     '2197': '9106 132657 700445 79 21 0 4',
     '2201': '101662 308103 477814 42 77 0 4',
     '2205': '370 286844 1149439 22 67 113 9',
     '2216': '5459 172796 1321733 91 142 0 6',
     '231': '11487 159012 991964 20 1 0 4',
     '272': '15174 26003 1108416 35 102 0 6',
     '286': '25485 104406 131847 42 51 15454 11',
     '302': '18621 745599 1628574 91 21 0 4',
     '311': '915 994 27461 60 51 0 4',
     '313': '243 531344 979528 22 27 113 9',
     '336': '370 4833 119845 22 67 113 9',
     '369': '66025 170445 1229175 109 94 0 4',
     '389': '9106 662422 1354071 79 21 0 4',
     '404': '821 888 1353465 59 10 439 11',
     '411': '9106 163120 220179 79 21 0 4',
     '420': '2676 692763 1451219 77 8 0 4',
     '432': '11437 18237 1081485 100 21 0 4',
     '436': '7926 378648 621766 77 8 0 4',
     '450': '45705 352827 565415 42 67 0 4',
     '454': '702 76252 1442655 22 24 5615 11',
     '471': '79 80 731893 22 10 38 11',
     '516': '702 20048 1106145 42 24 5615 11',
     '519': '370 358059 577602 22 67 113 9',
     '529': '10122 163352 220558 35 10 3733 11',
     '543': '1082 295940 1391569 59 22 0 6',
     '561': '44008 100565 808799 79 21 0 4',
     '562': '21017 167166 864509 109 179 0 4',
     '6': '7565 766460 1702986 35 94 0 4',
     '613': '915 31020 546986 22 51 0 4',
     '624': '5459 18683 1735807 59 218 0 6',
     '647': '5459 7527 910853 59 142 0 6',
     '660': '104071 473537 1160702 100 21 0 4',
     '671': '45705 352827 660519 42 67 0 4',
     '681': '728 174407 1638352 42 24 11636 11',
     '686': '370 696695 1464074 35 27 113 9',
     '688': '915 994 1753448 60 51 0 4',
     '692': '6946 296367 455396 59 24 3794 11',
     '699': '1082 295940 731679 59 13 0 6',
     '7': '3387 163957 221432 42 137 3826 11',
     '70': '327 5616 5977 22 27 113 9',
     '725': '370 170485 1485462 22 67 113 9',
     '727': '5552 7686 1473655 35 67 113 9',
     '74': '8668 13044 108752 35 10 4772 11',
     '748': '8203 37818 202309 59 142 0 6',
     '765': '388 134068 1271219 35 27 113 9',
     '792': '8350 331396 1564743 22 59 0 4',
     '838': '452 131853 1640724 93 10 12193 11',
     '846': '8864 310473 1073411 22 43 25730 9',
     '853': '29704 60929 154811 95 108 0 6',
     '86': '8203 76104 416399 59 282 0 6',
     '875': '60 128701 832650 35 34 3194 11',
     '886': '1082 49189 333622 42 13 0 6',
     '894': '452 38391 43862 35 10 12193 11',
     '903': '285 59293 210057 42 30 0 6',
     '914': '47823 111645 141973 100 21 0 4',
     '916': '17597 51385 838056 35 25 0 6',
     '927': '370 219802 492484 35 67 113 9',
     '932': '1025 1123 1806760 42 24 542 11',
     '939': '3993 84178 104188 59 100 24947 11',
     '951': '47823 475236 993205 100 21 0 4',
     '960': '702 52258 1655556 59 10 4669 11',
     '966': '915 31020 666210 22 51 0 4',
     '975': '8494 76011 913588 59 24 4666 11',
     '977': '5758 199508 1080962 100 21 0 4',
     '98': '2775 3372 130171 22 59 0 4'}

    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]

    for line in sys.stdin:
        if "train" in filename:
            if "uid" not in line:
                if line.strip() == '':
                    continue
                line_split = line.split(',')
                aid = line_split[0].strip()
                uid = line_split[1].strip()
                label = line_split[2].strip()
                addata = adFeature.get(aid).strip()
                print '\t'.join((uid + " flag2", "aid " + aid, "addata " + addata, label))
        elif "userFeature" in filename:
            if line.strip() == '':
                continue
            fields = line.split('|')
            uid = fields[0].split()[1].strip()
            userdata = '\t'.join(fields[1:len(fields)]).strip()
            print '\t'.join((uid + " flag1", userdata))

if __name__ == '__main__':
    mapper()
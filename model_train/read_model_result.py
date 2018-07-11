import pickle
import numpy as np
import csv

with open("/home/jx/Documents/lr_res") as label_, open("/home/jx/Documents/result_c_1.txt", 'w') as new_w, open("/home/jx/Downloads/test_aid_uid", 'r') as aid_uid:

    for i in range(2265989):
        label_line = label_.readline()
        uid_line = aid_uid.readline()
        uid = uid_line.strip("\n").split("\t")[1]
        aid = uid_line.strip().split("\t")[0]
        label = label_line.strip().strip("\n")
        if not label:
            print "\t".join((aid, uid, label))
        new_line = "\t".join((aid, uid, label))
        new_w.write(new_line + "\n")



with open('/home/jx/Documents/result_c_1.csv', 'wb') as csvfile, open('/home/jx/Documents/result_c_1.txt', 'rb') as filein:
    spamwriter = csv.writer(csvfile, dialect='excel')
    title_list = ["aid", "uid", "score"]
    spamwriter.writerow(title_list)
    for line in filein.readlines():
        line_list = line.strip("\n").split("\t")
        line_list[2] = line_list[2][:10]
        spamwriter.writerow(line_list)

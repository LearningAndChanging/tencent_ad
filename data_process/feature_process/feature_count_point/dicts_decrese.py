# -*- coding:utf-8 -*-
import os


rootdir = "/media/jiangxing/Entertainments/advertisement/PycharmProjects/data_process/feature_process/feature_count_point/dicts"
aim_title = ["appIdAction", "appIdInstall", "interest1", "interest2", "interest3", "interest4", "interest5", "topic1", "topic2", "topic3", "kw1", "kw2", "kw3"]
def calcu_sum():
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            list1=os.path.join(parent,filename)
            nowdir=list1.replace('\\','/')
            with open(nowdir) as f, open(nowdir + "_", 'w') as fw:
                new_dict = {}
                for line in f.readlines():
                    line_list = line.replace("{", '').replace("}", '').replace("\'" ,'').strip("\n").strip(",")
                    #print (line_list)
                    for title_ in aim_title:
                        if line_list.split(":")[0].split()[1] == title_:
                            if new_dict.get(filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_):
                                new_dict[filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_] += float(line_list.split(":")[1])
                            else:
                                new_dict[filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_] = float(line_list.split(":")[1])

                for (key, value) in new_dict.items():
                    fw.write(key + ' '+ str(value) + "\n")

def decrease2one:
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            list1=os.path.join(parent,filename)
            nowdir=list1.replace('\\','/')
            with open(nowdir) as f, open(nowdir + "_", 'w') as fw:
                new_dict = {}
                for line in f.readlines():
                    line_list = line.replace("{", '').replace("}", '').replace("\'" ,'').strip("\n").strip(",")
                    #print (line_list)
                    for title_ in aim_title:
                        if line_list.split(":")[0].split()[1] == title_:
                            if new_dict.get(filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_):
                                new_dict[filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_] += float(line_list.split(":")[1])
                            else:
                                new_dict[filename.split("_")[1] + ' ' + line_list.split(":")[0].split()[3] + ' ' + title_] = float(line_list.split(":")[1])
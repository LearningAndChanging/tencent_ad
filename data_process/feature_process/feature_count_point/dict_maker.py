#import pickle
import pprint

def dict_maker():
    dict = {}
    '''with open ("/home/jiangxing/Downloads/count_all_1") as f1:
        for line in f1.readlines():
            if line.strip() == '':
                continue
            line_split = line.split("\t")
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "appIdAction" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "appIdInstall" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "topic" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "interest" in line_split[0]:
            if float(line_split[1].strip()) and "productType" in line_split[0] and "kw" in line_split[0]:
                dict[line_split[0].strip()] = line_split[1].strip()
    #file = open("/home/jiangxing/Downloads/productType_interest_count.txt", 'w')
    #pickle.dump(dict, file)'''
    with open ("/home/jiangxing/Downloads/count_all_2") as f2:
        for line in f2.readlines():
            if line.strip() == '':
                continue
            line_split = line.split("\t")
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "appIdAction" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "appIdInstall" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "topic" in line_split[0]:
            #if float(line_split[1].strip()) and "productType" in line_split[0] and "interest" in line_split[0]:
            if float(line_split[1].strip()) and "productType" in line_split[0] and "kw" in line_split[0]:
                dict[line_split[0].strip()] = line_split[1].strip()
    pprint.pprint(dict)

if __name__ == "__main__":
    dict_maker()

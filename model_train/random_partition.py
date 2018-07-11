import random
with open("/home/jx/Downloads/data0510/train_single_feature_0510_libsvm") as f:
    w1 = open("/home/jx/Downloads/data0510/single_feature_data_0510_libsvm_train", 'w')
    w2 = open("/home/jx/Downloads/data0510/single_feature_data_0510_libsvm_test", 'w')
    # for line in f.readlines():
    #     if random.random() < 0.8:
    #         if line.split()[0] == '1':
    #             w1.write(line)
    #         else:
    #             if random.random() <0.05:
    #                 w1.write(line)
    #     elif line.split(" ")[0] == '1':
    #         # if random.random() < 0.5:
    #         w2.write(line)
    #     elif line.split(" ")[0] == '0':
    #         if random.random() < 0.05:
    #             w2.write(line)
    for line in f.readlines():
        if random.random()>0.7:
            continue
        if random.random() < 0.8:
            w1.write(line)
        else:
            w2.write(line)

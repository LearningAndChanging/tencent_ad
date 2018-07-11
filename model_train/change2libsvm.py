with open ("/home/jx/Downloads/data0510/traindata_join0510") as f:
    w = open ("/home/jx/Downloads/data0510/train_single_feature_0510_libsvm", 'w')
    for line in f.readlines():
        words_new = []
        if "id" not in line and line.strip():
            words = line.strip().strip("\n").split("\t")
            for i in range(1, len(words)-1):
            #for i in range(1, len(words)):
                if words[i] != '0' and words[i].strip():
                    words_new.append(str(i) + ':' + words[i])
            line_new = ' '.join((words[-1], ' '.join(words_new))).strip() + '\n'

            #line_new = ' '.join(('0', ' '.join(words_new))).strip() + '\n'
            w.write(line_new)
    w.close
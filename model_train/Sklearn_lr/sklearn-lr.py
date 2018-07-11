# -*- coding: utf-8 -*-

from sklearn import datasets as ds
from sklearn.metrics import auc
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

def load_data():
    #读取libsvm格式数据
    X_train, y_train = ds.load_svmlight_file("/home/jx/Downloads/data0510/single_feature_data_0510_libsvm_train")
    X_test, y_test = ds.load_svmlight_file("/home/jx/Downloads/data0510/test_single_feature_0510_libsvm")
    X_train.todense()
    X_test.todense()




    # sc = StandardScaler()
    # sc.fit(X_train)
    # X_train_std = sc.transform(X_train)
    # X_test_std = sc.transform(X_test)

    # X_combined_std = np.vstack((X_train_std, X_test_std))
    # y_combined = np.hstack((y_train, y_test))



    lr = LogisticRegression(C=1, random_state=0, class_weight='balanced')
    lr.fit(X_train, y_train)

    lpre = lr.predict_proba(X_test[:, :])  # 查看第一个测试样本属于各个类别的概率
    with open('/home/jx/Documents/lr_res', 'w') as fout:
        for i in lpre[:, 1]:
            fout.write('{}\n'.format(i))
        # for i, j, k in zip(lpre[:,0], lpre[:,1], y_test):
        #     fout.write('{}\t{}\t{}\n'.format(i, j, k))
    #print(auc(lpre[:, 0], y_test, reorder=True))
    #print(auc(lpre[:, 1], y_test, reorder=True))

    print(lr.coef_, lr.intercept_)

    # plot_decision_regions(X_combined_std, y_combined, classifier=lr, test_idx=range(105, 150))
    # plt.xlabel('petal length [standardized]')
    # plt.ylabel('petal width [standardized]')
    # plt.legend(loc='upper left')
    # plt.show()

def main():
    load_data()

if __name__ == '__main__':
    main()
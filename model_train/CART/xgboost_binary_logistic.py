# coding:utf-8
import xgboost as xgb
from sklearn.metrics import roc_curve, roc_auc_score
# 计算分类正确率
from sklearn.metrics import accuracy_score, auc
import pickle
import graphviz
# read data
dtrain = xgb.DMatrix("/home/jx/Downloads/data0510/single_feature_data_0510_libsvm_train")
dtest = xgb.DMatrix("/home/jx/Downloads/data0510/single_feature_data_0510_libsvm_test")

dtrain.num_col()
dtrain.num_row()
# max_depth_list = [x for x in range(10, 31, 10)]
# eta_list =[0.001, 0.005, 0.01]
n_estimators_list = []
aucresult = []
progress = {}
for i in {1}:
    for j in {1}:
# for i in eta_list:
#     for j in max_depth_list:
        # specify parameters via map
        param = {'max_depth': 10, 'eta': 0.01, 'silent': 1, 'objective': 'binary:logistic'}
        print param

        # 设置boosting迭代计算次数
        num_round = 10

        import time

        starttime = time.clock()
        bst = xgb.train(param, dtrain, num_round)  # dtrain是训练数据集

        endtime = time.clock()
        print endtime - starttime

        train_preds = bst.predict(dtrain)

        train_predictions = [round(value) for value in train_preds]
        #train_predprob = bst.predict_proba(dtrain)[:,1]
        y_train = dtrain.get_label()

        #train_accuracy = accuracy_score(y_train, train_predictions)
        #fpr_grd_lr, tpr_grd_lr, _ = roc_curve(y_train, train_predprob)
        #print "Train Accuary: %.2f%%" % (train_accuracy * 100.0)
        #bst.save_model('xgb.model')
        #print "AUC Score (Train): %f" % roc_auc_score(y_train, train_predprob)
        # make prediction
        preds = bst.predict(dtest)
        #print preds
        # w = open ("/home/jx/Documents/result2_15_0.4_10", 'w')
        # pickle.dump(preds, w)
        # w.close

        predictions = [round(value) for value in preds]

        y_test = dtest.get_label()
        #aucresult.append(roc_auc_score(y_test, preds))
        # print "test AUC = :", roc_auc_score(y_test, preds)
        test_accuracy = accuracy_score(y_test, predictions)
        with open('/home/jx/Documents/val_res', 'w') as f:
            for i1, j1 in zip(y_test, preds):
                f.write('{}\t{}\n'.format(i1,j1))
        #dtest.save_binary('dtest.buffer')
        print i, j, "Test Accuracy: %.2f%%" % (test_accuracy * 100.0)
        print i, j, 'Another auc: ', auc(y_test, preds, reorder=True)
    #print aucresult
    #print aucresult.index(max(aucresult))

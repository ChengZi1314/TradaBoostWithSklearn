# -*- coding: UTF-8 -*-
import numpy as np

# H 测试样本分类结果
# TrainT 原训练样本 np数组
# TrainS 辅助训练样本
# LabelT 原训练样本标签
# LabelS 辅助训练样本标签
# Test  测试样本
# self.epoch 迭代次数


class TradaBoostClassifier():
    def __init__(self, epoch, learner):
        self.epoch = epoch
        self.learner = learner
        self.beta = None
        self.beta_Tree = None
        result = None
        self.row_T = None
        self.models = []

    def fit(self, trans_T, trans_S, label_T, label_S, test):
        trans_data = np.concatenate((trans_S, trans_T), axis=0)
        trans_label = np.concatenate((label_S, label_T), axis=0)

        self.row_S = trans_S.shape[0]
        self.row_T = trans_T.shape[0]
        self.row_Test = test.shape[0]

        whole_data = np.concatenate((trans_data, test), axis=0)
        weights = np.ones([self.row_S+self.row_T, 1])
        self.beta = 1 / (1 + np.sqrt(2 * np.log(self.row_S / self.epoch)))

        # 存储每次迭代的标签和self.beta值？
        self.beta_Tree = np.zeros([1, self.epoch])   # beta值为每棵树的

        trans_data = np.asarray(trans_data, order='C')
        trans_label = np.asarray(trans_label, order='C')
        whole_data = np.asarray(whole_data, order='C')

        for i in range(self.epoch):
            # print(weights)
            total = np.sum(weights)/(self.row_S+self.row_T)
            sample_weights = np.asarray(weights/total, order='C')

            self.learner.fit(trans_data, trans_label, sample_weights[:, 0])
            self.models.append(self.learner)
            result = self.learner.predict_proba(whole_data)[:, 1]
            print(result)
            error_rate = self.calculate_error_rate(label_T, result[self.row_S:self.row_S + self.row_T],
                                              weights[self.row_S:self.row_S + self.row_T, :])

            if error_rate > 0.5:
                error_rate = 0.5
            if error_rate == 0:
                self.epoch = i
                break  # 防止过拟合

            self.beta_Tree[0, i] = error_rate / (1 - error_rate)

            # 调整源域样本权重
            for j in range(self.row_T):
                weights[self.row_S + j] = weights[self.row_S + j] * np.power(self.beta_Tree[0, i],
                                                                   (-np.abs(result[self.row_S + j] - label_T[j])))
            # 调整辅域样本权重
            for j in range(self.row_S):
                weights[j] = weights[j] * np.power(self.beta, (np.abs(result[j] - label_S[j])))

    def calculate_error_rate(self, label_R, label_H, weight):
        total = np.sum(weight)
        return np.sum(weight[:, 0] / total * np.abs(label_R - label_H))

    def predict(self, test_data):
        self.row_Test = test_data.shape[0]
        result = np.ones([self.row_Test, self.epoch])
        predict = np.ones([self.row_Test, 1])
        for i in range(self.epoch):
            result[:, i] = self.models[i].predict_proba(test_data)[:, 1]
        for i in range(self.row_Test):
            # 跳过训练数据的标签
            left = np.sum(result[i, int(np.ceil(self.epoch / 2)):self.epoch] * np.log(1 / self.beta_Tree[0, int(np.ceil(self.epoch / 2)):self.epoch]))
            right = 0.5 * np.sum(np.log(1 / self.beta_Tree[0, int(np.ceil(self.epoch / 2)):self.epoch]))
            if left >= right:
                predict[i] = 1
            else:
                predict[i] = 0
        return predict

    def predict_proba(self, test_data):
        self.row_Test = test_data.shape[0]
        # result = self.learner.predict_proba(test_data)[:, 0]
        result = np.ones([self.row_Test, self.epoch])
        predict = np.ones([self.row_Test, 1])
        for i in range(self.epoch):
            result[:, i] = self.models[i].predict_proba(test_data)[:, 1]
        for i in range(self.row_Test):
            # 跳过训练数据的标签
            predict[i] = np.sum(result[i, int(np.ceil(self.epoch / 2)):self.epoch] * np.log(
                1 / self.beta_Tree[0, int(np.ceil(self.epoch / 2)):self.epoch]))
        return predict




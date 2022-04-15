# 支持向量机
import numpy as np

my_seed = 512
np.random.seed(my_seed)
import random

random.seed(my_seed)
import tensorflow as tf

tf.random.set_seed(my_seed)

import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC, LinearSVR
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import pylab as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']


def PlotSpectrum(spec):
    plt.rcParams['axes.unicode_minus'] = False
    x = np.arange(357, 357 + 1.072 * spec.shape[1], 1.072)
    for i in range(spec.shape[0]):  # 给i赋值
        plt.plot(x, spec[i, :], linewidth=0.5)
    fonts = 11
    plt.xlim(357, 1017)
    # plt.ylim(0, 1.4)
    plt.xlabel('波长（nm）', fontsize=fonts)
    plt.ylabel('吸光度A（%）', fontsize=fonts)
    plt.yticks(fontsize=fonts)
    plt.xticks(fontsize=fonts)
    plt.tight_layout(pad=1)
    # plt.grid(True)
    return plt


# 标准正态变换
def snv(data):
    m = data.shape[0]
    n = data.shape[1]
    print(m, n)  #
    # 求标准差
    data_std = np.std(data, axis=1)  # 每条光谱的标准差
    # 求平均值
    data_average = np.mean(data, axis=1)  # 每条光谱的平均值
    # SNV计算
    data_snv = [[((data[i][j] - data_average[i]) / data_std[i]) for j in range(n)] for i in range(m)]
    data_snv = np.array(data_snv)
    return data_snv


from utils import read_csv
x, y = read_csv('../../../data/1.csv')
x = snv(x)  # 标准正态变换
pp = PlotSpectrum(x)
pp.show()
from sklearn.decomposition import PCA

pca = PCA(n_components=4)
x = pca.fit_transform(x)
# pca可视化
plt.plot(range(4), np.cumsum(pca.explained_variance_ratio_))
plt.title("  ")
plt.xlabel('PCA主成分数(个)', fontsize=12)
plt.ylabel('累计误差', fontsize=12)
plt.show()
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=0)
model = SVC(kernel='linear')  # 线性核支持向量机
model.fit(train_X, train_y)
y_pred = model.predict(test_X)
print(test_y)
print(y_pred)

# 模型评价
print('测试集混淆矩阵为：\n', confusion_matrix(test_y, y_pred))
print('平均分类准确率为：\n', accuracy_score(test_y, y_pred))
from sklearn.metrics import accuracy_score

print('准确率', accuracy_score(test_y, y_pred))
from sklearn.metrics import precision_score

print('精确率', precision_score(test_y, y_pred, average=None))
from sklearn.metrics import recall_score

print('召回率', recall_score(test_y, y_pred, average=None))
from sklearn.metrics import f1_score

print('F1 score', f1_score(test_y, y_pred, average=None))
from sklearn.metrics import roc_auc_score

print('auc', roc_auc_score(test_y, y_pred, average=None))
m = (test_y == y_pred)
score = np.sum(m == True) / len(test_y)
print('精度', score)

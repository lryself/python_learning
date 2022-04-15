# PLS-DA
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, roc_auc_score
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import pylab as mpl
from utils import PlotSpectrum, read_csv

my_seed = 512
np.random.seed(my_seed)

random.seed(my_seed)

mpl.rcParams['font.sans-serif'] = ['SimHei']


# 读取特征矩阵
x, y = read_csv("../../../data/1.csv")
pp = PlotSpectrum(x)
pp.show()

pca = PCA(n_components=4)
x = pca.fit_transform(x)

# pca可视化
plt.plot(range(4), np.cumsum(pca.explained_variance_ratio_))
plt.title("  ")
plt.xlabel('PCA主成分数(个)', fontsize=12)
plt.ylabel('累计误差', fontsize=12)
plt.show()

# 先做一个数据集的划分
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3)

# 然后对y进行转换
train_y = pd.get_dummies(train_y)

# 建模
model = PLSRegression(n_components=4)
model.fit(train_X, train_y)

# 预测
y_pred = model.predict(test_X)

# 将预测结果（类别矩阵）转换为数值标签
y_pred = np.array([np.argmax(i) for i in y_pred])

# 模型评价
print('测试集混淆矩阵为：\n', confusion_matrix(test_y, y_pred))
print('平均分类准确率为：\n', accuracy_score(test_y, y_pred))
print('准确率', accuracy_score(test_y, y_pred))
print('召回率', recall_score(test_y, y_pred, average=None))
print('F1 score', f1_score(test_y, y_pred, average=None))
print('auc', roc_auc_score(test_y, y_pred, average=None))

score = np.sum((test_y == y_pred) is True) / len(test_y)
print('精度', score)
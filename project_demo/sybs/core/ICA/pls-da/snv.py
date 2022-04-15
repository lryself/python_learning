# PLS-DA
import pandas as pd
import pylab as mpl
import numpy as np
from utils import PlotSpectrum, read_csv
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FastICA
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, roc_auc_score

my_seed = 512
np.random.seed(my_seed)

mpl.rcParams['font.sans-serif'] = ['SimHei']


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


# 读取特征矩阵
x, y = read_csv("../../../data/1.csv")
# todo 变换方法
x = snv(x)

pp = PlotSpectrum(x)
pp.show()

# PCA降维
# todo 降维方法
ica = FastICA(n_components=2)
S_ = ica.fit_transform(x) # 重构信号
A_ = ica.mixing_ # 获得估计混合后的矩阵
# pca可视化
plt.plot(S_)
plt.title("  ")
plt.show()


# 先做一个数据集的划分
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3)

# 然后对y进行转换
train_y = pd.get_dummies(train_y)

# 建模
# todo 建模方法
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

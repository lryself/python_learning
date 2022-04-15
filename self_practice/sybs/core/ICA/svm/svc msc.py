# 支持向量机
import random
import pandas as pd
import numpy as np
import pylab as mpl
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.utils import shuffle


my_seed = 512
np.random.seed(my_seed)
random.seed(my_seed)
mpl.rcParams['font.sans-serif'] = ['SimHei']


def PlotSpectrum(spec):
    plt.rcParams['axes.unicode_minus'] = False
    x = np.arange(357, 357 + 1.072 * spec.shape[1], 1.072)
    for i in range(spec.shape[0]):
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


# 多元散射矫正
def msc(sdata):
    n = sdata.shape[0]  # 样本数量
    k = np.zeros(sdata.shape[0])
    b = np.zeros(sdata.shape[0])
    M = np.mean(sdata, axis=0)
    from sklearn.linear_model import LinearRegression
    for i in range(n):
        y = sdata[i, :]  ##切割数据，和原先一样的方法  #需要什么就切什么
        # 如果等于-1的话，那么Numpy会根据剩下的维度计算出数组的另外一个shape属性值
        y = y.reshape(-1, 1)  # 先前我们不知道z的shape属性是多少，但是想让z变成只有一列，行数不知道多少,自动计算出行数
        M = M.reshape(-1, 1)
        model = LinearRegression()  # 创建回归模型
        model.fit(M, y)  # 带入切分好的数据
        k[i] = model.coef_  # 返回NxN矩阵
        print(k[i])
        b[i] = model.intercept_  # 截距
    spec_msc = np.zeros_like(sdata)  # 函数主要是想实现构造一个矩阵W_update，其维度与矩阵W一致，并为其初始化为全0；这个函数方便的构造了新矩阵，无需参数指定shape大小
    for i in range(n):
        bb = np.repeat(b[i], sdata.shape[1])  # 复制多维数组的每一个元素；axis来控制复制的轴，对于二维数组，就是行和列.
        kk = np.repeat(k[i], sdata.shape[1])
        temp = (sdata[i, :] - bb) / kk
        spec_msc[i, :] = temp
    return spec_msc


from utils import read_csv
x, y = read_csv('../../../data/1.csv')
x = msc(x)  # 多元散射校正
pp = PlotSpectrum(x)
pp.show()
from sklearn.decomposition import PCA, FastICA

ica = FastICA(n_components=4)
x = ica.fit_transform(x) # 重构信号
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=0)
model = SVC(kernel='linear')  # 线性核支持向量机
# 训练
model.fit(train_X, train_y)
# 预测
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

# 支持向量机
# PLS-DA
from utils import PlotSpectrum, read_csv
import numpy as np
import pandas as pd
import pylab as mpl
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, roc_auc_score
from sklearn.decomposition import FastICA

my_seed = 512
np.random.seed(my_seed)

mpl.rcParams['font.sans-serif'] = ['SimHei']


# 多元散射矫正预处理
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


# 读取特征矩阵
x, y = read_csv('../../../data/1.csv')
x = msc(x)

# 生成光谱
pp = PlotSpectrum(x)
pp.show()

# 降维
ica = FastICA(n_components=2)
S_ = ica.fit_transform(x) # 重构信号
A_ = ica.mixing_ # 获得估计混合后的矩阵
# pca可视化
plt.plot(S_)
plt.title("  ")
plt.show()
# plt.xlabel('PCA主成分数(个)', fontsize=12)
# plt.ylabel('累计误差', fontsize=12)

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

"""
random.seed(my_seed)
import tensorflow as tf

tf.random.set_seed(my_seed)

import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC ,LinearSVR
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
def PlotSpectrum(spec):
  plt.rcParams['axes.unicode_minus']=False
  x = np.arange(357, 357+1.072 * spec.shape[1], 1.072)
  for i in range(spec.shape[0]):              #给i赋值
      plt.plot(x, spec[i, :], linewidth=0.5)
  fonts = 11
  plt.xlim(357, 1017)
  #plt.ylim(0, 1.4)
  plt.xlabel('波长（nm）',fontsize=fonts)
  plt.ylabel('吸光度A（%）',fontsize=fonts)
  plt.yticks(fontsize=fonts)
  plt.xticks(fontsize=fonts)
  plt.tight_layout(pad=1)
  #plt.grid(True)
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
    data_snv= np.array(data_snv)
    return  data_snv

#多元散射矫正
def msc(sdata):
    n = sdata.shape[0]  # 样本数量
    k = np.zeros(sdata.shape[0])
    b = np.zeros(sdata.shape[0])
    M = np.mean(sdata, axis=0)
    from sklearn.linear_model import LinearRegression
    for i in range(n):
        y = sdata[i, :]  ##切割数据，和原先一样的方法  #需要什么就切什么
       # 如果等于-1的话，那么Numpy会根据剩下的维度计算出数组的另外一个shape属性值
        y = y.reshape(-1, 1)   #先前我们不知道z的shape属性是多少，但是想让z变成只有一列，行数不知道多少,自动计算出行数
        M = M.reshape(-1, 1)
        model = LinearRegression()        #创建回归模型
        model.fit(M, y)       #带入切分好的数据
        k[i] = model.coef_     #返回NxN矩阵
        print(k[i])
        b[i] = model.intercept_  #截距
    spec_msc = np.zeros_like(sdata)    # 函数主要是想实现构造一个矩阵W_update，其维度与矩阵W一致，并为其初始化为全0；这个函数方便的构造了新矩阵，无需参数指定shape大小
    for i in range(n):
        bb = np.repeat(b[i], sdata.shape[1])    # 复制多维数组的每一个元素；axis来控制复制的轴，对于二维数组，就是行和列.
        kk = np.repeat(k[i], sdata.shape[1])
        temp = (sdata[i, :] - bb)/kk
        spec_msc[i, :] = temp
    return spec_msc
data = pd.read_csv('F:\\11\\1.csv')
data=shuffle(data)
data= np.array(data)
x=data[:,:616]
y=data[:,616]
x = msc(x)  #多元散射校正
#x = snv(x)  #标准正态变换
pp = PlotSpectrum(x)
#pp.show()
from sklearn.decomposition import PCA
pca = PCA(n_components=11)
x = pca.fit_transform(x)
train_X,test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=0)
model = SVC(kernel='linear')#线性核支持向量机
#model =LinearSVC()#线性支持向量机
#model = SVC(kernel='poly')#多项式内核支持向量机
#model = SVC(kernel='rbf')#径向基核支持向量机
model.fit(train_X, train_y)
y_pred = model.predict(test_X)
print(test_y)
print(y_pred)


#模型评价
print('测试集混淆矩阵为：\n',confusion_matrix(test_y,y_pred))
print('平均分类准确率为：\n',accuracy_score(test_y,y_pred))
from sklearn.metrics import accuracy_score
print('准确率',accuracy_score(test_y, y_pred))
from sklearn.metrics import precision_score
print('精确率',precision_score(test_y, y_pred, average=None))
from sklearn.metrics import recall_score
print('召回率',recall_score(test_y, y_pred, average=None))
from sklearn.metrics import f1_score
print('F1 score',f1_score(test_y, y_pred, average=None))
from sklearn.metrics import roc_auc_score
print('auc',roc_auc_score(test_y, y_pred, average=None))
m=(test_y==y_pred)
score=np.sum(m==True)/len(test_y)
print('精度',score)
"""

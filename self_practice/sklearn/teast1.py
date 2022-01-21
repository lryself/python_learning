# coding: utf-8
# @Author : lryself
# @Date : 2020/12/24 17:48
# @Software: PyCharm
from collections import OrderedDict
import pandas as pd

examDict = {
    '学习时间': [0.5, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75,
             5.00, 5.50],
    '分数': [10, 22, 13, 43, 20, 22, 33, 50, 62, 48, 55, 75, 62, 73, 81, 76, 64, 82, 90, 93]}

examOderDict = OrderedDict(examDict)
examDF = pd.DataFrame(examOderDict)
exam_X = examDF.loc[:, '学习时间']
exam_Y = examDF.loc[:, '分数']

import matplotlib.pyplot as plt

plt.scatter(exam_X, exam_Y, color="b", label="exam data")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(exam_X, exam_Y, train_size=.8)
print('原始数据特征：', exam_X.shape,
      '训练集数据特征：', X_train.shape,
      '测试集数据特征：', X_test.shape,
      )
print('原始数据标签：', exam_X.shape,
      '训练集数据标签：', y_train.shape,
      '测试集数据标签：', y_test.shape,
      )
rDF = examDF.corr()

X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

a = model.intercept_
b = model.coef_
print("最佳拟合线：截距为：{}, 回归系数为：{}".format(a, b))

c = model.score(X_test, y_test)
print(c)

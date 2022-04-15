# coding: utf-8

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.utils import shuffle


# 显示光谱
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


def read_csv(file):
    data = pd.read_csv(file)
    data = shuffle(data)  # 样本打乱顺序
    data = np.array(data)
    x = data[:, :data.shape[1] - 1]
    y = data[:, data.shape[1] - 1]
    return x, y

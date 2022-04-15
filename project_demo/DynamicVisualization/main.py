# coding: utf-8
# @Author : lryself
# @Date : 2021/5/19 22:27
# @Software: PyCharm

import akshare as ak
import pandas as pd
import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.express as px
from datetime import datetime

init_notebook_mode()

# 从 akshare 获取数据
# df_all_history = ak.covid_19_history()
# 从csv文件获取数据
df_all_history = pd.read_csv('nCov.csv')

df_all = df_all_history
# 将字符串格式的日期 另保存为一列
df_all['dates'] = df_all_history['date']
# 将字符串格式的日期转换为 日期格式
df_all['date'] = pd.to_datetime(df_all['date'])

df_oversea = df_all.query("country!='中国'")
df_oversea.fillna(value="", inplace=True)

# fig_oversea = px.line(df_oversea, x='dates', y='confirmed',
#                       line_group='country',
#                       color='country',
#                       color_discrete_sequence=px.colors.qualitative.D3,
#                       hover_name='country',
#                       )
# fig_oversea.show()
# plotly.offline.plot(fig_oversea)
# print("end")

df_oversea_recent = df_oversea.set_index('date')
df_oversea_recent = df_oversea_recent['2020-02-10':]

# 由于部分国家，数据不是从2020年2月10日开始的，所以要补充数据，数值为 0
# 数据在 excel 表格中进行补充，这里进行读取

# df_oversea_buchong = pd.read_excel('epidemic_buchong.xlsx')
# df_oversea_buchong['dates'] = df_oversea_buchong['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
# df_oversea_buchong.set_index('date', inplace=True)
# df_oversea_buchong.fillna(value="", inplace=True)
# print(df_oversea_buchong.info())
#
# df_oversea_recent_new = df_oversea_recent.append(df_oversea_buchong)
# df_oversea_recent_new.sort_index(inplace=True)
df_oversea_recent.sort_index(inplace=True)

# fig_oversea_recent = px.bar(df_oversea_recent, x='dead', y='confirmed',
#                                 size='confirmed', text='country', color='country',
#                                 color_discrete_sequence=px.colors.qualitative.Light24,
#                                 animation_frame='dates', animation_group='country',
#                                 hover_name='country',
#                                 range_x=[-10, 260],
#                                 range_y=[0, 8000],
#                                 size_max=50,
#                                 template='plotly_white',
#                                 )
# 开始绘图
fig_oversea_recent = px.bar(data_frame=df_oversea_recent,
                            x='confirmed',
                            y='country',
                            color='country',
                            facet_row=None,
                            facet_col=None,
                            facet_col_wrap=0,
                            hover_name='confirmed',
                            hover_data=None,
                            custom_data=None,
                            text='confirmed',
                            error_x=None,
                            error_x_minus=None,
                            error_y=None,
                            error_y_minus=None,
                            animation_frame='dates',
                            animation_group='country',
                            category_orders={},
                            labels={},
                            color_discrete_sequence=px.colors.qualitative.Light24,
                            color_discrete_map={},
                            color_continuous_scale=None,
                            range_color=None,
                            color_continuous_midpoint=None,
                            opacity=None,
                            orientation='h',
                            barmode='relative',
                            log_x=False,
                            log_y=False,
                            range_x=None,
                            range_y=None,
                            title=None,
                            template='plotly_white',
                            width=None,
                            height=None)
# fig_oversea_recent.show()
plotly.offline.plot(fig_oversea_recent)

# 参数含义参考https://www.jianshu.com/p/aeffc6cb487e

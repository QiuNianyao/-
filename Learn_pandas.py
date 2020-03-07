#!/usr/bin/env python
# encoding: utf-8
"""
@author: 仇念尧
@contact: 1623343718@qq.com
@software: Pycharm
@file: Learn_pandas.py
@time: 2019/7/29 15:01
@desc:
"""

import pandas as pd
import os

# # pandas读写文本文件
# # 读取文本文件
# # 常用编码为UTF-8、UTF-16、GBK、GB 2312、GB 18030，
# # 文件编码解码格式应对应，不然会出现乱码
# a = pd.read_table('E:/data/meal_order_info.csv', sep=',', encoding='gbk')
# b = pd.read_csv('E:/data/meal_order_info.csv', encoding='gbk')
# # print(a[:10])
# # print(b[:10])
#
# # 将数据写入CSV文件
# # 对比两次输出，文件夹内会多出一个m.csv文件
# print(os.listdir('E:/data'))
# a.to_csv('E:/data/m.csv', sep=';', index=False)
# print(os.listdir('E:/data'))

# 读、写Excel文件
# 读取Excel文件
a = pd.read_excel('E:/data/users.xlsx')

# 将数据写入excel文件
# 对比两次输出，文件夹内会多出一个m.xlsx文件
print(os.listdir('E:/data'))
a.to_excel('E:/data/m.xlsx')
print(os.listdir('E:/data'))

# DataFrame常用操作












#!/usr/bin/env python
# encoding: utf-8
"""
@author: 仇念尧
@contact: 1623343718@qq.com
@software: Pycharm
@file: Learn_matplotlib.py
@time: 2019/7/27 20:36
@desc:
"""

import numpy as np
import matplotlib.pyplot as plt
# 确保显示不出现乱码
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示

# 绘制不含子图的图形
# 确定数据
x = np.arange(0, 1, 0.01)
y = x
z = x**2
# 创建画布，无子图该步骤可省略
a = plt.figure()
# 添加标题
plt.title('图像')
# 添加x，y轴名称
plt.xlabel('x')
plt.ylabel('y')
# 添加x，y轴范围
plt.xlim(0, 1)
plt.ylim(0, 1)
# 添加x，y轴刻度
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
# 绘制曲线
plt.plot(x, y, 'g-.', x, z, 'b--')
# 绘制图例，该步骤应在绘图后
plt.legend(['y = x', 'z = x^2'])
# 保存图片
plt.savefig('E:/DaiMa/data analysis by python/1.pdf')
# 显示图像，必须加这一句，不然看不到图像
plt.show()
#
# # # 绘制含子图的图形
# # 确定数据
# x = np.arange(0, 1, 0.01)
# y = x
# z = x**2
# # 创建画布，无子图该步骤可省略
# # 合理调整figsize、dpi可避免出现第一幅图横轴名称
# # 与第二幅图标题相互遮盖的现象
# a = plt.figure(figsize=(8, 14), dpi=80)
# # 创建两行一列子图中的第一幅子图
# a1 = a.add_subplot(2, 1, 1)
# # 添加标题
# plt.title('图像')
# # 添加x，y轴名称
# plt.xlabel('x')
# plt.ylabel('y')
# # 添加x，y轴范围
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# # 添加x，y轴刻度
# plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
# # 绘制曲线
# plt.plot(x, y, x, z)
# # 绘制图例，该步骤应在绘图后
# plt.legend(['y = x', 'z = x^2'])
#
# # 创建两行一列子图中的第二幅子图
# a2 = a.add_subplot(2, 1, 2)
# # 添加标题
# plt.title('图像')
# # 添加x，y轴名称
# plt.xlabel('x')
# plt.ylabel('y')
# # 添加x，y轴范围
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# # 添加x，y轴刻度
# plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
# # 绘制曲线
# plt.plot(x, np.sin(x), x, np.tan(x))
# # 绘制图例，该步骤应在绘图后
# plt.legend(['y = sin x', 'z = tan x'])
# # 保存图片
# plt.savefig('E:/data analysis by python/2.png')
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()
#
# # 确定数据
# x = np.arange(0, 10, 1)
# y = x
# z = x**2
# # 绘制曲线
# plt.plot(x, y, 'g-', x, z, 'b--')
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()
#
# plt.plot(x, y, c='r', ls='--', marker='o')
#
#
# # 确定数据
# x = np.arange(0, 10, 1)
# y = x
# z = x**2
# # 设置线条rc参数
# # 线条形状，linestyle可简写为ls
# plt.rcParams['lines.linestyle'] = '-.'
# # 线条宽度，linewidth可简写为lw
# plt.rcParams['lines.linewidth'] = 2
# # 线条颜色，color可简写为c
# plt.rcParams['lines.color'] = 'g'
# # 点形状
# plt.rcParams['lines.marker'] = 'D'
# # 点大小
# plt.rcParams['lines.markersize'] = '10'
# # 点边缘宽度
# plt.rcParams['lines.markeredgewidth'] = '2'
# # 点边缘颜色
# plt.rcParams['lines.markeredgecolor'] = 'y'
# # 点内部颜色
# plt.rcParams['lines.markerfacecolor'] = 'r'
#
# # 绘制曲线
# plt.plot(x, y, x, z)
# # 显示图像，必须加这一句，不然看不到图像
# # 保存图片, dpi为清晰度，数值越高越清晰
# plt.savefig('E:/data analysis by python/线条参数.png', dpi=500)
# plt.show()

#
# # 绘制散点图
# # 确定数据
# x = np.arange(1, 70, 1)
# y = [21329.9, 24043.4, 25712.5, 29194.3, 24086.4, 26726.6, 28333.3,
#      31716.8, 26295.0, 29194.8, 31257.3, 34970.3, 29825.5, 32537.3,
#      35291.9, 39767.4, 34544.6, 38700.8, 41855.0, 46739.8, 40453.3,
#      44793.1, 48047.8, 54024.8, 47078.9, 52673.3, 56064.7, 63621.6,
#      57177.0, 64809.6, 69524.3, 78721.4, 69410.4, 78769.0, 82541.9,
#      88794.3, 74053.1, 83981.3, 90014.1, 101032.8, 87616.7, 99532.4,
#      106238.7, 119642.5, 104641.3, 119174.3, 126981.6, 138503.3, 117593.9,
#      131682.5, 138622.2, 152468.9, 129747.0, 143967.0, 152905.3, 168625.1,
#      140618.3, 156461.3, 165711.9, 181182.5, 150986.7, 168503.0, 176710.4,
#      192851.9, 161572.7, 180743.7, 190529.5, 211281.3, 180682.7]
# z = ['2000年第一季度', '2001年第一季度', '2002年第一季度', '2003年第一季度',
#      '2004年第一季度', '2005年第一季度', '2006年第一季度', '2007年第一季度',
#      '2008年第一季度', '2009年第一季度', '2010年第一季度', '2011年第一季度',
#      '2012年第一季度', '2013年第一季度', '2014年第一季度', '2015年第一季度',
#      '2016年第一季度', '2017年第一季度']
# # 创建画布
# a = plt.figure(figsize=(8, 8), dpi=100)
# # 绘制散点图
# plt.scatter(x, y)
# # 设置X轴刻度标签，range(0, 70, 4)为每隔4个数据，添加一个坐标
# plt.xticks(range(0, 70, 4), z, rotation=45)
# # 保存图片，dpi越高，图像越清晰
# # plt.savefig('E:/data analysis by python/散点图.png', dpi=500)
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()

# # 绘制折线图
# # 确定数据
# x = np.arange(0, 69, 1)
# y = [21329.9, 24043.4, 25712.5, 29194.3, 24086.4, 26726.6, 28333.3,
#      31716.8, 26295.0, 29194.8, 31257.3, 34970.3, 29825.5, 32537.3,
#      35291.9, 39767.4, 34544.6, 38700.8, 41855.0, 46739.8, 40453.3,
#      44793.1, 48047.8, 54024.8, 47078.9, 52673.3, 56064.7, 63621.6,
#      57177.0, 64809.6, 69524.3, 78721.4, 69410.4, 78769.0, 82541.9,
#      88794.3, 74053.1, 83981.3, 90014.1, 101032.8, 87616.7, 99532.4,
#      106238.7, 119642.5, 104641.3, 119174.3, 126981.6, 138503.3, 117593.9,
#      131682.5, 138622.2, 152468.9, 129747.0, 143967.0, 152905.3, 168625.1,
#      140618.3, 156461.3, 165711.9, 181182.5, 150986.7, 168503.0, 176710.4,
#      192851.9, 161572.7, 180743.7, 190529.5, 211281.3, 180682.7]
# z = ['2000年第一季度', '2001年第一季度', '2002年第一季度', '2003年第一季度',
#      '2004年第一季度', '2005年第一季度', '2006年第一季度', '2007年第一季度',
#      '2008年第一季度', '2009年第一季度', '2010年第一季度', '2011年第一季度',
#      '2012年第一季度', '2013年第一季度', '2014年第一季度', '2015年第一季度',
#      '2016年第一季度', '2017年第一季度']
# # 创建画布
# a = plt.figure(figsize=(8, 8), dpi=100)
# # 绘制折线图
# plt.rcParams['lines.markersize'] = '3'
# plt.plot(x, y, marker='o')
# # 设置X轴刻度标签，range(0, 70, 4)为每隔4个数据，添加一个坐标
# plt.xticks(range(0, 69, 4), z, rotation=45)
# # 保存图片，dpi越高，图像越清晰
# plt.savefig('E:/data analysis by python/折线图.png', dpi=500)
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()
#
# # 绘制直方图
# # 确定数据
# x = np.arange(0, 7, 1)
# y = [21329.9, 22043.4, 21712.5, 23194.3, 24086.4, 21726.6, 22333.3]
# z = ['赵', '钱', '孙', '李', '周', '吴', '郑']
# # 创建画布
# a = plt.figure(figsize=(8, 8), dpi=100)
# # 绘制直方图
# plt.bar(x, y, width=0.5, color='blue')
# # 设置X轴刻度标签
# plt.xticks(range(7), z)
# plt.ylim(20000, 25000)
# # 保存图片，dpi越高，图像越清晰
# plt.savefig('E:/data analysis by python/直方图.png', dpi=500)
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()
#
# # 绘制饼图
# a = [100, 200, 300]
# b = ['赵', '钱', '孙']
# # 创建画布
# # 将图布设置为正方形，绘制的饼图为正圆
# c = plt.figure(figsize=(8, 8), dpi=100)
# # 设置饼图各部分距离饼图圆心为n个半径
# d = [0.01, 0.01, 0.01]
# # 绘制饼图,并自动显示各部分占比
# plt.pie(a, explode=d, labels=b, autopct='%.2f%%')
# # 保存图片，dpi越高，图像越清晰
# plt.savefig('E:/data analysis by python/饼图.png', dpi=500)
# # 显示图像，必须加这一句，不然看不到图像
# plt.show()
#
# a, b = 0, 0
# r = 0.05
# theta = np.arange(0, 2*np.pi, 0.01)
# x = a + r * np.cos(theta)
# y = b + r * np.sin(theta)
# fig = plt.figure()
# axes = fig.add_subplot(111)
# axes.plot(x, y)
# axes.axis('equal')

# def my_plotter(ax, data1, data2, param_dict):
#     out = ax.plot(data1, data2, **param_dict)
#     # plt.show()
#     # print(out)
#     return out
#
# # which you would then use as:
#
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(1, 1)
# my_plotter(ax, data1, data2, {'marker': 'x'})








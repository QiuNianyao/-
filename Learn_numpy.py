#!/usr/bin/env python
# encoding: utf-8
"""
@author: 仇念尧
@contact: 1623343718@qq.com
@software: Pycharm
@file: Learn_numpy.py
@time: 2019/7/25 10:56
@desc:
"""

import numpy as np

# # array
#
# # 创建一维数组
# arr1 = np.array([1, 2, 3, 4])
# print(arr1)
# # 创建二维数组
# arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
# print(arr2)
# # 查看数组结构
# print(arr2.shape)
# # 查看数组类型
# print(arr2.dtype)
# # 查看数组元素个数
# print(arr2.size)
# # 查看数组每个元素大小
# print(arr2.itemsize)
# # 重新设置数组结构
# arr2.shape = 4, 3
# print(arr2)
#
# # 使用arange函数创建数组(不包括终值)
# a = np.arange(0, 1, 0.1)
# print(a)
#
# # 使用linspace函数创建数组(包括终值)
# b = np.linspace(0, 1, 12)
# print(b)
#
# # 使用logspace函数创建数组(数值为10的指数)
# c = np.logspace(0, 2, 20)
# print(c)
#
# # 使用zeros函数创建数组
# d = np.zeros((2, 3))
# print(d)
#
# # 使用eye函数创建数组
# e = np.eye(3)
# print(e)
#
# # 使用diag函数创建数组
# f = np.diag([1, 2, 3, 4])
# print(f)
#
# # 使用ones函数创建数组
# g = np.ones((5, 3))
# print(g)
#
# # 数组数据类型装换
#
# # 整型转换为浮点型
# print(np.float64(42))
#
# # 浮点型转换为整型
# print(np.int8(42.0))
#
# # 整型转换为布尔型
# print(np.bool(42))
#
# # 布尔型转换为浮点型
# print(np.float(True))
#
# # 例子
# df = np.dtype([("name", np.str_, 40), ("numitems", np.int64),
#                ("price", np.float64)])
# itemz = np.array([("tomatoes", 42, 4.14), ("cabbage", 13, 1.72)], dtype=df)
#
# # 在[0,1)间生成100个随机数
# np.random.random(100)
#
# # 生成给定上下限范围的随机数
# np.random.randint(2, 10, size=[2, 5])
#
# # 在[0,1)间生成服从均匀分布、3行2列的随机数
# np.random.rand(3, 2)
#
# # 在[low, high)间生成服从均匀分布、3行2列的随机数
# np.random.uniform(1, 2, (3, 2))
#
# # 生成服从标准正态分布的随机数
# np.random.randn(10, 5)
#
# # 生成服从均值为1，方差为2的正态分布的随机数
# np.random.normal(1, 2)
#
# # 例子——蒙特卡洛求pi
# n = 400             # 定义生成随机数个数
# r = 4               # 半径为4
# a, b = (0, 0)       # 圆心为(0, 0)
# x1, x2 = a-r, a+r
# y1, y2 = b-r, b+r
#
# i = 0
# for j in range(0, n):
#     x = np.random.uniform(x1, x2)
#     y = np.random.uniform(y1, y2)
#     if x**2 + y**2 <= 16.0:
#         i += 1
#
# p = (i/float(n))*4
# print(p)

# 访问数组
a = np.arange(10)
print(a[0], a[:6], a[-1], a[1:-1:2])
# # 创建数组
# a = np.arange(12)
# # 设置数组形状
# b = a.reshape(3, 4)
# # 横向展平数组
# c = b.ravel()
# d = b.flatten()
# # 纵向展平数组
# e = b.flatten('F')
# # 横向组合数组
# f = b*3
# g = np.hstack((b, f))
# g = np.concatenate((b, f), axis=1)
# # 纵向组合数组
# h = np.vstack((b, f))
# h = np.concatenate((b, f), axis=0)
# # 横向平均分隔数组
# i = np.hsplit(g, 2)
# i = np.split(g, 4, axis=1)
# print(g, '\n', h, '\n', i)
# # 纵向平均分隔数组
# j = np.vsplit(h, 3)
# j = np.split(h, 2, axis=0)

# # 创建NumPy矩阵
# a = np.mat("1 2 3; 4 5 6; 7 8 9")
# b = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a[0], '\n', b)
#
# # 小矩阵合成大矩阵
# a = np.diag([1, 2, 3])
# b = np.eye(3)
# c = np.bmat("a b")     # 横向组合矩阵
# d = np.bmat("a; b")    # 纵向组合矩阵
# # print(a, '\n'*2, b, '\n'*2, c, '\n'*2, d)
#
# # 矩阵运算
# a = np.mat("1 3 3; 4 5 6; 7 8 9")
# b = np.mat("1 1 1; 2 2 2; 3 3 3")
# # 矩阵相加
# c = a + b
# # 矩阵相减
# d = a - b
# # 矩阵相乘
# e = 3*a
# f = a*b
# # 矩阵内乘
# g = np.multiply(a, b)
# # 矩阵转置
# h = a.T
# # 矩阵共轭转置
# i = a.H
# # 矩阵求逆(存在逆时)
# j = a.I
# # 矩阵的二维数组
# k = a.A
# print(a, b, c, d, e, f, g, h, i, j, k)

# # ufunc函数——通用函数
# # ufunc函数又称通用函数，是一种能够
# # 对数组中的所有元素进行操作的函数
#
# # 数组四则运算
# a = np.array([1, 2, 3])
# b = np.array([2, 1, 3])
# # 数组相加
# c = a + b
# # 数组相减
# d = a - b
# # 数组相乘
# e = a*b
# # 数组相除
# f = a/b
# # 数组幂运算
# g = a**b
# # print(a,b,c,d,e,f,g,'\n'*2)
#
# # 数组比较运算
# # 小于运算
# c = a < b
# # 大于运算
# d = a > b
# # 等于运算
# e = a == b
# # 小于、等于运算
# f = a <= b
# # 大于、等于运算
# g = a >= b
# # 不等运算
# h = a != b
#
# # 数组逻辑运算
# # and运算
# i = np.all(a == b)
# # or运算
# j = np.any(a == b)
# # print(c,d,e,f,g,h,'\n'*2)
# # print(i,j)
#
# # ufunc函数的广播机制
# # 广播是指不同形状的数组之间执行算数运算的方式
# a = np.array([[1, 2, 3], [2, 1, 3], [1, 4, 3]])
# b = np.array([2, 1, 3])
# c = np.array([[2], [1], [3]])
# d = a + b
# e = a + c
# print(a, '\n', b, '\n',  c, '\n',  d, '\n',  e)

# # NumPy文件读写方法
# # 二进制数据存储
# # 保存一个数组
# a = np.arange(10).reshape(2, 5)
# b = np.arange(6).reshape(3, 2)
# np.save("E://data analysis by python//a", a)
# # 保存多个数组
# np.savez("E://data analysis by python//a_b", a, b)
# # print(a, '\n', b)
# # 二进制文件读取
# # 读取单个文件
# c = np.load("E://data analysis by python//a.npy")
# # 读取多个文件
# d = np.load("E://data analysis by python//a_b.npz")
# print(c, '\n', d['arr_0'], '\n', d['arr_1'])
# # 保存数组至文本文件中
# # fmt="%f"表示保存为浮点型，delimiter=","表示数据间分隔符为","
# np.savetxt("E:/data analysis by python/a.txt", a, fmt="%f", delimiter=",")
# # 读取文本文件
# a = np.loadtxt("E:/data analysis by python/a.txt", delimiter=",")
# b = np.genfromtxt("E:/data analysis by python/a.txt", delimiter=",")
# print(a, b)
#
# # 数据排序
# # seed为随机数种子，随机数种子固定，随机数不变
# a = np.random.seed(10)
# b = np.random.randint(1, 10, size=10)
# c = np.random.randint(1, 10, size=(3, 3))
# print(a, b, c)
# # 直接排序
# d = b.sort()
# # 沿着横轴对每一行进行排序
# e = c.sort(axis=1)
# # 沿着纵轴对每一列进行排序
# f = c.sort(axis=0)
# # 请注意d,e,f返回值为None，因为sort排序是直接对数组操作，
# # a,b,c不可逆，d,e,f为中间变量。
# print(a, b, c)
# print(d, e, f)
# # argsort函数排序,返回重新排序值下标
# g = b.argsort()
#
# # 数据去重与重复
# # 数据去重，b、c能达到相同结果
# a = np.array(['赵', '钱', '孙', '李', '周', '赵', '钱'])
# b = np.unique(a)
# c = set(a)
# print(a, b, c)
# # 重复数组两次
# a = np.arange(5)
# b = np.tile(a, 2)
# # 重复数组元素两次
# a = np.array([[1, 2, 3], [2, 1, 3], [1, 4, 3]])
# # 按行进行元素重复
# b = a.repeat(2, axis=0)
# # 按列进行元素重复
# c = a.repeat(2, axis=1)
# print(a, b, c)

# # 常用函数
# a = np.array([[1, 2, 3], [2, 1, 3], [1, 4, 3]])
# # 数组元素求和
# b = np.sum(a)
# # 沿横轴求和
# c = a.sum(axis=1)
# # 沿纵轴求和
# d = a.sum(axis=0)
# # 数组元素求均值
# e = np.mean(a)
# # 沿横轴求均值
# f = a.mean(axis=1)
# # 沿纵轴求均值
# g = a.mean(axis=0)
# # 求数组标准差
# h = np.std(a)
# # 求数组方差
# i = np.var(a)
# # 求数组最大值
# j = np.max(a)
# # 求数组最小值
# k = np.min(a)
# # 求元素累计和
# m = np.cumsum(a)
# # 求元素累计积
# n = np.cumprod(a)
# print(a,b,c,d,'\n')
# print(e,f,g,'\n',h,j,k,m,n)

#
# a = np.array([0, 1, 2, 5])
# b = np.array([4, 5, 6, 7])
# # c = []
# # for i in range(len(a)):
# #     c.append(a[i]*b[i])
# # print(c)
#
# c = a + b
# print(c)
#
# a = np.arange(20).reshape(4, 5)
#
# print(a.ndim)


# b = np.array([[1.0, 2.0], [3.0, 4.0]])
# print(b)
# c = b.transpose()
# a = np.linalg.inv(c)
# print(b, '\n', c, '\n', a)
# d = a@c
# print(d)
# # 迹
# e = np.trace(d)
# print(e)

# a = np.array([[1.0, 2.0], [3.0, 4.0]])
#
# y = np.array([[5.], [7.]])
# b = np.linalg.solve(a, y)
# print(b)












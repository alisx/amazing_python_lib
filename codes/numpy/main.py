import numpy as np

# 创建一个简单的一维数组 
array_1d = np.array([1, 2, 3, 4])
print(array_1d)

# 创建一个二维数组 
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)

# 元素级别的运算，所有元素都乘以 2
print(array_1d * 2)

# 矩阵乘法 
print(np.dot(array_2d, array_2d.T))  # .T 表示矩阵的转置

# 获取第二行的所有数据 
print(array_2d[1])

# 获取第一列的所有数据 
print(array_2d[:, 0])

# 线性代数模块 
from numpy import linalg as LA

# 计算矩阵的行列式 
det = LA.det(array_2d)
print(det)
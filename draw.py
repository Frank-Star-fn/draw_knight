import matplotlib.pyplot as plt
import numpy as np
import time

# 创建一个空白的Figure对象和Axes对象
fig, ax = plt.subplots(figsize=(4.6, 6.4))  # 高度可以调整为适当的值，以适应半圆形
# 隐藏坐标轴
ax.axis('off')

# 左角
# 创建一个半圆形
size_horn=0.9
theta = np.linspace(np.pi/2, 3*np.pi/2, 100)
x_semicircle = np.cos(theta)*size_horn
y_semicircle = np.sin(theta)*size_horn-0.1

theta2 = np.linspace(np.pi*0.5, 3/2*np.pi, 50)
x_semicircle2 = np.cos(theta2)/2+0.11
y_semicircle2 = np.sin(theta2)/2-0.18
ax.plot(x_semicircle, y_semicircle, linewidth=2, color='blue')
ax.plot(x_semicircle2, y_semicircle2, linewidth=2, color='blue')

x_values = [0.11,-0.225]  # x坐标
y_values = [0.32,0.453]   # y坐标
plt.plot(x_values, y_values, 'b-')  # 'b-'表示蓝色实线，你可以根据需要更改线条的样式和颜色

x_values = [-0.225,0]  # x坐标
y_values = [0.453,0.8]   # y坐标
plt.plot(x_values, y_values, 'b-')  


# 小骑士的头顶线
x_values = [0.11,1.6-0.11]  # x坐标
y_values = [-0.68,-0.68]   # y坐标
plt.plot(x_values, y_values, 'b-')  # 'b-'表示蓝色实线，你可以根据需要更改线条的样式和颜色


# 右角
size_horn=0.9
theta3 = np.linspace(-np.pi/2, np.pi/2, 100)  # 调整角度范围
x_semicircle3 = np.cos(theta3)*size_horn+1.6
y_semicircle3 = np.sin(theta3)*size_horn-0.1

theta4 = np.linspace(-np.pi/2, np.pi/2, 100)  # 调整角度范围
x_semicircle4 = np.cos(theta4)/2+1.6-0.11
y_semicircle4 = np.sin(theta4)/2-0.18

ax.plot(x_semicircle3, y_semicircle3, linewidth=2, color='blue')
ax.plot(x_semicircle4, y_semicircle4, linewidth=2, color='blue')
# 右角
x_values = [1.49,1.811]  # x坐标
y_values = [0.33,0.429]   # y坐标
plt.plot(x_values, y_values, 'b-')  # 'b-'表示蓝色实线，你可以根据需要更改线条的样式和颜色

x_values = [1.811,1.59]  # x坐标
y_values = [0.429,0.8]   # y坐标
plt.plot(x_values, y_values, 'b-')  



x_values = [0,-0.1]  # x坐标
y_values = [-1,-1.8]   # y坐标
plt.plot(x_values, y_values, 'b-')  # 'b-'表示蓝色实线，你可以根据需要更改线条的样式和颜色

theta5 = np.linspace(-np.pi, -np.pi/2, 100)  # 调整角度范围
x_semicircle5 = np.cos(theta5)/2+0.5-0.1
y_semicircle5 = np.sin(theta5)/2-1.8
ax.plot(x_semicircle5, y_semicircle5, linewidth=2, color='blue')

x_values = [0.4,1.2]  # x坐标
y_values = [-2.3,-2.3]   # y坐标
plt.plot(x_values, y_values, 'b-')  # 'b-'表示蓝色实线

x_values = [1.6,1.7]  # x坐标
y_values = [-1,-1.8]   # y坐标
plt.plot(x_values, y_values, 'b-')

theta5 = np.linspace(-np.pi/2, 0, 100)  # 调整角度范围
x_semicircle5 = np.cos(theta5)/2+1.2
y_semicircle5 = np.sin(theta5)/2-1.8
ax.plot(x_semicircle5, y_semicircle5, linewidth=2, color='blue')


# 眼睛
center = (0.35, -1.77)  # 圆心坐标
radius = 0.26     # 半径
# 画实心圆
circle = plt.Circle(center, radius, facecolor='black', edgecolor='black')  # 蓝色填充，黑色边界
ax.add_patch(circle)

center = (1.25, -1.77)  # 圆心坐标
circle = plt.Circle(center, radius, facecolor='black', edgecolor='black')  # 蓝色填充，黑色边界
ax.add_patch(circle)


# 左披风
x_values = [0.4,0.1]  # x坐标
y_values = [-2.3,-3.3]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.1,-0.05]  # x坐标
y_values = [-3.3,-3.6]   # y坐标
plt.plot(x_values, y_values, 'b-')

theta5 = np.linspace(-np.pi/3, 0, 100)  # 调整角度范围
x_semicircle5 = np.cos(theta5)*1.5-0.8
y_semicircle5 = np.sin(theta5)*1.5-2.3
ax.plot(x_semicircle5, y_semicircle5, linewidth=2, color='blue')


x_values = [0.82,0.45]  # x坐标
y_values = [-2.89,-3.3]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.45,-0.05]  # x坐标
y_values = [-3.3,-3.6]   # y坐标
plt.plot(x_values, y_values, 'b-')



# 右披风
theta5 = np.linspace(-np.pi, -1.9/3*np.pi, 100)  # 调整角度范围
x_semicircle5 = np.cos(theta5)*1.5+2.2
y_semicircle5 = np.sin(theta5)*1.5-2.3
ax.plot(x_semicircle5, y_semicircle5, linewidth=2, color='blue')

x_values = [1.2,1.4]  # x坐标
y_values = [-2.3,-2.8]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [1.4,1.6]  # x坐标
y_values = [-2.8,-3.65]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.9,1.2]  # x坐标
y_values = [-2.3,-3]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [1.2,1.6]  # x坐标
y_values = [-3,-3.65]   # y坐标
plt.plot(x_values, y_values, 'b-')

# 腿
x_values = [0.4,0.481]  # x坐标
y_values = [-3.33,-3.76]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.481,0.64]  # x坐标
y_values = [-3.76,-3.77]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.64,0.8]  # x坐标
y_values = [-3.77,-3.36]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.8,0.96]  # x坐标
y_values = [-3.36,-3.77]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.96,0.96+0.159]  # x坐标
y_values = [-3.77,-3.76]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.96+0.159,1.176]  # x坐标
y_values = [-3.76,-3.4]   # y坐标
plt.plot(x_values, y_values, 'b-')



# 骨钉
x_values = [0.174,0.072]  # x坐标
y_values = [-2.243,-2.36]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.072,-0.214]  # x坐标
y_values = [-2.36,-2.153]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [-0.214,-0.296]  # x坐标
y_values = [-2.153,-2.253]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [-0.296,-0.04]  # x坐标
y_values = [-2.253,-2.453]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [-0.04,-0.122]  # x坐标
y_values = [-2.453,-2.543]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [-0.122,0.246]  # x坐标
y_values = [-2.543,-2.744]   # y坐标
plt.plot(x_values, y_values, 'b-')

x_values = [0.246,0.368]  # x坐标
y_values = [-2.273,-2.383]   # y坐标
plt.plot(x_values, y_values, 'b-')


# 定义多边形的顶点坐标
vertices = np.array([[0.174, -2.243], [0.072, -2.36], [-0.214, -2.153],
                     [-0.296, -2.253], [-0.04,-2.453], [-0.122, -2.543],
                     [0.246,-2.744], [0.368,-2.383], [0.174, -2.243]])

val=0.87
custom_gray = (val, val, val)  # 使用RGB分量，红色最大（1），绿色和蓝色为0

# 画实心多边形
pentagon = plt.Polygon(vertices, facecolor=custom_gray, edgecolor='gray')  # 绿色填充，黑色边界
ax.add_patch(pentagon)


# 显示图形
plt.show()

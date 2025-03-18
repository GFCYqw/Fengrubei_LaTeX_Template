import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)  # 设置随机种子以获得可重复的结果
n_points = 100  # 定义数据点的数量

# 生成线性分布的数据点
x = np.linspace(0, 5 * np.pi, n_points)
y = np.linspace(0, 5 * np.pi, n_points)
z = np.linspace(0, 0.3, n_points)

# 生成网格
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# 添加噪声
noise = np.random.normal(0, 0.1, (n_points, n_points))
Z_noisy = Z + noise

# 创建一个新的图形窗口
fig = plt.figure(figsize=(10, 8))

# 添加一个3D subplot
ax = fig.add_subplot(111, projection="3d")

# 绘制带有噪声的三维散点图
ax.scatter(X, Y, Z_noisy, c=Z_noisy, cmap="viridis", s=5)

# 添加颜色条
ax.figure.colorbar(
    ax.scatter(X, Y, Z_noisy, c=Z_noisy, cmap="viridis", s=5), label="Height"
)

# 设置标题和轴标签
ax.set_title("Surface Image in 3D")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# 显示图形
plt.show()

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # 设置随机种子以获得可重复的结果
n_points = 1000  # 定义数据点的数量

# 生成线性分布的x和y坐标
x = np.linspace(0, 10 * np.pi, n_points)
y = np.linspace(0, 10 * np.pi, n_points)
XX, YY = np.meshgrid(x, y)

# 生成模拟数据
Z = np.sin(XX) + np.sin(YY)  # 生成正弦波数据
noise = np.random.normal(0, 0.2, (n_points, n_points))
Z_noisy = Z + noise  # 添加噪声

# 创建一个新的图形窗口
plt.figure(figsize=(10, 8))

# 绘制带有噪声的正弦波
plt.contourf(XX, YY, Z_noisy, cmap="viridis", levels=20)
plt.colorbar(label="Height")
plt.title("Surface Image in 2D")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 显示网格
plt.grid(True)
plt.show()

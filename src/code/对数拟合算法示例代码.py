import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 生成模拟数据
x = np.linspace(1, 10, 50)
y = 100 * np.exp(-0.1 * x)  # 使用对数函数生成数据
y_noisy = y + np.random.normal(0, 5, x.shape)  # 添加一些噪声


# 定义对数函数模型
def log_model(x, a, b):
    return a * np.log(x) + b


# 使用curve_fit进行曲线拟合
popt, pcov = curve_fit(log_model, x, y_noisy)

# 使用拟合参数生成拟合曲线
x_fit = np.linspace(1, 10, 200)
y_fit = log_model(x_fit, *popt)

# 绘制原始数据和拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y_noisy, label="Noisy Data", color="blue", alpha=0.5)
plt.plot(x_fit, y_fit, label="Fitted Curve", color="red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Logarithmic Curve Fitting")
plt.legend()
plt.show()

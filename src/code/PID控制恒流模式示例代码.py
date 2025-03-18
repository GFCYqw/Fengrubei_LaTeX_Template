import time
import matplotlib.pyplot as plt
import math

# PID控制器参数
Kp = 1.0
Ki = 0.2
Kd = 5.0

# 初始化全局变量
setpoint = 1.0  # 目标隧穿电流
integral = 0.0  # 积分项初始化
previous_time = time.time()  # 上次控制时间初始化
sample_time = 0.2  # 控制循环的时间间隔，单位：秒
previous_error = 0.0  # 初始化previous_error
max_runtime = 10  # 最大运行时间，单位：秒

# 用于记录数据的列表
measurements = []
pid_outputs = []
times = []


# 假设的测量和调整函数
def measure_current():
    # 测量隧穿电流
    # 这里模拟一个正弦波电流，用于演示
    return 0.5 + 0.2 * math.sin(2 * math.pi * time.time())


def adjust_probe(position):
    # 调整探针位置
    # 这里记录PID输出值，用于后续绘图
    pid_outputs.append(position)


def pid_controller():
    global integral, previous_time, previous_error
    current_time = time.time()
    if current_time - previous_time >= max_runtime:  # 检查运行时间是否超过最大运行时间
        return False
    measured_current = measure_current()
    error = setpoint - measured_current  # 计算误差
    integral = min(
        max(integral + error * sample_time, -100), 100
    )  # 计算积分项，限制在-100到100
    derivative = (
        (error - previous_error) / sample_time if previous_time != 0 else 0
    )  # 计算微分项
    previous_error = error
    output = Kp * error + Ki * integral + Kd * derivative  # 计算PID输出
    output = max(min(output, 100.0), -100.0)  # PID输出限制在-100到100
    adjust_probe(output)  # 调整探针位置
    measurements.append(measured_current)  # 记录数据
    times.append(current_time - previous_time)
    return True


# 主函数
def main():
    try:
        while pid_controller():  # 调用PID控制器，根据返回值决定是否继续循环
            time.sleep(sample_time)  # 等待指定的采样时间
    except KeyboardInterrupt:
        print("用户中断了PID控制器。")
    finally:
        # 绘制测量电流随时间变化的图表
        plt.figure(figsize=(10, 5))
        plt.plot(times, measurements, label="Measured Current")
        plt.xlabel("Time (s)")
        plt.ylabel("Current")
        plt.title("Measured Current Over Time")
        plt.legend()
        plt.show()

    # 绘制PID控制器输出随时间变化的图表
    plt.figure(figsize=(10, 5))
    plt.plot(times, pid_outputs, label="PID Output", color="r")
    plt.xlabel("Time (s)")
    plt.ylabel("PID Output")
    plt.title("PID Output Over Time")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

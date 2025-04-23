import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from matplotlib.colors import ListedColormap

# 读取并处理数据（与之前相同）
file_path = 'T_FreeBoundary.xlsx'
sheet_name = 'Sheet1'

data_df = pd.read_excel(
    file_path,
    sheet_name=sheet_name,
    skiprows=6,
    usecols="B:E",
    header=None,
    names=['K', 'T1', 'T2', 'T3']
)

data_rows = []
for _, row in data_df.iterrows():
    if pd.isna(row['K']):
        continue
    k = float(row['K'])
    for t_col, t_val in zip(['T1', 'T2', 'T3'], [1.0, 2.0, 3.0]):
        loss = row[t_col]
        if pd.notna(loss):
            data_rows.append({'T': t_val, 'K': k, 'Loss': loss})

data = pd.DataFrame(data_rows)

# 按T分组数据
T_groups = data.groupby('T')


# 自定义拟合函数示例（可根据数据趋势调整）
def model_func(k, a, b, c):
    return a * k ** 2 + b * k + c  # 二次多项式拟合


# 创建三维图
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.xaxis.line.set_linewidth(2)
ax.yaxis.line.set_linewidth(2)
ax.zaxis.line.set_linewidth(2)

# 定义颜色和线型
colors = ['r', 'g', 'b']
t_values = [1.0, 2.0, 3.0]

# 遍历每个T值进行拟合和绘图
for idx, (t, group) in enumerate(T_groups):
    # 提取当前T的K和Loss数据并按K排序
    group_sorted = group.sort_values('K')
    k_data = group_sorted['K'].values
    loss_data = group_sorted['Loss'].values

    # 方法1：多项式拟合（此处用二次）
    coeffs = np.polyfit(k_data, loss_data, 2)
    poly = np.poly1d(coeffs)
    k_fit = np.linspace(min(k_data), max(k_data), 100)
    loss_fit = poly(k_fit)

    # 方法2：样条插值（若数据波动大）
    # spline = interp1d(k_data, loss_data, kind='cubic', fill_value="extrapolate")
    # loss_fit = spline(k_fit)

    # 在三维空间中绘制拟合曲线
    ax.plot(
        [t] * len(k_fit),  # 固定T值
        k_fit,
        loss_fit,
        color=colors[idx],
        linewidth=2,
        label=f'T={t} Fit'
    )

    # 叠加原始数据点
    ax.scatter(
        [t] * len(k_data),
        k_data,
        loss_data,
        color=colors[idx],
        s=50,
        alpha=0.6,
    )

# ========== 按K拟合曲线（5条） ==========
K_values = [100, 200, 400, 1000, 1500]
K_cmap = ListedColormap(['#FFD700', '#FFA500', '#FF6347', '#DC143C', '#8B0000'])  # 黄橙红渐变

for idx, k in enumerate(K_values):
    # 提取当前K的数据
    k_data = data[data['K'] == k].sort_values('T')
    if len(k_data) < 2:  # 需要至少2个点进行拟合
        continue

    # 多项式拟合（选择二次）
    coeffs = np.polyfit(k_data['T'], np.log10(k_data['Loss']), 2)  # 对数拟合
    poly = np.poly1d(coeffs)
    t_fit = np.linspace(1.0, 3.0, 100)
    loss_fit = 10 ** poly(t_fit)  # 指数转换回线性值

    # 绘制拟合曲线
    ax.plot(
        t_fit,
        [k] * 100,  # 固定K值
        loss_fit,
        color=K_cmap(idx / len(K_values)),
        linewidth=2,
        linestyle='--',
        label=f'K={k} Fit'
    )

    # 绘制原始数据点
    ax.scatter(
        k_data['T'],
        [k] * len(k_data),
        k_data['Loss'],
        color=K_cmap(idx / len(K_values)),
        s=60,
        edgecolor='k',
        alpha=0.8,
        marker='s'
    )

# 设置坐标轴和标签
ax.set_xlabel('T', fontsize=12, labelpad=10)
ax.set_ylabel('K', fontsize=12, labelpad=10)
ax.set_zlabel('FB Loss', fontsize=12, labelpad=10)

ax.xaxis.set_ticks_position('lower')  # X轴刻度在原点侧
ax.yaxis.set_ticks_position('lower')  # Y轴刻度在原点侧

ax.view_init(elev=20, azim=-120)
plt.legend()
plt.tight_layout()
plt.show()
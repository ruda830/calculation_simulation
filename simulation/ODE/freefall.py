"""
###連立１階常微分方程式を解く
##自由落下のシミュレーション

"""
"""
オイラー法を用いて解く。

v = v0 + gt
x = X0 + vt

→刻み幅hを用いる
"""
import numpy
import matplotlib.pyplot as plt

g = -9.80665

#初期時刻
t = 0.0
h = 0.01

v = float(input("初期速度v0を入力: "))
x = float(input("初期高度x0を入力: "))


#リストに格納
tlist = [t]
xlist = [x]

#メイン計算
while x >= 0:
    t += h
    v += g*h
    x += v*h

    print(t, x, v)
    #リストの要素
    tlist.append(t)
    xlist.append(x)

#グラフにプロット
plt.plot(tlist, xlist)
plt.show()


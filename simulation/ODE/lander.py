"""
###連立１階常微分方程式を解く
##着陸ロケットのシミュレーション

"""
"""
オイラー法を用いて解く。
速度は下向きを正とする。
dv/dt =  g - a  (aは逆噴射の加速度)
dx/dt = v

→逆噴射の時間(タイミング)はtfとする。
→刻み幅hを用いる
"""
import numpy
import matplotlib.pyplot as plt

#逆噴射時のロケットが出す加速度を決定する係数γ
γ = 1.5
g = 9.80665

#逆噴射の場合分け
def reverse_thrust(t, tf):
    #逆噴射タイミングを過ぎたとき
    if t >= tf:
        return g * -γ
        #returnで返してるのは上のa(= gγ)に値するところ
    else:
        return 0.0;

#初期時刻
t = 0.0
h = 0.01
v = 0

x0 = float(input("初期高度x0を入力: "))
tf =float(input("逆噴射の開始時刻（タイミング）tfを入力: "))
x = x0
#リストに格納
tlist = [t]
xlist = [x]

#メイン計算
while (x > 0) and (x <= x0):
    t += h
    v += (g + reverse_thrust(t, tf)) * h
    x -= v*h

    print(t, x, v)
    #リストの要素
    tlist.append(t)
    xlist.append(x)

#グラフにプロット
plt.plot(tlist, xlist)
plt.show()


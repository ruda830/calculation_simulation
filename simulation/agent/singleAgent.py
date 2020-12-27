"""
###シングルエージェント
#2次元座標上で動作するエージェント
"""
"""
#エージェントの情報を格納するAgentクラスの内部情報

Agentクラス【ポ〇モンで言うとピカ〇ュウ】
ーーーーーーーーーーインスタンス変数【ポ〇モンで言うと個体の状態、タイプ】ーーーーーーーーーーーー
名称      役割
category        エージェントのカテゴリ
x,y     エージェントのx座標、y座標
dx,dy       各座標の増分についての初期値

ーーーーーーーーーーメゾット【ポ〇モンで言うとバトル方法】ーーーーーーーーーーーー
__init__()      コンストラクタ(初期値の設定)
calcnext()      次時刻の状態への更新
cat()       カテゴリの計算メゾット
reverse()       マルチエージェント用の前処理
putstate()       エージェントの状態についての出力

"""
import numpy as np
import matplotlib.pyplot as plt

#シミュレーション打ち切り時刻
TIMELIMIT = 100


class Agent:
    def __init__(self, cat):
        #コンストラクタ
        self.category = cat
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 1

    def calcnext(self):
        #cat0に関する更新、今回はシングルエージェントなのでこれだけ
        if self.category == 0:
            self.cat0()
        else:
            print("ERROR カテゴリがありません")

    def cat0(self):
        #内部状態の更新
        self.dx = self.reverse(self.dx)
        self.dy = self.reverse(self.dy)
        self.x += self.dx
        self.y += self.dy

    def reverse(self,i):
        #dx,dy増減のためのメゾット
        if i == 0:
            return 1
        else:
            return 0

    def putstate(self):
        print(self.x, self.y)




#calcn()関数: calcnext()とputstate()を時間毎に呼び出す関数
def calcn(a):
    for i in range(len(a)):
        a[i].calcnext()
        a[i].putstate()

        xlist.append(a[i].x)
        ylist.append(a[i].y)


a = [Agent(0)]

xlist = []
ylist = []

#エージェントシミュレーション
for t in range(TIMELIMIT):
    calcn(a)

    plt.clf() #時間毎にプロットをするので毎時間グラフをきれいにするという意味
    plt.axis([0,60,0,60])
    plt.plot(xlist, ylist, ".") #"."は黒点でAgent[0]が表示されるという意味
    plt.pause(0.01) #時間毎にプロットをするのでそのインターバル
    xlist.clear()
    ylist.clear()

plt.show()
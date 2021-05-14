#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy
plt.rcParams['text.usetex'] = True

class Chart:
    def __init__(self , url , x , **y):
        self.url = url
        self.x = x
        self.y = y
        
    def read(self):
        #データの読み込み
        df = pd.read_excel(self.url)

        fig = plt.figure()

        plt.style.use('classic') #グラフの余白消去

        x = df[self.x] #x軸のデータ
        for (i, j) in self.y.items():
            a = df[i]
            plt.scatter(x , a , s=10 , color="black" , marker=j , label = i)      

        plt.tick_params(direction='in' , labelsize='8' ) #目盛りの向きとサイズ
        plt.gca().yaxis.set_ticks_position('left')
        plt.gca().xaxis.set_ticks_position('bottom')
        
        
    def show(self):
        plt.show() #グラフの出力
        
    def label(self , x_label , y_label):
        plt.xlabel(x_label) #x軸ラベル
        plt.ylabel(y_label) #y軸ラベル
        
    def line(self):
        df = pd.read_excel(self.url)
        x = df[self.x] #x軸のデータ
        for k in self.y:
            a = df[k]
            line = np.polyfit(x , a , 1) #傾きと切片
            print(line) #傾きと切片の出力
            f = np.poly1d(line)
            l = f(x)
            plt.plot(x , l , color="black" ) #直線の出力


# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:12:21 2020

@author: saima
"""


'''
import math
coins=[1,5,6,9]
w=10
a=[[0] + [math.inf]*w for x in range(len(coins))]
for i in range(0,len(coins)):
    for j in range(1,w+1):
        if(coins[i]>j):
            a[i][j]=a[i-1][j]
        else:
            a[i][j]=min((a[i-1][j]),(1+a[i][j-coins[i]]))
for i in range(len(coins)):
    print(a[i])
'''


import math
coins=[1,3,4]
w=int(input())
a=[[0] + [math.inf]*w for x in range(len(coins))]
for i in range(0,len(coins)):
    for j in range(1,w+1):
        if(coins[i]>j):
            a[i][j]=a[i-1][j]
        else:
            a[i][j]=min((a[i-1][j]),(1+a[i][j-coins[i]]))
print(a[i][j])




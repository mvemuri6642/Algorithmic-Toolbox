# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:25:42 2020

@author: mvemuri6642
"""
import operator
val=[]
wt=[]
x=0
l=[]
max=0
frac=0
n,m=list(map(int,input().split()))
for i in range(n):
    x=list(map(int,input().split()))
    val.append(int(x[0]))
    wt.append(int(x[1]))
for i in range(n):
    l.append([val[i],wt[i],val[i]*1/wt[i]])
l=sorted(l,reverse=True,key=operator.itemgetter(2))
for i in range(n):
    if m>0 and l[i][1]<m:
        m-=l[i][1]
        max+=l[i][0]
    else:
        frac=i
        break
if m>0:
    max+=m*l[frac][0]/l[frac][1]
print(max)
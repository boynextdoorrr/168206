# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:15:19 2018

@author: Yan
"""

RE={}
def fa(n):
    if n<2:
        return n
    else:
        return fa(n-2)+fa(n-1)
for i in range(40):
    if RE.get(i):
        print('here')
        print(RE.get(i),end=', ')
    else:
        tmp=fa(i)
        RE.setdefault(i,tmp)
        print(tmp,end=', ')
        
print(fa(20))

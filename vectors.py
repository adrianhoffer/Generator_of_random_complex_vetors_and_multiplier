# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:27:52 2020

@author: Adrian
"""

import random as rnd

for i in range (0,15):
    a=rnd.randint(-5,10)
    b=rnd.randint(-5,2)
    c=rnd.randint(-5,3)
    d=rnd.randint(-2,3)
    print("------------------------")
    print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))
    
    print(str(a*c-b*d) + " " +str(b*c+a*d))
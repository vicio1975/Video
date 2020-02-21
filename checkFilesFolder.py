# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:54:23 2020

@author: vsamm
"""

import os 

listFiles = [] 
loc = os.getcwd()
listFiles = [fn for fn in os.listdir(loc) if fn.endswith('.jpg')]
for p in listFiles:
    print (p)
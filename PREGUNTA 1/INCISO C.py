# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:25:16 2022

@author: 56946
"""

import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('diabetes.csv', sep=",")

for i in datos:
    plt.hist(datos[i])
    plt.show()
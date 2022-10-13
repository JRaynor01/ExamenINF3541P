# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:35:25 2022

@author: 56946
"""

import numpy as np
import pandas as pd

datos = pd.read_csv('diabetes.csv', sep=",")

for i in datos:
    print(i)
    p25 = np.percentile(datos[i], 25)
    p90 = np.percentile(datos[i], 90)
    p95 = np.percentile(datos[i], 95)
    print(p25,p90,p95)
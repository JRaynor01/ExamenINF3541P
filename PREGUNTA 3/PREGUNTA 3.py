# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:03:49 2022

@author: 56946
"""
#Algoritmos de preprocesamiento con python
import pandas as pd
import numpy as np

datos= pd.read_csv('diabetes.csv')

#print(datos.to_string())

print(datos.describe())

#ordenar segun edad
datos=datos.sort_values(["Age"],ascending=False)

print(datos)

#Discretizar los datos
from sklearn.preprocessing import KBinsDiscretizer

data = pd.read_csv('diabetes.csv', header=0)
x_datos = np.array(data)
prepro = KBinsDiscretizer(n_bins=3, encode= 'ordinal', strategy = 'uniform')
x_datos_discretinizados = prepro.fit_transform(x_datos)
print("Datos Discretizados")
print(x_datos_discretinizados)


#Mostrar el datset co ntenido
print(data.describe())

#Eliminar columnas no importantes
dataset = data.drop("Pregnancies", axis=1)
print(dataset)
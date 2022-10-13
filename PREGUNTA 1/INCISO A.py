# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:09:50 2022

@author: 56946
"""

# a. El calculo del 1er cuartil de datos, el percentil 50 por columna;
#  explique qué significa en cada caso mediante Python sin uso de librerías

import csv

def percentil(per, datos):
    # Copiar la lista para no alterarla
    x = datos.copy()
    x.sort()

    n = len(x)
    rank = (per / 100.0) * (n - 1)
    rank_int = int(rank)
    rank_dec = rank % 1

    if rank_dec:
        p = x[rank_int] + rank_dec * (x[rank_int + 1] - x[rank_int])
    else:
        p = x[rank_int]

    return p

def calculo(list):
    cuartil = percentil(25, list)
    percent_90 = percentil(90, list)
    percent_95 = percentil(95, list)
    quartiles = [cuartil, percent_90, percent_95]
    print(quartiles)


tabla=[]
Pregnancies=[]
Glucose=[]
BloodPressure=[]
SkinThickness=[]
Insulin=[]
BMI=[]
DiabetesPedigreeFunction=[]
Age=[]
Outcome=[]

with open('diabetes.csv', newline='') as File:
    corazonDatos = csv.reader(File)
    for row in corazonDatos:
        tabla.append(row)
header=tabla.pop(0)
for a in tabla:
    Pregnancies.append(int(a[0]))
    Glucose.append(int(a[1]))
    BloodPressure.append(int(a[2]))
    SkinThickness.append(int(a[3]))
    Insulin.append(int(a[4]))
    BMI.append(float(a[5]))
    DiabetesPedigreeFunction.append(float(a[6]))
    Age.append(int(a[7]))
    Outcome.append(int(a[8]))

print("Embarazos")
calculo(Pregnancies)
print("Concentración de glucosa plasmática a las 2 horas en una prueba de tolerancia oral a la glucosa")
calculo(Glucose)
print("Presion Arterial")
calculo(BloodPressure)
print("Grosor del pliegue cutáneo del tríceps ")
calculo(SkinThickness)
print("Insulina")
calculo(Insulin)
print("Indice de masa muscular")
calculo(BMI)
print("Diabetes pedigree function")
calculo(DiabetesPedigreeFunction)
print("Edad")
calculo(Age)
print("Positivo en la prueba de diabetes")
calculo(Outcome)

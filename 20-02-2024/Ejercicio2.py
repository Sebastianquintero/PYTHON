# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:46:39 2024

@author: Estudiante
"""

#1. Valor total de lo gastado x mes
#2. Suma Total de los productos en una lista

def operador(o,p,i):
    return(o+p+i)


listaen=[10000,20000,30000,40000,50000]
listafeb=[20000,30000,3400,5000,7500]
listamar=(30000,50000,2000,3000,5000)

acumulador=0;
acumulador2=0;
acumulador3=0;

print("*************************************")

op=list(map(operador,listaen,listafeb,listamar))

for elementos in listaen:
    acumulador +=elementos

for elementos in listafeb:
    acumulador2 +=elementos
    
for elementos in listamar:
    acumulador3 +=elementos


print(f"el total gastado en enero es: {acumulador}")
print(f"el total gastado en febrero es: {acumulador2}")
print(f"el total gastado en marzo es: {acumulador3}")

print("*/***********/*/*/*/*/*/*/*/*//***//*/*/*/*/*")

print(f"el resultado de la suma de cada seccion de producto es: {op}")


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:11:01 2024

@author: Estudiante
"""

#Ejercicio 1 

def operador(n,m):
    return(n+m)
#Lista
l1=[1,2,3,4,5,6]
print(l1)

#Tupla
t1=(1,2,3,4,5,6)
print(t1)

print("***************************************")

#Operaciones entre listas y tuplas
op=list(map(operador,l1,t1))

print(f"La lista 1 es: {l1}: ")
print(f"La tupla 2 es: {t1}: ")
print(f"El resultado de la operacion es: {op}")


print("*/**************************************")

#filtros

def filtro(elemento):
    return(elemento>10)

l1=[1,10,25,9,8,15]
f1=list(filter(filtro, l1))

print(f"La lista completa de: {l1}")
print(f"la lista filtrada es: {f1}")

print("***************************************")

#Reducir lista a una expresion

l5=[1,2,3,4,5]
acumulador=0

for elemento in l5:
    acumulador += elemento
    
print(f"La lista es: {l5}")
print(f"El resultado de reducir la lista es: {acumulador}")
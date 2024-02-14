# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:43:16 2024

@author: Estudiante
"""

def criterio(operacion): #Funcion Publica
    def mult(m,n): #Crear primera funcion
        return m * n
    def suma(m,n): #crear segunda funcion
        return m + n
    def resta(m,n): #Crear tercera funcion
        return m - n
    def division(m,n): #Crear cuarta funcion
        return m / n
    if operacion== '*': #Evaluar valor recibido
        return mult 
    elif operacion=='+':
        return suma
    elif operacion=='-':
        return resta 
    elif operacion=='/':
        return division
#crear variables de operaciones
sumar=criterio('+')
print(sumar(4,5)) #enviar valores

#crear variables de operacion multiplicacion
multiplicar=criterio('*')
print(multiplicar(4,5))

#Crear variables de operacion resta
resta=criterio('-')
print(resta(4,5))

#Crear variables de operacion division
division=criterio('/')
print(division(4,5))

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:59:17 2024

@author: Estudiante
"""

# definir funcion principal, esta recibe a otra funcion
def prueba1(f):
    return f()
#Genero la funcion a mostrar
def mostrar():
    return 10*20
#Almacenamios el resultado de llamar a la funcion principal
muestre = prueba1(mostrar)
#Imprima resultado
print(muestre)
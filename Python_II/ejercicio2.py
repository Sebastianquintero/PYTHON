# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:41:36 2024

@author: Estudiante
"""

naci=int(input("Ingrese Su Año de Nacimiento"))
res=2024

year=res-naci

print("Su edad es",year)

if year>=18:
    print("Es Mayor de edad")
    
else:
    print("Usted es menor de edad")
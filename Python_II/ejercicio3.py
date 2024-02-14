# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:11:06 2024

@author: Estudiante
"""

dinero=int(input("Ingrese El Dinero Que Tiene Actualmente: "))

prod=input("Ingrese El Primer Producto ")
prod1=int(input("Ingrese el valor del producto "))

prod2=input("Ingrese El Segundo Producto ")
prod21=int(input("Ingrese el valor del producto "))

prod3=input("Ingrese El Tercer Producto ")
prod31=int(input("Ingrese el valor del producto "))

prod4=input("Ingrese El Cuarto Producto ")
prod41=int(input("Ingrese el valor del producto "))

prod5=input("Ingrese El Quinto Producto ")
prod51=int(input("Ingrese el valor del producto "))

subtotal=prod1+prod21+prod31+prod41+prod51

print("El subtotal es: ",subtotal)

iva=subtotal*0.19

print("El iva es: ",iva)

total=subtotal+iva

print("El total es: ",total)


if dinero>=total:
    
    cash=dinero-total
    print("El dinero que le sobro fue :",cash)
    
    print("Afortunadamente Le alcanzo para comprar todos los productos")
    
else:
    cash1=dinero-total
    print("El dinero que queda debiendo es: ",cash1)
    
    print("Desafortunadamente NO le alcanza para comprar todos los productos")
    
def calcular (f):
    return f()

def mostrar ():
    return total   

muestre = calcular(mostrar)
print(muestre)
# -*- coding: utf-8 -*-
"""
Para cada uno de los sistemas dados mas abajo:
 • Discretizar los siguientes sistemas de ecuaciones diferenciales para t ∈ [0,5]
 usando el algoritmo de Euler con paso h.
 • Escribir un codigo para resolver numericamente el sistema discrtizado
 • Simular el sistema con paso h = 0.5 seg., h = 0.1 seg., h = 0.05 seg. para
 aproximar la solucion del sistema de ecuaciones diferenciales en el t0 dado.
 • Hacer un cuadro con los resultados obtenidos para los distintos valores h.
"""
import matplotlib.pyplot as plt #Libreria necesaria para graficar
import numpy as np #Libreria necesaria para trabajar con vectores
import os
import pandas as pd
os.system("cls") #Esto es para que cuando corro el codigo se me borre lo anterior


def eulerE(f, y0, t0, tf, h): 
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t)) # Array de 0 de longitud t para rellenar paso a paso con los valores
    y[0] = y0

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        y[i+1] = y[i] + h * f(t[i], y[i])

    return t, y

def eulerV(f, Y0, t0, tf, h): 
    t = np.arange(t0, tf + h, h)
    Y = np.zeros((len(Y0),len(t)))
    
    Y[:,0] = Y0

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        Y[:,i+1] = Y[:,i] + h * f(Y[0,i], Y[1,i])

    return t, Y

def eulerM(M, Y0, t0, tf, h): #M matriz de funciones, Y0 matriz inicial, t0 valor de tiempo inicial, h step
    
    t = np.arange(t0, tf + h, h)

    Y = np.zeros((M.shape[0] ,len(t))) # Matriz de 0 de la misma cantidad de filas que M y t columnas
    Y[:,0] = Y0 # Asigno el valor de la primera columna

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        Y[:,i+1]  = Y[:,i] + h * (M @ Y[:,i]) #: elige toda la fila, @ = producto matricial

    return t, Y

def graficar(x, y, titulo):
    plt.plot(x,y,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
    plt.plot(x,y,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
    plt.title(titulo) #Titulo del grafico
    plt.xlabel('Y') #Titulo del eje
    plt.ylabel('t [s]') #Titulo del eje 
    plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

    plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
    plt.show() #Muestra los graficos
    
    
plt.figure(12) #Genero otra ventana

# ----------------------------------Item A--------------------------------------

def funcA(t,y):
    
    fa= np.sqrt(y)
    
    return fa
        
ta1, fa1= eulerE(funcA, 2, 2, 5, 0.5)
ta2, fa2 = eulerE (funcA, 2, 2, 5, 0.1)
ta3, fa3= eulerE (funcA, 2, 2, 5, 0.05)

graficar(ta1, fa1, "Item A - h:0,5")
graficar(ta2, fa2, "Item A - h:0,1")
graficar(ta3, fa3, "Item A - h:0,05")


# ---------------------------------Item B---------------------------------------








# ---------------------------------Item C---------------------------------------

def funcC (x1,x2):
    
    Mc= np.transpose([x2,np.cos(10*np.pi*x1)])
        
    return Mc
Y0= np.transpose([0,1]) 
    
tc1, Yc1 = eulerV(funcC,Y0,1,5,0.5)
tc2, Yc2= eulerV(funcC,Y0,1,5,0.1)
tc3, Yc3= eulerV(funcC,Y0,1,5,0.05)

graficar(tc1, Yc1[0], "Item C - h:0,5")
graficar(tc2, Yc2[0], "Item C - h:0,1")
graficar(tc3, Yc3[0], "Item C - h:0,05")



# ---------------------------------Item D---------------------------------------

matrizD = np.array([ # Crear una matriz de 3x3 con valores específicos
[0, 1, 0],
[0, 0, 1],
[-2, -3, -4]
])
Y0 = [2,1,0]

#-------------------h=0.5----------------------------------
td1, Yd1 = eulerM(matrizD,Y0,1,5,0.5)
yD1= np.zeros (len(td1))
for i in range (len(td1)-1): 
    yD1[i+1]  = (7*Yd1[1,i])*(5*Yd1[2,i])


#----------------h=0.1-------------------------------------
td2, Yd2= eulerM(matrizD,Y0,1,5,0.1)
yD2= np.zeros (len(td2))

for i in range (len(td2)-1): 
    yD2[i+1]  = (7*Yd2[1,i])*(5*Yd2[2,i])

#-----------------h=0.05------------------------------------

td3, Yd3= eulerM(matrizD,Y0,1,5,0.05)
yD3= np.zeros (len(td3))

for i in range (len(td3)-1): 
    yD3[i+1]  = (7*Yd3[1,i])*(5*Yd3[2,i])

graficar(td1, yD1, "Item D - h:0,5")
graficar(td2, yD2, "Item D - h:0,1")
graficar(td3, yD3, "Item D - h:0,05")

"""


# Crear un diccionario con los datos
datos = {
    '': ['Ana', 'Luis', 'María'],
    'Edad': [23, 30, 27],
    'Ciudad': ['Madrid', 'Buenos Aires', 'Lima']
}


# Convertirlo en un DataFrame (tabla)
tabla = pd.DataFrame(datos)

# Mostrar la tabla
print(tabla) """
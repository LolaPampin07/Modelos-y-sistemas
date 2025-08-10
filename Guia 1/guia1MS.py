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


def eulerV(f, y0, t0, tf, h): 
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t)) # Array de 0 de longitud t para rellenar paso a paso con los valores
    y[0] = y0

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        y[i+1] = y[i] + h * f(t[i], y[i])

    
    # Grafico los resultados    
    plt.figure(1) #Genero otra ventana


    plt.plot(t,y,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
    plt.plot(t,y,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
    plt.title('Metodo de Euler') #Titulo del grafico
    plt.xlabel('Eje x') #Titulo del eje
    plt.ylabel('Eje y') #Titulo del eje 
    plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')


    plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
    plt.show() #Muestra los graficos

    return t, y

def eulerM(M, Y0, t0, tf, h): #M matriz de funciones, Y0 matriz inicial, t0 valor de tiempo inicial, h step
    
    t = np.arange(t0, tf + h, h)

    Y = np.zeros((M.shape[0] ,len(t))) # Matriz de 0 de la misma cantidad de filas que M y t columnas
    Y[:,0] = Y0 # Asigno el valor de la primera columna

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        Y[:,i+1]  = Y[:,i] + h * (M @ Y[:,i]) #: elige toda la fila, @ = producto matricial

    if (M.shape [0] == 1):
    # Grafico los resultado en caso de ser posible (solo una x)  
        plt.figure(1) #Genero otra ventana

        plt.plot(t,Y,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
        plt.plot(t,Y,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
        plt.title('Metodo de Euler') #Titulo del grafico
        plt.xlabel('Y') #Titulo del eje
        plt.ylabel('t [s]') #Titulo del eje 
        plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')
    
        plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
        plt.show() #Muestra los graficos

        return t, Y
    else:
        print (Y) #si la matriz no es graficable (x>1) ==> muestro los resultados de mi matriz
        return t, Y
# ----------------------------------Item A--------------------------------------

def funcA(t,y):
    
    fa= np.sqrt(y)
    
    return fa
        
ta1, fa1= eulerV(funcA, 2, 2, 5, 0.5)
ta2, fa2 = eulerV (funcA, 2, 2, 5, 0.1)
ta3, fa3= eulerV (funcA, 2, 2, 5, 0.05)

"""
# ---------------------------------Item B---------------------------------------

def funcB (t,y):
    
    fb=
    
    return fb

tb1, Yb1 = eulerM(matrizD,Y0,1,5,0.5)
tb2, Yb2= eulerM(matrizD,Y0,1,5,0.1)
tb3, Yb3= eulerM(matrizD,Y0,1,5,0.05)

# ---------------------------------Item C---------------------------------------

def funcC (t,y):
    
    matrizC= np.array(
        
        [0,1]
        
        )
"""
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
plt.figure(1) #Genero otra ventana

plt.plot(td1,yD1,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td1,yD1,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.title('Metodo de Euler - h=0.5') #Titulo del grafico
plt.xlabel('Y') #Titulo del eje
plt.ylabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos

#----------------h=0.1-------------------------------------
td2, Yd2= eulerM(matrizD,Y0,1,5,0.1)
yD2= np.zeros (len(td2))

for i in range (len(td2)-1): 
    yD2[i+1]  = (7*Yd2[1,i])*(5*Yd2[2,i])
    

plt.figure(2) #Genero otra ventana
plt.plot(td2,yD2,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td2,yD2,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.title('Metodo de Euler - h=0.1') #Titulo del grafico
plt.xlabel('Y') #Titulo del eje
plt.ylabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')
plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos


#-----------------h=0.05------------------------------------

td3, Yd3= eulerM(matrizD,Y0,1,5,0.05)
yD3= np.zeros (len(td3))

for i in range (len(td3)-1): 
    yD3[i+1]  = (7*Yd3[1,i])*(5*Yd3[2,i])
plt.figure(3) #Genero otra ventana
plt.plot(td3,yD3,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td3,yD3,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.title('Metodo de Euler - h=0.05') #Titulo del grafico
plt.xlabel('Y') #Titulo del eje
plt.ylabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos


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
# -*- coding: utf-8 -*-
"""
GUIA II 
"""
#-----------------------------LIBRERIAS----------------------------------------------------------------------
import matplotlib.pyplot as plt #Libreria necesaria para graficar
import numpy as np #Libreria necesaria para trabajar con vectores
import os
import pandas as pd
from scipy.integrate import solve_ivp


#-----------------------------EJERCICIO 2----------------------------------------------------------------------
"""
En ciertas circunstancias, el numero de individuos en determinadas poblaciones de bacterias se rige por la ley
 y′ = 0.2y.
 Si al comienzo del experimento hay 30.000 bacterias,
 (a) Cuantas habra 10 horas mas tarde?
 (b) En que instante habra 100.000 bacterias?

"""

y0=[30000] #condicion inicial

def f(t, y):
    return 0.2 * y
t_span=[0, 12]

# Resolviendo con el método RK23 (equivalente a ode23)
sol = solve_ivp(f, t_span, y0, method='RK23', t_eval=np.linspace(0, 12, 100))

# Graficamos la solución
plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solución y''= -2y usando RK23')
plt.grid(True)
plt.show()

#ver como hacer para buscar el valor 10 en py --> en matlab es interpolacion lineal al mas proximo
#el verdadero valor lo hallo en la funcion analitica

#-----------------------------EJERCICIO 5----------------------------------------------------------------------

"""
 Dibujar en la misma ventana grafica las soluciones correspondientes a la ley lineal y′ = −y+t
 en el intervalo [0,20] considerando distintos valores de y(0) entre −10 y 10. Analizar los resultados
"""

y0=np.arange(-10,10,1)
t_span=[0,20]
def f(t, y):
    return -y+t
for i in range (len(y0)):
    sol = solve_ivp(f, t_span, y0, method='RK23', t_eval=np.linspace(0, 12, 100))
    hold on
    plt.plot(sol.t, sol.y[0])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Solución y''= -2y usando RK23')
    plt.grid(True)
    plt.show()


























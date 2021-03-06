# -*- coding: utf-8 -*-
"""trabalho4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpznSlYSlrKrsrE5VGatvD4OKlaMSk42
"""

import numpy as np
from numpy import *
from __future__ import division  
import scipy
import scipy.linalg
import matplotlib.pyplot as plt

"""# **Regra do Trapezio**"""

#Regra do Trapezio Repetida
def trapezio_repetida(a, b, particoes,f):
    h = (b-a)/particoes
    
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
      x = xn + h
      aux = 2*f(x)
      y.append(aux)
      xn =  x
    y.append(f(b))

    resultado = h/2 * sum(y)
   
    return resultado

"""# **Simpson 1/3 e 3/8**"""

#Regra de 1/3 de Simpson Repetida
def simpson1_repetida (a, b, particoes,f):
    h = (b-a)/particoes
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
        x = xn + h
        if ((i+1)%2 == 0):
            aux = 2*f(x)
        else:
            aux = 4*f(x)
        y.append(aux)

    y.append(f(b))
    resultado = h/3 * (sum(y))
    return resultado

#Regra 3/8 de Simpson Repetida
def simpson3_repetida (a, b, particoes,f):
    h = (b-a)/particoes
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
        x = xn + h
        if ((i+1)%3 == 0):
            aux = 2*f(x)
        else:
            aux = 3*f(x)
        y.append(aux)

    y.append(f(b))
    resultado = (3/8)*h * sum(y)
    return resultado

"""#**Euler**"""

#Euler

def euler(x0, h, iteracoes,f):
    y0 = f(x0)
    intervaloX = [x0]
    intervaloY = [y0]
    intervaloYoriginal = [y0]
    
    for i in range (iteracoes):
        x1 = x0 + h
        intervaloX.append(x1)
        y = y0 + h*f(x0)
        intervaloY.append(y)
        intervaloYoriginal.append(f(x1))
        y0 = y
        x0 = x1
   
    plt.plot(intervaloX, intervaloYoriginal)
    plt.plot(intervaloX, intervaloY)
    plt.title("Euler")
    plt.show()
    return y

"""#**Runge Kutta de Segunda e quarta Ordem**"""

#Runge Kutta de Segunda Ordem
def kutta_2ordem(x0, h, N, f):

    
    y0 = f(x0)


    xn = x0
    intervaloX = [x0]
    intervaloY = [y0]
    intervaloYoriginal = [y0]
    yn = y0

    for i in range (N-1):
        xn1 = xn + h
        intervaloX.append(xn1)
        
        k1 = f(xn)
        k2 = f(xn1)
        intervaloYoriginal.append(f(xn1))

        yn1 = yn + (h/2)*(k1+k2)
        intervaloY.append(yn1)
        xn = xn1
        yn = yn1
  
    plt.plot(intervaloX, intervaloYoriginal)
    plt.plot(intervaloX, intervaloY)
    plt.title("Runge Kutta -  Segunda Ordem")
    plt.show()
    return yn1, xn1

#Rugen Kutta de Quarta Ordem
def kutta_4ordem(x0, h, N,f):
    y0 = f(x0)
    xn = x0
    intervaloX = [x0]
    intervaloY = [y0]
    intervaloYoriginal = [y0]
    yn = y0

    for i in range (N-1):
        xn1 = xn + h
        intervaloX.append(xn1)
        k1 = f(xn)
        k2 = f(xn+h/2)
        k3 = f(xn+1/2)
        k4 = f(xn+h)
        yn1 = yn + (h/6) * (k1 + 2*k2 + 2*k3 *k4)
        intervaloY.append(yn1)
        intervaloYoriginal.append(f(xn1))
        xn = xn1
        yn = yn1
    
    plt.plot(intervaloX, intervaloYoriginal)
    plt.plot(intervaloX, intervaloY)
    plt.title("Runge Kutta -  Quarta Ordem")
    plt.show()
    return yn1,xn1

"""#**ERROS**"""

def erro_trapezio(a,b,n,escolha):
    h=(b-a)/n
    temp=h**3
    e=(temp)/12
    g=[]
    aux=a
    i=1
    temp=0
    if escolha==1:

        while(i<=n):
            temp=abs((sp.diff(f(x),x,2).subs(x,aux)))
            g.append(temp)
            aux=aux+h
            i=i+1
    else:
        
        while(i<=n):
            temp=abs((sp.diff(trabalho(x),x,2).subs(x,aux)))
            g.append(temp)
            aux=aux+h
            i=i+1
    #print(g)
    #print(max(g))
    temp=max(g)
    #print (e)
    e=e*temp
    return abs(e)

def erro_simpson13(a,b,n):
    h=(b-a)/n
    e=((h**4)/180)*(b-a)
    g=[]
    aux=a
    i=1
    temp=0
    while(i<=n):
        temp=abs((sp.diff(f(x),x,4).subs(x,aux)))
        g.append(temp)
        aux=aux+h
        i=i+1
    temp=max(g)
    e=e*temp
    return abs(e)

def erro_simpson38(a,b,n):
    h=(b-a)/n
    e=((h**4)/80)*(a-b)
    g=[]
    aux=a
    i=1
    temp=0
    while(i<=n):
        temp=abs((sp.diff(f(x),x,4).subs(x,aux)))
        g.append(temp)
        aux=aux+h
        i=i+1
    temp=max(g)
    e=e*temp
    return abs(e)

"""#**lista 11**"""

a = lambda x: x*math.log(x)
b = lambda x: (pow(x,3))*exp(x)
c = lambda x: 2/((pow(x,2)+4))
d = lambda x: (x**2)*math.cos(x)
e = lambda x: exp(x**2)*sin(3*x)
f = lambda x: x/((pow(x,2)+4))
print("trapezio repetida")
print()
print("resultado para questão a)")
print(trapezio_repetida(1, 2, 4,a))
print("resultado para questão b)")
print (trapezio_repetida(-2, 2, 4,b))
print("resultado para questão c)")
print (trapezio_repetida(0, 2, 6,c))
print("resultado para questão d)")
print(trapezio_repetida(0, 2, 6,d))
print("resultado para questão e)")
print(trapezio_repetida(0, 2, 8,e))
print("resultado para questão f)")
print(trapezio_repetida(1, 3, 8,f))
print()
print("simpson 1/3 repetida")
print()
print("resultado para questão a)")
print(simpson1_repetida(1, 2, 4,a))
print("resultado para questão b)")
print (simpson1_repetida(-2, 2, 4,b))
print("resultado para questão c)")
print (simpson1_repetida(0, 2, 6,c))
print("resultado para questão d)")
print(simpson1_repetida(0, 2, 6,d))
print("resultado para questão e)")
print(simpson1_repetida(0, 2, 8,e))
print("resultado para questão f)")
print(simpson1_repetida(1, 3, 8,f))
print()
print("simpson 1/3 repetida")
print("Para Simpson 3/8 foi apenas realizados os exercicios C) e D) \npor serem os unicos divisives por 3")
print()
print("resultado para questão c)")
print (simpson3_repetida(0, 2, 6,c))
print("resultado para questão d)")
print(simpson3_repetida(0, 2, 6,d))

"""#**lista 12**"""

a = lambda x: 1*(x**2)-1
b = lambda x:-0.06*sqrt(x)
c= lambda x: 2*x*((92-x)/92)
print("resultado para questão 1) ")
r1,y=kutta_2ordem(2, 1, 3,c)

print("resultado: ", r1)
r2,y=kutta_4ordem(2, 1, 3,c)

print("resultado: ", r2)
print()
print("resultado para questão 2)")
r1,y=kutta_2ordem(3, 0.5, 32,b)
print("resultado: ", r1)
print("tempo para esvaziamento tolta ",y )
r2,y=kutta_4ordem(3, 0.5, 60,b)
print("resultado: ", r2)
print("tempo para esvaziamento tolta ",y )
print()
print("resultado para questão 3)")
r=euler(0, 0.5, 4,a)
print("resultado: ", r)
print()
print("resultado para questão 4)")
r,y=kutta_4ordem(0, 0.5, 4,a)
print("resultado: ", r)
# -*- coding: utf-8 -*-
"""Trabalho1CNC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iy7ZttA4wVRFi4F32G4Y-SlpOd9hxegC

# **Funções**
"""

from sympy import *
import math

f =lambda x: 5*(pow(x,5))-2*(pow(x,4))+3*(pow(x,2))-8*x-10
fdx=lambda x:25*(pow(x,4))-8*(pow(x,3))+6*x-8
f1 =lambda x:5*(pow(x,3))-2*(pow(x,2))-8*x-10
f1dx =lambda x: 15*(pow(x,2))-4*x+8
f2 =lambda x:2*((x**3))+5*(x**2)-(sin(x))-30
f2dx =lambda x:  -cos(x)+6*(pow(x,2))+10*x
f3 =lambda x:exp(x**-2)*math.cos(x)
f3dx =lambda x: -exp(x**-2)*sin(x)-2*x*exp(x**-2)*cos(x) 
f4 =lambda x:(x+1)*(x-1)*(x-3)*(x-3)**5
f4dx =lambda x:   5*((x-3)**4)*(x - 1)*(x+1)+((x-3)**5)(x+1)+((x-3)**5)*(x-1)
f5 =lambda x: pow((x+2),3)*sqrt(pow(x,2)+1)
f5dx =lambda x: 3(x+2)^2* sqrt(pow(x,2)+1)+(x*(x+2)**3)/sqrt(pow(x,2)+1)

"""# **Método de Bissecao**"""

def bisseccao (f,a,b,precisao,i):
  interador = 0
  raiz_apr = [] 
  if (f(a)*f(b))<0:
    x=(a+b)/2
    while abs(f(x))>precisao and interador<=i:
      if (f(a)*f(x))<0:
        b=x
      else:
        a=x
      x=(a+b)/2
      interador=interador+1
      
     # print("A raiz do intervalo é ",x)
      raiz_apr.append(x)
      print("Interação ",interador)
  else:
    print("Não a dados no intervalo")

  return raiz_apr

bisseccao (f1,0,2,10**-10,500)

bisseccao (f2,1,4,10**-10,500)

bisseccao (f3,-1,2,10**-10,500)

bisseccao (f4,2,5,10**-10,500)

bisseccao (f5,-3,0,10**-10,500)

"""# **Método da Falsa Posição**"""

def falsepos(f,a,b,precisao,i):
  interador = 0
  raiz_apr = []
  
  if (f(a)*f(b))<0:
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    while (interador<=i and abs(f(x))>precisao and abs(b-a)>precisao ):
      if (f(a)*f(x))<0:
        b=x
      else:
        a=x
        
      x=(a*f(b)-b*f(a))/(f(b)-f(a))
      interador=interador+1
      #print("A raiz do intervalo é ",x)
      raiz_apr.append(x)
      print("Interação ",interador)
  else:
    print("Não a dados no intervalo")
    
  return raiz_apr

falsepos (f1,0,2,10**-10,500)

falsepos (f2,1,4,10**-10,500)

falsepos (f3,-1,2,10**-10,500)

falsepos (f4,2,5,10**-10,500)

falsepos (f5,-3,0,10**-10,500)

"""# **Método da  Tangente**"""

def tangente(f,fdx,x0,precisao,i):
    interador = 0
    raiz_apr = []
    if abs(f(x0))<=precisao:
      raiz_apr.append(x0)
      return raiz_apr
    #print("k\t x0\t\t f(x0)")
    interador=1
    while interador<=i:
      x1=x0-f(x0)/fdx(x0)
      print("%d\t %e\t%e"%(interador,x1,f(x1)))
      if abs(f(x1))<=precisao:
        raiz_apr.append(x1)
        return raiz_apr
      x0=x1
      interador=interador+1
      raiz_apr.append(x1)
    print("Não a dados no intervalo")

tangente (f1,f1dx,2,10**-10,500)

tangente (f2,f2dx,4,0.001,500)

tangente (f3,f3dx,2,0.001,500)

tangente (f4,f4dx,5,0.001,500)

tangente (f5,f5dx,0,0.001,500)

"""# **Método da Secante**"""

def secante(f,x0,x1,p1,p2,i):
    interador = 0
    raiz_apr = []
    if abs(f(x0))<=p1:
      raiz_apr.append(x0)
      return raiz_apr
   # print("k\t f(x0)\t\t f(x1)")
    interador=1
    while interador<=i:
      x2=x1-(f(x1)/(f(x1)-f(x0)))*(x1-x0)
      print("%d\t %e\t%e"%(interador,f(x0),f(x1)))
      if (abs(f(x1))<=p1)or (abs(x1-x0)<=p2):
        raiz_apr.append(x1)
        return raiz_apr
      if (abs(f(x2))<=p1)or (abs(x2-x1)<=p2):
        raiz_apr.append(x2)
        return raiz_apr
      x0=x1
      x1=x2
      interador=interador+1
      raiz_apr.append(x1)
      raiz_apr.append(x2)
    print("Não a dados no intervalo")

secante (f,1.5,2.5,10**-10,0.001,500)

secante (f1,0,2,10**-10,0.001,500)

secante (f2,1,4,10**-10,0.001,500)

secante (f3,-1,2,10**-10,0.001,500)

secante (f4,2,5,10**-10,0.001,500)

secante (f5,-3,0,10**-10,0.001,500)

"""# **Gráfico**"""

import matplotlib.pyplot as plt
import numpy as np
import math



inicio = 0.0
final = 1.0
numero_pontos = 100

curve = np.linspace(inicio,final,numero_pontos+1)

values = [f(value) for value in curve]


raizes_bissecao = bisseccao (f1,0,2,10**-10,500)



x_aproximado = [f(value) for value in raizes_bissecao]


plt.plot(curve, values, linestyle='-')


plt.plot(raizes_bissecao, x_aproximado, 'x', marker='.', label='' + str(len(raizes_bissecao)) + ' iterações' )




i=0
for x,y in zip(raizes_bissecao, x_aproximado):
  i = i+1
  plt.text(x,y,str(i))

leg1 = plt.legend();


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Bisseção')


plt.axhline(0, color = "black")

plt.grid()

plt.show()





raizes_falsepos = falsepos (f1,0,2,10**-10,500)



x_aproximado = [f(value) for value in raizes_falsepos]


plt.plot(curve, values, linestyle='-')


plt.plot(raizes_falsepos, x_aproximado, 'x', marker='.', label='' + str(len(raizes_falsepos)) + ' iterações' )




i=0
for x,y in zip(raizes_falsepos, x_aproximado):
  i = i+1
  plt.text(x,y,str(i))

leg1 = plt.legend();


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Falsa Posição')


plt.axhline(0, color = "black")

plt.grid()

plt.show()




raizes_tangente = tangente (f1,f1dx,2,10**-10,500)


x_aproximado = [f(value) for value in raizes_tangente]


plt.plot(curve, values, linestyle='-')


plt.plot(raizes_tangente, x_aproximado, 'x', marker='.', label='' + str(len(raizes_tangente)) + ' iterações' )




i=0
for x,y in zip(raizes_tangente, x_aproximado):
  i = i+1
  plt.text(x,y,str(i))

leg1 = plt.legend();


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da  Tangente')


plt.axhline(0, color = "black")

plt.grid()

plt.show()

inicio = 0.0
final = 1.0
numero_pontos = 100

curve1 = np.linspace(inicio,final,numero_pontos+1)

values1 = [f(value1) for value1 in curve1]


raizes_bissecao1 = secante (f1,0,2,10**-10,0.001,500)


x_aproximado = [f(value1) for value1 in raizes_bissecao1]


plt.plot(curve1, values1, linestyle='-')


plt.plot(raizes_bissecao1, x_aproximado, 'x', marker='.', label='' + str(len(raizes_bissecao1)) + ' iterações' )




i=0
for x,y in zip(raizes_bissecao1, x_aproximado):
  i = i+1
  plt.text(x,y,str(i))

leg1 = plt.legend();


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Secante')


plt.axhline(0, color = "black")

plt.grid()

plt.show()
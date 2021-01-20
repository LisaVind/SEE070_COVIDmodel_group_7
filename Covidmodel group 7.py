#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:43:52 2021

@author: filipandersson
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

beta = 0.18
#Beta = antal som smittas per infekterad och per tid (beror på virusets egenskaper samt hur vi beter oss)


gamma = 0.1
# Gamma = Antalet personer som blir friska igen per dag

alpha = 0.05
#Alpha = risk att dö för infekterade

#R0 = initiala värdet på smittspridningen.


rho = 1/9
#1/antal dagar det tar för en person att avlida

def getAlpha():
    HospitalMaxCapacity = 150000
    extraMortality = 0.00000001
    if I < HospitalMaxCapacity:
        return alpha
    else:
        return alpha + (I - HospitalMaxCapacity)*extraMortality


# N antalet i befolkningen, Sverige ca 10 miljoner
N = 10 * 10**(6)

#I  – Infekterade just nu
I = 100000

#R – tillfrisknade, eller möjligen också döda personer

R = 523000
#R – tillfrisknade, eller möjligen också döda personer

V = 80000
#Antalet vaccinerade
 
S = N - R - I - V

#S – de som är mottagliga för infektion 

D = 10500
#D antalet döda

lista_R = []
lista_Rt = []
lista_S = []
lista_I = []
lista_V = []
lista_D = []


for t in range(0,150):
    
    V += 5000
    if V >= 10 * 10**(6):
        V = 10 * 10**(6)
    
    lista_V.append(V)
    
    R += I * gamma
    lista_R.append(R)
    
    S += -(beta)* I * (S/N) - 5000
    lista_S.append(S) 
    
    I += (beta * I * S)/N - (I * gamma)
    lista_I.append(I)
    
    D += getAlpha() * rho * I
    lista_D.append(D)

    
plt.figure(1)
plt.plot(lista_S, 'blue')
plt.plot(lista_I, 'red')
plt.plot(lista_R, 'g')
plt.plot(lista_V, 'purple')
plt.plot(lista_D, "black")

pop_a = mpatches.Patch(color='blue', label='Mottagliga för infektion')
pop_b = mpatches.Patch(color='red', label='Infekterade')
pop_c =  mpatches.Patch(color='green', label='Tillfrisknade')
pop_d =  mpatches.Patch(color='black', label='Döda')
pop_e =  mpatches.Patch(color='purple', label='Vaccinerade')

plt.legend(handles=[pop_a,pop_b,pop_c, pop_d,pop_e])


plt.figure(2)
plt.plot(lista_I, 'red')
plt.plot(lista_V, 'purple')
plt.plot(lista_D, "black")



plt.legend(handles=[pop_b, pop_d,pop_e])
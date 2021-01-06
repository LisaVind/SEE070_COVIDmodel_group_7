#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:57:20 2020
@author: LisaVind
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

beta = 1.1

gamma = 0.1

alpha = 0.05
#Alpha = risk att dö för infekterade

rho = 1/9
#1/antal dagar det tar för en person att avlida

def getAlpha():
    HospitalMaxCapacity = 150000
    extraMortality = 0.00000001
    if I < HospitalMaxCapacity:
        return alpha
    else:
        return alpha + (I - HospitalMaxCapacity)*extraMortality


#R0 = initiala värdet på smittspridningen.
#Beta = antal som smittas per infekterad och per tid (beror på virusets egenskaper samt hur vi beter oss)
# Gamma = Antalet personer som blir friska igen per dag

R0 = beta/gamma

# N antalet i befolkningen, Sverige ca 10 miljoner
N = 10 * 10**(6)

#I  – Infekterade just nu
I = 10

# b = effekt av policy och beteendeförändringar 0 < b < 1 
b = 0.25

#R – tillfrisknade, eller möjligen också döda personer, vi måste utgå från data som finns? Sedan lägga till en faktor I * gamma

R = 350000
 
S = N - R - I

D = 0
#S – de som är mottagliga för infektion 

Rt = R0 * (S/N) * (1 - b) 


lista_R = []
lista_Rt = []
lista_S = []
lista_I = []
lista_D = []


for t in range(0,60):
    R += (1 - getAlpha()) * I * gamma
    lista_R.append(R)    
    
    S += (-(beta*I*S))/N 
    lista_S.append(S)
    
    I += (beta * I * S)/N - (1 - getAlpha())*(I * gamma) - getAlpha() * rho * I
    lista_I.append(I)
    
    Rt += R0 * (S/N) * (1 - b) 
    lista_Rt.append(Rt)
    
    D += getAlpha() * rho * I
    lista_D.append(D)
    print(I)
    print(getAlpha())


#R – tillfrisknade, eller möjligen också döda personer, vi måste utgå från data som finns? Sedan lägga till en faktor I * gamma
#S – de som är mottagliga för infektion 
# Rt= R0* S(t)/Ntot* (1 –b) 


plt.plot(lista_S, 'blue')
plt.plot(lista_I, 'red')
plt.plot(lista_R, 'g')
plt.plot(lista_D, "black")

pop_a = mpatches.Patch(color='blue', label='Mottagliga för infektion')
pop_b = mpatches.Patch(color='red', label='Infekterade')
pop_c =  mpatches.Patch(color='green', label='Tillfrisknade')
pop_d =  mpatches.Patch(color='black', label='Döda')

plt.legend(handles=[pop_a,pop_b,pop_c,pop_d])


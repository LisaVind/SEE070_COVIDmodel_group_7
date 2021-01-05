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

#R0 = initiala värdet på smittspridningen.
#Beta = antal som smittas per infekterad och per tid (beror på virusets egenskaper samt hur vi beter oss)
# Gamma = Antalet personer som blir friska igen per dag

R0 = beta/gamma

# N antalet i befolkningen, Sverige ca 10 miljoner
N = 10 * 10**(6)

#I  – Infekterade just nu
I = 10000

# b = effekt av policy och beteendeförändringar 0 < b < 1 
b = 0.25

#R – tillfrisknade, eller möjligen också döda personer, vi måste utgå från data som finns? Sedan lägga till en faktor I * gamma

R = 350000
 
S = N - R - I

#S – de som är mottagliga för infektion 

Rt = R0 * (S/N) * (1 - b) 


lista_R = []
lista_Rt = []
lista_S = []
lista_I = []


for t in range(0,60):
    R += I * gamma
    lista_R.append(R)
    
    
    S += (-(beta*I*S))/N 
    lista_S.append(S)
    
    I += (beta * I * S)/N - (I * gamma)
    lista_I.append(I)
    
    Rt += R0 * (S/N) * (1 - b) 
    lista_Rt.append(Rt)


#R – tillfrisknade, eller möjligen också döda personer, vi måste utgå från data som finns? Sedan lägga till en faktor I * gamma
#S – de som är mottagliga för infektion 
# Rt= R0* S(t)/Ntot* (1 –b) 


plt.plot(lista_S, 'blue')
plt.plot(lista_I, 'red')
plt.plot(lista_R, 'g')

pop_a = mpatches.Patch(color='blue', label='Mottagliga för infektion')
pop_b = mpatches.Patch(color='red', label='Infekterade')
pop_c =  mpatches.Patch(color='green', label='Tillfrisknade')

plt.legend(handles=[pop_a,pop_b,pop_c])



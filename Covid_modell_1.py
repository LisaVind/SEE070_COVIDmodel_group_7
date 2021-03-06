#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:57:20 2020

@author: LisaVind
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

beta = 0.5

gamma = 0.2

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

V = 20000
#Antalet vaccinerade
 
S = N - R - I - V



#S – de som är mottagliga för infektion 

Rt = R0 * (S/N) * (1 - b) 


lista_R = []
lista_Rt = []
lista_S = []
lista_I = []
lista_V = []


for t in range(0,100):
    V += 2000
    
    if V >= 10 * 10**(6):
        V = 10 * 10**(6)
    
    lista_V.append(V)
    
    R += I * gamma + V
    lista_R.append(R)
    
    if R >= 10 * 10**(6):
        R = 10 * 10**(6)
    
    
    S += -(beta)* I * (S/N)
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
plt.plot(lista_V, 'purple')

print(lista_V)
print(lista_R)


pop_a = mpatches.Patch(color='blue', label='Mottagliga för infektion')
pop_b = mpatches.Patch(color='red', label='Infekterade')
pop_c =  mpatches.Patch(color='green', label='Tillfrisknade')
pop_d =  mpatches.Patch(color='purple', label='Vaccinerade')

plt.legend(handles=[pop_a,pop_b,pop_c, pop_d])



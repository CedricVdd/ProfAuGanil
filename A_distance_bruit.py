#!/usr/bin/env pythoN1
# -*- coding: utf-8 -*-
"""
@author: cedric vanden driessche, lycée Charles de Gaulle, CAEN
cedric.vanden-driessche@ac-normandie.fr
"""

import numpy as np
from matplotlib import pyplot as plt
import statistics as stat
from scipy.optimize import curve_fit        #permet de chercher une modélisation

plt.clf()

parametres=[]

incertitude=[]
Nmoyen=[]
distance=[]




fichier='A_d.txt'
data_file = open(fichier,"r")
   
      
distance=np.loadtxt(fichier,usecols=(0,), delimiter='\t')
Nmoyen= np.loadtxt(fichier,usecols=(33,),delimiter='\t')
incertitude= np.loadtxt(fichier,usecols=(34,),delimiter='\t')


plt.figure(dpi=300)

#plt.title('Pulses en fonction de la distance pour le manchon de Camping Gaz')
plt.xlabel("distance d (en cm)")
plt.ylabel("Activité pour 10S")
plt.errorbar(distance,Nmoyen,yerr=incertitude,xerr=0.2,fmt='b-',capsize = 5,ecolor='red',label='A=f(d)')
#plt.plot(distance,Nmoyen,'b+-',label='N=f(d)')

#Définition du modèle que l'on souhaite vérifier
def FonctionModele(distance,a,b):
        return a/distance**2 + b
   
#Calcul du modèle
parametre,covariance= curve_fit(FonctionModele,distance,Nmoyen)

a=parametre[0]
b=parametre[1]



#Tracé du modèle
distanceth=np.linspace(0.5,10,50)
Nth= a/distanceth**2 + b
plt.plot(distanceth, Nth, color = 'green', label = 'Modele', marker = '')
plt.legend()

#affichage de l'équation
plt.text(5,12,'A (d)= {: .1f} / d2 + {: .1f}'.format(a,b))

plt.show()

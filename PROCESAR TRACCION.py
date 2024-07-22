#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Codificaciones posibles: iso-8859-15, utf-8
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%
argumentos = {
'sep' : ';', #separador de datos
'skiprows' : 65,
'decimal' : ',',
'thousands' : None, #separador de mil
'encoding' : 'iso-8859-15' #codificaciones posibles: iso-8859-15, utf-8
    }
# argumentos = {
# 'sep' : ';', #separador de datos
# 'skiprows' : 58,
# 'decimal' : ',',
# 'thousands' : None, #separador de mil
# 'encoding' : 'utf-8' #codificaciones posibles: iso-8859-15, utf-8
#     }
# =============================================================================

from directorios import *

#%% GRAFICAR
# plt.figure(figsize=(6,4.5)) #size = 5.5,4.5
lista = ['ARS3', 'H3', 'H2', 'H1']
# lista = ['H3']
for ens in lista:
    x = ensayos[ens]['Deformación por tracción %'][:-10]
    y = ensayos[ens]['Esfuerzo de tracción MPa'][:-10]
    if ens == 'ARS3': ens = 'AR'
    plt.plot(x, y, label = ens)
    # plt.scatter(x, y, s=1, c='k')
    # plt.plot(x, y, label = 'AR', c='k')
plt.ylabel('Esfuerzo de tracción [MPa]')
plt.xlabel('Deformación porcentual [%]')
plt.legend()
plt.tight_layout()

# plt.xlim([-1, 3])
#%% PROP MECANICAS (requiere x e y de arriba)
###TS
max(y)

###ELONG A FRACTURA
max(x)

###YS
y.iloc[100]
xn = x.iloc[5:77]
yn = y.iloc[5:77]
plt.plot(xn, yn)
def lin(X):
    return np.poly1d(np.polyfit(xn, yn, 1))(X)

#%% a mano
tens = 466
(x.iloc[lin(x).searchsorted(tens)] - x.iloc[y.searchsorted(tens)])


plt.plot(x,y)
plt.plot(x, lin(x))
plt.ylim([-30, 700])
plt.grid()

#%% TEMPORAL

x = ensayos['H3']['Deformación por tracción %'][:-10]
y = ensayos['H3']['Esfuerzo de tracción MPa'][:-10]

x.searchsorted(6.658)
x.searchsorted(7.438)

x.iloc[2529:2829] = None
y.iloc[2529:2829] = None

plt.plot(x,y)


6.658 7.438


#%% MLC
argumentos = {
'sep' : '\t', #separador de datos
'skiprows' : 0,
'decimal' : ',',
'thousands' : None, #separador de mil
'encoding' : 'utf-8' #codificaciones posibles: iso-8859-15, utf-8
    }
#MLCFT1, MLCFT2, MLCFT3, MLCFT6
#A1, A2, B3, MLC


#%%
plt.figure(figsize = (6,4.5))
for ens in ensayos:
    x = ensayos[ens]['Deformación'][:-10]
    y = ensayos[ens]['Esfuerzo'][:-10]
    plt.plot(x, y, label = ens)
plt.ylabel('Esfuerzo de tracción [MPa]')
plt.xlabel('Deformación porcentual [%]')
plt.legend()
plt.grid()
plt.tight_layout()


#%%
nombre = 'traccion MLC'
# plt.savefig('./PROCESAR TRACCION/'+ nombre +'.png', format = 'png', dpi = 100)








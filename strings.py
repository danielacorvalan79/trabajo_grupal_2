import numpy as np

import random
caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1, 20) 
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres) 
    lista.append(string_aleatorio)
print(lista) 

#printlista)

#Punto 2         

#creando una lista vacia
numero_caracteres_lista = []

for i in lista:
    print(i," , ", len(i))
    numero_caracteres_lista.append(len(i))

print(numero_caracteres_lista)

#punto 3

#promedio usando numpy

promedio=np.mean(numero_caracteres_lista)
print("promedios de los string:" ,promedio)

#promedio normal  


suma=0
for i in numero_caracteres_lista:
    suma=suma+i

promedio=suma/len(numero_caracteres_lista)
print(promedio)

#punto 4


entero=int(promedio)
print("parte entera de promedio:" ,entero)


for i in range(len(lista)):
    # print( lista[ i ] )
    palabra=lista[i]
    lista[ i ]=palabra[:entero]
    
print("\n",lista)    

import random
import numpy as np

#punto 5
#generando lista con numeros de 1 a 20 digitos

caracteres = '1234567890'
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(int(string_aleatorio))

print(lista)
#calculando promedio
suma = 0
for elem in lista:
    suma = suma + elem

print("suma: ",suma)
print("numero de elementos: ", len(lista))
promedio = suma/ len(lista)
print("promedio: ", promedio)
print("promedio con numpy: ", np.mean(lista) )
for elem in range(len(lista)):
    lista[elem] = lista[elem]-promedio

print("Lista actualizada: \n",lista)
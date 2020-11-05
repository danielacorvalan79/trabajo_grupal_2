import random
caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)
print(lista)

print(len(lista))
print(type(lista))

#Se crea una lista float con 100 elementos con 3 decimales.
lista_float = []
for i in range(0, 100):
    a = round(random.uniform(10,50), 3)
    lista_float.append(a)

print(lista_float)
print("El número de elementos de la lista float es: ", len(lista_float))
print("La lista float es de tipo: ", type(lista_float))
lista = lista_float

#promedio de los valores de la lista
#suma de valores
suma=0
for i in lista_float:
    suma+=i
print("La suma de todos los valores de la lista aleatoria float es de: ", suma)
#PROMEDIO O MEDIA
media_lista_float = suma/len(lista_float)
print("La media de todos los valores es de: ", media_lista_float)
#VALOR MÁXIMO
print("El valor máximo de la lista aleatoria de flotantes es de ", max(lista_float))
#valor mínimo
print("El valor mínimo de la lista aleatoria de flotantes es de ", min(lista_float))

lista_flotante_normalizada = []

for i in lista_float:
    lista_flotante_normalizada.append((i-media_lista_float)/max(lista_float))
print(lista_flotante_normalizada)

print(len(lista_flotante_normalizada))
print(type(lista_flotante_normalizada))
suma_lista = 0
for i in lista_flotante_normalizada:
    suma_lista=suma_lista+i
print("La última lista suma en total: ", suma_lista)
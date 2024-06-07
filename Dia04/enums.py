lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1
print("\n\n")

for indice, item in enumerate(lista):
    print(indice, item)
print("\n\n")

mis_tuples = list(enumerate(lista))
print(mis_tuples[1])
print(mis_tuples)

print("\n\n")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
nombres = list(enumerate(lista_nombres))
for indice, nombre in nombres:
    print(f'{nombre} se encuentra en el índice {indice}')

print("\n\n")
texto = "Python"
lista_indices = list(enumerate(texto))
print(lista_indices)

print("\n\n")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    inicial = list(enumerate(nombre))[0][1]
    if(inicial == 'M'):
        print(indice)
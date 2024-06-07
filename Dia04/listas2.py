palabra = 'python'

lista = []
for l in palabra:
    lista.append(l)
    print(lista)

print("\n")
lista = [letra for letra in palabra]
print(lista)

print("\n")
lista = [letra for letra in 'python']
print(lista)

print("\n")
lista = [num for num in range(0,21,2)]
print(lista)

print("\n")
lista = [num/2 for num in range(0,21,2)]
print(lista)

print("\n")
lista = [num for num in range(0,21,3) if num%2==0]
print(lista)

print("\n")
lista = [num if num%2==0 else 'no' for num in range(0,21,3)]
print(lista)

print("\n")
pies = [10, 20, 30, 40, 50]
metros = []
metros = [num*3.281 for num in pies]
print(metros)


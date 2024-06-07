minimo = min(58,96,72,64,35)
maximo = max(58,96,72,64,35)
print(minimo, maximo)

print("\n--------------------------------------------------")
lista = [58, 96, 72, 64, 35]
print(lista)
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

print("\n--------------------------------------------------")
nombres = ['Juan', 'Pedro', 'Carlos', 'Zoe']
print(nombres)
print(f"El primero es {min(nombres)} y el último es {max(nombres)}")

print("\n--------------------------------------------------")
nombre = 'Juan'.lower()
print(nombre)
print(f"El primero es {min(nombre)} y el último es {max(nombre)}")

print("\n--------------------------------------------------")
dic = {'C1':45, 'C2':11}
print(dic)
print(f"El primero es {min(dic)} y el último es {max(dic)}")
print(f"El mínimo es {min(dic.values())} y el máximo es {max(dic.values())}")
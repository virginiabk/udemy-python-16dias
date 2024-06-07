print("---------- LOOPS ----------")
nombres = ['Juan', 'Ana', 'Carlos', 'Belén', 'Fran']
for e in nombres:
    print(f"Hola {e}")
    
lista = ['a', 'b', 'c']
for letra in lista:
    numero_letra = lista.index(letra)+1
    print(f"{numero_letra}: {letra}")
    
lista = ["Pablo", "Laura", "Paula", "Luis", "julia"]

for nombre in lista:
    if nombre.startswith("L"):
        print(nombre)

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

for letra in 'Python':
    print(letra)
    
for item in [1, 2, 3, ['a', 'b', 'c'], 4]:    
    if type(item)==list:
        for letra in item:
            print(letra)
    else:
        print(item)
        
# Iteracion en lista  
for a,b in [[1,2], [3,4], [5, 6]]:
    print(f"{a} {b}")
    
# Iteracion en diccionario
dic = {"clave1": "a", "clave2": "b"}
for clave in dic:
    print(clave)
    
dic = {"clave1": "a", "clave2": "b"}
for clave, valor in dic.items():
    print(f"{clave} {valor}")
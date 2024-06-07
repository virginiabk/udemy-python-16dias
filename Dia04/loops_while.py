monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print(f"Me quedé sin monedas\n\n\n")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print("Gracias!\n\n\n")


nombre = input("Nombre (federico): ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

nombre = input("\n\n\nNombre (federico): ")

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
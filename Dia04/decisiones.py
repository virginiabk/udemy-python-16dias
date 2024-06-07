if 10<9:
    print("se cumple")
else:
    print("no se cumple")

mascota = 'foca'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('Tienes otro animal')

edad= 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion>=7:
        print('Has aprobado')
    else:
        print('No has aprobado')
else:
    print('Eres adulto')
    
num1 = int(input("Ingresa un numero:"))
num2 = int(input("Ingresa otro numero:"))

print(f"num1 = {num1}, num2 = {num2}")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"num2 es mayor que num1")
else:
    print(f"num1 y num2 son iguales")
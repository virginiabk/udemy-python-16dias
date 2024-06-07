nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tus ventas: "))
comision = 0.13
ganancia = round(ventas * comision, 2)

print(f"Las ventas de {nombre} fueron ${ventas}. Su ganancia es de ${ganancia}")
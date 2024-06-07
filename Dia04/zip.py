nombres = ['Ana', 'Bruno', 'Carlos']
edades = [23, 34, 65]
residencia = ['Lima', 'Madrid', 'Argentina']

combinados = list(zip(nombres, edades, residencia))
for nombre, edad, residencia in combinados:
    print(f"{nombre} tiene {edad} años y vive en {residencia}")

print("\n\n")
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
info = zip(capitales, paises)
for capital, pais in list(info):
    print(f"La capital de {pais} es {capital}")

print("\n\n")
sp = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
pt = ['um', 'dois', 'três', 'quatro', 'cinco']
en = ['one', 'two', 'three', 'four', 'five']
numeros = list(zip(sp,pt,en))
print(numeros)
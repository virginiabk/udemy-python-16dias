

texto_ingresado = input("Ingresa un texto: ").upper()
letras = []
letras.append(input("Ingresa la primera letra: ").upper())
letras.append(input("Ingresa la segunda letra: ").upper())
letras.append(input("Ingresa la tercera letra: ").upper())
print("")
print(texto_ingresado)
print(letras)
print()
print(f"La letra {letras[0]} aparece {texto_ingresado.count(letras[0])} ")
print(f"La letra {letras[1]} aparece {texto_ingresado.count(letras[1])} ")
print(f"La letra {letras[2]} aparece {texto_ingresado.count(letras[2])} ")

print(f"El texto tiene {len(texto_ingresado.split())} palabras")
print(f"la primera letra es {texto_ingresado[0]} y la ùltima es {texto_ingresado[-1]}")
print(f"Al revés, es: {texto_ingresado[::-1]}")

print(f"\nAparece la palabra PYTHON: {texto_ingresado.find("PYTHON")>0}")
buscar_python = "PYTHON" in texto_ingresado
dic = {True : " ", False: " no "}
print(f"La palabra PYTHON{dic[buscar_python]}se encuentra en el texto ingresado")





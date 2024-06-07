texto = "Este es el texto de Federico"

print(texto.upper())
print(texto[2].upper())
print(texto.lower())
print(texto.split())
print(texto.split("t"))

a = "aprender"
b = "es"
c = "genial"
e = " ".join([a,"Python", b,c])
print(e)

print(texto.find("t"))
print(texto.index("t"))
print(texto.find("z"))
print(texto.index("x "))

print(texto.replace("Federico", "todos"))


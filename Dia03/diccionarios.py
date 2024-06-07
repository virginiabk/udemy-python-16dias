simbolos="[] {}"

cliente = {'nombre':'Vir', 'apellido':'bk', 'edad':39, 'talla':12.4, 'peliculas':['titanic', 'forrest gump', 'amelie']}
print(cliente["nombre"])
print(cliente["peliculas"][1].upper())

cliente["color"] = 'rosa'
print(cliente)

print(cliente.keys())
print(cliente.values())

print(cliente.items())
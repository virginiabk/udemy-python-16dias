lista = [1, 2, 15, 24, 13, 13, 7, 2]

def reducir_lista(lista_numeros):
    lista_numeros.remove(max(lista_numeros))
    resultado = [lista_numeros.remove(num) for num in lista_numeros if lista_numeros.count(num) > 1]
    lista_numeros.sort()
    return lista_numeros


def promedio(lista):
    suma = 0
    items = len(lista)
    for item in lista:
        suma += item
    return suma / items

print(f"Promedio: {promedio(reducir_lista(lista))}")


# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

def lanzar_moneda():

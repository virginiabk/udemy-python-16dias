def saludar_persona():
    # Voy a dar la bienvenida a la persona que ingresa
    print('Hola')


saludar_persona()


def saludar_persona(nombre):
    # Voy a dar la bienvenida a la persona que ingresa mencionando su nombre
    print('Hola ' + str(nombre))


saludar_persona('Juan')


def sumar(num1, num2):
    return num1 + num2


resultado = sumar(3, 4)
print(resultado)


def invertir_palabra(palabra):
    return palabra[::-1].upper()


palabra = 'Python'
print(invertir_palabra(palabra))


def chequea_3_cifras(numero):
    return numero in range(100, 1000)


print(chequea_3_cifras(12))


def chequea_3_cifras(lista):
    lista_3_cifras = []

    for item in lista:
        if item in range(100, 1000):
            lista_3_cifras.append(item)
        else:
            pass
    return lista_3_cifras


print(chequea_3_cifras([2, 34, 665, 45, 734]))


def suma_menores(lista):
    suma = 0
    for item in lista:
        if item in list(range(1, 1000)):
            suma += item
    return suma


lista_numeros = [2, 456, 1234, 4, -2]
print(suma_menores(lista_numeros))


def cantidad_pares(lista):
    listado = [num for num in lista if num % 2 == 0]
    return len(listado)


lista_numeros = [2, 5, 7, 6, 10]
print(cantidad_pares(lista_numeros))

from random import shuffle, randint

# lista inicial
palitos = ['-', '--', '---', '----']


# mezclar palitos
def mezclar(palitos):
    return shuffle(palitos)


# pedirle intento
def probar_suerte():
    mezclar(palitos)
    posicion = 0
    while posicion not in range(1, 5):
        posicion = int(input("Ingresar un número entre el 1 y el 4: "))
    return posicion


# comprobar intento
def chequear_intento(palitos, posicion):
    if palitos[posicion - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te salvaste!")

    print(f'Te tocó {palitos[posicion - 1]}')


chequear_intento(palitos, probar_suerte())

print("\n\n-----------Tirada de dos dados-----------")
def lanzar_dados():
    return ([randint(1, 6), randint(1, 6)])


def evaluar_jugada():
    dados = lanzar_dados()
    suma_dados = dados[0] + dados[1]

    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


evaluar_jugada()
from random import randint

numero_secreto = randint(1,100)

intentos = 0
nro = 0
i = 0
print(f'{numero_secreto} {intentos} {nro}')

while intentos < 8:
    nro = int(input('Ingresa un nùmero: '))
    intentos += 1

    if nro < numero_secreto: print('Tu número es menor al número secreto')
    elif nro > numero_secreto: print('Tu número es mayor al número secreto')
    else:
        print(f"\nGANASTE en el intento {intentos}!!!")
        break

if numero_secreto != nro:
    print(f'\nPerdiste, el nro. secreto era {numero_secreto}')

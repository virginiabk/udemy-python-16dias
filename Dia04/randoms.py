from random import *

aleat = randint(1,10)
print(aleat)

aleat = round(uniform(1,10),2)
print(aleat)

aleat = random()
print(aleat)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleat = choice(colores)
print(aleat)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

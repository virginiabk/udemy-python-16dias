mi_tupla = (1, 2, 3, 4)
t = (5, 5.5, ('a', 'b'), "hola")
print(t[-1])
print(t[2])
print(t[2][1])
print(type(t))

t = (1, 2, 3)
x, y, z = t
print(x, y, z)

t = (1, 2, 3, 1)
print(t.count(1))
print(t.index(1))
print(len(t))
serie = 'N-02'

'''if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
else:
    print('No se encontrò')'''

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case _:
        print('No se encontrò')

cliente = {'nombre' : 'Federico', 'edad' : 45, 'ocupacion' : 'instructor'}
pelicula = {'titulo' : 'Matrix', 'ficha_tecnica' : {'protagonista' : 'keanu reeves', 'director': 'Hermanos Wachowski'}}


elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print(f'>>Cliente {nombre}')
        case {'titulo' : titulo, 'ficha_tecnica' : {'protagonista' : protagonista, 'director': director}}:
            print(f'>>Peli {titulo}')
        case _:
            print('Elemento no reconocido')
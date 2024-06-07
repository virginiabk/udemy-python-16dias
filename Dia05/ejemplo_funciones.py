precios_cafe = [('capuccino', 1.5), ('Expresso', 1.2), ('Mocca', 1.35)]


def cafe_mas_caro(precios_cafe):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(cafe, precio)

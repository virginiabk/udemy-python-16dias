dic = {
    'clave1': 100,
    'clave2': 230}
a = dic.popitem()
print(dic)
print(a)

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(texto)
print(texto.lstrip(',:%_#'))


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

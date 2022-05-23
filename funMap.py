# Sintaxis
# map(función, objeto iterable)

lista = [4,5,8,0,6,9,7]
# programación imperativa
lista2 = []
for i in lista:
    lista2.append(i**2)
print(lista2)

# programación funcional
def cuadrado(numero):
    return numero**2
lista3 = list(map(cuadrado, lista))
print(lista3)

# programación funcional con lambda
lista4 = list(map(lambda numero: numero**2, lista))
print(lista4)

diccionario = {
    2019: False, 
    2020: False, 
    2021: True
    }
lista5 = list(map(lambda valor: not(valor), diccionario.values()))
print(lista5)
diccionario2 = dict(zip(diccionario.keys(),list(map(lambda valor: not(valor), diccionario.values())) ))
print(diccionario2)

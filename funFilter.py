# sintaxis
# filter(funcion, objeto iterable)
# la función debe retornar un valor booleano obligatoriamente

lista = [8,5,3,40,22,7,9]

lista2 = tuple(filter(lambda numero: numero%2 == 0, lista))
print(lista2)

lista3 = ['Marina','Cristian','Alex','Andrés','Carolina']
lista4 = list(filter(lambda nombre: nombre[0]=='A', lista3))
print(lista4)

diccionario = {
    'A': 5,
    'B':10,
    'C':8,
    'D':4,
    'E':9
}
# crear un nuevo diccionario con las llaves cuyo valor sea mayor a cinco

diccionario2 = dict(filter(lambda x: x[1]>5, diccionario.items()))
print(diccionario2)

# crear un nuevo dicccionario con filtro de los vendendores A,B y D con ventas mayores a cinco
#diccionario3 = dict(filter(lambda x: x[0]=='A' or x[0]=='B' or x[0]=='D',diccionario.items()))
#print(diccionario3)
diccionario4 = dict(filter(lambda y: y[1]>5,dict(filter(lambda x: x[0]=='A' or x[0]=='B' or x[0]=='D',diccionario.items())).items()))
print(diccionario4)
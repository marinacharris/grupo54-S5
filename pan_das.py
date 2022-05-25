import pandas as pd
import numpy as np
# Series
ciudades = ['Cali','Barranquilla', 'Bucaramanga','Bogotá']
A = pd.Series(ciudades)
print(ciudades) 
print(A)
print(A[1])
diccionario = {
    'enero': 50000000,
    'febrero': 150000000,
    'marzo': 60000000
}
B = pd.Series(data = diccionario,index = list(diccionario.keys()) )
print(B)
print(B['febrero'])
print(B[1])

#DataFrame a partir de un diccionario
inventario = {
    'Impresoras': ['Hp', 'Canon', 'Epson'],
    'Cantidad': [50, 40, 80]
}

InventarioDF = pd.DataFrame(inventario)
print(InventarioDF)
# Data Frame a partir de un diccionarioque contiene una serie
diccionario2 = {
    'columna1': [20,80,41,10],
    'columna2': pd.Series(ciudades)
}
DF1 = pd.DataFrame(diccionario2)
print(DF1)
# Data frame a partir de una array numpy
arreglo = np.array([[4,8,9],[8,8,8],[3,8,5]])

DF2 = pd.DataFrame(arreglo, columns = ['Vainilla','Chocolate','Fresa'], index = ['Lunes', 'Martes','Miércoles'])
print(DF2)
# metodo loc
print(DF2.loc['Lunes'])
print(DF2.loc[['Lunes','Martes']])
#print(DF2.loc[0]) No se puede con el indice numérico
# método iloc
print(DF2.iloc[-1])
print(DF2.iloc[[0,2]])
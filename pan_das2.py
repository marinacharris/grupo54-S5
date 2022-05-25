import pandas

inventario = {
    'Impresoras': ['Hp', 'Canon', 'Epson'],
    'Cantidad': [50, 40, 80]
}

InventarioDF = pandas.DataFrame(inventario)
print(InventarioDF)

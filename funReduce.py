#Sintaxis:
# reduce(funcion, objeto iterable)
# la función debe tener dos parámetros obligatios, uno que actúe como acumulador 
# y otro quer actúe como elemeto. 
from functools import reduce
lista = [4,5,8,9]
# forma imperativa
acumulador = 0
for i in lista:
    acumulador +=i
print(acumulador)

# forma funcional
#For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
resultado = reduce(lambda acumulador, numero: acumulador + numero, lista,40)
print(resultado)
#resultado = reduce(lambda acumulador, numero: acumulador + numero**2, lista)
#print(resultado)
# (((4+5^2)+8^2)+9^2)




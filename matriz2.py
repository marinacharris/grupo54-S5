import numpy as np

a = np.array([[1,2],[3,2]])
b = np.array([[3,4],[7,8]])

print(a+b)
print(np.add(a,b))

print(a*b)
print(np.multiply(a,b))

#Matriz de solo ceros
a = np.zeros((3,3,3))
print(a)

#Matriz de solo unos
print(np.ones((2,2)), '\n')

#Matriz identidad, matriz cuadrada, que tiene una diagonal de unos 
print(np.eye(5), '\n')

#matriz de numeros aleatorios
print(np.random.random((2,2)))
print(np.random.randint(0,10, size=(3,3)))

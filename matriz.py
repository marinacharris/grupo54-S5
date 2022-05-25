import numpy as np

arreglo1 = np.array([1,5,5], dtype=np.int8)
print(arreglo1, type(arreglo1), arreglo1.shape, arreglo1[1],type(arreglo1[1]),'\n')

arreglo2 = np.array([[4,8,9],[8,8,8]])
print(arreglo2, type(arreglo2), arreglo2.shape, arreglo2[0,2], '\n')

arreglo3 = np.array([[[2,3,4,6],[1,4,2,1]],[[5,6,3,41],[1,7,0,2]],[[4,5,6,1],[3,3,3,0]]])
print(arreglo3, arreglo3.shape)
print(arreglo3[1,0,3])
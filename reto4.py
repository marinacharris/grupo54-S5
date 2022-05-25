def ordenes(rutinaContable):
    from functools import reduce
    ListaTotales = list(map(lambda x: [x[0]]+ list(map(lambda z: z[1]*z[2]  ,x[1:])),rutinaContable))
    ListaTotales = list(map(lambda x: [x[0]]+[reduce(lambda a,e:round(a+e,2),x[1:])],ListaTotales))
    print(ListaTotales)
    ListaTotales = list(map(lambda x: x if x[1]>=600000 else [x[0], x[1]+25000],ListaTotales))
     
    print(ListaTotales)
 
    print('------------------------ Inicio Registro diario ---------------------------------')

    print('-------------------------- Fin Registro diario ---------------------------------')
    

rutinaContable = [  
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]  
] 

ordenes(rutinaContable)
## SECCION FUNCION FILTER
# -- Ejemplo -> obtener los numeros impares de la lista "my_list"

from cProfile import label
from functools import reduce
from unicodedata import numeric


my_list = [1,4,5,6,9,13,19,21]

# Funcion Filter
odd_1 = list(filter(lambda x: x%2 != 0, my_list))
print(odd_1)

# Utilizando List Comprehensions
odd_2 = [i for i in my_list if i%2!=0]
print(odd_2)

## SECCION FUNCION MAP
# -- Ejemplo -> obtener una lista donde sus elementos sean el cuadrado de los elementos de la lista "numeros"

numeros = [1,2,3,4,5]

# Utilizando List comprehensions
square_1 = [i**2 for i in numeros]
print(square_1)

# Utilizando un ciclo for
square_2 = []
for i in numeros:
    operacion = i**2
    square_2.append(operacion)
print(square_2)

# Funcion Map
square_3 = list(map(lambda x: x**2, numeros))
print(square_3)


## SECCION FUNCION REDUCE
# -- Ejemplo -> Obtener la multiplicacion de todos los elementos de la lista "base"

base = [2,2,2,2,2]

# Utilizando un ciclo for
resultado_1 = 1
for i in base:
    resultado_1 = resultado_1 * i
print(resultado_1)

# Funcion Reduce
from functools import reduce

resultado_2 = reduce(lambda a, b: a*b, base)
print(resultado_2)
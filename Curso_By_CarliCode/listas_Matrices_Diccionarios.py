# 1. Doble de los Números. 
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista 
# que contenga el doble de cada número usando una List Comprehension.

list1 = [1, 2, 3, 4, 5]
list1_1 = [x*2 for x in list1]
print(list1_1)


# 2. Filtrar y Transformar en un Solo Paso. 
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] 
# y quieres obtener una nueva lista con las palabras que tengan más de 3 letras 
# y estén en mayúsculas.

list2 = ["sol", "mar", "montaña", "rio", "estrella"]
list2_1 = [x.upper() for x in list2 if len(x) > 3]
print(list2_1)


# 3. Crear un Diccionario con List Comprehension.
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y 
# otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas 
# listas usando una List Comprehension.

lista3_a = ["nombre", "edad", "ocupación"]
lista3_b = ["Juan", 30, "Ingeniero"]
dic = {lista3_a[i]:lista3_b[i] for i in range(len(lista3_a))}
print(dic)


# 4. Anidación de List Comprehensions
# Dada una lista de listas (una matriz): 
# matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrizT = [[f[i] for f in matriz] for i in range(len(matriz[0]))]
print(matrizT)


# 5. Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:
# personas = [
#    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
# ]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

personasMadrid = [p["nombre"] for p in personas if p["ciudad"]=="Madrid" and p["edad"] > 30]
print(personasMadrid)


# 6. List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista 
# multiplicando por 2 los números pares y dejando los impares como están.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = [n*2 if n%2 == 0 else n for n in numeros]
print(resultado)
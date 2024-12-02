# Iteradores y Generadores

# Reto Numeros pare e impares

def numbersParImpar(limite, caso):
    """"Generador de numeros pares y impares"""
    i = []
    if caso == 'impar':
        i = range(1, limite + 1, 2)
        for num in i:
            yield num    
    elif caso == 'par':
        i = range(0, limite + 1, 2)
        for num in i:
            yield num
    else:
        print('Opcion invalida')

# Iteradores
print("""
    -------------
    numeros impares
    -------------""")
for i in numbersParImpar(10, 'impar'):
    print(i)

print("""
    -------------
    numeros pares
    -------------""")

for i in numbersParImpar(10, 'par'):
    print(i)
def run():
    lista = []
    for i in range(0,101):
        resultado = i**2
        if resultado % 3 != 0:
            lista.append(resultado)
        else:
            continue

    lista2 = [i**2 for i in range(0,101) if i%3 != 0]
    return lista,lista2   

if __name__ == '__main__':
    print(run()[0])
    print(run()[1])
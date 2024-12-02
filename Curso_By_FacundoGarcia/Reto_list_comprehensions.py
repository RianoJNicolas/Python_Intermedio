def run():
    lista1 = [i for i in  range (1,500) if i%4==0 & i%6==0 & i%9==0]
    lista = [i for i in  range (1,500) if i%4==0 or i%6==0 or i%9==0]
    print("resultado lista1", lista1)
    print("resultado lista", lista)


if __name__ == '__main__':
    run()
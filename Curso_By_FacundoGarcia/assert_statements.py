def divisors(num):      
    try:
        assert num>=0, "Debes ingresar un número positivo"
        if num == 0:
            raise ValueError("Debes ingresar un número mayor a cero")
        else:
            divisores = [i for i in range(1,num+1) if num%i == 0]
    except ValueError as ve:
        print(ve)
        divisores = False
    
    return divisores


def run():
    num = input("Ingresa un número: ")
    print(divisors(int(num)))
    
if __name__ == '__main__':
    run()
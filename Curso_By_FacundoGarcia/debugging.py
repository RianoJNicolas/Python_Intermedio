def divisors(num):      
    try:
        if num < 0:
            raise ValueError("Debes ingresar un número positivo")
        elif num == 0:
            raise ValueError("Debes ingresar un número mayor a cero")
        else:
            divisores = [i for i in range(1,num+1) if num%i == 0]
    except ValueError as ve:
        print(ve)
        divisores = False
    
    return divisores


def run():
    try:
        num = int(input("Ingresa un número: "))            
        print(divisors(num))
    except ValueError:
        print("Debes ingresar un número")

if __name__ == '__main__':
    run()
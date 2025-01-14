## Clases para simular un concesionario de carros

## Clase Carro - Estado avaliable True o False es visible en el concesionario
class Carro:
    def __init__(self, marca, modelo, color, motor):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.avalaible = True
    
    def soldCar(self):
        if self.avalaible:
            self.avalaible = False
            print(f"El carro {self.marca} {self.modelo} ha sido vendido")
        else:
            print(f"El carro {self.marca} {self.modelo} aún está disponible")

    def boughtCar(self):
        self.avalaible = True
        print(f"El carro {self.marca} {self.modelo} ha sido comprado")

## Clase Cliente -
class Cliente:
    def __init__(self, nombre, apellido, email, telefono, direccion, cliente_id):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.cliente_id = cliente_id
        self.bought_cars = []
    
    def buyCar(self, carro):
        if carro.avalaible: 
            carro.soldCar()
            self.bought_cars.append(carro)
        else:
            print(f"El carro {carro.marca} modelo {carro.modelo} no está disponible en el concesionario")
    
    def showCars(self):
        print(f"Carros disponibles de {self.nombre} son: ")
        for carro in self.bought_cars:
            print(f"{carro.marca} modelo {carro.modelo} de color {carro.color}")
        
## Clase Vendedor -
class Vendedor:
    def __init__(self, nombre, apellido, email, telefono, vendedor_id):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.vendedor_id = vendedor_id

    def sellCar(self, carro, cliente, fecha, precio):
        if carro.avalaible:


class Venta:
    def __init__(self, venta_id, carro, cliente, vendedor, fecha, precio):
        self.venta_id = venta_id
        self.carro = carro
        self.cliente = cliente
        self.vendedor = vendedor
        self.fecha = fecha
        self.precio = precio

class Concesionario:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carros = []
        self.clientes = []
        self.vendedores = []
        self.ventas = []

    def agregar_carro(self, carro):
        self.carros.append(carro)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)

    def registrar_venta(self, venta):
        self.ventas.append(venta)
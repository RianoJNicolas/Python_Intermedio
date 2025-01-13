## Clases para simular un concesionario de carros

class Carro:
    def __init__(self, marca, modelo, color, potencia):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.potencia = potencia

class Cliente:
    def __init__(self, nombre, apellido, email, telefono, direccion, cliente_id):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.cliente_id = cliente_id

class Vendedor:
    def __init__(self, nombre, apellido, email, telefono, vendedor_id):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.vendedor_id = vendedor_id

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
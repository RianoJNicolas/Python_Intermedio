class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no está disponible")
    
    def check_available(self):
        return self.available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

class Car(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del carro {self.brand} está en funcionamiento"
        else:
            return f"El carro {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.available:
            return f"El motor del coche {self.brand} está apagado"
        else:
            return f"El carro {self.brand} no está disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"El bicicleta {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.available:
            return f"La bicicleta {self.brand} se ha detenido" 
        else:
            return f"La bicicleta {self.brand} no está disponible"


class Truck(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del camión {self.brand} está en funcionamiento"
        else:
            return f"El camión {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.available:
            return f"El motor del camión {self.brand} está apagado"
        else:
            return f"El camión {self.brand} no está disponible"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, el vehículo {vehicle.brand} no está disponible")

    def info_vehicles(self, vehicle: Vehicle):
        if vehicle.check_available():
            available = "Disponible"
        else:
            available = "No disponible"
        
        print(f"El vehículo {vehicle.brand} está {available} y cuesta {vehicle.get_price()}")


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"Se ha añadido el vehículo {vehicle.brand} a la oficina")
    
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"Se ha registrado el cliente {customer.name} a la oficina")
    
    def show_inventory(self):
        print("Los vehículos disponibles en la oficina son:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"{vehicle.brand} {vehicle.model} por un precio de {vehicle.price}")


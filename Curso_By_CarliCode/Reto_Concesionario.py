## Class for cars
class cars:
    def __init__(self, name, brand, model, price, color):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El carro {self.name} ha sido vendido")
        else:
            print(f"El carro {self.name} no esta disponible")

## Class for client
class client:
    def __init__(self, name, lastname, email, phone, address, c_id):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address
        self.c_id = c_id
        self.own_cars = []
    
    def buy_car(self, car):
        if car.available:
            car.sell()
            self.own_cars.append(car)
            print(f"El carro {car.name} fue comprado por {self.name} {self.lastname}")
        else:
            print(f"El carro {car.name} no esta disponible")
    
    def show_own_cars(self):
        print(f"Los carros comprados por {self.name} {self.lastname} son:")
        for car in self.own_cars:
            print(f"{car.name} modelo {car.model}")

## Class for salesPerson
class salesPerson:
    def __init__(self, name, lastname, email, phone, s_id):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.s_id = s_id
        self.selled_cars = []
    
    def sell_car(self, car, client, dealership):
        if car.available:
            print(f"El carro {car.name} fue vendido por {self.name} {self.lastname}")
            client.buy_car(car)
            dealership.remove_stock_car(car)
            self.selled_cars.append(car)
        else:
            print(f"El carro {car.name} no esta disponible")

    def show_selled_cars(self):
        print(f"Los carros vendidos por {self.name} {self.lastname} son:")
        for car in self.selled_cars:
            print(f"{car.name} modelo {car.model} color {car.color} por un precio de {car.price}")

## Class for dealership
class dealership:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.salespersons = []
        self.clients = []
        self.stock_cars = []
    
    # Method for registar a salesperson
    def register_salesperson(self, salesperson):
        self.salespersons.append(salesperson)
        print(f"El vendedor {salesperson.name} {salesperson.lastname} ha sido registrado en el concesionario")
    
    # Method for registar a client
    def register_client(self, client):
        self.clients.append(client)
        print(f"El cliente {client.name} {client.lastname} ha sido registrado en el concesionario")
    
    # Method for add a car to stock
    def add_stock_car(self, car):
        self.stock_cars.append(car)
        print(f"El carro {car.name} ha sido agregado al stock del concesionario")

    # Method for remove a car from stock
    def remove_stock_car(self, car):
        self.stock_cars.remove(car)
    
    # Method for show stock cars
    def show_stock_cars(self):
        print(f"Los carros en stock del concesionario son:")
        for car in self.stock_cars:
            print(f"{car.name} modelo {car.model} color {car.color} y su precio es {car.price}")
        print("\n")


# Start of the program

# Create cars
car1 = cars("Alfa Romeo", "Alfa Romeo", "Giulietta", "10000", "Blanco")
car2 = cars("Audi", "Audi", "A4", "15000", "Negro")
car3 = cars("BMW", "BMW", "X5", "20000", "Blanco")
car4 = cars("Mercedes", "Mercedes", "C63", "25000", "Blanco")
car5 = cars("Volkswagen", "Volkswagen", "Passat", "30000", "Blanco")
car6 = cars("Ford", "Ford", "Mustang", "35000", "Blanco")

# Create salespersons
salesperson1 = salesPerson("Juan", "Perez", "juanperez@gmail.com", "123456789", "1")
salesperson2 = salesPerson("Maria", "suarez", "mariasuarez@gmail.com", "123456789", "2")
salesperson3 = salesPerson("Pedro", "Rodriguez", "pedrorodriguez@gmail.com", "123456789", "3")

# Create Clients
client1 = client("Daniel", "Contreras", "danielcontreras@gmail.com", "123456789", "Calle de la casa 1", "1")
client2 = client("Maria", "Montoya", "mariamontoya@gmail.com", "123456789", "Calle de la casa 2", "2")

# Create dealership
dealership = dealership("Concesionario", "Calle de la casa 3")

# Registar salespersons
dealership.register_salesperson(salesperson1)
dealership.register_salesperson(salesperson2)
dealership.register_salesperson(salesperson3)

# Registar clients
dealership.register_client(client1)
dealership.register_client(client2)

# Add stock cars
dealership.add_stock_car(car1)
dealership.add_stock_car(car2)
dealership.add_stock_car(car3)
dealership.add_stock_car(car4)
dealership.add_stock_car(car5)
dealership.add_stock_car(car6)

# Show stock cars
dealership.show_stock_cars()

# Sell car1 to client1
salesperson1.sell_car(car1, client1, dealership)
# Show selled cars by salesperson1
salesperson1.show_selled_cars()
# Show bought cars by client1
client1.show_own_cars()
# Show stock cars
dealership.show_stock_cars()

# Sell car2 to client2
salesperson2.sell_car(car2, client2, dealership)
# Show selled cars by salesperson2
salesperson2.show_selled_cars()
# Show bought cars by client2
client2.show_own_cars()
# Show stock cars
dealership.show_stock_cars()

# Sell car3 to client1
salesperson1.sell_car(car3, client2, dealership)
# Show selled cars by salesperson1
salesperson1.show_selled_cars()
# Show bought cars by client1
client1.show_own_cars()
# Show stock cars
dealership.show_stock_cars()

# Sell a car1 to a client2
salesperson1.sell_car(car1, client2, dealership)
# Show selled cars by salesperson1 and salesperson2
salesperson1.show_selled_cars()
salesperson2.show_selled_cars()
# Show bought cars by client1
client1.show_own_cars()
# Show stock cars
dealership.show_stock_cars()
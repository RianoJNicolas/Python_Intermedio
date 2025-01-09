class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Depositado {amount} a la cuenta de {self.account_holder}")
            print(f"Saldo actual: {self.balance}")
        else:
            print("La cuenta no esta activa")

    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Retirado {amount} de la cuenta de {self.account_holder}")
                print(f"Saldo actual: {self.balance}")
            else:
                print("No hay suficiente saldo")

    def deactivate(self):
        self.is_active = False
        print(f"La cuenta de {self.account_holder} ha sido desactivada")
    
    def activate(self):
        self.is_active = True
        print(f"La cuenta de {self.account_holder} ha sido activada")

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Juan", 1000)

# Llamada a los metodos
account1.deposit(200)
account2.deposit(100)
account1.deactivate()
account1.deposit(50)
account1.activate()
account1.deposit(50)

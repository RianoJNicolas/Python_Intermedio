class Person:
    ## Constructor
    def __init__(self, name, age):
        ## Propiedad = parametro
        self.name = name
        self.age = age

    def greet (self):
        print(f"Hola, mi nombre es {self.name} y tengo {str(self.age)} años.")


## Ejemplo de uso
person1 = Person("Carli", 25)
person2 = Person("Facundo", 30)

person1.greet()
person2.greet()
    
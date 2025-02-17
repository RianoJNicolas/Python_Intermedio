class Person:
    # Constructor SuperClass
    def __init__(self, name, age):
        # Attributes of the SuperClass
        self.name = name
        self.age = age

    # Method of the SuperClass
    def greet(self):
        print("Hello! I am a person")

class Student(Person):
    # Constructor SubClass
    def __init__(self, name, age, student_id):
        # Atributes of the SubClass
        # Call the constructor of the parent class
        super().__init__(name, age)
        # Attributes of the SubClass
        self.student_id = student_id
    
    # Method of the SubClass
    def greet(self):
        # Call the method of the parent class
        super().greet()
        # Print the message
        print(f"Hello, my student ID is {self.student_id}")

student = Student("John", 20, "12345")
student.greet()
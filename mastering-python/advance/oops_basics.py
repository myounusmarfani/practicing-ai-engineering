class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.greet())

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "The engine has started."

    def stop_engine(self):
        return "The engine has stopped."

    def honk(self):
        return "Beep beep!"

    def is_classic(self):
        return self.year < 1990


car1 = Car("Toyota", "Camry", 2020)
print(car1.get_info())
print(car1.start_engine())
print(car1.honk())
print(car1.is_classic())
print(car1.stop_engine())
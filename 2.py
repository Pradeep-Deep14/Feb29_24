class Vehicle:
    def printConsumation(self):
        print('low')

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def printConsumation(self):
        print('high')

car = Car()
car.printConsumation()

truck=Truck()
truck.printConsumation()
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class PetrolCar(Car):
    def start(self):
        print("Petrol engine started")

    def stop(self):
        print("Petrol engine stopped")


class ElectricCar(Car):
    def start(self):
        print("Electric motor started")

    def stop(self):
        print("Electric motor stopped")


# User only knows start() and stop()
p = PetrolCar()
p.start()  # Petrol engine started
p.stop()  # Petrol engine stopped

e = ElectricCar()
e.start()  # Electric motor started
e.stop()  # Electric motor stopped

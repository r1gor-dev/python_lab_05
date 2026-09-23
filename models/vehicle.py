from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @abstractmethod
    def move(self):
        pass

    @speed.setter
    def speed(self, value):
        if value <0:
            raise ValueError("Не по законам физики.")
        self._speed = value
    


    def accelerate(self, value):
        self.speed += value  # без _, значит используем setter

    def brake(self, value):
        speed_new = self.speed - value
        self.speed = max(0,speed_new)

    def stop(self):
        self._speed = 0
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) года."
    
    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}) года."
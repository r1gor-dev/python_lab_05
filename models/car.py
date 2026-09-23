from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,brand,model,year,doors):
        super().__init__(brand,model,year)
        self.doors=doors

    def move(self):
        print("По дороге едет машина", self.brand)

    def get_info(self):
        return f"{super().get_info()} Кол-во дверей: {self.doors}"

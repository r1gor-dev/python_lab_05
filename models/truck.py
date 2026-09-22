from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self,brand,model,year, max_load):
        super().__init__(brand,model,year)
        self.max_load=max_load

    def get_info(self):
        return f"{super().get_info()} Грузы до {self.max_load}т"

class Truck(Vehicle):
    def __init__(self,brand,model,year, has_sidecar):
        super().__init__(brand,model,year)
        self.has_sidecar=has_sidecar

    def get_info(self):
        sidecarout = "Да" if self.has_sidecar else "Нет"
        return f"{super().get_info()} Коляска: {sidecarout}"
    

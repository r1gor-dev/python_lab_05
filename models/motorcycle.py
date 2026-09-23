from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year, has_sidecar):
        super().__init__(brand,model,year)
        self.has_sidecar=has_sidecar

    def move(self):
        print("По дороге едет мотоцикл", self.brand)

    def get_info(self):
        sidecarout = "Да" if self.has_sidecar else "Нет"
        return f"{super().get_info()} Коляска: {sidecarout}"
from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self,brand,model,year,battery,autopilot):
        super().__init__(brand,model,year)
        self.battery = battery
        self.autopilot = autopilot

    def get_info(self):
        checkap = "Есть" if self.autopilot else "Нет"
        return f"{super().get_info()} Батарея: {self.battery} квт*ч, Автопилот: {checkap}"
    
    def move(self):
        print(f"По дороге едет электрокар {self.brand}")
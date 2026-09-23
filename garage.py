class Garage:
    def __init__(self):
        self.vehicles=[]
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self):
        print("\nТранспорт в гараже:")
        for x in self.vehicles:
            print(x.get_info())

    def find_by_brand(self,brand):
        print(f"\nПоиск '{brand}'...")
        for x in self.vehicles:
            if x.brand.lower() == brand.lower():
                print(x.get_info())
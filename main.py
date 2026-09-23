#from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from models.electric_car import ElectricCar
from garage import Garage

def main():
    car = Car("Lada", "Priora", 2000, 4)
    truck = Truck("MAN", "CO", 2019, 20)
    motik = Motorcycle("Yamaha", "R1", 2021, False)
    tesla = ElectricCar("Tesla", "Model X", 2023, 100, True)

    mygarage = Garage()
    mygarage.add_vehicle(car)
    mygarage.add_vehicle(truck)
    mygarage.add_vehicle(motik)
    mygarage.add_vehicle(tesla)

    mygarage.show_all()
    mygarage.find_by_brand("MAN")

if __name__ == "__main__":
    main()


# vehicles = [car,truck,motik]

# for x in vehicles:
#     print(x.get_info())
#     x.move()

# my_summer_car = Car("Honda", "Civic", 2016, 5)
# my_summer_car.accelerate(100)
# print(my_summer_car.get_info())
# print(my_summer_car)


# try:
#     m1 = Vehicle("Lada", "Priora", 2000)
# except TypeError as te:
#     print("Ошибка", te)
# m1.accelerate(40)
# print(m1)
# print(m1.speed)
# try:
#     m1.speed =-10
# except ValueError as ve:
#     print(f"Ошибка {ve}")



# # print(m1.get_info())

# # print("Скорость:", m1._speed)

# # m1.brake(20)
# # print("Скорость:", m1._speed)

# # m1.brake(50)
# # print("Скорость:", m1._speed)

# # m1.stop()
# # print("Скорость:", m1._speed)
# #m2 = Vehicle("Toyota", "Corolla", 2015)
# #print(m1.brand,m1.model,m1.year,m1._speed)
# #print(m2.brand,m2.model,m2.year,m2._speed)
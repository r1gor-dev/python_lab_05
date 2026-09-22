from models.vehicle import Vehicle
from models.car import Car

my_summer_car = Car("Honda", "Civic", 2016, 5)
my_summer_car.accelerate(100)
print(my_summer_car.get_info())
print(my_summer_car)

m1 = Vehicle("Lada", "Priora", 2000)
m1.accelerate(40)
print(m1)
print(m1.speed)
try:
    m1.speed =-10
except ValueError as ve:
    print(f"Ошибка {ve}")



# print(m1.get_info())

# print("Скорость:", m1._speed)

# m1.brake(20)
# print("Скорость:", m1._speed)

# m1.brake(50)
# print("Скорость:", m1._speed)

# m1.stop()
# print("Скорость:", m1._speed)
#m2 = Vehicle("Toyota", "Corolla", 2015)
#print(m1.brand,m1.model,m1.year,m1._speed)
#print(m2.brand,m2.model,m2.year,m2._speed)
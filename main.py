from models.vehicle import Vehicle

m1 = Vehicle("Lada", "Priora", 2000)
print(m1.get_info())

m1.accelerate(60)
print("Скорость:", m1._speed)

m1.brake(20)
print("Скорость:", m1._speed)

m1.brake(50)
print("Скорость:", m1._speed)

m1.stop()
print("Скорость:", m1._speed)
#m2 = Vehicle("Toyota", "Corolla", 2015)
#print(m1.brand,m1.model,m1.year,m1._speed)
#print(m2.brand,m2.model,m2.year,m2._speed)
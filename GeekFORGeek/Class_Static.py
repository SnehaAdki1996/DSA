class Car:
    wheels = 4
    def __init__(self):
        self.mil = 8



print(Car.wheels)
c1 = Car()
c2 = Car()
print(c1.wheels,c1.mil)
print(c2.wheels,c2.mil)

c1.wheels = 8
print("when c1 update the static variable")
print(c1.wheels,c1.mil)
print(c2.wheels,c2.mil)
print(Car.wheels)



Car.wheels = 10
print("Via Class  update the static variable")
print(c1.wheels,c1.mil)
print(c2.wheels,c2.mil)
print(Car.wheels)
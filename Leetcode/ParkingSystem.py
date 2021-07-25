class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big = self.big - 1
                return True
            else:
                return False

        if carType == 2:
            if self.medium > 0:
                self.medium = self.medium - 1
                return True
            else:
                return False

        if carType == 3:
            if self.small > 0:
                self.small = self.small - 1
                return True
            else:
                return False

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = ParkingSystem(2, 2, 3)

print(emp1.addCar(3))
print(emp1.addCar(3))
print(emp1.addCar(3))
print(emp1.addCar(1))
print(emp1.addCar(1))
print(emp1.addCar(1))
print(emp1.addCar(1))

stone = "Malahit"
for x in stone:
    print(x)

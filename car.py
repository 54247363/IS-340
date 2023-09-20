class Car:

    def __init__(self, year, make, speed):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed +=5

    def brake(self):
        self.__speed-=5

    def get_speed(self):
        print("current speed is: %s" %(self.__speed))

    def description(self):
        print("Year: %s, Model: %s, Current Speed: %s." % (self.__year_model, self.__make, self.__speed))

Car_object =Car("2010", "BMW", 0)

Car_object.description()

print("Acceleration")
Car_object.accelerate()
Car_object.get_speed()
Car_object.accelerate()
Car_object.get_speed()
Car_object.accelerate()
Car_object.get_speed()
Car_object.accelerate()
Car_object.get_speed()
Car_object.accelerate()
Car_object.get_speed()
print("Brake")
Car_object.brake()
Car_object.get_speed()
Car_object.brake()
Car_object.get_speed()
Car_object.brake()
Car_object.get_speed()
Car_object.brake()
Car_object.get_speed()
Car_object.brake()
Car_object.get_speed()



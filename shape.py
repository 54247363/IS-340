import math

class shape:
    def __init__(self, color):
        self.color = color

    # suppose we also have many methods/attributes
    #....
    def  do_something(self):
        print(f'a {self.color} task, hundred lines of code')

class Circle(shape):
    def __init__(self, color, radius):
        shape.__init__(self, color) #you must call this as the first
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi
    
class Rectangle (shape):
    # a special method is used to create an instance od this class
    #tthis method is called a constructor
    def __init__(self, color,length, width):
        shape.__init__(self, color)
        shape.length = length
        shape.width = width

    def area(self):
        return self.length * self.width
# an instance/objevt of the Rectangle class
rect = Rectangle('red', 5, 3)
circle = Circle('blue', 10)

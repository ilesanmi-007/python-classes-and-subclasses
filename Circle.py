from Shape import Shape

class Circle( Shape ):
    def __init__(self, radius = 0, pi = 3.142):
        super().__init__()
        self.radius = radius
        self.pi = pi

    def area(self):
        area = self.pi * self.radius * self.radius
        return  area
    def printAll(self):
        print(self.color)
        print(self.fill)
        print(self.radius)
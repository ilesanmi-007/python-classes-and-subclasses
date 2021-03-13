from Shape import Shape

class Triangle(Shape):
    def __init__(self, base=0, height= 0):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        return area
    def printAll(self):
        print(self.color)
        print(self.fill)
        print(self.height)
        print(self.base)
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length = 0, breadth= 0):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area
    #just adding this to print everything i have in it
    def printAll(self):
        print(self.color)
        print(self.fill)
        print(self.length)
        print(self.breadth)

from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle

def main():
    rect = Rectangle()
    rect.length = 5
    rect.breadth = 4
    rect.fill = True
    rect.color = 'Green'

    print('area of the rectangle is', rect.area())
    #rect.printAll

    #for triangle
    tri = Triangle()
    tri.color = "Black"
    tri.fill = False
    tri.base = 6
    tri.height = 14
    print('the area of the triangle is ', tri.area())
    #tri.printAll()

    #for circle
    cir = Circle()
    cir.fill = True
    cir.color = "PURPLE"
    cir.radius = 14
    print('the area of the circle is', cir.area())
    #cir.printAll()


main()
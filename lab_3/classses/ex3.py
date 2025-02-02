class Shape:
    def area(sh):
        return 0
class Rectangle():
    def __init__(sh, length, width):
        sh.length = length
        sh.width = width
    def area(sh):
        return sh.length * sh.width
length = float(input("Length: "))
width = float(input("Width: "))
area1=Rectangle(length,width)
print("Area of the rectangle:",area1.area())



    
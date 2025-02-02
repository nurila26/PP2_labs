class Shape():
    def area(sh):
        return 0
class Square(Shape):
    def __init__(sh,length):
        sh.length=length
    def area(sh):
        return sh.length ** 2
a = float(input("a:"))
mysquare=Square(a)
print("square area",mysquare.area())
myshape=Shape()
print("default:",myshape.area())
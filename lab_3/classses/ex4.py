import math

class Point:
    def __init__(sh,x,y):
        sh.x = x
        sh.y = y

    def show(sh):
        print(f"Coordinates: ({sh.x}, {sh.y})")

    def move(sh, x1, y1):
        sh.x = x1
        sh.y = y1

    def dist(sh, point2):
        dx = sh.x - point2.x
        dy = sh.y - point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
a=float(input("x:"))
b=float(input("y:"))
point1 = Point(a,b)
point2 = Point(a,b)

point1.show() 
k=float(input("x1:"))
p=float(input("y1:"))
point1.move(k,p)
point1.show() 

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")
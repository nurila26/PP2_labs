import math
def volume(r):
    V=(4*math.pi*(r**3))/3
    return V
r=float(input("sphere radius:"))
print("Volume of a sphere:",volume(r))
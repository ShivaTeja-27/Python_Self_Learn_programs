# 9- Area program --- circle, cube, cylinder, sphere, using import math

import math

pi = math.pi


def circle(radius):
    # print("circle ===>")
    return pi*(radius**2)  

def cube(side):
    # print("cube ===>")
    return 6*side*side

def cylinder(radius, height):
    # print("cylinder ===>")
    return 2*pi*radius + 2*pi*height

def sphere(radius):
    # print("sphere ===>")
    return 2*pi*(radius**2)


print(circle(10))
print(cube(4))
print(cylinder(4,6))
print(sphere(10))



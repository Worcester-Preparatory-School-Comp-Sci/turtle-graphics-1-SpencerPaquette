import turtle
import math

#Spencer Paquette 10/15/19

angle = float(input("What is the angle of the slope:"))
mass = float(input("What is the mass of the object"))
w = mass * 9.8
n = w * math.cos(math.radians(angle))
angle2 = 180 - (90 + angle)

triangle = turtle.Turtle() #draws the triangle
triangle.left(angle)
triangle.forward(400)
triangle.right(180 - angle2)
triangle.forward(400 * math.sin(math.radians(angle)))
triangle.right(90)
triangle.forward(400 * math.cos(math.radians(angle)))

square = turtle.Turtle() #draws the object on the slope
square.up()
square.goto((400 * math.cos(math.radians(angle))) / 2 , (400 * math.sin(math.radians(angle))) / 2)
square.down()
square.left(angle)
for x in range(0,4):
    square.forward(75)
    square.left(90)


square.up() #draws the normal force and gravity vectors
square.color('blue')
square.forward(38)
square.down()
square.left(90)
square.forward(n)
square.stamp()
square.up()
square.color('red')
square.left(180)
square.forward(n)
square.right(angle)
square.down()
square.forward(w)
square.stamp()



import math
import turtle

#1

t = turtle.Turtle()

def shape(side, length):
    angle = 360 / side
    t.down()
    for i in range(side):
        t.forward(length)
        t.left(angle)

    t.up()
    t.right(90)
    t.forward(2*length)

#triangle
shape_side = 3
shape_length = 100
shape(shape_side, shape_length)
#square
shape_side+= 1
shape(shape_side, shape_length)
#pentagon
shape_side+= 1
shape(shape_side, shape_length)

#2
radi = 50
for i in range(4):
    print(radi)
    t.down()
    t.circle(radi)
    t.up()
    t.right(90)
    t.forward(50)
    t.left(90)
    radi+= 50

#3
#factorial
print(math.factorial(100), '\n')
print(math.log2(1000000), '\n')
print(math.gcd(63, 49), '\n')
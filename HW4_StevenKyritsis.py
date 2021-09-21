'''
Steven Kyritsis CS100 
2021F Section 031 HW 04,
September 24, 2021
'''

import turtle

#1 & #2
a = 3
b = 4
c = 5

if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b: 
    print("OK")
else:
    print("NOT OK")
if (a+b) == c:
    print("OK")
else:
    print("NOT OK")
if (a**2 + b**2) == c**2:
    print("OK")
else:
    print("NOT OK")

#3
user_color = input('what color? ')
user_width = int(input('what line width? '))
user_length = int(input('what line length? '))
user_shape = input('line, triangle, or square? ')

t = turtle.Turtle()
t.color(user_color)
t.width(user_width)

def line(length):
    t.down()
    t.forward(length)

def triangle(length):
    angle = 360/3
    t.down()
    for i in range(3):
        t.forward(length)
        t.left(angle)

def square(length):
    angle = 360/4
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(angle)

if user_shape == 'line':
    line(user_length)
elif user_shape == 'triangle':
    triangle(user_length)
elif user_shape == 'square':
    square(user_length)
else:
    print('ERROR! Please enter a shape on the menu!')
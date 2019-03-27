# a = int(input('Radius? '))
# S = a**2 * 3.14
# print("Area =", S)

# a = int(input('Enter the temperature in Celsius? '))
# b = a * 5.0
# print(a, "(C) =", b, "(F)")

# from turtle import *
# speed(0)
# color('black', 'white')
# begin_fill()
# for i in range (100):
#     forward(200)
#     left(90)
#     forward(200)
#     left(90)
#     forward(200)
#     left(90)
#     forward(200)
#     left(20)
# end_fill()
# done()
# mainloop ()

# from turtle import *
# speed(0.5)
# color('lightblue', 'yellow')
# begin_fill()
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)
# end_fill()
# done()
# mainloop ()

# from turtle import *
# import math

# circle = Turtle()

# def polygon(t, n, length):
#     for i in range(n):
#         left(360/n)
#         forward(length)

# def draw_circle(t, r):
#     circumference = 2 * math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, n, length)
#     exitonclick()

# draw_circle(circle, 30)

# from turtle import *
# speed(1)
# # turtle.home
# # turtle.position()
# # turtle.heading()
# color('lightblue', 'yellow')
# begin_fill()
# circle(50)
# end_fill()
# done()

# from turtle import *
# speed(0)
# pencolor('green')
# for i in range (9):
#     for i in range(6):
#         circle(100)
#         left(60)
#     left(10)
# right(90)
# mainloop()

# message = "What’s up, Doc?"
# n = 17
# pi = 3.14159
# print(type(pi))

from turtle import *
speed(0)
pencolor('green')
for i in range (9):
    for i in range(6):
        circle(100)
        left(60)
    left(10)
right(90)
mainloop()

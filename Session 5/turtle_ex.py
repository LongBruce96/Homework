#Ex 1

# def hi():
#  for i in range(3):
#   print('Hello world!')

# hi()

#Ex 2

# def x(a,b):
#  print(a + b)

# x(1,2)

#Ex 3

# from turtle import *

# def draw_square(length, chose_color):
#  speed(0)
#  color(chose_color)
#  for i in range(4):
#   forward(length)
#   left(90)  
 
# #Ex 4

# for i in range(30):
#  draw_square(i * 5, 'red')
#  left(17)
#  penup()
#  forward(i * 2)
#  pendown()

# mainloop()

#Ex 5

from turtle import *

def draw_star(x, y, length):
 penup()
 setx(x)
 sety(y)
 pendown()
 for i in range(5):
  right(144)
  forward(length)

 #Ex 6

speed(0)
color('blue')
for i in range(100):
 import random
 x = random.randint(-300, 300)
 y = random.randint(-300, 300)
 length = random.randint(30, 100)
 draw_star(x, y, length)

mainloop()
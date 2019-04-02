# Task 1

# from turtle import *
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# speed(0)
# color(colors[4])
# pencolor(colors[1])
# for i in range(4):
#     forward(100)
#     left(90)
# left(120)
# pencolor(colors[3])
# for i in range(6):
#     forward(100)
#     right(60)
# right(12)
# pencolor(colors[2])
# for i in range(5):
#     forward(100)
#     right(72)
# right(48)
# pencolor(colors[0])
# for i in range(2):
#     forward(100)
#     right(120)
# forward(100)
# right(180)
# forward(100)
# pencolor(colors[4])
# for i in range(6):
#     left(180 - (5 * 180/7))
#     forward(100)
# left(180 - (5 * 180/7))
# mainloop()


# Task 2

from turtle import *

speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in colors:
    color(i,i) 
    begin_fill()
    lt(90)
    fd(100)
    rt(90)
    fd(30)
    rt(90)
    fd(100)
    rt(90)
    fd(30)
    bk(30)
    rt(180)
    end_fill()
lt(90)
fd(100)
rt(90)
mainloop()
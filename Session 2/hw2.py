x = int(input("nhap x: "))
y = int(input("nhap y: "))
if x < y:
    print("Long")
else:
        if x > y:
            print("Long Vip")
        else:
            print("Not Long")


from turtle import *
speed(0)
pencolor('red')
color('red')
right(150)
for i in range (4):
    forward(200)
    right(60)
    forward(200)
    right(120)
    forward(200)
    right(60)
    forward(200)
    left(150)
right(90)
mainloop()


from turtle import *
speed(0)
color('red')
pencolor('red')
for i in range (4):
    forward(100)
    left(90)
left(120)
for i in range (6):
    forward(100)
        right(60)
pencolor('blue')
right(12)
for i in range (5):
    forward(100)
    right(72)
right(48)
for i in range (2):
    forward(100)
    right(120)
pencolor('red')
forward(100)
right(180)
mainloop()


x = int(input("your height is (cm): "))
y = int(input("your weight is: (kg) "))
BMI = int(y / (x/100)**2)
print("BMI = mass (kg) / (height(m) x height(m)")
print("-> your BMI is equal to:", BMI)
if BMI < 16:
    print("you're: Severely Underweight")
elif BMI < 18.5:
    print("you're: Underweight")
elif BMI < 25:
    print("you're: Normal")
elif BMI < 30:
    print("you're: Overweight")
else:
    print("you're: Obese")


x = int(input('enter a number: '))
factorial = 1
if x < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, x + 1):
       factorial = factorial*i
   print("The factorial of",x,"is",factorial)


print("Hello", end = '') 
print(",my name", end = '')
print("is B-max", end = '')


for i in range (20):
    print('* ', end = '')


n = int(input('enter a number: '))
for i in range (n + 1):
    print('* ', end = '')


n = 9
for i in range (1, n, 2):
    print("x", "* ", end = '')
if n % 2 == 1:
    print("x", end = '')


n = int(input('enter a number: '))
for i in range (1, n, 2):
    print("x", "* ", end = '')
if n % 2 == 1:
    print("x", end = '')


print("long")
print()
print("dep trai")


n = 9
m = 9
for i in range (0, 3):
    print("* ", end = '' )
    for i in range (1, 7):
        print("* ", end = '' )
    print('')


n = int(input('enter a number: '))
m = int(input('enter a number: '))
for i in range (0, 3):
    print("* ", end = '' )
    for i in range (1, 7):
        print("* ", end = '' )
    print('')




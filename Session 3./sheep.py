# 2.1
# print('Hello, my name is Long and these are my sheep sizes')
# sheep_sizes = [5, 7, 300, 90, 24, 50, 75]

# 2.2
# print('Hello, my name is Long and these are my sheep sizes')
# flock = [5, 7, 300, 90, 24, 50, 75]
# print(flock)
# print()
# biggest_sheep = max(flock)
# print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")

# 2.3
# print('Hello, my name is Long and here is my flock')
# flock = [5, 7, 300, 90, 24, 50, 75]
# print(flock)
# print()
# biggest_sheep = max(flock)
# print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")
# index = flock.index(biggest_sheep)
# print('After shearing, here is my flock')
# flock[index] = 8
# print(flock)

# 2.4
# print('Hello, my name is Long and here is my flock')
# flock = [5, 7, 300, 90, 24, 50, 75]
# print(flock)
# print()
# biggest_sheep = max(flock)
# print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")
# index = flock.index(biggest_sheep)
# print('After shearing, here is my flock')
# flock[index] = 8
# print(flock)
# flock_after_1_month = [x+50 for x in flock]
# print()
# print('One month has passed, now here is my flock')
# print(flock_after_1_month)

#2.5
# print('Hello, my name is Long and here is my flock')
# flock = [5, 7, 300, 90, 24, 50, 75]
# print(flock)
# print()

# for i in range (4):
#     flock = [x+50 for x in flock]
#     print()
#     print('One month has passed, now here is my flock')
#     print(flock)
#     biggest_sheep = max(flock)
#     print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")
#     index = flock.index(biggest_sheep)
#     print('After shearing, here is my flock')
#     flock[index] = 8
#     print(flock)

#2.6
print('Hello, my name is Long and here is my flock')
flock = [5, 7, 300, 90, 24, 50, 75]
print(flock)
biggest_sheep = max(flock)
print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")
index = flock.index(biggest_sheep)
print('After shearing, here is my flock')
flock[index] = 8
print(flock)
print()

for i in range (2):
    flock = [x+50 for x in flock]
    print()
    print('One month has passed, now here is my flock')
    print(flock)
    biggest_sheep = max(flock)
    print("Now my biggest sheep has size", biggest_sheep, "let's sheer it")
    index = flock.index(biggest_sheep)
    print('After shearing, here is my flock')
    flock[index] = 8
    print(flock)

print()
flock = [x+50 for x in flock]
print('One month has passed, now here is my flock')
print(flock)

sum=0
for n in flock:
    sum = sum + n
print()
print('My flock has size in total:', sum)
price = sum * 2
print('I would get', sum, '* 2$ =', price, end = '')
print('$', end ='')


# # range(3)
# for i in [1,10]:
#     print(i)

# for i in range (2, 10, 0):
#     print(i)

# for i in range (100):
#     if 1 % 2 == 1:
#         print(i)

# n = int(input('nhap n: '))
# for i in range (1, n+1):
#     a = sum(i)
#         print(a)

# tong = 0
# for v in range [1,2,3,4,5]:
#     # tong_tam_thoi=tong+v
#     # tong = tong_tam_thoi
#     tong+=v


# for i in [1,3,5,9]:
#     x = i
#     y = 3*x**2 + 2*x + 1
#     print(y)

for x in range (1,101):
    for y in range (1,101):
        for z in range (1,101):
            if x*y*z == x*x+y*y+z*z:
                print(x,' ',y ,' ',z)

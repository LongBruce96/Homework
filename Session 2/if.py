# yob = int(input("nhap nam sinh: "))
# age = 2019 - yob
# if age <= 10:
#     print("Baby")
# # if 10 < age <= 18: 
# if age <= 18 and age > 10:
#     print("Teen")
# if age > 18:
#     print("Adult")

# n = int(input("nhap so: "))
# # a = int((n**2)**0.5)
# if n<0:
#     print('gia tri tuyet doi cua n =', -n)
# else
#     print('gia tri tuyet doi cua n =', n)

# n = int(input("nhap so: "))

# if n>=0:
#     print('gia tri tuyet doi cua n =', n)
# elif n==0:
#     print('gia tri tuyet doi cua n =', 0)
# else:
#     print('gia tri tuyet doi cua n =', -n)

yob = int(input("nhap nam sinh: "))
age = 2019 - yob
if age < 10:
    print("Baby")
elif age < 18:
    print("Teen")
else:
    print("Adult")
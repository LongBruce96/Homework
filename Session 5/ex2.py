
# def is_inside(x, y):
#     a = [x,y]
#     b = [140, 60, 100, 200]
#     if b[0] < a[0] < b[0] + 100 and b[1] < a[1] < b[1] + 200:
#         return True
#     else:
#         return False
#     print(a, b)

# is_inside([200, 120], [140, 60, 100, 200])

a =[6,7]
b =[9,9,100,100]

def is_inside(p,r):
    print(p)
    print(r)
    
is_inside(p = a, r = b)

if a[0] in range(b[0],b[0]+b[2]) and a[1] in range(b[1],b[1]+b[3]):
    print(True)
else: 
    print(False)


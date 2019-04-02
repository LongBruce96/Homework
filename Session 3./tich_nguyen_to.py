while True:
    n = int(input('nhap so ban can phan tich: '))
    if 0<=n<=1000000:
        print('So ban vua nhap la:', n)
        break
    else:
        print('hay nhap lai')
b = n
a = 2
ds = []
while True:     
        if b%a == 0:
                b=b//a
                ds.append(a)
        else:
                a=a+1
        if b==1:
                break
print('la tich cua cac co sau:')
print(ds)
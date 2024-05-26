Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fact(m):
    f=1
    if m==0:
        return 1
    else:
        while m>0:
            f=f*m
            m-=1
        return f
while True:
    num=int(input("ادخل عدد لحساب المضروب:"))
    print(num," ",{fact(num)})
    a=input("do you want to continue,y or n:")
    if a=="n":
        break

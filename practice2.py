num = int(input("enter a number"))

rem = num % 2
if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("a is greatest")
elif(b >= a and b >= c):
    print("b is greatest")
elif(c >= a and c >= b):
    print("c is greatest")

num = int(input("enter a number"))

rem = num % 7
if(num % 7 == 0):
    print("yes it is multiple of 7")
else:
    print("not")
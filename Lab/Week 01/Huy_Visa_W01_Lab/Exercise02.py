print("Enter the first number:") ; x = input()
print("Enter the second number:"); y = input()
print("Enter the third number:"); z = input()

a = int(x)
b = int(y)
c = int(z)
if a == b and a == c:
    print("None of them are the biggest number :)")
else:
    print("The biggest number is: ")
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
    elif a == b and a < c:
        print(c)
    elif a == c and a < b:
        print(b)
    elif b == c and b < a:
        print(a)

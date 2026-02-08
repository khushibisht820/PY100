import math                       

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b*b - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("The equation has two real and distinct roots")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    root = -b / (2*a)
    print("The equation has two real and equal roots")
    print("Root =", root)

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("The equation has imaginary roots")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")

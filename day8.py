#HERONS FORMULA
#S=a+b+c/2
#AREA= math.sqrt(s(s-a)(s-b)(s-c))
import math                               

a= float(input("enter first side: "))
b= float(input("enter second side: "))
c= float(input("enter third side: "))
s = a+b+c/2
AREA = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("area of triangle =", AREA)
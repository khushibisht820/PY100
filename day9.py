a= int(input("enter first number: "))      
b= int(input("enter second number: "))

c=a+b
b=c-b
a=c-b

print("after swapping:")
print("a =",a)
print("b =", b)
n = int(input("Enter number of values: "))       

count = [0, 0, 0, 0]

print("Enter", n, "values (between 0 and 3):")

for i in range(n):
    value = int(input())
    
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input! Only numbers between 0 and 3 allowed.")

print("\nOccurrences:")
for i in range(4):
    print(i, "occurred", count[i], "times")


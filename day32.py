n = int(input("Enter number of values: "))     

values = []

for i in range(n):
    num = float(input("Enter value: "))
    values.append(num)

numbers = tuple(values)

average = sum(numbers) / n

print("Tuple:", numbers)
print("Average:", average)


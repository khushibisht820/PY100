n = int(input("Enter number of fruits in each set: "))    

s1 = set()
s2 = set()

print("Enter fruits for set 1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)

print("Enter fruits for set 2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)
    s2.add(fruit)

# a) Fruits in both sets
common = s1 & s2

# b) Fruits only in s1
only_s1 = s1 - s2

# c) Count of all fruits from s1 and s2
total_fruits = len(s1 | s2)

print("Fruits in both sets:", common)
print("Fruits only in s1:", only_s1)
print("Total unique fruits from both sets:", total_fruits)
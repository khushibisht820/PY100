string = input("Enter a string: ")            

count = 0 
for volw in string:
    if volw in "aeiouAEIOU":
        count += 1

print("number of vowels:" , count)

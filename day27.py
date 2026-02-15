string = input("Enter a string: ")          

string = string.upper()   # sab letters ko capital bana diya

count_dict = {}

for ch in string:
    if ch.isalpha():      # sirf letters check karenge
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1

for key in sorted(count_dict):
    print(str(count_dict[key]) + key)
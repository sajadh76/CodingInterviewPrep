first_list = [5, 3, 0, 0, 0, 0, 7, 8]
unique_list = []

for num in first_list:
    if num not in unique_list:
        unique_list.append(num)

print (unique_list)

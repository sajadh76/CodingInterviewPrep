first_list = [5, 3, 0, 7, 7, 7, 7, 8, 0, 10, 11]
my_dict = {}
max_value = 0

for num in first_list:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

    if my_dict[num] > max_value:
        max_value = my_dict[num]

for key, value in my_dict.items():
    if value == max_value:
        print(key)

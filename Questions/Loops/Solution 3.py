input_list = [7, 4, -9, -2, -8, 6, 5]
max_value = input_list [0]
min_value = input_list [0]

for i in range (1, len(input_list)):
    if max_value < input_list [i]:
        max_value = input_list[i]
    if input_list [i] < min_value:
        min_value = input_list[i] 

print (max_value)
print (min_value)


num_list = [5, 3, 0, 0, 0, 0, 7, 8]
zero_count = 0
non_zero = []

for num in num_list:
    if num != 0:
        non_zero.append(num)
    else:
        zero_count += 1

final_list = non_zero
for i in range (zero_count):
    final_list.append(0)

print (final_list)
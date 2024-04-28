input_list = [7, 4, 8, 2, 9, 6, 5]
leader_list = []
temp_leader_list = []

for i in range(len(input_list)):
    is_leader = True
    for j in range(i+1, len(input_list)):
        if input_list[i] <= input_list[j]:
            is_leader = False
            break
    if is_leader:
        temp_leader_list.append(input_list[i])

leader_list.append(temp_leader_list)
print("leader values are:", leader_list)

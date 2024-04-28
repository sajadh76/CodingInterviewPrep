building_height = [7, 4, 8, 2, 9, 10]
max_height = 0
output = 0

for building in building_height:
    if building > max_height:
        max_height = building
        output += 1
    else:
        continue

print (output)
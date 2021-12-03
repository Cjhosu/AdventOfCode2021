depths = []
with open('day_one_sample') as file:
    for line in file:
        depths.append(int(line.strip()))

counter = 0

for idx, item in enumerate(depths[1:]):
    if item > depths[idx]:
        counter += 1

print(counter)

counter = 0
for idx, item in enumerate(depths[3:]):
    sum_set1 = depths[idx+2] + depths[idx+1] + depths[idx]
    sum_set2 = item + depths[idx+2] + depths[idx+1]
    if sum_set2 > sum_set1:
        counter += 1

print(counter)

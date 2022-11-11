bingo = []
call_nums = []

with open('day_four_sample') as file:
    first_line = file.readlines()[0].strip()
    call_nums.append(first_line)

with open('day_four_sample') as file:
    next(file)
    for line in file:
        bingo.append(line.strip())

bingo = list(filter(lambda a: a != '', bingo))

print(call_nums)
print(bingo)

counter =1

for i in bingo:
    l = list(i.split(' '))
    l= list(filter(lambda a: a != '', l))
    print(l)



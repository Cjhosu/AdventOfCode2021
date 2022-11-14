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


card_num =1
card_line_num = 1

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []


def create_card(card_num, full_line, card_line_num):
    print(full_line, card_num, card_line_num)

for i in bingo:
    l = list(i.split(' '))
    l= list(filter(lambda a: a != '', l))
    print(l)
    if card_line_num <= 5:
        create_card(card_num, l, card_line_num)
        card_line_num += 1
    else:
        card_line_num = 1
        card_num += 1
        create_card(card_num, l, card_line_num)
        card_line_num += 1


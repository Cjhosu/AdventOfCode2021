logs = []
with open('day_three_input') as file:
    for line in file:
        logs.append(line.strip())

bin_pos_dict = {1: [0,0], 2: [0,0], 3: [0,0], 4: [0,0], 5: [0,0], 6: [0,0], 5: [0,0], 6: [0,0], 7: [0,0], 8: [0,0], 9: [0,0], 10: [0,0], 11: [0,0], 12: [0,0]}

for item in logs:
    dict_key = 1
    pos_list = list(item)
    for i in pos_list:
        if i == '0':
            bin_pos_dict[dict_key][0] += 1
        else:
            bin_pos_dict[dict_key][1] += 1
        dict_key += 1

bin_num_list =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]          
bin_num_index = 0
for k in bin_pos_dict:
    if bin_pos_dict[k][0] > bin_pos_dict[k][1]:
        bin_num_list[bin_num_index] = 0
    else:
        bin_num_list[bin_num_index] = 1
    bin_num_index += 1

def invert_list(list):
    index = 0
    for i in list:
        if i == 0:
            list[index] =1
        else:
            list[index] = 0
        index += 1

def list_to_int(list):
    bin_strings = [str(integer) for integer in list]    
    bin_num = "".join(bin_strings)
    as_int = int(bin_num, 2)
    return(as_int)

gamma = list_to_int(bin_num_list)

invert_list(bin_num_list)

epsilon = list_to_int(bin_num_list)

print(gamma * epsilon)
        

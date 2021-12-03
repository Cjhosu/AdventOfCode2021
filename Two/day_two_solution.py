directions = []
with open('day_two_input') as file:
    for line in file:
        directions.append(line.strip())

coords = [0,0]
# position, depth

for step in directions:
    vector , delta = step.split()
    delta = int(delta)
    if vector == 'forward':
        coords[0] += delta
    if vector == 'up':
        coords[1] -= delta
    if vector == 'down':
        coords[1] += delta

pos = coords[0]
depth = coords[1]

print(pos, depth, pos*depth)

new_coords = [0,0,0]
# aim, position, depth

for step in directions:
    vector , delta = step.split()
    delta = int(delta)
    if vector == 'forward':
        new_coords[1] += delta
        new_coords[2] += new_coords[0] * delta
    if vector == 'up':
        new_coords[0] -= delta
    if vector == 'down':
        new_coords[0] += delta

aim = new_coords[0]
pos = new_coords[1]
depth = new_coords[2]

print(pos, depth, pos*depth)

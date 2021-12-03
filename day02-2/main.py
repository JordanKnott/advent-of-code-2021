
aim = 0
depth = 0
h_pos = 0

lines = [l.strip() for l in open('example.txt').readlines()]
for line in lines:
    parts = line.split(' ')
    if parts[0] == 'forward':
        h_pos += int(parts[1])
        if aim != 0:
            depth += (aim * int(parts[1]))
    elif parts[0] in ['up', 'down']:
        aim += -(int(parts[1])) if parts[0] == 'up' else int(parts[1])
    print(depth, h_pos, aim)

print(depth, h_pos, aim, depth * h_pos)

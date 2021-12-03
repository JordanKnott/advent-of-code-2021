lines = [l.strip() for l in open('input.txt').readlines()]


bit_totals = [0] * len(list(lines[0]))
line_total = 0
for line in lines:
    bits = list(line)
    idx = 0
    line_total += 1
    print(bits)
    for bit in bits:
        if bit == '1':
            bit_totals[idx] += 1
        idx += 1

idx = 0
gamma = ''
epsilon = ''
for bit_total in bit_totals:
    print(idx, bit_total, line_total - bit_total)
    if bit_total > line_total - bit_total:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
    idx += 1

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma, epsilon, gamma * epsilon)


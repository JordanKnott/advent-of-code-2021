lines = [l.strip() for l in open('input.txt').readlines()]


def get_remaining(lines_init, should_switch = False):
    lines_remaining = lines_init
    idx = 0
    while len(lines_remaining) != 0: 
        pos = []
        neg = []
        line_total = len(lines_remaining)
        bit_total = 0
        for line in lines_remaining:
            if list(line)[idx] == '1':
                pos.append(line)
                bit_total += 1
            else:
                neg.append(line)

        print(bit_total, line_total - bit_total,lines_remaining)
        if bit_total > line_total - bit_total:
            if should_switch:
                lines_remaining = neg
            else:
                lines_remaining = pos
        elif bit_total < line_total - bit_total:
            if should_switch:
                lines_remaining = pos
            else:
                lines_remaining = neg
        else:
            for line in lines_remaining:
                if should_switch and list(line)[idx] == '0':
                    return int(line, 2)
                elif should_switch is False and list(line)[idx] == '1':
                    return int(line, 2)
        idx += 1


oxy = get_remaining(lines, False)
co2 = get_remaining(lines, True)

print(oxy, co2, co2 * oxy)

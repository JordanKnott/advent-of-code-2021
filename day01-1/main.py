lines = [f.strip() for f in open('input.txt').readlines()]
prev = 0
increased = 0
for line in lines:
    line_parsed = int(line)
    if line_parsed > prev and prev != 0:
        increased += 1
    prev = line_parsed
print(increased)

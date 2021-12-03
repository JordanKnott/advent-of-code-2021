import collections

lines = [f.strip() for f in open('input.txt').readlines()]
window_id = 0
window_tracker = {}
window_totals = collections.OrderedDict()
for line in lines:
    line_parsed = int(line)
    if window_id not in window_tracker:
        window_tracker[window_id] = 0
    
    to_remove = None
    for wid in window_tracker.keys():
        window_tracker[wid] += 1
        if wid not in window_totals:
            window_totals[wid] = {"total": 0, "group": 0}
        window_totals[wid]['total'] += line_parsed
        window_totals[wid]['group'] += 1
        if window_tracker[wid] == 3:
            to_remove = wid
    if to_remove is not None:
        window_tracker.pop(to_remove, None)
    window_id += 1

prev = 0
increased = 0
for data in window_totals.values():
    if data['group'] != 3:
        continue
    if data['total'] > prev and prev != 0:
        increased += 1
    prev = data['total']
print(increased)

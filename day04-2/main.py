lines = [f.strip() for f in open('input.txt').readlines()]

moves = [int(s) for s in lines[0].split(',')]


combinations = []

diag_one = [0, 1, 2, 3, 4]
diag_two = [4, 3, 2, 1, 0]

def make_combination(board_idx, b):
    return {"values": b, "board": board_idx, "marked": 0}
boards = []
board_idx = 0
current_board = []
current_h = [[], [], [], [], []]
current_diag_one = []
current_diag_two = []
for line in lines[2:]:
    if line == '':
        for b in current_h:
            combinations.append(make_combination(board_idx, b))
        boards.append(current_board)
        current_board = []
        current_h = [[], [], [], [], []]
        combinations.append(make_combination(board_idx, current_diag_one))
        combinations.append(make_combination(board_idx, current_diag_two))
        current_diag_one = []
        current_diag_two = []
        board_idx += 1
        continue
    parts = [int(l) for l in line.split(' ') if l != '']
    current_board.extend(parts)
    combinations.append(make_combination(board_idx, parts))
    idx = 0
    for p in parts:
        current_h[idx].append(p)
        current_diag_one.append(current_board[diag_one[idx]])
        current_diag_two.append(current_board[diag_two[idx]])
        idx += 1
for b in current_h:
    combinations.append(make_combination(board_idx, b))
combinations.append(make_combination(board_idx, current_diag_one))
combinations.append(make_combination(board_idx, current_diag_two))
boards.append(current_board)

board_wins = []
total_boards = len(boards)
def calc_moves():
    completed_moves = []
    for move in moves:
        completed_moves.append(move)
        for c in combinations:
            if move in c["values"]:
                c["marked"] += 1
            if c["marked"] == 5:
                if c['board'] not in board_wins:
                    board_wins.append(c['board'])
                if len(board_wins) == total_boards:
                    print(c)
                    board = [x for x in boards[c['board']] if x not in completed_moves]
                    total = 0
                    for x in board:
                        total += x
                    print(c['board'])
                    print(total * move)
                    return


calc_moves()

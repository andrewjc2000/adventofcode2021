lines = open('day4.txt', 'r').readlines()

a = [line for line in lines]

def win(board, called):
    for i in range(5):
        row = True
        col = True
        for j in range(5):
            if board[i][j] not in called:
                row = False
            if board[j][i] not in called:
                col = False
        if row or col:
            return True
    return False


boards = []
i = 2
while i < len(lines):
    board = []
    for j in range(5):
        board.append([x.strip() for x in lines[i].split()])
        i += 1
    boards.append(board)
    i += 1

numbers = [x.strip() for x in lines[0].split(',')]

def get_winning_board_value(n):
    wins = set()
    for i in range(1, len(numbers)):
        curr = numbers[:i]
        for j in range(len(boards)):
            board = boards[j]
            if win(board, curr):
                wins.add(j)
                if len(wins) == n:
                    s = 0
                    for line in board:
                        for x in line:
                            if x not in curr:
                                s += int(x)
                    return s*int(curr[-1])

# part 1
print(get_winning_board_value(1))

# part 2
print(get_winning_board_value(100))

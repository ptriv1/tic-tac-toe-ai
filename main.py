spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for i in [0, 3, 6]:
    for j in range(3):
        cell = spaces[i + j]
        if cell in ["X", "O"]:
            symbol = cell
        else:
            symbol = " "
        if j < 2:
            print(symbol, end=" | ")
        else:
            print(symbol, end="")
    print()
    if i != 6:
        print("---+---+---")


def check_win(spaces, player):
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combination in combinations:
        if (
            spaces[combination[0]] == player
            and spaces[combination[1]] == player
            and spaces[combination[2]] == player
        ):
            return True
    return False

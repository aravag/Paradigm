def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def xo():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")

        row = int(input("Введите номер строки (1, 2, 3): ")) - 1
        col = int(input("Введите номер столбца (1, 2, 3): ")) - 1

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Некорректный ход. Попробуйте еще раз.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        elif is_full(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    xo()

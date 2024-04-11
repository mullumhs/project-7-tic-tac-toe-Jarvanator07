board = []

for i in range(6):
    board.append(["_","_","_","_","_","_","_"])

while True:

    def print_board():
        for row in board:
            print(row)

    def place_token(player_count):
        token = "X"
        if player_count % 2 == 0:
            token = "O"

    # to check for win
    for row in range(6):
        for colum in range(4):
            if board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] == "X":
                print("Player X wins")
                break
            elif board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] == "O":
                print("Player O wins")
                break

    def switch_player():
        global tokenX
        global tokenO
        if tokenX == 'X':
            tokenX = 'O'
            tokenO = 'X'
        else:
            tokenX = 'X'
            tokenO = 'O'
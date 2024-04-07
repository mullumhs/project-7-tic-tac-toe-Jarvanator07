board = []

for i in range(6):
    board.append(["_","_","_","_","_","_"])

for row in board:
    for colum in row:
        print(colum, end=' ')
    print()

int(input("Enter your choice(column 1-6): "))
if int(input()) in range(1,7):
    board[0][int(input())-1] = "X"
else:
    print("Invalid input")

def placeToken(board, column, player):

    for i in range(5, -1, -1):

        if board[i][column] == '-':

            # Place the token
            board[i][column] = player
            break

for row in range(4):
    for colum in range(6):
        if board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] and not board[row][colum + 3] == "_":
            print("Player X wins")
            break
        elif board[row][colum] == board[row+1][colum] == board[row+2][colum] == board[row+3][colum] == "O":
            print("Player O wins")
            break
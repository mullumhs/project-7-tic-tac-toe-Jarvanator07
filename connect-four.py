board = []

for i in range(6):
    board.append(["_","_","_","_","_","_","_"])

while True:

    starting_player = input("Do you want to play as X or O? ")
    if starting_player == "X" or starting_player == "O":
        break
    else:
        print("Invalid input")
    
    

    # to print the board
    for row in board:
        for colum in row:
            print(colum, end=' ')
        print()

    tokenX = 'X'
    tokenO = 'O'
    column = int(input("Enter your choice(column 1-6): "))

    # to place the token
    for row in range(5, -1, -1):
        if board[row][column] == "_":
            board[row][column] = tokenO 
            break

    # to check for win
    for row in range(6):
        for colum in range(4):
            if board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] == "X":
                print("Player X wins")
                break
            elif board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] == "O":
                print("Player O wins")
                break
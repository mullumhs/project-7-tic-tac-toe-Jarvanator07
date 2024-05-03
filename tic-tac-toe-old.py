
def init_board():
    board = []
    for i in range(3):
        board.append(["_","_","_"])
    return board

def print_board(board):
    for row in board:
        for colum in row:
            print(colum, end = " ")
        print()

def place_token(player_count, board):
    token = "X"
    if player_count % 2 == 0:
        token = "O"
    

    # get col
    colum = int(input("what column do you want?(1,2,3)")) - 1
    # get row
    row = int(input("what row do you want?(1,2,3)")) - 1
    # place token in the board  
    board[row][colum] = token
    player_count = player_count + 1
    return player_count

# to check for win
def check_win():
    for row in range(6):
        for colum in range(4):
            if board[row][colum] == board[row][colum + 1] == board[row][colum + 2] == board[row][colum + 3] == "X":
                print("Player X wins")
                break
            elif board[row][colum] == board[row][colum + 1] == board[row][colum+ + 2] == board[row][colum + 3] == "O":
                print("Player O wins")
                break


def main():
    player_count = 1
    board = init_board()
    while True:        
        print_board(board)
        player_count = place_token(player_count, board)

if __name__ == "__main__":
    main()
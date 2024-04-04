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
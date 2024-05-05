board = [' ' for x in range(9)] 

def print_board():
  row1 = '|_' + board[0] + '_|_' + board[1] + '_|_' + board[2] + '_| 1 R'
  row2 = '|_' + board[3] + '_|_' + board[4] + '_|_' + board[5] + '_| 2 O'
  row3 = '| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | 3 W'

  print()
  print("   COLUMN")
  print('  1   2   3')
  print("_"*13)
  print(row1)
  print(row2)
  print(row3)
  print("‾"*13)
  print()

def player_move(icon):
  if icon == 'X':
    number = 1
  elif icon == 'O':
    number = 2
    
  print('Your turn player ' + str(number))
  while True:
    try:
      col = int(input('Enter column (1-3): ').strip())
      if col < 1 or col > 3:
        raise ValueError
      break
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 3.")
  while True:
    try:
      row = int(input('Enter row (1-3): ').strip())
      if row < 1 or row > 3:
        raise ValueError
      break
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 3.")
  choice = (row - 1) * 3 + (col - 1)
  if board[choice] == ' ':
    board[choice] = icon
  else:
    print()
    print('That space is taken! You lost your turn.')

def is_victory(icon):
  if (board[0] == icon and board[1] == icon and board[2] == icon) or \
     (board[3] == icon and board[4] == icon and board[5] == icon) or \
     (board[6] == icon and board[7] == icon and board[8] == icon) or \
     (board[0] == icon and board[3] == icon and board[6] == icon) or \
     (board[1] == icon and board[4] == icon and board[7] == icon) or \
     (board[2] == icon and board[5] == icon and board[8] == icon) or \
     (board[0] == icon and board[4] == icon and board[8] == icon) or \
     (board[2] == icon and board[4] == icon and board[6] == icon):
    return True
  else:
    return False

def is_draw():
  if ' ' not in board:
    return True
  else:
    return False

while True:
  print_board()
  player_move('X')
  print_board()
  if is_victory('X'):
    print('X wins! Congratulations!')
    break
  elif is_draw():
    print('Its a draw!')
    break
  
  player_move('O') 
  if is_victory('O'):
    print_board()
    print('O wins! Congratulations!')
    break
  elif is_draw():
    print('Its a draw!')
    break
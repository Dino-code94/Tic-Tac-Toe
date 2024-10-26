print(''' 
    
Welcome to Tic-Tac-Toe Game! 
__________________________________

Let the Game Begin!    
_______________________

Simple Game Rules:
    Player 1 will be X , and Player 2 will be O.
    Players take turns putting their marks in empty squares. 
    The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
    When all 9 squares are full, the game is over. 
    If no player has 3 marks in a row, the game ends in a draw.
      
     
     Enjoy playing!!
___________________________

''')

board = [
  0,0,0,
  0,0,0,
  0,0,0
  ]

def print_board():
  display_positon = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  for i in range(9):
    if board[i] == 1:
      display_positon[i] = 'X'
    elif board[i] == 2:
      display_positon[i] = 'O'

  print('''
 ______________
|  {} |  {} |  {} |
|____|____|____|
|  {} |  {} |  {} |
|____|____|____|  
|  {} |  {} |  {} |
|____|____|____|        

'''.format(*display_positon))

# Checks if player has won
def check_win(num):
    if board[0] == num and board[1] == num and board[2] == num:
      return True
    elif board[3] == num and board[4] == num and board[5] == num:
      return True
    elif board[6] == num and board[7] == num and board[8] == num:
      return True
    elif board[0] == num and board[3] == num and board[6] == num:
      return True
    elif board[1] == num and board[4] == num and board[7] == num:
      return True
    elif board[2] == num and board[5] == num and board[8] == num:
      return True
    elif board[0] == num and board[4] == num and board[8] == num:
      return True
    elif board[2] == num and board[4] == num and board[6] == num:
      return True
    else:
      return False
# Turn counter
turn = 0

while turn < 9:
    # Player 1's turn.
    while True:
        try:
            p1_position = int(input("Player 1 enter position number (1 through 9): ")) - 1
            if 0 <= p1_position <= 8 and board[p1_position] == 0:
                board[p1_position] = 1
                break       

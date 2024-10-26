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

print(''' 
    
Welcome to Tic-Tac-Toe Game! 
__________________________________

Let the Game Begin!    
_______________________

Simple Game Rules:
    Player 1 will be X , and Player 2 will be O.
    Players take turns putting their marks in empty squares. 
    The first player to get 3 of her marks in a row 
    (up, down, across, or diagonally) is the winner.
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
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == num for i in combo):
            return True
    return False

# One full game session
def play_game():
    board = [0] * 9
    turn = 0

    while turn < 9:
        # Player 1's turn
        while True:
            try:
                p1_position = int(input("Player 1 enter position number (1 through 9): ")) - 1
                if 0 <= p1_position <= 8 and board[p1_position] == 0:
                    board[p1_position] = 1
                    break
                elif p1_position < 0 or p1_position > 8:
                    print('Invalid position number. Please enter a number between 1 and 9.')
                else:
                    print('Position already taken. Please choose another position.')
            except ValueError:
                print('Invalid input. Please enter a number.')

        turn += 1
        print_board(board)

        if check_win(board, 1):
            print('Player 1 WINS')
            return

        if turn == 9:
            print('Draw')
            return

        # Player 2's turn
        while True:
            try:
                p2_position = int(input("Player 2 enter position number (1 through 9): ")) - 1
                if 0 <= p2_position <= 8 and board[p2_position] == 0:
                    board[p2_position] = 2
                    break
                elif p2_position < 0 or p2_position > 8:
                    print('Invalid position number. Please enter a number between 1 and 9.')
                else:
                    print('Position already taken. Please choose another position.')
            except ValueError:
                print('Invalid input. Please enter a number.')

        turn += 1
        print_board(board)

        if check_win(board, 2):
            print('Player 2 WINS')
            return


# Loop to allow replaying
while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing!")
        break
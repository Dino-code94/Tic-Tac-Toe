import random


# Display game rules and intro message
def print_intro():
    print('''
Welcome to Tic-Tac-Toe Game!
__________________________________

Let the Game Begin!
_______________________

Simple Game Rules:
    Player 1 will be X , and Player 2 will be O.
    Players take turns putting their marks in empty squares.
    The first player to get X of their marks in a row
    (up, down, across, or diagonally) is the winner.
    When all squares are full, the game is over.
    If no player has X marks in a row, the game ends in a draw.

Enjoy playing!!
___________________________
''')


# Render the board based on size and current state
def print_board(board, size):
    symbols = ['-', 'X', 'O']
    for row in range(size):
        line = ' | '.join(
            symbols[board[row * size + col]] for col in range(size)
        )
        print(f" {line} ")
        if row < size - 1:
            print('---+' * (size - 1) + '---')


# Check all winning conditions for a given player
def check_win(board, player, size):
    for row in range(size):
        if all(board[row * size + col] == player for col in range(size)):
            return True
    for col in range(size):
        if all(board[row * size + col] == player for row in range(size)):
            return True
    if all(board[i * size + i] == player for i in range(size)):
        return True
    if all(board[i * size + (size - 1 - i)] == player for i in range(size)):
        return True
    return False


# One full game round, supports AI and board size selection
def play_game():
    while True:
        try:
            size = int(input("Enter board size (3, 4, or 5): "))
            if size in [3, 4, 5]:
                break
            print("Invalid size. Please choose 3, 4, or 5.")
        except ValueError:
            print("Please enter a valid number.")

    board = [0] * (size * size)
    turn = 0
    total_turns = size * size

    ai_prompt = "Do you want to play against the AI? (y/n): "
    vs_ai = input(ai_prompt).strip().lower() == 'y'

    while turn < total_turns:
        # Player 1
        while True:
            try:
                prompt = f"Player 1 enter position (1–{size * size}): "
                p1_pos = int(input(prompt)) - 1
                if 0 <= p1_pos < size * size and board[p1_pos] == 0:
                    board[p1_pos] = 1
                    break
                print("Invalid or taken position.")
            except ValueError:
                print("Please enter a valid number.")

        turn += 1
        print_board(board, size)

        if check_win(board, 1, size):
            print("Player 1 WINS")
            return
        if turn == total_turns:
            print("Draw")
            return

        # Player 2 or AI
        if vs_ai:
            print("AI is making a move...")
            empty = [i for i, val in enumerate(board) if val == 0]
            board[random.choice(empty)] = 2
        else:
            while True:
                try:
                    prompt = f"Player 2 enter position (1–{size * size}): "
                    p2_pos = int(input(prompt)) - 1
                    if 0 <= p2_pos < size * size and board[p2_pos] == 0:
                        board[p2_pos] = 2
                        break
                    print("Invalid or taken position.")
                except ValueError:
                    print("Please enter a valid number.")

        turn += 1
        print_board(board, size)

        if check_win(board, 2, size):
            print("Player 2 WINS")
            return
        if turn == total_turns:
            print("Draw")
            return


# Replay loop and program entry point
def main():
    print_intro()
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

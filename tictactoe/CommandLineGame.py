from tictactoe.board import Board

board = Board()

def play_again():
    ans = input("Play again (y/n): ")
    return True if ans == "y" else False

while(True):
    board.display()
    print(board.current.symbol + " plays")
    r = int(input("Row: "))
    c = int(input("Col: "))
    board.play(r, c)
    winner = board.get_winner()
    if winner is not None:
        board.display()
        # display score
        print(winner + " wins!")
        if play_again():
            board.reset()
        else:
            break
    if board.is_tie():
        board.display()
        print("It's a Tie!")
        if play_again():
            board.reset()
        else:
            break

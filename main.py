from tictactoe import Tictactoe

"""
3 classes:
- board
- player
- game (TicTacToe)

pseudocode:
    print board 3x3

    ask user to choose a square
        can choose a square based on its coords
        eg ask what row, what col
    if theres something in that place ask again
    otherwise place in that space

    check if someone has won from round 3
    win is whole row/col or diag

    possible improvements:
        - user class that keeps track of score
        - add visual eg colour of X,Os
        - clear screen every time and print board
"""

if __name__ == "__main__":
    
    game = Tictactoe()
    game.play()
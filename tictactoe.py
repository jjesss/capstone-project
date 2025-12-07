from board import Board
from player import Player

class Tictactoe:
    def __init__(self):
        self.board = Board(3,3)
        self.player_x = Player("X")
        self.player_o = Player("O")

        self.current_player = self.player_x

    def switch_player(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

    def play(self):
        print("Tic-Tac-Toe Game")
        self.board.display()

        while True:
            print(f"\nPlayer {self.current_player.symbol}'s turn.")
            row,col = self.current_player.get_move()

            if not self.board.move(row, col, self.current_player.symbol):
                print("That spot is already taken. Try again.")

            self.board.display()

            winner = self.board.check_winner()

            # check for winner
            if winner:
                print(f"\nPlayer {winner} wins!")

                break

            # check for draw
            if self.board.check_draw():
                print(f"\nIt's a draw!")
                break

            
            self.switch_player()
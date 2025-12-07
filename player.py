class Player:
    def __init__(self, symbol):
        self.symbol = symbol # X or O

    def get_move(self):
        while True:
            try:
                row = int(input(f"Player {self.symbol}, enter row: "))
                col = int(input(f"Player {self.symbol}, enter col: "))

                if row in [0,1,2] and col in [0,1,2]:
                    return row, col
                else:
                    print("Invalid input. Row and col must be 0,1,2")
            except ValueError:
                print("Please enter numbers only.")

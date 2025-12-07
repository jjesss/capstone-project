class Board:
    def __init__(self,rows,cols, fill = " "):
        """
        For tictactoe we are going to have a set grid size of 3x3
        """
        self.cols = cols
        self.rows = rows
        self.grid = [[fill for _ in range(cols)] for _ in range(rows)] # creates grid

    def display(self):
        print("+---" * self.cols + "+")
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
            print("+---" * self.cols + "+")

    def move(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True 
        return False 
          
    def check_winner(self):
        # check all rows
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
            
        # check all cols
        for col in range(3):
            if (self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " "):
                return self.grid[0][col]
            
        # check forwards diag
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " "):
            return self.grid[0][0]

        # check backwards diag
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " "):
            return self.grid[0][2]
        
        return None

    def check_draw(self):
        # no spaces then means they draw

        if any(" " in row for row in self.grid):
            return False
        
        return self.check_winner() is None

    # could have a def __str__(self) function but we have display so we wont



    
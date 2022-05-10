from tictactoe.player import Player


class Board:
    def __init__(self):
        self.grid = []
        self.player_x = Player("X")
        self.player_o = Player("O")
        self.current = None
        self.reset()

    def reset(self):
        self.grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.current = self.player_x

    def play(self, row, col):
        row = row - 1
        col = col - 1
        if row < 0 or col < 0 or row > 2 or col > 2:
            print("Values out of range")
            return False
        if self.grid[row][col] != '-':
            print('Cell already used')
            return False
        self.grid[row][col] = self.current.symbol
        self.current = self.player_x if self.current == self.player_o else self.player_o
        return True

    def display(self):
        for r in range(3):
            for c in range(3):
                print(self.grid[r][c], end=' ')
            print()

    def get_winner(self):
        for row in range(3):
            if self.grid[row][0] != '-' and self.grid[row][0] == self.grid[row][1] \
                    and self.grid[row][0] == self.grid[row][2]:
                return self.grid[row][0]
        for col in range(3):
            if self.grid[0][col] != '-' and self.grid[0][col] == self.grid[1][col] \
                    and self.grid[0][col] == self.grid[2][col]:
                return self.grid[0][col]
        if self.grid[0][0] != '-' and self.grid[0][0] == self.grid[1][1] \
                and self.grid[0][0] == self.grid[2][2]:
            return self.grid[0][0]
        if self.grid[0][2] != '-' and self.grid[0][2] == self.grid[1][1] \
                and self.grid[0][2] == self.grid[2][0]:
            return self.grid[0][2]
        return None

    def is_tie(self):
        return False
import random
import collections


class Board:
    rows: int
    cols: int
    mineCount: int
    initialized: bool
    board: list
    mineLocations: set
    moves: list
    seen: set
    availableSpaces: int

    def __init__(self, _rows, _cols, _mineCount):
        self.rows = _rows
        self.cols = _cols
        self.mineCount = _mineCount
        self.initialized = False
        self.board = [['H'] * _cols for _ in range(_rows)]
        self.mineLocations = set()
        self.seen = set()
        self.availableSpaces = _rows * _cols - _mineCount

        self.moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        self._printBoard()

    def play(self):
        while self._tilesAvailable():
            row = self._getRow()
            col = self._getCol()
            print('Mined: ', row, col)
            row -= 1
            col -= 1

            if not self.initialized:
                self._initializeBoard(row, col)

            if (row, col) in self.mineLocations:
                self._lose()
                
            self._bfs(row, col)
            self._printBoard()

        # win condition
        print("You Won!")

    def _getRow(self):
        while True:
            try:
                row = int(input(f'Enter row (1-{self.rows}): '))
                if 0 < row <= self.rows:
                    return row
            except ValueError:
                pass
            print('Invalid row! Try again.')

    def _getCol(self):
        while True:
            try:
                row = int(input(f'Enter column (1-{self.cols}): '))
                if 0 < row <= self.cols:
                    return row
            except ValueError:
                pass
            print('Invalid column! Try again.')

    def _initializeBoard(self, row, col):
        self.initialized = True
        rand = random
        placed = 0

        while placed < self.mineCount:
            mine_row = rand.randint(0, self.rows - 1)
            mine_col = rand.randint(0, self.cols - 1)
            if row != mine_row and col != mine_col and (mine_row, mine_col) not in self.mineLocations:
                self.mineLocations.add((mine_row, mine_col))
                # self.board[mine_row][mine_col] = '*'  # remove for actual game
                placed += 1
                
    def _lose(self):
        # lose condition
        for mine_row, mine_col in self.mineLocations:
            self.board[mine_row][mine_col] = '*'
        self._printBoard()
        print("You Lost!")
        quit()

    def _bfs(self, start_row, start_col):
        queue = collections.deque()
        queue.append((start_row, start_col))

        while queue:
            row, col = queue.popleft()
            if (row, col) in self.seen or (row, col) in self.mineLocations:
                continue

            self.seen.add((row, col))
            self.availableSpaces -= 1  # number non-bomb availableSpaces

            mines = self._checkSurroundingMines(row, col)
            if mines > 0:
                # change to number.
                self.board[row][col] = str(mines)
                continue
            elif mines == 0:
                self.board[row][col] = '.'

            # add possible moves
            for next_row, next_col in self.moves:
                next_row += row
                next_col += col

                if self.rows > next_row >= 0 <= next_col < self.cols and (next_row, next_col) not in self.mineLocations:
                    queue.append((next_row, next_col))

    def _checkSurroundingMines(self, row, col):
        mines = 0

        for next_row, next_col in self.moves:
            next_row += row
            next_col += col

            if (next_row, next_col) in self.mineLocations:
                mines += 1

        return mines

    def _tilesAvailable(self):
        return self.availableSpaces > 0

    def _printBoard(self):
        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                if i == 0 and j == 0:
                    print(' ', end=' ')
                elif i == 0:
                    print(j, end=' ')
                elif j == 0:
                    print(i, end=' ')
                else:
                    print(self.board[i - 1][j - 1], end=' ')
            print()
        print()

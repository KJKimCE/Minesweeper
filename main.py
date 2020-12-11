from Board import Board


def startGame():
    rows = int(input('Enter the size of the board (rows): '))
    cols = int(input('Enter the size of the board (columns): '))
    mines = int(input('Enter the number of mines: '))

    board = Board(rows, cols, mines)
    board.play()


if __name__ == '__main__':
    startGame()

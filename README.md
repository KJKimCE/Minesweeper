# Minesweeper # 
This is a simple command line based minesweeper game.

## Description ##
To begin, the user is prompted to enter 3 inputs to initialize the board:

    rows
    columns
    mine count

The board is filled using the following characters:

    H - Hidden
    * - Mine
    . - Clear tile with no surrounding mines
    1~9 - Clear tile with # surrounding mines 

## Gameplay ##
The user is continuously prompted to enter the row and column:

    row
    column

## Sample ##
User input (initialization):

    rows: 5
    columns: 5
    mines: 1

      1 2 3 4 5 
    1 H H H H H 
    2 H H H H H 
    3 H H H H H 
    4 H H H H H 
    5 H H H H H 

User input (gameplay):

    row: 3
    column: 3

      1 2 3 4 5 
    1 . . 1 H H 
    2 . . 1 1 1 
    3 . . . . . 
    4 . . . . . 
    5 . . . . . 

    row: 1
    column: 5

      1 2 3 4 5 
    1 . . 1 H 1
    2 . . 1 1 1 
    3 . . . . . 
    4 . . . . . 
    5 . . . . .

    You Won!
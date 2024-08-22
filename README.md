# Tic-Tac-Toe
A simple graphical Tic-Tac-Toe game implemented in Python using the tkinter library. This game allows you to play Tic-Tac-Toe against a computer opponent with a graphical user interface.

## Features
Play Tic-Tac-Toe against the computer.

Simple and intuitive graphical interface.

Game messages display when you win, lose, or if there is a tie.

Automatically resets the game after it ends.

## Requirements
Python 3.x

tkinter (included with standard Python installations)

## Code Overview

Main Window: Created using tkinter, it includes a 3x3 grid of buttons.
Game Logic:
### reset_board(): Resets the game board.
### check_win(player): Checks for a win condition for the specified player.
### on_button_click(row, col): Handles user moves and updates the board.
### computer_move(): Handles the computer’s move.
###M essage Boxes: Display game status and results using messagebox.showinfo.

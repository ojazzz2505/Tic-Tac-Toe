import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the game board as a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
board = [" " for _ in range(9)]

def reset_board():
    global board
    board = [" " for _ in range(9)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL)

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def on_button_click(row, col):
    index = row * 3 + col
    if board[index] == " ":
        board[index] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED)
        if check_win("X"):
            messagebox.showinfo("Game Over", "Congratulations! You win!")
            reset_board()
            return
        if " " not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
            return
        computer_move()

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    if available_moves:
        move = random.choice(available_moves)
        board[move] = "O"
        row, col = divmod(move, 3)
        buttons[row][col].config(text="O", state=tk.DISABLED)
        if check_win("O"):
            messagebox.showinfo("Game Over", "Sorry, you lose. Better luck next time.")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()

# Create and place buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", width=10, height=3,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Start the main event loop
root.mainloop()

# Tic-Tac-Toe-game---GUI-python-
"""This code is a simple implementation of a Tic-Tac-Toe game using the tkinter library for creating a graphical user interface. Let's go through the code step by step:

1. Importing Libraries:
   - `tkinter` and `messagebox` are imported to create the graphical user interface and show message boxes for the game results.

2. Game Logic Functions:
   - `check_win()`: This function checks if a player has won the game. It iterates through rows, columns, and diagonals of the game board to see if a player has three in a row. If it finds a winning combination, it returns `True`, indicating that the game is won.
   - `check_draw()`: This function checks if the game is a draw (a tie). It returns `True` if there are no empty cells left on the board.

3. `click_on()` Function:
   - This function is called when a button (representing a cell on the board) is clicked.
   - It takes the `row` and `col` arguments to determine which cell was clicked.
   - It checks if the clicked cell is empty and if the game is not already over.
   - If the conditions are met, it updates the game board, disables the clicked button, and checks for a win or a draw.
   - If a win or a draw is detected, a message box is displayed with the game result.
   - It also toggles the `current_player` between "X" and "O" for the next turn.

4. Main Application (`app`):
   - A tkinter window is created with the title "Tic_Tac-Toe".

5. Game Board (`board`) and Buttons:
   - The `board` is a 3x3 matrix to represent the state of the game. Initially, all cells are empty.
   - A grid of 3x3 buttons is created to represent the Tic-Tac-Toe game board. These buttons are placed in rows and columns and have a command associated with them to call the `click_on()` function when clicked.

6. `current_player` and `game_over`:
   - `current_player` keeps track of which player's turn it is, starting with "X."
   - `game_over` is initially set to `False` and is used to determine if the game has ended.

7. `app.mainloop()`:
   - This statement starts the tkinter event loop, allowing the graphical interface to function and respond to user interactions.

In summary, this code creates a basic Tic-Tac-Toe game with a graphical interface using tkinter. Players take turns clicking on empty cells, and the game checks for a win or a draw after each move, displaying a message box with the result.
"""

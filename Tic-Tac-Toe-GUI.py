#TIC-TAC-TOE --GUI (PYTHON SOURCE CODE)

import tkinter as tk  #create gui
from tkinter import messagebox #game result


#Checks  if a player has won the game or not
def check_win():
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":  #checks row-wise
            return True
        if board[0][i]==board[1][i]==board[2][i]!="":  #chcks columns-wise
            return True
    if board[0][0]==board[1][1]==board[2][2]!="":     #checks Right-diagonal
        return True
    if board[0][2]==board[1][1]==board[2][0]!="":     #checks Left-diagonal
        return True
    return False


#Checks if the game is draw(tie)
def check_draw():
    return all(board[i][j] !="" for i in range(3) for j in range(3))  #return True if there is no empty cells are in the board


def click_on(row,col):
    global current_player,game_over
    
    if board[row][col]=="" and not game_over:
        board[row][col]=current_player
        buttons[row][col].config(text=current_player,state="disabled")
        
        if check_win():
            messagebox.showinfo("Tic-tac-Toe", "Player " + current_player + " wins!")  #show the result
            game_over=True
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe","Its a draw!.")
            game_over=True
        else:
            current_player = "X" if current_player == "O" else "O"

#Main application            
app=tk.Tk()
app.title("Tic_Tac-Toe")

board=[["" for _ in range(3)] for _ in range(3)]
buttons=[]

for i in range(3):
    row_buttons=[]
    for j in range(3):
        button=tk.Button(app,text="",width=20,height=5,command=lambda i=i,j=j: click_on(i,j))  #grid buttons are created with command of rows,and columns
        button.grid(row=i,column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)
    
current_player="X"
game_over=False

app.mainloop()
            
        
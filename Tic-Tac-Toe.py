import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        # Create a 3x3 grid of buttons
        self.buttons = [[None for i in range(3)] for i in range(3)]
        self.create_buttons()

    def create_buttons(self):
        # Initialize buttons and place them in the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font='normal 20 bold', height=3, width=6,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        # Handle button click event
        if self.buttons[i][j]['text'] == "" and self.check_winner() is False:
            self.buttons[i][j]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                # Switch player
                self.player = 'O' 
                self.computer_move()

    def computer_move(self):
        # Block the player from winning
         marked = False

        # Check rows for a blocking move
         for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] != '' and self.buttons[i][2]['text'] == '':
                self.buttons[i][2]['text'] = self.player
                marked = True
                break
            elif self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '' and self.buttons[i][0]['text'] == '':
                self.buttons[i][0]['text'] = self.player
                marked = True
                break
            elif self.buttons[i][0]['text'] == self.buttons[i][2]['text'] != '' and self.buttons[i][1]['text'] == '':
                self.buttons[i][1]['text'] = self.player
                marked = True
                break

         # Check columns for a blocking move
         if not marked:
            for i in range(3):
                if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] != '' and self.buttons[2][i]['text'] == '':
                    self.buttons[2][i]['text'] = self.player
                    marked = True
                    break
                elif self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '' and self.buttons[0][i]['text'] == '':
                    self.buttons[0][i]['text'] = self.player
                    marked = True
                    break
                elif self.buttons[0][i]['text'] == self.buttons[2][i]['text'] != '' and self.buttons[1][i]['text'] == '':
                    self.buttons[1][i]['text'] = self.player
                    marked = True
                    break

         # Check diagonals for a blocking move
         if not marked:
            if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] != '' and self.buttons[2][2]['text'] == '':
                self.buttons[2][2]['text'] = self.player
                marked = True
            elif self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '' and self.buttons[0][0]['text'] == '':
                self.buttons[0][0]['text'] = self.player
                marked = True
            elif self.buttons[0][0]['text'] == self.buttons[2][2]['text'] != '' and self.buttons[1][1]['text'] == '':
                self.buttons[1][1]['text'] = self.player
                marked = True

            elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] != '' and self.buttons[2][0]['text'] == '':
                self.buttons[2][0]['text'] = self.player
                marked = True
            elif self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '' and self.buttons[0][2]['text'] == '':
                self.buttons[0][2]['text'] = self.player
                marked = True
            elif self.buttons[0][2]['text'] == self.buttons[2][0]['text'] != '' and self.buttons[1][1]['text'] == '':
                self.buttons[1][1]['text'] = self.player
                marked = True

         # If no block move, play randomly
         if not marked:
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == '':
                        self.buttons[i][j]['text'] = self.player
                        marked = True
                        break
                if marked:
                    break

         # Check if the AI won after making the move
         if self.check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            self.reset_board()
            return

         elif self.check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.reset_board()
            return

         # Switch turn back to Player X
         self.player = 'X'


    def check_winner(self):
        # Check rows for a win
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True
            # Check columns for a win
            elif self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                return True
        # Check diagonals for a win
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

    def check_draw(self):
        # Check if all buttons are filled and there's no winner
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == '':
                    return False
        return True

    def reset_board(self):
        # Reset the board for a new game
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.player = 'X'


#starting application
if __name__ == "__main__" :
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

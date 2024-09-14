from tkinter import *
current_player = 'X'
win = False
def main():

    #creation du fenetre de jeu
    window = Tk()
    buttons = []
    
    #fonctions
    def switch_player():
        global current_player
        if current_player == 'X':
            current_player = '0'
        else:
            current_player = 'X'
    def print_winner():
        global win
        win = True
        print("Le joueur " +current_player+ " a gagné :) ")    
    
    def check_nul():
        print("Match nul")

    
    def check_win(row,column):
       
       #horizontale 
       count = 0
       for i in range(3):
           current_button = buttons[i][row] 
           if current_button['text'] == current_player:
               count += 1
       if count == 3:
           print_winner()
        #verticale 
       count=0
       for i in range(3):
           current_button = buttons[column][i] 
           if current_button['text'] == current_player:
               count += 1
       if count == 3:
           print_winner()
       #diagonale    
       count=0
       for i in range(3):
           current_button = buttons[i][i] 
           if current_button['text'] == current_player:
               count += 1
       if count == 3:
           print_winner()
       #diagonale inverse   
       count=0
       for i in range(3):
           current_button = buttons[2 - i][i] 
           if current_button['text'] == current_player:
               count += 1 
       if count == 3:
           print_winner() 

       if win is False :
           count = 0
           for col in range(3):
               for row in range(3):
                   current_button = buttons[col][row]
                   if current_button['text'] == 'X' or current_button ['text'] == 'O':
                       count += 1
           if count == 9:
               print("Match nul")
                   



           

    def draw_grid():
        for column in range(3):
            buttons_in_col = []
            for row in range(3):
                button = Button(window,bg=bg_code,font=('Arial',70),command=lambda r=row,c=column: place_symbol(r,c))
                button.grid(row=row, column=column,sticky='nsew')
                buttons_in_col.append(button)
            buttons.append(buttons_in_col)
            window.grid_columnconfigure(column, weight=1)  # Colonne proportionnellement
            window.grid_rowconfigure(column, weight=1)     # Ligne proportionnellement
    
    def place_symbol(row, column):
        clicked_button = buttons[column][row]
        if clicked_button['text'] == "":
            clicked_button.config(text=current_player)
        
            check_win(row,column )
            switch_player()
 
        
    buttons = []

    window.title("TicTacToe")
    window.geometry("1080x720")
    window.minsize(300,300)
    window.iconbitmap("jeu.ico")
    bg_code = '#7996BC'
   
    window.config(bg=bg_code)
    draw_grid()
  
    window.mainloop()
   
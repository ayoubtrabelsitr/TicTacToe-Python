from tkinter import *
current_player = 'X'
def main():
    #creation du fenetre de jeu

    window=Tk()
    buttons = []
   
    def switch_player():
        global current_player
        if current_player == 'X':
            current_player = '0'
        else:
            current_player = 'X'

    def check_win(row,column):
       count = 0
       #horizontal 
       for i in range(3):
           current_button = buttons[i][row] 
           if current_button['text'] == current_player:
               count += 1
       if count == 3:
           print("Win Horizontale")   
        #vertical 
       count=0
       for i in range(3):
           current_button = buttons[column][i] 
           if current_button['text'] == current_player:
               count += 1
       if count == 3:
           print("Win Verticale")   
       #diagonale    
       count=0
       for i in range(3):
           current_button = buttons[i][i] 
           if current_button['text'] == current_player:
               count+=1
       if count==3:
           print("Win diagonale ") 
       #diagonale inverse   
       count=0
       for i in range(3):
           current_button = buttons[2 - i][i] 
           if current_button['text'] == current_player:
               count+=1
       if count==3:
           print("Win diagonale Inerse")            
    def draw_grid():
        for column in range(3):
            buttons_in_col = []
            for row in range(3):
                button=Button(window,bg=bg_code,font=('Arial',70),command=lambda r=row,c=column: place_symbol(r,c))
                button.grid(row=row, column=column,sticky='nsew')
                buttons_in_col.append(button)
            buttons.append(buttons_in_col)
            window.grid_columnconfigure(column, weight=1)  # Colonne s'étend proportionnellement
            window.grid_rowconfigure(column, weight=1)     # Ligne s'étend proportionnellement
    
    def place_symbol(row, column):
        clicked_button= buttons[column][row]
        if clicked_button['text'] == "":
            clicked_button.config(text=current_player)
        
            check_win(row,column )
            switch_player()
 
        
    buttons= []
    window.title("TicTacToe")
    window.geometry("1080x720")


    window.minsize(300,300)
    window.iconbitmap("jeu.ico")
    bg_code = '#7996BC'
   
    window.config(bg=bg_code)
    draw_grid()
  

    window.mainloop()
   
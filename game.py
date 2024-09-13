from tkinter import *
def main():
    #creation du fenetre de jeu

    window=Tk()
   
    def draw_grid():
        keys=[True,False,True,False,True,False,True,False,True]
        index=0
        for column in range(3):
            buttons_in_col = []
            for row in range(3):
                button=Button(window,bg=bg_code,font=('Arial',70),command=lambda r=row,c=column,p=keys[index]: place_symbol(r,c,p))
                button.grid(row=row, column=column,sticky='nsew')
                buttons_in_col.append(button)
                index+=1
            buttons.append(buttons_in_col)
            window.grid_columnconfigure(column, weight=1)  # Colonne s'étend proportionnellement
            window.grid_rowconfigure(column, weight=1)     # Ligne s'étend proportionnellement
    
    def place_symbol(row, column,key):
        print("click row: ",row, column)
        clicked_button= buttons[column][row]
        if key:
            clicked_button.config(text="X")
            
        else:
            clicked_button.config(text="O")
        
 
        
    buttons= []
    window.title("TicTacToe")
    window.geometry("1080x720")


    window.minsize(300,300)
    window.iconbitmap("jeu.ico")
    
    bg_code = '#7996BC'
   
    window.config(bg=bg_code)
    draw_grid()
  

    window.mainloop()
   
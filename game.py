from tkinter import *

def main():
    #creation du fenetre de jeu

    window=Tk()

    def draw_grid():
        for i in range(3):
            for j in range(3):
                button=Button(window,bg=bg_code,width=50,height=15)
                button.grid(row=j, column=i)

    window.title("TicTacToe")
    window.geometry("1080x720")


    window.minsize(300,300)
    window.iconbitmap("jeu.ico")
    
    bg_code = '#7996BC'
   
    window.config(bg=bg_code)
    draw_grid()
  

    window.mainloop()
   
from tkinter import *

#creation du fenetre de jeu

root=Tk()

root.title("TicTacToe")
root.geometry("1080x720")
root.minsize(300,300)
root.iconbitmap("jeu.ico")
bg_code = '#4574AC'
root.config(bg=bg_code)

#title
home_title = Label(root,bg=bg_code, text=("Welcome To TicTacToe :)"),font=("Arial",40))
home_title.place(relx=0.5, rely=0.1,anchor='center')

#image
width=height=250
image_home = PhotoImage(file="jeu.png").subsample(2)
canvas = Canvas(root,width=width, height=height,bg=bg_code, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image_home)
canvas.place(relx=0.5, rely=0.4, anchor="center")

#buttons
button_start=Button(root,bg='green',text="Start",font=('Arial',25))
button_start.place(relx=0.5, rely=0.7,anchor='center',relheight=0.1,relwidth=0.1)
button_exit=Button(root,bg='red',text="Exit",font=('Arial',25))
button_exit.place(relx=0.5, rely=0.810,anchor='center',relheight=0.1,relwidth=0.1)

root.mainloop()
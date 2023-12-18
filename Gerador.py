from tkinter import * 
import random 

tela = Tk()
tela.title('Gerador de senhas')
tela.geometry('500x500')

digite = Entry(tela)
digite.place(relx=0.5,rely=0.5,anchor='center')

tela.mainloop()
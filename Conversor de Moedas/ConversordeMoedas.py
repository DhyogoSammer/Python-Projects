from tkinter import * 

tela = Tk()
tela.geometry('600x700')
tela.resizable(False,False)
tela.title('Conversor de Moedas')
tela['bg'] = '#221d21'

cortitle = Label(tela,bg='#221d21', width=100,height=3)
cortitle.pack()


titulo = Label(tela,text='Conversor de Moedas', bg='#221d21', fg='#f77014', font='Arial 20 bold italic', padx='10', pady='10', height=2)
titulo.place(relx=0.5, rely=0.07, anchor='center')

quadro = Frame(tela, bg='#f77014', relief='sunken', bd=10)
quadro.pack(fill='both', expand=True, padx=10, pady=10)

insira_v = Label(tela,text='Insira o valor',bg='#221d21',fg='#f77014', font='Arial 12 bold italic', padx=5, pady=5, relief='sunken')
insira_v.place(relx=0.5, rely=0.18, anchor='center')

insira = Entry(tela)
insira.place(relx=0.5, rely=0.26, anchor='center')

converte_de = Label(tela, text='Opções de Conversão : \n R = Real \n  D = Dolar \nL = Libra',bg='#221d21',fg='#f77014', font='Arial 12 bold italic', padx=5, pady=5, relief='sunken')
converte_de.place(relx=0.5, rely=0.4, anchor='center')

converte = Entry(tela)
converte.place(relx=0.5,rely=0.54, anchor='center')

para = Label(tela,text='Para :',bg='#221d21',fg='#f77014', font='Arial 12 bold italic', padx=5, pady=5, relief='sunken')
para.place(relx=0.5, rely=0.62, anchor='center')

para_entry = Entry(tela)
para_entry.place(relx=0.5, rely=0.68, anchor='center')


#Função 1 

def click():
    insira_e = float(insira.get())
    converte_e = str(converte.get())
    para_e = str(para_entry.get())
    resul = ''
    if converte_e == 'R' or converte_e == 'D' or converte_e == 'L':
        if para_e == 'R' or para_e == 'D' or para_e == 'L':
            if converte_e == 'R' and para_e == 'D' :
                valor = insira_e / 4.98
                resul = f'{valor:.2f}U$'
            elif converte_e == 'D' and para_e == 'R' :
                valor = insira_e * 4.98
                resul = f'{valor:.2f}R$'
            elif converte_e == 'R' and para_e == 'L' :
                valor = insira_e * 0.16
                resul = f'{valor:.2f}GPB'
            elif converte_e == 'L' and para_e == 'R':
                valor = insira_e / 0.16
                resul = f'{valor:.2f}R$'
            elif converte_e == 'D' and para_e == 'L':
                valor = insira_e * 0.82
                resul = f'{valor:.2f}GPB'
            elif converte_e == 'L' and para_e == 'D' :
                valor = insira_e / 0.82
                resul = f'{valor:.2f}U$'
        else:
            resul = 'MOEDA INVALIDA'
    else : 
        resul = 'MOEDA INVALIDA'


    lb1 = Label(tela,text=f'{resul}', font='Arial 24 bold italic', relief='solid', bg='#d4c9ad',fg='#221d21')
    lb1.place(relx=0.5, rely=0.91, anchor='center', width=300, height=95)

butao = Button(tela, text='Calcule',bg='#221d21',fg='#f77014', font='Arial 12 bold italic', padx=5, pady=5, relief='sunken', command=click)
butao.place(relx=0.5, rely=0.78, anchor='center')


tela.mainloop()
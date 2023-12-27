from tkinter import *



tela = Tk() 
tela.geometry('600x600')
tela.resizable(False,False)
tela['bg'] = '#ece1c3'


# Primeira Função 

def selecionar():
    un = v_medidas.get()
    if un == lista_medidas[0]:
        print('Distância Selecionada')
        converte = Label(tela,text='Converter',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        converte.place(relx=0.5,rely=0.5,anchor='center')
        medidas = OptionMenu(tela,v_dist,*dist_medidas)
        medidas.place(relx=0.5,rely=0.6,anchor='center')
        para = Label(tela,text='Para',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        para.place(relx=0.5,rely=0.7,anchor='center')
        medidas_2 = OptionMenu(tela,v_dist,*dist_medidas)
        medidas_2.place(relx=0.5,rely=0.8,anchor='center')
    elif un == lista_medidas[1]:
        print('Temperatura Selecionada')
        converte = Label(tela,text='Converter',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        converte.place(relx=0.5,rely=0.5,anchor='center')
        para = Label(tela,text='Para',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        para.place(relx=0.5,rely=0.7,anchor='center')
        medidas_2 = OptionMenu(tela,v_dist,*dist_medidas)
        medidas_2.place(relx=0.5,rely=0.8,anchor='center')
    elif un == lista_medidas[2]:
        print('Volume Selecionado')
        converte = Label(tela,text='Converter',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        converte.place(relx=0.5,rely=0.5,anchor='center')
        para = Label(tela,text='Para',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
        para.place(relx=0.5,rely=0.7,anchor='center')
        medidas_2 = OptionMenu(tela,v_dist,*dist_medidas)
        medidas_2.place(relx=0.5,rely=0.8,anchor='center')





titulo = Label(tela,text='Conversor de Medidas',font='Ubuntu 26 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
titulo.pack()

selecione = Label(tela,text='Selecione',font='Arial 18 italic bold',fg='#063940',relief='sunken', bg='#8ebdb6')
selecione.place(relx=0.5,rely=0.2,anchor='center')

lista_medidas = ['Distância','Temperatura','Volume']

v_medidas = StringVar()
v_medidas.set(lista_medidas[0]) # Valor Padrão

medidas = OptionMenu(tela,v_medidas,*lista_medidas)
medidas.place(relx=0.5,rely=0.3,anchor='center')

dist_medidas = ['km','hm','dam','m','dm','cm','mm']

v_dist = StringVar() 
v_dist.set(dist_medidas[0]) # Valor Padrão


butao_1 = Button(tela,text='Selecione',command=selecionar)
butao_1.place(relx=0.5,rely=0.4,anchor='center')


tela.mainloop()
from tkinter import *


tela = Tk()
tela.geometry('500x500')
tela.title('Calculadora de IMC')
tela.resizable(False,False)
tela['bg'] = '#5e5953'
caixa1 = Label(tela, text='Calculadora IMC',
               font='Arial 16 bold italic',
               bg='#917c67',
               fg='#ebe7a7',
               relief='sunken',
               padx='10',
               pady='10',
               borderwidth=5,
               border=10
               )
caixa1.pack()



frame = Frame(tela, relief = 'sunken',
              bd = 0, bg = '#5e5953')
frame.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)


caixa2 = Label(frame, text='Valores do IMC Padrão :'
                          ' \n - IMC abaixo de 18,5:'' Abaixo do Peso \n'
                          ' - Entre 18,5 e 25: Peso Ideal \n'
                          ' - 25 até 30: Sobrepeso \n '
                            '- 30 até 40: Obesidade \n' 
                            '- Acima de 40: Obesidade Mórbida',
                    pady='12',
                    padx='12',
                    relief='sunken',
                    bg='#ebe7a7',
                    fg='black',
                    font='Arial 10 bold',
                    borderwidth=5)
altura_A = Label(tela, text='Altura',font='Arial 10 bold', bg='#917c67',fg='#ebe7a7', relief='sunken', padx='5', pady='5', borderwidth=3)
altura_A.place(relx=0.5,rely=0.45,anchor='center')
peso_P = Label(tela, text='Peso', bg='#917c67', font='Arial 10 bold', relief='sunken',fg='#ebe7a7', padx='5', pady='5', borderwidth=3)
peso_P.place(relx=0.5,rely=0.62,anchor='center')




def imc():
    altura = float(alturausu.get())
    peso = float(pesousu.get())
    calc = peso / altura**2
    resul = ''

    if calc < 18.5 :
        resul = 'Você está abaixo do peso \n Se alimente mais'
    elif calc >= 18.5 and calc < 25 :
        resul = 'Você está no peso ideal \n Parabéns!'
    elif calc >= 25 and calc < 30 :
        resul = 'Você está com sobrepeso \n Faça um regime'          
    elif calc >= 30 and calc < 40 :
        resul = 'Você está com obesidade \n Cuidado'
    elif calc >= 40 :
        resul = 'Você está com obesidade mórbida \n Cuidado com sua saúde'

    lb1 = Label(tela,text=f'Seu imc deu {calc:.2f}\n {resul}', bg='#ebe7a7', fg='black', width=100, font='Arial 14 bold italic')
    lb1.place(relx=0.5, rely=0.931, anchor='center')




alturausu = Entry(tela)
alturausu.place(relx=0.5, rely=0.53, anchor='center')
pesousu = Entry(tela)
pesousu.place(relx=0.5, rely=0.7, anchor='center')


butao = Button(tela,text='Calcule',font='Arial 11 bold', bg='#917c67', fg='#ebe7a7', command= imc, borderwidth=5)
butao.place(relx=0.5, rely=0.79, anchor='center')





caixa2.pack()

tela.mainloop()
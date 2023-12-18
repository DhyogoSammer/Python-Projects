import mysql.connector
from mysql.connector import Error 
from tkinter import *
from tkinter import Tk 




def entre():
    try : 
        if login_e.get() != "":
            log = login_e.get()
            sen = senha_e.get()
            con = mysql.connector.connect(host='localhost',database='teste',user='root',password='')

            if con.is_connected():
                db_info = con.get_server_info()
                print('CONEXÃO AO SERVIDOR REALIZADA COM SUCESSO')
                vquery = f"""INSERT INTO login (usuario,senha) VALUES ('{log}','{sen}');"""
                cursor = con.cursor()
                cursor.execute(vquery)
                con.commit()
                print('DADOS GRAVADOS COM SUCESSO')  
 

    except Error as ex :
            print(ex)
    
    finally : 
            if con.is_connected():
                cursor.close()
                con.close()
                print('CONEXÃO FINALIZADA COM SUCESSO')
                login_e.delete(0,END)
                senha_e.delete(0,END) 

    
    janela2 = Toplevel()
    janela2.title('Login Feito')
    janela2.geometry('500x500')
    janela2['bg'] = '#343838'
    janela2.resizable(False,False)
    msg = Label(janela2,text='Login feito com sucesso', font='Times 26 bold italic', bg='#005f6b',fg='#00dffc')
    msg.pack()


    

tela = Tk() 
tela.title('Tela de Login')
tela.geometry('500x500')
tela.resizable(False,False)
tela['bg'] = '#343838'

quadro = Frame(tela,height=300,width=400,bg='#005f6b',relief='sunken')
quadro.place(relx=0.1,rely=0.26)

linha = Label(tela,width=100,bg='#005f6b',relief='sunken')
linha.place(relx=0.5,rely=0.2,anchor='center')

linha2 = Label(tela,width=100,bg='#005f6b',relief='sunken')
linha2.place(relx=0.5,rely=0.92,anchor='center')

titulo = Label(tela,text='Tela de Login', font='Times 26 bold italic', bg='#005f6b',fg='#00dffc', relief='sunken')
titulo.pack()

login = Label(tela,text='Login :' ,font='Times 16 bold italic', bg='#005f6b',fg='#00dffc', relief='sunken', padx=5,pady=5)
login.place(relx=0.2,rely=0.4, anchor='center')

login_e = Entry(tela, width=40)
login_e.place(relx=0.6, rely=0.4, anchor='center',height=29)

senha = Label(tela,text='Senha :'  ,font='Times 16 bold italic', bg='#005f6b',fg='#00dffc', relief='sunken',padx=5,pady=5)
senha.place(relx=0.2,rely=0.6, anchor='center')

senha_e = Entry(tela, width=40,show='*')
senha_e.place(relx=0.6, rely=0.6, anchor='center',height=29)

butao = Button(tela, text='Entrar',font='Times 16 bold italic', bg='#005f6b',fg='#00dffc', relief='sunken', command=entre)
butao.place(relx=0.5,rely=0.8, anchor='center')


tela.mainloop()
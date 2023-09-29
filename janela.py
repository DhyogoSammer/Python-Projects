import customtkinter
import database

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x300')

def clique():
    print('Conexão Feita com Sucesso')

texto = customtkinter.CTkLabel(janela, text='Tela de Login', height=40, width=40)
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Digite seu email aqui')
email.pack(padx=10, pady=10)


senha = customtkinter.CTkEntry(janela, placeholder_text='Digite sua senha aqui', show='*')
senha.pack(padx=10,pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar login')
checkbox.pack(padx=10,pady=10)

botão = customtkinter.CTkButton(janela, text='Login', command=clique)
botão.pack(padx=10,pady=10)

janela.mainloop()
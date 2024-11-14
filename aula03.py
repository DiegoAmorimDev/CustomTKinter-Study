<<<<<<< HEAD
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)



#customizando o tema (aula03)
janela._set_appearance_mode("dark")

=======
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)



#customizando o tema (aula03)
janela._set_appearance_mode("dark")

>>>>>>> c683076286e62ffd22df96fea1c46a1deba89081
janela.mainloop() # rodando a janela
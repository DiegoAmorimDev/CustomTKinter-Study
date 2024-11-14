import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)



#customizando o tema (aula03)
#janela._set_appearance_mode("dark")

# criando nova janela (aula04)
def novaTela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("500x250")
    

btn_novaTela = ctk.CTkButton(master=janela, text="Abrir nova janela", command=novaTela).place(x=300, y=100)


janela.mainloop() 
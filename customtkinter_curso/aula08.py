import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

#aula08 caixas de dialogo

def abrir():
    dialogo = ctk.CTkInputDialog(title="Caixa de dialogo", text="Digite seu login", entry_border_color="blue",
    entry_fg_color="white", button_fg_color="blue", fg_color="#FF9800")
    print("login colhido:", dialogo.get_input())

btn = ctk.CTkButton(janela, text="Abrir caixa de dialogo", command=abrir)
btn.pack()

janela.mainloop()
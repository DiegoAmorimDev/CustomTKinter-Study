import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)


label1 = ctk.CTkLabel(janela, text="menu de opções", font=("arial bold", 20)).pack(pady=20, padx=15)

mes_var = ctk.StringVar(value="Escolha o mes")

def mesF(escolha):
    print(f"o seu mês de nascimento é:", escolha)

mes = ctk.CTkOptionMenu(janela, values=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "outros"], command=mesF, variable=mes_var, 
                        width=250, height=30, corner_radius=20, fg_color="blue", button_color="black", button_hover_color="teal",
                        dropdown_fg_color="blue", dropdown_text_color="white", dropdown_hover_color="teal")
mes.pack(pady=10)


""" outra opção de uso:
mes = ctk.CTkOptionMenu(janela, values=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "outros"], command=mesF)
mes.pack(pady=10)
mes.set("Escolha o mês")

"""




janela.mainloop()
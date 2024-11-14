import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

teste = ctk.CTkLabel(janela, text="digite o seu nome completo", font=("arial bold", 20))
teste.pack(pady=10)

# trabalhando com label de forma dinamica
# 1 forma = introduzindo text por input
"""

teste = ctk.CTkLabel(janela, text="digite o seu nome completo", font=("arial bold", 20))
teste.pack()

text_var = ctk.StringVar(value=input("digite seu nome completo"))

lab = ctk.CTkLabel(janela, textvariable=text_var, width=200, height=25, text_color="black", font=("arial bold", 16))
lab.pack(pady=10)

"""

# 2 forma = introduzindo text por entry

def enviar():
    input = entry.get()
    lab.configure(text=str(input))
    pass

entry = ctk.CTkEntry(janela, width=200, )
entry.pack()

btn = ctk.CTkButton(janela, text="Enviar", width=200, command=enviar).pack(pady=10)

lab = ctk.CTkLabel(janela, text="", text_color="white", font=("arial bold", 16), fg_color="teal", corner_radius=10)
lab.pack(pady=10)


janela.mainloop()
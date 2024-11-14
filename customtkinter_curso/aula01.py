import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela._set_appearance_mode("dark") #tema escuro

btn = ctk.CTkButton(janela, text="Ola")
btn.pack()

janela.mainloop()
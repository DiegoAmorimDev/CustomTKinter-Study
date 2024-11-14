import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)



#aula 05 frames
frame1 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="teal").place(x=10, y=60)
frame2 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="blue").place(x=230, y=60)
frame3 = ctk.CTkFrame(janela, width=200, height=330, fg_color="red", bg_color="transparent", border_width=5, corner_radius=30).place(x=450, y=60)

janela.mainloop()

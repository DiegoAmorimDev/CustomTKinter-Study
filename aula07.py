<<<<<<< HEAD
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

#aula07 usando textbox

textbox = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color="black", scrollbar_button_hover_color="blue", border_width=2,
 corner_radius=20, fg_color="white", border_spacing=15, activate_scrollbars=True)
textbox.pack()

textbox.insert("0.0", "Titulo do texto\n" + "Hello world.\n \n" *20)

=======
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

#aula07 usando textbox

textbox = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color="black", scrollbar_button_hover_color="blue", border_width=2,
 corner_radius=20, fg_color="white", border_spacing=15, activate_scrollbars=True)
textbox.pack()

textbox.insert("0.0", "Titulo do texto\n" + "Hello world.\n \n" *20)

>>>>>>> c683076286e62ffd22df96fea1c46a1deba89081
janela.mainloop()
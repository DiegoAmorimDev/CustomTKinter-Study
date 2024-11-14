<<<<<<< HEAD
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

#aula06 abas

tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=1, border_color="red", fg_color="white", 
segmented_button_fg_color="red", segmented_button_selected_color="blue", segmented_button_unselected_color="red")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("URL")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("URL").grid_columnconfigure(0, weight=1)

#adicionando elementos na tab nomes

text = ctk.CTkLabel(tabview.tab("Nomes"), text="Diego Amorim \n Eduardo Eugenio \n Antonia Mendes")
text.pack()

#adicionando elementos na tab idades

text2 = ctk.CTkLabel(tabview.tab("Idades"), text="19\n23\n45")
text2.pack()

#adicionando elementos na tab URl

text3 = ctk.CTkLabel(tabview.tab("URL"), text="seila.com.br\nseila2.com.br\nseila3.com.br")
text3.pack()

janela.mainloop()
=======
import customtkinter as ctk

janela = ctk.CTk() #criar janela

janela.title("app teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=250)
janela.resizable(width=True, height=False)

#aula06 abas

tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=1, border_color="red", fg_color="white", 
segmented_button_fg_color="red", segmented_button_selected_color="blue", segmented_button_unselected_color="red")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("URL")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("URL").grid_columnconfigure(0, weight=1)

#adicionando elementos na tab nomes

text = ctk.CTkLabel(tabview.tab("Nomes"), text="Diego Amorim \n Eduardo Eugenio \n Antonia Mendes")
text.pack()

#adicionando elementos na tab idades

text2 = ctk.CTkLabel(tabview.tab("Idades"), text="19\n23\n45")
text2.pack()

#adicionando elementos na tab URl

text3 = ctk.CTkLabel(tabview.tab("URL"), text="seila.com.br\nseila2.com.br\nseila3.com.br")
text3.pack()

janela.mainloop()
>>>>>>> c683076286e62ffd22df96fea1c46a1deba89081

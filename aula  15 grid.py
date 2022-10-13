from tkinter import *

janela = Tk()
janela.geometry("400x300+200+200")
lb1 = Label(janela, text="Label1", bg="green")
lb2 = Label(janela, text="Label2", bg="red")
lb3 = Label(janela, text="Label3", bg="yellow")
lb4 = Label(janela, text="Label4", bg="blue")

# por padrão é top
lb1.grid(column=0, row=0)
lb2.grid(column=1, row=1)
lb3.grid(column=1, columnspan=2, row=2)
lb4.grid(column=2, row=3)

janela.mainloop()

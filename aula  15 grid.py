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
lb3.grid(column=1, columnspan=2, row=2, sticky=E)
lb4.grid(column=2, row=3)

janela.mainloop()

# aula 16
janela1 = Tk()
janela1.geometry("200x100+20+20")
lab1 = Label(janela1, text="Usuario: ")
lab2 = Label(janela1, text="Senha: ")
ent1 = Entry(janela1)
ent2 = Entry(janela1)
bt = Button(janela1, text="Entrar")

lab1.grid(column=0, row=0)
lab2.grid(column=0, row=1)
ent1.grid(column=1, row=0)
ent2.grid(column=1, row=1)
bt.grid(column=0, columnspan=2, row=3)
janela1.mainloop()

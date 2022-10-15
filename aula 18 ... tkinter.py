from tkinter import *

janela = Tk()
janela.geometry("200x100+100+100")
lb1 = Label(janela, text="ESPAÇO", bg="green", width="10", height="3")
lbhorizontal = Label(janela, text="horizontal", bg="red")
lbvertical = Label(janela, text="vertical", bg="yellow")


# por padrão é top
lb1.grid(column=0, row=0)
lbhorizontal.grid(column=0, row=1, sticky=E)
lbvertical.grid(column=1, row=0, sticky=N)


janela.mainloop()

# aula 19 rowspan e columnspan


janela = Tk()
janela.geometry("350x200+100+100")
lab1 = Label(janela, text="", bg="red", width="10", height="3")
lab2 = Label(janela, text="", bg="black", width="10", height="3")
lab3 = Label(janela, text="", bg="blue", width="10", height="3")
lab4 = Label(janela, text="", bg="yellow", width="10", height="3")
lab5 = Label(janela, text="", bg="pink", width="4", height="3")
lab6 = Label(janela, text="", bg="green", width="10", height="1")


# por padrão é top
lab1.grid(column=0, row=0)
lab2.grid(column=1, row=0)
lab3.grid(column=0, row=1)
lab4.grid(column=1, row=1)
lab5.grid(column=2, row=0, rowspan=2, sticky=N+S)
lab6.grid(column=0, row=2, columnspan=2, sticky=W+E)


janela.mainloop()

# aulas concluidas
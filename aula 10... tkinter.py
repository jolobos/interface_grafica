# gerenciador de layout pack

#propriedade side
from tkinter import *

janela = Tk()
janela.geometry("400x300+200+200")
lb1 = Label(janela, text="Label1", bg="green")
lb2 = Label(janela, text="Label2", bg="red")
lb3 = Label(janela, text="Label3", bg="yellow")
lb4 = Label(janela, text="Label4", bg="blue")
# por padrão é top
lb1.pack(side=TOP)
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)

janela.mainloop()

# usando anchor
# quando não se expecifica o side, ele assume a propriedade de TOP
janela1 = Tk()
janela1["bg"] = "black"
janela1.geometry("400x300+200+200")

lab1 = Label(janela1, text="side1", bg="white")
lab2 = Label(janela1, text="side2", bg="red")
lab3 = Label(janela1, text="anchor1", bg="white")
lab4 = Label(janela1, text="anchor2", bg="red")

lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(anchor=NW)
lab4.pack(side=BOTTOM, anchor=SW)
janela1.mainloop()
# usando fill
janela2 = Tk()
janela2["bg"] = "black"
janela2.geometry("400x300+200+200")

lab5 = Label(janela2, text="horizontal", bg="white")
lab5.pack(side=TOP, fill=X)
lab6 = Label(janela2, text="horizontal", bg="red")
lab6.pack(side=LEFT, fill=Y)
lab7 = Label(janela2, text="horizontal", bg="red")
lab7.pack(side=RIGHT, fill=Y)

janela2.mainloop()
# usando extend

janela3 = Tk()
labe1 = Label(janela3, text="linha1", bg="white")
labe2 = Label(janela3, text="linha2", bg="yellow")
labe3 = Label(janela3, text="linha3", bg="blue")
labe4 = Label(janela3, text="linha4", bg="green")

labe1.pack(side=TOP, fill=BOTH, expand=1)
labe2.pack(side=TOP, fill=BOTH, expand=1)
labe3.pack(side=TOP, fill=Y, expand=1)
labe4.pack(side=TOP, fill=X, expand=True)

janela3.geometry("500x500+100+100")
janela3.mainloop()

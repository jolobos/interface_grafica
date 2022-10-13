# exercicio com tkinter

from tkinter import *

janela = Tk()
janela.geometry("500x500")


def metd_get():
    if str(text1.get()).isnumeric() and str(text2.get()).isnumeric():
        a = int(text1.get())
        b = int(text2.get())
        label1["text"] = a + b
    else:
        label1["text"] = "valor digitado incorreto"

text1 = Entry(janela)
text1.place(x=200, y=100)
text2 = Entry(janela)
text2.place(x=200, y=120)
botao1 = Button(janela, text="soma", command=metd_get)
botao1.place(x=200, y=140)
label1 = Label(janela, text='')
label1.place(x=200, y=170)
janela.mainloop()

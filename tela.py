import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='digoloko',
    database='testesgbd',
)


def consulta():
    cursor = conexao.cursor()
    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    lista = Label(janela, text='Nome\t\tValor\t\tdescrição')
    lista.grid(column=1, row=4)
    for c, e in enumerate(resultado):
        texto = f'{resultado[c][1]}\t\t{resultado[c][2]}\t\t{resultado[c][3]}'
        lista = Label(janela, text=texto)
        lista.grid(column=1, row=5 + c)


from tkinter import *

# abre a janela
janela = Tk()

# titulo da janela
janela.title('controle de produtos')
# cor do background
'''janela["bg"] = "green"
'''
# tamanho da tela
# referencia(larguraXaltura+distancia da esquerda+distancia do topo,ex:
janela.geometry("800x500+100+100")

# edição da janela
# os tipos de gerenciadores de widges sao place, pack e grid
# place = configura o widge por coordenada x e y(não recomendado)
'''teste1 = Label(janela, text='ola')
teste1.place(x=100, y=100)
'''
# pack = configura o widge por linha horizontal e vertical(pouco recomendado)
# grid = configura o widge por coluna e linha(recomendado)
texto_inicial = Label(janela, text="Tela de produtos")
texto_inicial.grid(column=0, row=0, padx=20, pady=20)

# campo label
texto_lista = Label(janela, text="Lista de produtos:")
texto_lista.grid(column=1, row=1)
# campo butao
botao = Button(janela, text="Selecionar", command=consulta)
botao.grid(column=1, row=3)
# campo caixa de entrada(text)
text1 = Entry(janela)
text1.grid(column=0, row=8)


# um exemplode enviar dao via get


def click_botao1():
    label2["text"] = text2.get()


text2 = Entry(janela)
text2.grid(column=0, row=9)
btn2 = Button(janela, text="click", command=click_botao1)
btn2.grid(column=2, row=9)
label2 = Label(janela, text='')
label2.grid(column=3, row=9)
# manten a janela aberta
janela.mainloop()

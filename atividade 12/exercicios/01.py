from tkinter import *

janela = Tk()
janela.title("SOMADOR")
janela.geometry("200x100+100+100")

#Rótulo e entrada para Valor 1
rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)
campo1 = Entry(janela)
campo1.grid(row=0, column=1)

#Rótulo e entrada para Valor 2
rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)
campo2 = Entry(janela)
campo2.grid(row=1, column=1)

#Rótulo e entrada para SOMA (desabilitada inicialmente)
rotulo3 = Label(janela, text="SOMA =")
rotulo3.grid(row=3, column=0)
campo3 = Entry(janela, state="disabled")  # Inicialmente desabilitado
campo3.grid(row=3, column=1)

#Função de Soma
def somar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    soma = v1 + v2
    campo3.config(state="normal")  # Habilita o campo para editar o valor
    campo3.delete(0, END)
    campo3.insert(0, soma)
    campo3.config(state="disabled")  # Desabilita novamente o campo

#Botão de soma
botao = Button(janela, text="somar", width=14, command=somar)
botao.grid(row=2, column=1)

janela.mainloop()

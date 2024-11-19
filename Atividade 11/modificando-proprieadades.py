from tkinter import *
janela = Tk()

rotulo = Label(janela, text='Olá, mundo!')
rotulo.grid(row=0, column=0)
rotulo["font"] = ('Arial', '18', 'bold', 'italic')
rotulo['fg'] = 'red'
rotulo['bg'] = 'white'

botao_sair = Button(janela)
botao_sair.grid(row=1, column=0)
botao_sair['text'] = 'Sair'
botao_sair['width']= 10
botao_sair['command'] = quit

janela.mainloop()
from tkinter import *

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("250x150+100+100")

# Rótulo e entrada para Valor 1
rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)
campo1 = Entry(janela)
campo1.grid(row=0, column=1)

# Rótulo e entrada para Valor 2
rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)
campo2 = Entry(janela)
campo2.grid(row=1, column=1)

# Rótulo e entrada para Resultado (desabilitado inicialmente)
rotulo3 = Label(janela, text="Resultado:")
rotulo3.grid(row=2, column=0)
campo3 = Entry(janela, state="disabled")  # Inicialmente desabilitado
campo3.grid(row=2, column=1)

# Função genérica para cálculo
def calcular(operacao):
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        if operacao == "soma":
            resultado = v1 + v2
        elif operacao == "subtracao":
            resultado = v1 - v2
        elif operacao == "multiplicacao":
            resultado = v1 * v2
        elif operacao == "divisao":
            if v2 == 0:
                resultado = "Erro: Divisão por 0"
            else:
                resultado = v1 / v2
        else:
            resultado = "Operação Inválida"
    except ValueError:
        resultado = "Erro: Entrada Inválida"
    
    # Atualiza o campo de resultado
    campo3.config(state="normal")  # Habilita o campo para edição
    campo3.delete(0, END)
    campo3.insert(0, resultado)
    campo3.config(state="disabled")  # Desabilita novamente

# Botões para as operações
botao_soma = Button(janela, text="Somar", width=15, command=lambda: calcular("soma"))
botao_soma.grid(row=3, column=0)

botao_subtracao = Button(janela, text="Subtrair", width=15, command=lambda: calcular("subtracao"))
botao_subtracao.grid(row=3, column=1)

botao_multiplicacao = Button(janela, text="Multiplicar", width=15, command=lambda: calcular("multiplicacao"))
botao_multiplicacao.grid(row=4, column=0)

botao_divisao = Button(janela, text="Dividir", width=15, command=lambda: calcular("divisao"))
botao_divisao.grid(row=4, column=1)

janela.mainloop()

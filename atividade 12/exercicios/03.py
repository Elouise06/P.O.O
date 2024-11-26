import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario_correto = "admin"
    senha_correta = "12345"
    
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == usuario_correto and senha == senha_correta:
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")

# Criação da janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# Label e campo de entrada para o usuário
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

# Label e campo de entrada para a senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(janela, show="*")  # O "show='*'" oculta os caracteres digitados
entry_senha.pack(pady=5)

# Botão para verificar o login
botao_entrar = tk.Button(janela, text="Entrar", command=verificar_login)
botao_entrar.pack(pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()

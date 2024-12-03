import tkinter as tk
from tkinter import ttk, messagebox

class BibliotecaApp:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("600x400")
        self.tela_inicial()

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        """Tela inicial com os botões principais."""
        self.limpar_tela()
        tk.Label(self.root, text="Menu Principal", font=("Arial", 16)).pack(pady=20)

        btn_cadastrar = tk.Button(self.root, text="Cadastrar Livro", command=self.tela_cadastro)
        btn_listar = tk.Button(self.root, text="Listar Livros", command=self.tela_listagem)
        btn_buscar = tk.Button(self.root, text="Buscar Livro", command=self.tela_busca)
        btn_sair = tk.Button(self.root, text="Sair", command=self.root.quit)

        btn_cadastrar.pack(pady=10)
        btn_listar.pack(pady=10)
        btn_buscar.pack(pady=10)
        btn_sair.pack(pady=10)

    def tela_cadastro(self):
        """Tela para cadastrar um novo livro."""
        self.limpar_tela()
        tk.Label(self.root, text="Cadastrar Livro", font=("Arial", 16)).pack(pady=10)

        # Campos de entrada
        campos = ["Título", "Autor", "Gênero", "Ano", "Código"]
        entradas = {}
        for campo in campos:
            tk.Label(self.root, text=f"{campo}:").pack(anchor="w", padx=20)
            entrada = tk.Entry(self.root)
            entrada.pack(fill="x", padx=20, pady=5)
            entradas[campo] = entrada

        def salvar():
            dados = {campo: entradas[campo].get() for campo in campos}
            if all(dados.values()):
                self.sistema.adicionar_livro(dados)
                messagebox.showinfo("Sucesso", f"Livro '{dados['Título']}' cadastrado!")
                self.tela_inicial()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

        # Botões
        btn_salvar = tk.Button(self.root, text="Salvar", command=salvar)
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.tela_inicial)

        btn_salvar.pack(side="left", padx=20, pady=20)
        btn_voltar.pack(side="right", padx=20, pady=20)

    def tela_listagem(self):
        """Tela para listar os livros cadastrados."""
        self.limpar_tela()
        tk.Label(self.root, text="Listagem de Livros", font=("Arial", 16)).pack(pady=10)

        # Treeview para exibir os livros
        colunas = ("Código", "Título", "Autor", "Gênero", "Ano")
        tree = ttk.Treeview(self.root, columns=colunas, show="headings")
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Inserir dados na Treeview
        for livro in self.sistema.listar_livros():
            tree.insert("", "end", values=(
                livro["Código"], livro["Título"], livro["Autor"], livro["Gênero"], livro["Ano"]
            ))

        # Botões
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.tela_inicial)
        btn_voltar.pack(side="bottom", pady=10)

    def tela_busca(self):
        """Tela para buscar livros cadastrados."""
        self.limpar_tela()
        tk.Label(self.root, text="Buscar Livro", font=("Arial", 16)).pack(pady=10)

        # Campos de busca
        entradas = {}
        for campo in ["Título", "Autor", "Gênero"]:
            tk.Label(self.root, text=f"{campo}:").pack(anchor="w", padx=20)
            entrada = tk.Entry(self.root)
            entrada.pack(fill="x", padx=20, pady=5)
            entradas[campo] = entrada

        def buscar():
            titulo = entradas["Título"].get()
            autor = entradas["Autor"].get()
            genero = entradas["Gênero"].get()
            resultados = self.sistema.buscar_livro(titulo, autor, genero)

            if resultados:
                self.limpar_tela()
                tk.Label(self.root, text="Resultados da Busca", font=("Arial", 16)).pack(pady=10)

                tree = ttk.Treeview(self.root, columns=("Código", "Título", "Autor", "Gênero", "Ano"), show="headings")
                for col in ("Código", "Título", "Autor", "Gênero", "Ano"):
                    tree.heading(col, text=col)
                    tree.column(col, width=100)
                tree.pack(fill="both", expand=True, padx=10, pady=10)

                for livro in resultados:
                    tree.insert("", "end", values=(livro["Código"], livro["Título"], livro["Autor"], livro["Gênero"], livro["Ano"]))

                btn_voltar = tk.Button(self.root, text="Voltar", command=self.tela_inicial)
                btn_voltar.pack(side="bottom", pady=10)
            else:
                messagebox.showinfo("Busca", "Nenhum livro encontrado!")

        # Botões
        btn_buscar = tk.Button(self.root, text="Buscar", command=buscar)
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.tela_inicial)

        btn_buscar.pack(side="left", padx=20, pady=20)
        btn_voltar.pack(side="right", padx=20, pady=20)

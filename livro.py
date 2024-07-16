class Livro:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano = ""

livro1 = Livro()
livro1.titulo = "1984"
livro1.autor = "george Orwell"
livro1.ano = "1984"
print(livro1.titulo, livro1.autor, livro1.ano)
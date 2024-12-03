# sistema.py

class SistemaBiblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def buscar_livro(self, titulo="", autor="", genero=""):
        return [
            livro for livro in self.livros
            if (titulo.lower() in livro["titulo"].lower() or not titulo) and
               (autor.lower() in livro["autor"].lower() or not autor) and
               (genero.lower() in livro["genero"].lower() or not genero)
        ]

    def buscar_por_codigo(self, codigo):
        for livro in self.livros:
            if livro["codigo"] == codigo:
                return livro
        return None

    def remover_livro(self, codigo):
        self.livros = [livro for livro in self.livros if livro["codigo"] != codigo]

    def editar_livro(self, codigo, novos_dados):
        for livro in self.livros:
            if livro["codigo"] == codigo:
                livro.update(novos_dados)
                break

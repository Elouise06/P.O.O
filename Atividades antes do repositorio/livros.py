class Livros:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacoes(self):
        print("O livro {} do autor {} possui {} páginas".format(self.titulo, self.autor, self.paginas))


livro01 = Livros("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 323)
livro01.informacoes()
livro01.paginas = 223
livro01.informacoes()
print()
print("Livro 01 \nTitulo:{} \nAutor:{} \nPaginas:{}".format(livro01.titulo, livro01.autor, livro01.paginas))

print()

livro02 = Livros("A Culpa é das Estrelas", "John Green", 313)
livro02.informacoes()
print()
print("Livro 02 \nTitulo:{} \nAutor:{} \nPaginas:{}".format(livro02.titulo, livro02.autor, livro02.paginas))

print()

livro03 = Livros("Abused Werewolf-grupo de resgate ao lobsomen", "Catherine Jinks", 437)
livro03.informacoes()
print()
print("Livro 03 \nTitulo:{} \nAutor:{} \nPaginas:{}".format(livro03.titulo, livro03.autor, livro03.paginas))
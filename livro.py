class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

livro1 = Livro("1984", "george Orwell", "1984")
print("O livro {} foi escrito por {} em {}".format(livro1.titulo, livro1.autor, livro1.ano))

livro_elouise = Livro("o mundo de sofia",  "Jostein Gaarder",  "1991")
print("O livro {} foi escrito por {} em {}".format(livro_elouise.titulo, livro_elouise.autor, livro_elouise.ano))
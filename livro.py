class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def info(self):
        print("O livro {} foi escrito por {} no ano {}".format(self.titulo, self.autor, self.ano))

livro1 = Livro("1984", "george Orwell", "1984")
livro1.info()
livro1.ano = 1894
livro1.info()

print()

livro_elouise = Livro("o primo brasilio",  "Eça de Queiroz",  "1878")
livro_elouise.info()
livro_elouise.ano = 1787
livro_elouise.info()
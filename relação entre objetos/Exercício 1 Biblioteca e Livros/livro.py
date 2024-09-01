from autor import Autor
class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setautor(self, autor):
        self.__autor = autor

    def setAnoPublicacao(self, anoPublicacao):
        self.__anoPublicacao = anoPublicacao

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAnoPublicacao(self):
        return self.__anoPublicacao

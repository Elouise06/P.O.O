from autor import Autor

class Livro:
    def __init__(self, titulo: str, autor: Autor, ano_publicacao: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao

    # Getters
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> Autor:
        return self.__autor

    def get_ano_publicacao(self) -> int:
        return self.__ano_publicacao

    # Setters
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autor(self, autor: Autor):
        self.__autor = autor

    def set_ano_publicacao(self, ano_publicacao: int):
        self.__ano_publicacao = ano_publicacao

class Autor:
    def __init__(self, nome: str, nacionalidade: str, data_nascimento: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    # Getters
    def get_nome(self) -> str:
        return self.__nome

    def get_nacionalidade(self) -> str:
        return self.__nacionalidade

    def get_data_nascimento(self) -> str:
        return self.__data_nascimento

    # Setters
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade

    def set_data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

    def exibir_autor(self):
        print(f"Nome: {self.__nome}")
        print(f"Nacionalidade: {self.__nacionalidade}")
        print(f"Data de Nascimento: {self.__data_nascimento}")

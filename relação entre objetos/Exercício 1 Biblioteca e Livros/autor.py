class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento

    def setNome(self, nome):
        self.__nome = nome

    def setNacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def getNome(self):
        return self.__nome

    def getNacionalidade(self):
        return self.__nacionalidade

    def getDataNascimento(self):
        return self.__dataNascimento
    
    def exibirAutor(self):
        print('Dados do Autor:')
        print(f'Nome: {self.__nome}')
        print(f'Nacionalidade: {self.__nacionalidade}')
        print(f'Data de nascimento: {self.__dataNascimento}')
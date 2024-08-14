class Pessoa:
    def __init__(self, nome, endereco, telefone, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

    #getters
    def get_nome(self):
        return(self.__nome)

    def get_endereco(self):
        return(self.__endereco)

    def get_telefone(self):
        return(self.__telefone)

    def get_email(self):
        return(self.__email)

    #Setters
    def set_nome(self,nome):
        self.__nome = nome
        return("Sucesso")

    def set_endereço(self,endereco):
        self.__endereco = endereco
        return ("Sucesso")

    def set_telefone(self,telefone):
        self.__telefone = telefone
        return("Sucesso")

    def set_email(self,email):
        self.__email = email
        return("Sucesso")
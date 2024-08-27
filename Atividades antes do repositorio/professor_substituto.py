from professor_pessoa import *
class Professor_substituto(Professor):
    def __init__(self, nome, endereco, telefone, email, salario, tempo_contrato):
        super().__init__(nome, endereco, telefone, email, salario, tempo_contrato)
        self.__tempo_contrato = tempo_contrato

    def mostrar_professor(self):
        print(self.get_nome())
        print(self.get_email())
        print(self.__tempo_contrato)

professor1 = Professor_substituto("Andriela", "xxxxxxx xxxx", "(xx)xxxxx-xxxx", "princesinhagleice20@gmail.com", "200.000,00")

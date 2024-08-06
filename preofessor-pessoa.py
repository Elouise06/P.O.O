from pessoa import *
class Professor(Pessoa):
    def __init__(self, nome, endereco, telefone, email, salario):
        super().__init__(nome, endereco, telefone, email)
        self.__salario = salario

    def get_salario(self):
        return(self.__salario)

    def set_salario(self, salario):
        self.__salario = salario
        return("Sucesso")

exemplo = Professor("Andriela", "xxxxxxx xxxx", "(xx)xxxxx-xxxx", "princesinhagleice20@gmail.com", "200.000,00")
print(exemplo.get_nome())
print(exemplo.get_endereco())
print(exemplo.get_telefone())
print(exemplo.get_email())
print(exemplo.get_salario())
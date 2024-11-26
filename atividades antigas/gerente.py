from funcionarios  import Funcionario

#classe filha 1 - gerente
class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super()__init__(nome, idade, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        #gerente recebe um bonus de 15% sobre salario
        return self.salario * 0.15

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhe(
            
        )
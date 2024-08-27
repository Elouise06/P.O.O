from funcionarios import Funcionario

# Classe Filha 1 - Gerente
class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        # Gerentes recebem um bônus de 15% sobre o salário
        return self.salario * 0.15

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}, Departamento: {self.departamento}, Bônus: R${self.calcular_bonus():.2f}"
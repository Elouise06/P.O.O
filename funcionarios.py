# Classe Pai
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def exibir_detalhes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}"

    def calcular_bonus(self):
        return 'Implementação específica das classes filha'
from conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, rendimento, saldo=0):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        print(f"Taxa de Rendimento: {self.rendimento * 100:.2f}% ao mês")

    def render(self):
        self.saldo += self.saldo * self.rendimento
        print("Rendimento aplicado com sucesso!")
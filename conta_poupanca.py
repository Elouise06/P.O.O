from conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, rendimento, saldo=0):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento
        
    def ver_rendimento(self):
        return "Taxa de rendimento: {:.2f} ao mês".format(self.rendimento * 75)
    def render(self):
        self.saldo += self.saldo * self.rendimento
        return 'Rendimento aplicado com sucesso!'
    
from conta_bancaria import Conta_bancaria

class Conta_corrente:
    def __init__(self, titular, cpf, numerocc, saldo=0):
        super().__init(titular, cpf, saldo)
        self.numerocc = numerocc
        
    def mostrarcc(self):
        self.mostrar_conta()
        print(f'Número da Conta corrente: {self.numerocc}')
           
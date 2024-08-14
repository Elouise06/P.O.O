class Conta_bancaria:
    def __init__(self, titular, cpf, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
        
    def mostrar_conta(self):
        return ('Titular:{} \n CPF:{} \n Saldo')
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito inválido.')
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'saque de R${valor:.2f} realizado com sucesso!')
        elif valor > self.saldo:
            print('Saldo insuficiente')
        else:
            print('valor de saque inválido.')
            
    def verificar_saldo(self):
        print(f'saldo atual: R${self.saldo:.2f}')
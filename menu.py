from conta_bancaria import Conta_bancaria
from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

print('\n --------MENU--------')
print('1. Criar conta Corrente')
print('2. Criar conta Poupança')
print('3. Depositar')
print('4. Sacar')
print('5. verificar saldo')
print('6. Verificar rendimento (poupança)')
print('7. Aplicar rendimento (poupança)')
print('8. Transferir entre contas Correntes')
print('9. SAIR)')

opcao = []
            
opcao = int(input('Escolha uma opção: '))
while (opcao!= 9): 
    if opcao == 1:
            titular = input('Nome do Titular: ')
            cpf = input('CPF do Titular')
            numerocc = input('Número da conta corrente:')
            conta = Conta_corrente(titular, cpf, numerocc)
            print('Conta Corrente criada com sucesso!')
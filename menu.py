from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

def menu():
    contas_correntes = []
    contas_poupancas = []

    while True:
        print("\n--- Menu do Banco ---")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Poupança")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Verificar Saldo")
        print("6. Verificar Rendimento")
        print("7. Aplicar Rendimento")
        print("8. Transferir entre Contas Correntes")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titular = input("Nome do titular: ")
            cpf = input("CPF: ")
            numerocc = input("Número da Conta Corrente: ")
            conta = Conta_corrente(titular, cpf, numerocc)
            contas_correntes.append(conta)
            print("Conta Corrente criada com sucesso!")

        elif opcao == '2':
            titular = input("Nome do titular: ")
            cpf = input("CPF: ")
            rendimento = float(input("Taxa de Rendimento (em decimal): "))
            conta = Conta_poupanca(titular, cpf, rendimento)
            contas_poupancas.append(conta)
            print("Conta Poupança criada com sucesso!")

        elif opcao == '3':
            cpf = input("CPF do titular: ")
            valor = float(input("Valor para depósito: "))
            for conta in contas_correntes + contas_poupancas:
                if conta.cpf == cpf:
                    conta.depositar(valor)
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == '4':
            cpf = input("CPF do titular: ")
            valor = float(input("Valor para saque: "))
            for conta in contas_correntes + contas_poupancas:
                if conta.cpf == cpf:
                    conta.sacar(valor)
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            cpf = input("CPF do titular: ")
            for conta in contas_correntes + contas_poupancas:
                if conta.cpf == cpf:
                    conta.verificar_saldo()
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == '6':
            cpf = input("CPF do titular: ")
            for conta in contas_poupancas:
                if conta.cpf == cpf:
                    conta.ver_rendimento()
                    break
            else:
                print("Conta Poupança não encontrada.")

        elif opcao == '7':
            cpf = input("CPF do titular: ")
            for conta in contas_poupancas:
                if conta.cpf == cpf:
                    conta.render()
                    break
            else:
                print("Conta Poupança não encontrada.")

        elif opcao == '8':
            cpf_origem = input("CPF do titular da conta de origem: ")
            cpf_destino = input("CPF do titular da conta de destino: ")
            valor = float(input("Valor para transferência: "))
            conta_origem = None
            conta_destino = None

            for conta in contas_correntes:
                if conta.cpf == cpf_origem:
                    conta_origem = conta
                if conta.cpf == cpf_destino:
                    conta_destino = conta

            if conta_origem and conta_destino:
                if conta_origem.saldo >= valor:
                    conta_origem.sacar(valor)
                    conta_destino.depositar(valor)
                    print("Transferência realizada com sucesso!")
                else:
                    print("Saldo insuficiente na conta de origem.")
            else:
                print("Uma ou ambas as contas não foram encontradas.")

        elif opcao == '0':
            print("Saindo do sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
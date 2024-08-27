from funcionarios import Funcionario
from vendedor import Vendedor
from gerente import Gerente

print("***Bem vindo ao RH ***")
print("1) Cadastrar novo funcionário")
print("2) Listar funcionários da empresa")
print("3) SAIR ")

lista_de_funcionarios = []

opcao = int(input("Digite a sua opção: "))
while(opcao != 3):

    #o usuário digitou a opção de cadastrar novo funcionário
    if opcao == 1:
        nome = input("Informe o nome do funcionário: ")
        idade = int(input("Informe a idade do funcionário: ")) 
        salario = float(input("Informe o salário do funcionário: "))
        tipo = int(input("Informe o tipo do funcionário: 1) Gerente  2) Vendedor: "))
        
        if (tipo == 1):
            departamento = input("Informe o departamento do gerente: ")
            funcionario = Gerente(nome, idade, salario, departamento)
            lista_de_funcionarios.append(funcionario)
        elif (tipo == 2):
            comissao = float(input("Informe a comissao do vendedor: "))
            funcionario = Vendedor(nome, idade, salario, comissao)
            lista_de_funcionarios.append(funcionario)
        else:
            print("Tipo inválido")
    
    #o usuário digitou a opção de exibir a listagem de funcionários
    elif opcao == 2:
        for teste in lista_de_funcionarios:
            print(teste.exibir_detalhes())
    
    elif opcao != 3:
        print("Opção inválida!")
    
    print("***Bem vindo ao RH ***")
    print("1) Cadastrar novo funcionário")
    print("2) Listar funcionários da empresa")
    print("3) SAIR ")
    opcao = int(input("Digite a sua opção: "))
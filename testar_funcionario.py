from funcionario import Funcionario
if __name__ == "__main__":
    # Criando objetos com valores iniciais válidos
    funcionario1 = Funcionario("Joooão", "Analista", 3000.00)
    funcionario2 = Funcionario("Maria", "Desenvolvedora", 4500.00)
    funcionario3 = Funcionario("Carlos", "Gerente", 6000.00)

    # Testando getters
    print(funcionario1.get_nome())  # João
    print(funcionario1.get_cargo())  # Analista
    print(funcionario1.get_salario())  # 3000.00

    print(funcionario2.get_nome())  # Maria
    print(funcionario2.get_cargo())  # Desenvolvedora
    print(funcionario2.get_salario())  # 4500.00

    print(funcionario3.get_nome())  #Carlos
    print(funcionario3.get_cargo())  # Gerente
    print(funcionario3.get_salario())  # 6000.00

    # Testando setters com valores válidos
    funcionario1.set_nome("João Silva")
    funcionario1.set_cargo("Analista Sênior")
    funcionario1.set_salario(3500.00)

    print(funcionario1.get_nome())  # João Silva
    print(funcionario1.get_cargo())  # Analista Sênior
    print(funcionario1.get_salario())  # 3500.00

    # Testando setters com valores inválidos
    funcionario1.set_salario(-500.00)  # Erro: O salário deve ser maior que zero.
    funcionario2.set_salario(0)        # Erro: O salário deve ser maior que zero.

from produtos import Produto

def testar_produto():
    # Criando os objetos Produto com valores válidos
    produto1 = Produto("Caneta", 2.50, 10)
    produto2 = Produto("Lápis", 1.00, 20)
    produto3 = Produto("Borracha", 0.75, 30)

    # Tentando definir valores inválidos
    print("\nDefinindo valores inválidos para o produto1:")
    produto1.set_preco(-1.00)
    produto1.set_quantidade(-5)

    # Exibindo os valores dos atributos após tentativas de modificação inválida
    print(f"Nome: {produto1.get_nome()}, Preço: {produto1.get_preco()}, Quantidade: {produto1.get_quantidade()}")

    print("\nDefinindo valores inválidos para o produto2:")
    produto2.set_preco(0)
    produto2.set_quantidade(-1)

    print(f"Nome: {produto2.get_nome()}, Preço: {produto2.get_preco()}, Quantidade: {produto2.get_quantidade()}")

    print("\nDefinindo valores inválidos para o produto3:")
    produto3.set_preco(-0.75)
    produto3.set_quantidade(-10)

    print(f"Nome: {produto3.get_nome()}, Preço: {produto3.get_preco()}, Quantidade: {produto3.get_quantidade()}")

if __name__ == "__main__":
    testar_produto()

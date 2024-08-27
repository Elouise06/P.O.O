class Protudo:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

protudo1 = Protudo("Notebook", 3800.00, 10)
print("Protudo 1: \nNome:{} \nPreço:{} \nQuantidade em estoque:{}".format(protudo1.nome, protudo1.preço, protudo1.quantidade))

print()

protudo2 = Protudo("Mouse", 50.00, 100)
print("Protudo 2: \nNome:{} \nPreço:{} \nQuantidade em estoque:{}".format(protudo2.nome, protudo2.preço, protudo2.quantidade))
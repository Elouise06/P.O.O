class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

animal1 = Animal("Rex", "Cachorro", 4)
print("Animal 1: \nNome:{} \nEspécie:{} \nIdade:{}".format(animal1.nome, animal1.especie, animal1.idade))

print()

animal2 = Animal("Mimosa", "Gato", 5)
print("Animal 1: \nNome:{} \nEspécie:{} \nIdade:{}".format(animal2.nome, animal2.especie, animal2.idade))
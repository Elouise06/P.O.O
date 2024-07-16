class veiculo:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

carro1 = veiculo('voyage', 'Volkswagen', 2015)
print("O carro de modelo {}, da marca {}, foi lançado em {} ".format(carro1.modelo, carro1.marca, carro1.ano))

print()

carro2 = veiculo('Ford Ka', 'Ford', 2018)
print("O carro de modelo {}, da marca {}, foi lançado em {} ".format(carro2.modelo, carro2.marca, carro2.ano))
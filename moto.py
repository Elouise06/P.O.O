class Moto:
    def __init__(self, marca, modelo, cilindradas):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas

    def dados(self):
        print("A moto {} possui {} cilindradas".format(self.modelo, self.cilindradas))


moto1 = Moto("Honda", "Honda CB 500F", 500)
moto1.dados()
print()
print("Moto 1 \nMarca:{} \nModelo:{} \nCilindradas:{}".format(moto1.marca, moto1.modelo, moto1.cilindradas))

print()

moto2 = Moto("Yamaha", "Yamaha YZF-R6", 600)
moto2.dados()
print()
print("Moto 2 \nMarca:{} \nModelo:{} \nCilindradas:{}".format(moto2.marca, moto2.modelo, moto2.cilindradas))
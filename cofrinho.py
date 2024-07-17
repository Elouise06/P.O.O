class Cofrinho:
    def __init__(self, valor, meta):
        self.valor = valor
        self.meta = meta

    def adicionar(self, quantia):
        self.valor = self.valor + quantia

    def falta(self):
        x = self.meta - self.valor
        print("falta {} para os {} da sua meta".format(x, self.meta))

meta_ise= Cofrinho(7000, 20000)
meta_ise.adicionar(400)
meta_ise.falta()

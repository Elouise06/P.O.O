class Numero:
    def __init__(self, num, ante, dob, tri, met):
        self.num = num
        self.ante = ante
        self.dob = dob
        self.tri = tri
        self.met = met
  
    def sucessor(self):
        valor = self.num + 1
        print('O sucessor de', self.num, ' é ', valor )

    def antecessor(self):
        valorant = self.num -1
        print('O antecessor de', self.num, ' é ', valorant )

    def dobro(self):
        valordob = self.num *2
        print('O Dobro de', self.num, ' é ', valordob )

    def triplo(self):
        valortri = self.num *3
        print('O Triplo de', self.num, ' é ', valortri )

    def metade(self):
        valormet = self.num /2
        print('A metade de', self.num, ' é ', valormet )


sucessor = Numero()
sucessor.sucessor()
print('O sucessor de', sucessor.num, ' é {}'.format(sucessor.sucessor)  )

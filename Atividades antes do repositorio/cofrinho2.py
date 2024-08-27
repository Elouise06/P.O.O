class Cofrinho:
    def __init__(self, valor, meta):
        self.__valor = valor
        self.meta = meta

    def getvalor(self):
        return self.__valor
    def setvalor(self, valor):
        if valor >= 0:
            self.__valor = valor    
    
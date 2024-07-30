class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        
    def setDia(self, dia):
        if dia >= 1 and dia <=31:
            self.__dia = dia
            
    def escreverData(self):
        print("{}/{}/{}".format(self.__dia, self.__mes, self.__ano))
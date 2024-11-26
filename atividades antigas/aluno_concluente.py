from aluno_cursando import *
class Aluno_concluente(Aluno_cursando):
    def __init__(self, matricula, nome, curso, data_concluir, emitiu_certificado):
        super().__init__(matricula, nome, curso, data_concluir, emitiu_certificado)
        self.__data_concluir = data_concluir
        self.__emitiu_certificado = emitiu_certificado

    def get_data_concluir(self):
        return(self.__data_concluir)

    def get_emitiu_certificado(self):
        return(self.__emitiu_certificado)

    def set_data_concluir(self, data_concluir):
        self.__data_concluir = data_concluir

    def set_emitiu_certificado(self, emitiu_certificado):
        self.__emitiu_certificado = emitiu_certificado


aluno_concluir = Aluno_concluente("20231041110026", "Andriela", "Informática", "2026", "11/01/2027")
print(aluno_concluir.get_matricula())
print(aluno_concluir.get_nome())
print(aluno_concluir.get_curso())
print(aluno_concluir.get_data_concluir())
print(aluno_concluir.get_emitiu_certificado())
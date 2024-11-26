from aluno1 import *
class Aluno_cursando(Aluno):
    def __init__(self, matricula, nome, curso, ano_atual, ano_concluir):
        super().__init__(matricula, nome, curso)
        self.__ano_atual = ano_atual
        self.__ano_concluir = ano_concluir

    def get_ano_atual(self):
        return(self.__ano_atual)

    def set_ano_atual(self, ano_atual):
        self.__ano_atual = ano_atual

    def get_ano_concluir(self):
        return(self.__ano_concluir)

    def set_ano_concluir(self, ano_concluir):
        self.__ano_concluir = ano_concluir

aluno1 = Aluno_cursando("20231041110026", "Andriela", "Informática", "2024", "2026")
print(aluno1.get_matricula())
print(aluno1.get_nome())
print(aluno1.get_curso())
print(aluno1.get_ano_atual())
print(aluno1.get_ano_concluir())
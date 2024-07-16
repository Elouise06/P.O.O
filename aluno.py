class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

aluno1 = Aluno("Maria José", "Informática", "1o ano")
print("Nome:{} \nCurso:{} \nSerie:{}".format(aluno1.nome, aluno1.curso, aluno1.serie))

print()

aluno2 = Aluno("Carlos Felipe", "Eletrônica", "3o ano")
print("Nome:{} \nCurso:{} \nSerie:{}".format(aluno2.nome, aluno2.curso, aluno2.serie))

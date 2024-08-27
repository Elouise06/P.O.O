class Funcionario:
    def __init__(self, nome, cargo, salario):
        self._nome = nome
        self._cargo = cargo
        self.set_salario(salario)
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_cargo(self):
        return self._cargo
    
    def set_cargo(self, cargo):
        self._cargo = cargo
    
    def get_salario(self):
        return self._salario
    
    def set_salario(self, salario):
        if salario > 0:
            self._salario = salario
        else:
            print("Erro: O salário deve ser maior que zero.")
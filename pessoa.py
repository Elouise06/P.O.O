class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)  # Usar o método set_idade para garantir validação na criação

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade is None:
            idade = 0  # Definindo um valor padrão caso a idade seja None
        elif not isinstance(idade, int):
            idade = 0  # Definindo um valor padrão caso o tipo da idade não seja inteiro
        elif idade < 0:
            idade = 0  # Definindo um valor padrão para idades negativas
        elif idade > 120:
            idade = 120  # Ajustando a idade para o máximo permitido

        self._idade = idade

# Exemplo de uso
p = Pessoa("João", 30)
print(p.get_idade())  # Saída: 30

p.set_idade(-5)
print(p.get_idade())  # Saída: 0 (idade negativa é ajustada para 0)

p.set_idade("trinta")
print(p.get_idade())  # Saída: 0 (idade inválida é ajustada para 0)

p.set_idade(150)
print(p.get_idade())  # Saída: 120 (idade acima do máximo é ajustada para 120)
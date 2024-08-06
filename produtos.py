class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def get_preco(self) -> float:
        return self._preco

    def set_preco(self, preco: float) -> None:
        if preco > 0:
            self._preco = preco
        else:
            print("Erro: O preço deve ser maior que zero.")

    def get_quantidade(self) -> int:
        return self._quantidade

    def set_quantidade(self, quantidade: int) -> None:
        if quantidade >= 0:
            self._quantidade = quantidade
        else:
            print("Erro: A quantidade deve ser um número inteiro não negativo.")
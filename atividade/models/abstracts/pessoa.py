from abc import ABC, abstractmethod
from models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"Pessoa: "
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n\nEndereço: {self.endereco}"
        )
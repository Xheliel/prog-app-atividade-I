from models.abstracts.pessoa import Pessoa
from models.endereco import Endereco  

class Juridico(Pessoa):
    def __init__(self, cnpj: str, inscricao_estadual: str, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(id, nome, idade, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nPESSOA JURÍDICA\n"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}\n"
        )
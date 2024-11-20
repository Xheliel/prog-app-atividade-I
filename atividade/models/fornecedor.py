from models.abstracts.juridica import Juridico
from models.endereco import Endereco

class Fornecedor(Juridico):
    def __init__(self, produto: str,cnpj: str, inscricao_estadual: str, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(cnpj, inscricao_estadual, id, nome, idade, telefone, email, endereco)
        self.produto = produto

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nPRODUTO\n"
            f"\nProduto: {self.produto}"
        )
    
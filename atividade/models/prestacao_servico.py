from models.abstracts.juridica import Juridico

class Fornecedor(Juridico):
    def __init__(self, produto: str, nome, telefone, email, endereco, cnpj, inscricao_estadual):
        super().__init__(nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.produto = produto

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nProduto: {self.produto}"
        )
    
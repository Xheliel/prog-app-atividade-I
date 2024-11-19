from models.abstracts.juridica import Juridico

class Fornecedor(Juridico):
    def __init__(self, contrato_inicio: str, contrato_fim: str, nome, telefone, email, endereco, cnpj, inscricao_estadual):
        super().__init__(nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nInício do contrato: {self.contrato_inicio}"
            f"\nFim do contrato: {self.contrato_fim}"
        )
    
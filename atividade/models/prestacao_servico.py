from models.abstracts.juridica import Juridico
from models.endereco import Endereco

class PrestacaoServico(Juridico):
    def __init__(self, contrato_inicio: str, contrato_fim: str, cnpj: str, inscricao_estadual: str, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(cnpj, inscricao_estadual, id, nome, idade, telefone, email, endereco)
        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nPRESTAÇÃO DE SERVIÇO\n"
            f"\nInício do contrato: {self.contrato_inicio}"
            f"\nFim do contrato: {self.contrato_fim}"
        )
    
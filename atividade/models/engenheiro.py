from models.endereco import Endereco
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.abstracts.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, crea: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, sexo: Sexo, data_nascimento: str, estado_civil: EstadoCivil, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(cpf, rg, matricula, setor, salario, sexo, data_nascimento, estado_civil, id, nome, idade, telefone, email, endereco)
        self.crea = crea

    def __str__(self):
        return (
            f"\n{super().__str__()}\n"
            f"\nCREA: {self.crea}"
        )
from abc import ABC
from models.abstracts.fisica import Fisica
from enums.setor import Setor
from enums.sexo import Sexo
from enums.estado_civil import EstadoCivil
from models.endereco import Endereco

class Funcionario(Fisica, ABC):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, sexo: Sexo, data_nascimento: str, estado_civil: EstadoCivil, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(sexo, data_nascimento, estado_civil, id, nome, idade, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self):
        return {
            f"\n{super().__str__()}\n"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalário: {self.salario}"
        }
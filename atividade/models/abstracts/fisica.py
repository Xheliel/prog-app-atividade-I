from models.abstracts.pessoa import Pessoa
from models.endereco import Endereco  
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo

class Fisica(Pessoa):
    def __init__(self, sexo: Sexo, data_nascimento: str, estado_civil: EstadoCivil, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(id, nome, idade, telefone, email, endereco)
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"FISÍCA\n"
            f"\nSexo: {self.sexo.nome} - {self.sexo.sigla}"
            f"\nData de nascimento: {self.data_nascimento}"
            f"\nEstado civil: {self.estado_civil.value}"
        )

    
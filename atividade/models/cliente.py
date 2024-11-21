from models.endereco import Endereco  
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.abstracts.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, protocolo_atendimento: int, sexo: Sexo, data_nascimento: str, estado_civil: EstadoCivil, id: int, nome: str, idade: int, telefone: str, email: str, endereco: Endereco):
        super().__init__(sexo, data_nascimento, estado_civil, id, nome, idade, telefone, email, endereco)
        self.protocolo_atendimento = protocolo_atendimento

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Protocolo de Atendimento: {self.protocolo_atendimento}"
        )


    
from enum import Enum

class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Jurídico"

print(Setor.ENGENHARIA.value)
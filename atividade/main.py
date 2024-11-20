from models.endereco import Endereco
from models.enums.unidade_federal import UnidadeFederativa
from models.abstracts.juridica import Juridico
import os

os.system("clear || cls")

endereco1 = Endereco("X XXXX XXXX", "XXX", "X XXXXX", "XXXXX-XXX", "XXXXXXXX", UnidadeFederativa.BAHIA)
juridico1 = Juridico("XXXXX", "XXXXX", 1, "XXXXXXXX", 18, "XX XXXXX XXXX", "XXXXX@XXXXX.XXX", endereco1)

print(juridico1)

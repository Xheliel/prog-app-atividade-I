from models.endereco import Endereco
from models.enums.unidade_federal import UnidadeFederativa
from models.abstracts.juridica import Juridico
import os

os.system("clear || cls")

endereco1 = Endereco("X XXXX XXXX", "XXX", "X XXXXX", "XXXXX-XXX", "XXXXXXXX", UnidadeFederativa.BAHIA)
juridico1 = Juridico("XXXX", "XX XXXXX XXXX", "XXXXXXX@XXXXX.XXX", endereco1, "XXXXXXXXXXX", "XXXXX")

print(juridico1)

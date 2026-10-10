import json
from Veiculo import Veiculo
from Combustivel import Combustivel
from Veiculo import Veiculo

etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")


with open ("recibo_posto.txt"), "w" as arquivo:


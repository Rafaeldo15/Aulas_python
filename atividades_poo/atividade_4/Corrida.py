from abc import ABC, abstractmethod

print ("Iniciando operação")

class Valores():
    def __init__(self, valor_km: float, valor_tempo: float):
        self.valor_km = valor_km
        self.valor_tempo = valor_tempo

    def exibir_resumo(Self):
        print(f"Taxa por KM: R$ {self.valor_km}\n"
              f"Taxa por Minuto: R$ {self.valor_tempo:.2f}")

class Corrida (ABC):
    @abstractmethod
    def calcular_valor(self):
        pass


def ValorCorrida (Valores):
    return Valores

def exibir_resumo ():
    print (f"o valor do km é {valor_km} e tempo é {valor_tempo}")


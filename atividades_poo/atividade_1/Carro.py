class Carro:
    def __init__(self, marca, modelo, ano, potencia, aceleracao):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.potencia = potencia
        self.aceleracao = aceleracao

   # def MostrarCarro(self):
        #print(self.marca, self.modelo, self.ano, self.potencia, self.aceleracao)

    def __str__(self):
        return (f"\tMarca  {self.marca}\n"
                f"\tModelo {self.modelo}\n"
                f"\tFabricação {self.ano}\n"
                f"\tPotência {self.potencia}\n"
                f"\tAceleracao {self.aceleracao} segundos"
                )

carro1= Carro(
    "Volks",
    "gol",
    "1998",
    "1.0 aspirado",
    "12.5"
)

carro2 = Carro(
    "Chevrolet",
    "onix",
    "2012",
    "1.0 aspirado",
   "15.0"
)
carro3 = Carro(
    "toyota",
    "corolla",
    "2015",
    "2.0 aspirado",
    "8.5"

)

print(carro1)
print("")
print(carro2)
print("")
print(carro3)

#carro4=Carro(
    #input("digite a marca do carro 4:"),
    #input("digite a modelo do carro 4:"),
    #input("digite a ano do carro 4:"),
    #input("digite a potencia do carro 4:"),
    #input("digite a aceleracao do carro 4:")
#)

#print("")
#print(carro4)

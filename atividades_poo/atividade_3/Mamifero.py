from Animal import Animal


class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    def correr (self):
        print (f"`{self.nome} correu na velocidade de {self.__velocidade_kmh} kmh!")
        self.nivel_fome += 15

    def emitir_som(self):
        print (f"O {self.nome} ruge alto!")

from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_fome)
        self.envergadura_asas = envergadura_asas

    def voar (self):
        if self.nivel_fome <= 80:
            print (f"{self.nome} Voo com sua asa de envergadura de {self.envergadura_asas} centímetros.")
            self.nivel_fome += 15
        else:
            print (f"{self.nome} esta faminto demais para voar. seu nível de fome está {self.nivel_fome}")


    def emitir_som(self):
        print (f"{self.nome} canta uma maravilhosa melodia")
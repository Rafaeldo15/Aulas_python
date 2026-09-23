from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, nivel_de_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_de_fome)
        self.envergadura_asas = envergadura_asas


from Animal import Animal


class Mamifero(Animal):
    def __init__(self,velocidade_kmh):
        self.__velocidade_kmh = velocidade_kmh

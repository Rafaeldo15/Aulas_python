class Coordenacao:
    def __init__(self, professores, cursos, alunos):
        self.__professores = professores
        self.__cursos = cursos
        self.__alunos = alunos

    @property
    def cursos(self):
        return self.__cursos

    @property
    def professores(self):
        return self.__professores
    @property
    def alunos(self):
        return self.__alunos

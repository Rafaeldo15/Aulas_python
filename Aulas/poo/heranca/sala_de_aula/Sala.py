from Aulas.poo.heranca.diretoria.Coordenacao import Coordenacao


class Sala (Coordenacao):
    def __init__(self, laboratorio, tipo, professores, cursos, alunos):
        super().__init__(professores, cursos, alunos)
        self.laboratorio = laboratorio
        self.tipo = tipo

    def ter_aula(self):
        print (f"Aula de {self.cursos}"
               f"no laboratorio de {self.laboratorio}"
               f"\n com o professor de {self.professores}"
               f"\n com os alunos: {self.alunos}"

               )

sala_1= Sala(
    "Lab 7",
    "tecnologia",
    "joao",
    "python",
    [
        "Fulano",
        "Ciclano"
        "Beltrano"
    ])
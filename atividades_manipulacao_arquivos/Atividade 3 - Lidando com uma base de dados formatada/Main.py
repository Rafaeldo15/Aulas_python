#criando função acrescentar aluno
def acrescentar_aluno():
    Nome = input("Digite o nome do aluno a ser adicionado: ")
    Turma = input("Digite o número da turma a ser adicionado: ")
    Bim1 = float(input("Digite a primeira nota do aluno: "))
    Bim2 = float(input("Digite a segunda nota do aluno: "))
    Bim3 = float(input("Digite a terceira nota do aluno: "))
    Bim4 = float (input("Digite a quarta nota do aluno: "))
    Status = (Bim1 + Bim2 + Bim3 + Bim4) / 4
    if Status >= 7.0:
            print ("\nAprovado\n\n")
    else:
            print ("\nReprovado\n\n")

    with open("Alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{Nome};{Turma};{Bim1},{Bim2},{Bim3},{Bim4},{Status}\n")


while True:
    finalizar = False
    print ("Sistema de Gestão de Alunos")
    opcao = int(input("Escolha uma das opções abaixo\n\n"
                      "1) Acrescentar Aluno\n"
                      "2) Procurar média de aluno(digite o nome do aluno)\n"
                      "3) Verificar STATUS\n"
                      "4) Mostrar maior média da turma\n"
                      "5) Encerrar programa\n"
                      ))
    match opcao:
        case 1:
            acrescentar_aluno()
        case _:
            print("Finalizando sistema...")
            finalizar = True
            break
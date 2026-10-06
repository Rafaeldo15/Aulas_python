#criando função acrescentar aluno



def acrescentar_aluno():
    nome = input("Digite o nome do aluno a ser adicionado: ")
    turma = input("Digite o número da turma a ser adicionado: ")
    bim1 = float(input("Digite a primeira nota do aluno: "))
    bim2 = float(input("Digite a segunda nota do aluno: "))
    bim3 = float(input("Digite a terceira nota do aluno: "))
    bim4 = float (input("Digite a quarta nota do aluno: "))
    media = (bim1 + bim2 + bim3 + bim4) / 4
    if media >= 7.0:
        print ("\nAprovado\n\n")
        status = "Aprovado"
    else:
        print ("\nReprovado\n\n")
        status = "Reprovado"

    with open("Alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};"
                      f"{turma};"
                      f"{bim1};"
                      f"{bim2};"
                      f"{bim3};"
                      f"{bim4};"
                      f"{status}\n")

def lista_nome_alunos():
    with open("Alunos.txt", "r", encoding="utf-8") as arquivo:
        lista_alunos = arquivo.readlines()
        for aluno in lista_alunos:
            aluno = aluno.strip()
            aluno = aluno.split(";")
            nome = aluno[0]
            print(nome)


def verificar_status_aluno():
    nome_busca = input("\nDigite o nome do aluno: ").strip()
    aluno_encontrado = False

    with open("Alunos.txt", "r", encoding="utf-8") as arquivo:
        status_aluno = arquivo.readlines()

        for status in status_aluno:
            dados = status.strip().split(";")

            if dados[0].strip() == nome_busca:
                print(f"\n{dados[0]} está {dados[6]}")
                aluno_encontrado = True
                break

    if aluno_encontrado == False:
        print("\nAluno não encontrado, tente novamente.")


def maior_media():
    turma_digitada = input("Digite o número da turma: ").strip()

    # Variáveis para guardar os dados do aluno com a maior média
    maior_media_encontrada = -1.0
    aluno_maior_media = None

    with open("Alunos.txt", "r", encoding="utf-8") as arquivo:
        lista_alunos = arquivo.readlines()

        for linha in lista_alunos:
            # Ignora linhas vazias, se houver
            if not linha.strip():
                continue

            aluno = linha.strip().split(";")

            # Supondo a estrutura: Nome;Turma;Nota1;Nota2;Nota3;Nota4
            # Ajuste os índices [0] e [1] abaixo se a ordem do seu arquivo for diferente!
            nome = aluno[0]
            turma_aluno = aluno[1].strip()

            # Verifica se o aluno pertence à turma digitada
            if turma_aluno == turma_digitada:
                # Calcula a média das 4 notas (índices 2, 3, 4 e 5)
                media = (float(aluno[2]) + float(aluno[3]) + float(aluno[4]) + float(aluno[5])) / 4

                # Se esta média for maior que a maior encontrada até agora, atualiza
                if media > maior_media_encontrada:
                    maior_media_encontrada = media
                    aluno_maior_media = nome

    # Exibe o resultado após ler o arquivo completo
    if aluno_maior_media is not None:
        print(
            f"\nO aluno com a maior média na turma {turma_digitada} é {aluno_maior_media} com a média {maior_media_encontrada:.2f}")
    else:
        print(f"\nNenhum aluno encontrado para a turma {turma_digitada}.")

while True:

    print ("\nSistema de Gestão de Alunos\n")
    opcao = int(input("\t=====Escolha uma das opções abaixo=====\n"
                      "1) Acrescentar Aluno\n"
                      "2) Listar alunos\n"
                      "3) Verificar status de aluno\n"
                      "4) Mostrar maior média da turma\n"
                      "5) Encerrar programa\n"
                      "Digite:"
                      ))
    match opcao:
        case 1:
            acrescentar_aluno()
        case 2:
            lista_nome_alunos()
        case 3:
            verificar_status_aluno()
        case 4:
            maior_media()


        case _:
            print("Finalizando sistema...")

            break
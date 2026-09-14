def aluno():
    return "rafael"


def nota ():
    nota1= float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"{aluno()}você teve média maior que 7 e foi aprovado")
    else:
        print(f"{aluno()} você teve média menor que 7 e foi reprovado")

    return print(f"{aluno()} suas notas: ", nota1, nota2, nota3, nota4,"e a media foi de:", media)

aluno()
nota()

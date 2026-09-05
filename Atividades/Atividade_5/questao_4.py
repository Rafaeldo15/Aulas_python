nome = input("Digite seu nome: ")
print("")
print (f"{nome} seja bem vindo a nossa agência de viagens.")
print("")
print("Aqui você irá descobrir qual estação do ano estará o seu lugar favorito no mês da sua viagem")
print("")
mes= int(input("Digite aqui (em número) o mês que você pretende viajar: "))
#criando uma história além dos códigos...
print("")
match mes:
    case 12 | 1 | 2:
        print(f"{nome} você irá aproveitar belos dias de sol. Este mês será VERÃO")
    case 3 | 4 | 5:
        print(f"{nome} você irá desfrutar de um clima ameno, dias de sol e menos chuva. Este mês será OUTONO")
    case 6 | 7 | 8:
        print(f"{nome} leve agasalho e prepare-se para o frio. Este mês será INVERNO")
    case 9 | 10 | 11:
        print(f"{nome} clima ameno, provavelmente um pouco de chuva e sol. este mês será PRIMAVERA")
    case _:
        print("Mês inválido, tente outra vez.")
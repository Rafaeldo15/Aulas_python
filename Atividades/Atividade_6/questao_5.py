numero_palpite = int(input("digite um numero inteiro: "))
inicio= 0

while True:
    resultado= numero_palpite * inicio
    print(f"{numero_palpite}*{inicio} = {resultado}")
    inicio += 1


    if inicio == 11:
        break





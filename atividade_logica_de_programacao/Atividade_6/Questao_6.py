numero_secreto= 5
numero_digitado = int(input("Digite um palpite:  "))

while numero_digitado != numero_secreto:
    numero_digitado = int(input("Número incorreto, digite novamente: "))
    numero_tentativas = (numero_digitado + 1) - 1
print(f"Parabéns você acertou o número secreto que era [{numero_secreto}] após [{numero_tentativas}] tentativas")


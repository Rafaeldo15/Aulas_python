soma = 0
numero = int(input("Digite um número: "))

while numero != 0:
    soma += numero
    numero = int(input("Número incorreto, digite novamente: "))


print(f"A soma de todos os números digitados é: {soma}")
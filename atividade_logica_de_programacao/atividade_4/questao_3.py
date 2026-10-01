#sabendo que no Brasil o voto, entre 16 e 18 anos não é obrigatorio mas permitido
#a partir de 18 obrigatorio. decidi inserir mais uma condição

print ("Seja bem vindo(a) ao validador de idade.")
min = 18
nome= input("Digite seu nome: ")

idade_real= int(input("Insira sua idade: "))
if idade_real > min:
    print(f"{nome} você é obrigado a votar!")

elif idade_real >=16 and idade_real <18:
    print (f"{nome} você poderá votar, mas não é obrigado.")

else:
    print(f"{nome} você não poderá votar este ano.")

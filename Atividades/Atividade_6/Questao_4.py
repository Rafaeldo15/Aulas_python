print("1- mostrar saudação")
print("2- sair do programa")
num= str(input("digite um número "))

while num != "1"  and num != "2":
    print("Opção incorreta, tente novamente")
    num = str(input("digite novamente um número "))

if num == "1":
        print ("Olá, seja muito bem vindo")

elif num == "2":
        print ("Saindo")

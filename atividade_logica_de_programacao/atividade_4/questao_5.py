idade= int(input("Digite sua idade: "))
vip= int(input("você é VIP? Digite 1 para sim 0 para nao: "))
org= int(input("voce é organizador? Digite 1 para sim 0 para nao: "))

if idade >= 18 or vip == 1 or org == 1:
    print("Você pode entrar")

else:
    print("você não pode entrar")

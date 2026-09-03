nome=str(input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))
plano_1=input("você tem plano de saude? (false ou true) ")
plano= plano_1 == "true"

print(f"{nome} você pode participar do formulario: {idade>= 18 and idade <= 70  and plano == True}")
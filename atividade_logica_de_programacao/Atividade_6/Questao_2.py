senha = 1234
acesso= int(input("digite sua senha: "))

while acesso != senha:
    print("sua senha esta incorreta, tente novamente")
    acesso = int(input("digite sua senha: "))

    if acesso == senha:
        print("sua senha esta correta")

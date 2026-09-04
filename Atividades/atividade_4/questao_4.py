saldo_atual = 600.00
saque = float(input("digite o valor do saque: "))

if saque < saldo_atual:
    saldo_atual = (saldo_atual - saque)
    print("Saque realizado com sucesso. saldo atual: ",saldo_atual)

else:
    print("Saldo insuficiente")
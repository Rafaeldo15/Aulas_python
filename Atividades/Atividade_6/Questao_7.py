orcamento = float(input("Digite o valor do orcamento: "))

while orcamento > 0:

    gasto= float(input("Digite o valor do gasto: "))
    orcamento -= gasto

print (f"Voce ficou sem saldo ou ultrapassou o orçamento. o valor ficou em :  {orcamento:.2f} ")



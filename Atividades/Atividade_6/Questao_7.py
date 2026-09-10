orcamento = float(input("Digite o valor do orcamento: "))

while orcamento >=0:

    gasto= float(input("Digite o valor do gasto: "))
    resultado = orcamento - gasto

print(resultado)

    if resultado <= 0.00:
        print("voce está ficando sem saldo ou estourou o orçamento")

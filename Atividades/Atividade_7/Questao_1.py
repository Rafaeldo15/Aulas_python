lista_funcionario = []
lista_demitido = []
n_funcionario = 0
while True:
    while True:

        funcionario = input("digite o nome do funcionario: ")
        lista_funcionario.append(funcionario)

        opcao = input("Deseja continuar S/N?")
        if opcao == "N":
            break
    print(f"Funcionarios adicionado:")
    for i in lista_funcionario:
        print(f"Funcionario {n_funcionario}: {i}")
        n_funcionario += 1
    print(f"Funcionários adicionados: {lista_funcionario}")

    for i in lista_funcionario:
        if i == "Felipe":
            lista_demitido.append(i)

    for i in lista_funcionario:
        if i == "Felipe":
            lista_funcionario.remove(i)

    print(f"lista de  funcionario : {lista_funcionario} e lista de demitido: {lista_demitido}")

    if opcao == "N":
        break



"""funcionario = []

while True:
    funcionario.append(input("digite o nome do funcionario: "))
    for desejo = print(f"deseja adicionar mais um funcionario? S/N: ")
    if desejo == "N":
        break
    while True:

             print (f"funcionario adicionado: {funcionario}")"""

lista_funcionario = []
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

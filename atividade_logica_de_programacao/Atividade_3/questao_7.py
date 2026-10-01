nome =  input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

pode_doar = (idade>=16 and idade <= 69) and (peso>=50.0)

print(f"{nome} você pode doar sangue: {pode_doar}")
nome= input("digite seu nome: ")
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
frequencia = int(input('dos 200 dias de aula, quantos dias você foi?: '))
frequencia= (frequencia/200)*100

resultado = ((nota_1 + nota_2) / 2)
print(f" {nome} sua média foi de: {resultado} e {frequencia:.2f}% de frequencia ")
aprovado = resultado>6 and frequencia>=75
print(f"{nome} você está aprovado? {aprovado}")


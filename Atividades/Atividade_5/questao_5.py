num_1 = int(input("digite um numero: "))
opera = input("digite uma operação: (+,-,*,/): ")
num_2 = int(input("digite outro numero: "))

match opera:
     case "+":
         print(f" O resultado da operação é= {num_1 + num_2}")

     case "-":
         print(f"O resultado da operação é== {num_1 - num_2}")

     case "*":
         print(f"O resultado da operação é= {num_1 * num_2}")

     case "/":
         print(f"O resultado da operação é= {num_1 / num_2}")

     case _:
         print("Digite uma operação válida!")


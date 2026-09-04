vel_max = 80
vel_min = 40 #50% da maxima
vel_real = int(input("digite sua velocidade em KM/h: "))
if vel_real > vel_max or vel_real < vel_min:
    print("você foi multado")

else:
   print("velocidade dentro do limite permitido. Boa viagem!")


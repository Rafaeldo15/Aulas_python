vip=str(input("você é cliente VIP?"))
vip_1 = vip == "sim"
compra=float(input("qual foi o valor da sua compra?"))

if compra >= 200 and vip_1 == True: print("Parabéns! Você ganhou frete grátis.")
else: print("O frete para esta compra será cobrado.")


produto_1= (input("digite o nome do produto: "))
custo= float(input("digite o valor do custo: "))
venda= float(input("digite o valor de venda: "))

print (f"o valor de lucro líquido obtido sobre {produto_1} é = {venda-custo}")
lucro= venda - custo
minimo = 20
print(f"o lucro foi bom: {lucro>minimo}")
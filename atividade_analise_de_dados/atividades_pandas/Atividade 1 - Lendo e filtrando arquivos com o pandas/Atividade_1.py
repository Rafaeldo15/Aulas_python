import pandas as pd
import csv

df = pd.read_csv(
    "funcionarios.csv",
                 sep=";"
                 )

df_filtrado=(df[
          (df['salario'] == 3100) |
          (df['salario'] < 3000) |
          (df['salario'] > 5000)
      ])
print("\n\n")
print("-" * 30)
print("CARREGANDO DADOS SALVOS")
print("-" * 30)
print("\n\n")

print("\nMostrando salários iguais a 3.1k, menores que 3k e maiores que 5k.\n")
print(df_filtrado)
print("-" * 30)
print("\n\nMostrar funcionários com cargos de: "
      "Analista de Dados,"
      "Analista de Sistemas,"
      "Desenvolvedor Java e "
      "Cientista de Dados.\n")
print("-" * 30)

df_funcoes=(df[
    (df['cargo'] == "Analista de Dados")|
    (df['cargo'] == "Analista de Sistemas")|
    (df['cargo'] == "Desenvolvedor Java")|
    (df['cargo'] == "Cientista de Dados")
])
print(df_funcoes)
print("-" * 30)
print("\n\nAgora mostraremos se, e quem, tem salários maiores que 6k\nsegue:\n")

for indice in df.index:
    if df.loc[indice, "salario"] > 6000:
        nome = df.loc[indice, "nome"]
        salario = df.loc[indice, "salario"]
        cargo = df.loc[indice, "cargo"]

        print(f"nome: {nome} cargo: {cargo} salario: {salario}")

print("-" * 30)

print("\n\nFicou curioso para saber quais os ID pares?\nsegue:")

id_pares=df[df['id'] % 2 == 0]

print (id_pares)





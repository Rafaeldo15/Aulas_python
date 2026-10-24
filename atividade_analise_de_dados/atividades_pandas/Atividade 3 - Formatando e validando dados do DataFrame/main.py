import pandas as pd

dados = pd.read_csv(
    "dados_despadronizados.csv",
    dtype={"cpf": "string", "salario": "string", "numero": "string"},
)

#cpf
dados["cpf_formatado"] = dados["cpf"].str.replace(r"\D", "", regex=True)
dados["cpf_valido"] = dados["cpf_formatado"].str.fullmatch(r"\d{11}")

#telefone
dados["numero_formatado"] = dados["numero"].str.replace(r"\D", "", regex=True)
dados["numero_valido"] = dados["numero_formatado"].str.fullmatch(r"\d{10,11}")


dados_salario_formatados = (
    dados["salario"]
    .str.replace(r"[^\d,.\-]", "", regex=True)
    .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
    .str.replace(r",", ".", regex=False)
    .astype(float)
)
dados["salario_formatado"] = dados_salario_formatados


dados["salario_anual"] = dados["salario_formatado"] * 12

colunas_desejadas = [
    "nome",
    "cpf",
    "cpf_formatado",
    "cpf_valido",
    "numero",
    "numero_formatado",
    "numero_valido",
    "salario",
    "salario_formatado",
    "salario_anual",
]

dados_padronizados = dados[colunas_desejadas]
dados_padronizados.to_csv("dados_padronizados.csv", index=False)

print("Arquivo 'dados_padronizados.csv' gerado com sucesso!")
print(dados_padronizados.to_string())
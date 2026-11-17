import pandas as pd

# =============================================================================
# 1. Carregamento dos dados
# =============================================================================
# Lemos todas as colunas como string para evitar conversões automáticas indesejadas antes da limpeza
df = pd.read_csv("estoque_supermercado.csv", dtype=str)


# =============================================================================
# 2. Execução das limpezas (Preço, Quantidade, Setor, Datas)
# =============================================================================

# --- Regra 2: Limpeza da Coluna preco ---
# Remova "R$", espaços e substitua vírgulas por pontos
df["preco"] = (
    df["preco"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.strip()
    .str.replace(",", ".", regex=False)
)
# Converte valores por extenso para NaN
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
# Preenche os valores nulos (NaN) com a média de preços da base
df["preco"] = df["preco"].fillna(df["preco"].mean())


# --- Regra 3: Limpeza da Coluna quantidade ---
# Textos por extenso viram NaN
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
# Preenche faltantes com 0 e converte para inteiro
df["quantidade"] = df["quantidade"].fillna(0).astype(int)


# --- Regra 4: Padronização da Coluna setor ---
# Remove espaços extras no início/fim e deixa com padrão Title Case ("Hortifruti")
df["setor"] = df["setor"].astype(str).str.strip().str.title()
# Garante o preenchimento de campos vazios ou convertidos incorretamente
df["setor"] = df["setor"].replace({"Nan": "sem setor", "": "sem setor"})
df["setor"] = df["setor"].fillna("sem setor")


# --- Regra 5: Tratamento de Datas ---
df["data_compra"] = pd.to_datetime(
    df["data_compra"], format="%d/%m/%Y", errors="coerce"
)
df["data_vencimento"] = pd.to_datetime(
    df["data_vencimento"], format="%d/%m/%Y", errors="coerce"
)


# --- Regra 6.5: Valor Patrimonial ---
df["valor_total_estoque"] = df["quantidade"] * df["preco"]


# =============================================================================
# 3. Exibição do DataFrame Limpo
# =============================================================================
print("\n--- BASE DE DADOS LIMPA ---")
print(df.head())


# =============================================================================
# 4. Resultados das Análises Gerenciais
# =============================================================================

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
# 1. Alerta de Vencimento (entre 27/10/2026 e 03/11/2026)
inicio_semana = pd.to_datetime("27/10/2026", format="%d/%m/%Y")
fim_semana = pd.to_datetime("03/11/2026", format="%d/%m/%Y")

vencendo_esta_semana = df[
    (df["data_vencimento"] >= inicio_semana)
    & (df["data_vencimento"] <= fim_semana)
]
print(
    vencendo_esta_semana[
        ["nome", "setor", "quantidade", "preco", "data_vencimento"]
    ]
)


print("\n--- MAIOR QUANTIDADE A VENCER ---")
# 2. Qualidade do Estoque: Produto que vai vencer esta semana com maior estoque
if not vencendo_esta_semana.empty:
    idx_maior_qtd = vencendo_esta_semana["quantidade"].idxmax()
    produto_maior_qtd = vencendo_esta_semana.loc[idx_maior_qtd]
    print(
        f"Produto: {produto_maior_qtd['nome']} | Quantidade em estoque: {produto_maior_qtd['quantidade']} un."
    )
else:
    print("Nenhum produto a vencer no período especificado.")


print("\n--- COMPRAS RECENTES (ÚLTIMOS 3 DIAS) ---")
# 3. Compras Recentes: Entradas entre 24/10/2026 e 27/10/2026
inicio_compras = pd.to_datetime("24/10/2026", format="%d/%m/%Y")
fim_compras = pd.to_datetime("27/10/2026", format="%d/%m/%Y")

compras_recentes = df[
    (df["data_compra"] >= inicio_compras) & (df["data_compra"] <= fim_compras)
]
print(compras_recentes[["nome", "setor", "data_compra"]])


print("\n--- PRODUTOS SEM DATA DE VENCIMENTO ---")
# 4. Produtos sem Vencimento: Data de vencimento nula (NaT)
produtos_sem_vencimento = df[df["data_vencimento"].isna()]
print(produtos_sem_vencimento[["nome", "setor", "quantidade", "data_compra"]])


print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
# 5. Valor Patrimonial por Setor
valor_por_setor = (
    df.groupby("setor")["valor_total_estoque"]
    .sum()
    .sort_values(ascending=False)
)
setor_maior_valor = valor_por_setor.idxmax()
total_maior_valor = valor_por_setor.max()

print("Valor total acumulado por setor:")
print(valor_por_setor.apply(lambda x: f"R$ {x:.2f}"))
print(
    f"\nSetor com MAIOR valor financeiro parado: {setor_maior_valor} (R$ {total_maior_valor:.2f})"
)
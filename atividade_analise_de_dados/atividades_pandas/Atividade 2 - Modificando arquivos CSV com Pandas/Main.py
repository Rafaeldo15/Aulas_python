import pandas as pd
import csv


base_de_dados = ('funcionarios.csv')
df = pd.read_csv(base_de_dados, sep=";")
df.columns.tolist()

salario_alto = df[
    (df['salario'] > 6000)
]
print ("\t-"*30,"\n\t\t\t\t\t\t\tEsses são os salários maior que R$ 6.000 na lista de Funcionários.\n","\t-"*30)
print (salario_alto)
salario_alto.to_csv("Salarios_alto.csv",
                    index=False,
                    encoding='utf-8',
                    sep="|")

print("\nAdicionando novos funcionários à lista, aguarde...")

adicionar_funcionario = [{
    'id': 31,
    'nome': 'Rafael O',
    'salario': 6500,
    'cargo': "Analista Atendimento"
},
    {
        'id': 32,
        'nome': 'Paula Marinho',
        'salario': 16800,
        'cargo': "CEO"
    }]

#erro aqui
df_novos = pd.DataFrame(adicionar_funcionario)
df_novos =pd.concat ([df_novos], ignore_index=True)

"""df_novos = pd.DataFrame(adicionar_funcionario)
df_novos.to_csv(
    'Salarios_alto.csv',
    mode='a',
    index=False,
    sep='|',
)
"""


#ERRO AQUI TAMBÉM

adicionar_funcionario = [{
    'id': 33,
    'nome': 'Jose',
    'salario': 500,
    'cargo': "Estagiário"
    "tempo de empresa": 10 #não reconhece a syntax
}]


df_novos.to_csv("cargos_altos.csv", index=False, sep=";")


print ("-"*10,"Dados analisados e adicionados a 'Salarios_alto.csv'", "-"*10)
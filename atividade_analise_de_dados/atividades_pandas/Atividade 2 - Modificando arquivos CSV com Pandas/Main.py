import pandas as pd
import csv

#leitura de todos arquivos
base_de_dados = ('funcionarios.csv')
df = pd.read_csv(base_de_dados, sep=";")
df.columns.tolist()
#separar salários altos como uma lista
salario_alto = df[
    (df['salario'] > 6000)
]
#print no terminal as informações da lista
print ("\t-"*30,"\n\t\t\t\t\t\t\tEsses são os salários maior que R$ 6.000 na lista de Funcionários.\n","\t-"*30)
print (salario_alto)

#criando doc salarios_altos.csv e adicionando a lista de salarios > R$ 6000
salario_alto.to_csv("Salarios_alto.csv",
                    index=False,
                    encoding='utf-8',
                    sep="|")

print("\nAdicionando novos funcionários à lista, aguarde...")
#criando filtro de adicionar funcionário, com id, nome, salario e cargo
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


#adicionando  no arquivo salários altos  em modo append
df_novos = pd.DataFrame(adicionar_funcionario)
df_novos.to_csv(
    'Salarios_alto.csv',
    mode='a',
    index=False,
    sep='|',
)
#adicionando estagiário e criando mais uma coluna: tempo empresa.
adicionar_funcionario = [{
    'id': 35,
    'nome': 'Aura',
    'salario': 1800,
    'cargo': "Estagiário",
    'tempo empresa': 10

}]


df_novos_func = pd.DataFrame(adicionar_funcionario)

df_atualizado = pd.concat([df, df_novos_func], ignore_index=True)


df_atualizado.to_csv(base_de_dados, index=False, sep=';', encoding='utf-8')





print ("-"*10,"Dados analisados e adicionados a 'Salarios_alto.csv'", "-"*10)
"""senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)"""

#aqui a correção só daria um  valor inteiro para variavel "senha digitada" que esta sendo reconhecida como STR


"""senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)"""


#usando logica da questao 5, if and else poderia ser assim tb
senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
if senha_digitada == senha_cadastrada : print("acesso liberado")
else: print("acesso negado")
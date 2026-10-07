import json
from operator import truediv

catalogo_livros = []

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    livro = arquivo.readlines()
    for livro in arquivo:
        livro = livro.strip()
        livro = livro.split(";")

        livro = {
            "id": int(livro[0]),
            "nome": livro[1],
            "descricao": livro[2],
            "preco": float(livro[3]),
            "em_estoque": int(livro[4])
        }

        catalogo_livros.append(livro)
print (livro)
with open("catalogo.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

print("Arquivo TXT transformado para JSON")

catalogo_livros.append({"id": 31,
                        "nome": "Decubra seus pontos fortes",
                        "descricao": "auto-ajuda",
                        "preco": 39.9,
                        "em_estoque": 10
                        })
catalogo_livros.append({"id": 32,
                        "nome": "A Arte da Guerra",
                        "descricao": "História",
                        "preco": 29.9,
                        "em_estoque": 25
                        })
catalogo_livros.append({"id": 34,
                        "nome": "50 tons de cinza",
                        "descricao": "Romance",
                        "preco": 12.90,
                        "em_estoque": 15
                        })
catalogo_livros.append({"id": 35,
                        "nome": "A Musa do Verão",
                        "descricao": "Comédia",
                        "preco": 22.90,
                        "em_estoque": 16
                        })
catalogo_livros.append({"id": 36,
                        "nome": "Maria Maria",
                        "descricao": "Auto-ajuda",
                        "preco": 15.90,
                        "em_estoque": 20
                        })

with open("catalogo.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)


def verificar_baixo_estoque():
    baixo_estoque = []
    with open('catalogo.json', 'r', encoding='utf-8') as arquivo:
        catalogo_livros = json.load(arquivo)
    for livro in catalogo_livros:
        quantidade = livro["em_estoque"]
        titulo = livro["nome"]
        if quantidade <= 15:
            baixo_estoque.append(livro)
            print(f"o título '{titulo}' está com {quantidade} no estoque\n")

def analistar_estoque():
    total_estoque = 0
    with open('catalogo.json', 'r', encoding='utf-8') as arquivo:
        livros = json.load(arquivo)
    for livro in livros:
        titulo = livro["nome"]
        preco = livro["preco"]
        quantidade =livro["em_estoque"]

        total_estoque += preco * quantidade
        print (f"Produto: {titulo}\n"
               f"Valor total estoque : {total_estoque:.2f}\n")




verificar_baixo_estoque()
analistar_estoque()
a = "Cachorro-quente R$ 10.00"
b = "Hambúrguer R$ 15.00"
c = "Batata frita R$ 8.00"
d = "Refrigerante R$ 5.00"

res=int(input("Digite o número do lanche: "))

match res:
    case 'a': print(f"{'a'}")
    case 'b': print(f"{'b'}")
    case 'c': print(f"{'c'}")
    case 'd': print(f"{'d'}")

nome= input('Digite o seu nome: ')
print("-")
print(f"{nome} você estuda em turno Matutino, Vespertino ou Noturno?")
print("-")
turno= input(f'{nome}, digite a primeira letra do turno do seu curso: ')
match turno:
    case 'M' | 'm':
        print(f"Bom dia!, {nome}")
    case 'V' | 'v':
        print(f"Boa tarde!, {nome}")
    case 'N' | 'n':
        print("Boa noite!,", nome)
    case _:
        print(nome," turno inválido!")
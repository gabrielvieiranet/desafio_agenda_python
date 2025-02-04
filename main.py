def adicionar_contato(agenda):
    print("\n# Adicionar um Contato\n")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False,
    }

    agenda.append(contato)

    print("\nContato adicionado com sucesso!")


def listar_contatos(agenda, favoritos=False):
    print("\n# Lista de Contatos Cadastrados\n")

    if agenda == []:
        print("Nenhum contato encontrado.")
        return

    espaco_indice = 3
    espaco_coluna = 19
    possui_favoritos = False

    print(
        f"{'#'.ljust(espaco_indice, ' ')}|",
        f"{'Nome'.ljust(espaco_coluna, ' ')}|",
        f"{'Telefone'.ljust(espaco_coluna, ' ')}|",
        f"{'E-mail'.ljust(espaco_coluna, ' ')}|",
        f"{'Favorito'.ljust(espaco_coluna, ' ')}|",
    )
    print(
        "|".rjust(espaco_indice + 1, "-"),
        "|".rjust(espaco_coluna + 1, "-"),
        "|".rjust(espaco_coluna + 1, "-"),
        "|".rjust(espaco_coluna + 1, "-"),
        "|".rjust(espaco_coluna + 1, "-"),
    )

    for contato in agenda:

        if favoritos and not contato["favorito"]:
            continue

        indice = str(agenda.index(contato) + 1)
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "\U00002764" if contato["favorito"] else ""
        possui_favoritos = True

        print(
            f"{indice.ljust(espaco_indice, ' ')}|",
            f"{nome.ljust(espaco_coluna, ' ')}|",
            f"{telefone.ljust(espaco_coluna, ' ')}|",
            f"{email.ljust(espaco_coluna, ' ')}|",
            f"{favorito.ljust(espaco_coluna, ' ')}|",
        )

    if not possui_favoritos or agenda == []:
        print("Nenhum contato encontrado.")


def editar_contato(agenda):

    if agenda == []:
        print("\nNenhum contato encontrado.")
        return

    print("\n# Editar um Contato\n")

    listar_contatos(agenda)

    try:
        indice = int(input("\nDigite o índice do contato que deseja editar: "))
    except ValueError:
        print("\nErro: Índice inválido.")
        return

    if indice < 1 or indice > len(agenda):
        print("\nErro: Índice inválido.")
        return

    contato = agenda[indice - 1]

    print("\nContato selecionado:")

    print(f"Nome: {contato['nome']}")
    print(f"Telefone: {contato['telefone']}")
    print(f"E-mail: {contato['email']}")

    nome = input("\nNome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato["nome"] = nome
    contato["telefone"] = telefone
    contato["email"] = email

    print("\nContato editado com sucesso!")


def marcar_desmarcar_contato(agenda):

    if agenda == []:
        print("\nNenhum contato encontrado.")
        return

    print("\n# Marcar / Desmarcar um Contato\n")

    listar_contatos(agenda)

    try:
        indice = int(
            input("\nDigite o índice do contato que deseja marcar/desmarcar: ")
        )
    except ValueError:
        print("\nErro: Índice inválido.")
        return

    if indice < 1 or indice > len(agenda):
        print("\nErro: Índice inválido.")
        return

    contato = agenda[indice - 1]

    contato["favorito"] = not contato["favorito"]

    resultado = "marcado" if contato["favorito"] else "desmarcado"

    print(f"\nContato {resultado} com sucesso!")


def deletar_contato(agenda):

    if agenda == []:
        print("\nNenhum contato encontrado.")
        return

    print("\n# Deletar um Contato\n")

    listar_contatos(agenda)

    try:
        indice = int(
            input("\nDigite o índice do contato que deseja deletar: ")
        )
    except ValueError:
        print("\nErro: Índice inválido.")
        return

    if indice < 1 or indice > len(agenda):
        print("\nErro: Índice inválido.")
        return

    contato_removido = agenda[indice - 1]

    agenda.remove(contato_removido)

    print("\nContato deletado com sucesso!")


def main():
    agenda = []
    while True:
        print("\n# Agenda de contatos\n")
        print("1 - Adicionar Contato")
        print("2 - Editar Contato")
        print("3 - Marcar / Desmarcar Contato")
        print("4 - Deletar Contato")
        print("5 - Listar Contatos")
        print("6 - Listar Favoritos")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            editar_contato(agenda)
        elif opcao == "3":
            marcar_desmarcar_contato(agenda)
        elif opcao == "4":
            deletar_contato(agenda)
        elif opcao == "5":
            listar_contatos(agenda)
        elif opcao == "6":
            listar_contatos(agenda, favoritos=True)
        elif opcao == "7":
            break
        else:
            print("\nOpção inválida")


if __name__ == "__main__":
    main()

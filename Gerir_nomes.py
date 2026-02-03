nomes = []

while True:
    print("\033[36m --- Gestor de Nomes --- \033[0m")
    print("\033[97m 1 - Adicionar Nome \033[0m")
    print("\033[97m 2 - Mostrar Nomes \033[0m")
    print("\033[97m 3 - Remover Nome \033[0m")
    print("\033[97m 4 - Procurar Nome \033[0m")
    print("\033[97m 5 - Total de Nomes \033[0m")
    print("\033[97m 6 - Limpar Lista \033[0m")
    print("\033[97m 0 - Sair do Programa \033[0m")
    print("\033[36m ----------------------- \033[0m")

    opcao = input("\033[97m Escolha uma opção:\033[0m")

    if opcao == "1":
        nome = input("\033[97m Digite o primeiro nome:\033[0m")
        sobrenome = input("\033[97m Digite o sobrenome:\033[0m")
        if nome.isalpha() and sobrenome.isalpha():
            nomes.append(nome + " " + sobrenome)
            print("\033[92m Nome adicionado com sucesso!\033[0m")
        else:
            print("\033[31m Deve usar apenas letras! \033[0m")

    elif opcao == "2":
        if nomes:
            print("\033[33m Lista de nomes: \033[0m")
            for nome_completo in nomes:
                print("\033[97m -", nome_completo)
        else:
            print("\033[31m Não há nenhum nome na lista. \033[0m")

    elif opcao == "3":
        if not nomes:
            print("\033[31m Não há nenhum nome na lista. \033[0m")
        else:
            nome_completo = input("\033[97m Digite o nome completo para remover: \033[0m")
        for nome_remover in nomes:
            if nome_remover.lower() == nome_completo.lower():
                nomes.remove(nome_remover)
                print("\033[92m Nome removido com sucesso! \033[0m")
                break
            else:
                print("\033[31m Nome não encontrado! \033[0m")

    elif opcao == "4":
        if not nomes:
            print("\033[31m Não há nenhum nome na lista. \033[0m")
        else:
            nome_completo = input("\033[97m Digite o nome completo para procurar: \033[0m")
            if nome_completo.lower() in [nome.lower() for nome in nomes]:
                print("\033[92m Nome encontrado! \033[0m")
            else:
                print("\033[31m Nome não encontrado. \033[0m")

    elif opcao == "5":
        if not nomes:
            print("\033[31m Não há nenhum nome na lista. \033[0m")
        else:
            print("\033[33m Total de nomes: \033[0m", len(nomes))

    elif opcao == "6":
        if nomes:
            nomes.clear()
            print("\033[92m Todos os nomes foram apagados!\033[0m")
        else:
            print("\033[31m A lista já está vazia.\033[0m")

    elif opcao == "0":
        print("\033[31m Saindo... \033[0m")
        break
    else:
        print("\033[31m Opção inválida. \033[0m")
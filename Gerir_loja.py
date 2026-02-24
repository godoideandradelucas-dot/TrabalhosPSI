def adicionar_produto():
    nome = input("\033[97m Nome do produto: \033[0m")
    if not nome.isalpha():
        print("\033[31m Deve usar apenas letras! \033[0m")
        return
    preco = input("\033[97m Preço: \033[0m")
    if not preco.isdigit():
        print("\033[31m Deve usar apenas letras! \033[0m")
        return
    quantidade = (input("\033[97m Quantidade: \033[0m"))
    if not quantidade.isdigit():
        print("\033[31m Digite apenas números! \033[0m")
        return

    preco = float(preco)
    quantidade = int(quantidade)

    produto = (nome, preco, quantidade)
    produtos.append(produto)
    print("\033[92m Produto adicionado com sucesso!\n \033[0m")

def listar_produtos():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
    else:
        for produto in produtos:
            print(f"\033[97m - {produto[0]} - {produto[1]} € - {produto[2]} itens \033[0m")
        print()

def remover_produto():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
        return
    nome_remover = input("\033[97m Nome do produto a remover: \033[0m")
    for produto in produtos:
        if produto[0].lower() == nome_remover.lower():
            produtos.remove(produto)
            print("\033[92m Produto removido com sucesso!\n \033[0m")
            return
    print("\033[31m Produto não encontrado.\n \033[0m")

def buscar_produto():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
        return
    nome = input("\033[97m Nome do produto para buscar: \033[0m")
    for produto in produtos:
        if nome.lower() in produto[0].lower():
            print("\033[93m Produto encontrado:"f" -{produto[0]} | {produto[1]} € | {produto[2]}" "\033[0m")
            return

    print("\033[31m Produto não encontrado.\n \033[0m")


def valor_total():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
        return
    total = 0
    for produto in produtos:
        total += produto[1] * produto[2]
    print("\033[93m Total do estoque:",total, "€ \033[0m")

def total_produtos():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
        return
    total = sum(produto[2] for produto in produtos)
    print("\033[93m Quantidade total de itens no estoque:", total, "\033[0m")


def limpar_estoque():
    if not produtos:
        print("\033[31m Nenhum produto cadastrado.\n \033[0m")
        return
    else:
        produtos.clear()
        print("\033[92m Estoque limpo com sucesso!\n \033[0m")

def sair():
    print("\033[31m Saindo do Sistema... \033[0m")

def invalido():
    print("\033[31m Opção inválida. \033[0m")

produtos = []

while True:
    print("\033[36m ----------------- Gerir Loja ----------------- \033[0m")
    print("\033[97m 1 - Adicionar Produto   5 - Valor Total        \033[0m")
    print("\033[97m 2 - Listar Produtos     6 - Total de Produtos  \033[0m")
    print("\033[97m 3 - Remover Produto     7 - Limpar Estoque     \033[0m")
    print("\033[97m 4 - Buscar Produto      0 - Sair da Loja       \033[0m")
    print("\033[36m ---------------------------------------------- \033[0m")
    opcao = input("\033[97m Escolhe uma opção: \033[0m")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        buscar_produto()
    elif opcao == "5":
        valor_total()
    elif opcao == "6":
        total_produtos()
    elif opcao == "7":
        limpar_estoque()
    elif opcao == "0":
        sair()
        break
    else:
        invalido()
import random
evento_escolhido = ""

participantes = []
turmas = set()
eventos = ("FUTEBOL", "BASKETBALL", "VOLLEYBALL", "HANDBALL", "TENIS DE MESA")


def evento():
    global evento_escolhido
    print("\n\033[34m---------\033[97m Eventos Possiveis \033[34m---------\033[0m")
    i = 1
    for esporte in eventos:
        print("\033[97m",i, "-", esporte,"\033[0m")
        i += 1
    print("\033[34m------------------------------------\033[0m")
    escolha = (input("\033[97mEscolha um evento: \033[0m"))
    while escolha not in ("1", "2", "3", "4", "5"):
        print("\033[31mOpção inválida! Digite apenas 1, 2, 3, 4 ou 5.\033[0m")
    evento_escolhido = eventos[int(escolha) - 1]


def adicionar_participante():
    nome = input("\033[34m Nome do participante: \033[0m")
    if not nome.isalpha():
        print("\033[31m Deve usar apenas letras! \033[0m")
        return
    turma = input("\033[34m Turma: \033[0m")
    participantes.append((nome, turma))
    turmas.add(turma)
    print("\033[92m",nome, "adicionado com sucesso! \033[0m")


def ver_participantes():
    if not participantes:
        print("\033[31m Nenhum participante registrado. \033[0m")
    else:
        print("\n\033[34m --- Lista de Participantes ---\033[0m")
        i = 1
        for (nome, turma) in participantes:
            print("\033[97m",i,"-",nome, "- Turma:", turma,"\033[0m")
            i += 1


def ver_turmas():
    print("\n\033[34m --- Turmas no Evento --- \033[0m")
    if turmas:
        for classe in turmas:
            print("\033[97m-",classe,"\033[0m")
    else:
        print("\033[31m Nenhuma turma registada. \033[0m")

def mudar_evento():
    confirmacao = input("\033[31m Tem certeza? Os participantes serão apagados! (s/n): \033[0m")
    if confirmacao.lower() == "s":
        print("\033[92m Todos os participantes foram apagados. Você pode criar um novo evento agora. \033[0m")
        participantes.clear()
        turmas.clear()
        evento()
    elif confirmacao.lower() == "n":
        print("\033[31m operaçao cancelada \033[0m")
    else:
        print("\033[31m Erro: digite 's' para sim ou 'n' para não. \033[0m")


def total_participantes():
    if not participantes:
        print("\033[31m Nenhum participante registrado. \033[0m")
    else:
        print("\033[34m Total de participantes:\033[97m", len(participantes), "\033[0m")


def turma_vencedora():
    if len(turmas) < 2:
        print("\033[31m É necessário pelo menos 2 turmas para ter uma vencedora! \033[0m")
        return
    vencedora = random.choice(list(turmas))
    print("\n\033[34m🏆 ==================== 🏆\033[0m")
    print("\033[97m  A turma vencedora é:", vencedora,"\033[0m")
    print("\033[34m🏆 ==================== 🏆\033[0m")


def remover_participante():
    if not participantes:
        print("\033[31m Nenhum aluno cadastrado.\033[0m")
        return
    nome_remover = input("\033[34m Nome do aluno para remover:\033[0m")
    if not nome_remover.isalpha():
        print("\033[31m Deve usar apenas letras! \033[0m")
        return
    for pessoa in participantes:
        if pessoa[0].lower() == nome_remover.lower():
            participantes.remove(pessoa)
            print("\033[92m Aluno removido com sucesso!\033[0m")
            return
    print("\033[31m Aluno não encontrado.\033[0m")
def adicionar(turma, faltas, notas):
    nome = input("\n\033[97m \033[40m Digite o nome do aluno: \033[0m")
    if not nome.isalpha():
        print("\033[31m \033[40m Deve usar apenas letras! \033[0m")
        return nome

    nota_add = input("\n\033[97m \033[40m Digite sua nota: \033[0m")
    if not nota_add.isdigit():
        print("\033[31m \033[40m Digite apenas números! \033[0m")
        return nota_add

    nota_add = int(nota_add)
    if not (0 <= nota_add <= 20):
        print("\033[31m \033[40m Nota inválida! Digite um valor entre 0 e 20. \033[0m")
        return nota_add

    turma.append(nome)
    faltas.append(0)
    notas.append(nota_add)
    print("\033[92m \033[40m Aluno adicionado com sucesso!\033[0m")


def add_falta(turma,faltas):
    if not turma:
        print("\033[31m \033[40m Não há alunos na turma. \033[0m")
    else:
        nome = input("\n\033[97m \033[40m Digite o nome do aluno:\033[0m")
        i = 0
        for aluno in turma:
            if aluno.lower() == nome.lower():
                faltas[i] += 1
                print("\033[92m \033[40m Falta adicionada com sucesso! \033[0m")
                return
            i += 1
        else:
            print("\033[31m \033[40m Aluno não encontrado. \033[0m")


def rem_faltas(turma,faltas):
    if not turma:
        print("\033[31m \033[40m Não há alunos na turma. \033[0m")
    else:
        nome = input("\n\033[97m \033[40m Digite o nome: \033[0m")
        i = 0
        for aluno in turma:
            if aluno.lower() == nome.lower():
                if faltas[i] > 0:
                    faltas[i] -= 1
                    print("\033[92m \033[40m Falta removida! \033[0m")
                else:
                    print("\033[31m \033[40m O aluno não tem faltas. \033[0m")
                return
            i += 1
        print("\033[31m \033[40m Aluno não encontrado. \033[0m")


def mostrar(turma,faltas):
    if turma:
        print("\n\033[36m \033[40m Lista de alunos: \033[0m")
        i = 0
        for nome in turma:
            print("\033[97m \033[40m -", nome, "- faltas:", faltas[i], "\033[0m")
            i += 1
    else:
        print("\033[31m \033[40m Não há nenhum nome na lista. \033[0m")


def remover(turma):
    if not turma:
        print("\033[31m \033[40m Não há nenhum nome na lista. \033[0m")
    else:
        nome = input("\n\033[97m \033[40m Digite o nome para remover: \033[0m")
        for nome_remover in turma:
            if nome_remover.lower() == nome.lower():
                turma.remove(nome_remover)
                print("\033[92m \033[40m Nome removido com sucesso! \033[0m")
                break
        else:
            print("\033[31m \033[40m Nome não encontrado! \033[0m")


def mostrar_notas(turma, notas):
    if not turma:
        print("\033[31m \033[40m Não há alunos na turma. \033[0m")
    else:
        print("\n\033[36m \033[40m Notas dos alunos: \033[0m")
        i = 0
        for aluno in turma:
            print("\033[97m \033[40m -", aluno, "- nota:", notas[i], "\033[0m")
            i += 1


def media_turma(notas):
    if not notas:
        print("\033[31m \033[40m Não há notas na turma. \033[0m")
        return
    media = sum(notas) / len(notas)
    print("\n\033[36m \033[40m Média da turma: \033[97m",(media),"\033[0m")
    return


def total(turma):
    if not turma:
        print("\033[31m \033[40m Não há nenhum nome na lista. \033[0m")
    else:
        print("\n\033[36m \033[40m Total de nomes:", "\033[97m",len(turma), "\033[0m")


def limpar(turma, faltas):
    turma.clear()
    faltas.clear()
    print("\033[92m \033[40m Lista de alunos e faltas limpa! \033[0m")

def sair():
    print("\033[31m \033[40m Saindo do Sistema... \033[0m")

def invalido():
    print("\033[31m \033[40m Opção inválida. \033[0m")


turma = []
faltas = []
nota = []

while True:
    print("\n\033[36m \033[40m _____________ \033[97mGestor de Turma\033[36m _____________ \033[0m")
    print("\033[36m \033[40m|\033[97m 1 - Adicionar aluno   6 - Mostrar Notas   \033[36m|\033[0m")
    print("\033[36m \033[40m|\033[97m 2 - Adicionar Faltas  7 - Média da Turma  \033[36m|\033[0m")
    print("\033[36m \033[40m|\033[97m 3 - Remover Faltas    8 - Total de alunos \033[36m|\033[0m")
    print("\033[36m \033[40m|\033[97m 4 - Mostrar alunos    9 - Limpar Lista    \033[36m|\033[0m")
    print("\033[36m \033[40m|\033[97m 5 - Remover aluno     0 - Sair            \033[36m|\033[0m")
    print("\033[36m \033[40m|___________________________________________|\033[0m")
    opcao = input("\033[97m \033[40m Escolhe uma opção: \033[0m")

    if opcao == "1":
        adicionar(turma,faltas, nota)
    elif opcao == "2":
        add_falta(turma,faltas)
    elif opcao == "3":
        rem_faltas(turma,faltas)
    elif opcao == "4":
        mostrar(turma,faltas)
    elif opcao == "5":
        remover(turma)
    elif opcao == "6":
        mostrar_notas(turma, nota)
    elif opcao == "7":
        media_turma(nota)
    elif opcao == "8":
        total(turma)
    elif opcao == "9":
        limpar(turma,faltas)
    elif opcao == "0":
        sair()
        break
    else:
        invalido()
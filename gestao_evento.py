import trabalhos_PSI.evento as ev


def menu():
    while True:
        print("\n\033[34m========================= \033[97mEVENTO DE", ev.evento_escolhido, "\033[34m=========================\033[0m")
        print("\033[97m\n 1. Adicionar Participante          5. Ver Total de Participantes \033[0m")
        print("\033[97m 2. Ver Participantes               6. Ver Turma Vencedora do Evento \033[0m")
        print("\033[97m 3. Ver Turmas                      7. Remover Participante \033[0m")
        print("\033[97m 4. Mudar de Evento                 0. Sair \033[0m")
        print("\033[34m\n======================================================================\033[0m")

        opcao = input("\033[97m Escolha uma opção: \033[0m")

        if opcao == "1":
            ev.adicionar_participante()
        elif opcao == "2":
            ev.ver_participantes()
        elif opcao == "3":
            ev.ver_turmas()
        elif opcao == "4":
            ev.mudar_evento()
        elif opcao == "5":
            ev.total_participantes()
        elif opcao == "6":
            ev.turma_vencedora()
        elif opcao == "7":
            ev.remover_participante()
        elif opcao == "0":
            print("\033[31m Voce saiu do programa!\033[0m")
            break
        else:
            print("\033[31m Opção inválida!\033[0m")

if __name__ == "__main__":
    ev.evento()
    menu()
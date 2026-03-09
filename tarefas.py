def criar_tarefas(lista_geral):
    nome = input("Digite uma tarefa: ")
    prioridade = input("Qual o nível de prioridade? "
                       "Alta, baixa ou média? ").capitalize()
    
    nova_tarefa = {
        "tarefa": nome,
        "prioridade": prioridade,
        "status": "Pendente"
    }
    
    lista_geral.append(nova_tarefa)
    print(f"{nome} salva com sucesso!")
    
def listar_tarefas(lista_geral):
    if not lista_geral:
        print("\n Nenhuma tarefa cadastrada")
        return
    
    print("=== LISTA DE TAREFAS ===")
    for indice, dicio in enumerate(lista_geral):
        status_icon = "✔" if dicio['status'] == "Concluída" else "☐"
        print(f"{indice}. [{status_icon}] {dicio['tarefa']} | Prioridade: {dicio['prioridade']}")
    
def excluir_tarefas(lista_geral):
    listar_tarefas(lista_geral)
    if lista_geral:
        try:
            indice = int(input("\nDigite o número da tarefa para excluir: "))
            removida = lista_geral.pop(indice)
            print(f"Tarefa {removida['tarefa']} removida!")
        except (ValueError, IndexError):
            print("Opção inválida")

    
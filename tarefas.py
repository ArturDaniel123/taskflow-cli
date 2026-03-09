def criar_tarefas(lista_geral):
    nome = input("Digite uma tarefa: ")
    prioridade = input("Qual o nível de prioridade? "
                       "Alta, baixa ou média? ").capitalize()
    
    nova_tarefa = {
        "tarefa" : nome,
        "prioridade" : prioridade,
        "status" : "Pendente"
    }
    
    lista_geral.append(nova_tarefa)
    print(f"{nome} salva com sucesso!")


    
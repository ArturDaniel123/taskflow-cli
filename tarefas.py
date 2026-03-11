import time

def criar_tarefas(lista_geral):
    while True:
        nome = input("\nDigite uma tarefa (ou tecle 'S' para sair): ").capitalize().strip()
        if not nome:
            print("\nEspaço vazio. Tente novamente")
            time.sleep(1)
            continue
        
        if nome.upper() == 'S':
            print("Saindo...")
            time.sleep(1)
            return
        
        while True:
            prioridade = input("\nQual o nível de prioridade? "
                            "Alta, baixa ou média? ").capitalize()
            if prioridade not in ['Alta', 'Média', 'Media', 'Baixa']:
                print(f'\n{prioridade} não é uma opção válida. Por favor, tente '
                    'novamente')
                time.sleep(0.9)
            else:
                break
    
        nova_tarefa = {
            "tarefa": nome,
            "prioridade": prioridade,
            "status": "Pendente"
        }
        
        lista_geral.append(nova_tarefa)
        print(f"\n{nome} salvo(a) com sucesso!")
        time.sleep(1)
        break
    
def listar_tarefas(lista_geral):
    if not lista_geral:
        print("\nNenhuma tarefa cadastrada")
        time.sleep(1)
        return
    
    print("\n=== LISTA DE TAREFAS ===")
    for indice, dicio in enumerate(lista_geral):
        status_icon = "✔" if dicio['status'] == "Concluída" else "☐"
        print(f"{indice}. [{status_icon}] {dicio['tarefa']} | Prioridade: {dicio['prioridade']}")
        time.sleep(0.2)
    
def excluir_tarefas(lista_geral):
    if not lista_geral:
        print("\nNão há tarefas para excluir")
        time.sleep(1)
        
    while True:
        listar_tarefas(lista_geral)
        
        entrada = input("\nDigite o número da tarefa para"
                   "excluir (ou 'S' para sair):")
        
        if entrada.upper() == 'S':
            print("\nSaindo da exclusão...")
            time.sleep(1)
            break
        
        if lista_geral:
            try:
                indice = int(entrada)
                removida = lista_geral.pop(indice)
                print(f"\nTarefa {removida['tarefa']} removida!")
                time.sleep(1)
                break
            except (ValueError, IndexError):
                print("\nOpção inválida. Tente novamente")
                time.sleep(0.9)

def concluir_tarefas(lista_geral):
    if not lista_geral:
        print("\nNão há tarefas para concluir")
        time.sleep(1)
        return
    
    while True:
        listar_tarefas(lista_geral)
        try:
            escolha = input("\nDigite o número da tarefa para concluir (ou 'S' para sair): ")
            if escolha.upper() == 'S':
                break
            
            indice = int(escolha)
            
            lista_geral[indice]['status'] = "Concluída"
            
            print(f"\n✅ Tarefa '{lista_geral[indice]['tarefa']}' marcada como concluída!")
            time.sleep(1)
            break
        
        except (ValueError, IndexError):
            print("\nOpção inválida. Tente novamente.")
            time.sleep(1)
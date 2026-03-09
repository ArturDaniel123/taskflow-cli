import time

def menu():
    print('\n==== TASK FLOW CLI ====')
    time.sleep(0.9)
    print('[1] Criar tarefas\n[2] Listar tarefas\n[3] Excluir tarefa\n'
          '[4] Concluir tarefa\n[0] Sair')
    time.sleep(1)
    
    return input("\nEscolha uma opção: ")  



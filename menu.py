import time
RESET = '\033[0m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'

def menu():
    print('\n==== TASK FLOW CLI ====')
    time.sleep(0.9)
    print(f'{AZUL}[1] Criar tarefas{RESET}\n{AMARELO}[2] Listar tarefas{RESET}'
          f'\n{VERMELHO}[3] Excluir tarefa{RESET}\n'
          f'{VERDE}[4] Concluir tarefa{RESET}\n[0] Sair')
    time.sleep(1)
    
    return input("\nEscolha uma opção: ")  



from menu import menu
from tarefas import criar_tarefas, listar_tarefas, excluir_tarefas

banco_de_tarefas = []

def iniciar():
    while True:
        opcao = menu()
        
        if opcao == '1':
            criar_tarefas(banco_de_tarefas)
        elif opcao == '2':
            listar_tarefas(banco_de_tarefas)
        elif opcao == '3':
            excluir_tarefas(banco_de_tarefas)
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente")
            
if __name__ == "__main__":
    iniciar()   
        
    
    
        
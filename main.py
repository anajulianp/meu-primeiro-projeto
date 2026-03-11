tasks = []

while True:
  print("\nGerenciador de tarefas:")
  print("1- Ver tarefas")
  print("2- Adicionar tarefas")
  print("3- Sair")

choice = input("Escolha uma opção: ")

if choise == "1":
  print(tasks)

elif choise == "2":
  task = input("Digite a tarefa: ")
  tasks.append(task)

elif choice == "3":
  break
  

# Solicita ao usuário que escolha um lugar de lazer
print("Escolha um lugar de lazer:")
print("1. Parque")
print("2. Cinema")
print("3. Restaurante")

opcao = input("Digite o número da opção desejada: ")

# Verifica a escolha do usuário e fornece o melhor horário para sair de casa
if opcao == "1":
    print("Para ir ao Parque, o melhor horário para sair de casa é de manhã.")
elif opcao == "2":
    print("Para ir ao Cinema, o melhor horário para sair de casa é à tarde.")
elif opcao == "3":
    print("Para ir ao Restaurante, o melhor horário para sair de casa é à noite.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")

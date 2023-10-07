print("Escolha um tamanho de calçado:")
print("1. Tamanho 36")
print("2. Tamanho 38")
print("3. Tamanho 40")
print("4. Tamanho 16 (Recém-nascido)")

opcao = input("Digite o número da opção desejada: ")

# Verifica a escolha do usuário e identifica o tipo de calçado
if opcao == "1":
    print("O tamanho 36 é geralmente usado por adultos.")
elif opcao == "2":
    print("O tamanho 38 é geralmente usado por adultos.")
elif opcao == "3":
    print("O tamanho 40 é geralmente usado por adultos.")
elif opcao == "4":
    print("O tamanho 16 (Recém-nascido) é usado para bebês recém-nascidos.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")

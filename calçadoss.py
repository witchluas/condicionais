print("Escolha um tamanho de calçado: ")
print("1. Tamanho 36")
print("2. Tamanho 38")
print("3. Tamanho 40")
print("4. Tamanho 26 (Criança)")
print("5. Tamanho 16 (Recém - Nascido)")

opcao = input("Por favor, digite o número da opção desejada: ")

if opcao == "1":
    print("O tamanho 36 é geralmente calçado por Adultos.")
elif opcao == "2":
    print("O tamanho 38 é geralmete calçado por Adultos. ")
elif opcao == "3":
    print("O tamanho 40 é geralmente calçado por Adultos. ")
elif opcao == "4":
    print("O tamanho 26 é geralmente calçado por Crianças. ")
elif opcao == "5":
    print("O tamanho 16 é geralmete calçado por Recém - Nascidos. ")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2,3, 4 ou 5). ")

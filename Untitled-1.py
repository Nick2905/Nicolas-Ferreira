print("Exceções e Try Except")

# estrutura basica do try except finally
try:
    pass
except:
    pass
finally:
    pass

opcao = 0

while opcao != 4:
    print("Super programa 9000")
    print("1. Cadastrar produto")
    print("2. Cadastrar cliente")
    print("3. Extrato de caixa")
    print("4. Sair")

    try:
        opcao = int( input("Digite sua escolha: "))
    except:
        print("se ferrou otário kkkkkkk")
    else:
        if opcao == 1:
            print("Produto cadastrado com sucesso!")
        elif opcao == 2:
            print("Cliente cadastrado com sucesso!")
        elif opcao == 3:
            print("Extrato de caixa enviado por email!")
        elif opcao == 4:
            print("Tchau!")
        else:
            print("Opção invalida")

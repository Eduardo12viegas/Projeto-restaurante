import pickle

# Carregar os produtos 
with open("produtos.pkl", "rb") as f:
    produtos_carregados = pickle.load(f)

# Definição do usuário
print ("Olá, bem vindo ao restaurante")
print ("você é um cliente, garçom ou administrador?")
print('Digite "A" Para cliente, ""B" para garçom, e "C" para administrador')
cargo = input("")

#Cliente
if cargo.upper() == "A":

#Escolha da comanda
    disponiveis = [1,2,3,6,7,9,10,12,15,16,17,19,20]

    print("Escolha sua comanda!")
    print("comandas disponiveis: ",*disponiveis)

    while True:
        try:
            comanda = int(input("digite sua comanda: "))

            if comanda in disponiveis:
                print(f"sua comanda é a comanda {comanda}!")
                break
            else:
                print("comanda indisponivel, digite novamente!")
        except ValueError:
            print("Entrada inválida, digite apenas números")

    comanda_cliente = []

    #Cardapio 
    print("")
    print("")
    print("Cardapio: ")

    for i, p in enumerate(produtos_carregados, start=1):
        codigo, nome, preco, estoque = p
        # p[0] = código, p[1] = nome, p[2] = preço p[3] = estoque
    
        if estoque <= 0:  
            print(f"{codigo} {nome} - R${preco} | Esgotado")
        else:
            print(f"{codigo} {nome} - R${preco}")

    print("")
    print("Digite o código dos produto para adicionar à comanda: ")
    print("Digite 'A' para finalizar a compra ou 'B' para sair")

    while True:
        escolha = input("Sua escolha: ")

        #Finalizar compra
        if escolha.upper() == "A": # Finalizar compra
            total = sum(preco for _, preco in comanda_cliente)
            print("Sua comanda contém: ")
            for nome, preco in comanda_cliente:
                print(f"- {nome} | R${preco}")
            print(f"Total a pagar: R${total:.2f}")
            break

        #Sair da compra
        elif escolha.upper() == "B":
            print("Você saiu sem comprar")
            break

        #Escolheu um código de produto
        else: 
            try:
                codigo = int(escolha)
                #verifica se o codigo existe
                if 1 <= codigo <= len(produtos_carregados):
                    codigo, nome, preco, estoque = produtos_carregados[codigo-1]
                    if estoque > 0:
                        comanda_cliente.append((nome, preco))
                        print(f"{nome} adicionado à comanda")
                    else:
                        print("Produto esgotado, escolha outro.")
                else:
                    print("Código invalido, tente novamente.")
            except ValueError:
                print("Entrada inválida, digite um número ou A/B.")


else:
    print("ainda em desinvolvimento")
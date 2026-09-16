import pickle

# Carregar os produtos 
with open("produtos.pkl", "rb") as f:
    produtos_carregados = pickle.load(f)

# Carregar as comandas
with open("comandas.pkl", "rb") as f:
    todas_comandas = pickle.load(f)

print("Olá, bem vindo ao restaurante")
print('Você pode digitar "SAIR" para encerrar o programa a qualquer momento')

# 🔹 Nome do cliente
nome_cliente = input("Digite seu nome: ")
if nome_cliente.upper() == "SAIR":
    print("Programa encerrado.")
    exit()

# Escolha da comanda
disponiveis = [c["numero"] for c in todas_comandas if c["status"] == "disponivel"]

print("Escolha sua comanda!")
print("Comandas disponíveis:", *disponiveis)

while True:
    comanda = input("Digite sua comanda: ")
    if comanda.upper() == "SAIR":
        print("Programa encerrado.")
        exit()
    try:
        comanda = int(comanda)
        comanda_obj = next((c for c in todas_comandas if c["numero"] == comanda), None)
        if comanda_obj and comanda_obj["status"] == "disponivel":
            print(f"Sua comanda é a comanda {comanda}!")
            comanda_obj["status"] = "ocupada"
            comanda_obj["cliente"] = {"nome": nome_cliente, "metodo_pagamento": None}
            break
        else:
            print("Comanda indisponível, digite novamente!")
    except ValueError:
        print("Entrada inválida, digite apenas números ou SAIR.")

comanda_cliente = []

# Cardápio 
print("")
print("")
print("Cardápio: ")

for i, p in enumerate(produtos_carregados, start=1):
    codigo, nome, preco, estoque = p
    if estoque <= 0:  
        print(f"{codigo} {nome} - R${preco} | Esgotado")
    else:
        print(f"{codigo} {nome} - R${preco}")

print("")
print("Digite o código do produto para adicionar à comanda: ")
print("Digite 'A' para finalizar a compra ou 'SAIR' para encerrar")

while True:
    escolha = input("Sua escolha: ")

    # Encerrar a qualquer momento
    if escolha.upper() == "SAIR":
        print("Você saiu sem comprar!")
        break

    # Finalizar compra
    elif escolha.upper() == "A":
        total = sum(preco for _, preco in comanda_cliente)
        print("Sua comanda contém: ")
        for nome, preco in comanda_cliente:
            print(f"- {nome} | R${preco}")
        print(f"Total a pagar: R${total:.2f}")

 # 🔹 Perguntar método de pagamento
        print("Escolha o método de pagamento:")
        print("A - Pix")
        print("B - Cartão")
        print("C - Dinheiro")
        metodo_escolha = input("")

        if metodo_escolha.upper() == "SAIR":
            print("Programa encerrado.")
            break

        if metodo_escolha.upper() == "A":
            metodo = "Pix"
        elif metodo_escolha.upper() == "B":
            metodo = "Cartão"
        elif metodo_escolha.upper() == "C":
            metodo = "Dinheiro"
        else:
            print("Opção inválida, pagamento definido como 'Indefinido'")
            metodo = "Indefinido"

        # Atualizar comanda com pedidos e pagamento
        comanda_obj["pedidos"] = [{"produto": nome, "preco": preco} for nome, preco in comanda_cliente]
        comanda_obj["total"] = total
        comanda_obj["cliente"]["metodo_pagamento"] = metodo

        with open("comandas.pkl", "wb") as f:
            pickle.dump(todas_comandas, f)

        print("Estoque e comanda atualizados com sucesso!")
        break

    # Escolheu um código de produto
    else: 
        try:
            codigo = int(escolha)
            if 1 <= codigo <= len(produtos_carregados):
                codigo, nome, preco, estoque = produtos_carregados[codigo-1]
                if estoque > 0:
                    comanda_cliente.append((nome, preco))
                    print(f"{nome} adicionado à comanda")
                else:
                    print("Produto esgotado, escolha outro.")
            else:
                print("Código inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número ou SAIR.")

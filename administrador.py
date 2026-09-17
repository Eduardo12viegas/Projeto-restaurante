import pickle
from faker import Faker
import random
from datetime import datetime, timedelta
fake = Faker("pt_BR")
data_atual = datetime(2026, 9, 16)

print("=== Sistema do Administrador ===")
print('Digite "SAIR" para encerrar o programa a qualquer momento')

while True:
    print("O que deseja gerenciar?")
    print("A - Clientes (histórico)")
    print("B - Produtos")
    escolha = input("")

    if escolha.upper() == "SAIR":
        print("Programa encerrado.")
        break

    elif escolha.upper() == "A":
        try:
            with open("historico.pkl", "rb") as f:
                historico = pickle.load(f)
        except (FileNotFoundError, EOFError):
            historico = []

        if not historico:
            print("Nenhum cliente registrado no histórico.")
        else:
            for h in historico:
                print(f"\nComanda {h['numero']} - Cliente: {h['cliente']['nome']} - Pagamento: {h['metodo_pagamento']}")
                for p in h["pedidos"]:
                    print(f"- {p['produto']} | R${p['preco']} | Validade: {p.get('validade','N/A')}")
                print(f"Total: R${h['total']:.2f}")

            escolha_del = input("\nDigite o número da comanda para deletar do histórico (ou SAIR): ")
            if escolha_del.upper() != "SAIR":
                try:
                    escolha_del = int(escolha_del)
                    historico = [h for h in historico if h["numero"] != escolha_del]
                    with open("historico.pkl", "wb") as f:
                        pickle.dump(historico, f)
                    print("Dados removidos do histórico.")
                except ValueError:
                    print("Entrada inválida.")

    elif escolha.upper() == "B":
        with open("produtos.pkl", "rb") as f:
            produtos = pickle.load(f)

        for codigo, nome, preco, estoque, validades in produtos:
            prox_validade = validades[0] if validades else "Sem validade"
            print(f"{codigo} {nome} - R${preco} | Estoque: {estoque} | Próxima validade: {prox_validade}")
            print(f"Lista de validades: {validades}")

        codigo_escolhido = input("\nDigite o código do produto para alterar (ou SAIR): ")
        if codigo_escolhido.upper() == "SAIR":
            continue

        try:
            codigo_escolhido = int(codigo_escolhido)
            produto = next((p for p in produtos if p[0] == codigo_escolhido), None)
            if produto:
                codigo, nome, preco, estoque, validades = produto
                novo_preco = input("Novo preço (ENTER para manter): ")
                if novo_preco.strip():
                    preco = float(novo_preco)

                novo_estoque = input("Novo estoque (ENTER para manter): ")
                if novo_estoque.strip():
                    novo_estoque = int(novo_estoque)
                    if novo_estoque > estoque:
                        qtd_add = novo_estoque - estoque

                        dias_sorteados = []
                        for _ in range(qtd_add):
                            dias_sorteados.append(random.randint(30, 90))
                        dias_sorteados.sort()

                        novas_validades = []
                        for dias in dias_sorteados:
                            validade = data_atual + timedelta(days=dias)
                            novas_validades.append(validade.strftime("%d/%m/%Y"))

                        validades.extend(novas_validades)
                    estoque = novo_estoque

                produtos[produtos.index(produto)] = (codigo, nome, preco, estoque, validades)
                with open("produtos.pkl", "wb") as f:
                    pickle.dump(produtos, f)
                print("Produto atualizado com sucesso!")
        except ValueError:
            print("Entrada inválida.")

    else:
        print("Opção inválida, digite A, B ou SAIR.")

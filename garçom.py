import pickle

# Carregar as comandas
with open("comandas.pkl", "rb") as f:
    todas_comandas = pickle.load(f)

print("=== Sistema do Garçom ===")
print('Digite "SAIR" para encerrar o programa a qualquer momento')

while True:
    # Mostrar comandas em uso (ocupadas ou atendidas)
    em_uso = [c for c in todas_comandas if c["status"] in ["ocupada", "atendida"]]

    if not em_uso:
        print("Não há comandas em uso no momento.")
    else:
        print("Comandas em uso:")
        for c in em_uso:
            print(f"Comanda {c['numero']} - Cliente: {c['cliente']['nome']} - Status: {c['status']} - Total: R${c['total']:.2f}")

    print("Digite o número da comanda que deseja gerenciar:")
    escolha = input("")
    if escolha.upper() == "SAIR":
        print("Programa encerrado.")
        break

    try:
        escolha = int(escolha)
        comanda = next((c for c in em_uso if c["numero"] == escolha), None)
        if comanda:
            print(f"Comanda {comanda['numero']} selecionada.")
            print("Pedidos:")
            for p in comanda["pedidos"]:
                print(f"- {p['produto']} | R${p['preco']}")
            print(f"Total: R${comanda['total']:.2f}")

            print("O que deseja fazer?")
            if comanda["status"] == "ocupada":
                print("A - Marcar como atendida (cliente recebeu o pedido)")
                print("B - Liberar comanda (cliente foi embora)")
            elif comanda["status"] == "atendida":
                print("B - Liberar comanda (cliente foi embora)")

            acao = input("")

            if acao.upper() == "SAIR":
                print("Voltando ao menu principal...")
                continue
            elif acao.upper() == "A" and comanda["status"] == "ocupada":
                comanda["status"] = "atendida"
                print("Comanda marcada como atendida. O cliente ainda está na mesa.")
            elif acao.upper() == "B":
                # Salvar no histórico antes de liberar
                try:
                    with open("historico.pkl", "rb") as f:
                        historico = pickle.load(f)
                except (FileNotFoundError, EOFError):
                    historico = []

                historico.append({
                    "numero": comanda["numero"],
                    "cliente": comanda["cliente"],
                    "pedidos": comanda["pedidos"],
                    "total": comanda["total"],
                    "metodo_pagamento": comanda["cliente"]["metodo_pagamento"] if comanda["cliente"] else None
                })

                with open("historico.pkl", "wb") as f:
                    pickle.dump(historico, f)

                # Liberar a comanda para novo uso
                comanda["status"] = "disponivel"
                comanda["cliente"] = None
                comanda["pedidos"] = []
                comanda["total"] = 0.0
                print("Comanda liberada e disponível novamente para novos clientes.")
            else:
                print("Opção inválida.")

            # Salvar alterações
            with open("comandas.pkl", "wb") as f:
                pickle.dump(todas_comandas, f)

        else:
            print("Comanda não encontrada ou não está em uso.")
    except ValueError:
        print("Entrada inválida, digite um número ou SAIR.")

from faker import Faker
import pickle
from datetime import datetime, timedelta

fake = Faker("pt_BR")

# Data atual considerada
data_atual = datetime(2026, 9, 16)

def gerar_validades(qtd, dias_min=5, dias_max=30):
    """Gera lista de validades para cada unidade em estoque"""
    validades = []
    for _ in range(qtd):
        dias = fake.random_int(min=dias_min, max=dias_max)
        validade = data_atual + timedelta(days=dias)
        validades.append(validade.strftime("%d/%m/%Y"))
    # ordenar para simular fila (mais próximo primeiro)
    validades.sort(key=lambda d: datetime.strptime(d, "%d/%m/%Y"))
    return validades

# ------------------------
# Produtos
# ------------------------
produtos_nomes = [
    "Pizza", "Hambúrquer", "Salada", "Café", "Suco de laranja", 
    "Suco de uva", "Sopa", "Porção de frango", "Porção de batata"
]

codigo = 0
produtos = []
for nome in produtos_nomes:
    codigo += 1
    preco = fake.pyfloat(min_value=10, max_value=80, right_digits=2, positive=True)
    estoque = fake.random_int(min=5, max=30)
    validades = gerar_validades(estoque)
    produtos.append((codigo, nome, preco, estoque, validades))

# Teste: mostrar produtos
for codigo, nome, preco, estoque, validades in produtos:
    prox_validade = validades[0] if validades else "Sem validade"
    print(f"{codigo} {nome} - R${preco} | Estoque: {estoque} | Próxima validade: {prox_validade}")

# Salvar com pickle
with open("produtos.pkl", "wb") as f:
    pickle.dump(produtos, f)

print("\nProdutos salvos em 'produtos.pkl'")

# ------------------------
# Comandas
# ------------------------
numeros_comandas = list(range(1, 21))

comandas = []
for numero in numeros_comandas:
    comanda = {
        "numero": numero,
        "status": "disponivel",
        "cliente": None,
        "pedidos": [],
        "total": 0.0
    }
    comandas.append(comanda)

# Teste: mostrar comandas
print("\nComandas geradas:")
for c in comandas:
    print(f"Comanda {c['numero']} - Status: {c['status']}")

# Salvar com pickle
with open("comandas.pkl", "wb") as f:
    pickle.dump(comandas, f)

print("\nComandas salvas em 'comandas.pkl'")
from faker import Faker 
import random
import pickle

fake = Faker("pt_BR")

# ------------------------
# Produtos
# ------------------------
produtos_nomes = [
    "Pizza", "Hambúrquer", "Salada", "Café", "Suco de laranja", 
    "Suco de uva", "Sopa", "Porção de frango", "Porção de batata"
]

# Atribuir valores aos produtos
codigo = 0
produtos = []
for nome in produtos_nomes:
    codigo += 1
    preco = round(random.uniform(10, 80), 2) 
    estoque = random.randint(5, 30) 
    produtos.append((codigo, nome, preco, estoque))

# Teste: mostrar produtos
for codigo, nome, preco, estoque in produtos:
    print(f"{codigo} {nome} - R${preco} | Estoque: {estoque}")

# Salvar com pickle
with open("produtos.pkl", "wb") as f:
    pickle.dump(produtos, f)

print("\nProdutos salvos em 'produtos.pkl'")

# ------------------------
# Comandas
# ------------------------
# Lista de números de comandas que existirão
numeros_comandas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

comandas = []
for numero in numeros_comandas:
    comanda = {
        "numero": numero,
        "status": "disponivel",   # pode ser 'disponivel', 'ocupada', 'liberada'
        "cliente": None,          # depois será preenchido com nome e pagamento
        "pedidos": [],            # lista de pedidos do cliente
        "total": 0.0              # valor total da comanda
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
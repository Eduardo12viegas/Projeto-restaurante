from faker import Faker 
import random
import pickle

produtos_nomes = [
    "Pizza", "Hambúrquer", "Salada", "Café", "Suco de laranja", 
    "Suco de uva", "Sopa", "Porção de frango", "Porção de batata"
]

# Atribuir valores aos produtos

produtos = []
for nome in produtos_nomes:
    preco = round(random.uniform(10, 80), 2) 
    estoque = random.randint(5, 30) 
    produtos.append((nome, preco, estoque))

#teste: mostrar produtos
for p in produtos:
    print(f"{p[0]} - R${p[1]} | Estoque: {p[2]}")


# Salvar com pickle
with open("produtos.pkl", "wb") as f:
    pickle.dump(produtos, f)

print("\nProdutos salvos em 'produtos.pkl'")
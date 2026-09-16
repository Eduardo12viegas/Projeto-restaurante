from faker import Faker 
import random
import pickle

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

#teste: mostrar produtos
for codigo, nome, preco, estoque in produtos:
    print(f"{codigo} {nome} - R${preco} | Estoque: {estoque}")

# Salvar com pickle
with open("produtos.pkl", "wb") as f:
    pickle.dump(produtos, f)

print("\nProdutos salvos em 'produtos.pkl'")
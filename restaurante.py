import pickle

# Carregar os produtos 
with open("produtos.pkl", "rb") as f:
    produtos_carregados = pickle.load(f)

#Cardapio 

print("Cardápio:")

for p in produtos_carregados:
    # p[0] = nome, p[1] = preço, p[2] = estoque
    
    if p[2] <= 0:  
        print(f"{p[0]} - R${p[1]} | Esgotado")
    else:
        print(f"{p[0]} - R${p[1]}")
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

    #Cardapio 
    print("")
    print("")
    print("")
    print("Cardapio: ")

    for p in produtos_carregados:
        # p[0] = nome, p[1] = preço, p[2] = estoque
    
        if p[2] <= 0:  
            print(f"{p[0]} - R${p[1]} | Esgotado")
        else:
            print(f"{p[0]} - R${p[1]}")

else:
    print("ainda em desinvolvimento")
#exercicio 1
idade = 0
print("Digite sua idade:")
idade = int(input())
print("Sua idade é: ", idade, " anos")
if (idade >= 18):
    print("Você é obrigado(a) a votar")
else:
    if (idade >= 16): 
        print("Você pode votar")
    else: 
        print("Você não pode votar")



#Nome e calculo da idade
nome = input("Digite seu nome:")
nascimento = int (input("Digite seu ano de nascimento:"))
atual = int(input ("Digite o ano atual:"))

print(atual - nascimento)

print () #Pula de linha

#Tabuada
tabuada=int (input("Digite um número:"))

print ("Tabuada do número:", tabuada)
for valor in range (1, 11, 1):
    print (str(tabuada) + " x " + str(valor) + " = " + str(tabuada*valor))
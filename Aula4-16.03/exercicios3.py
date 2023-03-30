#Exercicio 1
media = 0
print("Digite sua média em matemática:")
media=float(input())
if(media >= 6):
    print("Você foi aprovado")
else:
    if (media >5 <6):
        print("Você está de recuperação")
    else: 
        if (media <5):
            print("Você foi reprovado")

print()
print()
print()

#exercicio 2
num = 0
print("Digite um número inteiro qualquer:")
num = int(input())
if (num%2)== 0: 
    print("Este número é par")
else:
    print("Este número é impar")

print()
print()
print()

#exercicio 2.1
import math
print("Digite um número inteiro qualquer:")
num= float(input())
num2 = num / 2
if math.ceil(num2) * 2 != num:
    print("O número é impar.")
else:
    print("O número é par.")

print()
print()
print()

#ecercicio 2.2
num = resto = 0
print("Digite um número: ")
num = int(input())
resto = num % 2
if resto == 0:
    print("Par")
else:
    print("Impar")
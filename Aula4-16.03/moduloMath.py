#exercicio 1
base=0
altura=0
area=0
print("AREA DO RETANGULO")
print("Digite o valor da base: ")
base=float(input())
print("Digite o valor altura: ")
altura=float(input())
area=(base*altura)
print("A base do retangulo é: ", area)

print()
print()
print()

#exercicio 2
base=0
altura=0
area=0
print("AREA DO TRIANGULO")
print("Digite o valor da base:")
base=float(input())
print("digite a altura:")
altura=float(input())
area=(base*altura)/2
print("A area do triangulo é: ", area)

print()
print()
print()

#exercicio 3
baseMaior=0
baseMenor=0
altura=0
area=0
print("AREA DO TRAPEZIO")
print("Digite o valor da base maior:")
baseMaior=float(input())
print("Digite o valor da base menor:")
baseMenor=float(input())
print("Digite a altura:")
altura=float(input())
area=(baseMaior + baseMenor)*(altura)/2
print("A area do seu trapezio é: ", area)

print()
print()
print()

#exercicio 4
import math
print("EQUAÇÃO DO 2°GRAU")
print("Digite o valor de A:")
a=float(input())
print("Digite o valor de B:")
b=float(input())
print("Digite o valor de C:")
c=float(input())
delta=math.pow(b, 2) -4*a*c
print("Seu delta é: ", delta)
x1=(-(b) + math.sqrt(delta))/(2*a)
x2=(-(b) - math.sqrt(delta))/(2*a)
print("x1: ", x1)
print("x2: ", x2)

print()
print()
print()

#exercicio 4.1
import math
a = b = c = 0
delta = x1 = x2 = 0.0
print("Digite valores A, B e C:")
a= int(input())
b= int(input())
c= int(input())
delta = math.pow(b,2) -4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 *a)
x2 = (-b - math.sqrt(delta)) / (2 * a)


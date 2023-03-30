#exercicio 1
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

#exercicio 1.1
import math
print("EQUAÇÃO DO 2°GRAU PROFESSOR")
a = b = c = 0
delta = x1 = x2 = 0.0
print("Digite valores A, B e C:")
a= int(input())
b= int(input())
c= int(input())
delta = math.pow(b,2) -4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 *a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

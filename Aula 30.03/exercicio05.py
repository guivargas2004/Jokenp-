salario = 0
anos = 0

print("Digite seu salário")
salario = float(input()) 
print("Digite seu tempo de trabalhos em anos:")
anos = int(input())

if anos<5: 
    aumento =(salario*0.05)
    aumento1 = (salario+aumento)
    print("Seu salário atual é", aumento1)
elif anos >=5 and anos <=10 :
    aumento2 = (salario*0.10)
    aumento3 = (salario+aumento2)
    print("Seu salário atual é", aumento3)
elif anos>=10 and anos <=15:
    aumento4 = (salario*0.15)
    aumento5 = (salario+aumento4)
    print("Seu salário atual é", aumento5)
else:
    aumento6 = (salario*0.20)
    aumento7 = (salario+aumento6)
    print("Seu salário atual é", aumento7)

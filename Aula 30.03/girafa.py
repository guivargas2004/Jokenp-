print("Digite a altura de 5 girafas")
print("Girafa 1")
g1 = float(input())
print("Girafa 2")
g2 = float(input())
print("Girafa 3")
g3 = float(input())
print("Girafa 4")
g4 = float(input())
print("Girafa 5")
g5 = float(input())

if g1>g2 and g1>g3 and g1>g4 and g1>g5:
    print("A Girafa 1 é a maior de todas, e tem", g1, "metros de altura")
elif g2>g1 and g2>g3 and g2>g4 and g2>g5:
    print("A Girafa 2 é a maior de todas, e tem ", g2, "metros de altura")
elif g3>g1 and g3>g2 and g3>g4 and g3>g5:
    print("A Girafa 3 é a maior de todas, e tem ", g3, "metros de altura")
elif g4>g1 and g4>g2 and g4>g3 and g4>g5:
    print("A Girafa 4 é a maior de todas, e tem ", g4, "metros de altura")
else: 
    print("A Girafa 5 é a maior de todas, e tem", g5, "metros de altura")
    
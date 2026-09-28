# que peça um número e exiba a tabuada de 1 a 10 dessenúmero.

num = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    

#  que informe um número e diga se ele é positivo, negativo ou zero

numero  = float(input(" Informe um número qualquer"))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
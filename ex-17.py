print("exercício 19")
print("digite o primeiro valor:")
valor1 = float(input())
print("digite o segundo valor:")
valor2 = float(input())
print("digite o terceiro valor:")
valor3 = float(input())
if valor1 > valor2 > valor3:
    print("o primeiro valor é maior!")
if valor2 > valor1 > valor3:
    print("o segundo valor é maior!")
if valor3 > valor2 > valor1:
    print("o terceiro valor é maior!")

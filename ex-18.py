print("exercício 20")
print("digite um valor:")
valor1 = float(input())
print("digite o segundo valor:")
valor2 = float(input())
print("digite o terceiro valor:")
valor3 = float(input())
valores = [valor1,valor2,valor3]
valores.sort(reverse=True)
soma = valores[0] + valores[1]
print("a soma dos dois maiores valores é:")
print(soma)

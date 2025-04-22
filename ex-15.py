print("exercício 17")
print("qual sua idade?")
valor1 = int(input())
if valor1 < 12:
    print("é criança")
elif 12 <= valor1 <=17:
    print("é adolescente")
elif 18 <= valor1 <=59:
        print("é adulto")
elif valor1 >= 60:
    print("é idoso")

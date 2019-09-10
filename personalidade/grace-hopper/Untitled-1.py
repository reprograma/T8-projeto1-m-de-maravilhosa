c=1
fat=1
soma=1
n = int(input("Digite um número: "))
while (n>=c):
    fat = fat*c
    print(f'1/{fat}')
    c = c + 1
    soma = soma + 1/fat
print(soma)


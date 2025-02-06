qtde = 0 
while True:
    n = int(input("Digite um número: "))
    if n == 0: 
        break
    if n % 2 == 0:
        qtde += 1
print(f"Você entrou com {qtde} números pares.")



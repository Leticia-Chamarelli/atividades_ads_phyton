temperaturas = []
while True:
    t = int(input("Digite a temperatura: "))
    if t == 0:
        break
    temperaturas.append(t)
tamanho = len(temperaturas)
soma = 0
for t in temperaturas:
    soma += t
media = soma / tamanho
print(f"A média é: {media}.")
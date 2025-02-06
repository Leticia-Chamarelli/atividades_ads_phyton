linhas = 2
colunas = 2
matriz = []
for l in range(linhas):
    linha_aloc = [0] * colunas
    matriz.append(linha_aloc)
for l in range(linhas):
    for c in range(colunas):
        valor = int(input("Digite um valor: "))
        matriz[l][c] = valor
print(matriz)
for l in range(linhas):
    for c in range(colunas):
        print(matriz[l][c], end="")
        print()
        
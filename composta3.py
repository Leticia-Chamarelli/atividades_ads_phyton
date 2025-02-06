linhas = 2
colunas = 2
matriz = []
for l in range(linhas):
    linha_aloc = [0] * colunas
    matriz.append(linha_aloc)
for l in range(linhas):
    for c in range(colunas):
        print(f"Linha: {l}, Coluna: {c}")
        
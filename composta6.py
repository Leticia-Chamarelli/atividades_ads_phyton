matriz = [ [0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ] ]
somas = [0, 0, 0 ]
for l in range(3):
    for c in range(3):
        valor = int(input("Digite um valor: "))
        matriz[l][c] = valor
for c in range(3):
    s = 0
    for l in range(3):
        s += matriz[l][c]
    somas[c] = s
print(somas)
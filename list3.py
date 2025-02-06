lista = [40, 20, 60, 10]
valor = int(input("Qual número quer buscar? "))
achou = valor in lista
if achou: 
    print("Valor encontrado")
else: 
    print("Valor não encontrado")
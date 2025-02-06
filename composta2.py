arroz = ["arroz", 5, 8.5]
feijao = ["feijao", 1, 12.40]

compras = [arroz, feijao]
for item in compras:
   for x in item:
      print(x, end="")
      print()

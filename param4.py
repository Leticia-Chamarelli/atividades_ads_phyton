def triangulo(linhas=5, carac="#"):
    for l in range(1, linhas+1):
        for c in range(0, l):
            print(carac, end="")
        print()
triangulo()
triangulo(3, "@")
triangulo(2)
triangulo(linhas=3, carac="%")
triangulo(carac="*", linhas=2)
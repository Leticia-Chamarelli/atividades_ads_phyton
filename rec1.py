def fatorial(n):
    if n<=1:
        print(f"{n}! = 1")
        return 1
    else:
        print(f"{n}! = {n} x ({n-1}!)")
        aux = fatorial(n-1)
        print(f"{n}! = {n} x ({aux})")
        return n * aux
x = fatorial(4)
print(f"fatorial de quatro é: {x}")
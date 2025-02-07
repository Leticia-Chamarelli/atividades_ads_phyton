a = 10
b = 20
def calculo():
    global a
    a = 100
    b = 200
print(f"Valores - a={a}, b={b}")
calculo()
print(f"Valores - a={a}, b={b}")
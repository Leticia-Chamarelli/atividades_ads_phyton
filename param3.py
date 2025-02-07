import math
def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        x1 = None
        x2 = None
    elif delta == 0:
        x1 = -b / (2*a)
        x2 = None
    else: 
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
    return (x1, x2)
a = int(input("Entre com a: "))
b = int(input("Entre com b: "))
c = int(input("Entre com c: "))
(r1, r2) = bhaskara(a, b, c)
print(f"As raízes são: x1= {r1}, x2= {r2}")
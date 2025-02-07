def fibonacci(n):
    if n<=1:
        return n
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
    
f7 = fibonacci(7)
print(f"Fibo(7)={f7}")
for x in range(10):
    f = fibonacci(x)
    print(f"Fibo({x}={f})", end=", ")
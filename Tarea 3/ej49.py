# Ejercicio 49: Calcular n términos de la serie Fibonacci

# Función para calcular la serie de Fibonacci
def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Solicitar al usuario el número de términos
n = int(input("Ingrese el número de términos de la serie Fibonacci: "))
# Calcular la serie de Fibonacci
fib_series = fibonacci(n)
# Mostrar la serie de Fibonacci
print(f"Serie de Fibonacci para {n} términos: {fib_series}")

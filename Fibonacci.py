def fibonacci(numero):
    a, b = 0, 1
    sequencia = [0, 1]

    while b <= numero:
        if b == numero:
            return f"O numero {numero} pertence a sequencia de Fibonacci: {sequencia}"
        a, b = b, a + b
        sequencia.append(b)

    return f"O numero {numero} nao pertence a sequencia de Fibonacci: {sequencia}"

numero = int(input("Digite um numero: "))
resultado = fibonacci(numero)
print(resultado)
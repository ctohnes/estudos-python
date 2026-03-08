def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Não é possível dividir por zero")
        return None
    return a / b

operacoes = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir
}

calcular = input("Deseja usar a calculadora? \nDigite sim ou não: ").strip().lower()

while calcular == "sim":

    numero1 = pedir_numero("Digite o primeiro número: ")
    numero2 = pedir_numero("Digite o segundo número: ")

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao in operacoes:
        resultado = operacoes[operacao](numero1, numero2)

        if resultado is not None:
            print(f"Resultado: {resultado}")

    else:
        print("Operação inválida")

    calcular = input("Deseja continuar? \nDigite sim ou não: ").strip().lower()


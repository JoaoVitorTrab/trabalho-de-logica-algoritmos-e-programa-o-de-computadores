saida = ""
def adicao(q,w):
    return q+w
def subtracao(q,w):
    return q-w
def multiplicacao(q,w):
    return q*w
def divisao(q,w):
    if w == 0:
        return "não é possível realizar a divisão por 0"
    return q/w
def calculadora(n1,n2,O1):
    if O1 in ("+"):
        resultado = adicao(n1,n2)
    elif O1 in ("-"):
        resultado = subtracao(n1,n2)
    elif O1 in ("*"):
        resultado = multiplicacao(n1,n2)
    elif O1 in ("/"):
        resultado = divisao(n1,n2)
    else:
        resultado = "Operação inválida"
    return resultado

while saida.lower() != "n":
    try:
        n1 = float(input("digite o primeiro número: "))
        O1 = input("Digite a operação desejada (+, -, * , /): ")
        n2 = float(input("digite o segundo número: "))
        resultado = calculadora(n1,n2,O1)

        print("Resultado da operação: ",resultado)
    except ValueError:
        print("Por favor, insira valores válidos para os números")
    saida = input("Deseja continuar? Digita S para sim ou N para não").lower()

print("Programa encerrado")